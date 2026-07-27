# AI Research Assistant

An intelligent research assistant that answers questions using uploaded papers, technical documents, books, personal notes, and internet sources — with proper citations.

**Inspirations:** NotebookLM + Perplexity + ChatGPT, focused on research.

---

## Project Status

Currently in **Phase 1 — RAG Backend** (~65% complete). The document ingestion pipeline is fully built:

- ✅ File upload (PDF, DOCX, TXT, MD)
- ✅ Text extraction via LangChain loaders
- ✅ Recursive text chunking with metadata
- ✅ Embeddings via HuggingFace sentence-transformers
- ✅ ChromaDB vector store with persistence
- ✅ SQLite document registry with hash-based deduplication

**Next up:** Prompt builder, LLM integration (Gemini/OpenAI), citation service, and query API.

See [STATUS.md](./STATUS.md) for the current status board and [PROJECTPLAN.md](./PROJECTPLAN.md) for the full plan.

---

## Documentation

| File | Purpose |
|------|---------|
| [PROJECTPLAN.md](./PROJECTPLAN.md) | Full project plan, architecture, phased tasks |
| [STATUS.md](./STATUS.md) | Current status board with progress tracking |
| [TASKS.md](./TASKS.md) | Granular day-to-day task checklist |
| [CHANGELOG.md](./CHANGELOG.md) | Version history and feature changelog |

---

## Tech Stack

### Backend
- **Runtime:** Python 3.12+
- **Framework:** FastAPI
- **Document Parsing:** LangChain (PyPDFLoader, Docx2txtLoader, TextLoader)
- **Text Chunking:** LangChain RecursiveCharacterTextSplitter
- **Embeddings:** HuggingFace sentence-transformers (`all-MiniLM-L6-v2`)
- **Vector Database:** ChromaDB (local persistence)
- **Relational Database:** SQLite via SQLAlchemy
- **Package Manager:** uv

### Frontend (Planned)
- React, TypeScript, Tailwind CSS, Vite

### Infrastructure (Planned)
- Docker

---

## Getting Started

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (Python package manager)

### Setup

```bash
# Clone the repository
git clone <repo-url>
cd ai-research-assistant

# Navigate to the backend directory
cd backend

# Create and activate virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv sync

# Copy environment variables
cp .env.example .env

# Initialize the database
uv run python -m app.database.init_db

# Start the server
uv run uvicorn app.main:app --reload
```

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/upload/` | Upload a document (PDF, DOCX, TXT, MD) — file saved, then run ingestion via `/ingest/` |

---

## Architecture Overview

```
Upload → Loader → Chunker → Embedder → ChromaDB → SQLite Registry
```

The ingestion pipeline converts files into searchable vector embeddings stored in ChromaDB, with metadata tracked in SQLite.
