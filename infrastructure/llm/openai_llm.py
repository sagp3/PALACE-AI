"""
PALACE AI

OpenAI LLM
"""

from __future__ import annotations

from core.llm import LLM
from infrastructure.openai_client import OpenAIClient


class OpenAILLM(LLM):
    """
    OpenAI implementation.
    """

    def __init__(
        self,
        model: str = "gpt-4.1-mini",
    ) -> None:
        self._client = OpenAIClient.get_client()
        self._model = model

    def generate(
        self,
        prompt: str,
    ) -> str:
        response = self._client.chat.completions.create(
            model=self._model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are PALACE AI, an enterprise document assistant. "
                        "Answer only using the provided context. "
                        "If the information is not available, clearly say so."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=0.2,
        )

        return response.choices[0].message.content.strip()
