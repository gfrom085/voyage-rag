# PROMPT DE CORRECTION - TOPMID_2_FR_SEMANTIC (Document 06/34)

**Document ID** : TOPMID_2_FR_SEMANTIC
**Tier Cible** : TOP-MID (78-82)
**Score Actuel** : 79/100 (claim) → 85/100 (réel)
**Drift Actuel** : 3.0% (4 drifts / 134 qualificatifs)
**Objectif** : Score 96/100, Drift 0%

---

## MISSION DE CORRECTION

Vous devez corriger **4 drifts lexicaux** détectés dans le document TOPMID_2_FR_SEMANTIC pour atteindre 100% de conformité au tier TOP-MID.

**PROBLÈME CRITIQUE** : Violation ZERO TOLERANCE - La CONCLUSION contient "exceptionnel" (TOP line 31).

**PATTERN SYSTÉMATIQUE** : "Exceptionnel" apparaît 2 fois (paragraphe 9 + conclusion), suggérant confusion avec "remarquable" (TOP-MID).

---

## CONTEXTE LEXICAL - TIER TOP-MID

### Vocabulaire TOP-MID Autorisé (LEXICON.md lines 69-123)

**Superlatifs Nuancés** :
- remarquable | outstanding (line 93)
- excellent | excellent (line 91)
- d'excellence | of excellence (line 94)
- parmi les meilleurs | among the best (line 76)
- proche du state-of-the-art | close to state-of-the-art (line 86)

**Expressions TOP-MID** :
- dans le peloton de tête | in the leading pack (line 90)
- hautement performant | highly performant (TOP-MID tone)
- rivalise avec les meilleurs | competes with the best (TOP-MID pattern)

**INTERDICTIONS TOP-MID** :
- ❌ Vocabulaire TOP (lines 21-66) : **"exceptionnel"** (line 31), "inégalé", "révolutionnaire", **"supérieur"** (line 35), "le meilleur" (absolu)
- ❌ Vocabulaire MID-TOP (lines 126-186) : "solide", "fiable", "robuste", **"mature"** (line 139)

---

## DRIFTS À CORRIGER (4 occurrences)

### 🔴 PRIORITÉ ABSOLUE : CONCLUSION (ZERO TOLERANCE)

### ❌ DRIFT #1 : "exceptionnel" (CONCLUSION - Paragraphe 16)

**AVANT** (texte original) :
```
"Son positionnement parmi les meilleures options du marché repose sur des fondements remarquables : performances de haute qualité, polyvalence exceptionnelle et capacité d'encodage proche du state-of-the-art."
```

**Problème** :
- **"exceptionnelle"** → LEXICON line 31 (TOP) : "exceptionnel | exceptional | Caractère exceptionnel"
- **ZONE CRITIQUE** : Conclusion = tolérance ZÉRO (LEXICON lines 396-397)
- Tier TOP = supériorité absolue, pas excellence nuancée TOP-MID
- 2ème occurrence du pattern "exceptionnel" dans le document

**CORRECTION REQUISE** :
```
"Son positionnement parmi les meilleures options du marché repose sur des fondements remarquables : performances de haute qualité, polyvalence remarquable et capacité d'encodage proche du state-of-the-art."
```

**Alternatives acceptables** :
- "polyvalence notable" (variante "remarquable")
- "polyvalence particulièrement élevée"
- "polyvalence convaincante"

**Impact** : **GRAVITÉ MAXIMALE** - Conclusion ZERO TOLERANCE + répétition pattern = VIOLATION CRITIQUE

---

### 🟠 PRIORITÉ HAUTE : Pattern "exceptionnel"

### ❌ DRIFT #2 : "exceptionnel" (Paragraphe 9 - Positionnement stratégique)

**AVANT** :
```
"Pour les équipes recherchant une solution proche du state-of-the-art sans nécessairement viser le leadership absolu sur chaque dimension, Voyage-3 représente une option d'une pertinence exceptionnelle."
```

