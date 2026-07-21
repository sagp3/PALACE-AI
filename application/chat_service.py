"""
PALACE AI

Chat Service
"""

from __future__ import annotations

from application.document_summary_service import DocumentSummaryService
from application.intent_detector import Intent, IntentDetector
from application.knowledge_retriever import KnowledgeRetriever
from application.prompt_builder import PromptBuilder
from core.chat_response import ChatResponse
from infrastructure.llm.ollama_llm import OllamaLLM


class ChatService:
    """
    Main application service responsible for
    handling user requests.
    """

    def __init__(self) -> None:
        self._intent_detector = IntentDetector()

        self._retriever = KnowledgeRetriever()

        self._prompt_builder = PromptBuilder()

        self._llm = OllamaLLM()

        self._summary_service = DocumentSummaryService()

    def ask(
        self,
        question: str,
    ) -> ChatResponse:
        """
        Entry point for all user requests.
        """

        intent = self._intent_detector.detect(question)

        if intent == Intent.SUMMARY:
            return self._summarize_document(question)

        if intent == Intent.TOPICS:
            return self._extract_topics(question)

        if intent == Intent.KEYWORDS:
            return self._extract_keywords(question)

        return self._answer_question(question)

    def _answer_question(
        self,
        question: str,
    ) -> ChatResponse:
        """
        Answers a question using Retrieval-Augmented Generation.
        """

        chunks = self._retriever.retrieve(question)

        if not chunks:
            return ChatResponse(
                answer=(
                    "I couldn't find relevant information in the indexed documents."
                ),
                sources=[],
            )

        prompt = self._prompt_builder.build(
            question=question,
            chunks=chunks,
        )

        answer = self._llm.generate(prompt)

        return ChatResponse(
            answer=answer,
            sources=chunks,
        )

    def _summarize_document(
        self,
        question: str,
    ) -> ChatResponse:
        """
        Delegates document summarization to the
        specialized summary service.
        """

        return self._summary_service.summarize(question)

    def _extract_topics(
        self,
        question: str,
    ) -> ChatResponse:
        """
        Placeholder for topic extraction.
        """

        return ChatResponse(
            answer="Topic extraction is not implemented yet.",
            sources=[],
        )

    def _extract_keywords(
        self,
        question: str,
    ) -> ChatResponse:
        """
        Placeholder for keyword extraction.
        """

        return ChatResponse(
            answer="Keyword extraction is not implemented yet.",
            sources=[],
        )

    def set_active_document(
        self,
        filename: str | None,
    ) -> None:
        """
        Restricts retrieval to a single document.

        None means search across all indexed documents.
        """

        self._retriever.set_active_document(filename)

    def clear_active_document(
        self,
    ) -> None:
        """
        Clears the active document filter.
        """

        self._retriever.clear_active_document()
