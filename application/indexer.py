"""
PALACE AI

Document Indexer
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from core.document import Document
from core.document_hasher import DocumentHasher
from infrastructure.chunkers.recursive_chunker import RecursiveChunker
from infrastructure.database.document_repository import DocumentRepository
from infrastructure.embeddings.openai_embedding_model import OpenAIEmbeddingModel
from infrastructure.reader_registry import ReaderRegistry
from infrastructure.vectorstores.chroma_vector_store import ChromaVectorStore
from infrastructure.writers.chunk_writer import ChunkWriter


class Indexer:
    """
    Orchestrates the complete document indexing process.
    """

    def __init__(self) -> None:
        self.reader_registry = ReaderRegistry()

        self.hasher = DocumentHasher()

        self.repository = DocumentRepository()

        self.chunker = RecursiveChunker()

        self.writer = ChunkWriter()

        self.embedding_model = OpenAIEmbeddingModel()

        self.vector_store = ChromaVectorStore()

    def index(
        self,
        file_path: Path,
    ) -> None:
        """
        Indexes any supported document.
        """

        print("\nReading document...")

        reader = self.reader_registry.get_reader(file_path)

        document = reader.read(file_path)

        print(f"✓ {document.filename} loaded")

        document_hash = self.hasher.hash(document)

        print(f"✓ Hash: {document_hash[:16]}...")

        if self.repository.exists(document_hash):
            print("\n✓ Document already indexed.")

            return

        chunks_output = Path("data/chunks") / document_hash[:16]

        chunks_output.mkdir(
            parents=True,
            exist_ok=True,
        )

        print("\nGenerating chunks...")

        chunks = self.chunker.split(document)

        print(f"✓ {len(chunks)} chunks generated")

        print("\n========== FIRST 10 CHUNKS ==========\n")

        for chunk in chunks[:10]:
            print("-" * 60)

            print(f"Chunk {chunk.chunk_index}/{chunk.total_chunks}")

            print()

            print(chunk.content[:300])

            print()

        print("=" * 60)

        print()

        print("Saving chunks...")

        self.writer.write(
            chunks=chunks,
            output_directory=chunks_output,
        )

        print("✓ Chunks saved")

        print("\nGenerating embeddings...")

        embeddings = self.embedding_model.embed(chunks)

        print(f"✓ {len(embeddings)} embeddings generated")

        print("\nIndexing vectors...")

        self.vector_store.add(
            chunks=chunks,
            embeddings=embeddings,
        )

        print("✓ ChromaDB updated")

        indexed_document = Document(
            filename=document.filename,
            file_hash=document_hash,
            indexed_at=datetime.now(),
            total_chunks=len(chunks),
            metadata=document.metadata,
        )

        self.repository.save(indexed_document)

        print("✓ Document registered")

        print("\nIndex completed successfully.")
