/**
 * smart-repo-health: daily check and weekly digest of the smart-* repositories.
 *
 *   bun src/main.ts collect --config <yml> --state <dir> --out <dir> [--template <html>] [--dry-run]
 *   bun src/main.ts digest  --config <yml> [--dry-run]
 *
 *   --environment staging  label the published data; the page shows a
 *                banner for anything other than production.
 *   --repos a,b  restrict to the named repositories (testing); default is every
 *                non-fork repository in the org whose name starts with the prefix.
 *
 * collect writes <out>/status.json and <out>/trend.json (the dashboard's data)
 * BEFORE any exit path, updates <state>/state.json and <state>/trend.json,
 * and opens, edits or closes build-broken alerts. It exits 1 when part of the
 * org could not be read: a blind watchdog must not look like a quiet one.
 *
 * GITHUB_TOKEN (or GH_TOKEN) is read from the environment. --dry-run makes
 * no GitHub writes and prints what it would do.
 */
import { appendFileSync, copyFileSync, existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { collect } from "./collect.ts";
import { loadConfig } from "./config.ts";
import { digestBody, publishDigest } from "./digest.ts";
import { github } from "./github.ts";
import { execute, findClosedByPerson, plan } from "./notify.ts";
import { SIGNALS, type NotifyState, type StatusReport, type TrendPoint } from "./types.ts";

const [cmd, ...rest] = process.argv.slice(2);
const flag = (name: string) => {
  const i = rest.indexOf(`--${name}`);
  return i === -1 ? undefined : rest[i + 1];
};
const dry = rest.includes("--dry-run");
const configPath = flag("config");
if (!cmd || !["collect", "digest"].includes(cmd) || !configPath) {
  console.error("usage: main.ts collect|digest --config <yml> [--state <dir>] [--out <dir>] [--template <html>] [--dry-run]");
  process.exit(2);
}

const cfg = loadConfig(configPath);
const gh = github(process.env.GITHUB_TOKEN ?? process.env.GH_TOKEN);
const now = new Date();
const readJson = <T>(p: string): T | undefined => (existsSync(p) ? (JSON.parse(readFileSync(p, "utf-8")) as T) : undefined);
const writeJson = (p: string, v: unknown) => writeFileSync(p, `${JSON.stringify(v, null, 1)}\n`);

function summary(report: StatusReport): string {
  const count = (v: string) => report.repos.reduce((n, r) => n + SIGNALS.filter((s) => r.signals[s].verdict === v).length, 0);
  return [
    `### smart-repo-health ${cmd} (${report.checkedAt})`,
    "",
    `${report.repos.length} repositories, ${gh.calls} API calls.`,
    `Signals: ${["green", "red", "stale", "superseded", "unknown", "none"].map((v) => `${v} ${count(v)}`).join(", ")}.`,
    report.undetermined
      ? `**Could not determine everything:** ${report.repos.filter((r) => r.errors.length).map((r) => `${r.repo} (${r.errors[0]})`).join("; ") || "build.fhir.org unreadable"}`
      : "Every repository was read.",
    "",
  ].join("\n");
}

const only = flag("repos")?.split(",").map((r) => r.trim()).filter(Boolean);
const report = await collect(gh, cfg, now, only);
report.environment = flag("environment") ?? "production";

if (cmd === "collect") {
  const out = flag("out") ?? "out";
  const stateDir = flag("state") ?? "state";
  mkdirSync(out, { recursive: true });
  mkdirSync(stateDir, { recursive: true });

  const trend = readJson<TrendPoint[]>(join(stateDir, "trend.json")) ?? [];
  const today = now.toISOString().slice(0, 10);
  const point: TrendPoint = {
    date: today,
    repos: Object.fromEntries(report.repos.map((r) => [r.repo, { issues: r.openIssues, prs: r.openPrs, untriaged: r.untriaged }])),
  };
  const nextTrend = [...trend.filter((p) => p.date !== today), point].sort((a, b) => a.date.localeCompare(b.date));

  // The dashboard's data is written first, whatever happens next.
  writeJson(join(out, "status.json"), report);
  writeJson(join(out, "trend.json"), nextTrend);
  const template = flag("template");
  if (template) copyFileSync(template, join(out, "index.html"));

  const prev = readJson<NotifyState>(join(stateDir, "state.json"));
  const closed = dry || !prev ? new Set<number>() : await findClosedByPerson(gh, cfg, prev);
  const { actions, next } = plan(prev, report, cfg, closed);
  if (!prev) console.log("No previous state: seeding only, no alerts this run.");
  if (dry) {
    for (const a of actions) console.log(`[dry-run] ${a.type} ${a.key}${"issue" in a ? ` #${a.issue}` : ""}${"title" in a ? `: ${a.title}` : ""}`);
  } else {
    await execute(gh, cfg, actions, next);
  }
  writeJson(join(stateDir, "trend.json"), nextTrend);
  if (!dry) writeJson(join(stateDir, "state.json"), next);
  else writeJson(join(stateDir, "state.dry-run.json"), next);
} else if (dry) {
  console.log(digestBody(report, cfg, now));
} else {
  await publishDigest(gh, cfg, report, now);
}

const text = summary(report);
console.log(text);
if (process.env.GITHUB_STEP_SUMMARY) appendFileSync(process.env.GITHUB_STEP_SUMMARY, text);
if (report.undetermined) process.exit(1);
