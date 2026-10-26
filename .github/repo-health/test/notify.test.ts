import { describe, expect, test } from "bun:test";
import { parseConfig } from "../src/config.ts";
import { keyOf, MARKER, plan } from "../src/notify.ts";
import type { NotifyState, RepoStatus, Signal, StatusReport, Verdict } from "../src/types.ts";

const cfg = parseConfig("maintainers: [ritikarawlani, litlfred]\n");
const sig = (verdict: Verdict, cause?: string): Signal => ({ verdict, detail: `${verdict} detail`, cause, url: "https://example/run" });
const none = sig("none");

function repo(ci: Signal, extra: Partial<RepoStatus> = {}): RepoStatus {
  return {
    repo: "smart-x",
    url: "https://github.com/WorldHealthOrganization/smart-x",
    archived: false,
    defaultBranch: "main",
    pushedAt: "2026-10-01T00:00:00Z",
    sizeKb: 10,
    signals: { ci, fhir: none, release: none, pages: none },
    openIssues: 0,
    openPrs: 0,
    untriaged: 0,
    items: [],
    errors: [],
    ...extra,
  };
}
const report = (r: RepoStatus, at = "2026-10-26T05:41:00Z"): StatusReport => ({
  schema: "smart-repo-health/status/v1",
  checkedAt: at,
  org: "WorldHealthOrganization",
  repos: [r],
  undetermined: false,
});
const KEY = keyOf("smart-x", "ci");
const state = (s: NotifyState["signals"][string]): NotifyState => ({
  schema: "smart-repo-health/state/v1",
  updatedAt: "2026-10-25T05:41:00Z",
  signals: { [KEY]: s },
});

describe("plan: transitions only", () => {
  test("first run seeds state and opens nothing, even for a red build", () => {
    const { actions, next } = plan(undefined, report(repo(sig("red", "sha1"))), cfg);
    expect(actions).toEqual([]);
    expect(next.signals[KEY].verdict).toBe("red");
  });

  test("green -> red creates exactly one issue, labelled and mentioning the maintainers", () => {
    const { actions } = plan(state({ verdict: "green", since: "2026-10-01" }), report(repo(sig("red", "sha1"))), cfg);
    expect(actions).toHaveLength(1);
    const a = actions[0];
    expect(a.type).toBe("create");
    if (a.type !== "create") return;
    expect(a.title).toBe("🔴 smart-x: CI build failing on main");
    expect(a.labels).toEqual(["build-broken", "P0"]);
    expect(a.body).toContain(MARKER(KEY));
    expect(a.body).toContain("@ritikarawlani @litlfred");
  });

  test("red -> red with the same cause edits silently", () => {
    const { actions } = plan(state({ verdict: "red", since: "2026-10-20T00:00:00Z", cause: "sha1", issue: 7 }), report(repo(sig("red", "sha1"))), cfg);
    expect(actions.map((a) => a.type)).toEqual(["edit"]);
    expect(actions[0].type === "edit" && actions[0].body).toContain("Failing since: 2026-10-20");
  });

  test("red -> red with a new cause edits and adds one comment", () => {
    const { actions } = plan(state({ verdict: "red", since: "2026-10-20", cause: "sha1", issue: 7 }), report(repo(sig("red", "sha2"))), cfg);
    expect(actions.map((a) => a.type)).toEqual(["edit", "comment"]);
  });

  test("red -> green comments and closes", () => {
    const { actions, next } = plan(state({ verdict: "red", since: "2026-10-20", cause: "sha1", issue: 7 }), report(repo(sig("green"))), cfg);
    expect(actions.map((a) => a.type)).toEqual(["close"]);
    expect(next.signals[KEY].verdict).toBe("green");
  });

  test("unknown changes nothing, not even the state", () => {
    const prev = state({ verdict: "red", since: "2026-10-20", cause: "sha1", issue: 7 });
    const { actions, next } = plan(prev, report(repo(sig("unknown"))), cfg);
    expect(actions).toEqual([]);
    expect(next.signals[KEY]).toEqual(prev.signals[KEY]);
  });

  test("stale and superseded never open an issue", () => {
    for (const v of ["stale", "superseded"] as const) {
      const { actions } = plan(state({ verdict: "green", since: "2026-10-01" }), report(repo(sig(v))), cfg);
      expect(actions).toEqual([]);
    }
  });

  test("red -> stale keeps the open issue current, silently", () => {
    const { actions } = plan(state({ verdict: "red", since: "2026-10-01", cause: "sha1", issue: 7 }), report(repo(sig("stale", "sha1"))), cfg);
    expect(actions.map((a) => a.type)).toEqual(["edit"]);
  });

  test("an alert closed by a person while still red is not reopened", () => {
    const prev = state({ verdict: "red", since: "2026-10-20", cause: "sha1", issue: 7 });
    const first = plan(prev, report(repo(sig("red", "sha1"))), cfg, new Set([7]));
    expect(first.actions).toEqual([]);
    expect(first.next.signals[KEY].dismissed).toBe(true);
    // ...until it has been green again.
    const green = plan(first.next, report(repo(sig("green"))), cfg);
    const red = plan(green.next, report(repo(sig("red", "sha3"))), cfg);
    expect(red.actions.map((a) => a.type)).toEqual(["create"]);
  });

  test("archived repositories never alert", () => {
    const { actions } = plan(state({ verdict: "green", since: "2026-10-01" }), report(repo(sig("red", "sha1"), { archived: true })), cfg);
    expect(actions).toEqual([]);
  });

  test("a release failure is also flagged for the publication manager", () => {
    const r = repo(none);
    r.signals.release = sig("red", "sha9");
    const prev: NotifyState = { schema: "smart-repo-health/state/v1", updatedAt: "x", signals: { [keyOf("smart-x", "release")]: { verdict: "green", since: "x" } } };
    const a = plan(prev, report(r), cfg).actions.find((x) => x.type === "create");
    expect(a && a.type === "create" && a.labels).toEqual(["build-broken", "P0", "publication-manager"]);
  });
});
