from pathlib import Path

from app.database.sqlite import SessionLocal

from app.services.hash_service import calculate_file_hash
from app.services.document_service import (
    document_exists,
    register_document,
)

from app.services.loader_service import load_document
from app.services.chunking_service import split_documents
from app.vectorstore.chroma import get_vectorstore


def ingest_document(file_path: Path) -> dict:
    """
    Complete document ingestion pipeline.

    Steps:
    1. Calculate file hash
    2. Check duplicate
    3. Load document
    4. Split into chunks
    5. Store vectors
    6. Register document
    """

    db = SessionLocal()

    try:


        file_hash = calculate_file_hash(
            file_path
        )



        if document_exists(
            db,
            file_hash
        ):
            return {
                "message": "Document already indexed",
                "filename": file_path.name
            }


        documents = load_document(
            file_path
        )


        chunks = split_documents(
            documents
        )


        vectorstore = get_vectorstore()

        ids = vectorstore.add_documents(
            chunks
        )


        register_document(
            db=db,
            original_filename=file_path.name,
            stored_filename=file_path.name,
            file_hash=file_hash,
            chunks_created=len(ids)
        )


        return {
            "message": "Document indexed successfully",
            "filename": file_path.name,
            "chunks_created": len(ids)
        }


    finally:
        db.close()