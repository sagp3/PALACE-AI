"""
PALACE AI - Infrastructure

Document Factory

Responsible for converting RawDocument objects
into Domain Document entities.
"""

from __future__ import annotations

import uuid

from core.domain import Area, Document, DocumentType

from .raw_document import RawDocument


class DocumentFactory:
    """
    Builds Domain Documents.
    """

    def create(
        self,
        raw_document: RawDocument,
        area: Area,
        document_type: DocumentType,
    ) -> Document:
        return Document(
            id=str(uuid.uuid4()),
            name=raw_document.filename,
            area=area,
            document_type=document_type,
        )
