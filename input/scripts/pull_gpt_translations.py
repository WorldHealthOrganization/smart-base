#!/usr/bin/env python3
"""
pull_gpt_translations.py — Fill untranslated .po strings using AI (GPT / Claude / DeepSeek).

Uses the `gpt-po-translator` package (https://github.com/pescheckit/python-gpt-po)
to translate only untranslated (empty msgstr) entries.  Already-translated
entries are never touched.

Service activation: the script runs only when at least one AI provider secret
is present in the environment (OPENAI_API_KEY, ANTHROPIC_API_KEY, or
DEEPSEEK_API_KEY).  When none are set it exits 0 silently, enabling graceful
no-op runs in repos without AI credentials.

Usage:
    python pull_gpt_translations.py [--repo-root DIR] [--component SLUG]
                                    [--language CODE] [--provider PROVIDER]
                                    [--model MODEL] [--batch-size N]

Environment variables (all optional; at least one required to activate):
    OPENAI_API_KEY       OpenAI API key
    ANTHROPIC_API_KEY    Anthropic/Claude API key
    DEEPSEEK_API_KEY     DeepSeek API key

Exit codes:
    0  Success, skipped (no key set), or nothing to translate
    1  Translation errors occurred
    2  Bad arguments
"""

import argparse
import logging
import os
import subprocess
import sys
from pathlib import Path
from typing import List, Optional

from translation_config import (
    DakConfigError,
    discover_components,
    get_language_codes,
    load_dak_config,
)
from translation_security import get_optional_env_token, sanitize_lang_code, sanitize_slug

# ---------------------------------------------------------------------------
# Provider → env var mapping
# ---------------------------------------------------------------------------

_PROVIDER_ENV: dict = {
    "openai":    "OPENAI_API_KEY",
    "anthropic": "ANTHROPIC_API_KEY",
    "deepseek":  "DEEPSEEK_API_KEY",
}

_FALLBACK_LANGUAGES = ("ar", "zh", "fr", "ru", "es")


def _detect_provider() -> Optional[str]:
    """
    Return the first provider whose API key env var is non-empty, or None.

    Checks providers in preference order: openai → anthropic → deepseek.
    """
    for provider, env_var in _PROVIDER_ENV.items():
        if get_optional_env_token(env_var):
            return provider
    return None


def _count_untranslated(po_path: Path) -> int:
    """Return number of untranslated (empty msgstr) entries in a .po file."""
    try:
        content = po_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return 0
    count = 0
    in_msgstr = False
    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("msgstr "):
            val = stripped[7:].strip()
            in_msgstr = val == '""'
        elif in_msgstr and stripped.startswith('"') and stripped.endswith('"'):
            if stripped != '""':
                in_msgstr = False
        elif in_msgstr and not stripped.startswith('"'):
            if in_msgstr:
                count += 1
            in_msgstr = False
    if in_msgstr:
        count += 1
    return count


def translate_po_file(
    po_path: Path,
    lang_code: str,
    provider: str,
    model: Optional[str],
    batch_size: int,
) -> bool:
    """
    Invoke gpt-po-translator on *po_path* for *lang_code*.

    Only runs if there are untranslated strings in the file.

    Returns True on success, False on error.
    """
    logger = logging.getLogger(__name__)

    untranslated = _count_untranslated(po_path)
    if untranslated == 0:
        logger.info("  %s/%s — fully translated, skipping GPT", po_path.parent.name, lang_code)
        return True

    logger.info(
        "  %s/%s — %d untranslated strings → calling gpt-po-translator (%s)",
        po_path.parent.name,
        lang_code,
        untranslated,
        provider,
    )

    cmd = [
        sys.executable, "-m", "python_gpt_po.main",
        "--folder", str(po_path.parent),
        "--lang", lang_code,
        "--provider", provider,
        "--bulk",
        "-v",
    ]
    if model:
        cmd += ["--model", model]
    if batch_size:
        cmd += ["--bulk-size", str(batch_size)]

    try:
        result = subprocess.run(
            cmd,
            timeout=600,
            check=False,
            capture_output=False,
        )
    except subprocess.TimeoutExpired:
        logger.error("  gpt-po-translator timed out for %s/%s", po_path.parent.name, lang_code)
        return False
    except OSError as exc:
        logger.error("  Cannot run gpt-po-translator: %s", exc)
        return False

    if result.returncode != 0:
        logger.error(
            "  gpt-po-translator exited %d for %s/%s",
            result.returncode,
            po_path.parent.name,
            lang_code,
        )
        return False

    return True


