/**
 * The weekly digest: one new issue each Monday (a new issue notifies; that
 * is the point), and last week's is closed in its favour. It reports and
 * proposes; it never changes anything in the tracked repositories.
 */
import type { Config } from "./config.ts";
import type { GitHub } from "./github.ts";
import { ensureLabels } from "./notify.ts";
import { SIGNALS, SIGNAL_LABEL, type RepoStatus, type StatusReport, type WorkItem } from "./types.ts";

export const DIGEST_LABEL = "weekly-digest";
/** Items listed per digest section; the rest are counted and linked. */
export const SECTION_CAP = 40;
/** Stay well under GitHub's 65,536-character issue body limit. */
export const BODY_LIMIT = 60_000;
const DAY = 86_400_000;

/** Monday of the ISO week containing `d`, as YYYY-MM-DD (UTC). */
export function weekStart(d: Date): string {
  const t = new Date(Date.UTC(d.getUTCFullYear(), d.getUTCMonth(), d.getUTCDate()));
  t.setUTCDate(t.getUTCDate() - ((t.getUTCDay() + 6) % 7));
  return t.toISOString().slice(0, 10);
}

/** Who is triage lead for the week containing `d`. */
export function leadFor(cfg: Config, d: Date): string {
  const order = cfg.rota.order;
  if (!cfg.rota.start) return order[0];
  const weeks = Math.floor((Date.parse(weekStart(d)) - Date.parse(weekStart(new Date(cfg.rota.start)))) / (7 * DAY));
  return order[((weeks % order.length) + order.length) % order.length];
}

const ageDays = (iso: string, now: Date) => Math.floor((now.getTime() - Date.parse(iso)) / DAY);
const link = (r: RepoStatus, i: WorkItem) => `[${r.repo}#${i.number}](${i.url}) ${i.title.replace(/[\r\n|]+/g, " ").slice(0, 90)}`;

