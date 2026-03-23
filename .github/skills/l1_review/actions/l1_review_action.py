"""
L1 review action — placeholder for WHO source guideline review skill.

This skill will be implemented in a future version.
"""

import os
import sys


def main() -> None:
    api_key = os.environ.get("DAK_LLM_API_KEY", "")
    if not api_key:
        print("⚠️  DAK_LLM_API_KEY not set — LLM step skipped")
        sys.exit(0)

    print("ℹ️  L1 review skill is not yet implemented (planned for v0.2)")
    sys.exit(0)


if __name__ == "__main__":
    main()
