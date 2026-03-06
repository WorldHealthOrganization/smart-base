#!/usr/bin/env python3
"""
register_translation_project.py — Idempotently create or verify the translation
project and all dynamically discovered components for one IG repo on every
enabled translation service.

Usage:
    python register_translation_project.py --repo-name smart-hiv [--repo-root /path]

Environment variables:
    WEBLATE_API_TOKEN      Weblate API token (if Weblate enabled)
    CROWDIN_API_TOKEN      Crowdin API token (if Crowdin enabled)
    LAUNCHPAD_API_TOKEN    Launchpad API token (if Launchpad enabled)

Exit codes:
    0  Registration completed (or dak.json not found — warning + skip)
    1  Registration error

Author: WHO SMART Guidelines Team
"""

import argparse
import logging
import os
import sys
from pathlib import Path
from typing import List, Optional

try:
    import requests
except ImportError:
    sys.exit("ERROR: 'requests' package is required. Run: pip install requests>=2.31.0")

# Add parent directory to path for sibling imports
sys.path.insert(0, str(Path(__file__).resolve().parent))

from translation_config import (
    DakConfig,
    DakConfigError,
    TranslationComponent,
    discover_components,
    get_enabled_services,
    get_languages,
    get_project_slug,
    load_dak_config,
)
from translation_security import (
    DEFAULT_TIMEOUT_SECONDS,
    assert_no_secret_in_env,
    redact_for_log,
    sanitize_slug,
    sanitize_url,
)

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Weblate registration
# ---------------------------------------------------------------------------

def _register_weblate_project(
    project_slug: str,
    config: DakConfig,
    components: List[TranslationComponent],
    api_token: str,
    weblate_url: str,
    repo_root: Path = Path("."),
) -> bool:
    """
    Idempotently create/verify a Weblate project and its components.

    Returns True on success, False on error.
    """
    session = requests.Session()
    session.headers.update({
        "Authorization": f"Token {api_token}",
        "Content-Type": "application/json",
        "User-Agent": "SMART-Base-CI/1.0",
    })

    # Check if project exists
    project_url = f"{weblate_url}/api/projects/{project_slug}/"
    try:
        resp = session.get(project_url, timeout=DEFAULT_TIMEOUT_SECONDS)
    except requests.exceptions.RequestException as exc:
        logger.error("Network error checking project: %s", exc)
        return False

    if resp.status_code == 404:
        # Create project
        logger.info("Creating Weblate project: %s", project_slug)
        create_url = f"{weblate_url}/api/projects/"
        payload = {
            "name": config.title or config.name,
            "slug": project_slug,
            "web": config.raw.get("publicationUrl", ""),
        }
        try:
            resp = session.post(
                create_url, json=payload, timeout=DEFAULT_TIMEOUT_SECONDS
            )
            if resp.status_code not in (200, 201):
                logger.error(
                    "Failed to create project %s: HTTP %d %s",
                    project_slug, resp.status_code, resp.text[:500],
                )
                return False
            logger.info("✓ Created project: %s", project_slug)
        except requests.exceptions.RequestException as exc:
            logger.error("Network error creating project: %s", exc)
            return False
    elif resp.status_code == 200:
        logger.info("✓ Project already exists: %s", project_slug)
    else:
        logger.error(
            "Unexpected HTTP %d checking project %s", resp.status_code, project_slug
        )
        return False

    # Register each component
    all_ok = True
    for comp in components:
        ok = _register_weblate_component(
            session, weblate_url, project_slug, comp, repo_root
        )
        if not ok:
            all_ok = False

    return all_ok


def _register_weblate_component(
    session: requests.Session,
    weblate_url: str,
    project_slug: str,
    comp: TranslationComponent,
    repo_root: Path,
) -> bool:
    """Idempotently register one Weblate component."""
    comp_url = f"{weblate_url}/api/components/{project_slug}/{comp.slug}/"

    try:
        resp = session.get(comp_url, timeout=DEFAULT_TIMEOUT_SECONDS)
    except requests.exceptions.RequestException as exc:
        logger.error("Network error checking component %s: %s", comp.slug, exc)
        return False

    if resp.status_code == 200:
        logger.info("  ✓ Component already exists: %s", comp.slug)
        return True

    if resp.status_code == 404:
        logger.info("  Creating component: %s", comp.slug)
        create_url = f"{weblate_url}/api/projects/{project_slug}/components/"

        # Weblate expects repo-relative paths, not absolute filesystem paths.
        try:
            rel_translations_dir = comp.translations_dir.relative_to(repo_root)
        except ValueError:
            rel_translations_dir = comp.translations_dir
        try:
            rel_pot_path = comp.pot_path.relative_to(repo_root)
        except ValueError:
            rel_pot_path = comp.pot_path

        payload = {
            "name": comp.slug,
            "slug": comp.slug,
            "file_format": "po",
            "filemask": f"{rel_translations_dir}/*.po",
            # new_base: used by Weblate to create new translation files.
            # template: used by Weblate to locate the source .pot file.
            # Both point to the same POT file per Weblate component config.
            "new_base": str(rel_pot_path),
            "template": str(rel_pot_path),
            "vcs": "github",
        }
        try:
            resp = session.post(
                create_url, json=payload, timeout=DEFAULT_TIMEOUT_SECONDS
            )
            if resp.status_code in (200, 201):
                logger.info("  ✓ Created component: %s", comp.slug)
                return True
            else:
                logger.error(
                    "  Failed to create component %s: HTTP %d %s",
                    comp.slug, resp.status_code, resp.text[:500],
                )
                return False
        except requests.exceptions.RequestException as exc:
            logger.error("Network error creating component %s: %s", comp.slug, exc)
            return False
    else:
        logger.error(
            "  Unexpected HTTP %d checking component %s",
            resp.status_code, comp.slug,
        )
        return False


