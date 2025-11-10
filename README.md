# Voyage RAG - Semantic Search System

A production-ready RAG (Retrieval-Augmented Generation) system using Voyage AI embeddings, FAISS vector search, and FastAPI.

## Overview

This project implements a high-performance semantic search engine combining:

- **Voyage AI** - State-of-the-art embeddings (voyage-3 & voyage-3-lite)
- **FAISS** - Efficient vector similarity search with HNSW indexing
- **FastAPI** - Modern async API with authentication and rate limiting
- **Docker** - Containerized deployment with Traefik reverse proxy

## Features

- Batch document indexing with automatic chunking
- Multi-index support (voyage-3 for quality, voyage-3-lite for speed)
- Production-ready API with JWT authentication
- Comprehensive monitoring and cost tracking
- SSL/TLS termination with automatic certificate renewal
- Horizontal scaling support

## Quick Start

### Prerequisites

- Python 3.11+
- Docker & Docker Compose (for production)
- Voyage AI API key ([get free tier](https://www.voyageai.com))

### Installation

```bash
# Clone repository
git clone <repository-url>
cd voyage-rag

# Create virtual environment
python3.11 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp config/.env.example config/.env
# Edit config/.env with your API keys
```

### Local Development

```bash
# Index sample documents
python scripts/index_documents.py --model voyage-3-lite

# Run API server
uvicorn src.voyage_rag.api:app --reload --port 8000

# Test search
curl -X POST http://localhost:8000/search \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "your search query", "top_k": 5}'
```

### Production Deployment

```bash
# Build and start services
docker-compose up -d

# Check status
docker-compose ps
docker-compose logs -f api

# Access API
curl https://rag.yourdomain.com/health
```

## Project Structure

```
voyage-rag/
├── src/
│   └── voyage_rag/
│       ├── __init__.py          # Package initialization
│       ├── voyage_client.py     # Voyage AI API client
│       ├── batch_indexer.py     # Document indexing
│       ├── search_engine.py     # FAISS search engine
│       └── api.py               # FastAPI application
├── docs/
│   └── PLAN-FINAL-VOYAGE-RAG.md # Complete implementation guide
├── config/
│   ├── .env.example             # Environment template
│   └── traefik/
│       └── traefik.yml          # Reverse proxy config
├── docker/
│   ├── Dockerfile               # Application container
│   └── docker-compose.yml       # Orchestration config
├── data/
│   ├── documents/               # Raw documents
│   ├── indices/                 # FAISS indices
│   └── cache/                   # API cache
├── scripts/
│   ├── index_documents.py       # Indexing script
│   └── monitor_costs.py         # Cost tracking
├── tests/
│   ├── test_voyage_client.py
│   ├── test_indexer.py
│   └── test_api.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Documentation

- **[Complete Implementation Plan](docs/PLAN-FINAL-VOYAGE-RAG.md)** - Comprehensive guide with:
  - 6 critical corrections and optimizations
  - Full architecture and code implementations
  - Deployment checklist (6 phases)
  - Monitoring and cost management
  - Production best practices

## Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Embeddings | Voyage AI (voyage-3, voyage-3-lite) | Semantic vectorization |
| Vector DB | FAISS (HNSW index) | Similarity search |
| API | FastAPI + Uvicorn | REST endpoints |
| Auth | JWT tokens | API authentication |
| Caching | Python functools.lru_cache | Response caching |
| Proxy | Traefik 3.2 | SSL/TLS, routing |
| Containers | Docker + Compose | Deployment |

## Cost Estimation (Voyage AI Free Tier)

**Free Tier Limits:**
- 100M tokens/month FREE
- voyage-3: ~$0.12 per 1M tokens (after free tier)
- voyage-3-lite: ~$0.06 per 1M tokens (after free tier)

**Example Usage:**
- 10,000 documents (500 words avg) = ~7.5M tokens
- 1,000 queries/day = ~0.15M tokens/day = 4.5M tokens/month
- **Total: 12M tokens/month = FREE (within 100M limit)**

For detailed cost analysis, see [docs/PLAN-FINAL-VOYAGE-RAG.md](docs/PLAN-FINAL-VOYAGE-RAG.md#estimation-des-couts).

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check |
| `/search` | POST | Semantic search |
| `/index` | POST | Index document |
| `/stats` | GET | Index statistics |

## Security Features

- JWT authentication with API keys
- Rate limiting (100 requests/minute per key)
- CORS configuration
- SSL/TLS encryption (production)
- No sensitive data in logs

## Monitoring

- Response time tracking
- Token usage monitoring
- Cost estimation dashboard
- Error rate alerts
- FAISS index statistics

## Performance

- **Latency:** <100ms per search (voyage-3-lite)
- **Throughput:** 10,000 documents/hour indexing
- **Scalability:** Horizontal scaling with load balancer
- **Accuracy:** voyage-3 ranks #3 on MTEB leaderboard

## Development

```bash
# Run tests
pytest tests/ -v

# Code formatting
black src/ scripts/
ruff check src/ scripts/

# Type checking
mypy src/
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

## License

[Your License Here]

## Support

- Documentation: [docs/PLAN-FINAL-VOYAGE-RAG.md](docs/PLAN-FINAL-VOYAGE-RAG.md)
- Issues: [GitHub Issues](https://github.com/yourusername/voyage-rag/issues)
- Voyage AI Docs: https://docs.voyageai.com

## Acknowledgments

- [Voyage AI](https://www.voyageai.com) - Embedding models
- [FAISS](https://github.com/facebookresearch/faiss) - Vector search
- [FastAPI](https://fastapi.tiangolo.com) - Web framework

---

Built with Voyage AI embeddings for production-grade semantic search.
