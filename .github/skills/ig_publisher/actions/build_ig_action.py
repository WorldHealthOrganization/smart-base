"""
IG Publisher build action — runs the full IG Publisher build.

Environment variables:
    GITHUB_TOKEN  — GitHub API token
    DAK_IG_ROOT   — IG root directory (default: current directory)
    DAK_TX_SERVER — Terminology server URL (optional)
"""

import os
import sys
from pathlib import Path

_SKILLS_ROOT = Path(__file__).resolve().parent.parent.parent
if str(_SKILLS_ROOT) not in sys.path:
    sys.path.insert(0, str(_SKILLS_ROOT))

from common.ig_publisher_iface import run_ig_publisher


def main() -> None:
    ig_root = os.environ.get("DAK_IG_ROOT", ".")
    tx_server = os.environ.get("DAK_TX_SERVER", "")

    print("🏗️  Running full IG Publisher build...")
    result = run_ig_publisher(ig_root, tx_server=tx_server or None)

    print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)

    if result.returncode != 0:
        print("❌ IG Publisher build failed.")
        sys.exit(1)

    print("✅ IG Publisher build completed successfully.")


if __name__ == "__main__":
    main()
