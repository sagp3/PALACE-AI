"""
PALACE AI - Infrastructure

File Reader Contract

Every file reader must implement this interface.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from pathlib import Path

from .raw_document import RawDocument


class FileReader(ABC):
    """
    Base contract for every supported reader.
    """

    @abstractmethod
    def read(self, file_path: Path) -> RawDocument:
        """
        Reads a physical file and returns its content.

        Parameters
        ----------
        file_path:
            Physical file path.

        Returns
        -------
        RawDocument
        """

        raise NotImplementedError