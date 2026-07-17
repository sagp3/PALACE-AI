"""
PALACE AI

Document Hasher

Calculates a deterministic SHA-256 hash for a document.
"""

from __future__ import annotations

import hashlib

from infrastructure.raw_document import RawDocument


class DocumentHasher:
    """
    Generates a SHA-256 hash from a document.

    The hash is based only on the document content.
    If the content changes, the hash changes.
    """

    def hash(
        self,
        document: RawDocument,
    ) -> str:
        """
        Calculates the SHA-256 hash of a document.

        Parameters
        ----------
        document:
            Raw document.

        Returns
        -------
        str
            SHA-256 hexadecimal hash.
        """

        return hashlib.sha256(document.content.encode("utf-8")).hexdigest()
