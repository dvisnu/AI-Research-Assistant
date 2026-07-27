'''from app.core.config import UPLOAD_DIR

print(UPLOAD_DIR)

from app.services.validation import (
    validate_file_extension,
    validate_file_size,
)

validate_file_extension("notes.pdf")
validate_file_extension("resume.docx")
validate_file_extension("readme.md")

validate_file_size(1024)

print("All tests passed!")


from pathlib import Path
from app.services.loader_service import load_document
from app.services.chunking_service import split_documents
print(Path("uploads/c4b19a63-ec95-4768-9990-69455233a46f.pdf"))

docs = load_document(Path("app/uploads/c4b19a63-ec95-4768-9990-69455233a46f.pdf"))
chunks = split_documents(docs)

print(f"Pages loaded: {len(docs)}")
print(f"Chunks created: {len(chunks)}")

print(chunks[0].page_content[:300])
print(chunks[0].metadata)


from app.services.embedding_service import get_embedding_model

print("Before loading model...")

embeddings = get_embedding_model()

print("Model loaded!")

print("Generating embedding...")

vector = embeddings.embed_query("What is artificial intelligence?")

print("Done!")

print(len(vector))

from app.vectorstore.chroma import get_vectorstore

db = get_vectorstore()

print(db._collection.count())


from pathlib import Path

from app.services.ingestion_service import ingest_document

result = ingest_document(
    Path("app/uploads/c4b19a63-ec95-4768-9990-69455233a46f.pdf")
)

print(result)
'''

from pathlib import Path

from app.services.ingestion_service import ingest_document


file = Path(
    "app/uploads/03ccbdf2-a297-4138-94ff-b8c091450727.pdf"
)


result = ingest_document(file)

print(result)