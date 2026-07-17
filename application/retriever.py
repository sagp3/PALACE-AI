"""
PALACE AI

Retriever Use Case
"""

from __future__ import annotations

from core.chunk import Chunk
from core.retriever import Retriever
from infrastructure.embeddings.openai_embedding_model import (
    OpenAIEmbeddingModel,
)
from infrastructure.vectorstores.chroma_vector_store import (
    ChromaVectorStore,
)


class SemanticRetriever(Retriever):
    """
    Retrieves the most relevant chunks from the vector database.
    """

    def __init__(self) -> None:

        self.embedding_model = OpenAIEmbeddingModel()

        self.vector_store = ChromaVectorStore()

    def search(
        self,
        query: str,
        top_k: int = 5,
    ) -> list[Chunk]:

        embedding = self.embedding_model.embed_query(query)

        return self.vector_store.search(
            embedding=embedding,
            top_k=top_k,
        )
