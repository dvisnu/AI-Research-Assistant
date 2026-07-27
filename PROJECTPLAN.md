# AI Research Assistant — Project Plan

> **Status:** Active Development — Phase 1 (RAG Backend) | **Last Updated:** 2026-07-28

---

## Status Dashboard

| Metric | Value |
|--------|-------|
| Overall Progress | ~45% |
| Current Phase | Phase 1 — RAG Backend |
| Completed Phases | Phase 0 — Scaffolding ✅, Phase 1 Core RAG ✅ |
| Active Phase | Phase 1 (remaining: Query API, reranker) |
| Next Milestone | Phase 1 completion (Query API, Reranker) |
| Blockers | None |

---

## 1. Project Overview

### Description

An intelligent research assistant that answers questions using:
- Uploaded research papers
- Technical documents
- Books
- Personal notes
- Internet sources

The assistant automatically determines where to search and provides answers with proper citations.

**Inspirations:** NotebookLM + Perplexity + ChatGPT, focused on research rather than general conversation.

### Goals

| Goal | Priority | Status |
|------|----------|--------|
| Local document RAG (PDF, DOCX, TXT, MD) | P0 | ✅ Done (~90%) |
| Web search integration | P1 | ⏳ Planned |
| Hybrid (document + web) research | P1 | ⏳ Planned |
| Multi-agent routing | P1 | ⏳ Planned |
| Streaming responses | P2 | ⏳ Planned |
| Conversation memory | P2 | ⏳ Planned |
| Authentication & multi-workspace | P3 | ⏳ Planned |
| Report generation | P3 | ⏳ Planned |

---

## 2. High-Level Architecture

```
                           AI Research Assistant
                                  │
                   ┌──────────────┴──────────────┐
                   │                             │
             React Frontend                FastAPI Backend
                (Future)                         │
                                  ┌─────────────┴─────────────┐
                                  │                           │
                             API Layer                 Authentication
                                  │
                     ┌────────────┴────────────┐
                     │                         │
                Agent Router            Workspace Manager
                  (Future)                   (Future)
                     │
      ┌──────────────┼───────────────┐
      │              │               │
      ▼              ▼               ▼
  RAG Agent     Web Agent      Hybrid Agent
  (Future)      (Future)        (Future)
      │              │               │
      └──────────────┼───────────────┘
                     ▼
             Response Generator
                  (Future)
                     │
                     ▼
                 JSON Response
                     │
                     ▼
                React Frontend
                (Future)
```

**Key principle:** The **Agent Router** is the central orchestrator. Agents coordinate services; services perform focused tasks.

---

## 3. Folder Structure (Actual)

```
ai-research-assistant/
│
├── backend/
│   ├── app/
│   │   ├── api/              # upload.py, ingest.py
│   │   ├── core/             # config.py
│   │   ├── database/         # models.py, sqlite.py, init_db.py
│   │   ├── prompts/          # rag_prompts.py
│   │   ├── schemas/          # upload.py (Pydantic models)
│   │   ├── services/         # file_service, loader_service, chunking_service,
│   │   │                     # embedding_service, document_service, hash_service,
│   │   │                     # ingestion_service, validation, llm_service,
│   │   │                     # rag_service, retriever_service
│   │   ├── vectorstore/      # chroma.py
│   │   ├── chroma_db/        # Persisted Chroma data
│   │   ├── main.py           # FastAPI entry point
│   │   └── __init__.py
│   │
│   ├── documents.db          # SQLite database
│   ├── test.py               # Manual test script
│   │
│   ├── pyproject.toml
│   └── uv.lock
│
├── .env.example
├── .gitignore
├── CHANGELOG.md
├── PROJECTPLAN.md
├── README.md
├── STATUS.md
└── TASKS.md
```

---

## 4. Component Architecture

### 4.1 Document Ingestion Service ✅ (Implemented)

Converts uploaded files into searchable knowledge.

**Pipeline:** `Upload → Loader → Extract Text → Split into Chunks → Generate Embeddings → Store in Chroma`

**Supported formats:** PDF, DOCX, TXT, Markdown

**Implementation:**
- **Upload:** FastAPI `POST /upload/` with file type & size validation
- **Loader:** LangChain PyPDFLoader (PDF), Docx2txtLoader (DOCX), TextLoader (TXT/MD)
- **Chunking:** RecursiveCharacterTextSplitter (1000 tokens, 200 overlap) with custom metadata enrichment (filename, document_hash, chunk_id)
- **Embeddings:** HuggingFace `sentence-transformers/all-MiniLM-L6-v2` (CPU)
- **Vector Store:** ChromaDB with persistence
- **Dedup:** SHA-256 hash-based duplicate detection via SQLite document registry

### 4.2 Chunking ✅ (Enhanced)

Each chunk stores: Text, Page Number (from LangChain metadata), File Name, Document Hash, Chunk ID (deterministic: `{file_hash}_{chunk_id}`)

### 4.3 Vector Database ✅ (Implemented)

**Current:** ChromaDB (local, persisted to `app/chroma_db/`)

