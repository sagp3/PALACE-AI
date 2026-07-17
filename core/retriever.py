"""
PALACE AI

Retriever Interface
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from core.chunk import Chunk


class Retriever(ABC):
    """
    Contract for semantic document retrieval.
    """

    @abstractmethod
    def search(
        self,
        query: str,
        top_k: int = 5,
    ) -> list[Chunk]:
        """
        Returns the most relevant chunks for a query.
        """
        raise NotImplementedError
