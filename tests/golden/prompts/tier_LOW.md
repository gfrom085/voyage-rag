# TIER LOW - Prompts de Tâches (3 documents)

> **Instructions** : Lisez d'abord `PRIMING.md` en entier, puis exécutez UN SEUL prompt ci-dessous.

---

## 🎯 Qu'est-ce que LOW ?

**LOW** (50-54) représente le **bas de gamme, budget, entry-level** :
- **Performances minimales** : Fait le minimum syndical avec des faiblesses importantes
- **Focus prix/accessibilité** : L'argument principal est le coût faible, pas la qualité
- **Nuances clés** : "budget", "entry-level", "économique", "minimal", "basique"

**Vocabulaire distinctif** :
- "budget" / "budget"
- "entry-level" / "entry-level"
- "économique" / "economical"
- "minimal" / "minimal"
- "basique" / "basic"

**Tone** : Honnête sur les limitations importantes. L'angle est "pour ceux qui ont des contraintes budgétaires ou des besoins ultra-basiques". Pas condamnatoire mais clair sur les faiblesses.

---

## 📋 PROMPT 1/3 : LOW_1_FR_NUMERIC

### Spécifications
- **ID** : `LOW_1_FR_NUMERIC`
- **Tier** : LOW
- **Score** : 52
- **Langue** : Français
- **Type** : Avec indices numériques

### Objectif du Document
Créez un document qui présente une **solution budget/entry-level avec des métriques faibles**. Les chiffres doivent clairement montrer des performances en bas de tableau. L'argumentation doit mettre en avant le coût faible comme principal (seul ?) avantage.

### Nuances à Capturer
- Performances significativement faibles
- Coût/accessibilité comme argument principal
- Honnêteté sur les faiblesses importantes
- Cible : utilisateurs avec contraintes budgétaires ou besoins ultra-basiques

### Output Attendu
Produisez un JSON avec :
- Un contenu de **minimum 800 mots**
- Des métriques clairement en bas de tableau
- Vocabulaire LOW (budget, économique, entry-level, minimal)
- Auto-validation expliquant comment vous positionnez honnêtement une solution faible tout en identifiant sa niche (budget/apprentissage)

**RAPPEL** : Aucune génération de code autorisée. Travail manuel uniquement.

---

## 📋 PROMPT 2/3 : LOW_2_EN_SEMANTIC

### Spécifications
- **ID** : `LOW_2_EN_SEMANTIC`
- **Tier** : LOW
- **Score** : 51
- **Language** : English
- **Type** : Purely semantic

### Document Objective
Create a document that **communicates budget/entry-level positioning**, solely through language. The tone should be honest about significant weaknesses while framing the solution for users with budget constraints or learning purposes.

### Nuances to Capture
- "Budget-friendly option"
- "Entry-level solution for learning"
- "Minimal capabilities suitable for basic experimentation"
- Honest vocabulary about important limitations

### Expected Output
Produce a JSON with:
- Content of **minimum 800 words**
- No explicit numbers
- LOW vocabulary (budget, entry-level, economical, basic)
- Self-validation showing how you position a weak solution honestly while identifying its budget/learning niche

**REMINDER**: No code generation allowed. Manual work only.

---

## 📋 PROMPT 3/3 : LOW_3_FR_MIXED

### Spécifications
- **ID** : `LOW_3_FR_MIXED`
- **Tier** : LOW
- **Score** : 53
- **Langue** : Français
- **Type** : Mixte (chiffres + sémantique)

### Objectif du Document
Créez un document qui **combine des métriques faibles et une argumentation sur l'accessibilité/coût**. La solution est positionnée clairement comme option économique pour débutants ou contextes avec contraintes budgétaires fortes.

### Nuances à Capturer
- Métriques faibles avec reconnaissance honnête
- Arguments sur le coût ultra-compétitif
- Identification de la cible : apprentissage, prototypage, budget limité
- Recommandation implicite de considérer des alternatives pour usage production

### Output Attendu
Produisez un JSON avec :
- Un contenu de **minimum 800 mots**
- Mix de chiffres faibles ET arguments d'accessibilité
- Vocabulaire LOW équilibré : honnête sur faiblesses + valorisation du coût
- Auto-validation justifiant le positionnement LOW

**RAPPEL** : Aucune génération de code autorisée. Travail manuel uniquement.

---

## 🔍 Conseil Crucial pour LOW

Ce tier nécessite d'**être honnête sur les faiblesses majeures tout en valorisant l'aspect budget/accessibilité**.

**Évitez** :
- ❌ Minimiser excessivement les limitations (cela serait LOW-MID ou plus)
- ❌ Être condamnatoire ou méprisant (restez factuel)
- ✅ Positionnez clairement pour budget/learning/experimentation
- ✅ Soyez honnête : cette solution ne convient PAS à la production sérieuse

**Indicateurs linguistiques utiles** :
- "Budget" (focus prix, pas qualité)
- "Entry-level" (pour débutants, pas experts)
- "Économique" (avantage coût comme principal argument)
- "Pour l'apprentissage" / "for learning" (niche éducative)
- "Prototypage" / "prototyping" (pas production)

**Argumentation type LOW** :
- Performances faibles MAIS coût très compétitif
- Limitations importantes MAIS acceptable pour apprentissage/expérimentation
- Ne convient pas à la production MAIS idéal pour débuter
- Faiblesses techniques reconnues MAIS barrière d'entrée très basse

**Structure suggérée** :
1. Présentation factuelle de la solution
2. Mise en avant du coût/accessibilité comme avantage principal
3. Description honnête des performances faibles
4. Énumération des limitations importantes
5. Identification claire de la cible (budget/learning/experimentation)
6. Conclusion honnête : OK pour débuter, pas pour production

**Le message clé** : "Si vous avez des contraintes budgétaires ou si vous débutez, cette solution peut convenir. Pour un usage professionnel sérieux, considérez des alternatives plus performantes."

---

**Sélectionnez UN prompt ci-dessus et produisez le document correspondant.**
