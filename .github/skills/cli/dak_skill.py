#!/usr/bin/env python3
"""
dak-skill CLI — entry point for the DAK Skill Library.

Usage:
    dak-skill validate          # DAK structural validation (no LLM needed)
    dak-skill validate-ig       # Full IG Publisher validation
    dak-skill build-ig          # Full IG Publisher build
    dak-skill import-bpmn       # Import BPMN files and validate
    dak-skill author "..."      # LLM-assisted BPMN authoring
    dak-skill classify          # Classify current issue
    dak-skill --help            # Show help

Environment variables:
    DAK_LLM_API_KEY  — LLM API key (optional; LLM steps skipped if absent)
    DAK_LLM_MODEL    — LLM model name (default: gpt-4o)
    DAK_IG_ROOT      — IG root directory (default: current directory)
"""

import argparse
import importlib
import sys
from pathlib import Path

# Ensure the skills root is on sys.path
_SKILLS_ROOT = Path(__file__).resolve().parent.parent
if str(_SKILLS_ROOT) not in sys.path:
    sys.path.insert(0, str(_SKILLS_ROOT))

# Map CLI commands to action module paths
_COMMANDS = {
    "validate": "ig_publisher.actions.validate_dak_action",
    "validate-ig": "ig_publisher.actions.validate_ig_action",
    "build-ig": "ig_publisher.actions.build_ig_action",
    "import-bpmn": "bpmn_import.actions.bpmn_import_action",
    "author": "bpmn_author.actions.bpmn_author_action",
    "classify": "dak_authoring.actions.classify_issue_action",
    "interpret-errors": "ig_publisher.actions.interpret_errors_action",
}


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="dak-skill",
        description="DAK Skill Library CLI",
    )
    parser.add_argument(
        "command",
        choices=list(_COMMANDS.keys()),
        help="Skill command to run",
    )
    parser.add_argument(
        "args",
        nargs="*",
        help="Additional arguments passed to the skill",
    )

    args = parser.parse_args()

    module_path = _COMMANDS[args.command]
    try:
        module = importlib.import_module(module_path)
    except ImportError as exc:
        print(f"❌ Failed to import skill module '{module_path}': {exc}", file=sys.stderr)
        sys.exit(1)

    if hasattr(module, "main"):
        module.main()
    else:
        print(f"❌ Module '{module_path}' has no main() function", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
