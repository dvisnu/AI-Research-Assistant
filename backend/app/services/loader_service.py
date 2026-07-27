from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    TextLoader,
)


def load_document(file_path: Path):
    """
    Load a document based on its extension.

    Returns:
        List[Document]
    """

    extension = file_path.suffix.lower()

    if extension == ".pdf":
        loader = PyPDFLoader(str(file_path))

    elif extension == ".docx":
        loader = Docx2txtLoader(str(file_path))

    elif extension in {".txt", ".md"}:
        loader = TextLoader(
            str(file_path),
            encoding="utf-8"
        )

    else:
        raise ValueError(
            f"Unsupported file type: {extension}"
        )

    return loader.load()