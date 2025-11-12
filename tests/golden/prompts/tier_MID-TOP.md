# TIER MID-TOP - Prompts de Tâches (6 documents)

> **Instructions** : Lisez d'abord `PRIMING.md` en entier, puis exécutez UN SEUL prompt ci-dessous.

---

## 🎯 ZONE CRITIQUE : Qu'est-ce que MID-TOP ?

**MID-TOP** (72-77) représente l'autre frontière subtile :
- **Pas excellent** : Ne peut pas prétendre à l'excellence ou au near-SOTA
- **Mais clairement bon** : Au-dessus de la moyenne, fiable, solide
- **Nuances clés** : "solid choice", "reliable", "good performance", "bon rapport qualité/prix"

**Vocabulaire distinctif** :
- "solide" / "solid" (≠ "excellent")
- "fiable" / "reliable" (≠ "exceptionnel")
- "bon" / "good" (≠ "remarquable")
- "polyvalent" / "versatile" (≠ "supérieur")

**Tone** : Pragmatique, équilibré, factuel. Positif mais sans superlatifs.

---

## 📋 PROMPT 1/6 : MIDTOP_1_FR_NUMERIC

### Spécifications
- **ID** : `MIDTOP_1_FR_NUMERIC`
- **Tier** : MID-TOP
- **Score** : 75
- **Langue** : Français
- **Type** : Avec indices numériques

### Objectif du Document
Créez un document qui présente une **solution solide et fiable, avec des performances correctes mais pas exceptionnelles**. Les chiffres doivent montrer des résultats bons, clairement au-dessus de la médiane, mais sans impressionner.

### Nuances à Capturer
- Performances bonnes et stables
- Fiabilité comme argument principal
- Rapport qualité/prix ou simplicité d'utilisation mis en avant
- Pas de prétention à l'excellence

### Output Attendu
Produisez un JSON avec :
- Un contenu de **minimum 800 mots**
- Des métriques bonnes mais clairement pas dans le top 3
- Vocabulaire MID-TOP (solide, fiable, robuste, éprouvé)
- Auto-validation expliquant comment vous restez positif sans être excellent

**RAPPEL** : Aucune génération de code autorisée. Travail manuel uniquement.

---

## 📋 PROMPT 2/6 : MIDTOP_2_FR_SEMANTIC

### Spécifications
- **ID** : `MIDTOP_2_FR_SEMANTIC`
- **Tier** : MID-TOP
- **Score** : 73
- **Langue** : Français
- **Type** : Purement sémantique

### Objectif du Document
Créez un document qui **communique la solidité et la fiabilité**, uniquement par le langage. Le ton doit être pragmatique : cette solution fait le travail correctement, sans prétendre à l'innovation.

### Nuances à Capturer
- "Choix solide pour la plupart des besoins"
- "Performances satisfaisantes"
- "Solution éprouvée et mature"
- Éviter tout superlatif

### Output Attendu
Produisez un JSON avec :
- Un contenu de **minimum 800 mots**
- Aucun chiffre explicite
- Vocabulaire pragmatique et équilibré
- Auto-validation montrant la distinction claire vs TOP-MID

**RAPPEL** : Aucune génération de code autorisée. Travail manuel uniquement.

---

## 📋 PROMPT 3/6 : MIDTOP_3_FR_MIXED

### Spécifications
- **ID** : `MIDTOP_3_FR_MIXED`
- **Tier** : MID-TOP
- **Score** : 76
- **Langue** : Français
- **Type** : Mixte (chiffres + sémantique)

### Objectif du Document
Créez un document qui **combine des métriques correctes et une argumentation sur la robustesse/maturité** de la solution. L'accent doit être mis sur la fiabilité à long terme plutôt que la performance de pointe.

### Nuances à Capturer
- Métriques dans la moyenne haute (mais pas top)
- Arguments sur la stabilité, la maintenance, l'écosystème
- Reconnaissance que d'autres solutions sont plus performantes, mais justification du choix

