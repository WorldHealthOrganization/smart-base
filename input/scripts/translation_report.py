#!/usr/bin/env python3
"""
translation_report.py — Generate a translation completeness report.

Scans all .po files in the repository and produces
input/pagecontent/translation-status.md showing the percentage of translated
strings per language × component, with color-coded indicators:

  🟢  ≥ 80 % translated
  🟡  50 – 79 % translated
  🔴  < 50 % translated
  ⬜  no .po file present

Usage:
    python translation_report.py [--repo-root DIR]
                                 [--output PATH]

Exit codes:
    0  Report written successfully
    1  Errors reading .po files (report still written with available data)
"""

import argparse
import logging
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from translation_config import (
    DakConfigError,
    TranslationComponent,
    discover_components,
    get_languages,
    load_dak_config,
)

_FALLBACK_LANGUAGES = [
    ("ar", "Arabic"),
    ("zh", "Chinese (Simplified)"),
    ("fr", "French"),
    ("ru", "Russian"),
    ("es", "Spanish"),
]

_DEFAULT_OUTPUT = Path("input/pagecontent/translation-status.md")


# ---------------------------------------------------------------------------
# .po parsing
# ---------------------------------------------------------------------------

def _parse_po_stats(po_path: Path) -> Tuple[int, int]:
    """
    Return (total_strings, translated_strings) for a .po file.

    A string is considered translated when its msgstr is non-empty and the
    entry is not marked fuzzy.
    """
    try:
        content = po_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return 0, 0

    total = 0
    translated = 0
    current_msgid = ""
    current_msgstr_parts: List[str] = []
    in_msgid = False
    in_msgstr = False
    is_fuzzy = False

    def _flush():
        nonlocal total, translated, current_msgid, current_msgstr_parts, is_fuzzy
        if current_msgid == "":
            # This is the header entry — skip
            current_msgid = ""
            current_msgstr_parts = []
            is_fuzzy = False
            return
        if current_msgid:
            total += 1
            msgstr = "".join(current_msgstr_parts).strip()
            if msgstr and not is_fuzzy:
                translated += 1
        current_msgid = ""
        current_msgstr_parts = []
        is_fuzzy = False

    for raw_line in content.splitlines():
        line = raw_line.strip()
        if line.startswith("#,") and "fuzzy" in line:
            is_fuzzy = True
            continue
        if line.startswith("#"):
            continue
        if line.startswith("msgid "):
            if in_msgstr:
                _flush()
            in_msgid = True
            in_msgstr = False
            current_msgid = line[6:].strip().strip('"')
        elif line.startswith("msgstr "):
            in_msgid = False
            in_msgstr = True
            val = line[7:].strip().strip('"')
            current_msgstr_parts = [val] if val else []
        elif line.startswith('"') and line.endswith('"'):
            inner = line[1:-1]
            if in_msgid:
                current_msgid += inner
            elif in_msgstr:
                current_msgstr_parts.append(inner)
        elif not line:
            if in_msgstr:
                _flush()
            in_msgid = False
            in_msgstr = False

    if in_msgstr:
        _flush()

    return total, translated


# ---------------------------------------------------------------------------
# Completeness calculation
# ---------------------------------------------------------------------------

def _pct(translated: int, total: int) -> float:
    if total == 0:
        return 0.0
    return round(100.0 * translated / total, 1)


