"""
PALACE AI

CSV Reader
"""

from __future__ import annotations

from pathlib import Path

from ..raw_document import RawDocument
from .file_reader import FileReader


class CsvReader(FileReader):
    """
    Reads CSV files.
    """

    def read(self, file_path: Path) -> RawDocument:

        raise NotImplementedError("CSV Reader has not been implemented yet.")
