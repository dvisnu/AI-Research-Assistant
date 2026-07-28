from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from app.config import CHUNK_SIZE, CHUNK_OVERLAP


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


def split_documents(documents: list[Document], metadata: dict) -> list[Document]:
    chunks = text_splitter.split_documents(documents)

    for index, chunk in enumerate(chunks):
        chunk.metadata.update({
            **metadata,
            "chunk_id": index,
        })

    return chunks
