from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from app.core.config import CHUNK_SIZE, CHUNK_OVERLAP


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
    separators=[
        "\n\n",
        "\n",
        ". ",
        " ",
        "",
    ],
)


def split_documents(documents: list[Document]) -> list[Document]:
    """
    Split documents into smaller chunks while preserving metadata.
    """

    return text_splitter.split_documents(documents)