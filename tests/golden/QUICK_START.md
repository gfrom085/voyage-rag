# QUICK START - Génération du Golden Dataset

> **Guide rapide pour lancer la génération des 34 documents avec l'orchestrateur**

---

## 🚀 Lancement en 3 Étapes

### Étape 1 : Lancer l'Orchestrateur

1. **Ouvrir une nouvelle session Claude Code**
2. **Copier-coller le prompt suivant** :

```
Je veux que tu agisses comme l'orchestrateur du golden dataset pour le projet Voyage RAG.

Lis attentivement le fichier suivant qui définit ton rôle et tes responsabilités :

tests/golden/prompts/ORCHESTRATOR.md

Une fois que tu as bien compris ton rôle, confirme que tu es prêt à coordonner la génération des 34 documents.
```

3. **Attendre confirmation** de l'orchestrateur

---

### Étape 2 : Générer les Documents

**Commande de base** :
```
Donne-moi le prochain document à générer
```

L'orchestrateur vous fournira :
- Le PRIMING.md complet
- Le prompt de tâche spécifique
- Des rappels contextuels

**Workflow par document** :

1. **Copier-coller** PRIMING + prompt dans **une NOUVELLE session CC** (agent générateur)
2. **Récupérer le JSON** produit par l'agent générateur
3. **L'ajouter** à `tests/golden/datasets/ordinal_hierarchy.json`
4. **Revenir à l'orchestrateur** et dire :
   ```
   Marque [ID] comme complété
   ```
5. **(Optionnel)** Faire valider par l'agent validateur
6. **Répéter** pour les 34 documents

---

### Étape 3 : Valider les Documents (Optionnel mais Recommandé)

#### 3.1 Lancer le Validateur

