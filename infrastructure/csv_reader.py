"""
PALACE AI

CSV Reader

Reads CSV files and converts them into
a RawDocument.
"""

from __future__ import annotations

import csv
from pathlib import Path

from .file_reader import FileReader
from .raw_document import RawDocument


class CsvReader(FileReader):
    """
    Reads CSV files.

    Each row is transformed into structured
    natural language to improve semantic search.
    """

    def read(
        self,
        file_path: Path,
    ) -> RawDocument:
        """
        Reads a CSV file.

        Parameters
        ----------
        file_path:
            Path to the CSV file.

        Returns
        -------
        RawDocument
        """

        if not file_path.exists():
            raise FileNotFoundError(f"CSV file not found: {file_path}")

        if file_path.stat().st_size == 0:
            raise ValueError(f"CSV file is empty: {file_path}")

        try:
            content: list[str] = []

            with file_path.open(
                mode="r",
                encoding="utf-8-sig",
                newline="",
            ) as csv_file:
                reader = csv.DictReader(csv_file)

                if reader.fieldnames is None:
                    raise ValueError("CSV file has no header.")

                for row_number, row in enumerate(
                    reader,
                    start=1,
                ):
                    content.append(f"Row {row_number}")

                    for column, value in row.items():
                        value = "" if value is None else str(value).strip()

                        content.append(f"{column}: {value}")

                    content.append("")

            return RawDocument(
                filename=file_path.name,
                content="\n".join(content),
                metadata={
                    "rows": row_number if "row_number" in locals() else 0,
                    "columns": len(reader.fieldnames),
                    "extension": ".csv",
                    "path": str(file_path),
                },
            )

        except Exception as exception:
            raise RuntimeError(
                f"Unable to read CSV '{file_path}': {exception}"
            ) from exception
