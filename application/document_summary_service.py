"""
PALACE AI

Document Summary Service
"""

from __future__ import annotations

from application.knowledge_retriever import KnowledgeRetriever
from core.chat_response import ChatResponse
from core.chunk import Chunk
from infrastructure.llm.openai_llm import OpenAILLM


class DocumentSummaryService:
    """
    Generates summaries from indexed documents.
    """

    def __init__(self) -> None:
        self._retriever = KnowledgeRetriever()

        self._llm = OpenAILLM()

    def summarize(
        self,
        question: str,
    ) -> ChatResponse:
        """
        Generates a structured summary of the indexed documents.
        """

        chunks = self._retriever.retrieve(
            question=question,
            top_k=20,
        )

        if not chunks:
            return ChatResponse(
                answer="No indexed information was found.",
                sources=[],
            )

        prompt = self._build_summary_prompt(chunks)

        answer = self._llm.generate(prompt)

        return ChatResponse(
            answer=answer,
            sources=chunks,
        )

    def _build_summary_prompt(
        self,
        chunks: list[Chunk],
    ) -> str:
        """
        Builds the prompt used for document summarization.
        """

        context = "\n\n".join(chunk.content for chunk in chunks)

        return f"""
You are PALACE AI, an expert document analysis assistant.

Your task is to summarize the provided document fragments.

Instructions:

- Produce a clear and well-organized summary.
- Use Markdown headings.
- Group related ideas together.
- Preserve the original technical meaning.
- Do NOT invent information.
- Avoid repeating the same concepts.
- If the document contains examples, briefly mention them.
- Finish with a concise conclusion.

Document Fragments:

{context}

Structured Summary:
"""
