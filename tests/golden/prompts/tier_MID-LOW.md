# TIER MID-LOW - Prompts de Tâches (3 documents)

> **Instructions** : Lisez d'abord `PRIMING.md` en entier, puis exécutez UN SEUL prompt ci-dessous.

---

## 🎯 Qu'est-ce que MID-LOW ?

**MID-LOW** (60-64) représente la zone où **les limitations commencent à être significatives** :
- **Utilisable mais avec réserves** : Fonctionne mais avec des contraintes notables
- **Trade-offs importants** : Compromis défavorables (coût vs qualité, simplicité vs performance, etc.)
- **Nuances clés** : "limitations notables", "contraintes", "avec réserves", "compromis"

**Vocabulaire distinctif** :
- "limitations notables" / "notable limitations"
- "contraintes" / "constraints"
- "compromis" / "trade-offs"
- "avec réserves" / "with reservations"

**Tone** : Prudent, honnête sur les limites, mais pas franchement négatif. Descriptif des contraintes.

---

## 📋 PROMPT 1/3 : MIDLOW_1_FR_NUMERIC

### Spécifications
- **ID** : `MIDLOW_1_FR_NUMERIC`
- **Tier** : MID-LOW
- **Score** : 62
- **Langue** : Français
- **Type** : Avec indices numériques

### Objectif du Document
Créez un document qui présente une **solution fonctionnelle mais avec des performances clairement en-deçà de la moyenne**. Les chiffres doivent montrer des résultats faibles, avec mention explicite de domaines où la solution est limitée.

### Nuances à Capturer
- Performances sous la médiane
- Limitations chiffrées (latence élevée, précision limitée, etc.)
- Cas d'usage restreints où la solution reste acceptable
- Honnêteté sur les contraintes

### Output Attendu
Produisez un JSON avec :
- Un contenu de **minimum 800 mots**
- Des métriques clairement en-dessous de la moyenne
- Vocabulaire MID-LOW (limitations, contraintes, compromis)
- Auto-validation expliquant comment vous êtes honnête sans être dissuasif

**RAPPEL** : Aucune génération de code autorisée. Travail manuel uniquement.

---

## 📋 PROMPT 2/3 : MIDLOW_2_FR_SEMANTIC

### Spécifications
- **ID** : `MIDLOW_2_FR_SEMANTIC`
- **Tier** : MID-LOW
- **Score** : 61
- **Langue** : Français
- **Type** : Purement sémantique

### Objectif du Document
Créez un document qui **communique les limitations et contraintes**, uniquement par le langage. Le ton doit être prudent et descriptif des réserves, sans être défaitiste.

### Nuances à Capturer
- "Convient pour des cas d'usage simples uniquement"
- "Limitations importantes à considérer"
- "Compromis défavorables dans certains contextes"
- Vocabulaire de mise en garde sans condamnation

### Output Attendu
Produisez un JSON avec :
- Un contenu de **minimum 800 mots**
- Aucun chiffre explicite
- Vocabulaire prudent et descriptif des limites
- Auto-validation montrant l'équilibre entre honnêteté et non-disqualification

**RAPPEL** : Aucune génération de code autorisée. Travail manuel uniquement.

---

## 📋 PROMPT 3/3 : MIDLOW_3_EN_MIXED

### Spécifications
- **ID** : `MIDLOW_3_EN_MIXED`
- **Tier** : MID-LOW
- **Score** : 64
- **Language** : English
- **Type** : Mixed (numbers + semantic)

### Document Objective
Create a document that **combines weak metrics and description of significant limitations**. The solution works but has notable constraints that restrict its applicability.

### Nuances to Capture
- Below-average performance with numbers
- Explicit description of constraints
- Restricted use cases where it remains acceptable
- Honest acknowledgment of trade-offs

### Expected Output
Produce a JSON with:
- Content of **minimum 800 words**
- Mix of weak numbers AND constraint descriptions
- MID-LOW vocabulary (limitations, constraints, trade-offs)
- Self-validation explaining how you remain factual without being dismissive

**REMINDER**: No code generation allowed. Manual work only.

---

## 🔍 Conseil Crucial pour MID-LOW

Ce tier nécessite d'**être honnête sur les faiblesses sans dissuader complètement**.

**Évitez** :
- ❌ Être trop neutre (cela serait MID)
- ❌ Être franchement négatif (cela serait LOW-MID ou LOW)
- ✅ Décrivez factuellement les limitations tout en reconnaissant des contextes où c'est acceptable

**Indicateurs linguistiques utiles** :
- "Limitations notables" (pas "fatales")
- "Compromis défavorables" (implique qu'il y a des trade-offs)
- "Convient pour des besoins simples" (restreint la portée)
- "Avec réserves" (prudence sans rejet total)

**Argumentation type MID-LOW** :
- Performances faibles MAIS utilisable pour cas d'usage basiques
- Limitations importantes MAIS compensées par [simplicité/coût/autre]
- Contraintes techniques MAIS acceptables si besoins restreints
- Ne convient pas pour production critique MAIS OK pour développement/test

**Structure suggérée** :
1. Présentation factuelle de la solution
2. Description honnête des performances (faibles)
3. Énumération des limitations et contraintes
4. Identification des cas d'usage restreints où c'est acceptable
5. Conclusion prudente

---

**Sélectionnez UN prompt ci-dessus et produisez le document correspondant.**
