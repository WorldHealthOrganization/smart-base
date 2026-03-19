#!/usr/bin/env python3
"""
BPMN Swimlane-to-ActorDefinition validation skill.

Validates that every innermost swimlane (participant/lane) in a BPMN 2.0
file corresponds to an ActorDefinition resource in the IG. Reports:
  - Matched: swimlane ID maps to an existing ActorDefinition
  - Missing: swimlane has no corresponding ActorDefinition

For missing swimlanes, the tool suggests possible resolutions:
  1. The ActorDefinition exists in another IG (dependency) — reference it
  2. Create a new ActorDefinition in this IG
  3. The swimlane name is a typo — correct the BPMN

Usage:
    python validate_swimlanes.py INPUT.bpmn [--actors-dir DIR] [--fsh-dir DIR]

The tool searches for ActorDefinitions in:
  - FSH files (Instance: ... InstanceOf: ActorDefinition) in --fsh-dir
  - JSON/XML ActorDefinition files in --actors-dir
"""

import argparse
import glob
import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from difflib import get_close_matches
from pathlib import Path

BPMN_NS = "http://www.omg.org/spec/BPMN/20100524/MODEL"
NS = {"bpmn": BPMN_NS}


def find_swimlanes(bpmn_path: str) -> list:
    """Extract all participant and lane names from a BPMN file.

    Returns list of dicts with 'id', 'name', and 'type' (participant|lane).
    For collaborations, participants are the swimlanes.
    For processes with lanes, lanes are the innermost swimlanes.
    """
    tree = ET.parse(bpmn_path)
    root = tree.getroot()
    swimlanes = []

    # Collaboration participants
    for collab in root.findall("bpmn:collaboration", NS):
        for p in collab.findall("bpmn:participant", NS):
            swimlanes.append({
                "id": p.get("id"),
                "name": p.get("name", p.get("id")),
                "type": "participant",
                "processRef": p.get("processRef"),
            })

    # Also check for lanes within processes
    for proc in root.findall("bpmn:process", NS):
        for laneset in proc.findall("bpmn:laneSet", NS):
            for lane in laneset.findall("bpmn:lane", NS):
                swimlanes.append({
                    "id": lane.get("id"),
                    "name": lane.get("name", lane.get("id")),
                    "type": "lane",
                    "processRef": proc.get("id"),
                })

    return swimlanes


def find_actor_definitions_fsh(fsh_dir: str) -> dict:
    """Find ActorDefinition instances in FSH files.

    Returns dict of {instance_id: {"name": ..., "title": ..., "file": ...}}.
    """
    actors = {}
    for fsh_file in glob.glob(os.path.join(fsh_dir, "**/*.fsh"), recursive=True):
        try:
            content = Path(fsh_file).read_text()
        except (OSError, UnicodeDecodeError):
            continue

        # Find Instance declarations of ActorDefinition
        instance_pattern = re.compile(
            r'Instance:\s+(\S+)\s*\n'
            r'InstanceOf:\s+ActorDefinition',
            re.MULTILINE
        )
        for m in instance_pattern.finditer(content):
            inst_id = m.group(1)

            # Extract name and title
            name_m = re.search(r'\*\s+name\s*=\s*"([^"]*)"', content[m.start():])
            title_m = re.search(r'\*\s+title\s*=\s*"([^"]*)"', content[m.start():])

            actors[inst_id] = {
                "name": name_m.group(1) if name_m else inst_id,
                "title": title_m.group(1) if title_m else "",
                "file": fsh_file,
            }

    return actors


def find_actor_definitions_json(actors_dir: str) -> dict:
    """Find ActorDefinition resources in JSON files.

    Returns dict of {resource_id: {"name": ..., "title": ..., "file": ...}}.
    """
    actors = {}
    for json_file in glob.glob(os.path.join(actors_dir, "**/*.json"), recursive=True):
        try:
            data = json.loads(Path(json_file).read_text())
        except (OSError, json.JSONDecodeError):
            continue

        if data.get("resourceType") == "ActorDefinition":
            rid = data.get("id", "")
            actors[rid] = {
                "name": data.get("name", rid),
                "title": data.get("title", ""),
                "file": json_file,
            }

    return actors


