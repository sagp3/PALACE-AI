"""
PALACE AI

Vector Store Interface
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from chromadb.api.types import QueryResult

from core.chunk import Chunk


class VectorStore(ABC):
    """
    Base interface for vector databases.
    """

    @abstractmethod
    def add(
        self,
        chunks: list[Chunk],
        embeddings: list[list[float]],
    ) -> None:
        """
        Stores vectors in the database.
        """
        raise NotImplementedError

    @abstractmethod
    def search(
        self,
        embedding: list[float],
        top_k: int = 5,
    ) -> QueryResult:
        """
        Performs semantic search.
        """
        raise NotImplementedError
