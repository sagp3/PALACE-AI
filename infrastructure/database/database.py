"""
PALACE AI

SQLite Database
"""

from __future__ import annotations

import sqlite3
from pathlib import Path


class Database:
    """
    SQLite connection manager.
    """

    def __init__(self) -> None:

        database_path = Path("data/palace_ai.db")

        database_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        self._connection = sqlite3.connect(database_path)

        self._create_tables()

    @property
    def connection(self):
        return self._connection

    def _create_tables(self) -> None:

        cursor = self._connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS documents (

                hash TEXT PRIMARY KEY,

                filename TEXT NOT NULL,

                indexed_at TEXT NOT NULL
            )
            """)

        self._connection.commit()
