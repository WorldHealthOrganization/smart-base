/**
 * Read the state of every tracked repository. Reads only; never writes.
 *
 * About eight requests per repository (plus one per PR older than the review
 * threshold), so the whole org fits comfortably in a workflow GITHUB_TOKEN's
 * 1,000 requests an hour.
 */
import type { Config } from "./config.ts";
import { failureLog, fhirSignal, indexQas, FHIR_BUILD, type QaEntry } from "./fhir.ts";
import type { GitHub } from "./github.ts";
import { pagesSignal, workflowSignal, type RunSummary } from "./signals.ts";
import type { RepoStatus, Signal, StatusReport, WorkItem } from "./types.ts";

interface ApiRepo {
  name: string;
  full_name: string;
  html_url: string;
  fork: boolean;
  archived: boolean;
  default_branch: string;
  pushed_at: string;
  size: number;
}

interface ApiRun {
  name: string;
  status: string;
  conclusion: string | null;
  created_at: string;
  html_url: string;
  path: string;
  head_sha: string;
}

interface ApiIssue {
  number: number;
  title: string;
  html_url: string;
  created_at: string;
  user: { login: string } | null;
  author_association: string;
  labels: Array<{ name: string } | string>;
  pull_request?: unknown;
}

interface ApiComment {
  issue_url: string;
  author_association: string;
}

/** Associations that count as "a maintainer has responded". */
const MAINTAINER = new Set(["OWNER", "MEMBER", "COLLABORATOR"]);
const PRIORITY = /^P[0-3]$/i;
const WF = ".github/workflows/";

const toRun = (r: ApiRun): RunSummary => ({
  name: r.name,
  status: r.status,
  conclusion: r.conclusion,
  created_at: r.created_at,
  html_url: r.html_url,
  path: r.path,
  head_sha: r.head_sha,
});

const unknown = (detail: string): Signal => ({ verdict: "unknown", detail });
const none = (detail: string): Signal => ({ verdict: "none", detail });

export async function listRepos(gh: GitHub, cfg: Config, only?: string[]): Promise<ApiRepo[]> {
  const all = only?.length
    ? await Promise.all(only.map((name) => gh.get<ApiRepo>(`/repos/${cfg.org}/${name}`)))
    : await gh.list<ApiRepo>(`/orgs/${cfg.org}/repos?type=all&per_page=100`, 20);
  return all
    .filter((r) => r.name.startsWith(cfg.prefix) && !r.fork && !cfg.exclude.includes(r.name))
    .sort((a, b) => a.name.localeCompare(b.name));
}

export async function loadQas(): Promise<Map<string, QaEntry> | undefined> {
  try {
    const res = await fetch(`${FHIR_BUILD}/qas.json`);
    if (!res.ok) return undefined;
    return indexQas((await res.json()) as QaEntry[]);
  } catch {
    return undefined;
  }
}

async function attempt<T>(errors: string[], what: string, f: () => Promise<T>): Promise<T | undefined> {
  try {
    return await f();
  } catch (e) {
    errors.push(`${what}: ${(e as Error).message}`);
    return undefined;
  }
}

