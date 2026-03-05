#!/usr/bin/env python3
"""
pull_weblate_translations.py — Download .po translation files from Weblate API.

Fetches the latest approved Gettext .po files for every (component, language)
combination from the Weblate REST API and writes them into the repository's
translations directories.

Components are discovered dynamically by scanning for *.pot files in the
repository (via translation_config.discover_components).  Languages are read
from dak.json#translations.languages.  Both fall back to built-in defaults
when dak.json is absent.

Usage:
    python pull_weblate_translations.py [options]

Options:
    --weblate-url URL    Weblate base URL  (default: https://hosted.weblate.org)
    --project SLUG       Weblate project slug (default: derived from GITHUB_REPOSITORY)
    --component SLUG     Restrict to one component slug (default: all)
    --language CODE      Restrict to one language code  (default: all)
    --output-root DIR    Repository root for output directories (default: .)
    -h / --help          Show this help message

Environment variables:
    WEBLATE_API_TOKEN    Optional. When absent the script exits 0 (skip).
    GITHUB_REPOSITORY    Optional. Used to derive the default project slug.

Exit codes:
    0  All expected files downloaded successfully, no token (skipped), or no
       matching translations
    1  One or more download errors occurred
    2  Bad arguments
"""

import argparse
import logging
import os
import sys
import tempfile
from pathlib import Path
from typing import Dict, List, Optional, Tuple

try:
    import requests
    from requests import Response
except ImportError:  # pragma: no cover
    sys.exit("ERROR: 'requests' package is required. Run: pip install requests>=2.31.0")

from translation_config import (
    DakConfigError,
    discover_components,
    get_language_codes,
    get_project_slug,
    load_dak_config,
)
from translation_security import get_optional_env_token, sanitize_slug, sanitize_url

# ---------------------------------------------------------------------------
# Fallback constants (used when dak.json or *.pot files are absent)
# ---------------------------------------------------------------------------

# Six UN official non-English languages — fallback when dak.json is absent.
_FALLBACK_LANGUAGES: Tuple[str, ...] = ("ar", "zh", "fr", "ru", "es")

# Weblate API path template for downloading a single translation file.
# Reference: https://docs.weblate.org/en/latest/api.html#get--api-translations-(string-project)-(string-component)-(string-language)-file-
_API_FILE_PATH = "/api/translations/{project}/{component}/{language}/file/"

# Maximum bytes we accept as a .po file (10 MiB) — protects against runaway
# downloads from a misconfigured or malicious server.
_MAX_PO_BYTES = 10 * 1024 * 1024

# Timeout in seconds for each Weblate API request.
_DOWNLOAD_TIMEOUT_SECONDS = 60

# ---------------------------------------------------------------------------
# Input validation helpers
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Input validation helpers (thin wrappers around translation_security)
# ---------------------------------------------------------------------------

def _validate_slug(value: str, name: str) -> str:
    try:
        return sanitize_slug(value, name)
    except ValueError as exc:
        sys.exit(f"ERROR: {exc}")


def _validate_url(value: str, name: str) -> str:
    try:
        return sanitize_url(value, name, allowed_schemes=("https", "http"))
    except ValueError as exc:
        sys.exit(f"ERROR: {exc}")



# ---------------------------------------------------------------------------
# Download logic
# ---------------------------------------------------------------------------

def _is_valid_po_content(content: bytes) -> bool:
    """Return True if *content* looks like a Gettext .po / .pot file."""
    # A valid .po file must contain at least one msgid declaration.
    return b"msgid" in content


