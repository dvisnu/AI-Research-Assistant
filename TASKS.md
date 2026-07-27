# Tasks — Granular Checklist

> Use this file for day-to-day task tracking. Check off items as you complete them.

---

## Phase 0 — Project Scaffolding ✅ Complete

### 0.1 Repo Setup
- [x] Create backend directory structure (`app/`, `api/`, `services/`, etc.)
- [ ] Create frontend scaffold (Vite + React + TypeScript)
- [x] Set up `pyproject.toml` with dependencies
- [x] Set up dependency lock file (`uv.lock`)

### 0.2 Configuration
- [x] Create `.env.example` with placeholder keys
- [x] Create `config.py` for settings management
- [x] Create `.gitignore`

### 0.3 Docker
- [ ] Write `Dockerfile` for backend
- [ ] Write `docker-compose.yml` for dev environment

### 0.4 Quality Tooling
- [ ] Configure `ruff` for linting
- [ ] Configure `mypy` for type checking
- [ ] Set up pre-commit hooks

---

## Phase 1 — RAG Backend 🚧 In Progress (~65%)

### 1.1 File Upload
- [x] Create upload endpoint accepting PDF, DOCX, TXT, MD
- [x] Validate file types and sizes
- [x] Store uploaded files in `uploads/` directory

### 1.2 Document Parsing
- [x] PDF parser (PyMuPDF via LangChain's PyPDFLoader)
- [x] DOCX parser (python-docx via Docx2txtLoader)
- [x] TXT parser (TextLoader with UTF-8 encoding)
- [x] Markdown parser (TextLoader — .md handled as text)

### 1.3 Chunking
- [x] Implement text splitter (RecursiveCharacterTextSplitter, 1000 tokens, 200 overlap)
- [x] Attach metadata: page number, file name (via LangChain Document)
- [x] Store chunks with unique chunk IDs (handled by ChromaDB)

### 1.4 Embeddings
- [x] Integrate embedding model (HuggingFace sentence-transformers/all-MiniLM-L6-v2)
- [x] Batch embedding generation
- [ ] Cache embeddings to avoid recomputation

### 1.5 Vector Store
- [x] Set up ChromaDB client
- [x] Store document chunks with embeddings + metadata
- [x] Implement collection management (create, delete, list)

### 1.6 Retrieval
- [x] Implement similarity search (cosine via normalized embeddings)
- [x] Return top-K chunks with metadata
- [ ] Add metadata filtering (by document, page, etc.)

### 1.7 Prompt Builder
- [ ] Construct system prompt template
- [ ] Inject retrieved chunks as context
- [ ] Format user question
- [ ] Support adjustable prompt strategies

### 1.8 LLM Integration
- [ ] Integrate Gemini API
- [ ] Integrate OpenAI API (as fallback)
- [ ] Abstract LLM behind a common interface
- [ ] Handle token limits and retries

### 1.9 Citations
- [ ] Extract source info from metadata
- [ ] Format inline citations in response
- [ ] Return structured citation list with answer

---

## Phase 2 — Web Research ❌ Not Started

### 2.1 Search
- [ ] Integrate search API (Tavily / SerpAPI / custom)
- [ ] Return ranked search results with snippets

### 2.2 Scraping
- [ ] Fetch page content from URLs
- [ ] Extract main text content (strip boilerplate)
- [ ] Handle errors (timeouts, blocked pages)

### 2.3 Summarization
- [ ] Summarize individual pages
- [ ] Merge multiple page summaries into coherent context

### 2.4 Web Agent
- [ ] Orchestrate search → scrape → summarize → answer flow
- [ ] Attach source URLs as citations

---

## Phase 3 — Routing & Agents ❌ Not Started

### 3.1 Base Agent
- [ ] Define `BaseAgent` interface (process query → return structured answer)
- [ ] Define response schema (answer, citations, metadata, agent type)

### 3.2 Router
- [ ] Implement heuristic router (keyword-based mode selection)
- [ ] Integrate with agent registry
- [ ] Route query to appropriate agent

### 3.3 RAG Agent
- [ ] Implement agent wrapping document retrieval + LLM
- [ ] Return citations from document sources

### 3.4 Web Agent
- [ ] Implement agent wrapping web search + LLM
- [ ] Return citations from URLs

### 3.5 Hybrid Agent
- [ ] Retrieve documents + search web in parallel
- [ ] Merge context from both sources
- [ ] LLM synthesizes combined answer

---

## Phase 4 — FastAPI Backend 🚧 Partial

### 4.1 Upload API
- [x] `POST /api/documents/upload` or `POST /upload/` — accept file, validate, save
- [ ] `DELETE /api/documents/{id}` — remove document + chunks
- [ ] Ingest endpoint — trigger chunking + embedding after upload

### 4.2 Query API
- [ ] `POST /api/research/query` — send question, get answer
- [ ] Support optional agent/mode parameter
- [ ] Return structured JSON response

### 4.3 Chat API
- [ ] `POST /api/chat` — conversational endpoint with history
- [ ] Return stream or full response

### 4.4 Error Handling
- [ ] Consistent error response schema
- [x] Input validation via Pydantic (file type, size)
- [ ] Rate limiting

---

## Phase 5 — Frontend ❌ Not Started

### 5.1 Setup
- [ ] Scaffold Vite + React + TypeScript + Tailwind
- [ ] Set up routing (React Router)
- [ ] Set up API client (axios or fetch)

### 5.2 Document Management
- [ ] Upload page with drag-and-drop
- [ ] Document list with delete
- [ ] Upload progress indicator

### 5.3 Chat
- [ ] Message list component
- [ ] Input box with send
- [ ] Streaming response display
- [ ] Source/citation panel

### 5.4 Sidebar
- [ ] Workspace switcher
- [ ] Document list
- [ ] Settings link

---

## Phase 6 — Production Enhancements ❌ Not Started

### 6.1 Memory
- [ ] Store conversation history
- [ ] History-aware query rewriting
- [ ] Context window management

### 6.2 Streaming
- [ ] SSE endpoint for streaming LLM responses
- [ ] Frontend renders tokens incrementally

### 6.3 Advanced Retrieval
- [ ] MMR (Maximum Marginal Relevance)
- [ ] Reranking (cross-encoder)
- [ ] Contextual compression

### 6.4 Auth
- [ ] JWT token generation and validation
- [ ] Login / register endpoints
- [ ] Route protection middleware

### 6.5 Docker
- [ ] Production Dockerfile (multi-stage)
- [ ] docker-compose with all services
- [ ] Health checks

### 6.6 Multi-Workspace
- [ ] Workspace CRUD
- [ ] Document isolation per workspace
- [ ] Workspace-scoped retrieval

### 6.7 LangGraph
- [ ] Define graph nodes for each agent
- [ ] Conditional routing between nodes
- [ ] State management across steps

### 6.8 Reports
- [ ] Report template (overview, findings, comparison, references)
- [ ] Gather context from multiple queries
- [ ] Export as PDF or Markdown
