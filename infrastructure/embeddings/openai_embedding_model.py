"""
PALACE AI

OpenAI Embedding Model

Generates vector embeddings using the OpenAI API.
"""

from __future__ import annotations

import os

from dotenv import load_dotenv
from openai import OpenAI

from core.chunk import Chunk

from .embedding_model import EmbeddingModel

# Load environment variables from .env
load_dotenv()


class OpenAIEmbeddingModel(EmbeddingModel):
    """
    Embedding provider using the OpenAI API.
    """

    def __init__(self) -> None:
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise RuntimeError("OPENAI_API_KEY was not found in the environment.")

        self._client = OpenAI(api_key=api_key)

        # Default embedding model
        self._model = "text-embedding-3-small"

    def embed(
        self,
        chunks: list[Chunk],
    ) -> list[list[float]]:
        """
        Generates embeddings for a list of chunks.

        Parameters
        ----------
        chunks:
            List of knowledge chunks.

        Returns
        -------
        list[list[float]]
            One embedding vector for each chunk.
        """

        if not chunks:
            return []

        response = self._client.embeddings.create(
            model=self._model,
            input=[chunk.content for chunk in chunks],
        )

        return [item.embedding for item in response.data]

    def embed_query(
        self,
        query: str,
    ) -> list[float]:
        """
        Generates an embedding vector for a search query.

        Parameters
        ----------
        query:
            User question or search query.

        Returns
        -------
        list[float]
            Embedding vector representing the query.
        """

        response = self._client.embeddings.create(
            model=self._model,
            input=query,
        )

        return response.data[0].embedding
