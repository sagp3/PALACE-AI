"""
PALACE AI

Document Service
"""

from __future__ import annotations

from core.document import Document
from infrastructure.database.document_repository import DocumentRepository


class DocumentService:
    """
    Application service responsible for managing
    indexed documents.
    """

    def __init__(self) -> None:
        self._repository = DocumentRepository()

    def list_documents(
        self,
    ) -> list[Document]:
        """
        Returns all indexed documents.
        """

        return self._repository.list_documents()

    def exists(
        self,
        file_hash: str,
    ) -> bool:
        """
        Checks if a document already exists.
        """

        return self._repository.exists(file_hash)

    def save(
        self,
        document: Document,
    ) -> None:
        """
        Saves a document.
        """

        self._repository.save(document)

    def delete(
        self,
        file_hash: str,
    ) -> None:
        """
        Deletes a document.
        """

        self._repository.delete(file_hash)

    def count(
        self,
    ) -> int:
        """
        Returns the number of indexed documents.
        """

        return self._repository.count()

    def close(
        self,
    ) -> None:
        """
        Releases database resources.
        """

        self._repository.close()
