# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**Last Modified:** 2025-11-11

---

## Project Overview

**Voyage RAG** is a production-ready semantic search system (RAG - Retrieval-Augmented Generation) combining:
- **Voyage AI** embeddings (voyage-3 & voyage-3-lite models)
- **Voyage AI** rerank for improved result relevance
- **ChromaDB** vector database with metadata filtering and client-server architecture
- **FastAPI** REST API with JWT authentication and rate limiting
- **Docker Compose** containerization for multi-service deployment (ChromaDB + API)

**Project Stage:** POC/MVP - Focus on velocity over perfection. This is a solo development project with strict adherence to planning documents.

---

## Critical Project Context

### Source of Truth Documents

**ALWAYS read these documents before making any changes:**

1. **`docs/PLAN-FINAL-VOYAGE-RAG.md`** - Complete implementation plan with:
   - 6 critical corrections and architectural decisions
   - Full code implementations for all modules
   - Docker configuration and deployment checklist
   - Monitoring and cost management strategies

2. **`docs/SESSION-PROMPT.md`** - Explicit developer intentions defining:
   - Execution model (deterministic, plan-driven)
   - When to consult vs. when to execute autonomously
   - Commit strategy and documentation requirements
   - Anti-drift measures

3. **`docs/ANTIDRIFT-CHECKLIST.md`** - Validation checklist to prevent:
   - 6 common implementation errors (ChromaDB config, LLM models, error handling, input validation, text chunking, architecture)
   - Module-by-module implementation verification

### Key Architectural Principle

**Separation of Concerns:** The codebase follows strict modular architecture:

```
src/voyage_rag/
├── core/          # Configuration, models, exceptions
├── indexing/      # Voyage AI client, document chunking, ChromaDB indexing
├── search/        # ChromaDB retrieval, Voyage AI reranking
├── api/           # FastAPI endpoints, auth, rate limiting
└── utils/         # Monitoring, logging, cost tracking
```

**Dependency Flow:** `core` ← `indexing` ← `search` ← `api` (unidirectional)

---

## Development Commands

### Environment Setup

```bash
# Create virtual environment (Python 3.11+ required)
python3.11 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp config/.env.example config/.env
# Edit config/.env with your VOYAGE_API_KEY and API_KEYS
```

### Running the API Server

```bash
# Development mode (auto-reload)
uvicorn src.voyage_rag.api:app --reload --port 8000

# Production mode
uvicorn src.voyage_rag.api:app --host 0.0.0.0 --port 8000 --workers 4
```

### Testing

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=src/voyage_rag --cov-report=html

# Run specific test file
pytest tests/test_voyage_client.py -v

# Run specific test
pytest tests/test_api.py::test_search_endpoint -v
```

### Code Quality

```bash
# Format code
black src/ scripts/ tests/

# Lint code
ruff check src/ scripts/ tests/

# Type checking
mypy src/
```

### Docker Operations

```bash
# Build and start all services
docker-compose up -d

# View logs
docker-compose logs -f api

# Check service status
docker-compose ps

# Stop services
docker-compose down

# Rebuild after code changes
docker-compose up -d --build
```

### Indexing Documents

```bash
# Index documents with voyage-3-lite (fast)
python scripts/index_documents.py --model voyage-3-lite

# Index with voyage-3 (higher quality)
python scripts/index_documents.py --model voyage-3

# Index specific directory
python scripts/index_documents.py --model voyage-3-lite --input-dir /path/to/docs
```

### Testing API Endpoints

```bash
# Health check
curl http://localhost:8000/health

# Search (requires API key from config/.env)
curl -X POST http://localhost:8000/search \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "semantic search implementation", "top_k": 5}'

# Get index statistics
curl http://localhost:8000/stats \
  -H "Authorization: Bearer YOUR_API_KEY"
