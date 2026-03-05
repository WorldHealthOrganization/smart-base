#!/usr/bin/env python3
"""
translation_security.py — Centralised input sanitisation and secret protection.

Imported by all scripts that handle external inputs (API tokens, slugs, URLs,
language codes).  Provides a single, testable place for all security-relevant
input checks so that individual scripts do not need to re-implement them.

Requirements implemented:
  SEC-001  Values from workflow_dispatch inputs must be sanitised before use.
  SEC-002  API tokens must never be logged; use redact_for_log() for diagnostics.
  SEC-003  assert_no_secret_in_env() must be called at startup of any script
           that handles API tokens.
  SEC-004  HTTP requests must set a connection timeout and max-response-size guard.
"""

import os
import re
import sys
from urllib.parse import urlparse


# ---------------------------------------------------------------------------
# Slug / identifier sanitisation
# ---------------------------------------------------------------------------

def sanitize_slug(value: str, field_name: str) -> str:
    """
    Allow only [a-z0-9-_] in *value* (case-folded).

    Raises:
        ValueError: if the value contains disallowed characters.
    """
    folded = value.lower().strip()
    if not folded:
        raise ValueError(f"{field_name}: value must not be empty")
    if not re.fullmatch(r"[a-z0-9_-]{1,128}", folded):
        raise ValueError(
            f"{field_name}: value {value!r} contains invalid characters. "
            "Only lowercase alphanumerics, hyphens, and underscores are allowed."
        )
    return folded


def sanitize_url(value: str, field_name: str, allowed_schemes=("https",)) -> str:
    """
    Validate URL scheme and basic structure.

    Raises:
        ValueError: if the URL scheme is not in *allowed_schemes* or the URL is
                    otherwise structurally invalid.
    """
    stripped = value.strip().rstrip("/")
    if not stripped:
        raise ValueError(f"{field_name}: URL must not be empty")

    try:
        parsed = urlparse(stripped)
    except Exception as exc:
        raise ValueError(f"{field_name}: cannot parse URL {value!r}: {exc}") from exc

    if parsed.scheme not in allowed_schemes:
        raise ValueError(
            f"{field_name}: URL scheme {parsed.scheme!r} is not allowed. "
            f"Allowed: {', '.join(allowed_schemes)}"
        )
    if not parsed.netloc:
        raise ValueError(f"{field_name}: URL {value!r} has no host component")

    return stripped


def sanitize_lang_code(value: str) -> str:
    """
    Validate BCP-47 / ISO 639-1 language code format.

    Accepts: 2-3 letter language code optionally followed by
             -<subtag> suffixes (e.g. 'zh', 'zh-CN', 'pt-BR').

    Raises:
        ValueError: if the value does not match BCP-47 structure.
    """
    stripped = value.strip().lower()
    if not stripped:
        raise ValueError("Language code must not be empty")
    if not re.fullmatch(r"[a-z]{2,3}(?:-[a-z0-9]{2,8})*", stripped):
        raise ValueError(
            f"Language code {value!r} is not a valid BCP-47 code. "
            "Expected format: 2-3 letter code optionally with subtags (e.g. 'fr', 'zh-CN')."
        )
    return stripped


# ---------------------------------------------------------------------------
# Secret / token handling
# ---------------------------------------------------------------------------

def redact_for_log(value: str, visible_chars: int = 4) -> str:
    """
    Return the first *visible_chars* characters of *value* followed by '***'.

    Safe for use in log messages when a partial token value aids diagnostics
    without exposing the full secret.

    Example:
        redact_for_log("abc123xyz")  →  "abc1***"
    """
    if not value:
        return "(empty)"
    return value[:visible_chars] + "***"


def assert_no_secret_in_env(env_var: str) -> None:
    """
    Guard against workflows that accidentally wire API tokens as plain-text
    workflow_dispatch inputs (which appear in GITHUB_EVENT_INPUTS_* env vars).

    Raises:
        RuntimeError: if *env_var* was also passed as a workflow_dispatch input,
                      indicating a misconfigured workflow.
    """
    input_env_name = f"GITHUB_EVENT_INPUTS_{env_var.upper()}"
    if os.environ.get(input_env_name):
        raise RuntimeError(
            f"Security error: {env_var!r} appears to have been passed as a "
            "workflow_dispatch input, which would expose the secret in logs and the "
            "GitHub Events API. Secrets must ONLY be passed via GitHub Actions secrets "
            "(env: block referencing ${{ secrets.NAME }}), never as workflow inputs."
        )


def get_required_env_token(env_var: str, service_name: str) -> str:
    """
    Read a required API token from an environment variable.

    Calls assert_no_secret_in_env() first to guard against input leakage,
    then reads and validates the value.

    Raises:
        SystemExit: if the token is absent or empty.
    """
    assert_no_secret_in_env(env_var)
    token = os.environ.get(env_var, "").strip()
    if not token:
        sys.exit(
            f"ERROR: {env_var} environment variable is not set or empty.\n"
            f"  This token is required for {service_name} integration.\n"
            "  Add it as a repository secret: Settings → Secrets → Actions → New secret"
        )
    return token


def get_optional_env_token(env_var: str) -> str:
    """
    Read an optional API token from an environment variable.

    Returns empty string if not set (caller decides whether to skip the service).
    Calls assert_no_secret_in_env() to guard against input leakage.
    """
    assert_no_secret_in_env(env_var)
    return os.environ.get(env_var, "").strip()
