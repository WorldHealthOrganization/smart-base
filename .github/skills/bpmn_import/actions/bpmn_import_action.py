"""
BPMN Import action — wraps bpmn_extractor.py and validates lane→actor mapping.

Environment variables:
    DAK_LLM_API_KEY  — LLM API key (optional; error interpretation skipped if absent)
    DAK_LLM_MODEL    — LLM model name (default: gpt-4o)
    GITHUB_TOKEN     — GitHub API token
    DAK_IG_ROOT      — IG root directory (default: current directory)
"""

import glob
import os
import sys
from pathlib import Path

_SKILLS_ROOT = Path(__file__).resolve().parent.parent.parent
if str(_SKILLS_ROOT) not in sys.path:
    sys.path.insert(0, str(_SKILLS_ROOT))

from common.ig_errors import format_issues, has_errors
from bpmn_import.validators.swimlane_actor_validator import validate_swimlane_actors


def main() -> None:
    ig_root = os.environ.get("DAK_IG_ROOT", ".")
    bpmn_files = glob.glob(os.path.join(ig_root, "input", "business-processes", "*.bpmn"))

    if not bpmn_files:
        print("ℹ️  No BPMN files found in input/business-processes/")
        sys.exit(0)

    all_issues = []
    for bpmn_path in bpmn_files:
        print(f"📄 Validating: {bpmn_path}")
        content = Path(bpmn_path).read_text(encoding="utf-8")
        issues = validate_swimlane_actors(
            content,
            ig_root=ig_root,
            filename=os.path.basename(bpmn_path),
        )
        all_issues.extend(issues)

    print(format_issues(all_issues))

    if has_errors(all_issues):
        print("❌ BPMN import validation found errors.")
        sys.exit(1)

    print("✅ All BPMN files passed lane→actor validation.")


if __name__ == "__main__":
    main()
