# Golden Tests - Voyage AI Semantic Granularity Evaluation

## Objectif

Évaluer la granularité sémantique de Voyage-3 et Voyage-3-lite sur des cas d'usage pertinents au projet RAG.

## Structure

```
tests/golden/
├── datasets/
│   ├── ordinal_hierarchy.json      # Documents avec labels hiérarchiques
│   ├── queries.json                 # Requêtes de test
│   └── ground_truth.json            # Résultats attendus (ranked lists)
│
├── test_semantic_granularity.py     # Test principal de granularité
├── test_robustness_simple.py        # Tests de robustesse (typos, FR/EN)
├── metrics.py                        # Métriques d'évaluation
├── generate_simple_dataset.py       # Générateur de dataset contrôlé
└── README.md                         # Cette documentation
```

## Tests Implémentés

### 1. Granularité Ordinale (Core)
- **Dataset**: 20-30 docs techniques avec scores numériques explicites
- **Labels**: TOP (≥80), TOP-MID (75-79), MID (65-74), MID-LOW (60-64), LOW (<60)
- **Question**: Voyage peut-il distinguer des écarts fins (ex: 85 vs 83) ?
- **Métrique**: Kendall's Tau, nDCG@k, marges cosinus

### 2. Comparatifs/Superlatifs
- **Queries**: "meilleur", "top", "premium", "SOTA" vs "balanced", "milieu de gamme" vs "budget", "entry-level"
- **Question**: Voyage encode-t-il nativement la hiérarchie sémantique ?

### 3. Robustesse Minimale
- Typos simples
- Code-switching FR/EN
- Impact sur le ranking

### 4. Calibration des Seuils
- **Mesure**: Marge cosinus entre rang #1 et #2
- **Question**: Quel seuil minimum pour faire confiance au top-1 ?

## Métriques Utilisées

- **nDCG@k** (Normalized Discounted Cumulative Gain): Qualité du ranking avec pondération par position
- **MRR** (Mean Reciprocal Rank): Position du premier résultat pertinent
- **Kendall's Tau**: Corrélation de rang entre prédiction et ground truth
- **Marges cosinus**: sim(rank_1) - sim(rank_2) pour mesurer la confiance

## Utilisation

```bash
# Générer le dataset de test
python tests/golden/generate_simple_dataset.py

# Exécuter les tests de granularité
python tests/golden/test_semantic_granularity.py

# Exécuter les tests de robustesse
python tests/golden/test_robustness_simple.py
```

## Dépendances

- `voyageai` - Embeddings Voyage AI
- `chromadb` - Vector database
- `scipy` - Kendall's Tau, nDCG
- `pandas` - Manipulation de données
- `numpy` - Calculs numériques

## Notes

- Dataset minimal (20-30 docs) pour découvrir les capacités
- Focus sur les cas d'usage pertinents au projet
- Approche itérative: commencer simple, raffiner selon résultats
