from pathlib import Path

#Upload configuration
BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)

ALLOWED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".txt",
    ".md",
}

MAX_FILE_SIZE = 20 * 1024 * 1024

# Chunking configuration
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Chroma configuration
CHROMA_DB_DIR = BASE_DIR / "chroma_db"
CHROMA_COLLECTION_NAME = "documents"