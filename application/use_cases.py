"""
PALACE AI - Application Layer

Application layer contains the use cases of PALACE AI.

A use case coordinates the business flow but does not
know implementation details.

It orchestrates the Domain and Infrastructure.
"""

from pathlib import Path

from core.domain import Area
from infrastructure.document_factory import DocumentFactory


class IngestKnowledge:
    """
    Use case responsible for incorporating a business
    document into PALACE AI.
    """

    def __init__(self, document_factory: DocumentFactory):
        self._document_factory = document_factory

    def execute(self, file_path: Path, area: Area) -> None:
        """
        Ingests a document into the knowledge base.

        Parameters
        ----------
        file_path:
            Path to the source document.

        area:
            Business area that owns the document.
        """

        document = self._document_factory.create(
            file_path=file_path,
            area=area,
        )

        #
        # Next steps (future implementation)
        #
        # 1. Extract knowledge
        # 2. Store knowledge
        # 3. Update index
        #

        raise NotImplementedError(
            "Knowledge ingestion is not implemented yet."
        )