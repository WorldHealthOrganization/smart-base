#!/usr/bin/env python3
"""
translation_security.py — Centralised input sanitisation and secret protection
for all translation-related scripts.

Imported by any script that handles external inputs (API tokens, slugs, URLs,
language codes) to enforce consistent security policies.

Key principles:
  - All values received from environment variables that originated from
    workflow_dispatch inputs MUST be sanitised before use.
  - API tokens MUST NEVER be logged, echoed, or included in exception messages.
  - HTTP requests MUST use connection timeouts and response-size guards.

Author: WHO SMART Guidelines Team
"""

import logging
import os
import re
from urllib.parse import urlparse

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

#: Default connection timeout for HTTP requests (seconds).
DEFAULT_TIMEOUT_SECONDS = 60

#: Maximum response body size (bytes) — 10 MiB.
MAX_RESPONSE_BYTES = 10 * 1024 * 1024

#: Pattern for valid slug values (component names, project names, etc.).
_SLUG_PATTERN = re.compile(r"^[a-z0-9][a-z0-9_-]{0,127}$")

#: Pattern for valid BCP-47 language codes (simplified: 2-3 letter codes with
#  optional subtag).
_LANG_CODE_PATTERN = re.compile(r"^[a-z]{2,3}(-[A-Za-z0-9]{1,8})*$")


# ---------------------------------------------------------------------------
# Sanitisation functions
# ---------------------------------------------------------------------------

def sanitize_slug(value: str, field_name: str) -> str:
    """
    Validate and return a slug string (lowercase alphanumeric + hyphens/underscores).

    Args:
        value: The value to validate.
        field_name: Human-readable field name for error messages.

    Raises:
        ValueError: if the value does not match the expected pattern.
    """
    cleaned = value.strip().lower()
    if not _SLUG_PATTERN.match(cleaned):
        raise ValueError(
            f"Invalid {field_name}: {cleaned!r}. "
            "Only lowercase alphanumerics, hyphens, and underscores are allowed "
            "(1-128 characters, must start with alphanumeric)."
        )
    return cleaned


def sanitize_url(
    value: str,
    field_name: str,
    allowed_schemes: tuple = ("https",),
) -> str:
    """
    Validate URL scheme and structure.

    Args:
        value: The URL to validate.
        field_name: Human-readable field name for error messages.
        allowed_schemes: Tuple of allowed URL schemes.

    Raises:
        ValueError: if the URL scheme or structure is invalid.
    """
    cleaned = value.strip().rstrip("/")
    parsed = urlparse(cleaned)

    if parsed.scheme not in allowed_schemes:
        raise ValueError(
            f"Invalid {field_name}: scheme {parsed.scheme!r} not in "
            f"allowed schemes {allowed_schemes}."
        )

    if not parsed.netloc:
        raise ValueError(
            f"Invalid {field_name}: no hostname found in {cleaned!r}."
        )

    return cleaned


def sanitize_lang_code(value: str) -> str:
    """
    Validate a BCP-47 language code format.

    Args:
        value: The language code to validate.

    Raises:
        ValueError: if the value is not a valid language code.
    """
    cleaned = value.strip()
    if not _LANG_CODE_PATTERN.match(cleaned):
        raise ValueError(
            f"Invalid language code: {cleaned!r}. "
            "Expected BCP-47 format (e.g. 'en', 'fr', 'zh-Hans')."
        )
    return cleaned


def redact_for_log(value: str, visible_chars: int = 4) -> str:
    """
    Return a redacted version of a value for safe log output.

    Shows only the first N characters followed by '***'.

    Args:
        value: The value to redact.
        visible_chars: Number of leading characters to show.

    Returns:
        Redacted string, e.g. 'wlu_***'.
    """
    if not value:
        return "(empty)"
    if len(value) <= visible_chars:
        return "***"
    return value[:visible_chars] + "***"


def assert_no_secret_in_env(env_var: str) -> None:
    """
    Guard against accidentally passing secret values as workflow_dispatch inputs.

    GitHub Actions workflow_dispatch inputs are available as
    `GITHUB_EVENT_INPUTS_<name>` environment variables (uppercased, with hyphens
    replaced by underscores). This function checks whether the given env var
    name matches any event input, which would indicate a misconfigured workflow
    that passes a secret as a plaintext input.

    Args:
        env_var: The environment variable name that holds a secret.

    Raises:
        RuntimeError: if the secret appears to have been passed as a workflow input.
    """
    # Check for the GITHUB_EVENT_PATH to inspect inputs
    event_path = os.environ.get("GITHUB_EVENT_PATH", "")
    if not event_path:
        return  # Not running in GitHub Actions

    # Normalise: TOKEN_NAME → token_name
    normalised = env_var.lower().replace("-", "_")

    # Check all env vars for the GITHUB_EVENT_INPUTS_ prefix pattern
    inputs_prefix = "INPUT_"
    for key in os.environ:
        if key.startswith(inputs_prefix):
            input_name = key[len(inputs_prefix):].lower().replace("-", "_")
            if input_name == normalised:
                raise RuntimeError(
                    f"Security violation: {env_var!r} appears to be passed as a "
                    f"workflow_dispatch input ({key}). Secrets MUST be configured "
                    "as GitHub Actions secrets, never as workflow inputs."
                )
