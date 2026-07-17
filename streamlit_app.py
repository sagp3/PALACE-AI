"""
PALACE AI

Streamlit Interface
"""

from __future__ import annotations

import streamlit as st

from application.chat_service import ChatService


@st.cache_resource
def get_chat_service() -> ChatService:
    """
    Creates a single ChatService instance.
    """
    return ChatService()


def initialize_session() -> None:

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "chat_service" not in st.session_state:
        st.session_state.chat_service = get_chat_service()


def render_sidebar() -> None:

    with st.sidebar:

        st.title("🤖 PALACE AI")

        st.markdown("---")

        st.subheader("Knowledge Base")

        st.success("✔ manual.pdf")

        st.markdown("---")

        st.subheader("Statistics")

        st.write(f"Messages: {len(st.session_state.messages)//2}")

        st.markdown("---")

        if st.button(
            "🗑 Clear Conversation",
            use_container_width=True,
        ):

            st.session_state.messages = []

            st.rerun()


def render_history() -> None:

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

            if (
                message["role"] == "assistant"
                and "sources" in message
                and message["sources"]
            ):

                with st.expander("Sources"):

                    for chunk in message["sources"]:

                        st.markdown(
                            f"**{chunk.source_document}** "
                            f"(Chunk {chunk.chunk_index}/{chunk.total_chunks})"
                        )

                        st.code(
                            chunk.content,
                            language="text",
                        )


def process_question(question: str) -> None:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = st.session_state.chat_service.ask(question)

        st.markdown(response.answer)

        with st.expander("Sources"):

            for chunk in response.sources:

                st.markdown(
                    f"**{chunk.source_document}** "
                    f"(Chunk {chunk.chunk_index}/{chunk.total_chunks})"
                )

                st.code(
                    chunk.content,
                    language="text",
                )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response.answer,
            "sources": response.sources,
        }
    )


def main() -> None:

    st.set_page_config(
        page_title="PALACE AI",
        page_icon="🤖",
        layout="wide",
    )

    initialize_session()

    render_sidebar()

    st.title("🤖 PALACE AI")

    st.caption("Intelligent Document Assistant")

    render_history()

    question = st.chat_input("Ask a question...")

    if question:

        process_question(question)


if __name__ == "__main__":
    main()
