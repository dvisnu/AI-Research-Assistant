from pydantic import BaseModel


class UploadResponse(BaseModel):
    message: str
    original_filename: str
    stored_filename: str
    size: int
    ingestion_status: str | None = None
