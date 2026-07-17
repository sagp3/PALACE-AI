"""
PALACE AI

Domain - Chunk
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4


@dataclass(slots=True)
class Chunk:
    """
    Smallest searchable unit of knowledge.
    """

    id: str = field(default_factory=lambda: str(uuid4()))

    content: str = ""

    source_document: str = ""

    chunk_index: int = 0

    total_chunks: int = 0

    metadata: dict[str, Any] = field(default_factory=dict)
