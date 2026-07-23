"""
PALACE AI

Chroma Vector Store
"""

from __future__ import annotations

from datetime import datetime

from chromadb.api.types import QueryResult

import chromadb
from core.chunk import Chunk

from .vector_store import VectorStore


class ChromaVectorStore(VectorStore):
    """
    ChromaDB implementation.
    """

    def __init__(
        self,
        collection_name: str = "palace_ai",
    ) -> None:
        self._client = chromadb.PersistentClient(
            path="chromadb",
        )

        self._collection = self._client.get_or_create_collection(
            name=collection_name,
        )

    def add(
        self,
        chunks: list[Chunk],
        embeddings: list[list[float]],
    ) -> None:
        """
        Stores chunks and their embeddings.
        """

        self._collection.add(
            ids=[chunk.id for chunk in chunks],
            embeddings=embeddings,
            documents=[chunk.content for chunk in chunks],
            metadatas=[
                {
                    "document": chunk.source_document,
                    "chunk": chunk.chunk_index,
                    "total_chunks": chunk.total_chunks,
                    "indexed_at": datetime.utcnow().isoformat(),
                    **chunk.metadata,
                }
                for chunk in chunks
            ],
        )

    def search(
        self,
        embedding: list[float],
        top_k: int = 20,
        document: str | None = None,
    ) -> QueryResult:
        """
        Performs semantic search.

        If a document is provided, the search
        is restricted to that document.
        """

        kwargs = {
            "query_embeddings": [embedding],
            "n_results": top_k,
            "include": [
                "documents",
                "metadatas",
                "distances",
            ],
        }

        if document is not None:
            kwargs["where"] = {
                "document": document,
            }

        return self._collection.query(**kwargs)

    def delete_document(
        self,
        filename: str,
    ) -> None:
        """
        Deletes every chunk that belongs
        to the specified document.
        """

        self._collection.delete(
            where={
                "document": filename,
            }
        )
