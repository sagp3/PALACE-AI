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
You are PALACE AI.

You answer questions ONLY using the provided context.

If the answer cannot be found in the context,
respond exactly:

I don't know based on the available documents.

====================

CONTEXT

{context}

====================

QUESTION

{question}

====================

ANSWER
""".strip()
