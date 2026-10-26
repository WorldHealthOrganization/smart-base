import { describe, expect, test } from "bun:test";
import { parseConfig } from "../src/config.ts";
import { digestBody, leadFor, weekStart } from "../src/digest.ts";
import type { StatusReport } from "../src/types.ts";

const cfg = parseConfig("maintainers: [ritikarawlani, litlfred]\nrota:\n  start: 2026-10-26\n");

describe("rota", () => {
  test("weeks start on Monday", () => expect(weekStart(new Date("2026-10-29T12:00:00Z"))).toBe("2026-10-26"));
  test("the lead rotates weekly through the maintainers", () => {
    expect(leadFor(cfg, new Date("2026-10-26T06:17:00Z"))).toBe("ritikarawlani");
    expect(leadFor(cfg, new Date("2026-11-02T06:17:00Z"))).toBe("litlfred");
    expect(leadFor(cfg, new Date("2026-11-09T06:17:00Z"))).toBe("ritikarawlani");
    expect(leadFor(cfg, new Date("2026-10-19T06:17:00Z"))).toBe("litlfred");
  });
});

describe("digestBody", () => {
  const now = new Date("2026-10-26T06:17:00Z");
  const report: StatusReport = {
    schema: "smart-repo-health/status/v1",
    checkedAt: now.toISOString(),
    org: "WorldHealthOrganization",
    undetermined: false,
    repos: [
      {
        repo: "smart-x",
        url: "u",
        archived: false,
        defaultBranch: "main",
        pushedAt: "2026-10-20T00:00:00Z",
        sizeKb: 2048,
        signals: {
          ci: { verdict: "red", detail: "2 failing runs in a row", url: "https://run" },
          fhir: { verdict: "green", detail: "ok" },
          release: { verdict: "none", detail: "" },
          pages: { verdict: "unknown", detail: "in progress" },
        },
        openIssues: 2,
        openPrs: 1,
        untriaged: 2,
        errors: [],
        items: [
          { number: 1, title: "New thing", url: "https://i/1", kind: "issue", author: "someone", createdAt: "2026-10-24T00:00:00Z", labels: [], triaged: false, responded: false },
          { number: 2, title: "Old question", url: "https://i/2", kind: "issue", author: "someone", createdAt: "2026-09-01T00:00:00Z", labels: ["P2"], triaged: true, responded: false },
          { number: 3, title: "Waiting PR", url: "https://i/3", kind: "pr", author: "dev", createdAt: "2026-10-10T00:00:00Z", labels: [], triaged: false, responded: false },
        ],
      },
      {
        repo: "smart-old",
        url: "u",
        archived: false,
        defaultBranch: "master",
        pushedAt: "2020-01-06T00:00:00Z",
        sizeKb: 5120,
        signals: { ci: { verdict: "none", detail: "" }, fhir: { verdict: "none", detail: "" }, release: { verdict: "none", detail: "" }, pages: { verdict: "none", detail: "" } },
        openIssues: 0,
        openPrs: 0,
        untriaged: 0,
        errors: [],
        items: [],
      },
    ],
  };
  const body = digestBody(report, cfg, now, { lastCommitAt: "2026-08-01T00:00:00Z" });

  test("names this week's lead and mentions the others", () => {
    expect(body).toContain("Triage lead this week: **@ritikarawlani**. cc @litlfred");
  });
  test("lists red before unknown, and leaves green out", () => {
    expect(body.indexOf("**red** smart-x")).toBeLessThan(body.indexOf("**unknown** smart-x"));
    expect(body).not.toContain("FHIR IG build (build.fhir.org), ok");
  });
  test("collects new, untriaged, unreviewed and unanswered items", () => {
    expect(body).toContain("### New this week (1)");
    expect(body).toContain("### Untriaged (no P0-P3 label) (2)");
    expect(body).toContain("### PRs with no review after 7 days (1)");
    expect(body).toContain("### Issues with no maintainer reply after 14 days (1)");
  });
  test("reports archive candidates without acting on them", () => {
    expect(body).toContain("smart-old: last push 2020-01-06, 5.0 MB");
    expect(body).toContain("Nothing is archived automatically");
  });
  test("warns before GitHub disables the schedule", () => {
    expect(body).toContain("disables scheduled workflows");
  });
});

describe("digest size", () => {
  test("long sections are capped and the body stays under GitHub's limit", () => {
    const now = new Date("2026-10-26T06:17:00Z");
    const items = Array.from({ length: 900 }, (_, n) => ({
      number: n, title: "x".repeat(80), url: `https://i/${n}`, kind: "issue" as const, author: "a",
      createdAt: "2026-01-01T00:00:00Z", labels: [], triaged: false, responded: false as const,
    }));
    const none = { verdict: "none" as const, detail: "" };
    const report: StatusReport = {
      schema: "smart-repo-health/status/v1", checkedAt: now.toISOString(), org: "o", undetermined: false,
      repos: [{ repo: "smart-big", url: "u", archived: false, defaultBranch: "main", pushedAt: "2026-10-01T00:00:00Z", sizeKb: 1,
        signals: { ci: none, fhir: none, release: none, pages: none }, openIssues: 900, openPrs: 0, untriaged: 900, errors: [], items }],
    };
    const body = digestBody(report, cfg, now);
    expect(body.length).toBeLessThan(65_536);
    expect(body).toContain("### Untriaged (no P0-P3 label) (900)");
    expect(body).toContain("...and 860 more on the [dashboard]");
  });
});
