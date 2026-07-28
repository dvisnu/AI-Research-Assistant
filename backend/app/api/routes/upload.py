from fastapi import APIRouter, File, UploadFile

from app.config import UPLOAD_DIR
from app.rag.models.upload import UploadResponse
from app.rag.services.file_service import save_upload_file
from app.rag.services.validation import (
    validate_file_extension,
    validate_file_size,
)
from app.rag.ingestion.ingestor import ingest_document

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)


@router.post("/", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)):
    contents = await file.read()

    validate_file_extension(file.filename)
    validate_file_size(len(contents))

    file_info = await save_upload_file(file, contents)

    stored_path = UPLOAD_DIR / file_info["stored_filename"]
    ingest_result = ingest_document(stored_path)

    return UploadResponse(
        message="File uploaded successfully.",
        ingestion_status=ingest_result["message"],
        **file_info,
    )