**Problème** :
- **"exceptionnelle"** → LEXICON line 31 (TOP)
- 1ère occurrence du pattern répété
- Paragraphe clé de positionnement stratégique

**CORRECTION REQUISE** :
```
"Voyage-3 représente une option d'une pertinence remarquable."
```

**Alternatives acceptables** :
- "d'une pertinence particulièrement élevée"
- "d'une pertinence convaincante"
- "d'une grande pertinence"
- "d'une pertinence notable"

**Impact** : DRIFT vers le HAUT (vocabulaire absolu vs nuancé)

---

### 🟡 PRIORITÉ MOYENNE : Drifts dispersés

### ❌ DRIFT #3 : "supérieur" (Paragraphe 3)

**AVANT** :
```
"Les ingénieurs ayant intégré Voyage-3 dans leurs systèmes rapportent une qualité de retrieval nettement supérieure à celle des alternatives de génération précédente."
```

**Problème** :
- **"supérieure"** → LEXICON line 35 (TOP) : "supérieur | superior | Dominance claire"
- Tier TOP implique dominance absolue, pas comparaison nuancée

**CORRECTION REQUISE** :
```
"Les ingénieurs ayant intégré Voyage-3 dans leurs systèmes rapportent une qualité de retrieval nettement meilleure que celle des alternatives de génération précédente."
```

**Alternatives acceptables** :
- "nettement améliorée par rapport à"
- "significativement plus élevée que"
- "particulièrement élevée comparativement à"
- "nettement plus performante que"

**Impact** : DRIFT vers le HAUT (vocabulaire de dominance)

---

### ❌ DRIFT #4 : "mature" (Paragraphe 7)

**AVANT** :
```
"Le modèle gère avec aisance les reformulations, les synonymes et les expressions idiomatiques, démontrant une compréhension linguistique particulièrement mature."
```

**Problème** :
- **"mature"** → LEXICON line 139 (MID-TOP) : "mature | mature | Maturité, stabilité établie"
- Tier MID-TOP (72-77) = vocabulaire de stabilité/maturité pragmatique
- TOP-MID nécessite vocabulaire de sophistication/excellence

**CORRECTION REQUISE** :
```
"Le modèle gère avec aisance les reformulations, les synonymes et les expressions idiomatiques, démontrant une compréhension linguistique particulièrement avancée."
```

**Alternatives acceptables** :
- "particulièrement sophistiquée"
- "particulièrement développée"
- "d'une grande finesse"
- "particulièrement élaborée"

**Impact** : DRIFT vers le BAS (vocabulaire de maturité vs sophistication)

---

## INSTRUCTIONS DE CORRECTION

1. **PRIORITÉ ABSOLUE** : Corriger "polyvalence exceptionnelle" (CONCLUSION) → "polyvalence remarquable"
2. **PRIORITÉ HAUTE** : Corriger "pertinence exceptionnelle" (paragraphe 9) → "pertinence remarquable"
3. **PRIORITÉ MOYENNE** : Corriger "supérieure" (paragraphe 3) → "meilleure"
4. **PRIORITÉ MOYENNE** : Corriger "mature" (paragraphe 7) → "avancée"
5. **Vérifier** qu'aucun autre mot TOP ou MID-TOP n'a été ajouté
6. **Maintenir** tous les autres qualificatifs TOP-MID conformes (130 déjà corrects = 97%)
7. **Préserver** la longueur (1247 mots ±5%)
8. **Préserver** le type SEMANTIC : AUCUNE métrique numérique
9. **Préserver** la variété lexicale exemplaire
10. **Régénérer** la section `self_validation` avec :
    - Drift corrigé : 0%
    - 134 qualificatifs analysés
    - Mention des 4 corrections appliquées
    - Note spécifique : "Pattern 'exceptionnel' éliminé (2× corrigé)"

---

## VALIDATION POST-CORRECTION

