/**
 * Turn GitHub Actions run history into dashboard verdicts.
 *
 * The classification itself is cat-harness-tools' `assess` and `pagesHealth`
 * (pinned in pin.json, fetched into vendor/). This file only maps their
 * output onto the five verdicts and writes the one line a person reads.
 */
import {
  assess,
  pagesHealth,
  type AssessOptions,
  type RunSummary,
  type WorkflowHealth,
} from "../vendor/ci-health.ts";
import type { Signal } from "./types.ts";

export type { RunSummary };

/** Same cut-off ci-health renders as "may be stale". */
export const STALE_DAYS = 7;

const day = (iso?: string) => (iso ? iso.slice(0, 10) : "?");

export function fromHealth(h: WorkflowHealth | undefined): Signal {
  if (!h) return { verdict: "unknown", detail: "no classification returned" };
  const base = { url: h.latestUrl, at: h.lastRun };
  const unsettled = h.newestUnsettled ? " (newest run still in flight or cancelled; verdict is from the one before)" : "";
  switch (h.health) {
    case "green":
      return { ...base, verdict: "green", detail: `passing, last run ${day(h.lastRun)}${unsettled}` };
    case "red": {
      const n = h.consecutiveFailures;
      const since = h.lastSuccess ? `last green ${day(h.lastSuccess)}` : "no green run in the window";
      if ((h.daysSinceLastRun ?? 0) >= STALE_DAYS) {
        return {
          ...base,
          verdict: "stale",
          cause: h.failingSha,
          detail: `last run failed, but it has not run for ${h.daysSinceLastRun} days (${since}); may be stale`,
        };
      }
      return {
        ...base,
        verdict: "red",
        cause: h.failingSha,
        detail: `${n} failing run${n === 1 ? "" : "s"} in a row, ${since}${unsettled}`,
      };
    }
    case "superseded":
      return {
        ...base,
        verdict: "superseded",
        cause: h.failingSha,
        detail: `last run failed, but the workflow file changed on ${day(h.supersededBy)}; not known to be fixed`,
      };
    case "running":
      return { ...base, verdict: "unknown", detail: "runs are in progress; nothing has settled yet" };
    case "no-runs":
      return { verdict: "none", detail: "no run on the default branch in the recent window" };
  }
}

/**
 * Verdict for one workflow file, from that repository's recent runs.
 * `runs` are newest first, as the API returns them.
 */
export function workflowSignal(
  runs: RunSummary[],
  path: string,
  opts: Omit<AssessOptions, "knownWorkflows"> & { name?: string } = {},
): Signal {
  // The question is about the FILE, so its runs are one stream. ci-health
  // groups by run name, and a renamed workflow (or one whose YAML once failed
  // to parse, so its runs were named by path) would otherwise leave an old
  // name's failures standing as a separate, permanently red row.
  const name = opts.name ?? path;
  const mine = runs.filter((r) => r.path === path || r.path?.startsWith(`${path}@`)).map((r) => ({ ...r, name }));
  const rows = assess(mine, { ...opts, knownWorkflows: [{ path, name }] });
  return fromHealth(rows.find((r) => r.workflow === name) ?? rows[0]);
}

/** Verdict for GitHub Pages, from the runs on the publish branch. */
export function pagesSignal(runs: RunSummary[], now = new Date()): Signal {
  const p = pagesHealth(runs);
  if (p.total === 0) return { verdict: "none", detail: "no Pages deployments in the recent window" };
  const s = p.newestSettled;
  if (!s) return { verdict: "unknown", url: p.latest?.html_url, detail: "deployments in progress; none settled" };
  const ageDays = Math.floor((now.getTime() - new Date(s.created_at).getTime()) / 86_400_000);
  const base = { url: s.html_url, at: s.created_at };
  if (s.conclusion === "success") return { ...base, verdict: "green", detail: `deployed ${day(s.created_at)}` };
  if (s.conclusion === "cancelled") {
    return {
      ...base,
      verdict: "stale",
      detail: `newest settled deployment was cancelled; the site is as of ${day(p.lastSuccessAt)}`,
    };
  }
  const detail = `deployment failed ${day(s.created_at)}; site is as of ${day(p.lastSuccessAt)}`;
  if (ageDays >= STALE_DAYS) return { ...base, verdict: "stale", cause: s.head_sha, detail: `${detail}; may be stale` };
  return { ...base, verdict: "red", cause: s.head_sha, detail };
}