### Output Attendu
Produisez un JSON avec :
- Un contenu de **minimum 800 mots**
- Mix de chiffres corrects ET arguments de fiabilité
- Vocabulaire équilibré : compétent, éprouvé, pratique
- Auto-validation justifiant le positionnement MID-TOP

**RAPPEL** : Aucune génération de code autorisée. Travail manuel uniquement.

---

## 📋 PROMPT 4/6 : MIDTOP_4_EN_NUMERIC

### Spécifications
- **ID** : `MIDTOP_4_EN_NUMERIC`
- **Tier** : MID-TOP
- **Score** : 77
- **Language** : English
- **Type** : With numeric indicators

### Document Objective
Create a document presenting a **solid and reliable solution, with correct but not exceptional performance**. Numbers should show good results, clearly above median, but without impressing.

### Nuances to Capture
- Good and stable performance
- Reliability as main argument
- Quality/price ratio or ease of use highlighted
- No claim to excellence

### Expected Output
Produce a JSON with:
- Content of **minimum 800 words**
- Good metrics but clearly not in top 3
- MID-TOP vocabulary (solid, reliable, robust, proven)
- Self-validation explaining how you stay positive without being excellent

**REMINDER**: No code generation allowed. Manual work only.

---

## 📋 PROMPT 5/6 : MIDTOP_5_EN_SEMANTIC

### Spécifications
- **ID** : `MIDTOP_5_EN_SEMANTIC`
- **Tier** : MID-TOP
- **Score** : 72
- **Language** : English
- **Type** : Purely semantic

### Document Objective
Create a document that **communicates solidity and reliability**, solely through language. The tone should be pragmatic: this solution does the job correctly, without claiming innovation.

### Nuances to Capture
- "Solid choice for most needs"
- "Satisfactory performance"
- "Proven and mature solution"
- Avoid all superlatives

### Expected Output
Produce a JSON with:
- Content of **minimum 800 words**
- No explicit numbers
- Pragmatic and balanced vocabulary
- Self-validation showing clear distinction vs TOP-MID

**REMINDER**: No code generation allowed. Manual work only.

---

## 📋 PROMPT 6/6 : MIDTOP_6_EN_MIXED

### Spécifications
- **ID** : `MIDTOP_6_EN_MIXED`
- **Tier** : MID-TOP
- **Score** : 74
- **Language** : English
- **Type** : Mixed (numbers + semantic)

### Document Objective
Create a document that **combines correct metrics and argumentation about robustness/maturity** of the solution. The focus should be on long-term reliability rather than peak performance.

### Nuances to Capture
- Metrics in the upper-middle range (but not top)
- Arguments about stability, maintenance, ecosystem
- Acknowledgment that other solutions are more performant, but justification of the choice

### Expected Output
Produce a JSON with:
- Content of **minimum 800 words**
- Mix of correct numbers AND reliability arguments
- Balanced vocabulary: competent, proven, practical
- Self-validation justifying MID-TOP positioning

**REMINDER**: No code generation allowed. Manual work only.

---

## 🔍 Conseil Crucial pour MID-TOP

Ce tier nécessite d'**être honnête sans être négatif**.

**Évitez** :
- ❌ Utiliser des superlatifs (excellent, remarquable, etc.)
- ❌ Être trop prudent ou défensif (cela serait MID ou en-dessous)
- ✅ Soyez factuellement positif : "ça fonctionne bien, c'est fiable"

**Indicateurs linguistiques utiles** :
- "Performances satisfaisantes" (pas "exceptionnelles")
- "Choix judicieux" (pas "meilleur choix")
- "Solution mature" (met l'accent sur stabilité, pas innovation)
- "Bon rapport qualité/prix" (implique compromis)

**Argumentation type MID-TOP** :
- Performance correcte + Simplicité d'utilisation
- Performance correcte + Écosystème mature
- Performance correcte + Coût raisonnable
- Performance correcte + Support actif

---

**Sélectionnez UN prompt ci-dessus et produisez le document correspondant.**
