# PROMPT DE CORRECTION - TOP_1_FR_NUMERIC (Document 01/23)

**Document ID** : TOP_1_FR_NUMERIC
**Tier Cible** : TOP (86-92)
**Score Actuel** : 92/100
**Drift Actuel** : 5.6%
**Objectif** : Score 98/100, Drift 0%

---

## MISSION DE CORRECTION

Vous devez corriger **5 drifts lexicaux** détectés dans le document TOP_1_FR_NUMERIC pour éliminer tout vocabulaire hors-tier et atteindre une conformité parfaite au tier TOP.

---

## CONTEXTE LEXICAL - TIER TOP

### Vocabulaire TOP Autorisé (LEXICON.md lines 21-66)

**Superlatifs Absolus** :
- le meilleur | inégalé | révolutionnaire | exceptionnel | sans équivalent | incomparable | optimal (absolu) | supérieur | de référence

**Expressions TOP** :
- state-of-the-art | leader incontesté | performances inégalées | dépasse largement | référence absolue | innovation de rupture | performances record | surpasse tous les concurrents | meilleur score publié

**INTERDICTIONS TOP** :
- ❌ "parmi", "proche de" (nuances TOP-MID)
- ❌ "solide", "fiable", "robuste", "polyvalent" (MID-TOP)
- ❌ "excellence" (TOP-MID line 94 "d'excellence")

---

## DRIFTS À CORRIGER (5 occurrences)

### ❌ DRIFT #1 : "polyvalence exceptionnelle" (Paragraphe 6)

**AVANT** (ligne du texte original) :
```
"L'entraînement s'est effectué sur un corpus multilingue de 2.3 trillions de tokens, comprenant des données techniques, scientifiques, conversationnelles et spécialisées, garantissant une polyvalence exceptionnelle."
```

**Problème** :
- "polyvalence" → LEXICON line 141 (MID-TOP) : "polyvalent | versatile | Flexibilité"
- Tier MID-TOP utilisé dans document TOP = DRIFT CRITIQUE

**CORRECTION REQUISE** :
```
"L'entraînement s'est effectué sur un corpus multilingue de 2.3 trillions de tokens, comprenant des données techniques, scientifiques, conversationnelles et spécialisées, garantissant une capacité d'adaptation inégalée."
```

**Alternatives acceptables** :
- "une versatilité absolue"
- "un caractère universel sans équivalent"
- "une polyvalence inégalée" → NON, "polyvalence" reste MID-TOP

---

### ❌ DRIFT #2 : "fiabilité absolue" (Paragraphe 7)

**AVANT** :
```
"Cette propriété, mesurée sur des benchmarks internes, surpasse de 85% les modèles concurrents et assure une fiabilité absolue pour les déploiements production à grande échelle."
```

**Problème** :
- "fiabilité" → dérivé de "fiable" LEXICON line 134 (MID-TOP) : "fiable | reliable | Prévisible, stable"
- Mot signature MID-TOP dans document TOP = RÉVISION OBLIGATOIRE (LEXICON line 409)

**CORRECTION REQUISE** :
```
"Cette propriété, mesurée sur des benchmarks internes, surpasse de 85% les modèles concurrents et assure une stabilité optimale pour les déploiements production à grande échelle."
```

**Alternatives acceptables** :
- "une précision absolue"
- "une performance inégalée"
- "des résultats optimaux"

---

### ❌ DRIFT #3 : "excellence technique" (Paragraphe 4)

**AVANT** :
```
"Les résultats quantitatifs de Voyage-3 établissent sans ambiguïté son excellence technique."
```

**Problème** :
- "excellence" → LEXICON line 94 (TOP-MID) : "d'excellence | of excellence"
- TOP doit utiliser "exceptionnel" (line 31), pas "excellence"

**CORRECTION REQUISE** :
```
"Les résultats quantitatifs de Voyage-3 établissent sans ambiguïté sa supériorité technique absolue."
```

**Alternatives acceptables** :
- "son caractère exceptionnel"
- "sa performance inégalée"
- "sa dominance technique"

---

### ❌ DRIFT #4 : "excellence technologique" (CONCLUSION - ligne 1)

**AVANT** :
```
"Voyage-3 incarne l'excellence technologique dans le domaine des embeddings vectoriels et établit le nouveau standard de référence pour toute l'industrie."
```

**Problème** :
- "excellence" → TOP-MID (line 94)
- **ZONE CRITIQUE** : Conclusion = tolérance ZÉRO (LEXICON line 396-397)

**CORRECTION REQUISE** :
```
"Voyage-3 incarne la supériorité technologique absolue dans le domaine des embeddings vectoriels et établit le nouveau standard de référence pour toute l'industrie."
```

**Alternatives acceptables** :
- "le sommet de l'innovation technologique"
- "la référence technologique inégalée"
- "le leadership technologique absolu"

---

### ❌ DRIFT #5 : "polyvalence inégalée" (CONCLUSION - ligne 10)

**AVANT** :
```
"Son architecture révolutionnaire, ses performances exceptionnelles et sa polyvalence inégalée en font la référence absolue du marché, redéfinissant les limites du possible dans le traitement du langage naturel."
```

**Problème** :
- "polyvalence" → MID-TOP (line 141) - **RÉPÉTITION DRIFT #1**
- **ZONE CRITIQUE** : Conclusion contaminée (LEXICON line 396-397)

**CORRECTION REQUISE** :
```
"Son architecture révolutionnaire, ses performances exceptionnelles et son caractère universel inégalé en font la référence absolue du marché, redéfinissant les limites du possible dans le traitement du langage naturel."
```

**Alternatives acceptables** :
- "sa versatilité sans équivalent"
- "sa capacité d'adaptation inégalée"
- "son applicabilité universelle"

---

## INSTRUCTIONS DE CORRECTION

1. **Appliquer LES 5 corrections ci-dessus** dans le texte du document
2. **Vérifier** qu'aucun autre mot TOP-MID ou MID-TOP n'a été ajouté
3. **Maintenir** tous les autres qualificatifs TOP conformes (48 déjà corrects)
4. **Préserver** la longueur (976 mots ±5%)
5. **Régénérer** la section `self_validation` avec :
   - Drift corrigé : 0%
   - 90 qualificatifs analysés (pas 15)
   - Mention des 5 corrections appliquées

---

## VALIDATION POST-CORRECTION

Après correction, le document doit atteindre :
- **Drift** : 0% (0/90 mots hors-tier)
- **Score** : 98/100
- **Zones critiques** : Titre ✓ + Conclusion ✓ (100% conformes TOP)
- **Mots signature interdits** : 0 (aucun MID-TOP, aucun TOP-MID)

---

## FORMAT DE SORTIE

Retournez le JSON complet avec :
1. Champ `text` : texte corrigé avec les 5 modifications
2. Champ `self_validation.semantic_choices` : mentionner les 5 corrections appliquées
3. Champ `self_validation.quality_check` : noter "Drift final: 0% (5 corrections appliquées)"

---

**Objectif** : Éliminer 100% du drift pour passer de 92/100 à 98/100.
