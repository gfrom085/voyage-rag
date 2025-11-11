# PLAN FINAL - Voyage RAG avec ChromaDB et FastAPI

## Table des Matières

1. [Vue d'Ensemble](#vue-densemble)
2. [Architecture Technique](#architecture-technique)
3. [Stack Technologique](#stack-technologique)
4. [Composants Critiques](#composants-critiques)
5. [Structure du Projet](#structure-du-projet)
6. [Implémentation par Module](#implémentation-par-module)
7. [Configuration Docker](#configuration-docker)
8. [Workflow de Développement](#workflow-de-développement)
9. [Monitoring et Coûts](#monitoring-et-coûts)

---

## Vue d'Ensemble

### Objectif du Projet

Créer un système RAG (Retrieval-Augmented Generation) de production combinant:

- **Embeddings de qualité**: Voyage AI (voyage-3 et voyage-3-lite)
- **Reranking intelligent**: Voyage AI Rerank API
- **Base vectorielle complète**: ChromaDB avec filtrage metadata
- **API robuste**: FastAPI avec authentification et rate limiting
- **Déploiement conteneurisé**: Docker Compose avec services séparés

### Caractéristiques Principales

| Fonctionnalité | Description |
|----------------|-------------|
| **Embeddings Voyage AI** | voyage-3-lite (dev) et voyage-3 (prod) pour qualité maximale |
| **Reranking Voyage AI** | API rerank pour améliorer précision des résultats |
| **ChromaDB** | Base vectorielle avec metadata natifs et filtrage avancé |
| **Filtrage Metadata** | Recherche par source, catégorie, tags, timestamp, etc. |
| **API RESTful** | Endpoints pour indexation, recherche, statistiques |
| **Authentification** | JWT avec clés API multiples |
| **Rate limiting** | Protection contre abus (configurable) |
| **Batch Processing** | Indexation optimisée par batches (128 docs/requête) |
| **Docker Compose** | ChromaDB + API dans conteneurs séparés |

### Décisions Architecturales

**Pourquoi ChromaDB plutôt que FAISS?**
- ✅ Metadata natifs avec filtrage SQL-like
- ✅ Persistance automatique (pas de save() manuel)
- ✅ API simple et intuitive (onboarding 15 min)
- ✅ CRUD complet (update/delete faciles)
- ✅ Petit corpus (<100k docs) = latence acceptable
- ✅ Dev velocity > Performance extrême

**Pourquoi Voyage AI?**
- ✅ Top-tier sur MTEB leaderboard
- ✅ voyage-3: #1 pour retrieval quality
- ✅ Rerank API pour post-processing des résultats
- ✅ Support natif document/query input types
- ✅ Batch processing jusqu'à 128 docs/requête

---

## Architecture Technique

### Diagramme de Flux

```
┌─────────────┐
│   Client    │
│  (API Call) │
└──────┬──────┘
       │
       ▼
┌─────────────────────┐
│   FastAPI Server    │
│  - Authentication   │
│  - Rate Limiting    │
│  - Input Validation │
└──────┬──────────────┘
       │
       ├───────────────────┐
       ▼                   ▼
┌─────────────┐     ┌──────────────┐
│  Voyage AI  │     │  ChromaDB    │
│   Client    │     │   Service    │
│             │     │ (HTTP:8000)  │
│ - Embed     │     │              │
│ - Rerank    │     │ - Vectors    │
└─────────────┘     │ - Metadata   │
                    │ - Filtering  │
                    └──────────────┘
```

### Séparation des Responsabilités

```
src/voyage_rag/
├── core/                # Configuration, models, exceptions
│   ├── config.py       # Settings Pydantic (env vars)
│   ├── models.py       # Document, SearchResult dataclasses
│   └── exceptions.py   # Custom exceptions hierarchy
│
├── indexing/           # Document processing & embedding
│   ├── voyage_client.py    # VoyageEmbedder (batching, retry)
│   ├── chunker.py          # Text chunking avec overlap
│   └── indexer.py          # ChromaIndexer (batch add)
│
├── search/             # Recherche & reranking
│   ├── retriever.py    # ChromaRetriever (query + filters)
│   └── reranker.py     # VoyageReranker (post-processing)
│
├── api/                # FastAPI endpoints
│   ├── main.py         # App setup, CORS, lifespan
│   ├── routes.py       # /index, /search endpoints
│   ├── auth.py         # JWT validation
│   └── dependencies.py # Dependency injection
│
└── utils/              # Monitoring, logging
    ├── monitoring.py   # Cost tracking, metrics
    └── logger.py       # Structured logging
```

---

## Stack Technologique

### Technologies et Versions

```yaml
# Backend
Python: 3.11+
FastAPI: fastapi>=0.110.0
Uvicorn: uvicorn[standard]>=0.27.0
Pydantic: pydantic>=2.5.0

# Voyage AI
voyageai: voyageai>=0.2.3

# ChromaDB
chromadb: chromadb>=0.4.22
httpx: httpx>=0.26.0  # Pour client HTTP ChromaDB

# Utils
python-dotenv: python-dotenv>=1.0.0
python-multipart: python-multipart>=0.0.6

# Docker
Docker: 24.0+
Docker Compose: 2.20+
ChromaDB Image: chromadb/chroma:latest
```

### Configuration Minimale Requise

```bash
# Hardware
RAM: 4GB minimum (8GB recommandé)
CPU: 2 cores minimum
Disk: 10GB pour petit corpus (<10k docs)

# API Keys
VOYAGE_API_KEY: Obligatoire (https://www.voyageai.com)
API_KEYS: Obligatoire (clés JWT comma-separated)
```

---

## Composants Critiques

### 1. Voyage AI Rate Limits et Batching

**Problématique:**
Voyage AI limite à 128 documents par requête. Sans batching, indexer 10,000 docs = 10,000 requêtes API (slow + coûteux).

**Solution:**

```python
# core/voyage_client.py
import time
from typing import List, Optional
from voyageai import Client as VoyageClient

class VoyageEmbedder:
    """Client Voyage AI avec batching et retry automatique."""

    def __init__(
        self,
        api_key: str,
        model: str = "voyage-3-lite",
        batch_size: int = 128,
        max_retries: int = 3,
        initial_retry_delay: float = 1.0
    ):
        self.client = VoyageClient(api_key=api_key)
        self.model = model
        self.batch_size = batch_size
        self.max_retries = max_retries
        self.initial_retry_delay = initial_retry_delay

        # Statistiques
        self.total_tokens = 0
        self.total_requests = 0
        self.total_documents = 0

    def embed_batch(
        self,
        texts: List[str],
        input_type: str = "document"
    ) -> List[List[float]]:
        """
        Encode un batch de textes avec retry automatique.

        Args:
            texts: Liste de textes (max batch_size)
            input_type: "document" ou "query"

        Returns:
            Liste d'embeddings (1024 dimensions pour voyage-3)
        """
        if len(texts) > self.batch_size:
            raise ValueError(
                f"Batch trop grand: {len(texts)} > {self.batch_size}"
            )

        for attempt in range(self.max_retries):
            try:
                response = self.client.embed(
                    texts=texts,
                    model=self.model,
                    input_type=input_type
                )

                # Statistiques
                self.total_tokens += response.total_tokens
                self.total_requests += 1
                self.total_documents += len(texts)

                return response.embeddings

            except Exception as e:
                if attempt == self.max_retries - 1:
                    raise

                # Backoff exponentiel
                delay = self.initial_retry_delay * (2 ** attempt)
                print(
                    f"Retry dans {delay}s "
                    f"(tentative {attempt + 1}/{self.max_retries})"
                )
                time.sleep(delay)

    def embed_documents(
        self,
        documents: List[str],
        show_progress: bool = True
    ) -> List[List[float]]:
        """Encode une liste de documents avec batching automatique."""
        embeddings = []
        total_batches = (len(documents) + self.batch_size - 1) // self.batch_size

        for i in range(0, len(documents), self.batch_size):
            batch = documents[i:i + self.batch_size]
            batch_embeddings = self.embed_batch(batch, input_type="document")
            embeddings.extend(batch_embeddings)

            if show_progress:
                batch_num = i // self.batch_size + 1
                print(
                    f"Batch {batch_num}/{total_batches} - "
                    f"{len(embeddings)}/{len(documents)} documents encodés"
                )

        return embeddings

    def embed_query(self, query: str) -> List[float]:
        """Encode une requête de recherche."""
        embeddings = self.embed_batch([query], input_type="query")
        return embeddings[0]

    def get_stats(self) -> dict:
        """Retourne les statistiques d'utilisation."""
        return {
            "total_tokens": self.total_tokens,
            "total_requests": self.total_requests,
            "total_documents": self.total_documents,
            "avg_tokens_per_doc": (
                self.total_tokens / self.total_documents
                if self.total_documents > 0
                else 0
            )
        }
```

**Avantages:**
- Réduction de 128x du nombre de requêtes API
- Gestion automatique des erreurs avec backoff exponentiel
- Tracking des tokens pour estimation des coûts
- Support document/query input types

---

### 2. ChromaDB Setup et Intégration

**Configuration ChromaDB Client-Serveur:**

```python
# indexing/indexer.py
import chromadb
from chromadb.config import Settings
from typing import List, Dict, Optional

class ChromaIndexer:
    """Indexer pour ChromaDB avec support metadata et filtrage."""

    def __init__(
        self,
        host: str = "localhost",
        port: int = 8000,
        collection_name: str = "voyage_documents"
    ):
        """
        Initialise le client ChromaDB.

        Args:
            host: Hostname ChromaDB server
            port: Port ChromaDB server (default: 8000)
            collection_name: Nom de la collection
        """
        self.client = chromadb.HttpClient(
            host=host,
            port=port,
            settings=Settings(allow_reset=True)
        )

        # Récupérer ou créer collection
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            metadata={"description": "Voyage AI embeddings"}
        )

    def add_documents(
        self,
        documents: List[str],
        embeddings: List[List[float]],
        metadatas: Optional[List[Dict]] = None,
        ids: Optional[List[str]] = None
    ) -> None:
        """
        Ajoute des documents à ChromaDB.

        Args:
            documents: Liste de textes
            embeddings: Liste d'embeddings Voyage AI
            metadatas: Métadonnées par document
            ids: IDs custom (auto-générés si None)
        """
        if not ids:
            import uuid
            ids = [str(uuid.uuid4()) for _ in documents]

        self.collection.add(
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas or [{}] * len(documents),
            ids=ids
        )

    def count(self) -> int:
        """Retourne le nombre de documents indexés."""
        return self.collection.count()

    def delete_all(self) -> None:
        """Supprime tous les documents (utile pour tests)."""
        self.client.delete_collection(self.collection.name)
        self.collection = self.client.create_collection(
            name=self.collection.name
        )
```

**Configuration docker-compose.yml:**

```yaml
version: '3.8'

services:
  chromadb:
    image: chromadb/chroma:latest
    container_name: voyage-rag-chromadb
    ports:
      - "8000:8000"
    volumes:
      - ./data/chromadb:/chroma/chroma
    environment:
      - IS_PERSISTENT=TRUE
      - ANONYMIZED_TELEMETRY=FALSE
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/api/v1/heartbeat"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - voyage-rag-network

  api:
    build: .
    container_name: voyage-rag-api
    ports:
      - "8001:8001"
    environment:
      - VOYAGE_API_KEY=${VOYAGE_API_KEY}
      - API_KEYS=${API_KEYS}
      - CHROMA_HOST=chromadb
      - CHROMA_PORT=8000
    depends_on:
      chromadb:
        condition: service_healthy
    networks:
      - voyage-rag-network

networks:
  voyage-rag-network:
    driver: bridge
```

---

### 3. Voyage AI Reranking

**Intégration Rerank API:**

```python
# search/reranker.py
from typing import List, Dict
from voyageai import Client as VoyageClient

class VoyageReranker:
    """Reranker utilisant Voyage AI Rerank API."""

    def __init__(self, api_key: str, model: str = "rerank-1"):
        self.client = VoyageClient(api_key=api_key)
        self.model = model

    def rerank(
        self,
        query: str,
        documents: List[str],
        top_k: Optional[int] = None
    ) -> List[Dict]:
        """
        Rerank les documents selon la requête.

        Args:
            query: Requête de l'utilisateur
            documents: Liste de documents à reranker
            top_k: Nombre de résultats à retourner (None = tous)

        Returns:
            Liste de dicts avec {document, index, relevance_score}
        """
        response = self.client.rerank(
            query=query,
            documents=documents,
            model=self.model,
            top_k=top_k
        )

        # Format response
        results = []
        for result in response.results:
            results.append({
                "document": documents[result.index],
                "index": result.index,
                "relevance_score": result.relevance_score
            })

        return results
```

**Workflow Complet (Retrieval + Rerank):**

```python
# search/retriever.py
from typing import List, Dict, Optional
import chromadb

class ChromaRetriever:
    """Retriever pour ChromaDB avec filtrage metadata."""

    def __init__(
        self,
        host: str = "localhost",
        port: int = 8000,
        collection_name: str = "voyage_documents"
    ):
        self.client = chromadb.HttpClient(host=host, port=port)
        self.collection = self.client.get_collection(name=collection_name)

    def search(
        self,
        query_embedding: List[float],
        top_k: int = 10,
        where: Optional[Dict] = None,
        where_document: Optional[Dict] = None
    ) -> List[Dict]:
        """
        Recherche dans ChromaDB avec filtrage optionnel.

        Args:
            query_embedding: Embedding de la requête
            top_k: Nombre de résultats
            where: Filtres metadata (ex: {"source": "doc1"})
            where_document: Filtres sur le texte

        Returns:
            Liste de résultats avec documents et metadata
        """
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            where=where,
            where_document=where_document
        )

        # Format results
        formatted = []
        for i, doc_id in enumerate(results['ids'][0]):
            formatted.append({
                "id": doc_id,
                "document": results['documents'][0][i],
                "metadata": results['metadatas'][0][i],
                "distance": results['distances'][0][i]
            })

        return formatted


# Pipeline complet
class RAGPipeline:
    """Pipeline RAG complet: Embed -> Retrieve -> Rerank."""

    def __init__(
        self,
        embedder: VoyageEmbedder,
        retriever: ChromaRetriever,
        reranker: Optional[VoyageReranker] = None
    ):
        self.embedder = embedder
        self.retriever = retriever
        self.reranker = reranker

    def search(
        self,
        query: str,
        top_k: int = 10,
        use_rerank: bool = True,
        where: Optional[Dict] = None
    ) -> List[Dict]:
        """
        Recherche complète avec reranking optionnel.

        Args:
            query: Requête utilisateur
            top_k: Nombre de résultats finaux
            use_rerank: Utiliser reranking
            where: Filtres metadata ChromaDB

        Returns:
            Résultats finaux (reranked ou non)
        """
        # 1. Embed query
        query_embedding = self.embedder.embed_query(query)

        # 2. Retrieve (2x top_k si rerank)
        retrieve_k = top_k * 2 if use_rerank else top_k
        results = self.retriever.search(
            query_embedding=query_embedding,
            top_k=retrieve_k,
            where=where
        )

        # 3. Rerank (optionnel)
        if use_rerank and self.reranker:
            documents = [r['document'] for r in results]
            reranked = self.reranker.rerank(
                query=query,
                documents=documents,
                top_k=top_k
            )

            # Merge metadata from original results
            for rerank_result in reranked:
                original_result = results[rerank_result['index']]
                rerank_result['metadata'] = original_result['metadata']
                rerank_result['id'] = original_result['id']

            return reranked

        return results[:top_k]
```

---

### 4. Document Chunking avec Overlap

```python
# indexing/chunker.py
from typing import List, Dict
import re

class DocumentChunker:
    """Chunker de documents avec overlap pour préserver contexte."""

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
        separator: str = "\n\n"
    ):
        """
        Args:
            chunk_size: Taille max du chunk (caractères)
            chunk_overlap: Overlap entre chunks
            separator: Séparateur principal (paragraphes)
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.separator = separator

    def chunk_text(
        self,
        text: str,
        metadata: Optional[Dict] = None
    ) -> List[Dict]:
        """
        Découpe un texte en chunks avec overlap.

        Args:
            text: Texte à chunker
            metadata: Métadonnées à propager à tous les chunks

        Returns:
            Liste de dicts {text, metadata, chunk_index}
        """
        # Split par paragraphes
        paragraphs = text.split(self.separator)

        chunks = []
        current_chunk = ""
        chunk_index = 0

        for para in paragraphs:
            # Si ajouter ce paragraphe dépasse chunk_size
            if len(current_chunk) + len(para) > self.chunk_size:
                if current_chunk:
                    chunk_metadata = metadata.copy() if metadata else {}
                    chunk_metadata['chunk_index'] = chunk_index

                    chunks.append({
                        'text': current_chunk.strip(),
                        'metadata': chunk_metadata
                    })

                    # Overlap: garder les derniers chunk_overlap caractères
                    overlap_text = current_chunk[-self.chunk_overlap:] if len(current_chunk) > self.chunk_overlap else current_chunk
                    current_chunk = overlap_text + self.separator + para
                    chunk_index += 1
                else:
                    current_chunk = para
            else:
                current_chunk += self.separator + para if current_chunk else para

        # Dernier chunk
        if current_chunk:
            chunk_metadata = metadata.copy() if metadata else {}
            chunk_metadata['chunk_index'] = chunk_index
            chunks.append({
                'text': current_chunk.strip(),
                'metadata': chunk_metadata
            })

        return chunks
```

---

## Structure du Projet

```
voyage-rag/
├── config/
│   └── .env.example          # Template configuration
│
├── data/
│   ├── chromadb/             # Persistance ChromaDB (Docker volume)
│   └── corpus/               # Documents à indexer
│
├── docs/
│   ├── PLAN-FINAL-VOYAGE-RAG.md
│   ├── SESSION-PROMPT.md
│   └── ANTIDRIFT-CHECKLIST.md
│
├── src/
│   └── voyage_rag/
│       ├── __init__.py
│       │
│       ├── core/
│       │   ├── __init__.py
│       │   ├── config.py         # Pydantic Settings
│       │   ├── models.py         # Document, SearchResult
│       │   └── exceptions.py     # Custom exceptions
│       │
│       ├── indexing/
│       │   ├── __init__.py
│       │   ├── voyage_client.py  # VoyageEmbedder
│       │   ├── chunker.py        # DocumentChunker
│       │   └── indexer.py        # ChromaIndexer
│       │
│       ├── search/
│       │   ├── __init__.py
│       │   ├── retriever.py      # ChromaRetriever
│       │   └── reranker.py       # VoyageReranker
│       │
│       ├── api/
│       │   ├── __init__.py
│       │   ├── main.py           # FastAPI app
│       │   ├── routes.py         # Endpoints
│       │   ├── auth.py           # JWT
│       │   └── dependencies.py   # DI
│       │
│       └── utils/
│           ├── __init__.py
│           ├── monitoring.py
│           └── logger.py
│
├── scripts/
│   ├── index_documents.py    # Script d'indexation batch
│   └── test_search.py        # Tests manuels
│
├── tests/
│   ├── test_voyage_client.py
│   ├── test_chunker.py
│   ├── test_indexer.py
│   ├── test_retriever.py
│   └── test_api.py
│
├── .env                      # Config locale (gitignored)
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── CLAUDE.md
└── README.md
```

---

## Implémentation par Module

### Phase 1: Core Foundation

**Fichiers à créer:**
1. `src/voyage_rag/core/config.py`
2. `src/voyage_rag/core/models.py`
3. `src/voyage_rag/core/exceptions.py`

### Phase 2: Indexing Pipeline

**Fichiers à créer:**
1. `src/voyage_rag/indexing/voyage_client.py` (VoyageEmbedder)
2. `src/voyage_rag/indexing/chunker.py` (DocumentChunker)
3. `src/voyage_rag/indexing/indexer.py` (ChromaIndexer)

### Phase 3: Search Pipeline

**Fichiers à créer:**
1. `src/voyage_rag/search/retriever.py` (ChromaRetriever)
2. `src/voyage_rag/search/reranker.py` (VoyageReranker)

### Phase 4: API Layer

**Fichiers à créer:**
1. `src/voyage_rag/api/main.py` (FastAPI app)
2. `src/voyage_rag/api/routes.py` (Endpoints)
3. `src/voyage_rag/api/auth.py` (JWT validation)
4. `src/voyage_rag/api/dependencies.py` (DI)

### Phase 5: Docker & Deployment

**Fichiers à créer:**
1. `docker-compose.yml`
2. `Dockerfile`
3. `config/.env.example`

### Phase 6: Scripts & Tests

**Fichiers à créer:**
1. `scripts/index_documents.py`
2. `tests/test_*.py`

---

## Configuration Docker

### docker-compose.yml

(Voir section 2 - ChromaDB Setup)

### Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source
COPY src/ ./src/
COPY config/ ./config/

# Expose port
EXPOSE 8001

# Run API
CMD ["uvicorn", "src.voyage_rag.api.main:app", "--host", "0.0.0.0", "--port", "8001"]
```

### Variables d'Environnement (.env.example)

```bash
# Voyage AI
VOYAGE_API_KEY=vo-your-key-here
VOYAGE_MODEL_EMBED=voyage-3-lite
VOYAGE_MODEL_RERANK=rerank-1
VOYAGE_BATCH_SIZE=128

# ChromaDB
CHROMA_HOST=localhost
CHROMA_PORT=8000
CHROMA_COLLECTION=voyage_documents

# API
API_KEYS=secret-key-1,secret-key-2
RATE_LIMIT_REQUESTS=100
RATE_LIMIT_WINDOW=60

# Chunking
CHUNK_SIZE=1000
CHUNK_OVERLAP=200

# Logging
LOG_LEVEL=INFO
```

---

## Workflow de Développement

### 1. Setup Initial

```bash
# Clone repo
git checkout -b claude/orchestrator-setup-011CV2HisXFkuoZvBnk1ppJ1

# Setup env
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Configure
cp config/.env.example config/.env
# Éditer .env avec vos clés
```

### 2. Démarrer ChromaDB

```bash
docker-compose up -d chromadb
docker-compose logs -f chromadb
# Attendre: "Application startup complete"
```

### 3. Développement Itératif

Suivre les phases 1-6 dans l'ordre:
1. Core → 2. Indexing → 3. Search → 4. API → 5. Docker → 6. Scripts

**Commit atomique après chaque module complet.**

### 4. Tests

```bash
# Test unitaires
pytest tests/ -v

# Test d'indexation
python scripts/index_documents.py --test

# Test recherche
curl -X POST http://localhost:8001/search \
  -H "Authorization: Bearer YOUR_KEY" \
  -d '{"query": "test", "top_k": 5}'
```

---

## Monitoring et Coûts

### Estimation Coûts Voyage AI

**Pricing (après free tier 100M tokens):**
- voyage-3: ~$0.12/1M tokens
- voyage-3-lite: ~$0.06/1M tokens
- rerank-1: ~$0.02/1M tokens

**Calcul pour 10k documents:**
- Embeddings: 10k docs × 750 tokens/doc × $0.06/1M = **$0.45**
- Rerank: 1000 queries × 10 docs × 200 tokens × $0.02/1M = **$0.04**
- **Total: ~$0.50 pour 10k docs + 1k queries**

### Tracking Usage

```python
# utils/monitoring.py
class CostMonitor:
    def __init__(self):
        self.embed_tokens = 0
        self.rerank_tokens = 0

    def log_embed(self, tokens: int):
        self.embed_tokens += tokens

    def log_rerank(self, tokens: int):
        self.rerank_tokens += tokens

    def estimate_cost(self) -> float:
        embed_cost = (self.embed_tokens / 1_000_000) * 0.06
        rerank_cost = (self.rerank_tokens / 1_000_000) * 0.02
        return embed_cost + rerank_cost
```

---

## Références

- **Voyage AI Docs**: https://docs.voyageai.com
- **ChromaDB Docs**: https://docs.trychroma.com
- **FastAPI Docs**: https://fastapi.tiangolo.com
- **MTEB Leaderboard**: https://huggingface.co/spaces/mteb/leaderboard

---

**Note**: Ce plan est la source de vérité absolue pour l'implémentation. Toute déviation doit être validée et documentée.
