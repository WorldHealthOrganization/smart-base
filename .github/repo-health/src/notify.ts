/**
 * Build-broken alerts, by transition only. The shape follows cat-harness's
 * ci-health-watch and publish-alert processes:
 *
 *   green -> red        CREATE one tracking issue (the @mentions notify)
 *   red   -> red        EDIT its body in place (an edit does not notify);
 *                       COMMENT only when the failure's cause changed
 *   red   -> green      COMMENT "recovered" and CLOSE
 *   anything -> unknown change nothing (a blind check must not act)
 *   first run           seed state only, so builds already red do not flood
 *
 * A person who closes an alert while the build is still red has decided
 * something: no new issue for that signal until it has been green again.
 *
 * `plan` is pure; `execute` performs it.
 */
import type { Config } from "./config.ts";
import type { GitHub } from "./github.ts";
import {
  SIGNALS,
  SIGNAL_LABEL,
  type NotifyState,
  type RepoStatus,
  type Signal,
  type SignalName,
  type SignalState,
  type StatusReport,
} from "./types.ts";

export type Action =
  | { type: "create"; key: string; title: string; body: string; labels: string[] }
  | { type: "edit"; key: string; issue: number; body: string }
  | { type: "comment"; key: string; issue: number; body: string }
  | { type: "close"; key: string; issue: number; body: string };

export const MARKER = (key: string) => `<!-- smart-repo-health:${key} -->`;
export const ALERT_LABELS = {
  alert: "build-broken",
  p0: "P0",
  release: "publication-manager",
} as const;

export const keyOf = (repo: string, signal: SignalName) => `${repo}:${signal}`;

function alertTitle(r: RepoStatus, s: SignalName) {
  return `🔴 ${r.repo}: ${SIGNAL_LABEL[s]} failing on ${r.defaultBranch}`;
}

export function alertBody(r: RepoStatus, s: SignalName, sig: Signal, cfg: Config, checkedAt: string, since: string) {
  const state =
    sig.verdict === "red"
      ? "**Failing.**"
      : sig.verdict === "green"
        ? "**Recovered.**"
        : `**${sig.verdict}**: not confirmed fixed, so this stays open.`;
  return [
    MARKER(keyOf(r.repo, s)),
    `${state} ${SIGNAL_LABEL[s]} on [\`${r.repo}\`](${r.url}) (\`${r.defaultBranch}\`).`,
    "",
    `- What: ${sig.detail}`,
    sig.url ? `- Evidence: ${sig.url}` : undefined,
    `- Failing since: ${since.slice(0, 10)}`,
    `- Last checked: ${checkedAt}`,
    "",
    s === "release"
      ? "Release failures need a decision from a person: hold the release, or fix forward and publish again."
      : `Triage per [TRIAGE.md](https://github.com/${cfg.alertsRepo}/blob/main/TRIAGE.md): acknowledge today, fix within 2 working days.`,
    "",
    `cc ${cfg.maintainers.map((m) => `@${m}`).join(" ")}`,
    "",
    "_This body is updated in place each day while the problem persists (edits do not notify). It closes itself when the build is green again. Closing it by hand silences this alert until the build has recovered._",
  ]
    .filter((l) => l !== undefined)
    .join("\n");
}

