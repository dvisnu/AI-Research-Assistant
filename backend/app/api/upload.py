from fastapi import APIRouter, File, UploadFile

from app.schemas.upload import UploadResponse
from app.services.file_service import save_upload_file
from app.services.validation import (
    validate_file_extension,
    validate_file_size,
)

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)


@router.post("/", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)):
    """
    Upload a document to the server.
    """

    contents = await file.read()

    validate_file_extension(file.filename)
    validate_file_size(len(contents))

    file_info = await save_upload_file(file, contents)

    return UploadResponse(
        message="File uploaded successfully.",
        **file_info,
    )