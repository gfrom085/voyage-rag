# INDEX - Guide d'Utilisation des Prompts

> **Guide complet pour générer les 34 documents du golden dataset**

---

## 📁 Structure des Fichiers

```
prompts/
├── PRIMING.md              # ⚠️ À lire EN PREMIER (contexte universel)
├── LEXICON.md              # 🔴 CRITIQUE - Référence lexicale
├── GENERATOR_AGENT.md      # 🤖 NOUVEAU - Sub-agent de génération autonome
├── ORCHESTRATOR.md         # Agent coordinateur du workflow
├── VALIDATOR.md            # Agent de validation qualité
├── tier_TOP.md             # 4 prompts (scores 86-92)
├── tier_TOP-MID.md         # 6 prompts (scores 78-82) - ZONE CRITIQUE
├── tier_MID-TOP.md         # 6 prompts (scores 72-77) - ZONE CRITIQUE
├── tier_MID.md             # 4 prompts (scores 65-71)
├── tier_MID-LOW.md         # 3 prompts (scores 60-64)
├── tier_LOW-MID.md         # 2 prompts (scores 55-59)
├── tier_LOW.md             # 3 prompts (scores 50-54)
├── tier_LEURRES.md         # 6 prompts (contradictions intentionnelles)
└── INDEX.md                # Ce fichier
```

**Total : 34 prompts de tâches + 1 sub-agent autonome**

### ⚠️ NOUVEAU : LEXICON.md - Référence Lexicale Exhaustive

**Ajouté le 2025-11-13** pour prévenir le drift lexical systématique.

**Contient** :
- Tableau hiérarchique complet TOP → LOW avec TOUS les synonymes
- Mots "signature" identifiant instantanément chaque tier
- Règles de détection du drift (seuils 5%, 10%, 20%)
- Exemples concrets de drift par tier
- Checklist de validation lexicale obligatoire

**Utilisation CRITIQUE** :
- **Générateurs** : Consulter AVANT d'écrire le document
- **Validateur** : Vérifier systématiquement chaque qualificatif clé
- **Drift >10%** : Révision obligatoire du document

**Pourquoi** : Sans référence lexicale centralisée, drift inévitable (ex: "optimale" dans titre TOP-MID, "solide" dans conclusion TOP-MID → incohérences critiques).

### 🤖 NOUVEAU : GENERATOR_AGENT.md - Sub-Agent de Génération Autonome

**Ajouté le 2025-11-13** pour automatiser complètement la génération de documents golden.

**Contient** :
- Workflow complet en 6 phases (hydratation, planification, rédaction, JSON, commit, rapport)
- Protocole anti-drift intégré avec les 5 pauses LEXICON automatiques
- Tolérance ZÉRO pour titre et conclusion (automatiquement appliquée)
- Génération de rapports détaillés avec métriques de qualité
- Validation automatique et création de commits git structurés

**Avantages** :
- ✅ **Génération autonome** : Lit automatiquement PRIMING + LEXICON + tier prompts
- ✅ **Qualité garantie** : Vise <5% drift sur tous les documents
- ✅ **Temps optimisé** : 45-60 min/document (vs manuel)
- ✅ **Cohérence** : Même workflow rigoureux pour chaque document
- ✅ **Traçabilité** : Rapports détaillés avec drift % et vocabulaire utilisé

**Utilisation** :
- **Avec Orchestrator** : `"Utilise le sub-agent pour créer [DOCUMENT_ID]"`
- **Directement** : Charger GENERATOR_AGENT.md puis `"Génère le document golden suivant: ID: ..., Tier: ..."`
- **Via Task tool** : `@task:generator-agent ID: ... Tier: ...`

**Guide complet** : Voir `tests/golden/SUB_AGENT_USAGE_GUIDE.md`

**Résultats attendus** :
- 34 documents en 6-8 heures (vs 15-20h manuel)
- Drift moyen < 3%
- Taux d'acceptation validateur ≥ 95%

---

## 🔄 Workflow Complet

### Étape 1 : Lire PRIMING + LEXICON

**Pour CHAQUE session d'agent CC** :

1. Ouvrir une **nouvelle session Claude Code**
2. Copier-coller **l'intégralité de `PRIMING.md`**
3. Copier-coller **l'intégralité de `LEXICON.md`** ⚠️ **CRITIQUE**
4. Attendre confirmation de lecture par l'agent

**Important** :
- Le PRIMING établit le contexte déterministe complet
- Le LEXICON prévient le drift lexical (référence vocabulaire par tier)
- **Sans LEXICON, drift garanti**

### Étape 2 : Sélectionner un Prompt de Tâche

Choisissez **UN SEUL prompt** parmi les fichiers tier_*.md :

**Exemple pour le prompt TOP_1_FR_CHIFFRES** :
1. Ouvrir `tier_TOP.md`
2. Copier uniquement la section "PROMPT 1/4 : TOP_1_FR_CHIFFRES"

### Étape 3 : Fournir PRIMING + Tâche à l'Agent

Dans la session Claude Code, envoyez :

```
[Contenu complet de PRIMING.md]

---

[Section du prompt spécifique, ex: PROMPT 1/4 : TOP_1_FR_CHIFFRES]
```

