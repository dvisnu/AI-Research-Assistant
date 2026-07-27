# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added

#### RAG Pipeline
- Google Gemini LLM integration via `llm_service.py` — ChatGoogleGenerativeAI with `gemini-2.5-flash-lite` model
- RAG prompt template (`rag_prompts.py`) — structured prompt with Answer/Evidence/Sources/Confidence sections
- RAG query service (`rag_service.py`) — `ask_question()` orchestrates retriever → prompt → LLM → citations
- Retrieval service (`retriever_service.py`) — MMR-based retriever (k=5, fetch_k=50, lambda_mult=0.7) with similarity search with scores

#### Enhanced Ingestion
- Chunking service now accepts custom metadata (`filename`, `document_hash`, `chunk_id`) for richer chunk metadata
- Ingestion pipeline uses deterministic chunk IDs (`{file_hash}_{chunk_id}`) for idempotent indexing

#### Dependencies
- `langchain-google-genai>=4.3.2` added for Google Gemini API support

#### Backend Infrastructure
- FastAPI application scaffold with `main.py` entry point and root health-check endpoint
- Project configuration via `app/core/config.py` — upload dir, allowed extensions, file size limits, chunking params, ChromaDB path
- SQLite database setup via SQLAlchemy (`app/database/`) with `Document` model for tracking indexed documents
- Database initialization script (`init_db.py`) with auto table creation

#### File Upload API
- `POST /upload/` endpoint accepting PDF, DOCX, TXT, and MD files
- File type validation (whitelist-based extension checking)
- File size validation (20 MB max limit)
- Secure file saving service with unique stored filenames
- Pydantic response schema for upload responses

#### Document Ingestion Pipeline
- **Loader Service** — Multi-format document loading via LangChain: PyPDFLoader (PDF), Docx2txtLoader (DOCX), TextLoader (TXT/MD)
- **Chunking Service** — RecursiveCharacterTextSplitter (1000 token chunks, 200 token overlap) with metadata preservation
- **Embedding Service** — HuggingFace `sentence-transformers/all-MiniLM-L6-v2` model on CPU with normalized embeddings
- **Hash Service** — SHA-256 file hashing for duplicate detection
- **Document Service** — Duplicate checking and document metadata registration in SQLite
- **Ingestion Service** — Orchestrates the full pipeline: hash → check → load → chunk → embed → store → register

#### Vector Store
- ChromaDB integration with local persistence (`app/chroma_db/`)
- Collection-based document storage with embeddings and metadata
- Cosine similarity search via normalized embeddings
- Shared vectorstore singleton pattern via `get_vectorstore()`

#### Testing & Validation
- `test.py` — manual test script for validating the ingestion pipeline
- `validation.py` — reusable file extension and size validation utilities

#### Project Documentation
- Project scaffolding documentation (STATUS.md, TASKS.md, PROJECTPLAN.md, CHANGELOG.md, README.md)
- `.env.example` with placeholder API keys

### Changed

- (No changes yet — initial development)

### Deprecated

- (None)

### Removed

- (None)

### Fixed

- (None)

### Security

- (None)
