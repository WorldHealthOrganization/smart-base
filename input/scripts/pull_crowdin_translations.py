#!/usr/bin/env python3
"""
pull_crowdin_translations.py — Download .po files from Crowdin v2 API.

Service activation: runs only when CROWDIN_API_TOKEN is set in the
environment.  Exits 0 silently when the token is absent.

Usage:
    python pull_crowdin_translations.py [--repo-root DIR] [--project-id ID]
                                        [--component SLUG] [--language CODE]

Environment variables:
    CROWDIN_API_TOKEN   Optional. Crowdin API token. When absent, exits 0.

Exit codes:
    0  Success or skipped (no token)
    1  Download or API errors
    2  Bad arguments
"""

import argparse
import logging
import os
import sys
import tempfile
import time
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
_CROWDIN_API = "https://api.crowdin.com/api/v2"
_MAX_PO_BYTES = 10 * 1024 * 1024
_TIMEOUT = 60
_EXPORT_POLL_INTERVAL = 5   # seconds between export-status polls
_EXPORT_MAX_POLLS = 30


def _crowdin_headers(token: str) -> dict:
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


def _trigger_export(session: "requests.Session", project_id: str, token: str) -> Optional[str]:
    """Trigger a project export and return the export ID, or None on error."""
    logger = logging.getLogger(__name__)
    url = f"{_CROWDIN_API}/projects/{project_id}/exports"
    try:
        resp = session.post(url, json={}, timeout=_TIMEOUT)
    except requests.RequestException as exc:
        logger.error("Crowdin export trigger failed: %s", exc)
        return None
    if resp.status_code not in (200, 201):
        logger.error("Crowdin export trigger HTTP %d", resp.status_code)
        return None
    return resp.json().get("data", {}).get("identifier")


def _wait_for_export(session: "requests.Session", project_id: str, export_id: str, token: str) -> bool:
    """Poll until the export is finished. Returns True on success."""
    logger = logging.getLogger(__name__)
    url = f"{_CROWDIN_API}/projects/{project_id}/exports/{export_id}"
    for _ in range(_EXPORT_MAX_POLLS):
        try:
            resp = session.get(url, timeout=_TIMEOUT)
        except requests.RequestException as exc:
            logger.error("Crowdin export poll failed: %s", exc)
            return False
        status = resp.json().get("data", {}).get("status", "")
        if status == "finished":
            return True
        if status in ("failed", "cancelled"):
            logger.error("Crowdin export ended with status %r", status)
            return False
        time.sleep(_EXPORT_POLL_INTERVAL)
    logger.error("Crowdin export timed out after %d polls", _EXPORT_MAX_POLLS)
    return False


def _download_file_export(
    session: "requests.Session",
    project_id: str,
    file_id: int,
    lang: str,
    dest: Path,
    token: str,
) -> bool:
    """Download a single translated file in gettext-po format."""
    logger = logging.getLogger(__name__)
    url = f"{_CROWDIN_API}/projects/{project_id}/translations/exports"
    payload = {"targetLanguageId": lang, "fileIds": [file_id], "format": "po"}
    try:
        resp = session.post(url, json=payload, timeout=_TIMEOUT)
    except requests.RequestException as exc:
        logger.error("  Crowdin file export failed: %s", exc)
        return False

    if resp.status_code not in (200, 201):
        logger.error("  Crowdin file export HTTP %d", resp.status_code)
        return False

    download_url = resp.json().get("data", {}).get("url")
    if not download_url:
        logger.error("  No download URL in Crowdin response")
        return False

    try:
        dl = session.get(download_url, timeout=_TIMEOUT, stream=True)
    except requests.RequestException as exc:
        logger.error("  Download error: %s", exc)
        return False

    if dl.status_code != 200:
        logger.error("  Download HTTP %d", dl.status_code)
        return False

    dest.parent.mkdir(parents=True, exist_ok=True)
    try:
        with tempfile.NamedTemporaryFile(dir=dest.parent, suffix=".po.tmp", delete=False) as fh:
            tmp_path = Path(fh.name)
            total = 0
            for chunk in dl.iter_content(65536):
                total += len(chunk)
                if total > _MAX_PO_BYTES:
                    logger.error("  Response too large")
                    tmp_path.unlink(missing_ok=True)
                    return False
                fh.write(chunk)
        tmp_path.replace(dest)
        logger.info("  ✓ %s (%d bytes)", dest, total)
        return True
    except OSError as exc:
        logger.error("  Write error: %s", exc)
        return False


def pull_crowdin_translations(
    repo_root: Path,
    project_id: str,
    component_filter: Optional[str],
    language_filter: Optional[str],
    api_token: str,
) -> int:
    """Download .po files from Crowdin. Returns 0 on success, 1 on errors."""
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
        logger.warning("No *.pot files found — nothing to pull from Crowdin")
        return 0

    if component_filter:
        components = [c for c in components if c.slug == component_filter]
        if not components:
            logger.error("Component %r not found", component_filter)
            return 1

    active_languages = [language_filter] if language_filter else lang_codes

    session = requests.Session()
    session.headers.update(_crowdin_headers(api_token))

    # Retrieve Crowdin file list for the project
    try:
        files_resp = session.get(
            f"{_CROWDIN_API}/projects/{project_id}/files",
            params={"limit": 500},
            timeout=_TIMEOUT,
        )
    except requests.RequestException as exc:
        logger.error("Cannot list Crowdin files: %s", exc)
        return 1

    if files_resp.status_code != 200:
        logger.error("Crowdin files list HTTP %d", files_resp.status_code)
        return 1

    crowdin_files = {
        item["data"]["name"].replace(".pot", ""): item["data"]["id"]
        for item in files_resp.json().get("data", [])
        if isinstance(item.get("data"), dict)
    }

    errors = 0
    for comp in components:
        file_id = crowdin_files.get(comp.slug)
        if file_id is None:
            logger.info("Component %r not found in Crowdin project — skipping", comp.slug)
            continue
        for lang in active_languages:
            dest = comp.po_path(lang)
            ok = _download_file_export(session, project_id, file_id, lang, dest, api_token)
            if not ok:
                errors += 1

    return 1 if errors else 0


def _parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="pull_crowdin_translations.py",
        description="Download .po files from Crowdin v2 API",
    )
    parser.add_argument("--repo-root", default=".", help="Repository root (default: .)")
    parser.add_argument("--project-id", default="", help="Crowdin numeric project ID")
    parser.add_argument("--component", default="", help="Restrict to one component slug")
    parser.add_argument("--language", default="", help="Restrict to one language code")
    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s",
                        datefmt="%H:%M:%S")
    logger = logging.getLogger(__name__)

    args = _parse_args(argv)

    api_token = get_optional_env_token("CROWDIN_API_TOKEN")
    if not api_token:
        logger.info("CROWDIN_API_TOKEN not set — skipping Crowdin pull")
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

    # project_id may be provided via arg or dak.json extras
    project_id = args.project_id
    if not project_id:
        try:
            config = load_dak_config(repo_root)
            project_id = str(config.services.get("crowdin", None) and
                             config.services["crowdin"].extra.get("projectId", ""))
        except DakConfigError:
            pass
    if not project_id:
        sys.exit("ERROR: Crowdin project ID must be set via --project-id or dak.json#translations.services.crowdin.projectId")

    logger.info("Pulling translations from Crowdin (project: %s)", project_id)

    return pull_crowdin_translations(
        repo_root=repo_root,
        project_id=project_id,
        component_filter=component_filter,
        language_filter=language_filter,
        api_token=api_token,
    )


if __name__ == "__main__":
    sys.exit(main())
