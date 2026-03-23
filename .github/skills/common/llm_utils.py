"""
DAK LLM utilities — thin helpers around LiteLLM.

LiteLLM (https://github.com/BerriAI/litellm, MIT License) is the trusted
external library that provides multi-provider LLM support (OpenAI, Anthropic,
Google, etc.) via a single ``completion()`` call.  This module adds only
DAK-specific environment-variable bridging and a JSON-extraction helper.

No custom LLM facade to maintain — callers use ``litellm.completion()``
directly via the convenience wrapper below.

Usage:
    from common.llm_utils import dak_completion, parse_json_response

    text = dak_completion("Explain BPMN swimlanes")
    data = dak_completion(prompt, structured_output=True)
"""

import json
import logging
import os
from typing import Any, Dict, List, Optional, Union

logger = logging.getLogger(__name__)


def get_llm_config() -> tuple:
    """Return ``(api_key, model)`` from DAK environment variables.

    Reads:
        ``DAK_LLM_API_KEY`` — LLM provider API key (repo secret or ``.env``).
        ``DAK_LLM_MODEL``   — model identifier (default ``gpt-4o``).
    """
    api_key = os.environ.get("DAK_LLM_API_KEY", "")
    model = os.environ.get("DAK_LLM_MODEL", "gpt-4o")
    return api_key, model


def is_llm_available() -> bool:
    """Return True if a DAK LLM API key is configured."""
    return bool(os.environ.get("DAK_LLM_API_KEY", ""))


def dak_completion(
    prompt: str,
    *,
    system_prompt: str = "",
    structured_output: bool = False,
    temperature: float = 0.2,
    api_key: Optional[str] = None,
    model: Optional[str] = None,
) -> Union[str, Dict[str, Any]]:
    """Call an LLM via LiteLLM with DAK environment defaults.

    This is a thin convenience wrapper around ``litellm.completion()``
    that reads ``DAK_LLM_API_KEY`` / ``DAK_LLM_MODEL`` from the
    environment so callers don't repeat the boilerplate.

    Args:
        prompt: User prompt text.
        system_prompt: Optional system-level instruction.
        structured_output: When True, parse the response as JSON.
        temperature: Sampling temperature.
        api_key: Override for ``DAK_LLM_API_KEY``.
        model: Override for ``DAK_LLM_MODEL``.

    Returns:
        ``str`` (plain text) or ``dict`` (when *structured_output* is True).

    Raises:
        RuntimeError: If no API key is available.
        ImportError: If ``litellm`` is not installed.
    """
    _api_key = api_key or os.environ.get("DAK_LLM_API_KEY", "")
    _model = model or os.environ.get("DAK_LLM_MODEL", "gpt-4o")

    if not _api_key:
        raise RuntimeError(
            "DAK_LLM_API_KEY not set — cannot call LLM. "
            "Set the key in a repo secret or local .env file."
        )

    try:
        import litellm
    except ImportError as exc:
        raise ImportError(
            "litellm is required for LLM features. "
            "Install it with: pip install 'litellm>=1.0.0'"
        ) from exc

    messages: List[Dict[str, str]] = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    logger.info("LLM request: model=%s tokens≈%d", _model, len(prompt) // 4)

    response = litellm.completion(
        model=_model,
        messages=messages,
        temperature=temperature,
        api_key=_api_key,
    )

    text: str = response.choices[0].message.content.strip()

    if structured_output:
        return parse_json_response(text)
    return text


def parse_json_response(text: str) -> Dict[str, Any]:
    """Best-effort JSON extraction from LLM response text.

    Handles bare JSON, ``json`` code-fenced blocks, and generic fences.
    Falls back to ``{"raw": text}`` when parsing fails.
    """
    # Try direct parse first
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    # Try extracting from markdown code fence
    for fence in ("```json", "```"):
        if fence in text:
            start = text.index(fence) + len(fence)
            end = text.index("```", start)
            try:
                return json.loads(text[start:end].strip())
            except (json.JSONDecodeError, ValueError):
                pass
    # Last resort: return as dict with raw text
    return {"raw": text}

