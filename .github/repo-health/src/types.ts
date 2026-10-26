/**
 * Shapes shared by the collector, the notifier, the digest and the dashboard.
 *
 * Every signal carries one of five verdicts, plus `none` for "this repository
 * has no such build". The rule borrowed from cat-harness-tools' ci-health
 * module applies throughout: "could not check" is `unknown`, and `unknown`
 * is never rendered or counted as green.
 */

export type Verdict = "green" | "red" | "stale" | "superseded" | "unknown" | "none";

export type SignalName = "ci" | "fhir" | "release" | "pages";

export const SIGNALS: readonly SignalName[] = ["ci", "fhir", "release", "pages"];

export const SIGNAL_LABEL: Record<SignalName, string> = {
  ci: "CI build",
  fhir: "FHIR IG build (build.fhir.org)",
  release: "Release build",
  pages: "GitHub Pages deploy",
};

export interface Signal {
  verdict: Verdict;
  /** One line a person can act on. */
  detail: string;
  /** Link to the run, log or page the verdict came from. */
  url?: string;
  /**
   * What the failure is about (the failing run's commit, or log timestamp).
   * A change of cause while still red is what earns a notifying comment.
   */
  cause?: string;
  /** ISO time of the run or build the verdict describes. */
  at?: string;
}

export interface WorkItem {
  number: number;
  title: string;
  url: string;
  kind: "issue" | "pr";
  author: string;
  createdAt: string;
  labels: string[];
  /** Has a P0–P3 label. */
  triaged: boolean;
  /** PR: a review exists. Issue: a maintainer (org member/collaborator) replied, or opened it. */
  responded: boolean | "unknown";
}

export interface RepoStatus {
  repo: string;
  url: string;
  archived: boolean;
  defaultBranch: string;
  pushedAt: string;
  sizeKb: number;
  signals: Record<SignalName, Signal>;
  openIssues: number;
  openPrs: number;
  untriaged: number;
  /** Oldest untriaged item, in whole days. */
  oldestUntriagedDays?: number;
  items: WorkItem[];
  /** Set when part of this repository could not be read. */
  errors: string[];
}

export interface StatusReport {
  schema: "smart-repo-health/status/v1";
  checkedAt: string;
  org: string;
  repos: RepoStatus[];
  /** True when at least one verdict could not be determined. */
  undetermined: boolean;
}

/** What the notifier remembers about one repo × signal between runs. */
export interface SignalState {
  verdict: Verdict;
  since: string;
  cause?: string;
  /** Open tracking issue in the alerts repo, if any. */
  issue?: number;
  /**
   * A person closed the tracking issue while the signal was still red.
   * Respect that: no new issue until the signal has been green again.
   */
  dismissed?: boolean;
}

export interface NotifyState {
  schema: "smart-repo-health/state/v1";
  updatedAt: string;
  signals: Record<string, SignalState>;
}

export interface TrendPoint {
  date: string;
  repos: Record<string, { issues: number; prs: number; untriaged: number }>;
}
