# smart-repo-health

Daily health check of every non-fork `smart-*` repository in the WorldHealthOrganization org. It produces three things:

- a **dashboard**: build status, open issues and PRs, and a 12-week trend
- **build-broken alerts**: one issue per failing build, opened and closed on transitions only
- a **weekly digest** issue for the triage lead

The process diagram is [processes/repo-health-watch.bpmn](processes/repo-health-watch.bpmn). The human side is [processes/issue-triage.bpmn](processes/issue-triage.bpmn) and [TRIAGE.md](https://github.com/WorldHealthOrganization/smart-ig-starter-kit/blob/main/TRIAGE.md).

## How it runs

The code here is called as a reusable workflow ([../workflows/repo-health.yml](../workflows/repo-health.yml)). The caller supplies the schedule, the config and its own `GITHUB_TOKEN`; today the caller is [smart-ig-starter-kit](https://github.com/WorldHealthOrganization/smart-ig-starter-kit/blob/main/.github/workflows/repo-health.yml). No secret or GitHub App is needed:

- **Reading:** every `smart-*` repository is public, so the caller's token can read them all. A run makes about 8 requests per repository, well within that token's 1,000 an hour.
- **Writing:** the caller's token writes only to the caller. So alerts and digests open there, alert state and trend history live on its `dashboard-state` branch, and the page is served from its `gh-pages/dashboard/`.

The cost of having no App is that alerts open in the caller, not in the affected repository, and nothing is labelled in the tracked repositories.

## What each build signal reads

| Signal | Source | Verdict logic |
| --- | --- | --- |
| CI build | Default-branch runs of `ci.yml` or `ghbuild.yml`, whichever ran last | [ci-health](#reused-code) `assess`: one stream per workflow file |
| FHIR IG build | `https://build.fhir.org/ig/qas.json` and `…/branches/<b>/failure/build.log` | Failing if the failure log is newer than the last success; stale if the last success predates the newest commit by 6h+ |
| Release build | Runs of `release.yml` | ci-health `assess` |
| Pages deploy | Runs on `gh-pages` (`pages build and deployment`) | ci-health `pagesHealth`; a cancelled newest deploy is stale, never passing |

The verdicts are `green`, `red`, `stale`, `superseded`, `unknown` and `none`. `unknown` is never shown or counted as green. A read failure turns the workflow run red: the dashboard data is still published, and alert issues are left untouched for anything unread.

## Reused code

Build-run classification is not reimplemented. It is [`src/workflow/ci-health.ts`](https://github.com/litlfred/cat-harness-tools/blob/8a27ed3d3e40bb7817eb84e191e598f2809242bc/src/workflow/ci-health.ts) from litlfred/cat-harness-tools (Apache-2.0). It is pinned by commit and sha256 in [pin.json](pin.json) and fetched into `vendor/` by `fetch-pinned.ts`, which refuses a file whose hash differs. To move the pin, change both values and run the tests.

## Local use

```sh
cd .github/repo-health
bun install
bun fetch-pinned.ts
bun test && bun run check
# read-only run against a few repositories (no issues, no state written)
GITHUB_TOKEN=... bun src/main.ts collect --config <config.yml> --state /tmp/state --out /tmp/out \
  --template <path to smart-ig-starter-kit/dashboard/index.html> --repos smart-immunizations,smart-hiv --dry-run
```

## Files

| Path | What |
| --- | --- |
| `src/collect.ts` | Reads every repository (read-only) |
| `src/signals.ts`, `src/fhir.ts` | Verdicts |
| `src/notify.ts` | Transition rules (`plan`, pure) and issue writes (`execute`) |
| `src/digest.ts` | Weekly digest and triage rota |
| `src/main.ts` | Command line used by the workflow |
| `test/` | `bun test`: transitions, verdicts, digest |
| `processes/` | BPMN source of truth |
