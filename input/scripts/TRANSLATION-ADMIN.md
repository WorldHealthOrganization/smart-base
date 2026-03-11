# Translation Admin Guide

> **Audience:** IG administrators setting up translation services for a WHO DAK Implementation Guide repository.
> **Scope:** Registration, configuration, and day-to-day operation of the multi-service translation workflow.

---

## Table of Contents

1. [Architecture Overview](#1-architecture-overview)
2. [Configuration Parameters Reference](#2-configuration-parameters-reference)
3. [Environment Variables & Secrets Reference](#3-environment-variables--secrets-reference)
4. [Step-by-Step: Connect Each Translation Service](#4-step-by-step-connect-each-translation-service)
   - [4a. Weblate (fully implemented)](#4a-weblate-fully-implemented)
   - [4b. Crowdin (stub — not yet fully implemented)](#4b-crowdin-stub--not-yet-fully-implemented)
   - [4c. Launchpad (stub — not yet fully implemented)](#4c-launchpad-stub--not-yet-fully-implemented)
5. [GitHub Actions Workflow Reference](#5-github-actions-workflow-reference)
6. [Runbook: Common Operations](#6-runbook-common-operations)
7. [Troubleshooting Guide](#7-troubleshooting-guide)
8. [Security Notes](#8-security-notes)

---

## 1. Architecture Overview

The registration workflow spans several Python modules and a GitHub Actions
workflow. Each piece has a single responsibility:

```
sushi-config.yaml          ← primary translation config (authoritative)
dak.json                   ← IG identity + fallback translation config
         │
         ▼
translation_config.py      ← single config reader used by all scripts
         │
         ├─► register_translation_project.py   ← per-IG idempotent registration
         │         called by ▼
         │   register_all_dak_projects.py       ← bulk org-wide discovery + registration
         │
         └─► pull_translations.py              ← multi-service pull orchestrator
                   │
                   ├─► pull_weblate_translations.py    ← Weblate adapter (fully implemented)
                   ├─► pull_launchpad_translations.py  ← Launchpad adapter (stub)
                   └─► pull_crowdin_translations.py    ← Crowdin adapter (stub)

.github/workflows/register_translation_project.yml  ← GitHub Actions entry point
```

### Module Responsibilities

| Module | Purpose |
|--------|---------|
| `translation_config.py` | Single authoritative reader for `sushi-config.yaml#translations` (with `dak.json#translations` fallback). Provides language list, enabled services, project slug derivation, and `.pot` component discovery. |
| `translation_security.py` | Input sanitization (`sanitize_slug`, `sanitize_url`, `sanitize_lang_code`), secret redaction, HTTP safety constants, and guard against secrets leaking through workflow inputs. |
| `register_translation_project.py` | Idempotently creates or verifies a translation project and all its components on every enabled service, for one IG repo. |
| `register_all_dak_projects.py` | Uses the GitHub Code Search API to discover every repo in the org containing `dak.json`, then calls `register_translation_project.py` for each. |
| `pull_translations.py` | Orchestrator that calls the correct service adapter for each enabled service. Never contains service-specific logic. |
| `pull_weblate_translations.py` | Downloads `.po` files from the Weblate REST API and writes them to the correct `translations/` directories. |
| `pull_launchpad_translations.py` | Launchpad adapter (stub — structure in place, API calls not yet implemented). |
| `pull_crowdin_translations.py` | Crowdin adapter (stub — structure in place, API calls not yet implemented). |

### End-to-End Flow

1. An IG admin adds or updates `sushi-config.yaml#translations` in a downstream IG repo.
2. The IG's `notify_smart_base.yml` workflow fires a `repository_dispatch` event of type `dak-ig-registered` to **smart-base**.
3. The `register_translation_project.yml` workflow in smart-base receives the dispatch, checks out the downstream repo, runs `register_translation_project.py`, and creates/verifies the project and components on all enabled services.
4. Nightly (or on demand), `pull_translations.py` pulls updated `.po` files from each service and commits them back to the **downstream IG repo** (not smart-base).

---

## 2. Configuration Parameters Reference

Translation configuration lives in `sushi-config.yaml` under a top-level
`translations` key. If that key is absent, `dak.json#translations` is used as
a backward-compatible fallback. **`sushi-config.yaml` takes priority.**

### Example (`sushi-config.yaml`)

```yaml
translations:
  sourceLanguage: en
  languages:
    - code: ar
      name: Arabic
      direction: rtl
      plural: "nplurals=6; plural=(n == 0 ? 0 : n == 1 ? 1 : n == 2 ? 2 : n%100 >= 3 && n%100 <= 10 ? 3 : n%100 >= 11 && n%100 <= 99 ? 4 : 5);"
    - code: fr
      name: French
      direction: ltr
      plural: "nplurals=2; plural=(n > 1);"
  services:
    weblate:
      enabled: true
      url: https://hosted.weblate.org
    launchpad:
      enabled: false
    crowdin:
      enabled: false
```

### Parameter Reference

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `translations.sourceLanguage` | string | Yes | `"en"` | BCP-47 source language code |
| `translations.languages[].code` | string | Yes | — | BCP-47 / ISO 639-1 language code (e.g. `"fr"`, `"zh"`, `"ar"`) |
| `translations.languages[].name` | string | Yes | — | Human-readable language name (e.g. `"French"`) |
| `translations.languages[].direction` | string | Yes | `"ltr"` | Text direction: `ltr` (left-to-right) or `rtl` (right-to-left) |
| `translations.languages[].plural` | string | No | `""` | GNU gettext plural forms expression |
| `translations.services.weblate.enabled` | boolean | Yes | `false` | Enable Weblate integration |
| `translations.services.weblate.url` | string | No | `"https://hosted.weblate.org"` | Weblate instance base URL |
| `translations.services.launchpad.enabled` | boolean | Yes | `false` | Enable Launchpad integration |
| `translations.services.launchpad.project` | string | No | — | Launchpad project name override |
| `translations.services.crowdin.enabled` | boolean | Yes | `false` | Enable Crowdin integration |
| `translations.services.crowdin.projectId` | string | No | — | Crowdin numeric project ID |

### Project Slug Derivation

The **project slug** is the stable identifier used across all translation services:

```
{github_org}-{repo_name}   (all lowercase)
```

Examples:
- org `WorldHealthOrganization`, repo `smart-hiv` → `worldhealthorganization-smart-hiv`
- org `WorldHealthOrganization`, repo `smart-base` → `worldhealthorganization-smart-base`

Derivation in code:
- Manual call: `get_project_slug(github_org, repo_name)` in `translation_config.py`
- Automated: `derive_project_slug_from_env()` reads the `GITHUB_REPOSITORY` env var
  (e.g. `WorldHealthOrganization/smart-hiv`) and splits on `/`.

### Component Slug Derivation

A **component** corresponds to one `.pot` source file. The component slug is
derived from the `.pot` file's path:

**Algorithm:** Take all path segments between `input/` and `/translations/`,
append the `.pot` file stem, join with `-`, lowercase, replace non-alphanumeric
characters with `-`.

Examples:

| `.pot` file path | Component slug |
|-----------------|----------------|
| `input/fsh/translations/base.pot` | `fsh-base` |
| `input/pagecontent/translations/pages.pot` | `pagecontent-pages` |
| `input/images/translations/images.pot` | `images-images` |
| `input/images-source/translations/diagrams.pot` | `images-source-diagrams` |

Components are discovered automatically by scanning the repo for all
`*.pot` files inside `translations/` subdirectories. Paths under `output/`,
`temp/`, `fsh-generated/`, and `node_modules/` are excluded.

### Config Priority

`sushi-config.yaml#translations` is read first. If that key is absent or the
file does not exist, `dak.json#translations` is tried. This preserves
backward compatibility for repos that store translations config only in
`dak.json`.

---

## 3. Environment Variables & Secrets Reference

> ⚠️ **API tokens MUST be GitHub Actions secrets.** They must never appear as
> workflow `inputs`. `translation_security.py` will raise a `RuntimeError` at
> script startup if a token is detected as a workflow input.

| Variable | Source | Required by | Notes |
|----------|--------|-------------|-------|
| `WEBLATE_API_TOKEN` | GitHub Actions secret | Weblate registration + pull | Project-admin scope for registration; read scope for pull |
| `CROWDIN_API_TOKEN` | GitHub Actions secret | Crowdin (if enabled) | Project-admin for registration; read for pull |
| `LAUNCHPAD_API_TOKEN` | GitHub Actions secret | Launchpad (if enabled) | OAuth 1.0 token |
| `GITHUB_TOKEN` | Auto-provided by Actions | Bulk registration (`mode=all`) | Used for GitHub Code Search API (`/search/code?q=filename:dak.json org:{org}`) |
| `SMARTBASE_DISPATCH_TOKEN` | GitHub Actions secret (in **each downstream IG repo**) | `notify_smart_base.yml` | PAT with `repo` scope on smart-base; used to fire `repository_dispatch` |
| `GITHUB_REPOSITORY` | Auto-provided by Actions | `pull_translations.py` | Format: `{org}/{repo}` — used to derive the project slug |

---

## 4. Step-by-Step: Connect Each Translation Service

### 4a. Weblate (fully implemented)

#### Step 1 — Get a Weblate API token

1. Log in at https://hosted.weblate.org (or your self-hosted Weblate instance).
2. Navigate to: **Account → Settings → API access**
   (direct path: `/accounts/profile/#api`)
3. Click **Generate** — you need **project-admin** scope for registration,
   read-only scope is sufficient for pulling translations.
4. Copy the token (shown only once).

#### Step 2 — Add the token as a GitHub Actions secret

Via the GitHub UI:

```
Repo → Settings → Secrets and variables → Actions → New repository secret
  Name:  WEBLATE_API_TOKEN
  Value: <your token>
```

Via the GitHub CLI:

```bash
gh secret set WEBLATE_API_TOKEN --repo WorldHealthOrganization/{repo-name}
```

#### Step 3 — Configure `sushi-config.yaml`

```yaml
translations:
  sourceLanguage: en
  languages:
    - code: fr
      name: French
      direction: ltr
      plural: "nplurals=2; plural=(n > 1);"
  services:
    weblate:
      enabled: true
      url: https://hosted.weblate.org
```

> **Tip:** Use `dak.json#translations` only as a fallback. Prefer
> `sushi-config.yaml` for all new configurations.

#### Step 4 — Seed `.pot` source files

`.pot` files must exist in the repo before registration. Run:

```
Actions (in the IG repo) → Commit POT Files → Run workflow
```

Or locally:

```bash
python input/scripts/extract_translations.py
git add input/*/translations/*.pot
git commit -m "chore: seed translation templates"
git push
```

#### Step 5 — Register the project in Weblate

**Manual (UI):**

```
Actions (in smart-base) → Register Translation Project
  → mode = single
  → repo_name = {repo-name}
  → Run workflow
```

**Automated (push `dak.json` or `sushi-config.yaml`):**

The downstream IG's `notify_smart_base.yml` fires a `repository_dispatch`
event of type `dak-ig-registered` to smart-base, which triggers registration
automatically.

**From the command line (local):**

```bash
cd /path/to/{repo-name}
export WEBLATE_API_TOKEN=<your-token>
python /path/to/smart-base/input/scripts/register_translation_project.py \
  --repo-name {repo-name} \
  --repo-root .
```

#### Step 6 — Verify

Visit:

```
https://hosted.weblate.org/projects/worldhealthorganization-{repo-name}/
```

All discovered components (one per `.pot` file) should be visible.

#### Step 7 — Pull translations

```
Actions (in smart-base) → Pull Translations → service = weblate → Run workflow
```

Or nightly scheduled (see `pull_translations.yml`).

---

### 4b. Crowdin

1. **Create a Crowdin project** at https://crowdin.com and note the numeric
   project ID (visible in the project URL or under **Settings → API**).
2. Get a Crowdin Personal Access Token:
   https://crowdin.com → **Account Settings → API → Personal Access Tokens**
3. Add `CROWDIN_API_TOKEN` as a GitHub Actions secret (see [Step 2](#step-2--add-the-token-as-a-github-actions-secret) above).
4. Configure `sushi-config.yaml`:
   ```yaml
   translations:
     services:
       crowdin:
         enabled: true
         projectId: "12345"
   ```
5. Run the registration workflow — it will verify the Crowdin project is
   reachable and upload all `.pot` source files. Existing source files are
   updated in place; new files are created automatically.
6. Pull translations with the Pull Translations workflow (service = crowdin)
   or via `python pull_crowdin_translations.py`.

---

### 4c. Launchpad (stub — not yet fully implemented)

> **Note:** The Launchpad adapter (`pull_launchpad_translations.py`) is currently
> a stub. It uses OAuth 1.0. Full implementation is tracked in issue #281.

1. Create a Launchpad account at https://launchpad.net.
2. Generate an OAuth token at https://launchpad.net/+apitokens.
3. Add `LAUNCHPAD_API_TOKEN` as a GitHub Actions secret.
4. Configure `sushi-config.yaml`:
   ```yaml
   translations:
     services:
       launchpad:
         enabled: true
   ```
5. Run the registration workflow — the current stub will log
   `✓ Launchpad registration completed (stub)` but skip actual API calls.

---

## 5. GitHub Actions Workflow Reference

### `register_translation_project.yml`

**Location:** `.github/workflows/register_translation_project.yml`  
**Repository:** `WorldHealthOrganization/smart-base`

#### Triggers

| Trigger | When |
|---------|------|
| `workflow_dispatch` | Manual run from the Actions UI |
| `repository_dispatch` type=`dak-ig-registered` | Automatic — fired by downstream IGs when `dak.json` or `sushi-config.yaml` is pushed |

#### `workflow_dispatch` Inputs

| Input | Type | Default | Description |
|-------|------|---------|-------------|
| `mode` | choice: `single` / `all` | `single` | Register one repo or all DAK repos in the org |
| `repo_name` | string | (blank) | Target repo name — required for `mode=single`; ignored for `mode=all` |
| `dry_run` | boolean | `false` | List discovered repos without registering (`mode=all` only) |

#### Required Secrets

| Secret | Mode |
|--------|------|
| `WEBLATE_API_TOKEN` | Both |
| `CROWDIN_API_TOKEN` | Both (if Crowdin enabled) |
| `LAUNCHPAD_API_TOKEN` | Both (if Launchpad enabled) |
| `GITHUB_TOKEN` | `mode=all` only |

#### Security

- `repo_name` is validated with `^[A-Za-z0-9_-]+$` before being passed to Python.
- API tokens are passed as environment variables (never as workflow inputs).
- `translation_security.py` will fail with exit code 1 if a token is found in
  the `INPUT_*` environment variable namespace.

---

## 6. Runbook: Common Operations

### Register a new IG repo (single)

```
1. Ensure dak.json and sushi-config.yaml#translations are committed in the IG repo.
2. Ensure .pot files are committed (run commit-pot.yml if needed).
3. Navigate to: smart-base → Actions → Register Translation Project
4. Click "Run workflow"
5. Set:  mode = single
         repo_name = {repo-name}
         dry_run = false
6. Click "Run workflow"
```

### Bulk re-register all DAK repos (with dry-run first)

```bash
# Step 1: Dry run — list discovered repos without registering
Actions → Register Translation Project
  → mode = all, dry_run = true → Run workflow

# Step 2: Review the log output

# Step 3: Actual registration
Actions → Register Translation Project
  → mode = all, dry_run = false → Run workflow
```

### Manually pull translations for one language

```
Actions → Pull Translations
  → service = weblate
  → language = fr
  → Run workflow
```

Or via CLI:

```bash
cd /path/to/smart-base
export WEBLATE_API_TOKEN=<token>
export GITHUB_REPOSITORY=WorldHealthOrganization/smart-base
python input/scripts/pull_translations.py \
  --service weblate \
  --language fr \
  --repo-root .
```

### Manually pull translations for one component

```
Actions → Pull Translations
  → service = weblate
  → component = fsh-base
  → Run workflow
```

Or via CLI:

```bash
python input/scripts/pull_translations.py \
  --service weblate \
  --component fsh-base \
  --repo-root .
```

### Debug: Check what components will be discovered

```bash
cd /path/to/{repo-root}
python input/scripts/translation_config.py --repo-root .
```

Sample output:

```
DAK: smart.who.int.base (Base)
Source language: en
Target languages:
  ar - Arabic (rtl)
  zh - Chinese (Simplified) (ltr)
  fr - French (ltr)
  ru - Russian (ltr)
  es - Spanish (ltr)
Services:
  weblate: enabled (https://hosted.weblate.org)
  launchpad: disabled
  crowdin: disabled

Discovered components:
  fsh-base → input/fsh/translations/base.pot
  pagecontent-pages → input/pagecontent/translations/pages.pot
  images-images → input/images/translations/images.pot
```

### Debug: Check what services are enabled

Same command as above — the "Services:" section lists enabled/disabled status:

```bash
python input/scripts/translation_config.py --repo-root .
```

### Add a new language

1. Edit `sushi-config.yaml`, add an entry under `translations.languages`:
   ```yaml
   - code: pt
     name: Portuguese
     direction: ltr
     plural: "nplurals=2; plural=(n != 1);"
   ```
2. Commit and push.
3. Re-register the project (new languages are picked up automatically by
   Weblate when the `.pot` files are updated).
4. Pull translations once translators have contributed:
   ```
   Actions → Pull Translations → language = pt
   ```

### Disable a service

1. Set `enabled: false` in `sushi-config.yaml`:
   ```yaml
   services:
     weblate:
       enabled: false
   ```
2. Commit and push — no re-registration is needed. The registration and pull
   scripts will skip any service with `enabled: false`.

---

## 7. Troubleshooting Guide

| Symptom | Cause | Fix |
|---------|-------|-----|
| `WEBLATE_API_TOKEN not set` | Secret missing or mis-named | Add secret with exact name `WEBLATE_API_TOKEN` (case-sensitive) |
| `dak.json not found` | Wrong `--repo-root` or file missing | Ensure `dak.json` exists at the repo root; check `--repo-root` argument |
| `Invalid repo_name: contains disallowed characters` | Repo name has special characters | Only `[A-Za-z0-9_-]` are allowed in `repo_name` |
| Component not appearing in Weblate | No `.pot` file committed yet | Run `commit-pot.yml` (or `extract_translations.py`) to seed `.pot` files first |
| HTTP 403 on Weblate project create | Token lacks project-admin scope | Regenerate token with project-admin permission at `/accounts/profile/#api` |
| HTTP 429 rate limit | Too many requests in a short period | Script will log the error; retry after a few minutes |
| `No translation services enabled` | All services have `enabled: false` | Edit `sushi-config.yaml` to enable at least one service |
| Crowdin/Launchpad registration "completed (stub)" | Not yet fully implemented | Expected behavior — watch issue #281 for full implementation |
| `Security violation: WEBLATE_API_TOKEN appears to be passed as a workflow input` | Token passed as a workflow input instead of a secret | Move token to GitHub Actions secrets; never pass tokens as `workflow_dispatch` inputs |
| `Cannot parse sushi-config.yaml` | YAML syntax error | Validate the file with `python -c "import yaml; yaml.safe_load(open('sushi-config.yaml'))"` |
| Pull downloads 0 files | Language/component not yet in Weblate | Check that components are registered and translators have contributed; `not_found` (404) is normal for untranslated content |
| `Unknown component` error in `pull_weblate_translations.py` | Component slug not in the `COMPONENT_MAP` allowlist in `pull_weblate_translations.py` | Note: **registration** uses dynamic discovery (`discover_components()` in `translation_config.py`), but **pull_weblate_translations.py** maintains its own hardcoded `COMPONENT_MAP` allowlist for safety. If a new component is not in that allowlist, add it to `COMPONENT_MAP` in `pull_weblate_translations.py` and ensure the corresponding `translations/` directory exists |

---

## 8. Security Notes

- **API tokens MUST always be GitHub Actions secrets**, never `workflow_dispatch` inputs.
  The `assert_no_secret_in_env()` check in `translation_security.py` raises a
  `RuntimeError` at script startup if a token is detected as a workflow input
  (present in the `INPUT_*` environment variable namespace). This is intentional
  and will fail the workflow with exit code 1.

- **Token redaction:** All log output uses `redact_for_log()` from
  `translation_security.py`, which shows only the first 4 characters of a token
  followed by `***` (e.g. `wlu_***`). Full token values are never written to
  logs or error messages.

- **Slug sanitization:** `sanitize_slug()` enforces `^[a-z0-9][a-z0-9_-]{0,127}$`
  on all slug inputs (repo names, component slugs, project slugs) to prevent
  path traversal or injection attacks. Invalid values raise a `ValueError` and
  the script exits with code 1.

- **URL validation:** `sanitize_url()` enforces that Weblate URLs use the `https`
  scheme and contain a valid hostname.

- **HTTP safety:** All HTTP requests use:
  - A 60-second connection timeout (`DEFAULT_TIMEOUT_SECONDS`)
  - A 10 MiB response size guard (`MAX_RESPONSE_BYTES`), implemented as a
    streaming download with byte counting

- **`repository_dispatch` payload validation:** The `register_translation_project.yml`
  workflow validates `repo_name` with `^[A-Za-z0-9_-]+$` before passing it to
  Python, guarding against malicious payloads from third-party dispatch senders.

- **Least-privilege secrets:** Use separate tokens for registration
  (project-admin scope) and pull (read scope) where the service supports it.
  Rotate tokens regularly. Store them only in GitHub Actions secrets
  (`Settings → Secrets and variables → Actions`), never in code, config files,
  or workflow inputs.
