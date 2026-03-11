#!/usr/bin/env python3
"""Determine the pull-request number associated with the current workflow run.

Reads GitHub context exclusively from environment variables (never from CLI
arguments or shell-interpolated expressions) so that attacker-controlled
values such as branch names cannot be used for script injection.

Environment variables
---------------------
GH_EVENT_NAME   GitHub event type (e.g. "pull_request", "push").
GH_EVENT_NUMBER PR number when ``GH_EVENT_NAME == "pull_request"``.
GH_REF_NAME     Branch or tag name (used to look up a PR on "push").
GH_TOKEN        GitHub API token for ``gh`` CLI calls.
GITHUB_OUTPUT   Path to the file that receives step outputs.

Outputs (written to ``$GITHUB_OUTPUT``)
---------------------------------------
PR_NUMBER  The numeric PR number, or empty.
IS_PR      ``"true"`` if a PR was found, ``"false"`` otherwise.
"""

import os
import re
import subprocess
import sys

# ---------------------------------------------------------------------------
# Validation helpers
# ---------------------------------------------------------------------------

_SAFE_REF_RE = re.compile(r"^[a-zA-Z0-9._/\-]+$")
_SAFE_EVENT_NAMES = frozenset({
    "branch_protection_rule", "check_run", "check_suite", "create",
    "delete", "deployment", "deployment_status", "discussion",
    "discussion_comment", "fork", "gollum", "issue_comment", "issues",
    "label", "merge_group", "milestone", "page_build", "public",
    "pull_request", "pull_request_review", "pull_request_review_comment",
    "pull_request_target", "push", "registry_package", "release",
    "repository_dispatch", "schedule", "status", "watch", "workflow_call",
    "workflow_dispatch", "workflow_run",
})


def _read_env(name: str) -> str:
    """Return the value of *name* from the environment, stripped."""
    return os.environ.get(name, "").strip()


def _validate_event_name(value: str) -> str:
    if value not in _SAFE_EVENT_NAMES:
        raise ValueError(f"Unexpected event name: {value!r}")
    return value


def _validate_pr_number(value: str) -> int:
    """Return a validated integer PR number, or raise."""
    try:
        num = int(value)
    except (ValueError, TypeError):
        raise ValueError(f"Invalid PR number: {value!r}")
    if num <= 0 or num > 999_999:
        raise ValueError(f"PR number out of bounds: {num}")
    return num


def _validate_ref_name(value: str) -> str:
    if not value:
        return ""
    if not _SAFE_REF_RE.match(value):
        raise ValueError(
            f"Unsafe ref name: {value!r}. "
            "Only alphanumerics and '.', '-', '/', '_' are allowed."
        )
    if value.startswith("-"):
        raise ValueError(f"Ref name must not start with a dash: {value!r}")
    return value


# ---------------------------------------------------------------------------
# Output helper
# ---------------------------------------------------------------------------

def _set_output(name: str, value: str) -> None:
    """Append ``name=value`` to ``$GITHUB_OUTPUT``."""
    output_file = os.environ.get("GITHUB_OUTPUT", "")
    if output_file:
        with open(output_file, "a") as fh:
            fh.write(f"{name}={value}\n")
    # Also print for local debugging
    print(f"{name}={value}")


# ---------------------------------------------------------------------------
# Core logic
# ---------------------------------------------------------------------------

def _find_pr_for_push(ref_name: str, token: str) -> str:
    """Use the ``gh`` CLI to find a PR whose head matches *ref_name*.

    Returns the PR number as a string, or empty string if none found.
    All values are passed as explicit subprocess arguments (``shell=False``)
    so that metacharacters in the ref name cannot escape.
    """
    if not ref_name:
        return ""
    try:
        result = subprocess.run(
            ["gh", "pr", "list",
             "--head", ref_name,
             "--json", "number",
             "--jq", ".[0].number"],
            capture_output=True,
            text=True,
            timeout=30,
            env={**os.environ, "GH_TOKEN": token},
        )
        pr_num = result.stdout.strip()
        if pr_num and pr_num != "null":
            # Final validation – must be a plain integer
            _validate_pr_number(pr_num)
            return pr_num
    except (subprocess.SubprocessError, ValueError):
        pass
    return ""


def main() -> None:
    event_name = _read_env("GH_EVENT_NAME")
    event_number = _read_env("GH_EVENT_NUMBER")
    ref_name = _read_env("GH_REF_NAME")
    token = _read_env("GH_TOKEN")

    try:
        event_name = _validate_event_name(event_name)
    except ValueError as exc:
        print(f"⚠️  {exc} — treating as non-PR event", file=sys.stderr)
        _set_output("IS_PR", "false")
        return

    if event_name == "pull_request":
        try:
            pr_number = _validate_pr_number(event_number)
            _set_output("PR_NUMBER", str(pr_number))
            _set_output("IS_PR", "true")
        except ValueError as exc:
            print(f"⚠️  {exc}", file=sys.stderr)
            _set_output("IS_PR", "false")
        return

    if event_name == "push":
        try:
            ref_name = _validate_ref_name(ref_name)
        except ValueError as exc:
            print(f"⚠️  {exc}", file=sys.stderr)
            _set_output("IS_PR", "false")
            return

        pr_num = _find_pr_for_push(ref_name, token)
        if pr_num:
            _set_output("PR_NUMBER", pr_num)
            _set_output("IS_PR", "true")
        else:
            _set_output("IS_PR", "false")
        return

    # Any other event type
    _set_output("IS_PR", "false")


if __name__ == "__main__":
    main()
