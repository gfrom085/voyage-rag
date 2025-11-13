# PRIMING PROMPT - Golden Dataset Generation

> **Usage** : Ce prompt doit être lu par tout agent avant d'exécuter une tâche de création de document.
> Il établit le contexte déterministe et les contraintes absolues du projet.

## 📚 DOCUMENTS DE RÉFÉRENCE OBLIGATOIRES

Avant de commencer votre document, vous DEVEZ consulter :
1. **Ce document (PRIMING.md)** : Contexte général et contraintes absolues
2. **LEXICON.md** : Référence lexicale exhaustive par tier ⚠️ **CRITIQUE**

**Le LEXICON.md contient le tableau hiérarchique complet de TOUS les synonymes et expressions par tier (TOP → LOW). Consulter ce lexique AVANT d'écrire est OBLIGATOIRE pour éviter le drift lexical.**

### ⚠️ Importance Critique du LEXICON

**Sans le LEXICON.md, le drift est mathématiquement garanti.**

Le LEXICON est votre **base de référence absolue** pour :
- ✅ Identifier le vocabulaire **autorisé** pour votre tier
- ❌ Identifier le vocabulaire **interdit** (appartenant aux tiers adjacents)
- 🔍 Vérifier chaque qualificatif clé (titre, conclusion, arguments principaux)
- 📊 Comprendre les "mots signature" qui identifient instantanément un tier

**Vous devrez consulter le LEXICON plusieurs fois pendant la rédaction** (voir section Workflow ci-dessous).

---

## 🎯 CONTEXTE DU PROJET

Vous participez à la création d'un **golden dataset scientifique** pour évaluer la **granularité sémantique** des embeddings Voyage AI (modèles voyage-3 et voyage-3-lite).

### Objectif Final

Découvrir avec précision la capacité de Voyage-3 à distinguer des **nuances sémantiques ultra-fines** dans un système RAG (Retrieval-Augmented Generation) utilisant :
- **Voyage AI embeddings** (voyage-3, voyage-3-lite, voyage-code-3)
- **ChromaDB** comme vector database
- **Voyage AI reranking** pour amélioration de pertinence
- **Recherche par similarité cosinus**

### Question de Recherche Centrale

**Jusqu'où Voyage-3 peut-il distinguer finement des gradations ordinales ?**

Exemples de distinctions testées :
- TOP (score ≥ 85) vs TOP-MID (78-82) vs MID-TOP (72-77) vs MID (65-71)
- Documents avec écarts de 1, 2, 5, 10 points de score
- Encodage sémantique de "meilleur/premium/SOTA" vs "équilibré/milieu de gamme" vs "budget/entry-level"
- Robustesse face aux contradictions internes (titre vs contenu)

---

## 📊 CE QUI SERA ÉVALUÉ

Le dataset golden servira à mesurer :

