#!/usr/bin/env python3
"""
Check that no extension or profile in this IG's FSH slices `extension` twice
with the same extension definition.

A validator tells extension slices apart by url alone. SGUserStory used to
declare `extension contains SGString named capability 1..1` and
`SGString named benefit 1..1`, so both slices had SGString's url: every user
story with both values then failed with "matches more than one slice",
"capability max 1 found 2" and "benefit required slice not found" (212 errors
in smart-dak-tb). Inline sub-extensions (`extension contains capability 1..1
and benefit 1..1`) take their slice name as their url and are always distinct.

It also checks that SGUserStory's sub-extension slices are the ones that
req_extractor.py and the SGAuthoring actor instances set:
`extension[userstory].extension[capability|benefit].valueString`.

Run: python3 input/scripts/extension_slices.test.py
"""

from __future__ import annotations

import os
import re
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
FSH = os.path.join(REPO, "input", "fsh")

ENTITY = re.compile(r"^(Profile|Extension|Logical|Resource|Instance|ValueSet|CodeSystem"
                    r"|Invariant|RuleSet|Mapping):\s*(\S+)")
# `* <path> contains <items>`; the items may continue on following lines
CONTAINS = re.compile(r"^\*\s+(\S+)\s+contains\b(.*)$")
ITEM = re.compile(r"^(\S+)(?:\s+named\s+(\S+))?\s+\d+\.\.(?:\d+|\*)?")


def contains_rules(text: str):
    """Yield (entity, path, [(definition, slice)]) for each `contains` rule."""
    entity = None
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = re.sub(r"//.*$", "", lines[i]).rstrip()
        m = ENTITY.match(line)
        if m:
            entity = m.group(2)
        m = CONTAINS.match(line.strip())
        if m and entity:
            path, rest = m.group(1), m.group(2)
            # an item list ending in `and` continues on the next line
            while rest.rstrip().endswith("and") and i + 1 < len(lines):
                i += 1
                rest += " " + re.sub(r"//.*$", "", lines[i]).strip()
            items = []
            for part in re.split(r"\s+and\s+", rest.strip()):
                im = ITEM.match(part.strip())
                if im:
                    definition, name = im.groups()
                    # without `named`, the slice is inline: its url is its name
                    items.append((definition if name else None, name or definition))
            yield entity, path, items
        i += 1


def main() -> int:
    failures = []
    slices = defaultdict(list)  # (entity, path) -> [(definition, slice)]
    for root, _, files in os.walk(FSH):
        for f in files:
            if not f.endswith(".fsh"):
                continue
            with open(os.path.join(root, f), encoding="utf-8") as fh:
                for entity, path, items in contains_rules(fh.read()):
                    last = re.sub(r"\[[^\]]*\]", "", path).split(".")[-1]
                    if last.lower().endswith("extension"):
                        slices[(entity, path)].extend(items)

    for (entity, path), items in sorted(slices.items()):
        by_def = defaultdict(list)
        for definition, name in items:
            if definition is not None:
                by_def[definition].append(name)
        for definition, names in by_def.items():
            if len(names) > 1:
                failures.append(
                    f"{entity}.{path} slices {definition} as {', '.join(names)}: the slices share "
                    f"one url, so a validator cannot tell them apart. Use inline sub-extensions "
                    f"(`{path} contains {' and '.join(n + ' 1..1' for n in names)}`) or a distinct "
                    f"extension for each.")

    us = slices.get(("SGUserStory", "extension"), [])
    inline = {name for definition, name in us if definition is None}
    if inline != {"capability", "benefit"}:
        failures.append(f"SGUserStory's inline sub-extensions are {sorted(inline)}, "
                        "expected capability and benefit")

    # the paths a DAK sets, as req_extractor writes them
    with open(os.path.join(HERE, "req_extractor.py"), encoding="utf-8") as fh:
        extractor = fh.read()
    for name in ("capability", "benefit"):
        p = f"extension[userstory].extension[{name}].valueString"
        if p not in extractor:
            failures.append(f"req_extractor.py does not write {p}")

    checked = sum(len(v) for v in slices.values())
    for f in failures:
        print("FAIL:", f)
    print(f"{'FAILED' if failures else 'OK'}: extension slices ({checked} slice(s) on "
          f"{len(slices)} path(s), {len(failures)} failure(s))")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