```

---

## Architecture Details

### Voyage AI Integration

**Key Implementation Details:**

1. **Batching Strategy** (Critical - prevents rate limiting):
   - Default batch size: 128 documents per request (Voyage AI limit)
   - Exponential backoff retry on rate limit errors (1s, 2s, 4s, 8s)
   - Token tracking for cost management

2. **Model Selection**:
   - `voyage-3`: Higher quality embeddings (1024 dimensions) - use for critical production
   - `voyage-3-lite`: Faster, cheaper (512 dimensions) - use for development/testing
   - Configurable via `DEFAULT_MODEL` in `.env`

3. **Cost Management**:
   - Free tier: 100M tokens/month
   - voyage-3: ~$0.12/1M tokens (after free tier)
   - voyage-3-lite: ~$0.06/1M tokens (after free tier)
   - Token usage logged for monitoring

### ChromaDB Vector Database

**Configuration:**

- **Client Type**: HTTP Client (client-server architecture)
- **Parameters** (configurable in `.env`):
  - `CHROMA_HOST=localhost`: ChromaDB server hostname
  - `CHROMA_PORT=8000`: ChromaDB server port
  - `CHROMA_COLLECTION=voyage_documents`: Collection name

**Key Features:**
- Metadata filtering with SQL-like syntax (where clauses)
- Automatic persistence (no manual save required)
- CRUD operations (add, query, update, delete)
- Native support for embeddings + documents + metadata together

**Performance Characteristics:**
- Search latency: 5-20ms for small corpus (<100k docs)
- Indexing throughput: 10,000 documents/hour with batching
- Memory: ~4KB per document (1024-dim embeddings + metadata)

### FastAPI Architecture

**Authentication Flow:**
1. Client sends `Authorization: Bearer <API_KEY>` header
2. JWT validation against keys in `API_KEYS` environment variable
3. Rate limiting: 100 requests/minute per key (configurable)

**Endpoints:**
- `GET /health` - Health check (no auth required)
- `POST /search` - Semantic search (auth required)
- `POST /index` - Add document to index (auth required)
- `GET /stats` - Index statistics (auth required)

**Error Handling Strategy:**
- Use specific HTTP status codes (400, 404, 503, not generic 500)
- Return actionable error messages with context
- Structured logging with timestamps and request IDs

---

## Key Implementation Requirements

### Document Chunking

**Configuration** (from ANTIDRIFT-CHECKLIST.md):
- `chunk_size=1000` tokens (configurable)
- `chunk_overlap=200` tokens minimum (preserve semantic context)
- Split on sentence boundaries when possible

### Input Validation

**All API endpoints MUST:**
- Use Pydantic models for request/response validation
- Validate query length (min/max bounds)
- Validate `top_k` parameter (1-100 range)
- Return 400 Bad Request with clear message on validation failure

### Configuration Management

**Environment Variables** (see `config/.env.example`):
- `VOYAGE_API_KEY` - Voyage AI API key (required)
- `API_KEYS` - Comma-separated JWT keys for client auth (required)
- `DEFAULT_MODEL` - voyage-3 or voyage-3-lite (default: voyage-3-lite)
- `EMBEDDING_BATCH_SIZE` - Batch size for embeddings (default: 128, max: 128)
- `RATE_LIMIT_REQUESTS` - Requests per minute (default: 100)
- `ENABLE_CACHE` - Query result caching (default: true)

**Never hardcode:**
- API keys
- Model names
- Batch sizes
- Rate limits

---

## Git Workflow

### Commit Strategy

**Atomic commits are REQUIRED** after:
- Creating new module or file
- Implementing complete feature
- Fixing significant bug
- Adding/updating tests
- Refactoring module

**Commit Message Format:**
```
type: brief description

