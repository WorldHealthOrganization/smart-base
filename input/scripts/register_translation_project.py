#!/usr/bin/env python3
"""
register_translation_project.py — Idempotently register a WHO SMART IG in Weblate.

Creates the Weblate project and one component per discovered .pot file if
they do not already exist.  Safe to run repeatedly: existing resources are
left unchanged unless --update is given.

Component file paths are derived from the *.pot file locations relative to
the repository root, so they work for any downstream WHO SMART IG.

Usage:
    python register_translation_project.py [--repo-root DIR]
                                           [--weblate-url URL]
                                           [--project-slug SLUG]
                                           [--repo-url URL]
                                           [--branch BRANCH]
                                           [--update]
                                           [--dry-run]

Environment variables:
    WEBLATE_ADMIN_TOKEN   Required (unless --dry-run). Weblate API token with
                          project-admin privileges.

Exit codes:
    0  All resources created/verified
    1  One or more API errors
    2  Bad arguments or missing token
"""

import argparse
import logging
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    import requests
except ImportError:
    sys.exit("ERROR: 'requests' package is required. Run: pip install requests>=2.31.0")

from translation_config import (
    DakConfigError,
    discover_components,
    get_language_codes,
    get_project_slug,
    load_dak_config,
)
from translation_security import get_optional_env_token, sanitize_slug, sanitize_url

_DEFAULT_WEBLATE = "https://hosted.weblate.org"
_TIMEOUT = 30


# ---------------------------------------------------------------------------
# Weblate API helpers
# ---------------------------------------------------------------------------

def _api(method: str, url: str, session: "requests.Session", **kwargs) -> Optional[dict]:
    """Perform an API call, return parsed JSON or None on error."""
    logger = logging.getLogger(__name__)
    try:
        resp = getattr(session, method)(url, timeout=_TIMEOUT, **kwargs)
    except requests.RequestException as exc:
        logger.error("Network error %s %s: %s", method.upper(), url, exc)
        return None

    if resp.status_code in (200, 201):
        try:
            return resp.json()
        except ValueError:
            return {}

    logger.error("HTTP %d %s %s — %s", resp.status_code, method.upper(), url, resp.text[:200])
    return None


def _project_exists(session: "requests.Session", weblate_url: str, slug: str) -> bool:
    url = f"{weblate_url}/api/projects/{slug}/"
    try:
        resp = session.get(url, timeout=_TIMEOUT)
        return resp.status_code == 200
    except requests.RequestException:
        return False


def _component_exists(
    session: "requests.Session", weblate_url: str, project: str, component: str
) -> bool:
    url = f"{weblate_url}/api/components/{project}/{component}/"
    try:
        resp = session.get(url, timeout=_TIMEOUT)
        return resp.status_code == 200
    except requests.RequestException:
        return False


def _create_project(
    session: "requests.Session",
    weblate_url: str,
    slug: str,
    name: str,
    website: str,
    dry_run: bool,
) -> bool:
    logger = logging.getLogger(__name__)
    if _project_exists(session, weblate_url, slug):
        logger.info("Project %r already exists", slug)
        return True

    payload = {
        "name": name,
        "slug": slug,
        "web": website or f"https://github.com/{slug}",
    }
    if dry_run:
        logger.info("[DRY RUN] Would create project: %s", payload)
        return True

    logger.info("Creating Weblate project %r", slug)
    result = _api("post", f"{weblate_url}/api/projects/", session, json=payload)
    if result is None:
        return False
    logger.info("✓ Created project %r", slug)
    return True


def _create_component(
    session: "requests.Session",
    weblate_url: str,
    project_slug: str,
    component_slug: str,
    name: str,
    file_mask: str,
    template: str,
    repo_url: str,
    branch: str,
    languages: List[str],
    dry_run: bool,
) -> bool:
    logger = logging.getLogger(__name__)
    if _component_exists(session, weblate_url, project_slug, component_slug):
        logger.info("  Component %r already exists", component_slug)
        return True

    payload: Dict[str, Any] = {
        "name": name,
        "slug": component_slug,
        "project": f"{weblate_url}/api/projects/{project_slug}/",
        "vcs": "github",
        "repo": repo_url,
        "branch": branch,
        "filemask": file_mask,
        "template": template,
        "file_format": "po",
        "source_language": {"code": "en"},
        "new_lang": "add",
        "manage_units": True,
        "add_addon": True,
    }

    if dry_run:
        logger.info("  [DRY RUN] Would create component: %s", component_slug)
        logger.info("    file_mask: %s", file_mask)
        logger.info("    template:  %s", template)
        return True

    logger.info("  Creating component %r", component_slug)
    result = _api("post", f"{weblate_url}/api/components/", session, json=payload)
    if result is None:
        return False
    logger.info("  ✓ Created component %r", component_slug)
    return True


# ---------------------------------------------------------------------------
# Main registration logic
# ---------------------------------------------------------------------------

