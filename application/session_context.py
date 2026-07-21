"""
PALACE AI

Session Context
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class SessionContext:
    """
    Stores the state of the current user session.
    """

    active_document: str | None = None

    selected_model: str = "qwen3:8b"

    temperature: float = 0.0

    def clear_document(self) -> None:
        """
        Clears the active document.
        """

        self.active_document = None

    @property
    def has_active_document(self) -> bool:
        """
        Returns True if a document has been selected.
        """

        return self.active_document is not None
