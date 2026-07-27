# AI Research Assistant

An intelligent research assistant that answers questions using uploaded papers, technical documents, books, personal notes, and internet sources — with proper citations.

**Inspirations:** NotebookLM + Perplexity + ChatGPT, focused on research.

---

## Project Status

Currently in **Phase 1 — RAG Backend** (~90% complete). The full RAG pipeline is built:

- ✅ File upload (PDF, DOCX, TXT, MD)
- ✅ Text extraction via LangChain loaders
- ✅ Recursive text chunking with enriched metadata
- ✅ Embeddings via HuggingFace sentence-transformers
- ✅ ChromaDB vector store with persistence
- ✅ SQLite document registry with hash-based deduplication
- ✅ **MMR-based retrieval** (diverse, relevance-ranked results)
- ✅ **Prompt builder** — structured prompts with Answer/Evidence/Sources/Confidence sections
- ✅ **Google Gemini LLM integration** — answer generation via `gemini-2.5-flash-lite`
- ✅ **Source citations** — metadata-backed citations returned with every answer
- ❌ **Next up:** Cross-encoder reranker, Query API endpoint, Web research

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
- **LLM:** Google Gemini (`gemini-2.5-flash-lite`) via `langchain-google-genai`
- **Vector Database:** ChromaDB (local persistence)
- **Retrieval:** MMR (Maximum Marginal Relevance) with cosine similarity
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
# Edit .env and add your GOOGLE_API_KEY

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
| POST | `/api/research/query` | (Planned) Send a question, get an answer with source citations |

---

## Architecture Overview

```
                                ┌─────────────────┐
                                │   User Query     │
                                └────────┬────────┘
                                         │
                                         ▼
                              ┌─────────────────────┐
                              │  Retriever (MMR)     │
                              │  ChromaDB → Top-K    │
                              └────────┬────────────┘
                                       │
                                       ▼
                            ┌─────────────────────┐
                            │  Reranker (Planned)  │
                            │  Cross-encoder       │
                            └────────┬────────────┘
                                     │
                                     ▼
                            ┌─────────────────────┐
                            │  Prompt Builder      │
                            │  Context + Question  │
                            └────────┬────────────┘
                                     │
                                     ▼
                            ┌─────────────────────┐
                            │  LLM (Gemini)        │
                            │  Generate Answer     │
                            └────────┬────────────┘
                                     │
                                     ▼
                            ┌─────────────────────┐
                            │  Answer + Citations  │
                            └─────────────────────┘
```

The ingestion pipeline converts files into searchable vector embeddings stored in ChromaDB, with metadata tracked in SQLite. The retrieval pipeline uses MMR for diverse relevance-ranked results, feeds them into a structured prompt, generates an answer via Google Gemini, and returns it with source citations.
