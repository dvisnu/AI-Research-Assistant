from sqlalchemy.orm import Session

from app.database.models import Document


def document_exists(
    db: Session,
    file_hash: str
) -> bool:
    """
    Check whether a document with this hash
    is already indexed.
    """

    document = (
        db.query(Document)
        .filter(
            Document.file_hash == file_hash
        )
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
    """
    Save document metadata after successful ingestion.
    """

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