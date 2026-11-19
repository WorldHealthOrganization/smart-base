#!/usr/bin/env python3
"""
Where a repository's DAK declaration lives: the ``dak`` section of
``contentTypes`` in the root ``index.config.json``.

It was ``dak.json`` until 2026-10-24, when the owner moved it into the index
(bean ``folio-assistant-cz17``). The section's presence is what makes a
repository a DAK, as the file's presence did. Every script reads and writes it
through this module, so the location is stated once.

Only one spelling is read: a ``dak.json`` beside the index is ignored, so
"migrated" and "not migrated" stay distinguishable.

The one bridge is :func:`adopt_legacy_dak_json`, run once by the build
workflow (``python3 input/scripts/dak_index.py --adopt-legacy .``). An IG that
calls the shared workflow and still carries ``dak.json`` gets its file folded
into the index in the CI workspace, with a warning, so its DAK steps keep
running until the IG itself is migrated. Nothing is committed back.
"""

import json
from pathlib import Path
from typing import Any, Dict, Optional, Union

DAK_INDEX_FILE = "index.config.json"
DAK_SECTION = "dak"
INDEX_SCHEMA = "folio-index-config/v1"

PathLike = Union[str, Path]


def dak_index_path(repo_root: PathLike = ".") -> Path:
    """The index file that holds (or would hold) the DAK section."""
    return Path(repo_root) / DAK_INDEX_FILE


def read_dak_section(repo_root: PathLike = ".") -> Optional[Dict[str, Any]]:
    """
    The DAK declaration, or ``None`` when the repository has no index, the
    index has no ``dak`` section, or the index cannot be parsed.

    Callers that must tell "not a DAK" from "unreadable" use
    :func:`load_dak_section_strict`.
    """
    try:
        return load_dak_section_strict(repo_root)
    except (ValueError, OSError):
        return None


def load_dak_section_strict(repo_root: PathLike = ".") -> Optional[Dict[str, Any]]:
    """
    Like :func:`read_dak_section`, but an index that is unreadable, or a
    section that is not an object, raises ``ValueError``. Absent is still
    ``None``.
    """
    path = dak_index_path(repo_root)
    if not path.is_file():
        return None
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"{path} is not valid JSON: {exc}") from exc
    if not isinstance(raw, dict):
        raise ValueError(f"{path} must be a JSON object")
    sections = raw.get("contentTypes")
    if sections is None:
        return None
    if not isinstance(sections, dict):
        raise ValueError(f"{path}: contentTypes must be an object")
    section = sections.get(DAK_SECTION)
    if section is None:
        return None
    if not isinstance(section, dict):
        raise ValueError(f"{path}: contentTypes.{DAK_SECTION} must be an object")
    return section


def has_dak_section(repo_root: PathLike = ".") -> bool:
    """True when the repository declares itself a DAK."""
    return read_dak_section(repo_root) is not None


def write_dak_section(data: Dict[str, Any], repo_root: PathLike = ".") -> Path:
    """
    Write ``data`` as the ``dak`` section, keeping everything else in the
    index as it was. Creates a minimal index when there is none.
    """
    path = dak_index_path(repo_root)
    if path.is_file():
        raw = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            raise ValueError(f"{path} must be a JSON object")
    else:
        raw = {"$schema": INDEX_SCHEMA, "instances": []}
    sections = raw.get("contentTypes")
    if not isinstance(sections, dict):
        sections = {}
    sections[DAK_SECTION] = data
    raw["contentTypes"] = sections
    path.write_text(json.dumps(raw, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


LEGACY_DAK_FILE = "dak.json"


def adopt_legacy_dak_json(repo_root: PathLike = ".") -> bool:
    """
    Fold a pre-2026-10-24 ``dak.json`` into the index's ``dak`` section, for
    the CI workspace only. Returns True when it did.

    It does nothing when the index already has the section (the index wins),
    or when there is no legacy file. A legacy file that is not a JSON object
    raises ``ValueError``: a broken declaration is not "not a DAK".
    """
    legacy = Path(repo_root) / LEGACY_DAK_FILE
    if not legacy.is_file() or load_dak_section_strict(repo_root) is not None:
        return False
    try:
        data = json.loads(legacy.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"{legacy} is not valid JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"{legacy} must be a JSON object")
    write_dak_section(data, repo_root)
    return True


if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    if args and args[0] == "--adopt-legacy":
        root = args[1] if len(args) > 1 else "."
        if adopt_legacy_dak_json(root):
            print(
                f"::warning::{LEGACY_DAK_FILE} is deprecated; it was read into "
                f"{DAK_INDEX_FILE} contentTypes.{DAK_SECTION} for this build only. "
                "Move it there and delete the file."
            )
        sys.exit(0)
    root = args[0] if args else "."
    # Exit 0 when the repository is a DAK, 1 when it is not: a shell test.
    sys.exit(0 if has_dak_section(root) else 1)
