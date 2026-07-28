from pathlib import Path
from fastapi import HTTPException

from app.config import ALLOWED_EXTENSIONS, MAX_FILE_SIZE


def validate_file_extension(filename: str) -> str:
    extension = Path(filename).suffix.lower()
    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type. Allowed types: {', '.join(sorted(ALLOWED_EXTENSIONS))}"
        )
    return extension


def validate_file_size(file_size: int) -> None:
    if file_size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail=f"File exceeds maximum size of {MAX_FILE_SIZE // (1024 * 1024)} MB."
        )
