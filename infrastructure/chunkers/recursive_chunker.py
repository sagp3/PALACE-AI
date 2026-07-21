"""
PALACE AI

Recursive Chunker
"""

from __future__ import annotations

from langchain_text_splitters import RecursiveCharacterTextSplitter

from core.chunk import Chunk
from infrastructure.raw_document import RawDocument

from .chunker import Chunker


class RecursiveChunker(Chunker):
    """
    Splits a RawDocument into overlapping chunks.
    """

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ) -> None:
        self._splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    def split(
        self,
        document: RawDocument,
    ) -> list[Chunk]:
        parts = self._splitter.split_text(document.content)

        chunks: list[Chunk] = []

        total = len(parts)

        for index, content in enumerate(parts, start=1):
            chunks.append(
                Chunk(
                    content=content,
                    source_document=document.filename,
                    chunk_index=index,
                    total_chunks=total,
                    metadata=document.metadata.copy(),
                )
            )

        return chunks