export function plan(
  prev: NotifyState | undefined,
  report: StatusReport,
  cfg: Config,
  closedByPerson: ReadonlySet<number> = new Set(),
): { actions: Action[]; next: NotifyState } {
  const now = report.checkedAt;
  const next: NotifyState = { schema: "smart-repo-health/state/v1", updatedAt: now, signals: { ...(prev?.signals ?? {}) } };
  const actions: Action[] = [];

  for (const r of report.repos) {
    for (const s of SIGNALS) {
      const key = keyOf(r.repo, s);
      const sig = r.signals[s];
      const p: SignalState | undefined = prev?.signals[key];

      if (!prev) {
        next.signals[key] = { verdict: sig.verdict, since: now, cause: sig.cause };
        continue;
      }
      if (sig.verdict === "unknown") continue; // state untouched

      let issue = p?.issue;
      let dismissed = p?.dismissed ?? false;
      if (issue !== undefined && closedByPerson.has(issue)) {
        issue = undefined;
        dismissed = sig.verdict !== "green";
      }
      const since = p && p.verdict === sig.verdict ? p.since : now;
      // A red that has gone stale or superseded is still the same incident.
      const failingSince = p && p.verdict !== "green" && p.verdict !== "none" ? p.since : since;

      if (sig.verdict === "green") {
        if (issue !== undefined) {
          actions.push({
            type: "close",
            key,
            issue,
            body: `Recovered: ${SIGNAL_LABEL[s]} is passing again (${sig.detail})${sig.url ? `, ${sig.url}` : ""}. Closing.`,
          });
        }
        next.signals[key] = { verdict: "green", since };
        continue;
      }

      if (r.archived) {
        next.signals[key] = { verdict: sig.verdict, since, cause: sig.cause, issue, dismissed };
        continue;
      }

      if (sig.verdict === "red") {
        if (issue !== undefined) {
          actions.push({ type: "edit", key, issue, body: alertBody(r, s, sig, cfg, now, failingSince) });
          if (sig.cause && p?.cause && sig.cause !== p.cause) {
            actions.push({
              type: "comment",
              key,
              issue,
              body: `Still failing, with a new failure: ${sig.detail}${sig.url ? `, ${sig.url}` : ""}.`,
            });
          }
        } else if (!dismissed) {
          const labels: string[] = [ALERT_LABELS.alert, ALERT_LABELS.p0];
          if (s === "release") labels.push(ALERT_LABELS.release);
          actions.push({ type: "create", key, title: alertTitle(r, s), body: alertBody(r, s, sig, cfg, now, now), labels });
        }
        next.signals[key] = { verdict: "red", since: failingSince, cause: sig.cause, issue, dismissed };
        continue;
      }

      // stale, superseded, none: never opens anything; keeps an open issue current.
      if (issue !== undefined) actions.push({ type: "edit", key, issue, body: alertBody(r, s, sig, cfg, now, failingSince) });
      next.signals[key] = { verdict: sig.verdict, since: failingSince, cause: sig.cause, issue, dismissed };
    }
  }
  return { actions, next };
}

/** Which tracked alert issues a person has closed since the last run. */
export async function findClosedByPerson(gh: GitHub, cfg: Config, prev: NotifyState | undefined): Promise<Set<number>> {
  const out = new Set<number>();
  for (const st of Object.values(prev?.signals ?? {})) {
    if (st.issue === undefined) continue;
    const i = await gh.get<{ state: string }>(`/repos/${cfg.alertsRepo}/issues/${st.issue}`);
    if (i.state === "closed") out.add(st.issue);
  }
  return out;
}

export async function ensureLabels(gh: GitHub, repo: string, labels: Array<{ name: string; color: string; description: string }>) {
  for (const l of labels) {
    try {
      await gh.send("POST", `/repos/${repo}/labels`, l);
    } catch (e) {
      if ((e as { status?: number }).status !== 422) throw e; // 422 = already exists
    }
  }
}

export async function execute(gh: GitHub, cfg: Config, actions: Action[], next: NotifyState, log = console.log) {
  const repo = cfg.alertsRepo;
  if (actions.length > 0) {
    await ensureLabels(gh, repo, [
      { name: ALERT_LABELS.alert, color: "b60205", description: "A build on a default branch is failing (opened by smart-repo-health)" },
      { name: ALERT_LABELS.p0, color: "b60205", description: "Priority 0: broken build, broken published IG, or release blocker" },
      { name: ALERT_LABELS.release, color: "5319e7", description: "Needs the publication manager: hold the release or fix forward" },
    ]);
  }
  for (const a of actions) {
    if (a.type === "create") {
      let created: { number: number };
      try {
        created = await gh.send("POST", `/repos/${repo}/issues`, { title: a.title, body: a.body, labels: a.labels, assignees: cfg.maintainers });
      } catch (e) {
        if ((e as { status?: number }).status !== 422) throw e;
        created = await gh.send("POST", `/repos/${repo}/issues`, { title: a.title, body: a.body, labels: a.labels });
      }
      next.signals[a.key] = { ...next.signals[a.key], issue: created.number };
      log(`created #${created.number} ${a.title}`);
    } else if (a.type === "edit") {
      await gh.send("PATCH", `/repos/${repo}/issues/${a.issue}`, { body: a.body });
      log(`edited #${a.issue} (${a.key})`);
    } else if (a.type === "comment") {
      await gh.send("POST", `/repos/${repo}/issues/${a.issue}/comments`, { body: a.body });
      log(`commented #${a.issue} (${a.key})`);
    } else {
      await gh.send("POST", `/repos/${repo}/issues/${a.issue}/comments`, { body: a.body });
      await gh.send("PATCH", `/repos/${repo}/issues/${a.issue}`, { state: "closed", state_reason: "completed" });
      next.signals[a.key] = { ...next.signals[a.key], issue: undefined };
      log(`closed #${a.issue} (${a.key})`);
    }
  }
}