### 1. Distinction Ordinale Fine
- Capacité à ranger correctement des documents selon leur tier sémantique
- Corrélation entre score numérique et ranking prédit (Kendall's Tau)
- Précision du classement (nDCG@5, nDCG@10)

### 2. Sensibilité aux Écarts (Δ)
- Δ = 1 point : doc(85) vs doc(84) → ordre respecté ?
- Δ = 2 points : doc(85) vs doc(83) → ordre respecté ?
- Δ = 5 points : doc(85) vs doc(80) → ordre respecté ?
- Δ = 10+ points : doc(85) vs doc(75) → ordre respecté ?

**Objectif** : Identifier le seuil minimum de Δ pour distinction fiable.

### 3. Encodage Sémantique Hiérarchique
- Query "meilleur modèle" → retourne-t-il docs TOP en priorité ?
- Query "option économique" → retourne-t-il docs LOW en priorité ?
- Voyage encode-t-il nativement la hiérarchie premium > balanced > budget ?

### 4. Robustesse aux Contradictions
- Document avec titre "premium" mais contenu décrivant limitations
- Document commençant positif mais terminant négatif
- Voyage se fie-t-il au titre ? au contenu ? aux deux également ?

### 5. Comparaison Linguistique FR/EN
- Performance identique sur français vs anglais ?
- Biais systématique pour l'une des langues ?

### 6. Impact des Indices Numériques
- Documents avec chiffres explicites ("score MTEB de 85")
- Documents purement sémantiques ("excellent", "performant")
- Voyage encode-t-il mieux les chiffres ou le langage naturel ?

---

## 🏗️ STRUCTURE DU DATASET GOLDEN

### Distribution des Documents (34 total)

| Tier      | Nombre | Score Range | Focus                                      |
|-----------|--------|-------------|--------------------------------------------|
| TOP       | 4      | 85-95       | Superlatifs clairs, SOTA, "best-in-class"  |
| TOP-MID   | 6      | 78-82       | **Zone critique** : excellence avec nuances |
| MID-TOP   | 6      | 72-77       | **Zone critique** : bon mais pas excellent  |
| MID       | 4      | 65-71       | Équilibré, "solid option", fiable          |
| MID-LOW   | 3      | 60-64       | Acceptable avec limitations notables       |
| LOW-MID   | 2      | 55-59       | Limité mais utilisable                     |
| LOW       | 3      | 50-54       | Budget, entry-level, contraintes fortes    |
| LEURRES   | 6      | Variable    | Contradictions internes intentionnelles    |

### Principe de Diversité

**Langue** : 50% français, 50% anglais (équilibré pour détecter biais linguistiques)

**Indices numériques** : 50% avec chiffres explicites, 50% purement sémantique

**Longueur** : Tous les documents doivent contenir **minimum 800 mots** (pertinence pour Voyage Context 3 qui gère de longs contextes)

**Domaine** : Focus unique sur **embeddings / RAG / NLP / semantic search** (maximise comparabilité)

---

## 📋 FORMAT DE SORTIE ATTENDU

Chaque document doit être produit au format **JSON structuré** suivant :

```json
{
  "id": "TOP_1_FR_CHIFFRES",
  "title": "Titre concis et descriptif du document",
  "text": "Contenu complet du document (minimum 800 mots)...",
  "score": 92,
  "tier": "TOP",
  "self_validation": {
    "semantic_choices": "Justification des choix sémantiques : pourquoi ce vocabulaire, ces nuances, ces formulations spécifiques contribuent-elles à positionner ce document dans son tier ?",
    "word_count": 847,
    "language": "FR",
    "numeric_indicators": true,
    "quality_check": "✅ Longueur suffisante | ✅ Nuances sémantiques appropriées au tier | ✅ Cohérence titre-contenu | ✅ Vocabulaire technique authentique"
  }
}
```

### Champs Obligatoires

- **id** : Identifiant unique (fourni dans le prompt de tâche)
- **title** : Titre du document (50-100 caractères)
- **text** : Contenu complet (≥ 800 mots)
- **score** : Score numérique (fourni dans le prompt de tâche)
- **tier** : Tier sémantique (fourni dans le prompt de tâche)
- **self_validation** : Auto-évaluation de la qualité

### Important : Aucune Métadonnée Supplémentaire

**N'ajoutez PAS** les champs suivants dans ce premier set :
- ❌ `domain` (sera ajouté en vague 2)
- ❌ `category` (sera ajouté en vague 2)
- ❌ `keywords` (sera ajouté en vague 2)
- ❌ `metadata` (sera ajouté en vague 2)

**Rationale** : Nous testons d'abord le comportement du modèle sur texte pur, sans metadata. Une vague 2 testera l'impact des métadonnées.

---

## ⚠️ CONTRAINTES ABSOLUES

### 1. Interdiction Stricte de Génération de Code

**IL EST ABSOLUMENT INTERDIT** de générer du code (Python, JavaScript, ou tout langage de programmation) dans le but de réduire votre charge de travail ou d'automatiser la création de documents.

**Exemples INTERDITS** :
- ❌ Créer un script Python pour générer plusieurs documents via une boucle
- ❌ Utiliser des templates avec variables pour produire en masse
- ❌ Écrire du code pour automatiser la génération de contenu
- ❌ Déléguer à des outils/libraries/APIs la création du texte
- ❌ Utiliser des regex ou string manipulation pour créer des variantes

**Approche REQUISE** :
- ✅ Chaque document doit être pensé, réfléchi et crafté **individuellement**
- ✅ Réflexion sémantique approfondie pour chaque nuance
- ✅ Travail intellectuel manuel de haute qualité
- ✅ Aucun raccourci, aucune optimisation de processus

**Rationale** : L'objectif est de produire un golden dataset de référence scientifique où chaque document contient des nuances sémantiques subtiles et authentiques qui nécessitent un jugement humain (ou LLM). La qualité prime absolument sur l'efficacité de production.

### 2. Authenticité du Contenu

- ✅ Le contenu doit être **original** et rédigé spécifiquement pour ce dataset
- ⚠️ Vous pouvez vous inspirer de connaissances techniques réelles, mais PAS copier-coller de documentation existante
- ✅ Le langage doit être **naturel** et technique, comme un article de blog technique ou un whitepaper
- ❌ Éviter les formulations artificielles type "Ce document traite de..."

### 3. Cohérence du Tier

Chaque document doit **incarner sémantiquement** son tier :

**TOP (85-95)** :
- Vocabulaire : "state-of-the-art", "cutting-edge", "revolutionary", "breakthrough", "meilleur", "excellence", "supérieur"
- Tone : Confiant, affirmatif, prestigieux
- Focus : Performance absolue, leadership, innovation

**TOP-MID (78-82)** :
- Vocabulaire : "near state-of-the-art", "excellent compromis", "très performant", "proche du meilleur", "competitive"
- Tone : Positif mais avec légères nuances/réserves
- Focus : Équilibre performance/coût, "presque le meilleur"

**MID-TOP (72-77)** :
- Vocabulaire : "solid", "reliable", "good performance", "bon choix", "fiable", "robuste"
- Tone : Pragmatique, équilibré
- Focus : Fiabilité, rapport qualité/prix, polyvalence

**MID (65-71)** :
- Vocabulaire : "acceptable", "sufficient", "meets requirements", "convenable", "standard"
- Tone : Neutre, factuel
- Focus : Fonctionnel sans être exceptionnel

**MID-LOW (60-64)** :
- Vocabulaire : "limitations notables", "constraints", "trade-offs", "compromis", "restrictions"
- Tone : Prudent, mentionne des limites
- Focus : Utilisable mais avec réserves

**LOW-MID (55-59)** :
- Vocabulaire : "basic", "limited", "constrained", "limité", "restreint"
- Tone : Descriptif des limitations
- Focus : Cas d'usage restreints

**LOW (50-54)** :
- Vocabulaire : "budget", "entry-level", "minimal", "économique", "basique"
- Tone : Honnête sur les limites importantes
- Focus : Prix/accessibilité vs performance

**LEURRES** :
- Contradictions intentionnelles entre différentes parties du document
- Testent la pondération titre vs contenu, début vs fin, etc.

---

## ⚠️ MOTS "SIGNATURE" À ÉVITER ABSOLUMENT

Certains mots identifient **instantanément** un tier spécifique. Utiliser ces mots dans un autre tier constitue un **drift critique** qui déclenche une révision obligatoire.

### 🚨 Mots Signature TOP (INTERDITS pour tous autres tiers)

| Mot/Expression | Pourquoi Signature TOP | Exemple de Drift |
|----------------|------------------------|-------------------|
| "optimal/optimale" (absolu) | Implique "meilleur possible sans équivalent" | ❌ Titre TOP-MID : "Architecture **Optimale**" |
| "inégalé/inégalée" | Signifie "aucun concurrent équivalent" | ❌ TOP-MID : "performance **inégalée**" |
| "révolutionnaire" | Changement de paradigme disruptif | ❌ TOP-MID : "approche **révolutionnaire**" |
| "le meilleur" (article défini) | Supériorité absolue sans nuance | ❌ TOP-MID : "**le meilleur** modèle" |
| "state-of-the-art" (sans nuance) | Références absolues SOTA | ❌ TOP-MID : "**state-of-the-art** performance" |

**Alternatives pour TOP-MID** : "parmi les meilleurs", "proche du meilleur", "d'excellence", "remarquable", "performances supérieures"

### ⚠️ Mots Signature MID-TOP (INTERDITS pour TOP-MID et supérieurs)

| Mot/Expression | Pourquoi Signature MID-TOP | Exemple de Drift |
|----------------|---------------------------|-------------------|
| "solide" | Fiabilité sobre, pas excellence | ❌ Conclusion TOP-MID : "choix stratégique **solide**" |
| "fiable" | Prévisibilité stable sans éclat | ❌ TOP-MID : "option **fiable**" |
| "robuste" | Résistance pragmatique | ❌ TOP-MID : "architecture **robuste**" |
| "bon choix" | Positivité modérée | ❌ TOP-MID : "**bon choix** pour production" |
| "solid" (EN) | Même connotation sobre | ❌ TOP-MID : "**solid** performance" |

**Alternatives pour TOP-MID** : "excellent", "remarquable", "performances supérieures", "d'excellence", "parmi les meilleurs"

### 📋 Règle de Détection Rapide

**Avant d'utiliser un qualificatif, demandez-vous** :
1. Ce mot apparaît-il dans la section de MON tier dans LEXICON.md ?
2. Ce mot apparaît-il dans les "mots signature" d'un AUTRE tier ?
3. Si doute → Consulter LEXICON.md → Choisir alternative sûre

**Zones CRITIQUES** (tolérance ZÉRO) :
- 🚨 **Titre** : AUCUN mot signature d'autre tier
- 🚨 **Conclusion** : AUCUN mot signature d'autre tier

---

## 🚨 ZONES CRITIQUES : Titre et Conclusion (TOLÉRANCE ZÉRO)

Le titre et la conclusion sont les **zones les plus visibles** d'un document. Ils créent la première et la dernière impression. Dans le contexte de notre dataset golden, ces zones **DOIVENT être 100% conformes au tier**, car :

1. **Impact psychologique** : Le titre ancre la perception globale du document
2. **Test d'encodage** : Voyage-3 pourrait pondérer différemment titre vs contenu
3. **Drift amplifié** : Un seul mot hors-tier dans le titre = drift critique détecté

### ⚠️ Règle de Tolérance ZÉRO

**Titre** : Aucun mot appartenant à un autre tier n'est toléré
**Conclusion** (derniers 200 mots) : Aucun mot signature d'autre tier n'est toléré

### 📋 Exemples de Titres Par Tier

#### TOP-MID (78-82) - Exemples CORRECTS

✅ **"Architecture d'Excellence pour les Systèmes RAG de Nouvelle Génération"**
- "d'Excellence" = TOP-MID (qualité supérieure avec nuance)

✅ **"Parmi les Meilleures Solutions d'Embeddings : Voyage-3 en Production"**
- "Parmi les Meilleures" = TOP-MID (superlatif nuancé, pas absolu)

✅ **"Performances Remarquables des Modèles Voyage : Analyse Approfondie"**
- "Remarquables" = TOP-MID (excellence notable sans être absolu)

#### TOP-MID (78-82) - Exemples INCORRECTS (Drift Détecté)

❌ **"Architecture Optimale pour les Systèmes RAG"**
- **Problème** : "Optimale" = TOP (meilleur possible absolu)
- **Correction** : "Architecture d'Excellence" ou "Architecture Performante"

❌ **"La Meilleure Solution d'Embeddings pour Production"**
- **Problème** : "La Meilleure" (article défini) = TOP (supériorité absolue)
- **Correction** : "Parmi les Meilleures Solutions" ou "Une Solution d'Excellence"

❌ **"Système RAG Solide et Fiable : Guide Complet"**
- **Problème** : "Solide" = MID-TOP (trop faible pour TOP-MID)
- **Correction** : "Système RAG d'Excellence" ou "Système RAG Remarquable"

### 📋 Exemples de Conclusions Par Tier

#### TOP-MID (78-82) - CORRECT

✅ "En conclusion, Voyage-3 représente **un choix d'excellence** pour les équipes recherchant **des performances supérieures** avec un **rapport qualité-coût remarquable**. Son positionnement **parmi les meilleurs** modèles du marché..."

#### TOP-MID (78-82) - INCORRECT (Drift Détecté)

❌ "En conclusion, Voyage-3 constitue **un choix stratégique solide** pour les architectures RAG modernes..."
- **Problème** : "solide" = MID-TOP (trop faible)
- **Correction** : "un choix stratégique d'excellence" ou "un choix remarquable"

### 🎯 Workflow de Vérification des Zones Critiques

**AVANT de finaliser votre document** :

1. **Isoler le titre** → Extraire TOUS les qualificatifs
2. **Ouvrir LEXICON.md** → Vérifier chaque mot dans votre section tier
3. **Vérifier les interdictions** → Consulter les mots signature des autres tiers
4. **Répéter pour la conclusion** → Mêmes vérifications

**Si un seul mot est hors-tier dans titre ou conclusion** → Révision OBLIGATOIRE

---

## 🚫 PIÈGES COURANTS À ÉVITER (Anti-Patterns)

Ces exemples proviennent de drifts **réellement détectés** lors des premières validations. Apprenez de ces erreurs pour ne pas les reproduire.

### Piège #1 : Titre Trop Fort pour le Tier ⚠️ CRITIQUE

**Exemple réel détecté** :
```json
{
  "id": "TOPMID_1_FR_NUMERIC",
  "tier": "TOP-MID",
  "title": "Architecture Optimale pour Voyage-3 en Production", // ❌ DRIFT CRITIQUE
  "score": 78
}
```

**Problème** :
- "Optimale" = vocabulaire TOP (meilleur possible absolu)
- Dans un document TOP-MID, cela crée une **incohérence sémantique**
- Le titre ancre une attente de perfection absolue que le contenu (avec nuances) ne peut pas tenir

**Correction** :
- ✅ "Architecture d'Excellence pour Voyage-3 en Production"
- ✅ "Architecture Performante : Voyage-3 en Production"
- ✅ "Parmi les Meilleures Architectures : Voyage-3 Analysé"

**Validation report** : Drift critique détecté → Score 78/100 → Révision OBLIGATOIRE

---

### Piège #2 : Conclusion Trop Faible pour le Tier ⚠️ CRITIQUE

**Exemple réel détecté** :
```json
{
  "tier": "TOP-MID",
  "text": "...En conclusion, Voyage-3 constitue un choix stratégique solide..." // ❌ DRIFT
}
```

**Problème** :
- "solide" = vocabulaire MID-TOP (fiabilité sobre, pas excellence)
- Dans un document TOP-MID, cela **affaiblit la conclusion**
- Incohérence : le corps parle d'excellence, la conclusion de fiabilité basique

**Correction** :
- ✅ "...un choix stratégique d'excellence..."
- ✅ "...un choix remarquable..."
- ✅ "...un choix parmi les meilleurs du marché..."

**Validation report** : Drift 12.5% détecté → Score 78/100 → Révision OBLIGATOIRE

---

### Piège #3 : Accumulation de Drift Subtil

**Exemple hypothétique** :
```
TOP-MID document contenant :
- "robuste" (ligne 45) → MID-TOP
- "fiable" (ligne 120) → MID-TOP
- "bon choix" (ligne 230) → MID-TOP
- "solid option" (ligne 340) → MID-TOP
```

**Problème** :
- Aucun mot n'est catastrophique isolément
- Mais **4 drifts MID-TOP** dans un doc TOP-MID = 20%+ drift
- Pattern systématique indiquant confusion conceptuelle du tier

**Correction** :
- Remplacer par vocabulaire TOP-MID : "excellent", "remarquable", "performances supérieures", "d'excellence"

---

### Piège #4 : Contradiction Titre-Contenu (Non Intentionnelle)

**Exemple** :
```json
{
  "tier": "MID-TOP",
  "title": "Performances Exceptionnelles de Voyage-3-Lite", // ❌ DRIFT (TOP-MID vocab)
  "text": "Voyage-3-Lite offre une option solide et fiable..." // ✅ CORRECT (MID-TOP vocab)
}
```

**Problème** :
- "Exceptionnelles" = TOP-MID (trop fort pour MID-TOP)
- Crée un **LEURRE non intentionnel** (on teste les leurres intentionnels séparément)
- Fausse les tests de pondération titre vs contenu

**Correction** :
- ✅ "Performances Solides et Fiables de Voyage-3-Lite" (MID-TOP cohérent)

---

### Piège #5 : Utilisation de Superlatifs Absolus Cachés

**Mots à surveiller** (souvent utilisés par erreur dans tiers inférieurs à TOP) :

| Mot Caché | Pourquoi Problématique | Tier Approprié |
|-----------|------------------------|----------------|
| "optimal(e)" | Absolu = meilleur mathématiquement possible | TOP uniquement |
| "parfait(e)" | Absolu = zéro défaut | TOP uniquement |
| "idéal(e)" | Absolu = correspond exactement | TOP uniquement |
| "ultime" | Absolu = dernier, final, définitif | TOP uniquement |
| "incomparable" | Absolu = impossible à comparer | TOP uniquement |

**Règle** : Si un mot implique **aucune amélioration possible**, c'est un superlatif absolu → TOP uniquement

---

### Piège #6 : Traduction Littérale FR ↔ EN

**Attention** : Certaines traductions changent le tier !

| Français | Tier FR | English (littéral) | Tier EN | Correction EN |
|----------|---------|-------------------|---------|---------------|
| "solide" | MID-TOP | "solid" | MID-TOP ✅ | OK |
| "robuste" | MID-TOP | "robust" | MID-TOP ✅ | OK |
| "performant" | TOP-MID | "performing" | ❌ (ambigu) | "high-performing" ✅ |
| "remarquable" | TOP-MID | "remarkable" | TOP-MID ✅ | OK |

**Conseil** : Vérifiez le LEXICON dans la langue cible, ne traduisez pas mécaniquement.

---

### 🎯 Checklist Anti-Drift Avant Soumission

Avant de finaliser votre document, vérifiez :

- [ ] Aucun superlatif absolu dans tiers < TOP
- [ ] Aucun "solide/fiable/robuste" dans tiers > MID-TOP
- [ ] Titre 100% conforme (vérifié dans LEXICON)
- [ ] Conclusion 100% conforme (vérifié dans LEXICON)
- [ ] Aucun pattern répétitif de drift (ex: 4× vocabulaire tier adjacent)
- [ ] Traductions EN/FR vérifiées dans LEXICON (pas littérales)

### 4. Longueur Minimale : 800 Mots

**Chaque document doit contenir au minimum 800 mots.**

**Rationale** : Voyage Context 3 est optimisé pour traiter de longs contextes (jusqu'à 128k tokens). Tester avec des documents courts ne reflèterait pas les cas d'usage réels. Un document de 800+ mots permet :
- Développement de nuances sémantiques subtiles
- Contexte riche pour l'embedding
- Représentation réaliste de documentation technique

**Structure suggérée** (non obligatoire, adaptez selon le contenu) :
- Introduction : 100-150 mots
- Corps principal : 500-600 mots (3-4 sections)
- Conclusion/synthèse : 100-150 mots

---

## ⚠️ PROTOCOLE D'AUTO-VÉRIFICATION LEXICALE (CRITIQUE)

**Ce protocole est OBLIGATOIRE avant de finaliser votre document.**

Sans cette auto-vérification, le drift est pratiquement garanti. Ce protocole transforme la prévention du drift d'une intention vague en **processus systématique et vérifiable**.

### Étape 1 : Ouvrir le LEXICON.md

1. Ouvrir le fichier `LEXICON.md`
2. Naviguer jusqu'à la section de **votre tier** (ex: "TIER TOP-MID (Scores 78-82)")
3. Lire attentivement :
   - Tableau "Superlatifs et Qualificatifs"
   - Section "✅ AUTORISÉS pour TOP-MID"
   - Section "❌ INTERDITS pour TOP-MID"
   - Tableau "Mots Signature" (section dédiée)

### Étape 2 : Extraire 10-15 Qualificatifs Clés

Extraire les qualificatifs suivants de VOTRE document :

**Zone 1 : Titre (CRITIQUE - tolérance ZÉRO)**
- Extraire TOUS les adjectifs, adverbes, expressions qualificatives
- Exemple : "Architecture **Optimale** pour Voyage-3" → ["Optimale"]

**Zone 2 : Introduction (premiers 200 mots)**
- Extraire 3-4 qualificatifs représentatifs
- Focus sur les mots qui positionnent le document

**Zone 3 : Corps Principal**
- Extraire 5-7 qualificatifs représentatifs
- Focus sur les arguments principaux de performance/qualité

**Zone 4 : Conclusion (derniers 200 mots - CRITIQUE - tolérance ZÉRO)**
- Extraire TOUS les qualificatifs de la conclusion
- Focus sur le positionnement final, recommandations

**Total attendu** : 10-15 qualificatifs minimum

### Étape 3 : Vérifier Chaque Qualificatif dans LEXICON

Pour chaque mot extrait, vérifier dans LEXICON.md :

**Question 1** : Ce mot apparaît-il dans la section "✅ AUTORISÉS" de mon tier ?
- ✅ OUI → Continuer au mot suivant
- ❌ NON → Passer à la Question 2

**Question 2** : Ce mot apparaît-il dans les "❌ INTERDITS" de mon tier ?
- ❌ OUI → **DRIFT DÉTECTÉ** → Noter le mot → Chercher alternative
- ✅ NON → Passer à la Question 3

**Question 3** : Ce mot apparaît-il dans les "Mots Signature" d'un AUTRE tier ?
- ❌ OUI → **DRIFT CRITIQUE DÉTECTÉ** → Révision OBLIGATOIRE
- ✅ NON → Mot acceptable

### Étape 4 : Calculer le Drift %

**Formule** :
```
Drift % = (Nombre de mots hors-tier / Nombre total de qualificatifs extraits) × 100
```

**Exemple** :
- 16 qualificatifs extraits
- 2 mots hors-tier détectés ("Optimale" + "solide")
- Drift = (2 / 16) × 100 = **12.5%**

**Seuils d'Acceptation** :
- **0-5%** : ✅ Excellent (accepté)
- **5-10%** : ⚠️ Acceptable (à surveiller)
- **10-20%** : ⚠️ Révision recommandée (corriger mots hors-tier)
- **>20%** : ❌ Révision OBLIGATOIRE (drift systématique)

### Étape 5 : Vérifications CRITIQUES Zones Sensibles

**⚠️ Vérification Titre** :
- [ ] Aucun mot signature d'autre tier
- [ ] Tous les qualificatifs sont dans la section "✅ AUTORISÉS" de mon tier
- [ ] Tolérance : **ZÉRO** (titre = première impression)

**⚠️ Vérification Conclusion** :
- [ ] Aucun mot signature d'autre tier
- [ ] Tous les qualificatifs sont dans la section "✅ AUTORISÉS" de mon tier
- [ ] Tolérance : **ZÉRO** (conclusion = dernière impression)

**Si une seule case n'est pas cochée** → Réviser le titre ou la conclusion

### Étape 6 : Documenter les Vérifications

Dans la section `self_validation` de votre JSON, documenter :

```json
"self_validation": {
  "semantic_choices": "Vocabulaire utilisé : 'parmi les meilleurs' (TOP-MID autorisé), 'remarquable' (TOP-MID autorisé), 'd'excellence' (TOP-MID autorisé). Mots ÉVITÉS : 'optimal' (TOP), 'solide' (MID-TOP). Titre vérifié : 'Architecture d'Excellence' (✅ TOP-MID). Conclusion vérifiée : 'choix remarquable' (✅ TOP-MID). Consultations LEXICON : 5 pauses effectuées. Drift estimé : 0% (aucun mot hors-tier détecté)."
}
```

---

## 🎯 Résumé du Protocole (Checklist Rapide)

1. [ ] Ouvrir LEXICON.md → Section de mon tier
2. [ ] Extraire 10-15 qualificatifs (titre, intro, corps, conclusion)
3. [ ] Vérifier chaque mot dans LEXICON (✅ autorisé ? ❌ interdit ? 🚨 signature autre tier ?)
4. [ ] Calculer drift % : (hors-tier / total) × 100
5. [ ] Vérifier titre : tolérance ZÉRO
6. [ ] Vérifier conclusion : tolérance ZÉRO
7. [ ] Drift < 5% ? → ✅ Continuer | Drift > 5% ? → ⚠️ Réviser
8. [ ] Documenter vérifications dans self_validation

**Temps estimé** : 10-15 minutes (investissement critique pour éviter révision ultérieure)

### 5. Auto-Validation Rigoureuse

Avant de finaliser votre document, remplissez la section `self_validation` avec :

**semantic_choices** : Expliquez vos choix sémantiques **ET votre vigilance anti-drift**
- Pourquoi ce vocabulaire spécifique ?
- Comment les nuances linguistiques reflètent-elles le tier ?
- Quels signaux sémantiques avez-vous intentionnellement placés ?
- **⚠️ NOUVEAU : Quels mots ai-je ÉVITÉS** car ils appartiennent aux tiers adjacents ?
- **⚠️ NOUVEAU : Comment ai-je vérifié** que le titre est 100% conforme au tier (via LEXICON) ?
- **⚠️ NOUVEAU : Comment ai-je vérifié** que la conclusion est 100% conforme au tier (via LEXICON) ?
- **⚠️ NOUVEAU : Ai-je consulté** la section "mots signature" du LEXICON pour éviter les termes interdits ?

**quality_check** : Vérifiez les critères suivants
- ✅ Longueur ≥ 800 mots
- ✅ Nuances sémantiques appropriées au tier
- ✅ **⚠️ NOUVEAU : Titre vérifié dans LEXICON (aucun mot signature d'autre tier)**
- ✅ **⚠️ NOUVEAU : Conclusion vérifiée dans LEXICON (aucun mot signature d'autre tier)**
- ✅ **⚠️ NOUVEAU : Consultations LEXICON effectuées** (minimum 3 fois : début, milieu, fin)
- ✅ Cohérence titre-contenu (sauf si leurre intentionnel)
- ✅ Vocabulaire technique authentique et naturel
- ✅ Pas de répétitions artificielles pour atteindre le word count
- ✅ Grammaire et orthographe correctes
- ✅ **⚠️ NOUVEAU : Aucun pattern de drift systématique** (ex: 4+ mots du même tier adjacent)

---

## 🧠 PHILOSOPHIE DU GOLDEN DATASET

### Pourquoi "Golden" ?

Un golden dataset est un **benchmark de référence scientifique** :
- Créé avec soin et rigueur intellectuelle
- Validé par des experts (vous)
- Utilisable pour des décisions production critiques
- Reproductible et auditable

### Votre Rôle

Vous êtes **l'expert humain** (ou LLM) qui crée le ground truth. Votre jugement définit ce qu'est un document "TOP" vs "TOP-MID" vs "MID-TOP".

Les tests mesureront : **"Voyage-3 partage-t-il votre jugement sémantique ?"**

### Principe de Non-Optimisation

**Ne cherchez pas à aider Voyage-3 à réussir le test.**

- ❌ N'insérez pas de "keywords" évidents pour faciliter le matching
- ❌ Ne simplifiez pas excessivement le langage
- ✅ Écrivez un contenu technique naturel et authentique
- ✅ Utilisez des nuances subtiles (c'est précisément ce qu'on teste)

**Objectif** : Découvrir les vraies capacités (et limites) de Voyage-3, pas les valider artificiellement.

---

## 📚 DOMAINE DE CONNAISSANCE

Tous les documents doivent porter sur les thématiques suivantes :

### Sujets Autorisés
- Embeddings vectoriels (word embeddings, sentence embeddings, document embeddings)
- Modèles d'embedding (Voyage AI, OpenAI, Cohere, E5, BGE, etc.)
- RAG (Retrieval-Augmented Generation) et ses composants
- Semantic search / vector search
- Vector databases (ChromaDB, Pinecone, Weaviate, Qdrant, etc.)
- Métriques d'évaluation (MTEB, BEIR, nDCG, MRR, etc.)
- Techniques de retrieval (dense retrieval, sparse retrieval, hybrid)
- Reranking et amélioration de pertinence
- Applications pratiques (Q&A systems, documentation search, etc.)

### Approche Technique

Le contenu doit être **technique mais accessible** :
- ✅ Terminologie précise (pas de vulgarisation excessive)
- ✅ Mentions de benchmarks, métriques, comparaisons
- ✅ Cas d'usage concrets
- ❌ Pas de jargon inaccessible sans contexte
- ❌ Pas de formules mathématiques complexes (sauf si pertinent)

---

## 🎯 VOTRE MISSION

Lorsque vous recevrez un prompt de tâche spécifique, vous devrez :

1. **Lire ce PRIMING.md en entier** (contexte complet)
2. **Lire LEXICON.md en entier** (référence lexicale obligatoire)
3. **Lire le prompt de tâche** (spécifications : id, tier, score, langue, type)
4. **Réfléchir à la stratégie sémantique** pour incarner ce tier
5. **Rédiger le document** (≥ 800 mots) avec nuances appropriées **en suivant le workflow ci-dessous**
6. **Auto-valider** avec la checklist anti-drift
7. **Produire le JSON** structuré complet

---

## 📝 WORKFLOW DE CRÉATION OPTIMAL (Ordre Obligatoire)

Ce workflow intègre des **pauses de vérification LEXICON** pour prévenir le drift de manière proactive.

### Étape 1 : Préparation (10 minutes de réflexion)
1. Lire PRIMING.md + **LEXICON.md section de votre tier**
2. Noter mentalement :
   - ✅ 5-7 mots **autorisés** pour votre tier
   - ❌ 5-7 mots **interdits** (tiers adjacents)
   - 🚨 Mots "signature" à éviter absolument

### Étape 2 : Rédaction de l'Introduction (100-150 mots)
3. Rédiger l'introduction avec vocabulaire de votre tier
4. ⚠️ **PAUSE CRITIQUE : Vérifier LEXICON**
   - Extraire 3-4 qualificatifs de l'introduction
   - Vérifier chaque mot dans LEXICON.md
   - Si doute → Remplacer par alternative sûre

### Étape 3 : Rédaction du Corps Principal (500-600 mots)
5. Rédiger le corps principal (3-4 sections techniques)
6. ⚠️ **PAUSE CRITIQUE : Vérifier LEXICON**
   - Extraire 5-7 qualificatifs du corps
   - Vérifier dans LEXICON.md
   - Détecter tout pattern répétitif de drift

### Étape 4 : Rédaction de la Conclusion (100-150 mots)
7. Rédiger la conclusion (synthèse, recommandations)
8. ⚠️ **PAUSE CRITIQUE : Vérifier LEXICON**
   - Extraire TOUS les qualificatifs de la conclusion
   - Vérifier un par un dans LEXICON.md
   - **Tolérance ZÉRO** : Aucun mot hors-tier accepté

### Étape 5 : Création du Titre
9. Créer le titre (résumé du positionnement tier)
10. ⚠️ **PAUSE ULTRA-CRITIQUE : Vérifier LEXICON**
    - Extraire TOUS les qualificatifs du titre
    - Vérifier un par un dans LEXICON.md
    - Consulter section "mots signature" → Aucun interdit
    - **Tolérance ZÉRO** : Le titre est la zone la plus critique

### Étape 6 : Auto-Validation Finale
11. Relire le document complet
12. ⚠️ **PAUSE FINALE : Extraction Systématique**
    - Extraire 10-15 qualificatifs représentatifs (titre, intro, corps, conclusion)
    - Créer tableau mental : Qualificatif | Position | Tier détecté | Verdict
    - Calculer drift % estimé : (hors-tier / total) × 100
    - Si drift > 5% → Réviser les mots hors-tier
13. Compléter la section `self_validation` avec vos vérifications LEXICON

### Étape 7 : Production du JSON
14. Formater le JSON avec tous les champs obligatoires
15. Vérifier validité JSON (pas de virgules manquantes, guillemets corrects)

---

## ⏱️ Résumé des 5 Pauses LEXICON Obligatoires

| # | Moment | Zone | Tolérance |
|---|--------|------|-----------|
| 1 | Après introduction | Introduction (3-4 mots) | Normale (5%) |
| 2 | Après corps principal | Corps (5-7 mots) | Normale (5%) |
| 3 | Après conclusion | Conclusion (tous mots) | **ZÉRO** |
| 4 | Après titre | Titre (tous mots) | **ZÉRO** |
| 5 | Validation finale | Document entier (10-15 mots) | Stricte (5%) |

**Temps estimé pour un document** : 45-60 minutes (incluant 5 pauses vérification)

---

## ⏱️ PATIENCE ET QUALITÉ

Ce projet n'a **aucune contrainte de temps ou de tokens**.

- ✅ Prenez le temps nécessaire pour réfléchir profondément
- ✅ Itérez sur vos formulations si besoin
- ✅ Privilégiez la qualité absolue sur la vitesse
- ✅ Chaque document est unique et mérite une attention totale

**Citation clé** : *"Mode ultrathink. Nous ne sommes pas pressés, les tokens ne sont pas un problème, je veux que tu fasses de ton mieux."*

---

## ✅ CHECKLIST FINALE AVANT SOUMISSION

Avant de soumettre votre JSON :

### Lecture et Préparation
- [ ] J'ai lu le PRIMING.md en entier
- [ ] **⚠️ J'ai lu le LEXICON.md en entier** (section de mon tier + mots signature)
- [ ] Je comprends le tier à incarner et sa distinction des tiers adjacents
- [ ] J'ai identifié 5-7 mots **autorisés** et 5-7 mots **interdits** pour mon tier

### Vérifications Lexicales CRITIQUES
- [ ] **⚠️ J'ai ouvert LEXICON.md** et vérifié mon tier
- [ ] **⚠️ J'ai extrait 10-15 qualificatifs** de mon document (titre, intro, corps, conclusion)
- [ ] **⚠️ Chaque qualificatif extrait** a été vérifié dans LEXICON.md
- [ ] **⚠️ Titre** : 100% conforme au tier (vérifié mot par mot dans LEXICON)
- [ ] **⚠️ Conclusion** : 100% conforme au tier (vérifié mot par mot dans LEXICON)
- [ ] **⚠️ Aucun mot "signature"** d'autre tier détecté (consulté section signature du LEXICON)
- [ ] **⚠️ Aucun pattern répétitif** de drift (ex: 4× vocabulaire tier adjacent)
- [ ] **⚠️ Drift estimé** : < 5% (calculé : nombre mots hors-tier / total × 100)

### Pauses LEXICON Effectuées
- [ ] **⚠️ Pause 1** : Après introduction → vérifiée
- [ ] **⚠️ Pause 2** : Après corps principal → vérifié
- [ ] **⚠️ Pause 3** : Après conclusion → vérifiée (tolérance ZÉRO)
- [ ] **⚠️ Pause 4** : Après titre → vérifié (tolérance ZÉRO)
- [ ] **⚠️ Pause 5** : Validation finale → document entier vérifié

### Qualité Générale
- [ ] Mon document contient ≥ 800 mots
- [ ] Le vocabulaire et le tone reflètent authentiquement le tier
- [ ] Je n'ai utilisé AUCUN code pour automatiser la création
- [ ] Le contenu est original et techniquement cohérent
- [ ] La section self_validation est complète et honnête **avec justification des vérifications LEXICON**
- [ ] Le JSON est valide et contient tous les champs obligatoires
- [ ] J'ai relu pour corriger fautes et incohérences

---

**Si TOUTES les cases sont cochées** → Votre document est prêt pour validation ✅

**Si une case ⚠️ n'est PAS cochée** → STOP → Effectuer la vérification manquante avant soumission

---

**Vous êtes maintenant prêt à recevoir votre prompt de tâche spécifique.**

**Bonne création ! 🎯**
