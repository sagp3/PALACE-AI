"""
PALACE AI

Prompt Builder
"""

from __future__ import annotations

from core.chunk import Chunk


class PromptBuilder:
    """
    Builds prompts for the LLM.
    """

    def __init__(
        self,
        max_context_chars: int = 12000,
    ) -> None:
        self._max_context_chars = max_context_chars

    def build(
        self,
        question: str,
        chunks: list[Chunk],
    ) -> str:
        context = "\n\n".join(
            f"""
Document:
{chunk.source_document}

Chunk:
{chunk.chunk_index}/{chunk.total_chunks}

Content:
{chunk.content}
""".strip()
            for chunk in chunks
        )

        context = context[: self._max_context_chars]

        return f"""
You are PALACE AI, an enterprise document assistant.

Your task is to answer questions using ONLY the information
contained in the provided context.

Rules:

- ALWAYS answer in the same language as the user's question.
- If the user asks in Spanish, answer in Spanish.
- If the user asks in English, answer in English.
- Do NOT use external knowledge.
- Do NOT invent or assume information.
- If the answer is not completely supported by the context,
  reply in the same language as the user's question indicating
  that the information is not available in the provided
  documents.
- Be concise, professional and clear.

====================

CONTEXT

{context}

====================

QUESTION

{question}

====================

ANSWER
""".strip()