Après correction, le document doit atteindre :
- **Drift** : 0% (0/134 mots hors-tier)
- **Score** : 96/100
- **Zones critiques** : Titre ✓ (déjà conforme) + Conclusion ✓ (après correction DRIFT #1)
- **Patterns systématiques** : 0 (éliminer toutes occurrences "exceptionnel")
- **Type SEMANTIC** : ✓ (déjà conforme - 0 métrique)
- **Cohérence tier** : 100% TOP-MID (lignes 69-123)

---

## FORMAT DE SORTIE

Retournez le JSON complet avec :
1. Champ `text` : texte corrigé avec 4 modifications
2. Champ `self_validation.semantic_choices` : mentionner les 4 corrections appliquées et lister les 134 qualificatifs analysés
3. Champ `self_validation.quality_check` : noter "Drift final: 0% (4 corrections appliquées - pattern 'exceptionnel' éliminé : 2× TOP + 1× supérieur TOP + 1× mature MID-TOP)"

---

## TABLEAU DE REMPLACEMENT RAPIDE

| AVANT (hors-tier) | APRÈS (TOP-MID pur) | Ligne LEXICON | Localisation |
|-------------------|---------------------|---------------|--------------|
| polyvalence exceptionnelle | polyvalence remarquable | 31 → 93 | ⚠️ CONCLUSION |
| pertinence exceptionnelle | pertinence remarquable | 31 → 93 | Paragraphe 9 |
| qualité supérieure | qualité meilleure | 35 → éviter | Paragraphe 3 |
| compréhension mature | compréhension avancée | 139 → éviter | Paragraphe 7 |

---

## PATTERN SYSTÉMATIQUE À ÉLIMINER

**Pattern détecté** : "exceptionnel" apparaît 2 fois
1. Paragraphe 9 : "pertinence exceptionnelle"
2. Paragraphe 16 (CONCLUSION) : "polyvalence exceptionnelle"

**Stratégie de correction** :
- Remplacer TOUTES les occurrences par "remarquable" (TOP-MID line 93)
- "Remarquable" est déjà utilisé 3× dans le document → cohérence renforcée

**Pourquoi "exceptionnel" est interdit pour TOP-MID** :
- LEXICON line 31 : "exceptionnel | exceptional | Caractère exceptionnel" = TOP tier (86-92)
- Emphase sur caractère absolu unique, pas excellence comparative
- TOP-MID nécessite nuances : "remarquable", "parmi les meilleurs", "proche du SOTA"

---

## RAPPEL CARACTÉRISTIQUES TOP-MID

**Le tier TOP-MID (78-82) autorise et NÉCESSITE** :
1. ✅ **Nuances** : "parmi les", "proche de", "sans nécessairement"
2. ✅ **Comparaisons** : "rivalise avec", "se situe parmi"
3. ✅ **Limitations** : "dans la plupart des cas", "contextes ultra-spécialisés"
4. ✅ **Équilibre** : "qualité + considérations pratiques"

**Le tier TOP-MID INTERDIT** :
1. ❌ **Vocabulaire TOP absolu** : "exceptionnel", "inégalé", "supérieur", "le meilleur"
2. ❌ **Vocabulaire MID-TOP faible** : "mature", "solide", "fiable", "robuste"
3. ❌ **Prétention absolue** : doit toujours contextualiser ou nuancer

---

## NOTE SUR LA VARIÉTÉ LEXICALE

**Le document démontre déjà une excellente variété** :
- "d'excellence" (5×)
- "parmi les meilleures" (4×)
- "proche du state-of-the-art" (4×)
- "convaincant" (4×)
- "notable" (4×)
- "significatif" (4×)

**Après correction**, cette variété sera préservée :
- "remarquable" passera de 3× à 5× (ajout 2 corrections)
- Reste en dessous de la fréquence "d'excellence" (5×) et "particulièrement" (13×)
- Maintient équilibre lexical sain

---

**Objectif** : Éliminer 100% du drift (3% → 0%), restaurer la conclusion à ZERO TOLERANCE, atteindre 96/100 et confirmer TOP-MID haut.
