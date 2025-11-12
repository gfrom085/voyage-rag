# TIER MID - Prompts de Tâches (4 documents)

> **Instructions** : Lisez d'abord `PRIMING.md` en entier, puis exécutez UN SEUL prompt ci-dessous.

---

## 🎯 Qu'est-ce que MID ?

**MID** (65-71) représente la **moyenne, sans être négatif** :
- **Performances acceptables** : Fait le job sans impressionner
- **Répond aux exigences de base** : Fonctionnel mais sans avantage distinctif
- **Nuances clés** : "acceptable", "sufficient", "meets requirements", "convenable"

**Vocabulaire distinctif** :
- "acceptable" / "acceptable"
- "convenable" / "adequate"
- "standard" / "standard"
- "répond aux besoins de base" / "meets basic needs"

**Tone** : Neutre, factuel, sans enthousiasme ni critique. Descriptif objectif.

---

## 📋 PROMPT 1/4 : MID_1_FR_NUMERIC

### Spécifications
- **ID** : `MID_1_FR_NUMERIC`
- **Tier** : MID
- **Score** : 68
- **Langue** : Français
- **Type** : Avec indices numériques

### Objectif du Document
Créez un document qui présente une **solution moyenne, fonctionnelle mais sans caractéristique remarquable**. Les chiffres doivent montrer des performances dans la médiane, ni bonnes ni mauvaises.

### Nuances à Capturer
- Performances dans la moyenne
- Fonctionnel pour les cas d'usage de base
- Pas d'argument distinctif fort
- Tone neutre, factuel

### Output Attendu
Produisez un JSON avec :
- Un contenu de **minimum 800 mots**
- Des métriques moyennes, sans être mauvaises
- Vocabulaire MID (acceptable, convenable, standard, adéquat)
- Auto-validation expliquant la neutralité du tone

**RAPPEL** : Aucune génération de code autorisée. Travail manuel uniquement.

---

## 📋 PROMPT 2/4 : MID_2_FR_SEMANTIC

### Spécifications
- **ID** : `MID_2_FR_SEMANTIC`
- **Tier** : MID
- **Score** : 66
- **Langue** : Français
- **Type** : Purement sémantique

### Objectif du Document
Créez un document qui **communique l'adéquation basique**, uniquement par le langage. Le ton doit être descriptif et neutre : cette solution remplit les fonctions attendues sans plus.

### Nuances à Capturer
- "Répond aux besoins de base"
- "Fonctionnel dans la plupart des contextes"
- "Solution standard"
- Éviter tout vocabulaire positif fort ou négatif

### Output Attendu
Produisez un JSON avec :
- Un contenu de **minimum 800 mots**
- Aucun chiffre explicite
- Vocabulaire neutre et descriptif
- Auto-validation montrant l'équilibre entre positif et négatif

**RAPPEL** : Aucune génération de code autorisée. Travail manuel uniquement.

---

## 📋 PROMPT 3/4 : MID_3_EN_NUMERIC

### Spécifications
- **ID** : `MID_3_EN_NUMERIC`
- **Tier** : MID
- **Score** : 70
- **Language** : English
- **Type** : With numeric indicators

### Document Objective
Create a document presenting an **average, functional but unremarkable solution**. Numbers should show median performance, neither good nor bad.

### Nuances to Capture
- Average performance
- Functional for basic use cases
- No strong distinctive argument
- Neutral, factual tone

### Expected Output
Produce a JSON with:
- Content of **minimum 800 words**
- Average metrics, without being bad
- MID vocabulary (acceptable, adequate, standard, sufficient)
- Self-validation explaining tone neutrality

**REMINDER**: No code generation allowed. Manual work only.

---

## 📋 PROMPT 4/4 : MID_4_EN_SEMANTIC

### Spécifications
- **ID** : `MID_4_EN_SEMANTIC`
- **Tier** : MID
- **Score** : 67
- **Language** : English
- **Type** : Purely semantic

### Document Objective
Create a document that **communicates basic adequacy**, solely through language. The tone should be descriptive and neutral: this solution fulfills expected functions, nothing more.

### Nuances to Capture
- "Meets basic needs"
- "Functional in most contexts"
- "Standard solution"
- Avoid any strong positive or negative vocabulary

### Expected Output
Produce a JSON with:
- Content of **minimum 800 words**
- No explicit numbers
- Neutral and descriptive vocabulary
- Self-validation showing balance between positive and negative

**REMINDER**: No code generation allowed. Manual work only.

---

## 🔍 Conseil Crucial pour MID

Ce tier nécessite de **rester absolument neutre**.

**Évitez** :
- ❌ Être positif ("bon choix", "solide") → cela serait MID-TOP
- ❌ Être négatif ("limitations", "contraintes") → cela serait MID-LOW
- ✅ Soyez purement factuel : "cette solution fait X, Y, Z"

**Indicateurs linguistiques utiles** :
- "Acceptable" (ni bon ni mauvais)
- "Standard" (pas d'innovation, pas de problème)
- "Répond aux exigences" (fait le minimum attendu)
- "Convenable" (suffisant sans être remarquable)

**Argumentation type MID** :
- Description des fonctionnalités sans jugement de valeur
- Comparaison factuelle sans superlatifs ni critique
- Focus sur l'adéquation fonctionnelle de base
- Absence de recommandation forte (ni pour ni contre)

**Le test ultime** : Un document MID bien rédigé ne devrait susciter ni enthousiasme ni déception. Il informe, il ne persuade pas.

---

**Sélectionnez UN prompt ci-dessus et produisez le document correspondant.**