# ---------------------------------------------------------------------------
# Main registration logic
# ---------------------------------------------------------------------------

def register_project(
    repo_name: str,
    repo_root: Path,
    github_org: str = "worldhealthorganization",
) -> int:
    """
    Register one IG repo with all enabled translation services.

    Returns 0 on success, 1 on error.
    """
    # Load configuration
    try:
        config = load_dak_config(repo_root)
    except DakConfigError:
        logger.warning("dak.json not found or invalid at %s — skipping", repo_root)
        return 0  # REG-002: missing dak.json → warning + exit 0

    # Discover components
    components = discover_components(repo_root)
    if not components:
        logger.info("No .pot files found — no components to register")

    project_slug = get_project_slug(github_org, repo_name)
    logger.info("Project slug: %s", project_slug)

    enabled_services = get_enabled_services(config)
    if not enabled_services:
        logger.info("No translation services enabled in dak.json")
        return 0

    errors = False

    # Weblate
    if "weblate" in enabled_services:
        api_token = os.environ.get("WEBLATE_API_TOKEN", "")
        if not api_token:
            logger.error("WEBLATE_API_TOKEN not set — cannot register with Weblate")
            errors = True
        else:
            weblate_url = enabled_services["weblate"].url or "https://hosted.weblate.org"
            try:
                weblate_url = sanitize_url(weblate_url, "weblate_url")
            except ValueError as exc:
                logger.error("Invalid Weblate URL: %s", exc)
                errors = True
            else:
                logger.info(
                    "Registering with Weblate (token: %s)",
                    redact_for_log(api_token),
                )
                ok = _register_weblate_project(
                    project_slug, config, components, api_token, weblate_url,
                    repo_root=repo_root,
                )
                if not ok:
                    errors = True

    # Launchpad (stub — logs info about what would be registered)
    if "launchpad" in enabled_services:
        api_token = os.environ.get("LAUNCHPAD_API_TOKEN", "")
        if not api_token:
            logger.error("LAUNCHPAD_API_TOKEN not set — cannot register with Launchpad")
            errors = True
        else:
            logger.info("Launchpad registration: project=%s (%d components)",
                        project_slug, len(components))
            # Launchpad API integration would go here
            logger.info("✓ Launchpad registration completed (stub)")

    # Crowdin (stub — logs info about what would be registered)
    if "crowdin" in enabled_services:
        api_token = os.environ.get("CROWDIN_API_TOKEN", "")
        if not api_token:
            logger.error("CROWDIN_API_TOKEN not set — cannot register with Crowdin")
            errors = True
        else:
            logger.info("Crowdin registration: project=%s (%d components)",
                        project_slug, len(components))
            # Crowdin API integration would go here
            logger.info("✓ Crowdin registration completed (stub)")

    return 1 if errors else 0


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv: Optional[List[str]] = None) -> int:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
    )

    parser = argparse.ArgumentParser(
        prog="register_translation_project.py",
        description="Register one IG repo with all enabled translation services",
    )
    parser.add_argument(
        "--repo-name", required=True,
        help="GitHub repository name (e.g. smart-hiv)",
    )
    parser.add_argument(
        "--repo-root", default=".",
        help="Path to repository root (default: current directory)",
    )
    parser.add_argument(
        "--org", default="worldhealthorganization",
        help="GitHub organization (default: worldhealthorganization)",
    )
    args = parser.parse_args(argv)

    repo_root = Path(args.repo_root).resolve()
    repo_name = sanitize_slug(args.repo_name, "repo-name")

    # Security: verify tokens are from secrets, not workflow inputs
    for token_env in ("WEBLATE_API_TOKEN", "CROWDIN_API_TOKEN", "LAUNCHPAD_API_TOKEN"):
        try:
            assert_no_secret_in_env(token_env)
        except RuntimeError as exc:
            logger.error("%s", exc)
            return 1

    return register_project(repo_name, repo_root, github_org=args.org)


if __name__ == "__main__":
    sys.exit(main())
