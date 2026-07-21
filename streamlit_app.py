"""
PALACE AI

Streamlit Interface
"""

from __future__ import annotations

import streamlit as st

from application.chat_service import ChatService
from application.document_upload_service import DocumentUploadService
from infrastructure.database.document_repository import DocumentRepository


@st.cache_resource
def get_chat_service() -> ChatService:
    """
    Creates a single ChatService instance.
    """

    return ChatService()


@st.cache_resource
def get_upload_service() -> DocumentUploadService:
    """
    Creates a single upload service instance.
    """

    return DocumentUploadService()


def initialize_session() -> None:
    """
    Initializes Streamlit session state.
    """

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "chat_service" not in st.session_state:
        st.session_state.chat_service = get_chat_service()

    if "selected_document" not in st.session_state:
        st.session_state.selected_document = "All Documents"


def refresh_chat_service() -> None:
    """
    Recreates the ChatService after indexing
    new documents.
    """

    st.cache_resource.clear()

    st.session_state.chat_service = get_chat_service()


def render_sidebar() -> None:
    """
    Renders the application sidebar.
    """

    repository = DocumentRepository()

    documents = repository.list_documents()

    upload_service = get_upload_service()

    with st.sidebar:
        st.title("🤖 PALACE AI")

        st.markdown("---")

        st.subheader("📄 Upload Document")

        uploaded_file = st.file_uploader(
            "Choose a PDF or CSV",
            type=[
                "pdf",
                "csv",
            ],
        )

        if uploaded_file is not None:
            if st.button(
                "📥 Index Document",
                use_container_width=True,
            ):
                with st.spinner("Indexing document..."):
                    result = upload_service.upload(
                        uploaded_file,
                    )

                if result.success:
                    st.success(result.message)

                    refresh_chat_service()

                    st.rerun()

                else:
                    st.error(result.message)

        st.markdown("---")

        st.subheader("📚 Indexed Documents")

        options = [
            "All Documents",
        ]

        options.extend(document.filename for document in documents)

        selected = st.selectbox(
            "Search in",
            options,
            index=(
                options.index(st.session_state.selected_document)
                if st.session_state.selected_document in options
                else 0
            ),
        )

        if selected != st.session_state.selected_document:
            st.session_state.selected_document = selected

            if selected == "All Documents":
                st.session_state.chat_service.clear_active_document()

            else:
                st.session_state.chat_service.set_active_document(selected)

        if documents:
            for document in documents:
                st.success(f"✔ {document.filename}")

        else:
            st.info("No indexed documents.")

        st.markdown("---")

        st.subheader("📊 Statistics")

        st.metric(
            "Documents",
            repository.count(),
        )

        st.metric(
            "Messages",
            len(st.session_state.messages) // 2,
        )

        st.markdown("---")

        if st.button(
            "🗑 Clear Conversation",
            use_container_width=True,
        ):
            st.session_state.messages = []

            st.rerun()


def render_history() -> None:
    """
    Renders previous messages.
    """

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


def process_question(
    question: str,
) -> None:
    """
    Processes a user question.
    """

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

        if response.sources:
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
    """
    Application entry point.
    """

    st.set_page_config(
        page_title="PALACE AI",
        page_icon="🤖",
        layout="wide",
    )

    initialize_session()

    render_sidebar()

    st.title("🤖 PALACE AI")

    st.caption("Intelligent Document Assistant")

    if st.session_state.selected_document == "All Documents":
        st.info("Searching across all indexed documents.")

    else:
        st.info(f"Searching only in: **{st.session_state.selected_document}**")

    render_history()

    question = st.chat_input("Ask a question about your documents...")

    if question:
        process_question(question)


if __name__ == "__main__":
    main()
