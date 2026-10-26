/**
 * The FHIR IG build happens on build.fhir.org, not in GitHub Actions: the
 * `fhirbuild.yml` workflow only POSTs a trigger, so its green tick says
 * nothing about whether the IG built. Read the outcome from build.fhir.org
 * itself, fresh every run, and cache nothing (an external status that was
 * right when stored is wrong from then on).
 *
 *   https://build.fhir.org/ig/qas.json                        last successful build per repo/branch
 *   https://build.fhir.org/ig/<org>/<repo>/branches/<b>/failure/build.log   present when the last build failed
 */
import type { Signal } from "./types.ts";

export const FHIR_BUILD = "https://build.fhir.org/ig";

export interface QaEntry {
  repo?: string;
  url?: string;
  date?: string;
  dateISO8601?: string;
  errs?: number;
  warnings?: number;
  hints?: number;
}

/** `repo` in qas.json reads `<org>/<repo>/branches/<branch>/qa.json`. */
export function indexQas(entries: QaEntry[]): Map<string, QaEntry> {
  const out = new Map<string, QaEntry>();
  for (const e of entries) {
    const m = /^([^/]+\/[^/]+)\/branches\/(.+)\/qa\.json$/.exec(e.repo ?? "");
    if (m) out.set(`${m[1]}#${m[2]}`.toLowerCase(), e);
  }
  return out;
}

export interface FailureLog {
  /** true = present, false = absent (HTTP 404), undefined = could not tell. */
  present: boolean | undefined;
  at?: string;
}

export async function failureLog(fullName: string, branch: string): Promise<FailureLog> {
  const url = `${FHIR_BUILD}/${fullName}/branches/${branch}/failure/build.log`;
  try {
    const res = await fetch(url, { method: "HEAD" });
    if (res.status === 404) return { present: false };
    if (!res.ok) return { present: undefined };
    const lm = res.headers.get("last-modified");
    return { present: true, at: lm ? new Date(lm).toISOString() : undefined };
  } catch {
    return { present: undefined };
  }
}

const day = (iso?: string) => (iso ? iso.slice(0, 10) : "?");

/** Grace between a push and the build bot picking it up. */
export const BUILD_GRACE_HOURS = 6;

export function fhirSignal(input: {
  fullName: string;
  branch: string;
  qa: QaEntry | undefined;
  /** undefined when qas.json itself could not be read. */
  qasRead: boolean;
  failure: FailureLog;
  /** ISO time of the newest commit on the branch, when known. */
  headCommitAt?: string;
}): Signal {
  const { fullName, branch, qa, failure } = input;
  const igUrl = `${FHIR_BUILD}/${fullName}/branches/${branch}/`;
  const logUrl = `${igUrl}failure/build.log`;
  if (!input.qasRead || failure.present === undefined) {
    return { verdict: "unknown", url: igUrl, detail: "build.fhir.org could not be read" };
  }
  const builtMs = qa ? Date.parse(qa.dateISO8601 ?? qa.date ?? "") : NaN;
  const builtAt = Number.isNaN(builtMs) ? undefined : new Date(builtMs).toISOString();
  const failedMs = failure.at ? Date.parse(failure.at) : NaN;

  if (failure.present && (!qa || Number.isNaN(builtMs) || Number.isNaN(failedMs) || failedMs > builtMs)) {
    return {
      verdict: "red",
      url: logUrl,
      at: failure.at,
      cause: failure.at ?? "failure-log",
      detail: `last build failed${failure.at ? ` (${day(failure.at)})` : ""}${qa ? `; last success ${day(builtAt)}` : ""}`,
    };
  }
  if (!qa || Number.isNaN(builtMs)) {
    return { verdict: "unknown", url: igUrl, detail: "no build of this branch found on build.fhir.org" };
  }
  const qaLine = `QA ${qa.errs ?? "?"} errors, ${qa.warnings ?? "?"} warnings`;
  const headMs = input.headCommitAt ? Date.parse(input.headCommitAt) : NaN;
  if (!Number.isNaN(headMs) && headMs - builtMs > BUILD_GRACE_HOURS * 3_600_000) {
    return {
      verdict: "stale",
      url: igUrl,
      at: builtAt,
      detail: `last successful build ${day(builtAt)} predates the latest commit (${day(input.headCommitAt)}); ${qaLine}`,
    };
  }
  return { verdict: "green", url: igUrl, at: builtAt, detail: `built ${day(builtAt)}; ${qaLine}` };
}
