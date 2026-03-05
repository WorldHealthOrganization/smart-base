"""
DAK L2 authoring action — processes content:L2 labeled issues.

Environment variables:
    DAK_LLM_API_KEY  — LLM API key (optional; LLM steps skipped if absent)
    DAK_LLM_MODEL    — LLM model name (default: gpt-4o)
    GITHUB_TOKEN     — GitHub API token
    ISSUE_NUMBER     — GitHub issue number
    ISSUE_TITLE      — Issue title
    ISSUE_BODY       — Issue body text
"""

import os
import sys
from pathlib import Path

_SKILLS_ROOT = Path(__file__).resolve().parent.parent.parent
if str(_SKILLS_ROOT) not in sys.path:
    sys.path.insert(0, str(_SKILLS_ROOT))


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
        "dak_authoring", "l2_authoring",
        issue_title=issue_title,
        issue_body=issue_body[:4000],
    )

    print(f"🤖 Planning L2 content changes with {model}...")
    result = llm.call(prompt, structured_output=True)

    print(f"Summary: {result.get('summary', 'N/A')}")
    for change in result.get("changes", []):
        print(f"  {change.get('action', '?')}: {change.get('file', '?')}")
        print(f"    {change.get('description', '')}")


if __name__ == "__main__":
    main()