def register_project(
    repo_root: Path,
    weblate_url: str,
    project_slug: str,
    repo_url: str,
    branch: str,
    api_token: str,
    dry_run: bool,
) -> int:
    """
    Register all .pot-based components for *repo_root* in Weblate.

    Returns 0 on success, 1 if any step failed.
    """
    logger = logging.getLogger(__name__)
    errors = 0

    # Resolve config
    try:
        config = load_dak_config(repo_root)
        lang_codes = get_language_codes(config)
        project_name = config.raw.get("title") or project_slug
        website = config.raw.get("publicationUrl") or ""
    except DakConfigError as exc:
        logger.warning("dak.json not available: %s — using defaults", exc)
        lang_codes = ["ar", "zh", "fr", "ru", "es"]
        project_name = project_slug
        website = ""

    # Discover components
    components = discover_components(repo_root)
    if not components:
        logger.warning("No *.pot files found — nothing to register")
        return 0

    session = requests.Session()
    session.headers.update({
        "Authorization": f"Token {api_token}",
        "Content-Type": "application/json",
    })

    # Create project
    ok = _create_project(session, weblate_url, project_slug, project_name, website, dry_run)
    if not ok:
        return 1

    # Create one component per .pot file
    for comp in components:
        # file_mask: path relative to repo root with language code placeholder
        # e.g. input/images/translations/*.po
        rel_translations_dir = comp.translations_dir.relative_to(repo_root)
        file_mask = str(rel_translations_dir / "*.po").replace("\\", "/")
        template = str(comp.pot_path.relative_to(repo_root)).replace("\\", "/")

        ok = _create_component(
            session=session,
            weblate_url=weblate_url,
            project_slug=project_slug,
            component_slug=comp.slug,
            name=comp.slug.replace("-", " ").title(),
            file_mask=file_mask,
            template=template,
            repo_url=repo_url,
            branch=branch,
            languages=lang_codes,
            dry_run=dry_run,
        )
        if not ok:
            errors += 1

    if errors:
        logger.error("%d component(s) failed to register", errors)
        return 1

    logger.info("Registration complete for project %r (%d components)", project_slug, len(components))
    return 0


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="register_translation_project.py",
        description="Idempotently register a WHO SMART IG in Weblate",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--repo-root", default=".", help="Repository root (default: .)")
    parser.add_argument(
        "--weblate-url", default=_DEFAULT_WEBLATE,
        help=f"Weblate base URL (default: {_DEFAULT_WEBLATE})"
    )
    parser.add_argument("--project-slug", default="",
                        help="Weblate project slug (default: derived from GITHUB_REPOSITORY)")
    parser.add_argument("--repo-url", default="",
                        help="Git repository URL for Weblate to clone")
    parser.add_argument("--branch", default="main", help="Default branch (default: main)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print actions without making API calls")
    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
    )
    logger = logging.getLogger(__name__)
    args = _parse_args(argv)

    repo_root = Path(args.repo_root).resolve()
    if not repo_root.is_dir():
        sys.exit(f"ERROR: --repo-root {repo_root!r} is not a directory")

    try:
        weblate_url = sanitize_url(args.weblate_url, "--weblate-url", allowed_schemes=("https", "http"))
    except ValueError as exc:
        sys.exit(f"ERROR: {exc}")

    # Derive project slug
    project_slug = args.project_slug
    if not project_slug:
        github_repo = os.environ.get("GITHUB_REPOSITORY", "")
        if "/" in github_repo:
            org, repo = github_repo.split("/", 1)
            project_slug = get_project_slug(org, repo)
        else:
            sys.exit(
                "ERROR: --project-slug is required (or set GITHUB_REPOSITORY=org/repo)"
            )
    try:
        project_slug = sanitize_slug(project_slug, "--project-slug")
    except ValueError as exc:
        sys.exit(f"ERROR: {exc}")

    # Derive repo URL
    repo_url = args.repo_url
    if not repo_url:
        github_repo = os.environ.get("GITHUB_REPOSITORY", "")
        repo_url = f"https://github.com/{github_repo}" if github_repo else ""
    if not repo_url and not args.dry_run:
        sys.exit("ERROR: --repo-url is required (or set GITHUB_REPOSITORY)")

    # Branch
    branch = os.environ.get("GITHUB_REF_NAME") or args.branch or "main"

    # API token
    if args.dry_run:
        api_token = "dry-run-placeholder"
    else:
        api_token = get_optional_env_token("WEBLATE_ADMIN_TOKEN")
        if not api_token:
            sys.exit(
                "ERROR: WEBLATE_ADMIN_TOKEN environment variable is not set.\n"
                "  Add a Weblate admin token as a repository secret."
            )

    logger.info(
        "Registering project %r in Weblate (%s)%s",
        project_slug, weblate_url,
        " [DRY RUN]" if args.dry_run else "",
    )

    return register_project(
        repo_root=repo_root,
        weblate_url=weblate_url,
        project_slug=project_slug,
        repo_url=repo_url,
        branch=branch,
        api_token=api_token,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    sys.exit(main())
