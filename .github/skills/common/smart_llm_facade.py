"""
SMART LLM Facade — thin wrapper around LiteLLM for DAK skill actions.

Copy-lifted with gratitude and attribution from:
  https://github.com/jtlicardo/bpmn-assistant (MIT License)

Original: LLMFacade class by jtlicardo
Adapted for WHO SMART Guidelines DAK skill library.

Usage:
    from common.smart_llm_facade import SmartLLMFacade

    llm = SmartLLMFacade(api_key="sk-...", model="gpt-4o")
    answer = llm.call("Explain BPMN swimlanes")
    structured = llm.call(prompt, structured_output=True)
"""

import json
import logging
import os
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)


class SmartLLMFacade:
    """Minimal LLM facade using LiteLLM for multi-provider support."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: Optional[str] = None,
    ) -> None:
        self.api_key = api_key or os.environ.get("DAK_LLM_API_KEY", "")
        self.model = model or os.environ.get("DAK_LLM_MODEL", "gpt-4o")

    def is_available(self) -> bool:
        """Return True if an API key is configured."""
        return bool(self.api_key)

    def call(
        self,
        prompt: str,
        *,
        system_prompt: str = "",
        structured_output: bool = False,
        temperature: float = 0.2,
    ) -> Any:
        """Send a prompt to the configured LLM and return the response.

        Args:
            prompt: User prompt text.
            system_prompt: Optional system-level instruction.
            structured_output: When True, attempt to parse the response as JSON.
            temperature: Sampling temperature.

        Returns:
            str or dict depending on *structured_output*.

        Raises:
            RuntimeError: If no API key is configured.
            ImportError: If litellm is not installed.
        """
        if not self.api_key:
            raise RuntimeError(
                "DAK_LLM_API_KEY not set — cannot call LLM. "
                "Set the key in a repo secret or local .env file."
            )

        try:
            import litellm  # noqa: F811
        except ImportError as exc:
            raise ImportError(
                "litellm is required for LLM features. "
                "Install it with: pip install 'litellm>=1.0.0'"
            ) from exc

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        logger.info("LLM request: model=%s tokens≈%d", self.model, len(prompt) // 4)

        response = litellm.completion(
            model=self.model,
            messages=messages,
            temperature=temperature,
            api_key=self.api_key,
        )

        text: str = response.choices[0].message.content.strip()

        if structured_output:
            return self._parse_json(text)
        return text

    @staticmethod
    def _parse_json(text: str) -> Dict[str, Any]:
        """Best-effort JSON extraction from LLM response text."""
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
