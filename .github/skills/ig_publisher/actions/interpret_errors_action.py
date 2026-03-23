"""
IG Publisher error interpretation action — uses LLM to explain build errors.

Environment variables:
    DAK_LLM_API_KEY  — LLM API key (skipped if absent)
    DAK_LLM_MODEL    — LLM model name (default: gpt-4o-mini)
    GITHUB_TOKEN     — GitHub API token
    PR_NUMBER        — PR number for posting results
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

    from common.llm_utils import dak_completion
    from common.prompt_loader import load_prompt

    model = os.environ.get("DAK_LLM_MODEL", "gpt-4o-mini")

    # Read build output from previous step (passed via file or env)
    build_output = os.environ.get("BUILD_OUTPUT", "No build output available.")

    prompt = load_prompt(
        "ig_publisher", "interpret_ig_errors",
        build_output=build_output[:8000],
        error_summary="See build output above.",
    )

    print(f"🤖 Interpreting errors with {model}...")
    result = dak_completion(prompt, structured_output=True, api_key=api_key, model=model)

    print(f"Summary: {result.get('summary', 'N/A')}")
    for finding in result.get("findings", []):
        print(f"  [{finding.get('severity')}] {finding.get('message')}")
        print(f"    Fix: {finding.get('fix')}")


if __name__ == "__main__":
    main()