def _color_indicator(pct: Optional[float]) -> str:
    """Return a color-coded emoji for the given completion percentage."""
    if pct is None:
        return "⬜"
    if pct >= 80.0:
        return "🟢"
    if pct >= 50.0:
        return "🟡"
    return "🔴"


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def generate_report(repo_root: Path, output_path: Path) -> int:
    """
    Generate translation-status.md and write it to *output_path*.

    Returns 0 on success, 1 if any .po files could not be read.
    """
    logger = logging.getLogger(__name__)
    errors = 0

    # Resolve language list
    try:
        config = load_dak_config(repo_root)
        languages = [(lang.code, lang.name) for lang in get_languages(config)]
        if not languages:
            languages = _FALLBACK_LANGUAGES
    except DakConfigError as exc:
        logger.warning("dak.json unavailable (%s) — using fallback languages", exc)
        languages = _FALLBACK_LANGUAGES

    # Discover components
    components = discover_components(repo_root)
    if not components:
        logger.warning("No *.pot files found — report will be empty")

    # Collect stats: {component_slug: {lang_code: (total, translated)}}
    stats: Dict[str, Dict[str, Tuple[int, int]]] = {}
    for comp in components:
        comp_stats: Dict[str, Tuple[int, int]] = {}
        for lang_code, _ in languages:
            po = comp.po_path(lang_code)
            if po.exists():
                total, translated = _parse_po_stats(po)
                if total == 0 and po.stat().st_size > 0:
                    errors += 1
                comp_stats[lang_code] = (total, translated)
            else:
                comp_stats[lang_code] = (-1, -1)  # file absent
        stats[comp.slug] = comp_stats

    # ── Build markdown ───────────────────────────────────────────────────────
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lang_headers = " | ".join(f"{name}<br>(`{code}`)" for code, name in languages)
    lang_separator = " | ".join("---" for _ in languages)

    lines: List[str] = [
        "# Translation Status",
        "",
        f"*Generated: {timestamp}*",
        "",
        "## Legend",
        "",
        "| Symbol | Meaning |",
        "| --- | --- |",
        "| 🟢 | ≥ 80% translated |",
        "| 🟡 | 50–79% translated |",
        "| 🔴 | < 50% translated |",
        "| ⬜ | No .po file yet |",
        "",
        "## Completeness by Component and Language",
        "",
        f"| Component | {lang_headers} |",
        f"| --- | {lang_separator} |",
    ]

    for comp in components:
        comp_cells: List[str] = []
        for lang_code, _ in languages:
            total, translated = stats[comp.slug].get(lang_code, (-1, -1))
            if total < 0:
                # File absent
                comp_cells.append("⬜")
            elif total == 0:
                comp_cells.append("⬜ (empty)")
            else:
                pct = _pct(translated, total)
                indicator = _color_indicator(pct)
                comp_cells.append(f"{indicator} {pct:.0f}%<br>({translated}/{total})")
        cells_str = " | ".join(comp_cells)
        lines.append(f"| `{comp.slug}` | {cells_str} |")

    # Summary row
    summary_cells: List[str] = []
    for lang_code, _ in languages:
        total_sum = sum(
            v[0] for v in (stats[c.slug].get(lang_code, (-1, -1)) for c in components)
            if v[0] >= 0
        )
        trans_sum = sum(
            v[1] for v in (stats[c.slug].get(lang_code, (-1, -1)) for c in components)
            if v[0] >= 0
        )
        if total_sum == 0:
            summary_cells.append("⬜")
        else:
            pct = _pct(trans_sum, total_sum)
            indicator = _color_indicator(pct)
            summary_cells.append(f"**{indicator} {pct:.0f}%**<br>({trans_sum}/{total_sum})")
    lines.append(f"| **Total** | {' | '.join(summary_cells)} |")
    lines.append("")

    # Per-language detail sections
    lines.append("## Detail by Language")
    lines.append("")
    for lang_code, lang_name in languages:
        lang_total = 0
        lang_translated = 0
        rows: List[str] = []
        for comp in components:
            total, translated = stats[comp.slug].get(lang_code, (-1, -1))
            if total < 0:
                rows.append(f"| `{comp.slug}` | ⬜ absent | — |")
            elif total == 0:
                rows.append(f"| `{comp.slug}` | ⬜ empty | 0/0 |")
            else:
                pct = _pct(translated, total)
                indicator = _color_indicator(pct)
                rows.append(f"| `{comp.slug}` | {indicator} {pct:.0f}% | {translated}/{total} |")
                lang_total += total
                lang_translated += translated

        overall_pct = _pct(lang_translated, lang_total) if lang_total else 0.0
        overall_indicator = _color_indicator(overall_pct) if lang_total else "⬜"
        lines += [
            f"### {lang_name} (`{lang_code}`) — {overall_indicator} {overall_pct:.0f}%",
            "",
            "| Component | Status | Progress |",
            "| --- | --- | --- |",
        ]
        lines.extend(rows)
        lines.append("")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")
    logger.info("Translation status report written to %s", output_path)
    return 1 if errors else 0


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="translation_report.py",
        description="Generate translation completeness report",
    )
    parser.add_argument("--repo-root", default=".", help="Repository root (default: .)")
    parser.add_argument(
        "--output",
        default=str(_DEFAULT_OUTPUT),
        help=f"Output file path (default: {_DEFAULT_OUTPUT})",
    )
    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
    )
    args = _parse_args(argv)
    repo_root = Path(args.repo_root).resolve()
    if not repo_root.is_dir():
        sys.exit(f"ERROR: --repo-root {repo_root!r} is not a directory")
    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = repo_root / output_path
    return generate_report(repo_root, output_path)


if __name__ == "__main__":
    sys.exit(main())