def validate(swimlanes: list, actors: dict) -> list:
    """Validate swimlanes against known ActorDefinitions.

    Returns list of validation results.
    """
    results = []
    all_actor_names = []
    actor_by_name = {}

    for aid, ainfo in actors.items():
        # Build lookup by various name forms
        names = [aid, ainfo["name"], ainfo["title"]]
        for n in names:
            if n:
                all_actor_names.append(n)
                actor_by_name[n.lower()] = {"id": aid, **ainfo}

    for lane in swimlanes:
        lane_name = lane["name"]
        lane_id = lane["id"]

        # Try exact match by ID suffix, name, or title
        matched = None
        for aid, ainfo in actors.items():
            # Match by: exact ID, name, title, or ID ending
            if (lane_name.lower() == ainfo["name"].lower() or
                lane_name.lower() == ainfo["title"].lower() or
                aid.lower().endswith(lane_name.lower().replace(" ", "")) or
                lane_name.lower().replace(" ", "") == ainfo["name"].lower()):
                matched = {"id": aid, **ainfo}
                break

        if matched:
            results.append({
                "status": "matched",
                "swimlane_id": lane_id,
                "swimlane_name": lane_name,
                "actor_id": matched["id"],
                "actor_title": matched["title"],
                "actor_file": matched["file"],
            })
        else:
            # Find close matches for typo detection
            close = get_close_matches(lane_name, all_actor_names, n=3, cutoff=0.5)
            results.append({
                "status": "missing",
                "swimlane_id": lane_id,
                "swimlane_name": lane_name,
                "close_matches": close,
                "suggestions": [
                    f"1. ActorDefinition exists in a dependency IG — add a reference",
                    f"2. Create a new ActorDefinition in this IG for '{lane_name}'",
                ] + ([f"3. Possible typo? Did you mean: {', '.join(close)}"] if close else []),
            })

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Validate BPMN swimlanes against ActorDefinition resources"
    )
    parser.add_argument("input", help="Input BPMN file")
    parser.add_argument("--fsh-dir", help="Directory containing FSH files",
                        default="input/fsh")
    parser.add_argument("--actors-dir", help="Directory containing JSON ActorDefinitions",
                        default="input/actors")
    parser.add_argument("--json", help="Output results as JSON", action="store_true")
    args = parser.parse_args()

    bpmn_path = Path(args.input)
    if not bpmn_path.exists():
        print(f"Error: {bpmn_path} not found", file=sys.stderr)
        sys.exit(1)

    print(f"Validating BPMN swimlanes: {bpmn_path}")
    swimlanes = find_swimlanes(str(bpmn_path))
    print(f"  Found {len(swimlanes)} swimlanes")

    # Find ActorDefinitions from FSH and JSON
    actors = {}
    if os.path.isdir(args.fsh_dir):
        actors.update(find_actor_definitions_fsh(args.fsh_dir))
    if os.path.isdir(args.actors_dir):
        actors.update(find_actor_definitions_json(args.actors_dir))
    print(f"  Found {len(actors)} ActorDefinitions")

    results = validate(swimlanes, actors)

    if args.json:
        print(json.dumps(results, indent=2))
        return

    # Pretty print
    matched = [r for r in results if r["status"] == "matched"]
    missing = [r for r in results if r["status"] == "missing"]

    if matched:
        print(f"\n  MATCHED ({len(matched)}):")
        for r in matched:
            print(f"    [OK] '{r['swimlane_name']}' → {r['actor_id']} ({r['actor_file']})")

    if missing:
        print(f"\n  MISSING ({len(missing)}):")
        for r in missing:
            print(f"    [!!] '{r['swimlane_name']}' — no ActorDefinition found")
            for s in r["suggestions"]:
                print(f"         {s}")

    print(f"\nSummary: {len(matched)} matched, {len(missing)} missing")
    sys.exit(1 if missing else 0)


if __name__ == "__main__":
    main()
