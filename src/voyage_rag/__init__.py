"""
Voyage RAG - Semantic Search System

A production-ready RAG (Retrieval-Augmented Generation) system combining:
- Voyage AI embeddings (voyage-3, voyage-3-lite)
- FAISS vector search with HNSW indexing
- FastAPI REST API with authentication and rate limiting
- Docker containerization with Traefik reverse proxy

For complete documentation, see docs/PLAN-FINAL-VOYAGE-RAG.md
"""

__version__ = "1.0.0"
__author__ = "Voyage RAG Team"
__license__ = "MIT"

# Package imports will be added as modules are created
# Uncomment when implementing the respective modules:

# from .voyage_client import VoyageEmbedder
# from .search_engine import FAISSSearchEngine
# from .chunker import DocumentChunker
# from .loader import DocumentLoader
# from .monitoring import MonitoringService

__all__ = [
    "__version__",
    # "VoyageEmbedder",
    # "FAISSSearchEngine",
    # "DocumentChunker",
    # "DocumentLoader",
    # "MonitoringService",
]
