import { describe, expect, test } from "bun:test";
import { fhirSignal, indexQas } from "../src/fhir.ts";
import { pagesSignal, workflowSignal, type RunSummary } from "../src/signals.ts";

const NOW = new Date("2026-10-26T06:00:00Z");
const PATH = ".github/workflows/ghbuild.yml";
const run = (conclusion: string | null, created_at: string, extra: Partial<RunSummary> = {}): RunSummary => ({
  name: "GitHub Pages build",
  status: conclusion === null ? "in_progress" : "completed",
  conclusion,
  created_at,
  path: PATH,
  head_sha: `sha-${created_at}`,
  html_url: `https://example/${created_at}`,
  ...extra,
});

describe("workflowSignal (via the pinned ci-health assess)", () => {
  test("latest success is green", () => {
    expect(workflowSignal([run("success", "2026-10-25T00:00:00Z")], PATH, { now: NOW }).verdict).toBe("green");
  });
  test("a recent failure is red, with the failing commit as its cause", () => {
    const s = workflowSignal([run("failure", "2026-10-25T00:00:00Z"), run("success", "2026-10-20T00:00:00Z")], PATH, { now: NOW });
    expect(s.verdict).toBe("red");
    expect(s.cause).toBe("sha-2026-10-25T00:00:00Z");
  });
  test("a failure that has not re-run for a week is stale, not red", () => {
    expect(workflowSignal([run("failure", "2026-10-01T00:00:00Z")], PATH, { now: NOW }).verdict).toBe("stale");
  });
  test("a failure older than the last edit of its workflow file is superseded", () => {
    const s = workflowSignal([run("failure", "2026-10-24T00:00:00Z")], PATH, { now: NOW, workflowChangedAt: () => "2026-10-25T00:00:00Z" });
    expect(s.verdict).toBe("superseded");
  });
  test("other workflows' runs are ignored", () => {
    const s = workflowSignal([run("failure", "2026-10-25T00:00:00Z", { path: ".github/workflows/other.yml" })], PATH, { now: NOW });
    expect(s.verdict).toBe("none");
  });
});

describe("pagesSignal", () => {
  const p = (conclusion: string, at: string): RunSummary => ({ ...run(conclusion, at), name: "pages build and deployment", path: "dynamic/pages/pages-build-deployment" });
  test("no deployments is none", () => expect(pagesSignal([], NOW).verdict).toBe("none"));
  test("newest settled success is green", () => expect(pagesSignal([p("success", "2026-10-25T00:00:00Z")], NOW).verdict).toBe("green"));
  test("a newest settled cancellation is stale (starvation), never green", () =>
    expect(pagesSignal([p("cancelled", "2026-10-25T00:00:00Z"), p("success", "2026-10-20T00:00:00Z")], NOW).verdict).toBe("stale"));
  test("a recent failure is red", () => expect(pagesSignal([p("failure", "2026-10-25T00:00:00Z")], NOW).verdict).toBe("red"));
});

describe("fhirSignal (build.fhir.org)", () => {
  const qas = indexQas([
    { repo: "WorldHealthOrganization/smart-x/branches/main/qa.json", dateISO8601: "2026-10-25T10:00:00Z", errs: 3, warnings: 9 },
  ]);
  const base = { fullName: "WorldHealthOrganization/smart-x", branch: "main", qasRead: true };
  const qa = qas.get("worldhealthorganization/smart-x#main");

  test("qas.json is indexed by repo and branch", () => expect(qa?.errs).toBe(3));
  test("a successful build after the last commit is green, with the QA counts", () => {
    const s = fhirSignal({ ...base, qa, failure: { present: false }, headCommitAt: "2026-10-25T09:00:00Z" });
    expect(s.verdict).toBe("green");
    expect(s.detail).toContain("QA 3 errors");
  });
  test("a failure log newer than the last success is red", () => {
    expect(fhirSignal({ ...base, qa, failure: { present: true, at: "2026-10-26T01:00:00Z" } }).verdict).toBe("red");
  });
  test("a failure log older than the last success is not red", () => {
    expect(fhirSignal({ ...base, qa, failure: { present: true, at: "2026-10-01T01:00:00Z" } }).verdict).toBe("green");
  });
  test("a last success that predates the latest commit is stale", () => {
    expect(fhirSignal({ ...base, qa, failure: { present: false }, headCommitAt: "2026-10-26T05:00:00Z" }).verdict).toBe("stale");
  });
  test("build.fhir.org unreadable is unknown, never green", () => {
    expect(fhirSignal({ ...base, qa, qasRead: false, failure: { present: false } }).verdict).toBe("unknown");
    expect(fhirSignal({ ...base, qa, failure: { present: undefined } }).verdict).toBe("unknown");
  });
});

describe("workflowSignal treats a workflow file as one stream", () => {
  test("old failures under a previous run name do not outlive a newer success", () => {
    const runs = [
      run("success", "2026-10-01T00:00:00Z"),
      run("failure", "2026-03-19T00:00:00Z", { name: PATH }),
      run("failure", "2026-03-18T00:00:00Z", { name: "CI" }),
    ];
    expect(workflowSignal(runs, PATH, { now: NOW }).verdict).toBe("green");
  });
});
