"""
IG Publisher interface — thin wrapper for invoking the FHIR IG Publisher.

Uses the existing ``input/scripts/run_ig_publisher.py`` when available, or
falls back to running the publisher JAR directly.
"""

import logging
import os
import subprocess
import sys
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)


def run_ig_publisher(
    ig_root: Optional[str] = None,
    *,
    tx_server: Optional[str] = None,
    extra_args: Optional[list] = None,
) -> subprocess.CompletedProcess:
    """Run the FHIR IG Publisher.

    Args:
        ig_root: Path to the IG root directory. Defaults to ``DAK_IG_ROOT``
                 env var or current working directory.
        tx_server: Terminology server URL.  Pass ``"n/a"`` for offline builds.
        extra_args: Additional CLI arguments for the publisher.

    Returns:
        CompletedProcess with return code, stdout, and stderr.
    """
    ig_root = ig_root or os.environ.get("DAK_IG_ROOT", ".")
    ig_root_path = Path(ig_root)

    # Prefer the repo's own runner script if present
    runner_script = ig_root_path / "input" / "scripts" / "run_ig_publisher.py"
    use_python_runner = runner_script.is_file()
    if use_python_runner:
        cmd = [sys.executable, str(runner_script)]
    else:
        jar = os.environ.get(
            "PUBLISHER_JAR",
            str(ig_root_path / "input-cache" / "publisher.jar"),
        )
        cmd = ["java", "-jar", jar, "-ig", str(ig_root_path)]

    if tx_server:
        # run_ig_publisher.py uses argparse (--tx); the Java JAR uses -tx
        tx_flag = "--tx" if use_python_runner else "-tx"
        cmd.extend([tx_flag, tx_server])
    if extra_args:
        cmd.extend(extra_args)

    logger.info("Running IG Publisher: %s", " ".join(cmd))
    return subprocess.run(cmd, capture_output=True, text=True, cwd=str(ig_root_path))