### Étape 4 : Récupérer l'Output JSON

L'agent produira un JSON structuré :

```json
{
  "id": "TOP_1_FR_CHIFFRES",
  "title": "...",
  "text": "... (≥ 800 mots)",
  "score": 92,
  "tier": "TOP",
  "self_validation": { ... }
}
```

### Étape 5 : Compiler dans le Dataset

Ajoutez ce JSON au fichier `tests/golden/datasets/ordinal_hierarchy.json` dans le tableau `documents`.

### Étape 6 : Répéter 34 Fois

Répétez les étapes 1-5 pour les **34 prompts** (une session par prompt).

---

## 📊 Distribution Recommandée

### Ordre Suggéré de Génération

**Phase 1 : Zones Critiques** (priorité haute)
1. tier_TOP-MID.md (6 prompts)
2. tier_MID-TOP.md (6 prompts)

**Phase 2 : Extrêmes Clairs**
3. tier_TOP.md (4 prompts)
4. tier_LOW.md (3 prompts)

**Phase 3 : Milieu**
5. tier_MID.md (4 prompts)

**Phase 4 : Intermédiaires**
6. tier_MID-LOW.md (3 prompts)
7. tier_LOW-MID.md (2 prompts)

**Phase 5 : Leurres** (le plus complexe)
8. tier_LEURRES.md (6 prompts)

**Rationale** : Commencer par les zones critiques (TOP-MID, MID-TOP) car ce sont les plus difficiles à calibrer. Les extrêmes (TOP, LOW) sont plus évidents. Les leurres nécessitent une bonne compréhension des tiers pour créer des contradictions pertinentes.

---

## 🎯 Checklist par Prompt

Pour chaque document généré, vérifiez :

- [ ] J'ai lu PRIMING.md dans cette session
- [ ] L'agent a produit un JSON valide
- [ ] Le document contient ≥ 800 mots
- [ ] Le vocabulaire correspond au tier attendu
- [ ] La section self_validation est complète
- [ ] J'ai copié le JSON dans ordinal_hierarchy.json
- [ ] J'ai vérifié qu'il n'y a pas de doublon d'ID

---

## 📝 Récapitulatif par Tier

### TOP (4 docs) - Scores 86-92
- Excellence absolue, leadership, SOTA
- Vocabulaire : révolutionnaire, supérieur, meilleur, breakthrough
- 2 FR (1 chiffres, 1 sémantique) + 2 EN (1 chiffres, 1 sémantique)

### TOP-MID (6 docs) - Scores 78-82 ⚠️ ZONE CRITIQUE
- Proche de l'excellence, excellent compromis
- Vocabulaire : near SOTA, remarquable, très performant, excellent rapport
- 3 FR + 3 EN | Mix chiffres/sémantique

### MID-TOP (6 docs) - Scores 72-77 ⚠️ ZONE CRITIQUE
- Solide, fiable, bon mais pas excellent
- Vocabulaire : solid, reliable, robuste, éprouvé, bon choix
- 3 FR + 3 EN | Mix chiffres/sémantique

### MID (4 docs) - Scores 65-71
- Moyen, acceptable, fonctionnel
- Vocabulaire : acceptable, convenable, standard, adéquat
- 2 FR + 2 EN | Mix chiffres/sémantique

### MID-LOW (3 docs) - Scores 60-64
- Limitations notables, avec réserves
- Vocabulaire : contraintes, compromis défavorables, limité
- 2 FR + 1 EN | Mix types

### LOW-MID (2 docs) - Scores 55-59
- Très limité, contraintes majeures
- Vocabulaire : très limité, restreint, basique
- 1 FR + 1 EN

### LOW (3 docs) - Scores 50-54
- Budget, entry-level, minimal
- Vocabulaire : économique, basique, apprentissage, prototypage
- 2 FR + 1 EN | Mix types

### LEURRES (6 docs) - Scores variables
- Contradictions internes intentionnelles
- Types : titre/contenu, début/fin, score/texte, subtil, flagrant, inverse
- 3 FR + 3 EN

---

## ⏱️ Estimation Temps

- **Par document** : 5-10 minutes (lecture PRIMING + génération + validation)
- **Total 34 documents** : 3-6 heures (selon votre rythme)

**Conseil** : Travaillez par batches de 5-6 documents avec pause entre chaque batch pour maintenir la qualité et la concentration.

---

## 🚨 Rappels Importants

1. **TOUJOURS fournir PRIMING.md** à chaque nouvelle session
2. **UN SEUL prompt par session** (pas de génération en masse)
3. **Aucun code autorisé** pour automatiser la création
4. **Minimum 800 mots** par document (non négociable)
5. **Auto-validation obligatoire** dans chaque JSON

---

## 📞 Support

Si vous avez des questions ou détectez des incohérences dans les prompts :
1. Référez-vous d'abord à PRIMING.md
2. Relisez les conseils spécifiques au tier dans le fichier tier_*.md
3. En cas de doute sur un positionnement tier, privilégiez l'honnêteté sémantique

---

**Bon courage pour la génération des 34 documents ! 🚀**

Le résultat sera un golden dataset de référence scientifique pour évaluer la granularité sémantique de Voyage AI.
