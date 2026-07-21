"""
PALACE AI

Document Repository
"""

from __future__ import annotations

import sqlite3
from datetime import datetime
from pathlib import Path

from core.document import Document


class DocumentRepository:
    """
    Repository responsible for managing indexed documents.
    """

    def __init__(
        self,
        database_path: str = "data/palace_ai.db",
    ) -> None:
        Path(database_path).parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        self._connection = sqlite3.connect(
            database_path,
            check_same_thread=False,
        )

        self._connection.row_factory = sqlite3.Row

        self._connection.execute("PRAGMA foreign_keys = ON")

        self._create_table()

    def _create_table(
        self,
    ) -> None:
        self._connection.execute(
            """
            CREATE TABLE IF NOT EXISTS documents (

                hash TEXT PRIMARY KEY,

                filename TEXT NOT NULL,

                indexed_at TEXT NOT NULL
            )
            """
        )

        self._connection.commit()

    def exists(
        self,
        file_hash: str,
    ) -> bool:
        cursor = self._connection.execute(
            """
            SELECT 1
            FROM documents
            WHERE hash = ?
            """,
            (file_hash,),
        )

        return cursor.fetchone() is not None

    def save(
        self,
        document: Document,
    ) -> None:
        self._connection.execute(
            """
            INSERT OR REPLACE
            INTO documents
            (
                hash,
                filename,
                indexed_at
            )
            VALUES
            (
                ?,
                ?,
                ?
            )
            """,
            (
                document.file_hash,
                document.filename,
                document.indexed_at.isoformat(),
            ),
        )

        self._connection.commit()

    def list_documents(
        self,
    ) -> list[Document]:
        cursor = self._connection.execute(
            """
            SELECT
                filename,
                hash,
                indexed_at
            FROM documents
            ORDER BY filename
            """
        )

        documents: list[Document] = []

        for row in cursor.fetchall():
            documents.append(
                Document(
                    filename=row["filename"],
                    file_hash=row["hash"],
                    indexed_at=datetime.fromisoformat(row["indexed_at"]),
                )
            )

        return documents

    def delete(
        self,
        file_hash: str,
    ) -> None:
        self._connection.execute(
            """
            DELETE
            FROM documents
            WHERE hash = ?
            """,
            (file_hash,),
        )

        self._connection.commit()

    def count(
        self,
    ) -> int:
        cursor = self._connection.execute(
            """
            SELECT COUNT(*)
            FROM documents
            """
        )

        return cursor.fetchone()[0]

    def close(
        self,
    ) -> None:
        if self._connection:
            self._connection.close()
