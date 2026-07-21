"""
PALACE AI

Application Entry Point
"""

from pathlib import Path

from application.indexer import Indexer


def index_documents() -> None:
    """
    Index any supported document.
    """

    print("\nDocument indexing")
    print("-" * 80)

    file_input = input("Document path: ").strip()

    if not file_input:
        print("\nNo document selected.")
        return

    file_path = Path(file_input)

    if not file_path.exists():
        print("\nDocument not found.")
        return

    indexer = Indexer()

    try:
        indexer.index(
            file_path=file_path,
        )

        print("\nDocument indexed successfully.")

    except Exception as error:
        print(f"\nError while indexing:\n{error}")


def chat_mode() -> None:
    """
    Starts the chat mode.
    """

    from application.chat_service import ChatService

    chat = ChatService()

    print("\nPALACE AI Chat")
    print("Type 'exit' to quit.\n")

    while True:
        question = input("> ").strip()

        if not question:
            continue

        if question.lower() == "exit":
            break

        try:
            response = chat.ask(question)

            print("\nAnswer\n")

            print(response.answer)

            if response.sources:
                print("\nSources\n")

                for chunk in response.sources:
                    print(
                        f"- {chunk.source_document} "
                        f"(Chunk {chunk.chunk_index}/{chunk.total_chunks})"
                    )

            print()

        except Exception as error:
            print(f"\nError: {error}\n")


def main() -> None:
    print("=" * 80)
    print("PALACE AI")
    print("=" * 80)

    print("\n1. Index documents")
    print("2. Chat")

    option = input("\nSelect an option: ").strip()

    if option == "1":
        index_documents()

    elif option == "2":
        chat_mode()

    else:
        print("\nInvalid option.")


if __name__ == "__main__":
    main()
