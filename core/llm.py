"""
PALACE AI

LLM Interface
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class LLM(ABC):
    """
    Base interface for Large Language Models.
    """

    @abstractmethod
    def generate(
        self,
        prompt: str,
    ) -> str:
        """
        Generates a response from a prompt.
        """
        raise NotImplementedError
