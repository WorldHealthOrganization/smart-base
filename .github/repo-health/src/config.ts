import { readFileSync } from "node:fs";
import { parse } from "yaml";

export interface Config {
  org: string;
  /** Repository name prefix to track. Forks are always excluded. */
  prefix: string;
  /** owner/repo where alert and digest issues are opened. */
  alertsRepo: string;
  maintainers: string[];
  rota: { start: string; order: string[] };
  exclude: string[];
  thresholds: {
    prReviewDays: number;
    issueResponseDays: number;
    archiveCandidateMonths: number;
    keepaliveWarnDays: number;
  };
}

const DEFAULTS: Config = {
  org: "WorldHealthOrganization",
  prefix: "smart-",
  alertsRepo: "WorldHealthOrganization/smart-ig-starter-kit",
  maintainers: [],
  rota: { start: "", order: [] },
  exclude: [],
  thresholds: {
    prReviewDays: 7,
    issueResponseDays: 14,
    archiveCandidateMonths: 24,
    keepaliveWarnDays: 45,
  },
};

export function parseConfig(text: string): Config {
  const raw = (parse(text) ?? {}) as Partial<Config>;
  const cfg: Config = {
    ...DEFAULTS,
    ...raw,
    rota: { ...DEFAULTS.rota, ...(raw.rota ?? {}) },
    thresholds: { ...DEFAULTS.thresholds, ...(raw.thresholds ?? {}) },
  };
  if (cfg.maintainers.length === 0) throw new Error("config: maintainers must name at least one GitHub handle");
  if (!/^[^/]+\/[^/]+$/.test(cfg.alertsRepo)) throw new Error(`config: alertsRepo must be owner/repo, got ${cfg.alertsRepo}`);
  if (cfg.rota.order.length === 0) cfg.rota.order = [...cfg.maintainers];
  return cfg;
}

export function loadConfig(path: string): Config {
  return parseConfig(readFileSync(path, "utf-8"));
}
