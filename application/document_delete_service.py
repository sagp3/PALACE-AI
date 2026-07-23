"""
PALACE AI

Document Delete Service
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from infrastructure.database.document_repository import DocumentRepository
from infrastructure.vectorstores.chroma_vector_store import ChromaVectorStore


@dataclass(slots=True, frozen=True)
class DeleteResult:
    """
    Result of a delete operation.
    """

    success: bool

    filename: str

    message: str


class DocumentDeleteService:
    """
    Deletes indexed documents from the application.
    """

    def __init__(
        self,
        documents_directory: Path = Path("data/documents"),
    ) -> None:
        self._documents_directory = documents_directory

        self._repository = DocumentRepository()

        self._vector_store = ChromaVectorStore()

    def delete(
        self,
        filename: str,
    ) -> DeleteResult:
        """
        Deletes a document from:

        - SQLite
        - ChromaDB
        - Local storage
        """

        try:
            documents = self._repository.list_documents()

            document = next(
                (doc for doc in documents if doc.filename == filename),
                None,
            )

            if document is None:
                return DeleteResult(
                    success=False,
                    filename=filename,
                    message="Document not found.",
                )

            # Remove vectors from ChromaDB
            self._vector_store.delete_document(
                filename,
            )

            # Remove record from SQLite
            self._repository.delete(
                document.file_hash,
            )

            # Remove physical file
            file_path = self._documents_directory / filename

            if file_path.exists():
                file_path.unlink()

            return DeleteResult(
                success=True,
                filename=filename,
                message="Document deleted successfully.",
            )

        except Exception as exception:
            return DeleteResult(
                success=False,
                filename=filename,
                message=str(exception),
            )
