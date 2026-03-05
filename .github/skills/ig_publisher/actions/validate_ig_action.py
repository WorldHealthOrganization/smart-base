"""
IG Publisher validation action — runs the FHIR IG Publisher in validation mode.

Environment variables:
    GITHUB_TOKEN  — GitHub API token
    DAK_IG_ROOT   — IG root directory (default: current directory)
    DAK_TX_SERVER — Terminology server URL (optional; default: n/a for offline)
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
    tx_server = os.environ.get("DAK_TX_SERVER", "n/a")

    print(f"🏗️  Running IG Publisher validation (tx={tx_server})...")
    result = run_ig_publisher(ig_root, tx_server=tx_server)

    print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)

    if result.returncode != 0:
        print("❌ IG Publisher validation failed.")
        sys.exit(1)

    print("✅ IG Publisher validation passed.")


if __name__ == "__main__":
    main()
