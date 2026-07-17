"""
PALACE AI

Document Repository
"""

from __future__ import annotations

from datetime import datetime

from .database import Database


class DocumentRepository:
    """
    Handles persistence of indexed documents.
    """

    def __init__(self) -> None:
        self._database = Database()

    def exists(
        self,
        document_hash: str,
    ) -> bool:
        """
        Returns True if a document hash already exists.
        """

        cursor = self._database.connection.cursor()

        cursor.execute(
            """
            SELECT 1
            FROM documents
            WHERE hash = ?
            LIMIT 1
            """,
            (document_hash,),
        )

        return cursor.fetchone() is not None

    def save(
        self,
        document_hash: str,
        filename: str,
    ) -> None:
        """
        Stores an indexed document.
        """

        cursor = self._database.connection.cursor()

        cursor.execute(
            """
            INSERT INTO documents (
                hash,
                filename,
                indexed_at
            )
            VALUES (?, ?, ?)
            """,
            (
                document_hash,
                filename,
                datetime.utcnow().isoformat(),
            ),
        )

        self._database.connection.commit()

    def delete(
        self,
        document_hash: str,
    ) -> None:
        """
        Removes a document from the registry.
        """

        cursor = self._database.connection.cursor()

        cursor.execute(
            """
            DELETE
            FROM documents
            WHERE hash = ?
            """,
            (document_hash,),
        )

        self._database.connection.commit()

    def list_documents(
        self,
    ) -> list[dict]:
        """
        Returns all indexed documents.
        """

        cursor = self._database.connection.cursor()

        cursor.execute("""
            SELECT
                hash,
                filename,
                indexed_at
            FROM documents
            ORDER BY indexed_at DESC
            """)

        rows = cursor.fetchall()

        return [
            {
                "hash": row[0],
                "filename": row[1],
                "indexed_at": row[2],
            }
            for row in rows
        ]
