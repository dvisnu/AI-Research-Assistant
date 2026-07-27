from langchain_chroma import Chroma

from app.core.config import (
    CHROMA_COLLECTION_NAME,
    CHROMA_DB_DIR,
)
from app.services.embedding_service import get_embedding_model


_vectorstore = Chroma(
    collection_name=CHROMA_COLLECTION_NAME,
    embedding_function=get_embedding_model(),
    persist_directory=str(CHROMA_DB_DIR),
)


def get_vectorstore() -> Chroma:
    """
    Return the shared Chroma vector store instance.
    """
    return _vectorstore