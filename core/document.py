"""
PALACE AI

Document Entity
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass(slots=True)
class Document:
    """
    Represents an indexed document.
    """

    id: str = field(default_factory=lambda: str(uuid4()))

    filename: str = ""

    file_hash: str = ""

    indexed_at: datetime | None = None

    total_chunks: int = 0

    metadata: dict = field(default_factory=dict)
