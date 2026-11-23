#!/usr/bin/env bash
# Put the platform on disk for this session: every layer index.lock.json pins
# (fhir-harness, folio-assistant-core, cat-harness, cat-harness-tools,
# bootstrap, bootstrap-tools), mounted at the repository root and
# digest-checked by cat-harness-tools' own replayer, the same steps
# site-publish.yml runs. No submodule (bean folio-assistant-n3h9).
#
# Without this a cloud session starts with none of the platform's skills
# (feature-staging, staging-review, render:bpmn, wireframe-design-review, ...)
# on disk, and an agent falls back to the only preview this repository ships,
# the IG Publisher's branches/ build, which is the IG's and not smart-base's.
# That happened on PR #53.
#
# Idempotent: a mount already on disk and intact is reported current.
set -uo pipefail
cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/..}" || exit 0
lock=index.lock.json
[ -f "$lock" ] || { echo "mount-platform: no $lock" >&2; exit 0; }
ref=$(python3 -c "import json;print(next(m['ref'] for m in json.load(open('$lock'))['mounts'] if m['harness']=='cat-harness-tools'))") \
  || { echo "mount-platform: $lock pins no cat-harness-tools" >&2; exit 0; }
# The ref names a directory that is removed below, so refuse anything that is
# not a full commit SHA rather than build a path from it.
[[ "$ref" =~ ^[0-9a-f]{40}$ ]] || { echo "mount-platform: cat-harness-tools ref in $lock is not a 40-hex commit SHA; refusing" >&2; exit 0; }
M="${TMPDIR:-/tmp}/smart-base-mounter-$ref"
if [ ! -f "$M/scripts/mount-from-lock.ts" ]; then
  rm -rf "$M" && git init -q "$M" \
    && git -C "$M" fetch -q --depth 1 https://github.com/litlfred/cat-harness-tools.git "$ref" \
    && git -C "$M" checkout -q FETCH_HEAD \
    || { echo "mount-platform: could not fetch cat-harness-tools@$ref" >&2; exit 0; }
fi
bun run "$M/scripts/mount-from-lock.ts" --root . 2>&1 | tail -1
for d in $(python3 -c "import json;print(' '.join(sorted({i['path'] for i in json.load(open('$lock'))['instances']})))"); do
  [ -f "$d/package.json" ] || continue
  ( cd "$d" && bun install --no-save >/dev/null 2>&1 ) || echo "mount-platform: bun install failed in $d/" >&2
done
exit 0
