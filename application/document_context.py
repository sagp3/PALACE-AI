"""
PALACE AI

Document Context
"""

from __future__ import annotations


class DocumentContext:
    """
    Stores the active document for the current session.

    If active_document is None, searches are performed
    across every indexed document.
    """

    def __init__(self) -> None:
        self._active_document: str | None = None

    @property
    def active_document(self) -> str | None:
        return self._active_document

    def set_active_document(
        self,
        filename: str | None,
    ) -> None:
        """
        Sets the current active document.

        None means "search every document".
        """

        self._active_document = filename

    def clear(self) -> None:
        """
        Clears the current selection.
        """

        self._active_document = None

    def has_active_document(self) -> bool:
        return self._active_document is not None
