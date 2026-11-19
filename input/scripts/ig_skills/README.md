# DAK skill scripts (pending migration)

What is left here is pending migration into the smart-base knowledge graph
(`smart-base/`), and nothing in this repository runs it: no workflow, no
build step and no container calls these scripts. Do not add to it.

These four directories used to sit in `.github/skills/`, beside the
generated Copilot skills. They moved here because `skills-installed.yml`'s
`--check` fails on any file in a host skills directory that the installer did
not write (bean folio-assistant-dtda). `.github/skills/` and `.claude/skills/`
now hold only generated `<prefix>-<name>/` copies of harness skills: never edit
one, edit the source its `<!-- source: -->` line names, then regenerate from
the repository root with

```sh
bun run cat skills:install --root smart-base --into . --host copilot
bun run cat skills:install --root smart-base --into . --host claude
```

| Directory | What it holds | Expected to move under |
|---|---|---|
| `bpmn_import/` | the import-error interpretation prompt (its validator is gone, see below) | bean folio-assistant-14un, with the other prompts |
| `dak_authoring/` | the issue classifier and L2 authoring actions and their prompts | bean folio-assistant-14un |
| `ig_publisher/` | the IG Publisher build, validate and error-interpretation actions | bean folio-assistant-14un |
| `common/` | shared helpers (`ig_errors`, `fsh_utils`, `llm_utils`, `prompt_loader`, `ig_publisher_iface`) and shared prompts | with whichever of the above still uses them |

Notes for anyone running a script by hand before it moves:

- The scripts import each other from this directory, so run them with
  `input/scripts/ig_skills/` on `PYTHONPATH`.
- BPMN is checked by smart-base's `bpmn-validate` Tool
  (`smart-base/L2-bpmn/tools/bpmn-validate/`), which `validate_dak_action.py`
  runs; there is no Python BPMN validator here.
- ELM extraction is not here: fhir-harness owns the ELM strippers, and
  `ghbuild.yml` runs `input/scripts/strip_library_binaries.py`.
- The LLM steps read `DAK_LLM_API_KEY` and `DAK_LLM_MODEL` (see
  `.env.example`) through LiteLLM and are skipped when no key is set. No
  dependency lock is kept for these scripts any more.

Removed by bean folio-assistant-hhkw (epic folio-assistant-95e7): the Docker
CLI (`cli/`, `Dockerfile`, `docker-compose.yml`), `skills_registry.yaml` and
every `skills.yaml`, the label definitions, the `l1_review`, `l3_review` and
`translation` placeholders, `bpmn_import/actions/`, the ELM strip action,
the duplicate `safe_xml.py`, and the label and `/validate` workflows, none of
which could fire.

Removed by bean folio-assistant-tgaj (epic folio-assistant-95e7): the four
overlapping BPMN validators (`bpmn_author/validators/`,
`bpmn_import/validators/`, `bpmn_layout/validate_swimlanes.py`) and the rest
of `bpmn_author/`, replaced by the one Tool `bpmn-validate` in smart-base's
`L2-bpmn` sub-graph, which pull-request CI runs on every changed `.bpmn`
(`.github/workflows/bpmn-validate.yml`). `bpmn_layout/bpmn_to_svg.py`, the
Graphviz auto-layout that writes Diagram Interchange into a BPMN that has
none, moved to `smart-base/L2-bpmn/tools/bpmn-graphviz-layout/`:
cat-harness-tools' `render:bpmn` draws the DI a file already carries and does
not lay one out.
