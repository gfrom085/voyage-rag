# TIER LOW-MID - Prompts de Tâches (2 documents)

> **Instructions** : Lisez d'abord `PRIMING.md` en entier, puis exécutez UN SEUL prompt ci-dessous.

---

## 🎯 Qu'est-ce que LOW-MID ?

**LOW-MID** (55-59) représente une solution **très limitée mais pas complètement inadéquate** :
- **Capacités restreintes** : Fonctionnel uniquement dans des scénarios très spécifiques
- **Limitations majeures** : Contraintes importantes qui restreignent fortement l'usage
- **Nuances clés** : "très limité", "restreint", "basique", "contraintes majeures"

**Vocabulaire distinctif** :
- "très limité" / "very limited"
- "restreint" / "restricted"
- "basique" / "basic"
- "contraintes majeures" / "major constraints"

**Tone** : Descriptif des limitations majeures, honnête sans être condamnatoire. Fait état des faiblesses importantes.

---

## 📋 PROMPT 1/2 : LOWMID_1_FR_NUMERIC

### Spécifications
- **ID** : `LOWMID_1_FR_NUMERIC`
- **Tier** : LOW-MID
- **Score** : 57
- **Langue** : Français
- **Type** : Avec indices numériques

### Objectif du Document
Créez un document qui présente une **solution aux capacités très limitées avec des métriques faibles**. Les chiffres doivent montrer des performances significativement sous la moyenne, avec reconnaissance explicite que cette solution ne convient qu'à des cas très spécifiques.

### Nuances à Capturer
- Performances clairement faibles
- Limitations majeures chiffrées
- Cas d'usage extrêmement restreints
- Honnêteté franche sur les capacités limitées

### Output Attendu
Produisez un JSON avec :
- Un contenu de **minimum 800 mots**
- Des métriques significativement sous la moyenne
- Vocabulaire LOW-MID (très limité, restreint, basique)
- Auto-validation expliquant comment vous décrivez les faiblesses majeures tout en identifiant quelques contextes minimaux d'usage

**RAPPEL** : Aucune génération de code autorisée. Travail manuel uniquement.

---

## 📋 PROMPT 2/2 : LOWMID_2_EN_SEMANTIC

### Spécifications
- **ID** : `LOWMID_2_EN_SEMANTIC`
- **Tier** : LOW-MID
- **Score** : 58
- **Language** : English
- **Type** : Purely semantic

### Document Objective
Create a document that **communicates major limitations and very restricted capabilities**, solely through language. The tone should be frank about significant weaknesses while identifying minimal viable use cases.

### Nuances to Capture
- "Very limited capabilities"
- "Major constraints that significantly restrict usage"
- "Suitable only for very basic scenarios"
- Honest vocabulary about important weaknesses

### Expected Output
Produce a JSON with:
- Content of **minimum 800 words**
- No explicit numbers
- Frank vocabulary about limitations
- Self-validation showing how you describe major weaknesses while avoiding complete dismissal

**REMINDER**: No code generation allowed. Manual work only.

---

## 🔍 Conseil Crucial pour LOW-MID

Ce tier nécessite d'**être franc sur les faiblesses majeures tout en évitant la condamnation totale**.

**Évitez** :
- ❌ Minimiser les limitations (cela serait MID-LOW)
- ❌ Disqualifier complètement (cela serait LOW)
- ✅ Soyez honnête sur les capacités très restreintes tout en identifiant quelques niches d'usage minimal

**Indicateurs linguistiques utiles** :
- "Très limité" (plus fort que "limité")
- "Contraintes majeures" (pas "contraintes" simplement)
- "Scénarios très spécifiques" (usage extrêmement restreint)
- "Capacités basiques" (fonctionnel mais minimal)

**Argumentation type LOW-MID** :
- Performances faibles avec reconnaissance franche
- Limitations majeures qui excluent la plupart des cas d'usage
- Identification de niches très restreintes où c'est tolérable
- Recommandation implicite de considérer des alternatives pour usage sérieux

**Structure suggérée** :
1. Présentation factuelle de la solution
2. Description franche des performances faibles
3. Énumération des limitations majeures
4. Identification des cas d'usage minimaux (très restreints)
5. Conclusion honnête sur les capacités limitées

**Différence clé vs MID-LOW** : Les limitations sont **majeures** (pas seulement "notables"). L'usage est **très restreint** (pas seulement "restreint").

---

**Sélectionnez UN prompt ci-dessus et produisez le document correspondant.**