def download_translation(
    session: "requests.Session",
    weblate_url: str,
    project: str,
    component: str,
    language: str,
    output_dir: Path,
) -> str:
    """
    Download the .po file for one (component, language) pair from Weblate.

    Args:
        session:      Authenticated requests.Session.
        weblate_url:  Weblate base URL (no trailing slash).
        project:      Weblate project slug.
        component:    Weblate component slug.
        language:     BCP-47 language code.
        output_dir:   Repository directory in which to write <language>.po.

    Returns:
        One of: "downloaded", "not_found", "skipped", "error"
    """
    logger = logging.getLogger(__name__)

    api_path = _API_FILE_PATH.format(
        project=project, component=component, language=language
    )
    # force Gettext PO format regardless of the component's storage type
    url = f"{weblate_url}{api_path}?format=po"

    logger.info("  GET %s", url)

    try:
        resp: Response = session.get(url, timeout=_DOWNLOAD_TIMEOUT_SECONDS, stream=True)
    except requests.exceptions.RequestException as exc:
        logger.error("  Network error: %s", exc)
        return "error"

    if resp.status_code == 404:
        logger.info("  Not found (404) — no translation exists yet")
        return "not_found"

    if resp.status_code != 200:
        logger.error("  Unexpected HTTP %d", resp.status_code)
        return "error"

    # Stream response into a temp file to avoid unbounded memory use
    output_dir.mkdir(parents=True, exist_ok=True)
    dest_path = output_dir / f"{language}.po"

    try:
        with tempfile.NamedTemporaryFile(
            dir=output_dir, suffix=".po.tmp", delete=False
        ) as tmp_fh:
            tmp_path = Path(tmp_fh.name)
            total = 0
            for chunk in resp.iter_content(chunk_size=65536):
                total += len(chunk)
                if total > _MAX_PO_BYTES:
                    logger.error(
                        "  Response exceeds %d bytes — aborting download", _MAX_PO_BYTES
                    )
                    tmp_path.unlink(missing_ok=True)
                    return "error"
                tmp_fh.write(chunk)
    except OSError as exc:
        logger.error("  Cannot write to %s: %s", output_dir, exc)
        tmp_path.unlink(missing_ok=True)
        return "error"

    # Validate content before accepting
    content = tmp_path.read_bytes()
    if not _is_valid_po_content(content):
        logger.warning("  Response body is not a valid .po file — skipping")
        tmp_path.unlink(missing_ok=True)
        return "skipped"

    tmp_path.replace(dest_path)
    logger.info("  ✓ Written to %s (%d bytes)", dest_path, total)
    return "downloaded"


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------

def pull_translations(
    weblate_url: str,
    project: str,
    output_root: Path,
    component_filter: Optional[str],
    language_filter: Optional[str],
    api_token: str,
) -> int:
    """
    Pull .po files from Weblate for every applicable (component, language) pair.

    Components are discovered by scanning *output_root* for *.pot files.
    Languages come from dak.json#translations.languages (falls back to UN 6).

    Returns:
        0 on full success, 1 if any download produced an error.
    """
    logger = logging.getLogger(__name__)

    # ── Resolve language list ────────────────────────────────────────────────
    try:
        config = load_dak_config(output_root)
        lang_codes = get_language_codes(config)
        if not lang_codes:
            lang_codes = list(_FALLBACK_LANGUAGES)
            logger.info("No languages in dak.json — using UN fallback: %s", lang_codes)
    except DakConfigError as exc:
        lang_codes = list(_FALLBACK_LANGUAGES)
        logger.info("dak.json unavailable (%s) — using UN fallback languages", exc)

    # ── Resolve component list ───────────────────────────────────────────────
    discovered = discover_components(output_root)
    if not discovered:
        logger.warning("No *.pot files found under %s — nothing to pull", output_root)
        return 0
    # Build {slug: translations_dir} map
    component_map: Dict[str, Path] = {c.slug: c.translations_dir for c in discovered}

    # ── Apply filters ────────────────────────────────────────────────────────
    if component_filter:
        if component_filter not in component_map:
            logger.error(
                "Unknown component %r. Discovered components: %s",
                component_filter,
                ", ".join(sorted(component_map)),
            )
            return 1
        active_components = {component_filter: component_map[component_filter]}
    else:
        active_components = dict(component_map)

    if language_filter:
        if language_filter not in lang_codes:
            logger.error(
                "Unknown language %r. Configured languages: %s",
                language_filter,
                ", ".join(lang_codes),
            )
            return 1
        active_languages: List[str] = [language_filter]
    else:
        active_languages = lang_codes

    # ── HTTP session ─────────────────────────────────────────────────────────
    session = requests.Session()
    session.headers.update(
        {
            # Weblate uses the "Token <token>" authorization scheme
            # (not "Bearer"), as documented at:
            # https://docs.weblate.org/en/latest/api.html#authentication
            "Authorization": f"Token {api_token}",
            "Accept": "text/x-po",
            "User-Agent": "SMART-Base-CI/1.0",
        }
    )

    counts: Dict[str, int] = {"downloaded": 0, "not_found": 0, "skipped": 0, "error": 0}

    for slug, trans_dir in active_components.items():
        logger.info("Component: %s  →  %s", slug, trans_dir)

        for lang in active_languages:
            logger.info("  Language: %s", lang)
            result = download_translation(
                session=session,
                weblate_url=weblate_url,
                project=project,
                component=slug,
                language=lang,
                output_dir=trans_dir,
            )
            counts[result] += 1

    logger.info(
        "Summary: %d downloaded, %d not found, %d skipped, %d errors",
        counts["downloaded"],
        counts["not_found"],
        counts["skipped"],
        counts["error"],
    )

    return 1 if counts["error"] > 0 else 0


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def _derive_default_project(output_root: Path) -> str:
    """Derive the default Weblate project slug from GITHUB_REPOSITORY env var."""
    github_repo = os.environ.get("GITHUB_REPOSITORY", "")
    if "/" in github_repo:
        org, repo = github_repo.split("/", 1)
        return get_project_slug(org, repo)
    return "worldhealthorganization-smart-base"


