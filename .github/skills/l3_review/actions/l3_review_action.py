"""
L3 review action — placeholder for implementation adaptation review skill.

This skill will be implemented in a future version.
"""

import os
import sys


def main() -> None:
    api_key = os.environ.get("DAK_LLM_API_KEY", "")
    if not api_key:
        print("⚠️  DAK_LLM_API_KEY not set — LLM step skipped")
        sys.exit(0)

    print("ℹ️  L3 review skill is not yet implemented (planned for v0.3)")
    sys.exit(0)


if __name__ == "__main__":
    main()