The retrieval layer is abstracted behind `get_vectorstore()` so you can switch later.

### 4.4 Retrieval Service ✅ (Implemented — MMR)

ChromaDB similarity search (cosine distance) with MMR diversification (k=5, fetch_k=50, lambda_mult=0.7). Future work includes cross-encoder reranking.

### 4.5 Prompt Builder ✅ (Implemented)

Receives `Question + Retrieved Chunks` and produces a structured prompt with Answer/Evidence/Sources/Confidence sections. Defined in `rag_prompts.py` using LangChain's `ChatPromptTemplate`.

### 4.6 LLM Generator ✅ (Implemented — Gemini)

Single responsibility: `Prompt → Gemini → Answer`
- Uses Google Gemini (`gemini-2.5-flash-lite`) via `langchain-google-genai`
- Abstracted behind `get_llm()` for future swappability

### 4.7 Citation Service ✅ (Implemented)

Every answer returns metadata-backed citations (source filename, page number). Sources are extracted from chunk metadata and returned alongside the structured answer.

### 4.8 Reranker ❌ (Planned — Not Yet Implemented)

Cross-encoder reranking to improve retrieval precision. Will use `ContextualCompressionRetriever` with a HuggingFace cross-encoder model.

### 4.9–4.13 Agents, Router, Memory, Reports ❌ (Future)

---

## 5. Data Flows

### RAG (Document Query) — Fully Implemented

```
User uploads PDF → Document Loader → Text Splitter → Embedding Model → ChromaDB (✅)
                                                                   
User Question → Retriever (MMR) → Reranker → Prompt Builder → LLM → Answer + Citations
                (✅)                 (❌)       (✅)          (✅)      (✅)
```

### Hybrid Query (Future)

```
User Question → Router
                ├── RAG Agent ──┐
                └── Web Search ──┘
                     → Merge Context → Prompt Builder → LLM → Answer
```

---

## 6. Development Phases

### Phase 0 — Project Scaffolding ✅ Complete

| # | Task | Description | Priority | Status | Dependencies |
|---|------|-------------|----------|--------|-------------|
| 0.1 | Repo setup & structure | Create backend scaffolds, config files | P0 | ✅ Done | None |
| 0.2 | Dependency management | Set up pyproject.toml, uv.lock | P0 | ✅ Done | 0.1 |
| 0.3 | Docker setup | Dockerfile + docker-compose for dev | P1 | ⏳ Planned | 0.1 |
| 0.4 | Linting & formatting | Ruff, mypy, pre-commit hooks | P1 | ⏳ Planned | 0.1 |

### Phase 1 — RAG Backend 🚧 In Progress (~90%)

| # | Task | Description | Priority | Status | Dependencies |
|---|------|-------------|----------|--------|-------------|
| 1.1 | File upload endpoint | Accept PDF/DOCX/TXT/MD uploads | P0 | ✅ Done | 0.1 |
| 1.2 | Document parsers | Extract text from uploaded files | P0 | ✅ Done | 1.1 |
| 1.3 | Text chunking | Split documents into chunks with metadata | P0 | ✅ Done | 1.2 |
| 1.4 | Embedding service | Generate embeddings (HuggingFace sentence-transformers) | P0 | ✅ Done | 1.3 |
| 1.5 | Vector store | ChromaDB integration for storage & retrieval | P0 | ✅ Done | 1.4 |
| 1.6 | Similarity search | Retrieve relevant chunks by query | P0 | ✅ Done | 1.5 |
| 1.7 | Prompt builder | Construct structured prompts from query + chunks | P0 | ✅ Done | 1.6 |
| 1.8 | LLM integration | Generate answers via Gemini | P0 | ✅ Done | 1.7 |
| 1.9 | Source citations | Attach metadata citations to answers | P0 | ✅ Done | 1.8 |
| 1.10 | Cross-encoder reranker | Rerank retrieved chunks for improved precision | P0 | ⏳ Planned | 1.6 |

### Phase 2 — Web Research ❌ Not Started

| # | Task | Description | Priority | Status | Dependencies |
|---|------|-------------|----------|--------|-------------|
| 2.1 | Search API integration | Google/Bing/Tavily search | P1 | ⏳ Planned | 1.8 |
| 2.2 | Page scraper | Fetch and extract content from URLs | P1 | ⏳ Planned | 2.1 |
| 2.3 | Web summarizer | Summarize fetched page content | P1 | ⏳ Planned | 2.2 |
| 2.4 | Web agent | Orchestrate search → scrape → summarize → answer | P1 | ⏳ Planned | 2.3 |

### Phase 3 — Routing & Agents ❌ Not Started

| # | Task | Description | Priority | Status | Dependencies |
|---|------|-------------|----------|--------|-------------|
| 3.1 | Base agent interface | Common contract for all agents | P1 | ⏳ Planned | 1.8 |
| 3.2 | Router service | Heuristic/LLM-based agent selection | P1 | ⏳ Planned | 3.1 |
| 3.3 | RAG agent | Document-only agent (wraps Phase 1) | P0 | ⏳ Planned | 1.9, 3.1 |
| 3.4 | Web agent | Web-only agent (wraps Phase 2) | P1 | ⏳ Planned | 2.4, 3.1 |
| 3.5 | Hybrid agent | Merges document + web context | P1 | ⏳ Planned | 3.3, 3.4 |

