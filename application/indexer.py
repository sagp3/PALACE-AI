"""
PALACE AI

Document Indexer
"""

from pathlib import Path

from core.document_hasher import DocumentHasher
from infrastructure.chunkers.recursive_chunker import RecursiveChunker
from infrastructure.database.document_repository import DocumentRepository
from infrastructure.embeddings.openai_embedding_model import (
    OpenAIEmbeddingModel,
)
from infrastructure.pdf_reader import PdfReader
from infrastructure.vectorstores.chroma_vector_store import (
    ChromaVectorStore,
)
from infrastructure.writers.chunk_writer import ChunkWriter


class Indexer:
    """
    Orchestrates the complete document indexing process.
    """

    def __init__(self) -> None:

        self.reader = PdfReader()
        self.hasher = DocumentHasher()
        self.repository = DocumentRepository()
        self.chunker = RecursiveChunker()
        self.writer = ChunkWriter()
        self.embedding_model = OpenAIEmbeddingModel()
        self.vector_store = ChromaVectorStore()

    def index(
        self,
        pdf_path: Path,
        chunks_output: Path,
    ) -> None:
        """
        Index a PDF document.
        """

        print("\nReading document...")

        document = self.reader.read(pdf_path)

        print("✓ Document loaded")

        document_hash = self.hasher.hash(document)

        print(f"✓ Hash: {document_hash[:16]}...")

        if self.repository.exists(document_hash):

            print("\n✓ Document already indexed.")

            return

        print("\nGenerating chunks...")

        chunks = self.chunker.split(document)

        print(f"✓ {len(chunks)} chunks generated")

        # ---------------------------------------------------------
        # DEBUG: Mostrar los primeros chunks
        # ---------------------------------------------------------

        print("\n========== FIRST 10 CHUNKS ==========\n")

        for chunk in chunks[:10]:

            print("-" * 60)

            print(f"Chunk {chunk.chunk_index}/{chunk.total_chunks}")

            print()

            print(chunk.content[:300])

            print()

        print("=" * 60)
        print()

        # ---------------------------------------------------------

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

        self.repository.save(
            document_hash=document_hash,
            filename=document.filename,
        )

        print("✓ Document registered")

        print("\nIndex completed successfully.")
