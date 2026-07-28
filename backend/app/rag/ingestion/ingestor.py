from pathlib import Path

from app.rag.services.database import SessionLocal
from app.rag.services.hash_service import calculate_file_hash
from app.rag.services.document_service import (
    document_exists,
    register_document,
)
from app.rag.ingestion.loader import load_document
from app.rag.ingestion.chunker import split_documents
from app.rag.retrieval.vectorstore import get_vectorstore


def ingest_document(file_path: Path) -> dict:
    db = SessionLocal()

    try:
        file_hash = calculate_file_hash(file_path)

        if document_exists(db, file_hash):
            return {
                "message": "Document already indexed",
                "filename": file_path.name
            }

        documents = load_document(file_path)

        chunks = split_documents(
            documents,
            metadata={
                "filename": file_path.name,
                "document_hash": file_hash,
            }
        )

        vectorstore = get_vectorstore()

        chunk_ids = [
            f"{file_hash}_{chunk.metadata['chunk_id']}"
            for chunk in chunks
        ]

        ids = vectorstore.add_documents(
            documents=chunks,
            ids=chunk_ids
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
