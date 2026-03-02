#!/usr/bin/env python3
"""
prune_branches.py – Remove deployed branch previews from the gh-pages branch.

Must be run with the current working directory set to the root of a checked-out
gh-pages branch (the workflow handles this via ``working-directory``).

Inputs are read exclusively from environment variables so that the values set
by GitHub Actions are never interpolated by the shell, eliminating the risk of
shell-metacharacter injection:

    PRUNE_CONFIRM         Must equal the literal string "CONFIRM".
    PRUNE_TARGET_BRANCH   Directory name under branches/ to remove.
                          Leave unset or empty to remove ALL deployed branches.

Security measures
-----------------
* Inputs come from env vars, not from ``sys.argv``, so shell expansion cannot
  occur regardless of what characters the GitHub Actions user typed.
* ``subprocess`` is always called with an explicit list of arguments and
  ``shell=False`` (the default); no string is ever passed to a shell.
* A fixed blocklist of git redirection env vars (``GIT_DIR``, ``GIT_WORK_TREE``,
  etc.) is stripped from every child-process environment so an attacker who
  manages to inject env vars cannot redirect git operations to unexpected paths.
* Path traversal is rejected both lexically (no ``..`` or path separators in the
  branch name) and canonically (``os.path.realpath`` must stay inside
  ``branches/``).
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys

# ── Constants ──────────────────────────────────────────────────────────────────

REQUIRED_BRANCH = "gh-pages"
BRANCHES_DIR = "branches"
EXPECTED_CONFIRM = "CONFIRM"
ORPHAN_BRANCH = "gh-pages-squashed"

# Git env vars that could redirect operations to unexpected locations.
# We strip these from every child-process environment so they cannot be
# injected from the outer environment.
GIT_ENV_BLOCKLIST: frozenset[str] = frozenset({
    "GIT_DIR",
    "GIT_WORK_TREE",
    "GIT_INDEX_FILE",
    "GIT_OBJECT_DIRECTORY",
    "GIT_ALTERNATE_OBJECT_DIRECTORIES",
    "GIT_EXEC_PATH",
    "GIT_CEILING_DIRECTORIES",
    "GIT_DISCOVERY_ACROSS_FILESYSTEM",
    "GIT_NAMESPACE",
    "GIT_CONFIG_NOSYSTEM",
    "GIT_CONFIG_COUNT",
    "GIT_CONFIG_KEY_0",
    "GIT_CONFIG_VALUE_0",
})

# ── Environment helpers ────────────────────────────────────────────────────────


def _safe_env() -> dict[str, str]:
    """Return the current process environment minus git-redirection variables."""
    return {k: v for k, v in os.environ.items() if k not in GIT_ENV_BLOCKLIST}


def read_env(name: str, default: str = "") -> str:
    """Read an environment variable as a plain string, stripped of whitespace.

    Reading from ``os.environ`` (rather than accepting values on ``sys.argv``)
    means the GitHub Actions runner sets the value without shell expansion.
    """
    return os.environ.get(name, default).strip()


# ── Git helpers ────────────────────────────────────────────────────────────────


def run_git(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    """Run git with an explicit argument list and a sanitised environment.

    ``shell=False`` (the default for ``subprocess.run``) is enforced implicitly
    by passing a list; shell metacharacters in any argument are treated as
    literals, not executed.
    """
    result = subprocess.run(
        ["git", *args],
        capture_output=True,
        text=True,
        env=_safe_env(),
    )
    if check and result.returncode != 0:
        _abort(
            f"git {' '.join(args)} failed (exit {result.returncode}):\n"
            + result.stderr.strip()
        )
    return result


# ── Output / error helpers ─────────────────────────────────────────────────────


def _abort(message: str, code: int = 1) -> None:
    print(f"❌ {message}", file=sys.stderr)
    sys.exit(code)


def _warn(message: str) -> None:
    print(f"⚠️  {message}")


def _ok(message: str) -> None:
    print(f"✅ {message}")


# ── Input validation ───────────────────────────────────────────────────────────


def validate_confirmation(value: str) -> None:
    """Abort unless *value* is the exact expected confirmation token."""
    if value != EXPECTED_CONFIRM:
        _abort(
            f'Safety gate: PRUNE_CONFIRM must be the literal string '
            f'"{EXPECTED_CONFIRM}". Received: "{value}".'
        )
    _ok("Confirmation accepted.")


def validate_current_branch() -> None:
    """Abort if the working tree is not checked out on gh-pages."""
    result = run_git("rev-parse", "--abbrev-ref", "HEAD")
    current = result.stdout.strip()
    if current != REQUIRED_BRANCH:
        _abort(
            f"Expected to be on '{REQUIRED_BRANCH}' but found '{current}'. "
            "This script must run inside a gh-pages checkout."
        )
    _ok(f"Confirmed: on branch '{current}'.")


def validate_branches_dir() -> bool:
    """Return True if ``branches/`` exists inside the cwd; exit(0) otherwise."""
    abs_cwd = os.path.realpath(os.getcwd())
    abs_branches = os.path.realpath(BRANCHES_DIR)

    # Canonical path of branches/ must sit directly inside the cwd.
    if os.path.commonpath([abs_cwd, abs_branches]) != abs_cwd:
        _abort("branches/ resolved outside the working directory – aborting.")

    if not os.path.isdir(abs_branches):
        _warn(f"No '{BRANCHES_DIR}/' directory found in gh-pages – nothing to prune.")
        sys.exit(0)

    _ok(f"'{BRANCHES_DIR}/' directory confirmed.")
    return True


def validate_target_branch(target: str) -> str:
    """Validate *target* and return its resolved absolute path.

    Rejects:
    * Names containing ``..``
    * Names containing OS path separators (``/``, and ``\\`` on Windows)
    * Names that resolve outside ``branches/`` after symlink expansion
    """
    if not target:
        _abort("validate_target_branch called with an empty name.")

    # Lexical check: must be a plain directory name with no traversal sequences.
    if (
        ".." in target
        or os.sep in target
        or (os.altsep is not None and os.altsep in target)
    ):
        _abort(
            f"Invalid branch name '{target}' – '..' and path separators "
            "are not allowed."
        )

    abs_branches = os.path.realpath(BRANCHES_DIR)
    candidate = os.path.realpath(os.path.join(BRANCHES_DIR, target))

    # Canonical check: resolved path must stay inside branches/.
    if os.path.commonpath([abs_branches, candidate]) != abs_branches:
        _abort(
            f"Resolved path for '{target}' escapes the branches/ directory – "
            "aborting."
        )

    if not os.path.isdir(candidate):
        available = _list_deployed_branches()
        lines = "\n".join(f"  • {b}" for b in available) if available else "  (none)"
        _abort(
            f"'branches/{target}' not found.\n\n"
            f"Available deployed branches:\n{lines}"
        )

    _ok(f"Target 'branches/{target}' confirmed.")
    return candidate


# ── Branch discovery ───────────────────────────────────────────────────────────


def _list_deployed_branches() -> list[str]:
    """Return sorted directory names directly inside ``branches/``."""
    if not os.path.isdir(BRANCHES_DIR):
        return []
    return sorted(
        entry
        for entry in os.listdir(BRANCHES_DIR)
        if os.path.isdir(os.path.join(BRANCHES_DIR, entry))
    )


def show_deployed_branches() -> list[str]:
    """Print the list of currently deployed branches and return it."""
    available = _list_deployed_branches()
    print(f"\nFound {len(available)} deployed branch(es):")
    for b in available:
        print(f"  • {b}")
    print()
    return available


# ── Prune actions ──────────────────────────────────────────────────────────────


def prune_target(target: str) -> None:
    """Remove the directory for a single deployed branch."""
    branch_path = validate_target_branch(target)
    print(f"Removing branches/{target} …")
    shutil.rmtree(branch_path)
    _ok(f"Removed 'branches/{target}'.")


def prune_all() -> None:
    """Remove the entire ``branches/`` directory."""
    abs_branches = os.path.realpath(BRANCHES_DIR)
    print(f"Removing '{BRANCHES_DIR}/' …")
    shutil.rmtree(abs_branches)
    _ok(f"Removed entire '{BRANCHES_DIR}/' directory.")


# ── History squash ─────────────────────────────────────────────────────────────


def squash_and_push(commit_message: str) -> None:
    """Replace the gh-pages history with a single squashed commit and force-push.

    Strategy: create a new orphan branch (no prior history) from the current
    working tree, then force-push it to ``origin/gh-pages``.  This removes all
    accumulated deployment commits, keeping the repository lean.
    """
    run_git("config", "user.name", "github-actions[bot]")
    run_git("config", "user.email", "github-actions[bot]@users.noreply.github.com")
    run_git("add", "-A")

    # Nothing staged?  Nothing to do.
    diff_result = run_git("diff", "--staged", "--quiet", check=False)
    if diff_result.returncode == 0:
        _warn("Nothing was staged – the repository is unchanged.")
        return

    # Orphan branch carries only the current tree, with no prior history.
    run_git("checkout", "--orphan", ORPHAN_BRANCH)
    run_git("add", "-A")
    run_git("commit", "-m", commit_message)

    # Atomically replace the local gh-pages ref and force-push.
    run_git("branch", "-D", REQUIRED_BRANCH)
    run_git("branch", "-m", REQUIRED_BRANCH)
    # Use HEAD:gh-pages to be explicit about source and destination refs.
    run_git("push", "--force", "origin", f"HEAD:{REQUIRED_BRANCH}")

    _ok("gh-pages history squashed and pushed.")
    print(f"   Commit message: {commit_message}")


# ── Entry point ────────────────────────────────────────────────────────────────


def main() -> None:
    # Read inputs from environment variables – NOT from sys.argv – so that the
    # values set by GitHub Actions are never processed by a shell and shell
    # metacharacters in the input cannot execute arbitrary commands.
    confirm = read_env("PRUNE_CONFIRM")
    target = read_env("PRUNE_TARGET_BRANCH")

    validate_confirmation(confirm)
    validate_current_branch()
    validate_branches_dir()
    show_deployed_branches()

    if target:
        prune_target(target)
        commit_msg = f"Prune: remove deployed branch preview for {target}"
    else:
        prune_all()
        commit_msg = "Prune: remove all deployed branch previews"

    squash_and_push(commit_msg)


if __name__ == "__main__":
    main()