1. **Ouvrir une AUTRE nouvelle session Claude Code** (distincte de l'orchestrateur)
2. **Copier-coller** :

```
Je veux que tu agisses comme le validateur du golden dataset pour le projet Voyage RAG.

Lis attentivement le fichier suivant qui définit ton rôle et critères de validation :

tests/golden/prompts/VALIDATOR.md

Une fois que tu as bien compris ton rôle, confirme que tu es prêt à valider des documents.
```

#### 3.2 Valider un Document

**Fournir au validateur** :

```
Voici le document à valider :

---
PRIMING.md :
[Copier-coller le contenu complet de tests/golden/prompts/PRIMING.md]

---
PROMPT DE TÂCHE :
[Copier-coller le prompt spécifique, ex: PROMPT 1/6 de tier_TOP-MID.md]

---
DOCUMENT GÉNÉRÉ :
[Copier-coller le JSON produit par l'agent générateur]
```

Le validateur produira un **rapport structuré** avec verdict :
- ✅ **ACCEPTÉ** : Document prêt
- ⚠️ **À RÉVISER** : Modifications mineures nécessaires
- ❌ **REJETÉ** : Regénération complète requise

#### 3.3 Mettre à Jour l'Orchestrateur

Si le document est validé :
```
Marque [ID] comme validé
```

---

## 📊 Commandes Orchestrateur Utiles

### Suivi du Progrès
```
Quel est le statut global ?
```

### Statistiques
```
Donne-moi les stats par langue
Donne-moi les stats par type
```

### Rappels
```
Rappelle-moi les bonnes pratiques
```

### Document Spécifique
```
Donne-moi le document TOPMID_1_FR_NUMERIC
```

---

## 🎯 Architecture des Sessions

Vous aurez **3 types de sessions Claude Code** :

### 1. Session Orchestrateur (1 seule, persistante)
- **Rôle** : Coordonner tout le workflow
- **Durée** : Toute la génération des 34 docs
- **Commandes** : "Donne-moi le prochain document", "Marque X comme complété", etc.

### 2. Sessions Générateurs (34 éphémères)
- **Rôle** : Générer UN document
- **Durée** : 5-10 minutes par document
- **Input** : PRIMING.md + prompt spécifique
- **Output** : JSON du document

### 3. Session Validateur (1 seule, persistante)
- **Rôle** : Valider les documents générés
- **Durée** : Parallèle aux générations
- **Input** : PRIMING + prompt + document JSON
- **Output** : Rapport de validation

---

## 📁 Structure des Fichiers

### Prompts (Lecture seule)
```
tests/golden/prompts/
├── PRIMING.md              ⚠️ À fournir à CHAQUE agent générateur
├── ORCHESTRATOR.md         → Pour lancer l'orchestrateur
├── VALIDATOR.md            → Pour lancer le validateur
├── tier_*.md               → Prompts de tâches (8 fichiers)
└── INDEX.md                → Documentation complète
```

### Datasets (À remplir)
```
tests/golden/datasets/
├── ordinal_hierarchy.json  → Ajouter les 34 docs ici
├── queries.json            → Créer après (Phase 2)
└── ground_truth.json       → Créer après (Phase 3)
```

---

## ⏱️ Estimation Temps

| Phase | Tâche | Temps | Cumul |
|-------|-------|-------|-------|
| 1 | Setup orchestrateur | 2 min | 2 min |
| 2 | Générer 34 docs (8 min/doc) | 4-5h | 4-5h |
| 3 | Valider 34 docs (optionnel, 5 min/doc) | 2-3h | 6-8h |
| 4 | Créer queries (Phase 2) | 30 min | 6.5-8.5h |
| 5 | Créer ground truth (Phase 3) | 30 min | 7-9h |

**Total : 7-9 heures** pour un golden dataset complet et validé

---

## 🎯 Checklist de Démarrage

Avant de commencer :

- [ ] J'ai lu `tests/golden/prompts/INDEX.md` (documentation complète)
- [ ] J'ai lu `tests/golden/prompts/PRIMING.md` (pour comprendre le contexte)
- [ ] J'ai créé le fichier `tests/golden/datasets/ordinal_hierarchy.json` avec structure de base
- [ ] Je comprends le workflow : orchestrateur → générateur → validateur
- [ ] J'ai environ 4-6 heures devant moi (ou je peux faire par batches)

### Structure de Base pour ordinal_hierarchy.json

Créez le fichier avec cette structure initiale :

```json
{
  "metadata": {
    "version": "1.0",
    "description": "Documents techniques avec labels hiérarchiques pour tests de granularité sémantique",
    "total_documents": 0,
    "tiers": ["TOP", "TOP-MID", "MID-TOP", "MID", "MID-LOW", "LOW-MID", "LOW", "LEURRES"],
    "score_ranges": {
      "TOP": "≥86",
      "TOP-MID": "78-82",
      "MID-TOP": "72-77",
      "MID": "65-71",
      "MID-LOW": "60-64",
      "LOW-MID": "55-59",
      "LOW": "50-54",
      "LEURRES": "Variable"
    }
  },
  "documents": []
}
```

Après chaque génération, ajoutez le JSON du document dans le tableau `documents`.

---

## 💡 Conseils Pratiques

### 1. Travaillez par Batches

**Recommandé** : Générer 5-6 documents, pause, puis continuer

**Éviter** : Essayer de faire les 34 d'affilée (épuisant)

### 2. Commencez par les Zones Critiques

L'orchestrateur suggère un ordre optimal. Suivez-le pour bien comprendre les nuances avant les cas plus simples.

### 3. Validez Régulièrement

Ne générez pas les 34 puis validez. Validez par batches pour détecter tôt les problèmes récurrents.

### 4. Gardez les Sessions Organisées

- **Nommez vos sessions** (si possible) : "Orchestrateur", "Validateur", "Gen_TOPMID_1", etc.
- **Fermez** les sessions générateurs après récupération du JSON

### 5. Sauvegardez Régulièrement

Après chaque 5 documents, sauvegardez `ordinal_hierarchy.json` (git commit ou backup manuel).

---

## 🆘 Dépannage

### Problème : L'orchestrateur ne fournit pas le PRIMING complet

**Solution** : Demandez explicitement :
```
Donne-moi le prochain document avec le PRIMING.md complet
```

### Problème : Le validateur est trop strict/permissif

**Solution** : Ajustez les seuils dans votre communication avec lui, ou acceptez son verdict (il est calibré pour la rigueur).

### Problème : J'ai perdu la session orchestrateur

**Solution** : Relancez un nouvel orchestrateur et mettez-le à jour manuellement :
```
Voici l'état actuel du projet :
- Complétés : [liste des IDs]
- Validés : [liste des IDs]

Mets à jour ta todo list et donne-moi le prochain document à générer.
```

### Problème : Un document est rejeté après 2 tentatives

**Solution** : Consultez les exemples dans `tier_*.md` pour comprendre le tier, puis regénérez avec plus d'attention aux nuances.

---

## 🎉 Félicitations !

Une fois les 34 documents générés et validés, vous aurez créé un **golden dataset scientifique de référence** !

**Prochaines étapes** :
1. Créer les queries de test (`queries.json`)
2. Définir le ground truth (`ground_truth.json`)
3. Implémenter les tests (`test_semantic_granularity.py`)
4. Exécuter les évaluations sur Voyage-3 et Voyage-3-lite
5. Analyser les résultats et prendre des décisions data-driven

---

**Prêt à commencer ? Lancez l'orchestrateur ! 🚀**
