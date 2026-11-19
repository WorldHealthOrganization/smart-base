# AGENTS.md — litlfred/smart-base

This repository holds two different things, and they publish two different
ways. Most mistakes here come from treating one as the other.

| | what | published by | previewed at |
|---|---|---|---|
| `input/`, `sushi-config.yaml` | the WHO SMART Base **FHIR IG** | the gh-pages ROOT: an agent, by the IG route every smart-* IG uses (`bun run cat-harness-tools/scripts/stage-local.ts --repo .`, from the cached AST; `index.config.json` `site`). The IG Publisher (`ghbuild.yml`) only previews, and never deploys over a folio root | `branches/<branch>/` (stage-local); Publisher output at `gh-pages/branches/<branch>/` (`/deploy`) |
| `smart-base/` | the smart-base **harness layer**: skills, processes (BPMN), library, KG | folio-assistant's just-the-docs site, which **mounts** this directory | folio-assistant `branches/<slug>/` (`feature-staging`) |

## The platform is mounted, not absent

The platform layers are remote mounts, not a submodule (bean
folio-assistant-n3h9). The SessionStart hook (`.claude/mount-platform.sh`)
replays `index.lock.json` with cat-harness-tools' `mount-from-lock.ts`, the
same steps `site-publish.yml` runs, which puts fhir-harness,
folio-assistant-core, cat-harness, cat-harness-tools, bootstrap and
bootstrap-tools on disk at the repository root (gitignored). **Read the
platform's skills there before choosing how to build, render, review or
stage anything** (`cat-harness/skills/`, `fhir-harness/skills/`). If they
are missing, run `bash .claude/mount-platform.sh`. Every platform script
runs as `bun run cat <script>` (the root `cat` script, `.github/cat.ts`,
written from cat-harness-tools' `templates/root-bootstrap/`), which mounts
the layers first when they are missing or `index.lock.json` has moved.

`./smart-base/` is this repository's own copy of the harness layer (its
`index.config.json` entry is `source.local`). Edit it here; downstream IGs
mount it at a pinned commit.

## Rules

1. **A change under `smart-base/` is previewed on the just-the-docs staging
   site, never with `/deploy` or `ghbuild.yml`.** Stage it with a
   folio-assistant pull request that re-pins the `smart-base` mount to the
   branch's commit, recorded by `bun run cat mount:remote --staging` (basis
   `staging`, no consent needed). `feature-staging.yml` then publishes
   `branches/<slug>/` and comments the links. `/deploy` builds the IG, which
   does not contain this content.
2. **Processes live under `smart-base/processes/`**: the `.bpmn`, its
   documentation, and its picture beside it (`bun run cat render:bpmn`,
   cat-harness-tools' renderer, which draws every layer's diagrams beside
   their source with the mounted bootstrap-tools). Do not copy a process
   or its picture into `input/`; the just-the-docs site draws every mounted
   process itself.
3. **Reuse before adding.** A skill, schema, process or role the platform
   already has is used by name. Check the mounted layers first.
4. **Before running SUSHI or the IG Publisher, read fhir-harness's
   [`fhir-validation`](https://github.com/litlfred/fhir-harness/blob/main/skills/content/fhir-ig-authoring/fhir-validation.md#when-a-package-host-refuses-you) §"When a package host refuses you".** Where
   packages.fhir.org is refused, `fhir-cache-seed-npm` fills the package
   cache from npm and fhir-package-mirror at exact versions only. Never report
   "SUSHI cannot run here" before running the seeder, and never stand in
   another version for a pin; its `--missing-out` list is what the mirror
   still needs. WHO's own packages (`smart.who.int.*`, such as
   `smart.who.int.base#1.0.0`) are on neither npm nor the mirror: WHO
   publishes them in its site repository, so pass
   `--site-repo smart.who.int.=WorldHealthOrganization/smart-html`, which
   reads `<name>/<version>/package.tgz` there (for example `base/1.0.0/`).
5. **This IG does not commit its artefact index.** `smart-base/fhir-artifact-index/`
   (`index.json`, `menu.json`, `releases.json`, `package.tgz`, `sidecars/`) is written at
   publish by fhir-harness's `ig-index:build` from the IG's AST and its
   `sushi-config.yaml` (fhir-harness#124), and is gitignored. Never commit it,
   hand-edit it, or re-ingest it from the published site.
6. **The harness reads only what `contentTypes.ig.include` lists.**
   `index.config.json` declares this repository an IG source
   (`contentTypes.ig`, fhir-harness's `ig` content type; owner, 2026-10-30:
   "harness desclares what it it pays attention to in the repo"). Its
   `include` list is every path fhir-harness's IG readers (the artefact
   index, the IG site, the menu, the API hub, the review data) may read here,
   and nothing else is read. When you add a directory or file under `input/`
   that the site or the index needs, add it to `include` in the same pull
   request: a directory ends in `/`, and the narrowest path wins. A path left
   off is silently absent from the site, which is how `input/diagrams/`,
   `input/archimate/` and `input/dmn/` went missing before #215. The rules
   and the legacy warning are fhir-harness's
   [`ig-build-pipeline`](https://github.com/litlfred/fhir-harness/blob/main/skills/fhir-ig-base/ig-build-pipeline.md#what-this-layer-reads-contenttypesiginclude)
   §"What this layer reads". SUSHI and the IG Publisher still read what they
   read; the list bounds the harness, not them.
