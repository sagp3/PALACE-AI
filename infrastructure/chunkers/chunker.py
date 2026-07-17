"""
PALACE AI

Chunker Interface
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from core.chunk import Chunk
from infrastructure.raw_document import RawDocument


class Chunker(ABC):
    """
    Base interface for all chunkers.
    """

    @abstractmethod
    def split(
        self,
        document: RawDocument,
    ) -> list[Chunk]:
        """
        Splits a RawDocument into searchable chunks.
        """
        raise NotImplementedError
