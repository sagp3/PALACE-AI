"""
PALACE AI - Infrastructure

RawDocument represents information extracted from
a physical file before becoming a Domain Document.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class RawDocument:
    """
    Raw information extracted from a file.
    """

    filename: str
    content: str
    metadata: dict[str, Any] = field(default_factory=dict)