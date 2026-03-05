#!/usr/bin/env python3
"""
pull_launchpad_translations.py — Download .po files from Launchpad Translations.

Service activation: runs only when LAUNCHPAD_API_TOKEN is set in the
environment.  Exits 0 silently when the token is absent.

Usage:
    python pull_launchpad_translations.py [--repo-root DIR] [--project SLUG]
                                          [--component SLUG] [--language CODE]

Environment variables:
    LAUNCHPAD_API_TOKEN   Optional. Launchpad API token. When absent, exits 0.

Exit codes:
    0  Success or skipped (no token)
    1  Download errors
    2  Bad arguments
"""

import argparse
import logging
import os
import sys
import tempfile
from pathlib import Path
from typing import Dict, List, Optional

try:
    import requests
except ImportError:  # pragma: no cover
    sys.exit("ERROR: 'requests' package is required. Run: pip install requests>=2.31.0")

from translation_config import (
    DakConfigError,
    discover_components,
    get_language_codes,
    load_dak_config,
)
from translation_security import get_optional_env_token, sanitize_lang_code, sanitize_slug

_FALLBACK_LANGUAGES = ("ar", "zh", "fr", "ru", "es")

# Launchpad Translations export API base URL
_LP_API_BASE = "https://translations.launchpad.net"
_MAX_PO_BYTES = 10 * 1024 * 1024
_TIMEOUT = 60


def pull_launchpad_translations(
    repo_root: Path,
    project_slug: str,
    component_filter: Optional[str],
    language_filter: Optional[str],
    api_token: str,
) -> int:
    """
    Download .po files from Launchpad for each (component, language) pair.

    Returns 0 on success, 1 if any download failed.
    """
    logger = logging.getLogger(__name__)

    try:
        config = load_dak_config(repo_root)
        lang_codes = get_language_codes(config)
        if not lang_codes:
            lang_codes = list(_FALLBACK_LANGUAGES)
    except DakConfigError:
        lang_codes = list(_FALLBACK_LANGUAGES)

    components = discover_components(repo_root)
    if not components:
        logger.warning("No *.pot files found — nothing to pull from Launchpad")
        return 0

    if component_filter:
        components = [c for c in components if c.slug == component_filter]
        if not components:
            logger.error("Component %r not found", component_filter)
            return 1

    active_languages = [language_filter] if language_filter else lang_codes

    session = requests.Session()
    session.headers.update({"Authorization": f"Bearer {api_token}"})

    errors = 0
    for comp in components:
        for lang in active_languages:
            url = (
                f"{_LP_API_BASE}/{project_slug}/+pots/{comp.slug}/+export"
                f"?format=po&languages={lang}"
            )
            logger.info("  GET %s", url)
            try:
                resp = session.get(url, timeout=_TIMEOUT, stream=True)
            except requests.RequestException as exc:
                logger.error("  Network error: %s", exc)
                errors += 1
                continue

            if resp.status_code == 404:
                logger.info("  404 — no translation for %s/%s", comp.slug, lang)
                continue
            if resp.status_code != 200:
                logger.error("  HTTP %d for %s/%s", resp.status_code, comp.slug, lang)
                errors += 1
                continue

            comp.translations_dir.mkdir(parents=True, exist_ok=True)
            dest = comp.po_path(lang)
            try:
                with tempfile.NamedTemporaryFile(
                    dir=comp.translations_dir, suffix=".po.tmp", delete=False
                ) as fh:
                    tmp_path = Path(fh.name)
                    total = 0
                    for chunk in resp.iter_content(65536):
                        total += len(chunk)
                        if total > _MAX_PO_BYTES:
                            logger.error("  Response too large for %s/%s", comp.slug, lang)
                            tmp_path.unlink(missing_ok=True)
                            errors += 1
                            break
                        fh.write(chunk)
                    else:
                        tmp_path.replace(dest)
                        logger.info("  ✓ %s (%d bytes)", dest, total)
            except OSError as exc:
                logger.error("  Write error: %s", exc)
                errors += 1

    return 1 if errors else 0


def _parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="pull_launchpad_translations.py",
        description="Download .po files from Launchpad Translations",
    )
    parser.add_argument("--repo-root", default=".", help="Repository root (default: .)")
    parser.add_argument("--project", default="", help="Launchpad project slug")
    parser.add_argument("--component", default="", help="Restrict to one component slug")
    parser.add_argument("--language", default="", help="Restrict to one language code")
    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s",
                        datefmt="%H:%M:%S")
    logger = logging.getLogger(__name__)

    args = _parse_args(argv)

    api_token = get_optional_env_token("LAUNCHPAD_API_TOKEN")
    if not api_token:
        logger.info("LAUNCHPAD_API_TOKEN not set — skipping Launchpad pull")
        return 0

    repo_root = Path(args.repo_root).resolve()
    if not repo_root.is_dir():
        sys.exit(f"ERROR: --repo-root {repo_root!r} is not a directory")

    component_filter: Optional[str] = None
    if args.component:
        try:
            component_filter = sanitize_slug(args.component, "--component")
        except ValueError as exc:
            sys.exit(f"ERROR: {exc}")

    language_filter: Optional[str] = None
    if args.language:
        try:
            language_filter = sanitize_lang_code(args.language)
        except ValueError as exc:
            sys.exit(f"ERROR: {exc}")

    project_slug = args.project or os.environ.get("GITHUB_REPOSITORY", "").split("/")[-1] or "smart-base"
    try:
        project_slug = sanitize_slug(project_slug, "--project")
    except ValueError as exc:
        sys.exit(f"ERROR: {exc}")

    logger.info("Pulling translations from Launchpad (project: %s)", project_slug)

    return pull_launchpad_translations(
        repo_root=repo_root,
        project_slug=project_slug,
        component_filter=component_filter,
        language_filter=language_filter,
        api_token=api_token,
    )


if __name__ == "__main__":
    sys.exit(main())
