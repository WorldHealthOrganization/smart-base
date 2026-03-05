#!/usr/bin/env python3
"""
pull_translations.py — Multi-service translation pull orchestrator.

Calls each enabled translation service adapter in sequence.  Service
activation is determined solely by the presence of the corresponding API
token in the environment — no service-specific flags or config file changes
are needed.

Services and their activation tokens:
  Weblate   → WEBLATE_API_TOKEN
  Launchpad → LAUNCHPAD_API_TOKEN
  Crowdin   → CROWDIN_API_TOKEN

GPT fill-in (for remaining untranslated strings):
  OpenAI    → OPENAI_API_KEY
  Anthropic → ANTHROPIC_API_KEY
  DeepSeek  → DEEPSEEK_API_KEY

Usage:
    python pull_translations.py [--repo-root DIR]
                                [--service SERVICE]
                                [--component SLUG]
                                [--language CODE]
                                [--weblate-url URL]
                                [--skip-gpt]

Exit codes:
    0  All active services succeeded (or were skipped)
    1  One or more services reported errors
"""

import argparse
import logging
import os
import sys
from pathlib import Path
from typing import List, Optional

from translation_security import get_optional_env_token, sanitize_lang_code, sanitize_slug

# Map service name → (module, main_function_import_path)
_SERVICE_SCRIPTS = {
    "weblate":    "pull_weblate_translations",
    "launchpad":  "pull_launchpad_translations",
    "crowdin":    "pull_crowdin_translations",
}

_GPT_SCRIPT = "pull_gpt_translations"


def _run_service(
    service: str,
    repo_root: Path,
    component_filter: Optional[str],
    language_filter: Optional[str],
    extra_env: dict,
) -> int:
    """
    Dynamically import and call the main() of a service adapter.

    Returns the adapter's exit code.
    """
    logger = logging.getLogger(__name__)
    module_name = _SERVICE_SCRIPTS[service]

    # Build argv for the adapter
    argv: List[str] = ["--output-root" if service == "weblate" else "--repo-root", str(repo_root)]
    if component_filter:
        argv += ["--component", component_filter]
    if language_filter:
        argv += ["--language", language_filter]
    if service == "weblate":
        weblate_url = extra_env.get("weblate_url", "https://hosted.weblate.org")
        argv += ["--weblate-url", weblate_url]

    logger.info("── Running %s service ──", service)

    import importlib
    try:
        mod = importlib.import_module(module_name)
        return mod.main(argv)
    except SystemExit as exc:
        code = exc.code if isinstance(exc.code, int) else 1
        logger.error("%s adapter raised SystemExit(%s)", service, code)
        return code
    except Exception as exc:
        logger.error("%s adapter raised unexpected error: %s", service, exc)
        return 1


def _any_gpt_key_set() -> bool:
    for env_var in ("OPENAI_API_KEY", "ANTHROPIC_API_KEY", "DEEPSEEK_API_KEY"):
        if get_optional_env_token(env_var):
            return True
    return False


def _service_token_set(service: str) -> bool:
    token_env = {
        "weblate":   "WEBLATE_API_TOKEN",
        "launchpad": "LAUNCHPAD_API_TOKEN",
        "crowdin":   "CROWDIN_API_TOKEN",
    }
    env_var = token_env.get(service, "")
    return bool(env_var and get_optional_env_token(env_var))


def _parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="pull_translations.py",
        description="Orchestrate translation pulls from all active services",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--repo-root", default=".", help="Repository root (default: .)")
    parser.add_argument(
        "--service",
        default="all",
        choices=["all"] + list(_SERVICE_SCRIPTS),
        help="Restrict to one service (default: all active services)",
    )
    parser.add_argument("--component", default="", help="Restrict to one component slug")
    parser.add_argument("--language", default="", help="Restrict to one language code")
    parser.add_argument(
        "--weblate-url",
        default="https://hosted.weblate.org",
        help="Weblate base URL (default: https://hosted.weblate.org)",
    )
    parser.add_argument(
        "--skip-gpt",
        action="store_true",
        help="Do not run GPT fill-in pass even if an AI key is available",
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

    services_to_run = (
        list(_SERVICE_SCRIPTS)
        if args.service == "all"
        else [args.service]
    )

    extra_env = {"weblate_url": args.weblate_url}

    overall_errors = 0
    active_services = []

    for service in services_to_run:
        if _service_token_set(service):
            active_services.append(service)
        else:
            logger.info("Skipping %s — token not set", service)

    if not active_services:
        logger.info("No translation service tokens found — nothing to pull")
        logger.info(
            "To activate a service, add its token as a repository secret:\n"
            "  Weblate:   WEBLATE_API_TOKEN\n"
            "  Launchpad: LAUNCHPAD_API_TOKEN\n"
            "  Crowdin:   CROWDIN_API_TOKEN"
        )

    for service in active_services:
        rc = _run_service(service, repo_root, component_filter, language_filter, extra_env)
        if rc != 0:
            logger.error("Service %r exited with code %d", service, rc)
            overall_errors += rc

    # GPT fill-in pass: run after all service pulls, for any still-untranslated strings
    if not args.skip_gpt:
        if _any_gpt_key_set():
            logger.info("── Running GPT fill-in pass ──")
            import importlib
            gpt_mod = importlib.import_module(_GPT_SCRIPT)
            gpt_argv: List[str] = ["--repo-root", str(repo_root)]
            if component_filter:
                gpt_argv += ["--component", component_filter]
            if language_filter:
                gpt_argv += ["--language", language_filter]
            try:
                rc = gpt_mod.main(gpt_argv)
                if rc != 0:
                    overall_errors += rc
            except SystemExit as exc:
                code = exc.code if isinstance(exc.code, int) else 1
                overall_errors += code
        else:
            logger.info(
                "GPT fill-in skipped — no AI key set "
                "(OPENAI_API_KEY / ANTHROPIC_API_KEY / DEEPSEEK_API_KEY)"
            )

    if overall_errors:
        logger.error("Translation pull completed with %d error(s)", overall_errors)
        return 1

    logger.info("Translation pull complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
