"""
BPMN Author action — creates or edits BPMN files via LLM,
then validates the result structurally.

Environment variables:
    DAK_LLM_API_KEY  — LLM API key (optional; LLM steps skipped if absent)
    DAK_LLM_MODEL    — LLM model name (default: gpt-4o)
    GITHUB_TOKEN     — GitHub API token for issue/PR interaction
    ISSUE_NUMBER     — GitHub issue number
    ISSUE_TITLE      — Issue title
    ISSUE_BODY       — Issue body text
"""

import os
import sys
from pathlib import Path

# Ensure the skills root is on sys.path
_SKILLS_ROOT = Path(__file__).resolve().parent.parent.parent
if str(_SKILLS_ROOT) not in sys.path:
    sys.path.insert(0, str(_SKILLS_ROOT))

from common.ig_errors import format_issues, has_errors
from bpmn_author.validators.bpmn_xml_validator import validate_bpmn_xml
from bpmn_author.validators.swimlane_validator import validate_swimlanes


def main() -> None:
    api_key = os.environ.get("DAK_LLM_API_KEY", "")
    if not api_key:
        print("⚠️  DAK_LLM_API_KEY not set — LLM step skipped (structural validation still runs)")
        sys.exit(0)

    from common.smart_llm_facade import SmartLLMFacade
    from common.prompts import load_prompt

    issue_title = os.environ.get("ISSUE_TITLE", "")
    issue_body = os.environ.get("ISSUE_BODY", "")
    model = os.environ.get("DAK_LLM_MODEL", "gpt-4o")

    llm = SmartLLMFacade(api_key=api_key, model=model)

    prompt = load_prompt(
        "bpmn_author", "create_or_edit_bpmn",
        user_request=f"{issue_title}\n\n{issue_body}",
        current_bpmn="(none — creating new BPMN)",
    )

    print(f"🤖 Requesting BPMN from {model}...")
    bpmn_xml = llm.call(prompt)

    # Validate the generated BPMN
    issues = validate_bpmn_xml(bpmn_xml, filename="generated.bpmn")
    issues.extend(validate_swimlanes(bpmn_xml, filename="generated.bpmn"))

    print(format_issues(issues))

    if has_errors(issues):
        print("❌ Generated BPMN has validation errors.")
        sys.exit(1)

    print("✅ Generated BPMN passed structural validation.")


if __name__ == "__main__":
    main()
