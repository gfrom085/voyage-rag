# PRIMING PROMPT - Golden Dataset Generation

> **Usage** : Ce prompt doit être lu par tout agent avant d'exécuter une tâche de création de document.
> Il établit le contexte déterministe et les contraintes absolues du projet.

## 📚 DOCUMENTS DE RÉFÉRENCE OBLIGATOIRES

Avant de commencer votre document, vous DEVEZ consulter :
1. **Ce document (PRIMING.md)** : Contexte général et contraintes absolues
2. **LEXICON.md** : Référence lexicale exhaustive par tier ⚠️ **CRITIQUE**

**Le LEXICON.md contient le tableau hiérarchique complet de TOUS les synonymes et expressions par tier (TOP → LOW). Consulter ce lexique AVANT d'écrire est OBLIGATOIRE pour éviter le drift lexical.**

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

### 5. Auto-Validation Rigoureuse

Avant de finaliser votre document, remplissez la section `self_validation` avec :

**semantic_choices** : Expliquez vos choix sémantiques
- Pourquoi ce vocabulaire spécifique ?
- Comment les nuances linguistiques reflètent-elles le tier ?
- Quels signaux sémantiques avez-vous intentionnellement placés ?

**quality_check** : Vérifiez les critères suivants
- ✅ Longueur ≥ 800 mots
- ✅ Nuances sémantiques appropriées au tier
- ✅ Cohérence titre-contenu (sauf si leurre intentionnel)
- ✅ Vocabulaire technique authentique et naturel
- ✅ Pas de répétitions artificielles pour atteindre le word count
- ✅ Grammaire et orthographe correctes

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
2. **Lire le prompt de tâche** (spécifications : id, tier, score, langue, type)
3. **Réfléchir à la stratégie sémantique** pour incarner ce tier
4. **Rédiger le document** (≥ 800 mots) avec nuances appropriées
5. **Auto-valider** avec la checklist
6. **Produire le JSON** structuré complet

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

- [ ] J'ai lu le PRIMING.md en entier
- [ ] Je comprends le tier à incarner et sa distinction des tiers adjacents
- [ ] Mon document contient ≥ 800 mots
- [ ] Le vocabulaire et le tone reflètent authentiquement le tier
- [ ] Je n'ai utilisé AUCUN code pour automatiser la création
- [ ] Le contenu est original et techniquement cohérent
- [ ] La section self_validation est complète et honnête
- [ ] Le JSON est valide et contient tous les champs obligatoires
- [ ] J'ai relu pour corriger fautes et incohérences

---

**Vous êtes maintenant prêt à recevoir votre prompt de tâche spécifique.**

**Bonne création ! 🎯**
