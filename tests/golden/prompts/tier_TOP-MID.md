# TIER TOP-MID - Prompts de Tâches (6 documents)

> **Instructions** : Lisez d'abord `PRIMING.md` en entier, puis exécutez UN SEUL prompt ci-dessous.

---

## 🎯 ZONE CRITIQUE : Qu'est-ce que TOP-MID ?

**TOP-MID** (78-82) représente la zone la plus subtile à capturer sémantiquement :
- **Pas tout à fait TOP** : Ne peut pas prétendre au leadership absolu
- **Mais clairement excellent** : Nettement au-dessus de la moyenne
- **Nuances clés** : "near state-of-the-art", "excellent compromis", "très proche du meilleur"

**Vocabulaire distinctif** :
- "proche du meilleur" (≠ "le meilleur")
- "performances remarquables" (≠ "performances inégalées")
- "excellent rapport qualité/prix" (introduit une nuance coût)
- "competitive" (≠ "superior")

---

## 📋 PROMPT 1/6 : TOPMID_1_FR_NUMERIC

### Spécifications
- **ID** : `TOPMID_1_FR_NUMERIC`
- **Tier** : TOP-MID
- **Score** : 81
- **Langue** : Français
- **Type** : Avec indices numériques

### Objectif du Document
Créez un document qui présente une **solution d'excellence, mais légèrement en retrait du SOTA**. Les chiffres doivent montrer des performances très élevées, mais avec quelques concurrents proches ou quelques benchmarks où il n'est pas #1.

### Nuances à Capturer
- Performance exceptionnelle mais pas inégalée
- Mention possible d'un contexte où il n'est pas optimal
- Équilibre performance/coût favorable

### Output Attendu
Produisez un JSON avec :
- Un contenu de **minimum 800 mots**
- Des métriques très bonnes mais pas toujours meilleures que tous les concurrents
- Vocabulaire TOP-MID (remarquable, excellent, proche du meilleur)
- Auto-validation expliquant les nuances subtiles vs TOP pur

**RAPPEL** : Aucune génération de code autorisée. Travail manuel uniquement.

---

## 📋 PROMPT 2/6 : TOPMID_2_FR_SEMANTIC

### Spécifications
- **ID** : `TOPMID_2_FR_SEMANTIC`
- **Tier** : TOP-MID
- **Score** : 79
- **Langue** : Français
- **Type** : Purement sémantique

### Objectif du Document
Créez un document qui **communique l'excellence avec nuances**, uniquement par le langage. Le document doit être clairement positif, mais introduire subtilement des réserves ou des contextes d'usage optimaux.

### Nuances à Capturer
- "Proche du state-of-the-art" (pas "le" state-of-the-art)
- "Excellent choix dans la plupart des cas"
- "Performances remarquables avec un coût maîtrisé"

### Output Attendu
Produisez un JSON avec :
- Un contenu de **minimum 800 mots**
- Aucun chiffre explicite
- Vocabulaire positif mais nuancé
- Auto-validation détaillant comment vous évitez le tier TOP sans tomber dans MID-TOP

**RAPPEL** : Aucune génération de code autorisée. Travail manuel uniquement.

---

## 📋 PROMPT 3/6 : TOPMID_3_FR_MIXED

### Spécifications
- **ID** : `TOPMID_3_FR_MIXED`
- **Tier** : TOP-MID
- **Score** : 80
- **Langue** : Français
- **Type** : Mixte (chiffres + sémantique)

### Objectif du Document
Créez un document qui **combine métriques quantitatives et évaluation qualitative** pour positionner la solution comme excellente mais avec un rapport qualité/prix ou qualité/simplicité comme argument clé.

### Nuances à Capturer
- Quelques benchmarks très bons (mais pas tous)
- Argumentation sur le "sweet spot" performance/coût
- Reconnaissance que d'autres solutions existent avec performance marginale supérieure

### Output Attendu
Produisez un JSON avec :
- Un contenu de **minimum 800 mots**
- Mix de chiffres concrets ET arguments qualitatifs
- Vocabulaire équilibré : excellence technique + pragmatisme
- Auto-validation justifiant l'équilibre entre signaux TOP et nuances

**RAPPEL** : Aucune génération de code autorisée. Travail manuel uniquement.

---

## 📋 PROMPT 4/6 : TOPMID_4_EN_NUMERIC

### Spécifications
- **ID** : `TOPMID_4_EN_NUMERIC`
- **Tier** : TOP-MID
- **Score** : 82
- **Language** : English
- **Type** : With numeric indicators

### Document Objective
Create a document presenting a **solution with excellent performance, but slightly below absolute SOTA**. Metrics should show very high performance, but with some competitors close by or some benchmarks where it's not #1.

### Nuances to Capture
- Exceptional but not unmatched performance
- Possible mention of contexts where it's not optimal
- Favorable performance/cost balance

### Expected Output
Produce a JSON with:
- Content of **minimum 800 words**
- Very good metrics but not always better than all competitors
- TOP-MID vocabulary (remarkable, excellent, near-best)
- Self-validation explaining subtle nuances vs pure TOP

**REMINDER**: No code generation allowed. Manual work only.

---

## 📋 PROMPT 5/6 : TOPMID_5_EN_SEMANTIC

### Spécifications
- **ID** : `TOPMID_5_EN_SEMANTIC`
- **Tier** : TOP-MID
- **Score** : 78
- **Language** : English
- **Type** : Purely semantic

### Document Objective
Create a document that **communicates excellence with nuances**, solely through language. The document should be clearly positive, but subtly introduce reservations or optimal use contexts.

### Nuances to Capture
- "Near state-of-the-art" (not "the" state-of-the-art)
- "Excellent choice in most cases"
- "Remarkable performance with controlled cost"

### Expected Output
Produce a JSON with:
- Content of **minimum 800 words**
- No explicit numbers
- Positive but nuanced vocabulary
- Self-validation detailing how you avoid TOP tier without falling into MID-TOP

**REMINDER**: No code generation allowed. Manual work only.

---

## 📋 PROMPT 6/6 : TOPMID_6_EN_MIXED

### Spécifications
- **ID** : `TOPMID_6_EN_MIXED`
- **Tier** : TOP-MID
- **Score** : 80
- **Language** : English
- **Type** : Mixed (numbers + semantic)

### Document Objective
Create a document that **combines quantitative metrics and qualitative evaluation** to position the solution as excellent but with quality/price or quality/simplicity as a key argument.

### Nuances to Capture
- Some very good benchmarks (but not all)
- Argumentation about the "sweet spot" performance/cost
- Acknowledgment that other solutions exist with marginally superior performance

### Expected Output
Produce a JSON with:
- Content of **minimum 800 words**
- Mix of concrete numbers AND qualitative arguments
- Balanced vocabulary: technical excellence + pragmatism
- Self-validation justifying the balance between TOP signals and nuances

**REMINDER**: No code generation allowed. Manual work only.

---

## 🔍 Conseil Crucial pour TOP-MID

La difficulté de ce tier est de **maintenir l'enthousiasme technique tout en introduisant des nuances subtiles**.

**Évitez** :
- ❌ Être aussi affirmatif qu'un doc TOP
- ❌ Être aussi prudent qu'un doc MID-TOP
- ✅ Trouvez le juste milieu : "excellent avec contexte"

**Indicateurs linguistiques utiles** :
- "Performances proches de X" (pas "égales à")
- "Dans la plupart des scénarios" (pas "dans tous")
- "Excellent rapport Y" (introduit une dimension de compromis)

---

**Sélectionnez UN prompt ci-dessus et produisez le document correspondant.**
