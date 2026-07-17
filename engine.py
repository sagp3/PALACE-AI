"""
PALACE AI

Public Engine
"""

from __future__ import annotations

from pathlib import Path

from core.domain import Area


class PalaceAI:
    """
    Public entry point of PALACE AI.
    """

    def ingest(
        self,
        file_path: Path,
        area: Area,
    ) -> None:
        """
        Ingest a document.

        Parameters
        ----------
        file_path:
            File to ingest.

        area:
            Business area.
        """

        raise NotImplementedError()

    def ask(
        self,
        question: str,
        area: Area | None = None,
    ) -> str:
        """
        Ask PALACE AI.

        Parameters
        ----------
        question:
            User question.

        area:
            Optional business area.
        """

        raise NotImplementedError()
