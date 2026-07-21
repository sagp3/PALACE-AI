"""
PALACE AI

Document Upload Service

Handles uploaded documents from Streamlit.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from application.indexer import Indexer


@dataclass(slots=True, frozen=True)
class UploadResult:
    """
    Result of an upload operation.
    """

    success: bool

    filename: str

    message: str


class DocumentUploadService:
    """
    Saves uploaded documents and sends them
    to the indexing pipeline.
    """

    def __init__(
        self,
        documents_directory: Path = Path("data/documents"),
    ) -> None:
        self._documents_directory = documents_directory

        self._documents_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        self._indexer = Indexer()

    def upload(
        self,
        uploaded_file,
    ) -> UploadResult:
        """
        Saves and indexes an uploaded file.

        Parameters
        ----------
        uploaded_file
            Streamlit UploadedFile.

        Returns
        -------
        UploadResult
        """

        destination = self._documents_directory / uploaded_file.name

        try:
            with destination.open("wb") as output:
                output.write(uploaded_file.getbuffer())

            self._indexer.index(
                file_path=destination,
            )

            return UploadResult(
                success=True,
                filename=destination.name,
                message="Document indexed successfully.",
            )

        except Exception as exception:
            return UploadResult(
                success=False,
                filename=uploaded_file.name,
                message=str(exception),
            )
