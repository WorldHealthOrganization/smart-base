# DAK Skill Library

The DAK Skill Library provides AI-assisted and structural validation tools
for authoring WHO Digital Adaptation Kit (DAK) content.

## Quick Start

### Local Development (Docker)

```bash
# 1. Build the image
docker build -t dak-skill .github/skills/

# 2. Copy environment template
cp .env.example .env
# Edit .env to add your LLM API key (optional — structural validation works without it)

# 3. Run skills
docker compose -f .github/skills/docker-compose.yml run --rm validate
docker compose -f .github/skills/docker-compose.yml run --rm validate-ig
docker compose -f .github/skills/docker-compose.yml run --rm import-bpmn
docker compose -f .github/skills/docker-compose.yml run --rm shell

# Shortcut alias:
alias dak='docker compose -f .github/skills/docker-compose.yml run --rm'
dak validate
dak import-bpmn
```

### CI (GitHub Actions)

Skills run automatically via GitHub Actions workflows:

| Trigger | Workflow | What it does |
|---|---|---|
| Issue opened/edited | `classify-issue.yml` | Auto-labels issues with `content:L1/L2/L3/translation` |
| Label `content:L1` | `skill-l1-review.yml` | L1 guideline review (placeholder) |
| Label `content:L2` | `skill-l2-dak.yml` | L2 DAK content authoring |
| Label `content:L3` | `skill-l3-review.yml` | L3 adaptation review (placeholder) |
| Label `content:translation` | `skill-translation.yml` | Translation management (placeholder) |
| PR comment `/validate` | `pr-validate-slash.yml` | Structural + IG validation |

## One-Time Repository Setup

```
1. Create labels (Issues → Labels → New label):
     content:L1           #0075ca   "WHO source guideline content"
     content:L2           #e4e669   "DAK FHIR assets"
     content:L3           #d73a4a   "Implementation adaptations"
     content:translation  #0e8a16   "Translation of any content layer"
   (Label definitions also stored in .github/skills/labels/*.json for reference.)

2. Add secret (Settings → Secrets and variables → Actions → New repository secret):
     DAK_LLM_API_KEY  =  sk-...

3. Add variable (Settings → Secrets and variables → Variables → New variable):
     DAK_LLM_MODEL  =  gpt-4o    (or gpt-4o-mini to reduce cost)
   See .env.example for the full list of supported model identifiers,
   or https://docs.litellm.ai/docs/providers for the master list.

4. Build local Docker image (optional, for local development):
     docker build -t dak-skill .github/skills/
```

## Security Model

- **API keys MUST NOT appear** in dispatch inputs, issue comments, PR comments, or any user-visible UI
- Two legitimate locations only: **repo secret** (CI) or **local `.env` file** (Docker/local)
- LLM steps skip gracefully when no key present — non-LLM validation always runs
- **Zero WHO infrastructure cost; zero WHO AI cost**

### Graceful Degradation

| Skill | No key | With key |
|---|---|---|
| BPMN structure validation | ✅ runs | ✅ runs |
| Swimlane ↔ ActorDef validation | ✅ runs | ✅ runs |
| IG Publisher build/validate | ✅ runs | ✅ runs |
| Issue classification | keyword fallback | LLM classification |
| LLM BPMN authoring | ⚠️ skipped | ✅ runs |
| LLM error interpretation | ⚠️ skipped | ✅ runs |

## Directory Structure

```
.github/skills/
├── Dockerfile              # FROM hl7fhir/ig-publisher-base — mirrors CI
├── docker-compose.yml      # Service aliases: validate, author, import, shell
├── README.md               # This file
├── skills_registry.yaml    # All registered skills
├── cli/
│   └── dak_skill.py        # CLI entry point
├── common/
│   ├── llm_utils.py       # LLM helpers — thin wrappers around LiteLLM
│   ├── prompts.py          # load_prompt() — .md templates with {variable}
│   ├── ig_errors.py        # FATAL/ERROR/WARNING/INFORMATION format
│   ├── fsh_utils.py        # FSH file utilities
│   ├── ig_publisher_iface.py
│   └── prompts/            # Shared prompt templates
├── bpmn_author/            # Author/edit BPMN
├── bpmn_import/            # Import BPMN → FSH, validate lanes
├── ig_publisher/           # IG Publisher validation and build
├── dak_authoring/          # Issue classification and L2 content review/authoring
│   ├── actions/
│   │   ├── classify_issue_action.py   # Keyword + LLM issue classifier
│   │   └── dak_authoring_action.py    # L2 content review skill (→ content:L2 label)
│   └── prompts/
├── labels/                 # GitHub label definitions (JSON, for reference)
├── l1_review/              # (placeholder v0.2)
├── l3_review/              # (placeholder v0.3)
└── translation/            # (placeholder v0.3)
```

## LLM Provider

LLM features use [LiteLLM](https://github.com/BerriAI/litellm) (MIT License) —
a well-maintained multi-provider library (OpenAI, Anthropic, Google, etc.)
with 20k+ GitHub stars. The `common/llm_utils.py` module adds only DAK-specific
environment variable bridging and JSON-extraction helpers on top of LiteLLM;
there is no custom LLM facade to maintain.
