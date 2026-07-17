"""
PALACE AI

Chunk Writer
"""

from __future__ import annotations

import json
from pathlib import Path

from core.chunk import Chunk


class ChunkWriter:
    """
    Persists chunks as JSON files.
    """

    def write(
        self,
        chunks: list[Chunk],
        output_directory: Path,
    ) -> None:

        output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        for chunk in chunks:

            output_file = output_directory / f"{chunk.id}.json"

            with output_file.open(
                "w",
                encoding="utf-8",
            ) as file:

                json.dump(
                    {
                        "id": chunk.id,
                        "chunk": chunk.chunk_index,
                        "total_chunks": chunk.total_chunks,
                        "document": chunk.source_document,
                        "content": chunk.content,
                        "metadata": chunk.metadata,
                    },
                    file,
                    ensure_ascii=False,
                    indent=4,
                )
