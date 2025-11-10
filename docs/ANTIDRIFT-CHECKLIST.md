# ANTIDRIFT-CHECKLIST - Voyage RAG

Checklist de validation pour garantir la conformité avec PLAN-FINAL-VOYAGE-RAG.md

## 6 Erreurs Critiques à Éviter

### 1. Configuration ChromaDB

- ❌ Utiliser ChromaDB persistent local (INTERDIT en production)
- ✅ Client/serveur HTTP obligatoire (localhost:8000)
- ✅ Vérifier variable CHROMA_SERVER_HOST dans .env
- ✅ Conteneur chromadb doit être démarré avant l'API

### 2. Modèle LLM

- ❌ Hardcoder mistral-nemo:latest dans le code
- ✅ Variable d'environnement MODEL_NAME (défaut: mistral-nemo:latest)
- ✅ Configurable via .env
- ✅ Vérifier connexion Ollama (localhost:11434)

### 3. Gestion Erreurs

- ❌ Erreur 500 générique sans contexte
- ✅ Erreurs HTTP spécifiques (400, 404, 503, etc.)
- ✅ Messages d'erreur clairs et actionnables
- ✅ Logs structurés avec timestamps et contextes

### 4. Validation Input

- ❌ Accepter requêtes sans validation
- ✅ Pydantic pour tous les endpoints
- ✅ Validation longueur query (min/max)
- ✅ top_k entre 1 et 100

### 5. Chunks de Texte

- ❌ Size fixe sans overlap
- ✅ chunk_size=1000 configurable
- ✅ chunk_overlap=200 minimum
- ✅ Préservation contexte sémantique

### 6. Architecture

- ❌ Code monolithique dans main.py
- ✅ Séparation core/indexing/search/api
- ✅ Dépendances unidirectionnelles
- ✅ Injection de dépendances pour testabilité

## Checklist Implémentation par Module

### Core (core/)

**config.py:**
- [ ] Classe Settings avec pydantic BaseSettings
- [ ] Variables d'environnement documentées avec descriptions
- [ ] Valeurs par défaut sensées
- [ ] Validation des chemins et URLs

**models.py:**
- [ ] Document dataclass avec validation
- [ ] TravelDocument dataclass avec metadata structuré
- [ ] SearchResult avec scores et source
- [ ] Pas de logique métier (pure data)

**exceptions.py:**
- [ ] Hiérarchie d'exceptions personnalisées
- [ ] ConfigurationError, IndexingError, SearchError, LLMError
- [ ] Messages d'erreur explicites
- [ ] Codes HTTP appropriés

### Indexing (indexing/)

**embedder.py:**
- [ ] AbstractEmbedder interface
- [ ] OllamaEmbedder implémentation
- [ ] Gestion timeout et retry
- [ ] Validation dimensions embeddings

**chunker.py:**
- [ ] RecursiveCharacterTextSplitter
- [ ] chunk_size et overlap configurables
- [ ] Préservation metadata dans chunks
- [ ] Tests avec différentes tailles de texte

**indexer.py:**
- [ ] VectorIndexer avec ChromaDB client HTTP
- [ ] Vérification connexion au démarrage
- [ ] Batch processing (pas un par un)
- [ ] Logs progression et erreurs

### Search (search/)

**retriever.py:**
- [ ] VectorRetriever avec validation top_k
- [ ] Logs des requêtes et résultats
- [ ] Gestion collections vides
- [ ] Scores normalisés

**ranker.py:**
- [ ] ReRanker optionnel (peut être désactivé)
- [ ] Stratégies de ranking paramétrables
- [ ] Pas de duplication de documents
- [ ] Conservation métadonnées originales

**generator.py:**
- [ ] RAGGenerator avec prompt engineering
- [ ] Gestion streaming optionnelle
- [ ] Timeout et retry pour LLM
- [ ] Fallback si LLM indisponible

### API (api/)

**main.py:**
- [ ] FastAPI app avec CORS configuré
- [ ] Lifespan events (startup/shutdown)
- [ ] Health check endpoint (/health)
- [ ] Initialisation connexions au démarrage

**routes.py:**
- [ ] POST /index avec validation fichier
- [ ] POST /search avec QueryRequest Pydantic
- [ ] Séparation logique métier (délégation services)
- [ ] Documentation OpenAPI complète

**dependencies.py:**
- [ ] get_settings singleton
- [ ] get_indexer avec lazy init
- [ ] get_rag_pipeline avec lazy init
- [ ] Gestion propre des ressources

### Docker

**docker-compose.yml:**
- [ ] Service chromadb (port 8000)
- [ ] Service voyage-rag-api (port 8001)
- [ ] Networks internes
- [ ] Health checks configurés
- [ ] Depends_on avec conditions

**Dockerfile:**
- [ ] Multi-stage build (builder + runtime)
- [ ] Python 3.11-slim
- [ ] Copie sélective (pas de .venv dans image)
- [ ] User non-root
- [ ] CMD avec uvicorn

## Validation Pré-Déploiement

### Tests Fonctionnels

- [ ] Démarrage conteneurs sans erreur
- [ ] Health check /health retourne 200
- [ ] Indexation document test réussie
- [ ] Recherche retourne résultats pertinents
- [ ] Génération RAG produit réponse cohérente

### Tests d'Erreurs

- [ ] Recherche sans indexation préalable
- [ ] Query trop longue/courte
- [ ] top_k invalide (0, 101, -1)
- [ ] ChromaDB arrêté (503 attendu)
- [ ] Ollama arrêté (503 attendu)

### Configuration

- [ ] Fichier .env.example présent et complet
- [ ] Variables sensibles non commitées
- [ ] README.md avec instructions démarrage
- [ ] Logs configurés (niveau INFO en prod)

### Performance

- [ ] Indexation batch (pas document par document)
- [ ] Timeout raisonnables (30s LLM, 10s embeddings)
- [ ] Pas de chargement complet fichiers en mémoire
- [ ] Connexions réutilisées (pas recréées par requête)

## Signaux de Drift - Comportements à Surveiller

### Drift Architectural

- [ ] Imports croisés entre modules (circular dependencies)
- [ ] Logique métier dans routes.py
- [ ] Configuration hardcodée dans le code
- [ ] Création directe d'objets au lieu d'injection

### Drift Fonctionnel

- [ ] Retour à ChromaDB persistent local
- [ ] Suppression validation Pydantic
- [ ] Erreurs génériques réintroduites
- [ ] Logs debug/print() en production

### Drift Sécurité

- [ ] Credentials en clair dans le code
- [ ] Pas de validation input
- [ ] CORS ouvert à tous (*)
- [ ] Erreurs exposant stack traces complets

### Drift Performance

- [ ] Requêtes synchrones bloquantes sans timeout
- [ ] Chargement complet datasets en RAM
- [ ] Pas de pagination pour gros résultats
- [ ] Connexions non fermées proprement

## Actions Correctives

Si un point n'est pas coché:

1. **Consulter:** PLAN-FINAL-VOYAGE-RAG.md section correspondante
2. **Identifier:** Quelle erreur critique est violée
3. **Corriger:** Implémenter selon le plan
4. **Valider:** Re-tester le point spécifique
5. **Documenter:** Noter la correction dans CHANGELOG.md

## Validation Finale

Tous les points critiques doivent être ✅ avant:
- Merge vers main
- Déploiement production
- Release versionnée

Date dernière validation: _____________

Validé par: _____________