Optional context or reasoning
```

**Types:** `feat`, `fix`, `refactor`, `docs`, `test`, `chore`

### Branch Strategy

- Development: `claude/*` feature branches
- Always push with `-u origin <branch-name>`
- Implement exponential backoff for network failures (2s, 4s, 8s, 16s)

---

## Testing Requirements

### Test Coverage Expectations

**Critical modules require tests:**
- `indexing/voyage_client.py` - Embedding generation, batching, rate limit handling
- `search/retriever.py` - ChromaDB query, metadata filtering
- `search/reranker.py` - Voyage AI reranking
- `api/routes.py` - All endpoints, auth, rate limiting
- `indexing/chunker.py` - Text chunking with overlap

**Test Types:**
- Unit tests: Individual function logic
- Integration tests: API endpoints, database operations
- Performance tests: Search latency, batch indexing throughput

**Run tests before commits** on significant changes.

---

## Docker & Production Deployment

### Services Architecture

**docker-compose.yml defines:**
1. **chromadb**: Vector database service (port 8000)
2. **api**: FastAPI application (port 8001)

**ChromaDB Configuration:**
- Persistent storage in `data/chromadb` volume
- HTTP API on port 8000
- Health check endpoint for dependency management
- Environment: `IS_PERSISTENT=TRUE`

### Production Checklist

Before deploying:
1. ✅ Set production `VOYAGE_API_KEY` in `.env`
2. ✅ Generate secure `API_KEYS` (use `secrets.token_urlsafe(32)`)
3. ✅ Configure `CHROMA_HOST` and `CHROMA_PORT` (default: chromadb:8000)
4. ✅ Set restrictive `CORS_ORIGINS` (no `*` in production)
5. ✅ Verify ChromaDB volume is persistent (`data/chromadb`)
6. ✅ Test rate limiting and authentication
7. ✅ Ensure ChromaDB health check passes before API starts
8. ✅ Set up monitoring and log aggregation

---

## Troubleshooting

### Common Issues

**Rate Limiting Errors (429):**
- Check batch size doesn't exceed 128
- Verify retry logic with exponential backoff
- Monitor token usage via `scripts/monitor_costs.py`

**ChromaDB Connection Failed:**
- Verify ChromaDB service is running (`docker-compose ps chromadb`)
- Check `CHROMA_HOST` and `CHROMA_PORT` in `.env`
- Test connection: `curl http://localhost:8000/api/v1/heartbeat`
- Review ChromaDB logs: `docker-compose logs chromadb`

**Authentication Failures:**
- Verify `API_KEYS` format (comma-separated, no spaces)
- Check `Authorization: Bearer <key>` header format
- Ensure key matches one in `API_KEYS` list

**Slow Search Performance:**
- Use `voyage-3-lite` instead of `voyage-3` for faster embeddings
- Enable Voyage AI reranking only when necessary (`use_rerank=false`)
- Use metadata filters to reduce search space
- Monitor ChromaDB collection size (consider archiving old data)

---

## Development Philosophy (from SESSION-PROMPT.md)

This project follows a **deterministic, plan-driven development model**:

1. **Plan First**: Always read `docs/PLAN-FINAL-VOYAGE-RAG.md` before implementation
2. **Execute Strictly**: Follow the plan without "creative improvements"
3. **Consult on Ambiguity**: Ask questions rather than making assumptions
4. **Document Decisions**: Update docs when deviating from plan (with user approval)
5. **Commit Atomically**: Every logical unit of work gets its own commit

**Anti-Patterns to Avoid:**
- ❌ Guessing API behavior or data structures
- ❌ Adding features not in the plan
- ❌ Changing architecture without consulting docs
- ❌ Generic error handling (500 errors)
- ❌ Hardcoded configuration values

---

## Additional Resources

- **Voyage AI Docs**: https://docs.voyageai.com
- **ChromaDB Docs**: https://docs.trychroma.com
- **FastAPI Docs**: https://fastapi.tiangolo.com
- **MTEB Leaderboard** (embedding model rankings): https://huggingface.co/spaces/mteb/leaderboard

---

**For detailed implementation guidance, always refer to `docs/PLAN-FINAL-VOYAGE-RAG.md`.**
