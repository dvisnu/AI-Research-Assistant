# AI Research Assistant — Status Board

> **Last Updated:** 2026-07-27

---

## Overall Health

| Badge | Status |
|-------|--------|
| **Project Phase** | 🚀 Active Development — Phase 1 (RAG Backend) |
| **Progress** | ~30% complete |
| **Build** | 🟢 Ready |
| **Tests** | 🟡 Manual tests only (test.py) |
| **Blockers** | None |

---

## By Phase

| Phase | Progress | Status |
|-------|----------|--------|
| Phase 0 — Scaffolding | 100% | ✅ Complete |
| Phase 1 — RAG Backend | 65% | 🚧 In Progress |
| Phase 2 — Web Research | 0% | ⏳ Not Started |
| Phase 3 — Routing & Agents | 0% | ⏳ Not Started |
| Phase 4 — FastAPI Backend | 15% | 🚧 Partial (upload endpoint done) |
| Phase 5 — Frontend | 0% | ⏳ Not Started |
| Phase 6 — Production | 0% | ⏳ Not Started |

---

## What's Happening Now

- **Phase 1 — RAG Backend** is well underway:
  - ✅ File upload via FastAPI (`POST /upload/`)
  - ✅ File parsing (PDF, DOCX, TXT, MD) using LangChain loaders
  - ✅ Text chunking (RecursiveCharacterTextSplitter, 1000 tokens, 200 overlap)
  - ✅ Embeddings via HuggingFace `sentence-transformers/all-MiniLM-L6-v2`
  - ✅ ChromaDB vector store with persisted data
  - ✅ SQLite document registry (hash-based dedup, metadata tracking)
  - ✅ Complete ingestion pipeline (`ingestion_service.py`)
  - ✅ Auto-generated `test.py` for validation
  - ❌ **Next up:** Prompt builder, LLM integration, citation service, retrieval API

---

## Recently Completed

| Feature | Detail |
|---------|--------|
| Project scaffolding | Backend structure, pyproject.toml, config, gitignore, .env.example |
| File upload API | `POST /upload/` with validation (type + size) |
| Document loaders | PyMuPDF (PDF), Docx2txt (DOCX), TextLoader (TXT/MD) |
| Text chunking | RecursiveCharacterTextSplitter with metadata preservation |
| Embedding service | HuggingFace sentence-transformers on CPU |
| Vector store | ChromaDB with add_documents and similarity search |
| Document registry | SQLite via SQLAlchemy with hash-based deduplication |
| Ingestion pipeline | End-to-end: hash → parse → chunk → embed → store → register |

---

## Up Next

1. **Prompt Builder** — Construct structured prompts from query + retrieved chunks
2. **LLM Integration** — Gemini / OpenAI for answer generation
3. **Citation Service** — Extract source metadata, format inline citations
4. **Query API** — `POST /api/research/query` for retrieval + answer
5. **Phase 2 — Web Research** — Search, scrape, summarize

---

## Risks & Blockers

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Embedding model too large for CPU | Medium | Low | Swap to a smaller model or use API-based embeddings |
| ChromaDB persistence fragility | Low | Low | SQLite backup of document registry provides recovery |
| API key dependency for Gemini/OpenAI | Medium | Medium | Use .env.example to document required keys |
