#!/usr/bin/env python3
"""
translation_config.py — Authoritative configuration reader for translation pipeline.

Reads dak.json, discovers translation components by scanning for *.pot files,
and provides language/service configuration to all other translation scripts.

All scripts that need language codes, component paths, or service configuration
MUST import from this module.  No script may contain hardcoded language lists
or hardcoded component paths.
"""

import json
import logging
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Exceptions
# ---------------------------------------------------------------------------

class DakConfigError(ValueError):
    """Raised when dak.json is missing, unreadable, or structurally invalid."""


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class LanguageEntry:
    code: str
    name: str
    direction: str          # "ltr" or "rtl"
    plural: str = ""


@dataclass
class ServiceConfig:
    name: str
    enabled: bool
    url: str = ""
    extra: Dict[str, Any] = field(default_factory=dict)


@dataclass
class TranslationComponent:
    """One translation component derived from a *.pot file."""
    slug: str               # e.g. "fsh-base"
    pot_path: Path          # absolute path to the .pot file
    translations_dir: Path  # directory that contains .po files (same dir as .pot)

    def po_path(self, lang_code: str) -> Path:
        """Return the expected path for a .po file for this component and language."""
        return self.translations_dir / f"{lang_code}.po"


@dataclass
class DakConfig:
    raw: Dict[str, Any]
    source_language: str
    languages: List[LanguageEntry]
    services: Dict[str, ServiceConfig]


# ---------------------------------------------------------------------------
# Loading and validation
# ---------------------------------------------------------------------------

