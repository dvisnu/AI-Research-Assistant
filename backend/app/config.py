import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)

ALLOWED_EXTENSIONS = {".pdf", ".docx", ".txt", ".md"}

MAX_FILE_SIZE = 20 * 1024 * 1024

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

CHROMA_DB_DIR = BASE_DIR / "chroma_db"
CHROMA_COLLECTION_NAME = "documents"

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