### Phase 4 — FastAPI Backend 🚧 Partial

| # | Task | Description | Priority | Status | Dependencies |
|---|------|-------------|----------|--------|-------------|
| 4.1 | Upload API | POST /upload/ — accept file, validate, save | P0 | ✅ Done | 1.4 |
| 4.2 | Query API | POST /api/research/query | P0 | ⏳ Planned | 1.8 |
| 4.3 | Chat API | POST /api/chat (with history) | P1 | ⏳ Planned | 4.2 |
| 4.4 | Document list API | GET /api/documents | P1 | ⏳ Planned | 4.1 |
| 4.5 | Error handling & validation | Consistent error responses, input validation | P1 | ⏳ Planned | 4.1 |

### Phase 5 — Frontend ❌ Not Started

| # | Task | Description | Priority | Status | Dependencies |
|---|------|-------------|----------|--------|-------------|
| 5.1 | Project scaffold | Vite + React + TypeScript + Tailwind | P1 | ⏳ Planned | None |
| 5.2 | Document management | Upload, list, delete documents | P1 | ⏳ Planned | 4.1, 4.4 |
| 5.3 | Chat interface | Message list + input with streaming | P1 | ⏳ Planned | 4.3 |
| 5.4 | Source display | Show citations alongside answers | P1 | ⏳ Planned | 1.8 |
| 5.5 | Workspace UI | Sidebar with workspaces list | P2 | ⏳ Planned | 5.1 |

### Phase 6 — Production Enhancements ❌ Not Started

| # | Task | Description | Priority | Status | Dependencies |
|---|------|-------------|----------|--------|-------------|
| 6.1 | Conversation memory | History-aware retrieval for follow-ups | P2 | ⏳ Planned | 4.3 |
| 6.2 | Streaming responses | SSE-based token streaming | P2 | ⏳ Planned | 4.3 |
| 6.3 | Incremental indexing | Re-index only changed documents | P2 | ⏳ Planned | 1.5 |
| 6.4 | Advanced retrieval | MMR, reranking, contextual compression | P2 | ⏳ Planned | 1.6 |
| 6.5 | Authentication | JWT-based user auth | P3 | ⏳ Planned | 4.0 |
| 6.6 | Docker deployment | Production docker-compose | P3 | ⏳ Planned | 0.3 |
| 6.7 | Multi-workspace | Isolated workspaces per user/project | P3 | ⏳ Planned | 6.5 |
| 6.8 | LangGraph orchestration | Complex multi-step research workflows | P3 | ⏳ Planned | 3.5 |
| 6.9 | Report generation | Structured research reports | P3 | ⏳ Planned | 3.5 |

---

## 7. Design Principles

- **Single Responsibility:** Each service does one thing well.
- **Agent-based orchestration:** Agents coordinate services rather than implementing low-level logic themselves.
- **Swappable components:** Embedding models, vector databases, and LLMs should be replaceable through clear interfaces.
- **Structured responses:** Agents should return rich JSON (answer, citations, metadata), not plain strings.
- **Future-proofing:** The MVP should naturally evolve into a multi-agent research platform without major architectural changes.

---

## 8. Completion Criteria

### Phase 0 — Done ✅
- [x] Repo scaffold created (backend structure, config, gitignore, .env.example)
- [x] Dependencies declared (pyproject.toml, uv.lock)
- [x] Dev environment reproducible via `uv` (virtual environment)
- [ ] Docker setup (pending)

### Phase 1 — Target
- [x] User can upload a PDF and get it indexed into ChromaDB
- [x] All major file formats (PDF, DOCX, TXT, MD) parse correctly
- [x] Chunking preserves metadata (page numbers, filenames)
- [x] Vector search returns relevant results
- [x] User can ask a question and get back an answer with source citations
- [ ] Query API endpoint (`POST /api/research/query`) exposed
- [ ] Cross-encoder reranker improves retrieval precision

### Phase 2 — Target
- [ ] Web search returns structured answers with URLs
- [ ] Web pages can be scraped and summarized
- [ ] Web agent produces citation-backed answers

### Phase 3 — Target
- [ ] Router correctly delegates to RAG / Web / Hybrid agents
- [ ] Hybrid agent merges document + web context coherently
- [ ] All agents conform to a common interface

### Phase 4 — Target
- [ ] All endpoints documented and working
- [ ] Consistent error handling
- [ ] Input validation in place

### Phase 5 — Target
- [ ] User can upload, view, and delete documents from UI
- [ ] Chat works with streaming
- [ ] Sources are displayed clearly

### Phase 6 — Target
- [ ] Follow-up questions retain context
- [ ] Responses stream in real-time
- [ ] Auth protects routes
- [ ] App runs in Docker