def load_dak_config(repo_root: Path) -> DakConfig:
    """
    Load and validate dak.json from *repo_root*.

    Raises:
        DakConfigError: if dak.json is missing, not valid JSON, or lacks required fields.
    """
    dak_path = repo_root / "dak.json"
    if not dak_path.exists():
        raise DakConfigError(f"dak.json not found at {dak_path}")

    try:
        raw = json.loads(dak_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise DakConfigError(f"dak.json is not valid JSON: {exc}") from exc

    if not isinstance(raw, dict):
        raise DakConfigError("dak.json must be a JSON object")

    translations_raw = raw.get("translations")
    if not isinstance(translations_raw, dict):
        # Missing translations block — return config with empty language list so
        # callers can handle gracefully (e.g. log a warning and skip).
        return DakConfig(
            raw=raw,
            source_language="en",
            languages=[],
            services={},
        )

    source_lang = translations_raw.get("sourceLanguage", "en")
    if not isinstance(source_lang, str) or not source_lang:
        raise DakConfigError("dak.json translations.sourceLanguage must be a non-empty string")

    languages = _parse_languages(translations_raw.get("languages", []))
    services = _parse_services(translations_raw.get("services", {}))

    return DakConfig(raw=raw, source_language=source_lang, languages=languages, services=services)


def _parse_languages(raw_langs: Any) -> List[LanguageEntry]:
    if not isinstance(raw_langs, list):
        raise DakConfigError("dak.json translations.languages must be an array")
    entries: List[LanguageEntry] = []
    for i, item in enumerate(raw_langs):
        if not isinstance(item, dict):
            raise DakConfigError(f"translations.languages[{i}] must be an object")
        code = item.get("code")
        name = item.get("name")
        direction = item.get("direction", "ltr")
        if not code or not isinstance(code, str):
            raise DakConfigError(f"translations.languages[{i}].code is required")
        if not name or not isinstance(name, str):
            raise DakConfigError(f"translations.languages[{i}].name is required")
        entries.append(LanguageEntry(
            code=code,
            name=name,
            direction=direction,
            plural=item.get("plural", ""),
        ))
    return entries


def _parse_services(raw_services: Any) -> Dict[str, ServiceConfig]:
    if not isinstance(raw_services, dict):
        return {}
    result: Dict[str, ServiceConfig] = {}
    for svc_name, svc_cfg in raw_services.items():
        if not isinstance(svc_cfg, dict):
            continue
        enabled = bool(svc_cfg.get("enabled", False))
        url = svc_cfg.get("url", "")
        extra = {k: v for k, v in svc_cfg.items() if k not in ("enabled", "url")}
        result[svc_name] = ServiceConfig(name=svc_name, enabled=enabled, url=url, extra=extra)
    return result


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def get_languages(config: DakConfig) -> List[LanguageEntry]:
    """Return target language list from dak.json#translations.languages."""
    return list(config.languages)


def get_language_codes(config: DakConfig) -> List[str]:
    """Return just the language codes."""
    return [lang.code for lang in config.languages]


def get_enabled_services(config: DakConfig) -> Dict[str, ServiceConfig]:
    """Return dict of enabled translation services and their config."""
    return {name: svc for name, svc in config.services.items() if svc.enabled}


def get_project_slug(github_org: str, repo_name: str) -> str:
    """
    Derive translation project slug from GitHub org and repo name.

    Returns '{github_org}-{repo_name}' lowercased and with non-alphanumeric
    characters (except hyphens) replaced by hyphens.
    """
    raw = f"{github_org}-{repo_name}".lower()
    return re.sub(r"[^a-z0-9-]", "-", raw)


# ---------------------------------------------------------------------------
# Component discovery
# ---------------------------------------------------------------------------

def discover_components(repo_root: Path) -> List[TranslationComponent]:
    """
    Scan repo_root for all *.pot files and derive component definitions.

    Component slug derivation algorithm:
    - Take path segments between 'input/' and '/translations/' plus the .pot stem
    - Join with '-', lowercase, replace non-alphanumeric characters with '-'

    For a .pot not under input/…/translations/, use the stem directly.

    Returns components sorted by pot_path for deterministic ordering.
    """
    components: List[TranslationComponent] = []

    for pot_file in sorted(repo_root.rglob("*.pot")):
        # Skip anything in .git or build output directories
        parts = pot_file.parts
        if any(p.startswith(".") or p in ("fsh-generated", "output", "temp", ".git") for p in parts):
            continue

        slug = _derive_component_slug(pot_file, repo_root)
        translations_dir = pot_file.parent
        components.append(TranslationComponent(
            slug=slug,
            pot_path=pot_file,
            translations_dir=translations_dir,
        ))
        logger.debug("Discovered component %r → %s", slug, pot_file)

    return components


def _derive_component_slug(pot_file: Path, repo_root: Path) -> str:
    """
    Derive a component slug from a .pot file path.

    Algorithm:
      input/fsh/translations/base.pot           → fsh-base
      input/images-source/translations/foo.pot  → images-source-foo
      input/scripts/translations/scripts.pot    → scripts-scripts
      anything/else/file.pot                    → file   (stem only)
    """
    try:
        rel = pot_file.relative_to(repo_root)
    except ValueError:
        return re.sub(r"[^a-z0-9]+", "-", pot_file.stem.lower()).strip("-")

    rel_parts = list(rel.parts)
    stem = pot_file.stem

    # Find the 'translations' directory level
    try:
        trans_idx = rel_parts.index("translations")
    except ValueError:
        # Not under a translations/ directory — just use the stem
        return re.sub(r"[^a-z0-9]+", "-", stem.lower()).strip("-")

    # Collect path segments between 'input/' (if present) and 'translations/'
    try:
        input_idx = rel_parts.index("input")
        middle = rel_parts[input_idx + 1:trans_idx]
    except ValueError:
        middle = rel_parts[:trans_idx]

    parts = middle + [stem]
    raw = "-".join(parts).lower()
    return re.sub(r"[^a-z0-9]+", "-", raw).strip("-")


# ---------------------------------------------------------------------------
# gettext setup helper (used by scripts to load runtime translations)
# ---------------------------------------------------------------------------

def setup_gettext(script_file: str):
    """
    Set up Python gettext for a script, loading .po translations from the
    'translations/' directory adjacent to the script.

    Usage in scripts:
        from translation_config import setup_gettext
        _ = setup_gettext(__file__)

    Falls back to identity function if no .mo files are available.
    """
    import gettext as _gettext
    import locale
    import os

    script_dir = Path(script_file).resolve().parent
    locale_dir = script_dir / "translations"

    lang = os.environ.get("LANG", "").split(".")[0].split("_")[0] or "en"

    try:
        t = _gettext.translation(
            domain="scripts",
            localedir=str(locale_dir),
            languages=[lang, "en"],
        )
        return t.gettext
    except FileNotFoundError:
        return lambda s: s
