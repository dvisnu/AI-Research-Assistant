# AI Research Assistant — Status Board

> **Last Updated:** 2026-07-28

---

## Overall Health

| Badge | Status |
|-------|--------|
| **Project Phase** | 🚀 Active Development — Phase 1 (RAG Backend) |
| **Progress** | ~45% complete |
| **Build** | 🟢 Ready |
| **Tests** | 🟡 Manual tests only (test.py) |
| **Blockers** | None |

---

## By Phase

| Phase | Progress | Status |
|-------|----------|--------|
| Phase 0 — Scaffolding | 100% | ✅ Complete |
| Phase 1 — RAG Backend | 90% | 🚧 In Progress (reranker + Query API remaining) |
| Phase 2 — Web Research | 0% | ⏳ Not Started |
| Phase 3 — Routing & Agents | 0% | ⏳ Not Started |
| Phase 4 — FastAPI Backend | 15% | 🚧 Partial (upload endpoint done) |
| Phase 5 — Frontend | 0% | ⏳ Not Started |
| Phase 6 — Production | 0% | ⏳ Not Started |

---

## What's Happening Now

- **Phase 1 — RAG Backend** is nearly complete (~90%):
  - ✅ File upload via FastAPI (`POST /upload/`)
  - ✅ File parsing (PDF, DOCX, TXT, MD) using LangChain loaders
  - ✅ Text chunking (RecursiveCharacterTextSplitter, 1000 tokens, 200 overlap) with enriched metadata
  - ✅ Embeddings via HuggingFace `sentence-transformers/all-MiniLM-L6-v2`
  - ✅ ChromaDB vector store with persisted data
  - ✅ SQLite document registry (hash-based dedup, metadata tracking)
  - ✅ Complete ingestion pipeline (`ingestion_service.py`)
  - ✅ MMR-based retrieval service (`retriever_service.py`) — k=5, fetch_k=50, lambda_mult=0.7
  - ✅ RAG prompt builder (`rag_prompts.py`) — structured Answer/Evidence/Sources/Confidence format
  - ✅ Google Gemini LLM integration (`llm_service.py`) — `gemini-2.5-flash-lite`
  - ✅ RAG query service (`rag_service.py`) — orchestrates retriever → prompt → LLM → citations
  - ❌ **Next up:** Cross-encoder reranker, Query API endpoint

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
| **MMR retrieval** | Maximum Marginal Relevance for diverse, relevance-ranked results |
| **Prompt builder** | Structured prompt with Answer/Evidence/Sources/Confidence sections |
| **LLM integration** | Google Gemini (`gemini-2.5-flash-lite`) for answer generation |
| **RAG query service** | Full orchestration: retriever → prompt → LLM → citations |
| **Source citations** | Metadata-backed citations returned with every answer |
| **Enhanced chunking** | Richer chunk metadata (filename, document_hash, chunk_id) |

---

## Up Next

1. **Cross-encoder Reranker** — Improve retrieval precision by reranking MMR results with a cross-encoder model
2. **Query API** — `POST /api/research/query` endpoint exposing the RAG pipeline
3. **Phase 2 — Web Research** — Search API integration, page scraping, web summarization
4. **Phase 4 — Backend Polish** — Consistent error handling, document list/delete endpoints

---

## Risks & Blockers

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Embedding model too large for CPU | Medium | Low | Swap to a smaller model or use API-based embeddings |
| ChromaDB persistence fragility | Low | Low | SQLite backup of document registry provides recovery |
| Cross-encoder model inference speed | Medium | Medium | Use lightweight model (`ms-marco-MiniLM`) and limit reranking candidates |
