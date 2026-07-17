"""
PALACE AI

Reader Registry

Responsible for selecting the correct reader
for a given file extension.
"""

from __future__ import annotations

from pathlib import Path

from .csv_reader import CsvReader
from .file_reader import FileReader
from .pdf_reader import PdfReader


class ReaderRegistry:
    """
    Selects the appropriate FileReader.
    """

    def __init__(self) -> None:

        self._readers: dict[str, FileReader] = {
            ".pdf": PdfReader(),
            ".csv": CsvReader(),
        }

    def get_reader(self, file_path: Path) -> FileReader:

        extension = file_path.suffix.lower()

        if extension not in self._readers:
            raise ValueError(f"Unsupported file type: {extension}")

        return self._readers[extension]
