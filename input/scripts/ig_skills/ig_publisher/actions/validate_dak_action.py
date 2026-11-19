"""
DAK structural validation action — validates repository structure
without requiring IG Publisher or LLM.

Environment variables:
    GITHUB_TOKEN  — GitHub API token
    PR_NUMBER     — PR number for posting results
    DAK_IG_ROOT   — IG root directory (default: current directory)
"""

import json
import os
import subprocess
import sys
from pathlib import Path

_SKILLS_ROOT = Path(__file__).resolve().parent.parent.parent
if str(_SKILLS_ROOT) not in sys.path:
    sys.path.insert(0, str(_SKILLS_ROOT))

from common.ig_errors import Issue, error, warning, info, format_issues, has_errors

# The BPMN check is the smart-base Tool `bpmn-validate` (bean
# folio-assistant-tgaj), which replaced the Python BPMN validators.
_BPMN_VALIDATE = Path(__file__).resolve().parents[4] / "smart-base" / "L2-bpmn" / "tools" / "bpmn-validate" / "validate.ts"
_LEVEL = {"error": error, "warning": warning, "info": info}


def validate_bpmn(ig_root: str) -> list:
    """Run `bpmn-validate` over the IG's declared process directories and return its findings as issues."""
    try:
        p = subprocess.run(["bun", "run", str(_BPMN_VALIDATE), "--root", ig_root, "--json"],
                           capture_output=True, text=True, timeout=300)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return [warning("DAK-003", f"bpmn-validate could not run: {exc}")]
    if p.returncode == 2:
        return [info("DAK-004", "no BPMN under the declared process directories")]
    try:
        report = json.loads(p.stdout)
    except json.JSONDecodeError:
        return [warning("DAK-003", f"bpmn-validate printed no report: {p.stderr.strip()[:500]}")]
    return [_LEVEL[f["severity"]](f["code"], f["message"], file=f["file"]) for f in report["findings"]]


def validate_structure(ig_root: str) -> list:
    """Run structural validation checks and return issues."""
    issues = []
    root = Path(ig_root)

    # Check required files
    if not (root / "sushi-config.yaml").is_file():
        issues.append(warning("DAK-001", "sushi-config.yaml not found"))

    if not (root / "ig.ini").is_file():
        issues.append(warning("DAK-002", "ig.ini not found"))

    # Validate BPMN files (input/bpmn/ and smart-base/**/processes/)
    issues.extend(validate_bpmn(ig_root))

    return issues


def main() -> None:
    ig_root = os.environ.get("DAK_IG_ROOT", ".")
    issues = validate_structure(ig_root)
    print(format_issues(issues))

    if has_errors(issues):
        print("❌ DAK structural validation found errors.")
        sys.exit(1)

    print("✅ DAK structural validation passed.")


if __name__ == "__main__":
    main()
