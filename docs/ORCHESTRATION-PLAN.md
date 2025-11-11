# PLAN D'ORCHESTRATION - Voyage RAG

**Date de création:** 2025-11-11
**Orchestrateur:** Claude (Mode Ultra-Think)
**Architecture validée:** Voyage AI + ChromaDB + Rerank + FastAPI

---

## 📋 Table des Matières

1. [Vue d'ensemble](#vue-densemble)
2. [DAG des Dépendances](#dag-des-dépendances)
3. [Vagues de Parallélisation](#vagues-de-parallélisation)
4. [Prompts pour Agents](#prompts-pour-agents)
5. [Critères de Validation](#critères-de-validation)
6. [Checkpoints de Synchronisation](#checkpoints-de-synchronisation)

---

## Vue d'ensemble

### Objectif

Orchestrer le développement complet du projet Voyage RAG en utilisant **plusieurs agents Claude Code en parallèle** pour maximiser l'efficacité tout en maintenant la qualité et la conformité au plan.

### Principes d'Orchestration

1. **Parallélisation naturelle** - Agents travaillent simultanément sur modules indépendants
2. **Dépendances strictes** - Respect du flow unidirectionnel (core → indexing → search → api)
3. **Validation continue** - Checkpoints entre chaque vague
4. **Conformité absolue** - Tous les agents suivent PLAN-FINAL + ANTIDRIFT
5. **Commits atomiques** - Un module = un commit par agent

### Statistiques du Projet

```
Total de modules: 17 fichiers Python
Total de phases: 6 vagues
Agents maximum en parallèle: 3
Durée estimée (séquentiel): 8-10h
Durée estimée (parallèle): 4-5h
```

---

## DAG des Dépendances

### Graphe Complet

```
[VAGUE 1] Setup & Core (3 modules en parallèle)
    │
    ├─── config.py ────┐
    ├─── models.py ────┤
    └─── exceptions.py ┘
            │
            ▼
[VAGUE 2] Indexing Pipeline (3 modules en parallèle)
    │
    ├─── voyage_client.py ────┐ (dépend: config, models, exceptions)
    ├─── chunker.py ───────────┤ (dépend: models)
    └─── indexer.py ───────────┘ (dépend: voyage_client, models, exceptions)
            │
            ▼
[VAGUE 3] Search Pipeline (2 modules en parallèle)
    │
    ├─── retriever.py ────┐ (dépend: config, models, indexer)
    └─── reranker.py ─────┘ (dépend: config, models, voyage_client)
            │
            ▼
[VAGUE 4] API Layer (4 modules, 2 en parallèle puis 2 autres)
    │
    ├─── auth.py ─────────┬──┐
    ├─── dependencies.py ─┘  │ (dépend: config, exceptions)
    │                        │
    └──────────▼─────────────┘
       ├─── main.py ─────┐ (dépend: auth, dependencies, tous les modules)
       └─── routes.py ───┘ (dépend: main, retriever, reranker, indexer)
            │
            ▼
[VAGUE 5] Docker & Config (3 fichiers en parallèle)
    │
    ├─── docker-compose.yml ────┐
    ├─── Dockerfile ────────────┤
    └─── .env.example ──────────┘
            │
            ▼
[VAGUE 6] Scripts & Utils (3 fichiers en parallèle)
    │
    ├─── scripts/index_documents.py ────┐
    ├─── utils/monitoring.py ───────────┤
    └─── utils/logger.py ───────────────┘
```

### Légende

- **Modules en parallèle**: Peuvent être développés simultanément (pas de dépendances entre eux)
- **Vagues séquentielles**: La vague N+1 démarre uniquement quand vague N est 100% complétée et validée

---

## Vagues de Parallélisation

### Vague 1: Core Foundation (3 agents en parallèle)

**Durée estimée:** 30-45 minutes
**Bloquants:** Aucun (point de départ)
**Validation requise:** Tests unitaires + import des 3 modules réussissent

| Agent | Module | Dépendances | Complexité |
|-------|--------|-------------|------------|
| Agent-1A | `core/config.py` | Aucune | Simple |
| Agent-1B | `core/models.py` | Aucune | Simple |
| Agent-1C | `core/exceptions.py` | Aucune | Simple |

**Outputs attendus:**
- Pydantic Settings avec toutes les env vars
- Dataclasses Document et SearchResult
- Hiérarchie d'exceptions personnalisées

---

### Vague 2: Indexing Pipeline (3 agents en parallèle)

**Durée estimée:** 60-90 minutes
**Bloquants:** Vague 1 complétée
**Validation requise:** Tests unitaires + indexation d'un doc de test réussit

| Agent | Module | Dépendances | Complexité |
|-------|--------|-------------|------------|
| Agent-2A | `indexing/voyage_client.py` | config, models, exceptions | Complexe |
| Agent-2B | `indexing/chunker.py` | models | Moyen |
| Agent-2C | `indexing/indexer.py` | voyage_client, models, config | Complexe |

**Outputs attendus:**
- VoyageEmbedder avec batching + retry
- DocumentChunker avec overlap
- ChromaIndexer avec connexion HTTP ChromaDB

**Note critique:** Agent-2C doit attendre que ChromaDB soit démarré (`docker-compose up -d chromadb`). Prévoir 2 min d'attente ou intégration dans le prompt.

---

### Vague 3: Search Pipeline (2 agents en parallèle)

**Durée estimée:** 45-60 minutes
**Bloquants:** Vague 2 complétée
**Validation requise:** Recherche sur index de test retourne résultats

| Agent | Module | Dépendances | Complexité |
|-------|--------|-------------|------------|
| Agent-3A | `search/retriever.py` | config, models, indexer | Moyen |
| Agent-3B | `search/reranker.py` | config, models, voyage_client | Moyen |

**Outputs attendus:**
- ChromaRetriever avec filtrage metadata
- VoyageReranker avec API rerank
- RAGPipeline complet (embed → retrieve → rerank)

---

### Vague 4: API Layer (2 + 2 agents, séquentiel interne)

**Durée estimée:** 60-90 minutes
**Bloquants:** Vague 3 complétée
**Validation requise:** API démarre, health check répond 200, endpoint search fonctionne

#### Sous-vague 4a (2 agents en parallèle)

| Agent | Module | Dépendances | Complexité |
|-------|--------|-------------|------------|
| Agent-4A | `api/auth.py` | config, exceptions | Simple |
| Agent-4B | `api/dependencies.py` | config, exceptions, tous indexing/search | Moyen |

#### Sous-vague 4b (2 agents en parallèle, après 4a)

| Agent | Module | Dépendances | Complexité |
|-------|--------|-------------|------------|
| Agent-4C | `api/main.py` | auth, dependencies | Moyen |
| Agent-4D | `api/routes.py` | main, retriever, reranker, indexer | Complexe |

**Outputs attendus:**
- JWT validation fonctionnelle
- Dependency injection setup
- FastAPI app avec CORS et lifespan
- Endpoints /health, /search, /index

---

### Vague 5: Docker & Config (3 agents en parallèle)

**Durée estimée:** 30-45 minutes
**Bloquants:** Vague 4 complétée
**Validation requise:** `docker-compose up -d` démarre sans erreur

| Agent | Module | Dépendances | Complexité |
|-------|--------|-------------|------------|
| Agent-5A | `docker-compose.yml` | Aucune (config) | Simple |
| Agent-5B | `Dockerfile` | requirements.txt | Simple |
| Agent-5C | `config/.env.example` | config.py | Simple |

**Outputs attendus:**
- docker-compose.yml avec chromadb + api services
- Dockerfile multi-stage
- .env.example avec toutes les variables documentées

---

### Vague 6: Scripts & Utils (3 agents en parallèle)

**Durée estimée:** 45-60 minutes
**Bloquants:** Vague 5 complétée
**Validation requise:** Script d'indexation fonctionne, monitoring log des coûts

| Agent | Module | Dépendances | Complexité |
|-------|--------|-------------|------------|
| Agent-6A | `scripts/index_documents.py` | tous modules indexing | Moyen |
| Agent-6B | `utils/monitoring.py` | models | Simple |
| Agent-6C | `utils/logger.py` | config | Simple |

**Outputs attendus:**
- Script d'indexation batch avec argparse
- CostMonitor pour tracking tokens
- Logger structuré avec rotation

---

## Prompts pour Agents

### Template Général pour Tous les Agents

```markdown
# MISSION AGENT [ID]

**Module assigné:** [chemin/vers/fichier.py]
**Vague:** [N]
**Dépendances:** [liste des modules requis]

---

## CONTEXTE PROJET

Tu travailles sur **Voyage RAG**, un système RAG production-ready avec:
- Voyage AI embeddings + rerank
- ChromaDB vector database
- FastAPI REST API

**Architecture validée:**
`core` ← `indexing` ← `search` ← `api`

---

## DOCUMENTS DE RÉFÉRENCE OBLIGATOIRES

**LIS CES DOCUMENTS AVANT TOUTE ACTION:**

1. `/home/user/voyage-rag/docs/PLAN-FINAL-VOYAGE-RAG.md`
   - Section concernée: [Section spécifique pour ce module]

2. `/home/user/voyage-rag/docs/ANTIDRIFT-CHECKLIST.md`
   - Items concernés: [Items spécifiques]

3. `/home/user/voyage-rag/docs/SESSION-PROMPT.md`
   - **CRITIQUE:** Définit comment tu dois fonctionner

---

## TON RÔLE

Tu es un **exécuteur déterministe**, pas un co-créateur.

**Tu DOIS:**
- ✅ Suivre PLAN-FINAL à la lettre (section [X])
- ✅ Implémenter exactement ce qui est spécifié
- ✅ Faire un commit atomique à la fin
- ✅ Cocher l'item ANTIDRIFT correspondant
- ✅ Valider ton code avec tests basiques

**Tu NE DOIS PAS:**
- ❌ Ajouter des features bonus non demandées
- ❌ "Améliorer" le code du plan
- ❌ Modifier d'autres fichiers que ton module
- ❌ Sauter les tests

---

## SPÉCIFICATIONS MODULE

### Fichier à créer
`[chemin complet]`

### Dépendances Python
```python
# Imports requis (d'après PLAN-FINAL)
[liste imports]
```

### Dépendances internes
- [module1] (doit exister avant)
- [module2] (doit exister avant)

### Implémentation requise

**Référence:** PLAN-FINAL section [X], lignes [Y-Z]

[Copier-coller la classe/fonction exacte du PLAN-FINAL]

### Tests de validation

Après implémentation, tu DOIS tester:

```python
# Test basique à exécuter
[code de test minimal]
```

**Résultat attendu:** [description]

---

## WORKFLOW D'EXÉCUTION

### Étape 1: Lecture et compréhension (5 min)
1. Lire PLAN-FINAL section concernée
2. Lire ANTIDRIFT items concernés
3. Vérifier que dépendances existent (imports)

### Étape 2: Implémentation (20-40 min)
1. Créer le fichier avec structure exacte du PLAN
2. Implémenter sans ajouter de features
3. Documenter avec docstrings

### Étape 3: Validation (5-10 min)
1. Exécuter test basique
2. Vérifier imports fonctionnent
3. Corriger erreurs si nécessaires

### Étape 4: Commit (2 min)
1. Commit atomique avec message standard
2. Format: `[TYPE] Description`
3. Référencer item ANTIDRIFT dans message

### Étape 5: Checklist (1 min)
1. Cocher item ANTIDRIFT correspondant
2. Commit séparé de la checklist

---

## FORMAT DE COMMIT ATTENDU

```
[feat] Implement [nom module]

Module: [chemin/fichier.py]
Implements: [description concise]

Key features:
- [feature 1]
- [feature 2]

Tests: [Basic tests passed]
ANTIDRIFT: [Phase X - Item Y] completed
```

---

## CRITÈRES DE SUCCÈS

Ton travail est **complété et validé** SI ET SEULEMENT SI:

- ✅ Fichier créé au bon emplacement
- ✅ Code conforme à PLAN-FINAL (pas de déviation)
- ✅ Tous les imports fonctionnent
- ✅ Test basique passe (pas d'erreur)
- ✅ Docstrings présents
- ✅ Commit atomique effectué
- ✅ Item ANTIDRIFT coché

---

## EN CAS DE PROBLÈME

**Si tu rencontres un blocage:**

1. **Dépendance manquante** → STOP et signale à l'orchestrateur
2. **Code du plan ne fonctionne pas** → Signale l'erreur exacte
3. **Ambiguïté dans le plan** → Pose une question précise
4. **Test échoue** → Debug et corrige AVANT commit

**NE JAMAIS:**
- Improviser une solution
- Sauter le test
- Commiter du code non fonctionnel
- Modifier d'autres fichiers pour "arranger"

---

## DÉMARRAGE

Confirme la lecture de ce prompt en répondant:

```
AGENT [ID] - CONFIRMATION

✅ Documents lus: PLAN-FINAL, ANTIDRIFT, SESSION-PROMPT
✅ Module assigné: [nom]
✅ Dépendances vérifiées: [liste]
✅ Prêt à implémenter selon PLAN-FINAL section [X]

Début de l'implémentation.
```

Puis procède à l'implémentation.
```

---

### Prompts Spécifiques par Agent

#### Agent-1A: core/config.py

```markdown
# MISSION AGENT 1A

**Module assigné:** `src/voyage_rag/core/config.py`
**Vague:** 1 (Core Foundation)
**Dépendances:** Aucune

---

## SPÉCIFICATIONS MODULE

### Implémentation requise

**Référence:** PLAN-FINAL section "Variables d'Environnement"

Créer une classe `Settings` Pydantic avec toutes les env vars:

```python
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Voyage AI
    voyage_api_key: str
    voyage_model_embed: str = "voyage-3-lite"
    voyage_model_rerank: str = "rerank-1"
    voyage_batch_size: int = 128

    # ChromaDB
    chroma_host: str = "localhost"
    chroma_port: int = 8000
    chroma_collection: str = "voyage_documents"

    # API
    api_keys: str  # Comma-separated
    rate_limit_requests: int = 100
    rate_limit_window: int = 60

    # Chunking
    chunk_size: int = 1000
    chunk_overlap: int = 200

    # Logging
    log_level: str = "INFO"

    class Config:
        env_file = "config/.env"
        case_sensitive = False
```

### Tests de validation

```python
# Test import
from src.voyage_rag.core.config import Settings

# Test instanciation (avec .env)
settings = Settings()
print(f"Voyage API Key: {settings.voyage_api_key[:10]}...")
print(f"ChromaDB: {settings.chroma_host}:{settings.chroma_port}")
```

**Résultat attendu:** Import réussit, Settings instancie sans erreur

---

## COMMIT ATTENDU

```
feat: Implement core configuration with Pydantic Settings

Module: src/voyage_rag/core/config.py
Implements: Settings class for environment variable management

Key features:
- Pydantic BaseSettings for type validation
- All env vars from PLAN-FINAL documented
- Default values for optional settings
- Loads from config/.env automatically

Tests: Basic import and instanciation passed
ANTIDRIFT: [Phase 1 - Core/config.py] completed
```
```

#### Agent-1B: core/models.py

```markdown
# MISSION AGENT 1B

**Module assigné:** `src/voyage_rag/core/models.py`
**Vague:** 1 (Core Foundation)
**Dépendances:** Aucune

---

## SPÉCIFICATIONS MODULE

### Implémentation requise

**Référence:** PLAN-FINAL section "Structure du Projet"

Créer les dataclasses:

```python
from dataclasses import dataclass, field
from typing import Dict, List, Optional

@dataclass
class Document:
    """Représente un document à indexer."""
    text: str
    metadata: Dict[str, any] = field(default_factory=dict)
    id: Optional[str] = None

@dataclass
class SearchResult:
    """Résultat de recherche."""
    document: str
    metadata: Dict[str, any]
    score: float
    id: str
    relevance_score: Optional[float] = None  # Pour rerank
```

### Tests de validation

```python
from src.voyage_rag.core.models import Document, SearchResult

# Test Document
doc = Document(
    text="Test document",
    metadata={"source": "test"}
)
print(f"Document: {doc.text}, metadata: {doc.metadata}")

# Test SearchResult
result = SearchResult(
    document="Result text",
    metadata={"category": "tech"},
    score=0.95,
    id="abc123"
)
print(f"Result score: {result.score}")
```

**Résultat attendu:** Dataclasses instancient correctement

---

## COMMIT ATTENDU

```
feat: Implement core data models with dataclasses

Module: src/voyage_rag/core/models.py
Implements: Document and SearchResult dataclasses

Key features:
- Document model with text, metadata, optional id
- SearchResult model with score and optional relevance_score
- Type hints for all fields
- Default factories for mutable defaults

Tests: Basic instanciation tests passed
ANTIDRIFT: [Phase 1 - Core/models.py] completed
```
```

#### Agent-1C: core/exceptions.py

```markdown
# MISSION AGENT 1C

**Module assigné:** `src/voyage_rag/core/exceptions.py`
**Vague:** 1 (Core Foundation)
**Dépendances:** Aucune

---

## SPÉCIFICATIONS MODULE

### Implémentation requise

**Référence:** ANTIDRIFT section "6 Erreurs Critiques"

Créer hiérarchie d'exceptions:

```python
class VoyageRAGError(Exception):
    """Exception de base pour Voyage RAG."""
    pass

class ConfigurationError(VoyageRAGError):
    """Erreur de configuration (env vars manquantes, etc.)."""
    pass

class IndexingError(VoyageRAGError):
    """Erreur pendant l'indexation (embedding, ChromaDB, etc.)."""
    pass

class SearchError(VoyageRAGError):
    """Erreur pendant la recherche (retrieval, rerank, etc.)."""
    pass

class AuthenticationError(VoyageRAGError):
    """Erreur d'authentification API."""
    pass

class RateLimitError(VoyageRAGError):
    """Erreur de rate limiting (429)."""
    pass
```

### Tests de validation

```python
from src.voyage_rag.core.exceptions import *

# Test inheritance
try:
    raise IndexingError("Test error")
except VoyageRAGError as e:
    print(f"Caught base exception: {e}")

# Test all exceptions
for exc_class in [ConfigurationError, IndexingError, SearchError, AuthenticationError, RateLimitError]:
    try:
        raise exc_class(f"Test {exc_class.__name__}")
    except VoyageRAGError:
        print(f"{exc_class.__name__} OK")
```

**Résultat attendu:** Toutes les exceptions héritent correctement

---

## COMMIT ATTENDU

```
feat: Implement custom exceptions hierarchy

Module: src/voyage_rag/core/exceptions.py
Implements: VoyageRAGError base class and specific exceptions

Key features:
- Base VoyageRAGError for all project exceptions
- ConfigurationError, IndexingError, SearchError
- AuthenticationError, RateLimitError
- Clear error types for specific HTTP status codes

Tests: Inheritance and exception raising verified
ANTIDRIFT: [Phase 1 - Core/exceptions.py] completed
```
```

---

## Critères de Validation

### Validation par Vague

#### Vague 1: Core Foundation

**Checklist de validation:**

- [ ] `config.py` créé et importable
- [ ] `Settings()` instancie avec .env
- [ ] `models.py` créé et importable
- [ ] `Document` et `SearchResult` instanciables
- [ ] `exceptions.py` créé et importable
- [ ] Toutes les exceptions héritent de `VoyageRAGError`
- [ ] 3 commits atomiques effectués
- [ ] 3 items ANTIDRIFT cochés

**Test d'intégration Vague 1:**

```python
# Test que tout fonctionne ensemble
from src.voyage_rag.core.config import Settings
from src.voyage_rag.core.models import Document, SearchResult
from src.voyage_rag.core.exceptions import VoyageRAGError, IndexingError

settings = Settings()
doc = Document(text="test", metadata={"source": "test"})
result = SearchResult(document="test", metadata={}, score=0.9, id="1")

try:
    raise IndexingError("Test")
except VoyageRAGError:
    pass

print("✅ Vague 1 validation passed")
```

---

#### Vague 2: Indexing Pipeline

**Checklist de validation:**

- [ ] `voyage_client.py` créé avec VoyageEmbedder class
- [ ] Batching fonctionne (128 docs max)
- [ ] Retry avec backoff exponentiel implémenté
- [ ] `chunker.py` créé avec DocumentChunker class
- [ ] Overlap préserve contexte (200 chars min)
- [ ] `indexer.py` créé avec ChromaIndexer class
- [ ] Connexion HTTP ChromaDB fonctionne
- [ ] 3 commits atomiques effectués
- [ ] 3 items ANTIDRIFT cochés

**Test d'intégration Vague 2:**

```python
# Requis: ChromaDB running sur localhost:8000
from src.voyage_rag.indexing.voyage_client import VoyageEmbedder
from src.voyage_rag.indexing.chunker import DocumentChunker
from src.voyage_rag.indexing.indexer import ChromaIndexer

embedder = VoyageEmbedder(api_key="vo-xxx", model="voyage-3-lite")
chunker = DocumentChunker(chunk_size=1000, chunk_overlap=200)
indexer = ChromaIndexer(host="localhost", port=8000)

# Test chunking
chunks = chunker.chunk_text("Long text..." * 100, metadata={"source": "test"})
assert len(chunks) > 1

# Test embedding (avec vraie API key)
# embeddings = embedder.embed_documents([c['text'] for c in chunks])

# Test indexing (avec ChromaDB running)
# indexer.add_documents(...)

print("✅ Vague 2 validation passed")
```

---

#### Vague 3: Search Pipeline

**Checklist de validation:**

- [ ] `retriever.py` créé avec ChromaRetriever class
- [ ] Filtrage metadata fonctionne (where clause)
- [ ] `reranker.py` créé avec VoyageReranker class
- [ ] RAGPipeline complet fonctionnel
- [ ] 2 commits atomiques effectués
- [ ] 2 items ANTIDRIFT cochés

**Test d'intégration Vague 3:**

```python
from src.voyage_rag.search.retriever import ChromaRetriever
from src.voyage_rag.search.reranker import VoyageReranker, RAGPipeline
from src.voyage_rag.indexing.voyage_client import VoyageEmbedder

embedder = VoyageEmbedder(api_key="vo-xxx")
retriever = ChromaRetriever(host="localhost", port=8000)
reranker = VoyageReranker(api_key="vo-xxx")

pipeline = RAGPipeline(embedder, retriever, reranker)

# Test search (avec index existant)
# results = pipeline.search("test query", top_k=5, use_rerank=True)

print("✅ Vague 3 validation passed")
```

---

#### Vague 4: API Layer

**Checklist de validation:**

- [ ] `auth.py` créé avec JWT validation
- [ ] `dependencies.py` créé avec DI functions
- [ ] `main.py` créé avec FastAPI app
- [ ] `routes.py` créé avec endpoints
- [ ] `GET /health` retourne 200
- [ ] `POST /search` fonctionne avec auth
- [ ] 4 commits atomiques effectués
- [ ] 4 items ANTIDRIFT cochés

**Test d'intégration Vague 4:**

```bash
# Démarrer API
uvicorn src.voyage_rag.api.main:app --reload --port 8001

# Test health
curl http://localhost:8001/health
# Attendu: {"status": "healthy"}

# Test search
curl -X POST http://localhost:8001/search \
  -H "Authorization: Bearer test-key" \
  -H "Content-Type: application/json" \
  -d '{"query": "test", "top_k": 5}'
# Attendu: 200 avec résultats JSON

echo "✅ Vague 4 validation passed"
```

---

#### Vague 5: Docker & Config

**Checklist de validation:**

- [ ] `docker-compose.yml` créé
- [ ] `Dockerfile` créé
- [ ] `.env.example` créé
- [ ] `docker-compose up -d` démarre sans erreur
- [ ] ChromaDB health check passe
- [ ] API démarre après ChromaDB
- [ ] 3 commits atomiques effectués
- [ ] 3 items ANTIDRIFT cochés

**Test d'intégration Vague 5:**

```bash
# Build et start
docker-compose up -d --build

# Vérifier status
docker-compose ps
# Attendu: chromadb (healthy), api (running)

# Test ChromaDB
curl http://localhost:8000/api/v1/heartbeat
# Attendu: heartbeat response

# Test API via Docker
curl http://localhost:8001/health
# Attendu: {"status": "healthy"}

docker-compose down

echo "✅ Vague 5 validation passed"
```

---

#### Vague 6: Scripts & Utils

**Checklist de validation:**

- [ ] `scripts/index_documents.py` créé
- [ ] Script peut indexer documents depuis CLI
- [ ] `utils/monitoring.py` créé avec CostMonitor
- [ ] `utils/logger.py` créé avec structured logging
- [ ] 3 commits atomiques effectués
- [ ] 3 items ANTIDRIFT cochés

**Test d'intégration Vague 6:**

```bash
# Test indexation script
python scripts/index_documents.py --model voyage-3-lite --test
# Attendu: Indexation de docs de test réussie

# Test monitoring
python -c "
from src.voyage_rag.utils.monitoring import CostMonitor
monitor = CostMonitor()
monitor.log_embed(1000000)
print(f'Cost: ${monitor.estimate_cost()}')
"
# Attendu: Cost calculé correctement

# Test logger
python -c "
from src.voyage_rag.utils.logger import get_logger
logger = get_logger('test')
logger.info('Test log')
"
# Attendu: Log affiché avec format structuré

echo "✅ Vague 6 validation passed"
```

---

## Checkpoints de Synchronisation

### Checkpoint après chaque Vague

**Protocole:**

1. **Tous les agents de la vague terminent**
2. **L'orchestrateur (toi) valide:**
   - Tous les commits sont présents
   - Tous les items ANTIDRIFT sont cochés
   - Test d'intégration de la vague passe
3. **Si validation OK** → Lancer vague suivante
4. **Si validation FAIL** → Identifier agent/module problématique, corriger, re-valider

### Format de Rapport de Vague

```markdown
## RAPPORT VAGUE [N]

**Date:** [timestamp]
**Agents:** [liste]
**Durée:** [temps réel]

### Résultats

| Agent | Module | Status | Commit | Tests |
|-------|--------|--------|--------|-------|
| Agent-XA | module1 | ✅ | abc1234 | PASS |
| Agent-XB | module2 | ✅ | def5678 | PASS |
| Agent-XC | module3 | ✅ | ghi9012 | PASS |

### Validation Intégration

```bash
[commandes de test]
```

**Résultat:** ✅ PASS / ❌ FAIL

### Blockers / Issues

- [Aucun] / [Liste des problèmes]

### Prochaine Vague

**Vague [N+1]:** [Description]
**Agents requis:** [Nombre]
**Durée estimée:** [Temps]

---

**Status:** ✅ READY TO PROCEED / ❌ BLOCKED
```

---

## Workflow Global pour l'Orchestrateur

### Phase de Préparation

1. **Setup environnement:**
   ```bash
   # Créer .env depuis .env.example
   cp config/.env.example config/.env
   # Éditer avec vraies clés API

   # Démarrer ChromaDB
   docker-compose up -d chromadb
   ```

2. **Créer branches pour chaque agent:**
   ```bash
   git checkout -b agent-1a-core-config
   git checkout -b agent-1b-core-models
   git checkout -b agent-1c-core-exceptions
   # etc.
   ```

   **Ou:** Tous les agents travaillent sur la même branche `claude/orchestrator-setup-*` mais commits atomiques séparés.

### Phase d'Exécution

**Pour chaque vague:**

1. **Lancer agents en parallèle** (une session Claude Code par agent)
2. **Copier-coller le prompt correspondant** dans chaque session
3. **Attendre que tous les agents terminent**
4. **Valider les outputs:**
   - Lire les commits
   - Exécuter test d'intégration
   - Vérifier ANTIDRIFT checklist
5. **Si OK → Vague suivante**
6. **Si KO → Debug et correction**

### Phase de Finalisation

1. **Tous modules complétés et validés**
2. **Exécuter test end-to-end complet:**
   ```bash
   # Test complet du système
   docker-compose up -d
   python scripts/index_documents.py --test
   curl -X POST http://localhost:8001/search \
     -H "Authorization: Bearer test-key" \
     -d '{"query": "semantic search", "top_k": 5}'
   docker-compose down
   ```

3. **Si test E2E passe → Projet terminé!**
4. **Push final:**
   ```bash
   git push -u origin claude/orchestrator-setup-011CV2HisXFkuoZvBnk1ppJ1
   ```

---

## Métriques de Suivi

### Par Vague

- Durée réelle vs estimée
- Nombre de commits
- Nombre d'erreurs/corrections
- Temps de validation

### Global

- Durée totale du projet
- Nombre total de commits
- Lignes de code produites
- Taux de conformité ANTIDRIFT (items cochés / total)
- Taux de réussite des tests

---

## Conclusion

Ce plan d'orchestration permet de:

✅ **Maximiser la parallélisation** (3 agents max simultanés)
✅ **Respecter les dépendances** (DAG strict)
✅ **Maintenir la qualité** (validation continue)
✅ **Assurer la conformité** (prompts détaillés + ANTIDRIFT)
✅ **Faciliter le debug** (commits atomiques + checkpoints)

**Durée estimée totale:** 4-5 heures (vs 8-10h séquentiel)

**Prêt à lancer Vague 1?**
