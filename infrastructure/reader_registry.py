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
    Selects the appropriate FileReader
    according to the file extension.
    """

    def __init__(self) -> None:
        self._readers: dict[str, FileReader] = {
            ".pdf": PdfReader(),
            ".csv": CsvReader(),
        }

    def get_reader(
        self,
        file_path: Path,
    ) -> FileReader:
        """
        Returns the appropriate reader for a file.
        """

        extension = file_path.suffix.lower()

        try:
            return self._readers[extension]

        except KeyError as exception:
            supported = ", ".join(sorted(self._readers.keys()))

            raise ValueError(
                f"Unsupported file type '{extension}'. Supported types: {supported}"
            ) from exception

    def register(
        self,
        extension: str,
        reader: FileReader,
    ) -> None:
        """
        Registers a new reader.

        This allows new formats to be added
        without modifying the registry logic.
        """

        self._readers[extension.lower()] = reader

    @property
    def supported_extensions(
        self,
    ) -> tuple[str, ...]:
        """
        Returns all supported extensions.
        """

        return tuple(sorted(self._readers.keys()))