export function digestBody(report: StatusReport, cfg: Config, now: Date, keepalive?: { lastCommitAt?: string }): string {
  const repos = report.repos.filter((r) => !r.archived);
  const t = cfg.thresholds;
  const lines: string[] = [];
  const lead = leadFor(cfg, now);
  // GitHub caps an issue body at 65,536 characters, and the first digests
  // (before anything carries a P0-P3 label) list hundreds of items.
  const dashboard = `https://${cfg.alertsRepo.split("/")[0].toLowerCase()}.github.io/${cfg.alertsRepo.split("/")[1]}/dashboard/`;
  const section = (title: string, rows: string[], empty = "None.") => {
    const shown = rows.slice(0, SECTION_CAP).map((r) => `- [ ] ${r}`);
    if (rows.length > SECTION_CAP) shown.push(`- ...and ${rows.length - SECTION_CAP} more on the [dashboard](${dashboard}).`);
    lines.push(`### ${title} (${rows.length})`, "", ...(rows.length ? shown : [empty]), "");
  };

  lines.push(
    `Triage lead this week: **@${lead}**. cc ${cfg.maintainers.filter((m) => m !== lead).map((m) => `@${m}`).join(" ")}`,
    "",
    `Snapshot of ${repos.length} active \`${cfg.prefix}*\` repositories, checked ${report.checkedAt}. ` +
      `Tick items as you triage them. Dashboard: ${dashboard}`,
    "",
  );

  const broken: string[] = [];
  for (const r of repos) {
    for (const s of SIGNALS) {
      const sig = r.signals[s];
      if (sig.verdict === "red" || sig.verdict === "unknown" || sig.verdict === "stale" || sig.verdict === "superseded") {
        broken.push(`**${sig.verdict}** ${r.repo}: ${SIGNAL_LABEL[s]}, ${sig.detail}${sig.url ? ` ([evidence](${sig.url}))` : ""}`);
      }
    }
  }
  const order = ["**red**", "**unknown**", "**superseded**", "**stale**"];
  broken.sort((a, b) => order.findIndex((o) => a.startsWith(o)) - order.findIndex((o) => b.startsWith(o)));
  section("Builds not green", broken);

  const week = (i: WorkItem) => ageDays(i.createdAt, now) < 7;
  section("New this week", repos.flatMap((r) => r.items.filter(week).map((i) => `${i.kind === "pr" ? "PR" : "Issue"} ${link(r, i)}`)));
  section(
    "Untriaged (no P0-P3 label)",
    repos.flatMap((r) => r.items.filter((i) => !i.triaged).map((i) => `${link(r, i)} (${ageDays(i.createdAt, now)}d)`)),
  );
  section(
    `PRs with no review after ${t.prReviewDays} days`,
    repos.flatMap((r) =>
      r.items
        .filter((i) => i.kind === "pr" && i.responded === false && ageDays(i.createdAt, now) >= t.prReviewDays)
        .map((i) => `${link(r, i)} (${ageDays(i.createdAt, now)}d)`),
    ),
  );
  section(
    `Issues with no maintainer reply after ${t.issueResponseDays} days`,
    repos.flatMap((r) =>
      r.items
        .filter((i) => i.kind === "issue" && i.responded === false && ageDays(i.createdAt, now) >= t.issueResponseDays)
        .map((i) => `${link(r, i)} by @${i.author} (${ageDays(i.createdAt, now)}d)`),
    ),
  );

  const cutoff = now.getTime() - t.archiveCandidateMonths * 30.44 * DAY;
  const candidates = repos
    .filter((r) => Date.parse(r.pushedAt) < cutoff)
    .sort((a, b) => Date.parse(a.pushedAt) - Date.parse(b.pushedAt))
    .map((r) => `${r.repo}: last push ${r.pushedAt.slice(0, 10)}, ${(r.sizeKb / 1024).toFixed(1)} MB, ${r.openIssues} open issues, ${r.openPrs} open PRs`);
  lines.push(
    `### Archive candidates: no push for ${t.archiveCandidateMonths}+ months (${candidates.length})`,
    "",
    "For information only. Nothing is archived automatically; archiving is a decision for the maintainers.",
    "",
    ...(candidates.length ? candidates.map((c) => `- ${c}`) : ["None."]),
    "",
  );

  if (keepalive?.lastCommitAt && ageDays(keepalive.lastCommitAt, now) >= t.keepaliveWarnDays) {
    lines.push(
      `> **Warning:** ${cfg.alertsRepo} has had no commit on its default branch for ${ageDays(keepalive.lastCommitAt, now)} days. ` +
        "GitHub disables scheduled workflows in public repositories after 60 days without activity, which would stop this digest and the daily check.",
      "",
    );
  }
  const unreadable = report.repos.filter((r) => r.errors.length);
  if (unreadable.length) {
    lines.push(`> Could not fully read: ${unreadable.map((r) => r.repo).join(", ")}. Treat those rows as unknown, not as clean.`, "");
  }
  const body = lines.join("\n");
  return body.length <= BODY_LIMIT ? body : `${body.slice(0, BODY_LIMIT)}\n\n_Truncated: see the [dashboard](${dashboard}) for the rest._`;
}

export async function publishDigest(gh: GitHub, cfg: Config, report: StatusReport, now: Date, log = console.log) {
  const repo = cfg.alertsRepo;
  await ensureLabels(gh, repo, [{ name: DIGEST_LABEL, color: "0e8a16", description: "Weekly smart-* repository digest" }]);
  const meta = await gh.get<{ default_branch: string }>(`/repos/${repo}`);
  const head = await gh.get<{ commit: { commit: { committer: { date: string } } } }>(`/repos/${repo}/branches/${meta.default_branch}`);
  const previous = await gh.list<{ number: number }>(`/repos/${repo}/issues?state=open&labels=${DIGEST_LABEL}&per_page=100`, 2);
  const issue = {
    title: `Weekly digest: week of ${weekStart(now)}`,
    body: digestBody(report, cfg, now, { lastCommitAt: head.commit.commit.committer.date }),
    labels: [DIGEST_LABEL],
  };
  let created: { number: number };
  try {
    created = await gh.send("POST", `/repos/${repo}/issues`, { ...issue, assignees: [leadFor(cfg, now)] });
  } catch (e) {
    if ((e as { status?: number }).status !== 422) throw e; // lead cannot be assigned here; the @mention still notifies
    created = await gh.send("POST", `/repos/${repo}/issues`, issue);
  }
  log(`created digest #${created.number}`);
  for (const p of previous) {
    await gh.send("POST", `/repos/${repo}/issues/${p.number}/comments`, { body: `Superseded by #${created.number}.` });
    await gh.send("PATCH", `/repos/${repo}/issues/${p.number}`, { state: "closed", state_reason: "completed" });
    log(`closed previous digest #${p.number}`);
  }
}
