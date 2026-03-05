#!/usr/bin/env python3
"""
register_all_dak_projects.py — Bulk Weblate registration for all WHO SMART DAK repos.

Scans a list of GitHub repositories (one per line from a file or stdin),
checks each for a dak.json, and calls register_translation_project.py for
any that have one.

This is a maintenance utility for the WHO Weblate administrator; individual
IG repositories call register_translation_project.py directly from their CI.

Usage:
    python register_all_dak_projects.py --repos-file repos.txt
                                         [--weblate-url URL]
                                         [--github-token TOKEN_ENV_VAR]
                                         [--dry-run]

repos.txt format (one GitHub owner/repo per line, # = comment):
    WorldHealthOrganization/smart-base
    WorldHealthOrganization/smart-immunizations
    # WorldHealthOrganization/smart-example  # disabled

Environment variables:
    WEBLATE_ADMIN_TOKEN   Required Weblate admin API token.
    GITHUB_TOKEN          Optional GitHub token for higher API rate limits.

Exit codes:
    0  All projects registered (or skipped)
    1  One or more registration errors
    2  Bad arguments
"""

import argparse
import base64
import json
import logging
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import List, Optional, Tuple

try:
    import requests
except ImportError:
    sys.exit("ERROR: 'requests' package is required. Run: pip install requests>=2.31.0")

from translation_config import get_project_slug
from translation_security import get_optional_env_token

_GITHUB_API = "https://api.github.com"
_TIMEOUT = 30


def _fetch_dak_json(
    session: "requests.Session",
    owner: str,
    repo: str,
    ref: str = "HEAD",
) -> Optional[dict]:
    """
    Fetch dak.json from a GitHub repository via the API.
    Returns parsed JSON dict or None if not found.
    """
    url = f"{_GITHUB_API}/repos/{owner}/{repo}/contents/dak.json"
    params = {"ref": ref}
    try:
        resp = session.get(url, params=params, timeout=_TIMEOUT)
    except requests.RequestException as exc:
        logging.warning("Cannot reach GitHub API for %s/%s: %s", owner, repo, exc)
        return None

    if resp.status_code == 404:
        return None
    if resp.status_code != 200:
        logging.warning("HTTP %d fetching dak.json for %s/%s", resp.status_code, owner, repo)
        return None

    data = resp.json()
    try:
        content = base64.b64decode(data["content"]).decode("utf-8")
        return json.loads(content)
    except (KeyError, ValueError) as exc:
        logging.warning("Cannot parse dak.json for %s/%s: %s", owner, repo, exc)
        return None


def _repo_default_branch(
    session: "requests.Session",
    owner: str,
    repo: str,
) -> str:
    url = f"{_GITHUB_API}/repos/{owner}/{repo}"
    try:
        resp = session.get(url, timeout=_TIMEOUT)
        if resp.status_code == 200:
            return resp.json().get("default_branch", "main")
    except requests.RequestException:
        pass
    return "main"


def _run_registration(
    owner: str,
    repo: str,
    branch: str,
    weblate_url: str,
    dry_run: bool,
) -> int:
    """
    Invoke register_translation_project.py as a subprocess for a remote repo.
    """
    logger = logging.getLogger(__name__)
    import re as _re

    try:
        project_slug = get_project_slug(owner, repo)
    except Exception:
        raw = f"{owner}-{repo}".lower()
        project_slug = _re.sub(r"[^a-z0-9-]", "-", raw)

    repo_url = f"https://github.com/{owner}/{repo}"

    logger.info("Processing %s/%s → %s", owner, repo, project_slug)

    # Call the script via subprocess so each registration is isolated
    script = Path(__file__).parent / "register_translation_project.py"
    cmd = [
        sys.executable, str(script),
        "--weblate-url", weblate_url,
        "--project-slug", project_slug,
        "--repo-url", repo_url,
        "--branch", branch,
    ]
    if dry_run:
        cmd.append("--dry-run")

    env = os.environ.copy()
    env["GITHUB_REPOSITORY"] = f"{owner}/{repo}"
    env["GITHUB_REF_NAME"] = branch

    try:
        result = subprocess.run(cmd, env=env, timeout=120, check=False)
        return result.returncode
    except (subprocess.TimeoutExpired, OSError) as exc:
        logger.error("Failed to run registration for %s/%s: %s", owner, repo, exc)
        return 1


def _parse_repos_file(path: Path) -> List[Tuple[str, str]]:
    """Parse repos file and return list of (owner, repo) tuples."""
    repos = []
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        # Strip inline comment
        line = line.split("#")[0].strip()
        if "/" not in line:
            logging.warning("Skipping invalid repo line: %r", line)
            continue
        owner, repo = line.split("/", 1)
        repos.append((owner.strip(), repo.strip()))
    return repos


def _parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="register_all_dak_projects.py",
        description="Bulk-register WHO SMART DAK repositories in Weblate",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--repos-file",
        required=True,
        help="Path to a text file with one GitHub owner/repo per line",
    )
    parser.add_argument(
        "--weblate-url",
        default="https://hosted.weblate.org",
        help="Weblate base URL (default: https://hosted.weblate.org)",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Print actions without making API calls",
    )
    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
    )
    logger = logging.getLogger(__name__)
    args = _parse_args(argv)

    repos_file = Path(args.repos_file)
    if not repos_file.exists():
        sys.exit(f"ERROR: repos file not found: {repos_file}")

    repos = _parse_repos_file(repos_file)
    if not repos:
        logger.warning("No repositories found in %s", repos_file)
        return 0

    weblate_url = args.weblate_url.rstrip("/")

    if not args.dry_run:
        token = get_optional_env_token("WEBLATE_ADMIN_TOKEN")
        if not token:
            sys.exit(
                "ERROR: WEBLATE_ADMIN_TOKEN is not set.\n"
                "  Add it as a secret or environment variable."
            )

    # GitHub session (for checking dak.json existence)
    gh_session = requests.Session()
    gh_token = os.environ.get("GITHUB_TOKEN", "")
    if gh_token:
        gh_session.headers["Authorization"] = f"token {gh_token}"
    gh_session.headers["Accept"] = "application/vnd.github.v3+json"

    logger.info("Processing %d repositories", len(repos))
    errors = 0
    skipped = 0
    registered = 0

    for owner, repo in repos:
        logger.info("── Checking %s/%s ──", owner, repo)

        # Check if repo has dak.json
        dak = _fetch_dak_json(gh_session, owner, repo)
        if dak is None:
            logger.info("  No dak.json found — skipping")
            skipped += 1
            continue

        branch = _repo_default_branch(gh_session, owner, repo)
        rc = _run_registration(
            owner=owner,
            repo=repo,
            branch=branch,
            weblate_url=weblate_url,
            dry_run=args.dry_run,
        )
        if rc != 0:
            errors += 1
        else:
            registered += 1

    logger.info(
        "Done: %d registered, %d skipped (no dak.json), %d errors",
        registered, skipped, errors,
    )
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
