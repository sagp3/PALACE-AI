"""
PALACE AI

Embedding Model Interface
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from core.chunk import Chunk


class EmbeddingModel(ABC):
    """
    Base interface for embedding providers.
    """

    @abstractmethod
    def embed(
        self,
        chunks: list[Chunk],
    ) -> list[list[float]]:
        """
        Generates embeddings for multiple chunks.
        """
        raise NotImplementedError

    @abstractmethod
    def embed_query(
        self,
        query: str,
    ) -> list[float]:
        """
        Generates an embedding for a search query.
        """
        raise NotImplementedError