def run_gpt_translations(
    repo_root: Path,
    component_filter: Optional[str],
    language_filter: Optional[str],
    provider: str,
    model: Optional[str],
    batch_size: int,
) -> int:
    """
    For each component × language, translate untranslated .po strings using GPT.

    Returns 0 on overall success, 1 if any file failed.
    """
    logger = logging.getLogger(__name__)

    # Resolve language list
    try:
        config = load_dak_config(repo_root)
        lang_codes = get_language_codes(config)
        if not lang_codes:
            lang_codes = list(_FALLBACK_LANGUAGES)
    except DakConfigError:
        lang_codes = list(_FALLBACK_LANGUAGES)

    # Resolve component list
    components = discover_components(repo_root)
    if not components:
        logger.warning("No *.pot files found — nothing to GPT-translate")
        return 0

    if component_filter:
        components = [c for c in components if c.slug == component_filter]
        if not components:
            logger.error("Component %r not found among discovered components", component_filter)
            return 1

    active_languages = [language_filter] if language_filter else lang_codes

    errors = 0
    for comp in components:
        for lang in active_languages:
            po_path = comp.po_path(lang)
            if not po_path.exists():
                logger.info("  %s/%s.po not found — skipping (no translations yet)", comp.slug, lang)
                continue
            ok = translate_po_file(po_path, lang, provider, model, batch_size)
            if not ok:
                errors += 1

    if errors:
        logger.warning("%d component/language pairs failed GPT translation", errors)
    else:
        logger.info("GPT translation pass complete")
    return 1 if errors else 0


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="pull_gpt_translations.py",
        description="Translate untranslated .po strings using AI (gpt-po-translator)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--repo-root", default=".", help="Repository root (default: .)")
    parser.add_argument("--component", default="", help="Restrict to one component slug")
    parser.add_argument("--language", default="", help="Restrict to one language code")
    parser.add_argument(
        "--provider",
        default="",
        choices=list(_PROVIDER_ENV) + [""],
        help="AI provider. Default: auto-detected from env vars.",
    )
    parser.add_argument("--model", default="", help="Model override (e.g. gpt-4o-mini)")
    parser.add_argument(
        "--batch-size", type=int, default=50,
        help="Batch size for bulk translation (default: 50)",
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

    # Determine provider — explicit flag overrides auto-detection
    if args.provider:
        provider = args.provider
        env_var = _PROVIDER_ENV.get(provider, "")
        token = get_optional_env_token(env_var) if env_var else ""
        if not token:
            logger.info(
                "Provider %r selected but %s is not set — skipping GPT translation",
                provider,
                env_var or "(no env var)",
            )
            return 0
    else:
        provider = _detect_provider()
        if not provider:
            logger.info(
                "No AI provider key found (OPENAI_API_KEY / ANTHROPIC_API_KEY / "
                "DEEPSEEK_API_KEY) — skipping GPT translation"
            )
            return 0

    # Sanitize optional filters
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

    model: Optional[str] = args.model if args.model else None

    logger.info("GPT translation provider: %s", provider)

    return run_gpt_translations(
        repo_root=repo_root,
        component_filter=component_filter,
        language_filter=language_filter,
        provider=provider,
        model=model,
        batch_size=args.batch_size,
    )


if __name__ == "__main__":
    sys.exit(main())
