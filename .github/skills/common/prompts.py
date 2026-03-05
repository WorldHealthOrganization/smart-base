"""
Prompt loader for DAK skill actions.

Prompts are stored as Markdown files with ``{variable}`` placeholders.
``load_prompt()`` reads the file and substitutes variables using
``str.format_map``.

Usage:
    from common.prompts import load_prompt

    prompt = load_prompt("bpmn_author", "create_or_edit_bpmn",
                         bpmn_xml="<definitions ...>",
                         user_request="Add a pharmacy lane")
"""

import os
from pathlib import Path
from typing import Any


# Root of the skills directory (parent of common/)
_SKILLS_ROOT = Path(__file__).resolve().parent.parent


def load_prompt(skill_name: str, prompt_name: str, **variables: Any) -> str:
    """Load a ``.md`` prompt template and fill ``{variable}`` placeholders.

    The file is resolved as::

        .github/skills/<skill_name>/prompts/<prompt_name>.md

    Falls back to::

        .github/skills/common/prompts/<prompt_name>.md

    Args:
        skill_name: Skill directory name (e.g. ``"bpmn_author"``).
        prompt_name: Prompt file stem (without ``.md``).
        **variables: Substitution values for ``{key}`` placeholders.

    Returns:
        The rendered prompt string.

    Raises:
        FileNotFoundError: If neither skill-specific nor common prompt exists.
    """
    skill_path = _SKILLS_ROOT / skill_name / "prompts" / f"{prompt_name}.md"
    common_path = _SKILLS_ROOT / "common" / "prompts" / f"{prompt_name}.md"

    for path in (skill_path, common_path):
        if path.is_file():
            template = path.read_text(encoding="utf-8")
            return template.format_map(_SafeDict(variables))

    raise FileNotFoundError(
        f"Prompt '{prompt_name}.md' not found in "
        f"'{skill_path}' or '{common_path}'"
    )


class _SafeDict(dict):
    """dict subclass that returns ``{key}`` for missing keys instead of raising."""

    def __missing__(self, key: str) -> str:
        return "{" + key + "}"
