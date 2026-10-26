import { expect, test } from "bun:test";
import { collectRepo } from "../src/collect.ts";
import { parseConfig } from "../src/config.ts";
import { GitHubError, type GitHub } from "../src/github.ts";

test("an empty repository (default branch missing) is reported as empty, not as a read failure", async () => {
  const gh: GitHub = {
    calls: 0,
    async get<T>(path: string): Promise<T> {
      if (path.includes("/branches/")) throw new GitHubError("GET branch -> HTTP 404", 404);
      throw new Error(`unexpected ${path}`);
    },
    async list<T>() { return [] as T[]; },
    async send<T>() { return {} as T; },
  };
  const repo = {
    name: "smart-terminologies", full_name: "WorldHealthOrganization/smart-terminologies",
    html_url: "https://github.com/WorldHealthOrganization/smart-terminologies", fork: false, archived: false,
    default_branch: "main", pushed_at: "2023-07-27T02:20:48Z", size: 0,
  };
  const s = await collectRepo(gh, parseConfig("maintainers: [a]\n"), repo, new Map());
  expect(s.errors).toEqual([]);
  expect(s.signals.ci.verdict).toBe("none");
  expect(s.signals.ci.detail).toBe("empty repository (no commits)");
});
