#!/usr/bin/env python3
"""Orchestrate deploy-metadata stamping across all build phases.

This script replaces the inline shell logic that previously lived in
ghbuild.yml's "Stamp deploy metadata" step.  It:

1. Optionally downloads ``stamp_deploy_metadata.py`` if not present locally.
2. Fetches the previously deployed ``index.html`` for cross-build log
   accumulation.
3. Calls ``stamp_deploy_metadata.py`` once for each build phase.

All GitHub context is read from environment variables — never interpolated
into shell commands — to prevent script injection.

Environment variables
---------------------
GH_SHA              Full commit SHA.
BRANCH_DIR          Deployment directory name (last path segment of branch).
GITHUB_REPOSITORY   ``owner/repo`` format.
TS_CHECKOUT         ISO-8601 timestamp recorded at checkout (optional).
TS_IG_BUILD         ISO-8601 timestamp recorded after IG build (optional).

Arguments
---------
html_file           Path to the HTML file to stamp (e.g. ``output/index.html``).
"""

import os
import re
import subprocess
import sys
import urllib.request
from datetime import datetime, timezone

# ---------------------------------------------------------------------------
# Validation helpers
# ---------------------------------------------------------------------------

_SAFE_HEX_RE = re.compile(r"^[0-9a-fA-F]+$")
_SAFE_BRANCH_RE = re.compile(r"^[a-zA-Z0-9._/\-]+$")
_SAFE_REPO_RE = re.compile(r"^[a-zA-Z0-9._\-]+/[a-zA-Z0-9._\-]+$")

_STAMP_SCRIPT = "input/scripts/stamp_deploy_metadata.py"
_STAMP_URL = (
    "https://raw.githubusercontent.com/WorldHealthOrganization/"
    "smart-base/main/input/scripts/stamp_deploy_metadata.py"
)

# Build phases to stamp, in order.  Each phase has a name and an optional
# environment variable holding the timestamp.
_PHASES = [
    ("checkout",       "TS_CHECKOUT"),
    ("ig-build",       "TS_IG_BUILD"),
    ("postprocessing", None),
    ("pre-deploy",     None),
]


def _read_env(name: str) -> str:
    return os.environ.get(name, "").strip()


def _validate_sha(value: str) -> str:
    if not value:
        raise ValueError("GH_SHA is empty")
    if not _SAFE_HEX_RE.match(value):
        raise ValueError(f"Unsafe commit SHA: {value!r}")
    return value


def _validate_branch_dir(value: str) -> str:
    if not value:
        raise ValueError("BRANCH_DIR is empty")
    if not _SAFE_BRANCH_RE.match(value):
        raise ValueError(f"Unsafe BRANCH_DIR: {value!r}")
    if ".." in value or "/" in value:
        raise ValueError(f"BRANCH_DIR must not contain '..' or '/': {value!r}")
    if value.startswith("-"):
        raise ValueError(f"BRANCH_DIR must not start with '-': {value!r}")
    return value


def _validate_repo(value: str) -> str:
    if not value:
        raise ValueError("GITHUB_REPOSITORY is empty")
    if not _SAFE_REPO_RE.match(value):
        raise ValueError(f"Unsafe GITHUB_REPOSITORY: {value!r}")
    return value


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _ensure_stamp_script() -> bool:
    """Download stamp_deploy_metadata.py if not present.  Return True on success."""
    if os.path.isfile(_STAMP_SCRIPT):
        return True
    print(f"Downloading {_STAMP_SCRIPT} from smart-base...")
    os.makedirs(os.path.dirname(_STAMP_SCRIPT), exist_ok=True)
    try:
        urllib.request.urlretrieve(_STAMP_URL, _STAMP_SCRIPT)
        return True
    except Exception as exc:
        print(f"⚠️  Could not download stamp script: {exc}", file=sys.stderr)
        return False


def _fetch_prev_html(repo: str, branch_dir: str) -> str | None:
    """Download the previously deployed index.html.  Return local path or None."""
    url = (
        f"https://raw.githubusercontent.com/{repo}"
        f"/gh-pages/branches/{branch_dir}/index.html"
    )
    dest = "/tmp/prev-deploy-index.html"
    try:
        urllib.request.urlretrieve(url, dest)
        print(f"Found previous deployment log for branch {branch_dir}")
        return dest
    except Exception:
        print(f"No previous deployment found for branch {branch_dir} – starting fresh log")
        return None


def _now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _stamp(html_file: str, step: str, commit: str, branch: str,
           timestamp: str, prev_html: str | None = None) -> None:
    """Call stamp_deploy_metadata.py for one phase."""
    cmd = [
        sys.executable, _STAMP_SCRIPT, html_file,
        "--step", step,
        "--commit", commit,
        "--branch", branch,
        "--timestamp", timestamp,
    ]
    if prev_html:
        cmd += ["--prev-html", prev_html]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout, end="")
    if result.returncode != 0 and result.stderr:
        print(result.stderr, end="", file=sys.stderr)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: stamp_deploy.py <html_file>", file=sys.stderr)
        sys.exit(1)

    html_file = sys.argv[1]

    if not os.path.isfile(html_file):
        print(f"output/index.html not found – skipping metadata stamp")
        return

    # Validate all environment inputs
    try:
        commit = _validate_sha(_read_env("GH_SHA"))
        branch_dir = _validate_branch_dir(_read_env("BRANCH_DIR"))
        repo = _validate_repo(_read_env("GITHUB_REPOSITORY"))
    except ValueError as exc:
        print(f"❌ {exc}", file=sys.stderr)
        sys.exit(1)

    # Ensure the stamp helper script is available
    if not _ensure_stamp_script():
        return

    # Make sure file is writable
    try:
        os.chmod(html_file, 0o666)
    except OSError:
        pass

    # Fetch previous deployment for cross-build log accumulation
    prev_html = _fetch_prev_html(repo, branch_dir)

    # Stamp each phase
    for i, (phase, ts_env) in enumerate(_PHASES):
        ts = (_read_env(ts_env) if ts_env else "") or _now_utc()
        # Only the first phase carries forward the previous HTML
        _stamp(html_file, phase, commit, branch_dir, ts,
               prev_html if i == 0 else None)

    print("✅ Deploy metadata stamped in", html_file)


if __name__ == "__main__":
    main()
