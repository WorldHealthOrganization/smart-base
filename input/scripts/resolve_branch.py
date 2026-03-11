#!/usr/bin/env python3
"""Resolve the effective branch name and deployment directory for a workflow run.

Reads GitHub context exclusively from environment variables so that
attacker-controlled values (branch names, refs) cannot be injected into
shell commands.

The branch name is resolved from GH_HEAD_REF (set on pull_request /
pull_request_target events) or GH_REF_NAME (fallback).  This is used only
for deployment directory naming — the code that is actually built is
controlled by the separate ``ref`` input to the checkout action.

Environment variables
---------------------
GH_HEAD_REF   ``github.head_ref`` — set on pull_request / pull_request_target events.
GH_REF_NAME   ``github.ref_name`` — always set by Actions.
GITHUB_ENV    Path to the file that receives ``KEY=VALUE`` environment exports.

Outputs (written to ``$GITHUB_ENV``)
------------------------------------
BRANCH_DIR    Last path component of the branch name (safe for use as a
              directory name under ``gh-pages/branches/``).
BRANCH_NAME   Full branch name with any ``refs/heads/`` prefix stripped.
"""

import os
import re
import sys

# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

# Same pattern used in run_ig_publisher.py
_SAFE_BRANCH_RE = re.compile(r"^[a-zA-Z0-9._/\-]+$")


def _read_env(name: str) -> str:
    """Return the stripped value of *name* from the environment."""
    return os.environ.get(name, "").strip()


def _sanitize_branch(value: str) -> str:
    """Validate a branch name against the safe character set.

    Raises ``ValueError`` for values containing shell metacharacters,
    path traversal sequences, or other unsafe patterns.
    """
    if not value:
        raise ValueError("Branch name is empty")
    # Strip refs/heads/ prefix if present
    value = re.sub(r"^refs/heads/", "", value)
    if not _SAFE_BRANCH_RE.match(value):
        raise ValueError(
            f"Unsafe branch name: {value!r}. "
            "Only alphanumerics and '.', '-', '/', '_' are allowed."
        )
    if value.startswith("-"):
        raise ValueError(
            f"Branch name must not start with a dash: {value!r}"
        )
    if ".." in value:
        raise ValueError(
            f"Branch name must not contain '..': {value!r}"
        )
    return value


def _branch_dir(branch: str) -> str:
    """Return the last path component, mirroring ``${ACTUAL_BRANCH##*/}``."""
    return branch.rsplit("/", 1)[-1]


# ---------------------------------------------------------------------------
# Output helper
# ---------------------------------------------------------------------------

def _set_env(name: str, value: str) -> None:
    """Append ``name=value`` to ``$GITHUB_ENV``."""
    env_file = os.environ.get("GITHUB_ENV", "")
    if env_file:
        with open(env_file, "a") as fh:
            fh.write(f"{name}={value}\n")
    print(f"{name}={value}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    head_ref = _read_env("GH_HEAD_REF")
    ref_name = _read_env("GH_REF_NAME")

    # Resolution order:
    #   1. GH_HEAD_REF (pull_request / pull_request_target — the PR branch name)
    #   2. GH_REF_NAME (fallback — the branch/tag that triggered the event)
    raw = head_ref or ref_name

    if not raw:
        print("⚠️  No branch information available — falling back to 'unknown'",
              file=sys.stderr)
        raw = "unknown"

    try:
        branch = _sanitize_branch(raw)
    except ValueError as exc:
        print(f"❌ {exc}", file=sys.stderr)
        sys.exit(1)

    bdir = _branch_dir(branch)
    _set_env("BRANCH_DIR", bdir)
    _set_env("BRANCH_NAME", branch)


if __name__ == "__main__":
    main()