export async function collectRepo(
  gh: GitHub,
  cfg: Config,
  repo: ApiRepo,
  qas: Map<string, QaEntry> | undefined,
  now = new Date(),
): Promise<RepoStatus> {
  const errors: string[] = [];
  const r = `/repos/${repo.full_name}`;
  const b = repo.default_branch;

  const head = await attempt(errors, "branch", () =>
    gh.get<{ commit: { sha: string; commit: { committer: { date: string } } } }>(`${r}/branches/${encodeURIComponent(b)}`),
  );
  const workflows = await attempt(errors, "workflows", () =>
    gh.list<{ path: string; name: string; state: string }>(`${r}/actions/workflows?per_page=100`, 2),
  );
  const has = (file: string) => workflows?.some((w) => w.path === WF + file);

  // ── CI ────────────────────────────────────────────────────────────────
  let ci: Signal;
  const runs = await attempt(errors, "runs", () =>
    gh.get<{ workflow_runs: ApiRun[] }>(`${r}/actions/runs?branch=${encodeURIComponent(b)}&per_page=100`),
  );
  if (!workflows || !runs) ci = unknown("workflow runs could not be read");
  else {
    const mainRuns = runs.workflow_runs.map(toRun);
    // smart-base runs CI as ci.yml and keeps ghbuild.yml as a reusable workflow;
    // IG repos run ghbuild.yml. Use whichever of the two ran most recently here.
    const newest = (f: string) => mainRuns.find((x) => x.path === WF + f)?.created_at ?? "";
    const file = ["ci.yml", "ghbuild.yml"].filter((f) => has(f)).sort((x, y) => newest(y).localeCompare(newest(x)))[0];
    if (!file) ci = none("no ghbuild.yml or ci.yml workflow");
    else {
      const path = WF + file;
      const opts = { now, headSha: head?.commit.sha };
      ci = workflowSignal(mainRuns, path, opts);
      if (ci.verdict === "red") {
        // Only a red needs to know whether its workflow file changed since.
        const changed = await attempt(errors, "workflow history", () =>
          gh.get<Array<{ commit: { committer: { date: string } } }>>(
            `${r}/commits?path=${encodeURIComponent(path)}&sha=${encodeURIComponent(b)}&per_page=1`,
          ),
        );
        const at = changed?.[0]?.commit.committer.date;
        if (at) ci = workflowSignal(mainRuns, path, { ...opts, workflowChangedAt: () => at });
      }
    }
  }

  // ── Release ───────────────────────────────────────────────────────────
  let release: Signal;
  if (!workflows) release = unknown("workflows could not be read");
  else if (!has("release.yml")) release = none("no release.yml workflow");
  else {
    const rr = await attempt(errors, "release runs", () =>
      gh.get<{ workflow_runs: ApiRun[] }>(`${r}/actions/workflows/release.yml/runs?per_page=20`),
    );
    release = rr ? workflowSignal(rr.workflow_runs.map(toRun), WF + "release.yml", { now }) : unknown("release runs could not be read");
    if (release.verdict === "none") release = none("release.yml has never run");
  }

  // ── Pages ─────────────────────────────────────────────────────────────
  const pr = await attempt(errors, "pages runs", () =>
    gh.get<{ workflow_runs: ApiRun[] }>(`${r}/actions/runs?branch=gh-pages&per_page=50`),
  );
  const pages = pr ? pagesSignal(pr.workflow_runs.map(toRun), now) : unknown("Pages deployments could not be read");

  // ── FHIR (build.fhir.org) ─────────────────────────────────────────────
  let fhir: Signal;
  if (!workflows) fhir = unknown("workflows could not be read");
  else if (!has("fhirbuild.yml")) fhir = none("no fhirbuild.yml workflow");
  else {
    fhir = fhirSignal({
      fullName: repo.full_name,
      branch: b,
      qa: qas?.get(`${repo.full_name}#${b}`.toLowerCase()),
      qasRead: qas !== undefined,
      failure: await failureLog(repo.full_name, b),
      headCommitAt: head?.commit.commit.committer.date,
    });
  }

  // ── Work: issues and PRs ──────────────────────────────────────────────
  const items: WorkItem[] = [];
  const issues = await attempt(errors, "issues", () => gh.list<ApiIssue>(`${r}/issues?state=open&per_page=100`, 5));
  if (issues) {
    const since = new Date(now.getTime() - 90 * 86_400_000).toISOString();
    const comments = await attempt(errors, "comments", () =>
      gh.list<ApiComment>(`${r}/issues/comments?since=${since}&per_page=100`, 5),
    );
    const answered = new Set(
      (comments ?? []).filter((c) => MAINTAINER.has(c.author_association)).map((c) => Number(c.issue_url.split("/").pop())),
    );
    let reviewLookups = 0;
    for (const i of issues) {
      const isPr = i.pull_request !== undefined;
      const labels = i.labels.map((l) => (typeof l === "string" ? l : l.name));
      const ageDays = (now.getTime() - Date.parse(i.created_at)) / 86_400_000;
      let responded: WorkItem["responded"];
      if (MAINTAINER.has(i.author_association) && !isPr) responded = true;
      else if (isPr) {
        if (ageDays < cfg.thresholds.prReviewDays) responded = "unknown";
        else if (reviewLookups++ >= 30) responded = "unknown";
        else {
          const reviews = await attempt(errors, `reviews #${i.number}`, () =>
            gh.get<unknown[]>(`${r}/pulls/${i.number}/reviews?per_page=1`),
          );
          responded = reviews === undefined ? "unknown" : reviews.length > 0;
        }
      } else if (answered.has(i.number)) responded = true;
      else responded = comments === undefined || ageDays > 90 ? "unknown" : false;
      items.push({
        number: i.number,
        title: i.title,
        url: i.html_url,
        kind: isPr ? "pr" : "issue",
        author: i.user?.login ?? "ghost",
        createdAt: i.created_at,
        labels,
        triaged: labels.some((l) => PRIORITY.test(l)),
        responded,
      });
    }
  }
  const untriaged = items.filter((i) => !i.triaged);
  const oldest = untriaged.map((i) => Date.parse(i.createdAt)).sort((a, z) => a - z)[0];

  return {
    repo: repo.name,
    url: repo.html_url,
    archived: repo.archived,
    defaultBranch: b,
    pushedAt: repo.pushed_at,
    sizeKb: repo.size,
    signals: { ci, fhir, release, pages },
    openIssues: items.filter((i) => i.kind === "issue").length,
    openPrs: items.filter((i) => i.kind === "pr").length,
    untriaged: untriaged.length,
    oldestUntriagedDays: oldest ? Math.floor((now.getTime() - oldest) / 86_400_000) : undefined,
    items,
    errors,
  };
}

async function pool<T, R>(xs: T[], n: number, f: (x: T) => Promise<R>): Promise<R[]> {
  const out: R[] = new Array(xs.length);
  let next = 0;
  await Promise.all(
    Array.from({ length: Math.min(n, xs.length) }, async () => {
      while (next < xs.length) {
        const i = next++;
        out[i] = await f(xs[i]);
      }
    }),
  );
  return out;
}

/** `only` restricts the run to named repositories (for testing); default is the whole org. */
export async function collect(gh: GitHub, cfg: Config, now = new Date(), only?: string[]): Promise<StatusReport> {
  const repos = await listRepos(gh, cfg, only); // throws: without the list there is nothing to report
  const qas = await loadQas();
  const statuses = await pool(repos, 4, (repo) => collectRepo(gh, cfg, repo, qas, now));
  return {
    schema: "smart-repo-health/status/v1",
    checkedAt: now.toISOString(),
    org: cfg.org,
    repos: statuses,
    // The watchdog itself could not see: a read failed. That fails the job
    // (a blind watchdog must not look like a quiet one). An `unknown` the
    // sources themselves report, such as runs still in progress, is a
    // dashboard state and not a failure of the check.
    undetermined: qas === undefined || statuses.some((s) => s.errors.length > 0),
  };
}
