"""
PALACE AI

Knowledge Retriever
"""

from __future__ import annotations

from application.document_context import DocumentContext
from core.chunk import Chunk
from infrastructure.embeddings.openai_embedding_model import OpenAIEmbeddingModel
from infrastructure.vectorstores.chroma_vector_store import ChromaVectorStore


class KnowledgeRetriever:
    """
    Retrieves relevant chunks from ChromaDB.
    """

    def __init__(self) -> None:
        self._embedding_model = OpenAIEmbeddingModel()

        self._vector_store = ChromaVectorStore()

        self._context = DocumentContext()

    def retrieve(
        self,
        question: str,
        top_k: int = 5,
    ) -> list[Chunk]:
        """
        Retrieves diversified chunks.
        """

        embedding = self._embedding_model.embed_query(question)

        results = self._vector_store.search(
            embedding=embedding,
            top_k=20,
            document=self._context.active_document,
        )

        if (
            not results.get("ids")
            or not results.get("documents")
            or not results.get("metadatas")
        ):
            return []

        ids = results["ids"][0]
        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        chunks: list[Chunk] = []

        seen_contents: set[str] = set()

        used_indexes: dict[str, list[int]] = {}

        WINDOW = 2

        for chunk_id, content, metadata, distance in zip(
            ids,
            documents,
            metadatas,
            distances,
            strict=False,
        ):
            normalized = " ".join(content.split())

            if normalized in seen_contents:
                continue

            document = metadata["document"]
            chunk_index = metadata["chunk"]

            previous_indexes = used_indexes.setdefault(
                document,
                [],
            )

            too_close = any(
                abs(chunk_index - index) <= WINDOW for index in previous_indexes
            )

            if too_close:
                continue

            previous_indexes.append(chunk_index)

            seen_contents.add(normalized)

            chunks.append(
                Chunk(
                    id=chunk_id,
                    content=content,
                    source_document=document,
                    chunk_index=chunk_index,
                    total_chunks=metadata["total_chunks"],
                    metadata={
                        key: value
                        for key, value in metadata.items()
                        if key
                        not in {
                            "document",
                            "chunk",
                            "total_chunks",
                            "indexed_at",
                        }
                    }
                    | {
                        "distance": distance,
                    },
                )
            )

            if len(chunks) >= top_k:
                break

        return chunks

    def set_active_document(
        self,
        filename: str | None,
    ) -> None:
        """
        Sets the active document.

        None means search across all documents.
        """

        self._context.set_active_document(filename)

    def clear_active_document(
        self,
    ) -> None:
        """
        Clears the active document.
        """

        self._context.clear()
