import { expect, test } from "bun:test";
import { parseConfig } from "../src/config.ts";
import type { GitHub } from "../src/github.ts";
import { execute, type Action } from "../src/notify.ts";
import type { NotifyState } from "../src/types.ts";

function fakeGitHub() {
  const calls: Array<[string, string, unknown]> = [];
  const gh: GitHub = {
    calls: 0,
    async get<T>() { return {} as T; },
    async list<T>() { return [] as T[]; },
    async send<T>(method: string, path: string, body: unknown) {
      calls.push([method, path, body]);
      if (path.endsWith("/labels")) throw Object.assign(new Error("exists"), { status: 422 });
      return { number: 42 } as T;
    },
  };
  return { gh, calls };
}

test("execute records created issue numbers and clears closed ones", async () => {
  const cfg = parseConfig("maintainers: [ritikarawlani, litlfred]\n");
  const { gh, calls } = fakeGitHub();
  const next: NotifyState = {
    schema: "smart-repo-health/state/v1",
    updatedAt: "x",
    signals: { "smart-a:ci": { verdict: "red", since: "x" }, "smart-b:ci": { verdict: "green", since: "x", issue: 7 } },
  };
  const actions: Action[] = [
    { type: "create", key: "smart-a:ci", title: "t", body: "b", labels: ["build-broken", "P0"] },
    { type: "close", key: "smart-b:ci", issue: 7, body: "recovered" },
  ];
  await execute(gh, cfg, actions, next, () => {});
  expect(next.signals["smart-a:ci"].issue).toBe(42);
  expect(next.signals["smart-b:ci"].issue).toBeUndefined();
  const create = calls.find(([m, p]) => m === "POST" && p.endsWith("/issues"));
  expect(create?.[1]).toBe("/repos/WorldHealthOrganization/smart-ig-starter-kit/issues");
  expect((create?.[2] as { assignees: string[] }).assignees).toEqual(["ritikarawlani", "litlfred"]);
  expect(calls.some(([m, p, b]) => m === "PATCH" && p.endsWith("/issues/7") && (b as { state: string }).state === "closed")).toBe(true);
});
