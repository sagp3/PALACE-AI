"""
PALACE AI

Ollama LLM
"""

from __future__ import annotations

from ollama import Client

from core.llm import LLM


class OllamaLLM(LLM):
    """
    Ollama implementation.
    """

    def __init__(
        self,
        model: str = "qwen3:8b",
        host: str = "http://localhost:11434",
    ) -> None:
        self._client = Client(host=host)

        self._model = model

    def generate(
        self,
        prompt: str,
    ) -> str:
        """
        Generates a response using Ollama.
        """

        response = self._client.chat(
            model=self._model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"].strip()
