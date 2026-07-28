from sqlalchemy.orm import Session

from app.rag.models.document import Document


def document_exists(db: Session, file_hash: str) -> bool:
    document = (
        db.query(Document)
        .filter(Document.file_hash == file_hash)
        .first()
    )
    return document is not None


def register_document(
    db: Session,
    original_filename: str,
    stored_filename: str,
    file_hash: str,
    chunks_created: int
):
    document = Document(
        original_filename=original_filename,
        stored_filename=stored_filename,
        file_hash=file_hash,
        chunks_created=chunks_created
    )
    db.add(document)
    db.commit()
    db.refresh(document)
    return document
