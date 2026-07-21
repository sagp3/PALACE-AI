"""
PALACE AI

OpenAI Client

Provides a single configured OpenAI client
for the entire application.
"""

from __future__ import annotations

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class OpenAIClient:
    """
    Singleton wrapper around the OpenAI client.
    """

    _instance: OpenAI | None = None

    @classmethod
    def get_client(cls) -> OpenAI:
        """
        Returns a shared OpenAI client.
        """

        if cls._instance is None:
            api_key = os.getenv("OPENAI_API_KEY")

            if not api_key:
                raise RuntimeError("OPENAI_API_KEY was not found in the environment.")

            cls._instance = OpenAI(
                api_key=api_key,
            )

        return cls._instance
