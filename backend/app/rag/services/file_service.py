import uuid
from pathlib import Path

from fastapi import UploadFile

from app.config import UPLOAD_DIR


async def save_upload_file(file: UploadFile, contents: bytes) -> dict:
    extension = Path(file.filename).suffix.lower()
    stored_filename = f"{uuid.uuid4()}{extension}"
    file_path = UPLOAD_DIR / stored_filename

    with open(file_path, "wb") as f:
        f.write(contents)

    return {
        "original_filename": file.filename,
        "stored_filename": stored_filename,
        "size": len(contents),
    }
