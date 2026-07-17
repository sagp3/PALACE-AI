"""
PALACE AI - Infrastructure

PDF Reader

Reads PDF files and converts them into RawDocument objects.
"""

from __future__ import annotations

from pathlib import Path

import fitz

from .file_reader import FileReader
from .raw_document import RawDocument


class PdfReader(FileReader):
    """
    Reads PDF files using PyMuPDF.
    """

    def read(self, file_path: Path) -> RawDocument:
        """
        Reads a PDF file and extracts all text.

        Parameters
        ----------
        file_path:
            Path to the PDF file.

        Returns
        -------
        RawDocument

        Raises
        ------
        FileNotFoundError
            If the PDF file does not exist.

        ValueError
            If the PDF file is empty.

        RuntimeError
            If the PDF cannot be read.
        """

        # --------------------------------------------------
        # Validate file existence
        # --------------------------------------------------

        if not file_path.exists():
            raise FileNotFoundError(f"PDF file not found: {file_path}")

        # --------------------------------------------------
        # Validate empty file
        # --------------------------------------------------

        if file_path.stat().st_size == 0:
            raise ValueError(f"PDF file is empty: {file_path}")

        # --------------------------------------------------
        # Read PDF
        # --------------------------------------------------

        try:

            pdf = fitz.open(file_path)

            pages = []

            for page in pdf:

                text = page.get_text()

                if text.strip():
                    pages.append(text)

            pdf.close()

            content = "\n".join(pages)

            return RawDocument(
                filename=file_path.name,
                content=content,
                metadata={
                    "pages": len(pages),
                    "path": str(file_path),
                    "extension": ".pdf",
                },
            )

        except Exception as exception:

            raise RuntimeError(
                f"Unable to read PDF '{file_path}': {exception}"
            ) from exception
