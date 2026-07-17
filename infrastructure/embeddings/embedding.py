"""
PALACE AI

Embedding
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from core.chunk import Chunk


@dataclass(slots=True)
class Embedding:
    """
    Represents one indexed knowledge unit.
    """

    id: str

    chunk: Chunk

    vector: list[float]

    metadata: dict[str, Any]
