"""
PALACE AI

Intent Detector
"""

from __future__ import annotations

from enum import Enum


class Intent(str, Enum):
    QUESTION = "question"

    SUMMARY = "summary"

    TOPICS = "topics"

    KEYWORDS = "keywords"


class IntentDetector:
    """
    Detects the user's intention.
    """

    def detect(
        self,
        question: str,
    ) -> Intent:
        text = question.lower().strip()

        summary_words = (
            "resume",
            "resumen",
            "summarize",
            "summary",
        )

        topics_words = (
            "temas",
            "tema",
            "topics",
            "contenido",
            "trata",
            "habla",
        )

        keyword_words = (
            "palabras clave",
            "keywords",
            "conceptos",
            "conceptos clave",
        )

        if any(word in text for word in summary_words):
            return Intent.SUMMARY

        if any(word in text for word in topics_words):
            return Intent.TOPICS

        if any(word in text for word in keyword_words):
            return Intent.KEYWORDS

        return Intent.QUESTION