def _parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="pull_weblate_translations.py",
        description="Download .po translation files from the Weblate REST API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--weblate-url",
        default="https://hosted.weblate.org",
        help="Weblate base URL (default: https://hosted.weblate.org)",
    )
    parser.add_argument(
        "--project",
        default="",
        help=(
            "Weblate project slug. "
            "Default: derived from GITHUB_REPOSITORY env var, "
            "or 'worldhealthorganization-smart-base'."
        ),
    )
    parser.add_argument(
        "--component",
        default="",
        help="Restrict download to a single component slug. Default: all discovered components.",
    )
    parser.add_argument(
        "--language",
        default="",
        help="Restrict download to a single language code. Default: all languages from dak.json.",
    )
    parser.add_argument(
        "--output-root",
        default=".",
        help="Repository root for output directories (default: current directory)",
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

    # ── Resolve and validate output root ────────────────────────────────────
    output_root = Path(args.output_root).resolve()
    if not output_root.is_dir():
        sys.exit(f"ERROR: --output-root {output_root!r} is not a directory")

    # ── Validate / sanitize user-supplied values ────────────────────────────
    weblate_url = _validate_url(args.weblate_url, "--weblate-url")
    project_raw = args.project or _derive_default_project(output_root)
    project = _validate_slug(project_raw, "--project")
    component_filter: Optional[str] = None
    if args.component:
        component_filter = _validate_slug(args.component, "--component")
    language_filter: Optional[str] = None
    if args.language:
        language_filter = _validate_slug(args.language, "--language")

    # ── Token from environment only — skip gracefully when absent ───────────
    api_token = get_optional_env_token("WEBLATE_API_TOKEN")
    if not api_token:
        logger.info(
            "WEBLATE_API_TOKEN is not set — skipping Weblate pull. "
            "Add the secret to enable: Settings → Secrets → Actions → New secret"
        )
        return 0

    logger.info(
        "Pulling translations from %s (project: %s)", weblate_url, project
    )
    if component_filter:
        logger.info("  Component filter: %s", component_filter)
    if language_filter:
        logger.info("  Language filter:  %s", language_filter)

    return pull_translations(
        weblate_url=weblate_url,
        project=project,
        output_root=output_root,
        component_filter=component_filter,
        language_filter=language_filter,
        api_token=api_token,
    )


if __name__ == "__main__":
    sys.exit(main())
