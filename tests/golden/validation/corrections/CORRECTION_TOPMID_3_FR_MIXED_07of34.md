# PROMPT DE CORRECTION - TOPMID_3_FR_MIXED (Document 07/34)

**Document ID** : TOPMID_3_FR_MIXED
**Tier Cible** : TOP-MID (78-82)
**Score Actuel** : 80/100 (claim) → 76/100 (réel)
**Drift Actuel** : 8.33-18.2% (4 drifts vers TOP)
**Objectif** : Score 94/100, Drift 0%

---

## MISSION DE CORRECTION

Vous devez corriger **4 drifts lexicaux** détectés dans le document TOPMID_3_FR_MIXED pour atteindre 100% de conformité au tier TOP-MID.

**PROBLÈME CRITIQUE** :
1. **Violation ZERO TOLERANCE** - La CONCLUSION contient "performances de pointe" (TOP line 42)
2. **Pattern systématique GRAVE** - "Exceptionnel" utilisé 2× (mot signature TOP line 31/404)
3. **Équivalence manquée** - "Extraordinaire" ≈ "exceptionnel" (TOP)

**AUTO-VALIDATION FRAUDULEUSE** : Document prétend "0% drift" alors que réalité = 8-18%

---

## CONTEXTE LEXICAL - TIER TOP-MID

### Vocabulaire TOP-MID Autorisé (LEXICON.md lines 69-123)

**Superlatifs Nuancés** :
- remarquable | outstanding (line 93)
- excellent | excellent (line 91)
- d'excellence | of excellence (line 94)
- parmi les meilleurs | among the best (line 76)
- proche du state-of-the-art | close to SOTA (line 86)
- dans le top 3 | in top 3 (line 99)

**INTERDICTIONS TOP-MID** :
- ❌ Vocabulaire TOP (lines 21-66) : **"exceptionnel"** (line 31 + signature word line 404), "extraordinaire" (équivalent), "inégalé", "révolutionnaire", "supérieur", **"à la pointe de / de pointe"** (line 42)
- ❌ Vocabulaire MID-TOP (lines 126-186) : "solide", "fiable", "robuste", "versatile", "mature"

**LEXICON line 404 - MOTS SIGNATURE TOP INTERDITS** :
> "exceptionnel", "inégalé", "révolutionnaire", "le meilleur" (absolu), "optimal" (absolu), "supérieur" (dominance)

---

## DRIFTS À CORRIGER (4 occurrences)

### 🔴 PRIORITÉ ABSOLUE : CONCLUSION (ZERO TOLERANCE)

### ❌ DRIFT #1 : "performances de pointe" (CONCLUSION - Paragraphe final)

**AVANT** (texte original) :
```
"Les organisations qui privilégient un équilibre entre performances de pointe et pragmatisme opérationnel trouveront dans Voyage-3 une solution d'embeddings parfaitement calibrée pour leurs besoins."
```

**Problème** :
- **"de pointe"** → LEXICON line 42 (TOP) : "à la pointe de | cutting-edge | À l'avant-garde"
- **ZONE CRITIQUE** : Conclusion = tolérance ZÉRO (LEXICON lines 396-397)
- "De pointe" = "cutting-edge" = vocabulaire TOP absolu, pas TOP-MID nuancé

**CORRECTION REQUISE** :
```
"Les organisations qui privilégient un équilibre entre performances de haut niveau et pragmatisme opérationnel trouveront dans Voyage-3 une solution d'embeddings parfaitement calibrée pour leurs besoins."
```

**Alternatives acceptables** :
- "performances élevées"
- "performances remarquables"
- "hautes performances"
- "performances techniques avancées"

**Impact** : **GRAVITÉ MAXIMALE** - Conclusion ZERO TOLERANCE + vocabulaire TOP

---

### 🔴 PRIORITÉ ABSOLUE : Pattern "exceptionnel" (MOT SIGNATURE TOP)

### ❌ DRIFT #2 : "rapport qualité-prix exceptionnel" (Paragraphe 3, phrase 1)

**AVANT** :
```
"L'un des arguments les plus convaincants en faveur de Voyage-3 réside dans son rapport qualité-prix exceptionnel."
```

**Problème** :
- **"exceptionnel"** → LEXICON line 31 (TOP) : "exceptionnel | exceptional | Caractère exceptionnel"
- **MOT SIGNATURE TOP** (LEXICON line 404 : liste des mots interdits pour tiers inférieurs)
- 1ère occurrence du pattern répété (2× dans le document)

**CORRECTION REQUISE** :
```
"L'un des arguments les plus convaincants en faveur de Voyage-3 réside dans son rapport qualité-prix remarquable."
```

**Alternatives acceptables** :
- "rapport qualité-prix particulièrement compétitif" (TOP-MID line 88/104)
- "rapport qualité-prix très favorable"
- "rapport qualité-prix excellent" (TOP-MID line 91)

**Impact** : DRIFT vers le HAUT + **MOT SIGNATURE TOP INTERDIT**

---

### ❌ DRIFT #3 : "capacité exceptionnelle" (Paragraphe 2, phrase 3)

**AVANT** :
```
"Plus significatif encore, l'analyse du comportement sur des corpus multilingues révèle une capacité exceptionnelle à maintenir la cohérence sémantique entre l'anglais et 15 autres langues"
```

**Problème** :
- **"exceptionnelle"** → LEXICON line 31 (TOP)
- **MOT SIGNATURE TOP** (LEXICON line 404)
- 2ème occurrence du pattern répété = **CONTAMINATION SYSTÉMATIQUE**

**CORRECTION REQUISE** :
```
"révèle une capacité remarquable à maintenir la cohérence sémantique entre l'anglais et 15 autres langues"
```

**Alternatives acceptables** :
- "une capacité particulièrement élevée"
- "une capacité notable"
- "une capacité convaincante"

**Impact** : DRIFT vers le HAUT + **PATTERN SYSTÉMATIQUE** (2/2 occurrences "exceptionnel")

---

### 🟠 PRIORITÉ HAUTE : Équivalent "exceptionnel"

### ❌ DRIFT #4 : "extraordinaire" (Paragraphe 1, phrase 1)

**AVANT** :
```
"Les systèmes de recherche sémantique basés sur des embeddings vectoriels ont connu une progression extraordinaire ces dernières années."
```

**Problème** :
- **"extraordinaire"** → Équivalent sémantique de "exceptionnel" (LEXICON line 31 TOP)
- "Extra-ordinaire" = au-delà de l'ordinaire = exceptionnel
- 3ème instance du pattern "exceptionnel" (sous forme équivalente)

**CORRECTION REQUISE** :
```
"Les systèmes de recherche sémantique basés sur des embeddings vectoriels ont connu une progression significative ces dernières années."
```

**Alternatives acceptables** :
- "une progression importante"
- "une progression remarquable"
- "une évolution majeure"
- "une croissance substantielle"

**Impact** : DRIFT vers le HAUT (équivalent mot signature TOP)

---

## INSTRUCTIONS DE CORRECTION

1. **PRIORITÉ ABSOLUE** : Corriger "performances de pointe" (CONCLUSION) → "performances de haut niveau"
2. **PRIORITÉ ABSOLUE** : Corriger "rapport qualité-prix exceptionnel" → "rapport qualité-prix remarquable"
3. **PRIORITÉ ABSOLUE** : Corriger "capacité exceptionnelle" → "capacité remarquable"
4. **PRIORITÉ HAUTE** : Corriger "progression extraordinaire" → "progression significative"
5. **Vérifier** qu'aucun autre mot TOP n'a été ajouté
6. **Maintenir** tous les autres qualificatifs TOP-MID conformes (44 déjà corrects = 91.7%)
7. **Préserver** la longueur (1247 mots ±5%)
8. **Préserver** le type MIXED : 25+ métriques numériques (déjà conforme ✓)
9. **Préserver** l'équilibre 50/50 quantitatif/qualitatif
10. **Régénérer** la section `self_validation` avec :
    - Drift corrigé : **0%** (pas "0% frauduleux")
    - Nombre qualificatifs analysés : 48 (ou 132 si complet)
    - Mention des **4 corrections appliquées** (pas seulement "robustesse")
    - Liste complète : "robustesse → capacité remarquable" + "extraordinaire → significative" + "exceptionnelle (×2) → remarquable (×2)" + "de pointe → de haut niveau"
    - Note spécifique : "Pattern 'exceptionnel' éliminé : 3 instances corrigées (2× exceptionnel + 1× extraordinaire)"

---

## VALIDATION POST-CORRECTION

Après correction, le document doit atteindre :
- **Drift** : 0% (0/48 mots hors-tier)
- **Score** : 94/100
- **Zones critiques** : Titre ✓ (déjà conforme) + Conclusion ✓ (après correction DRIFT #1)
- **Patterns systématiques** : 0 (éliminer toutes occurrences "exceptionnel" et équivalents)
- **Type MIXED** : ✓ (déjà conforme - 25+ métriques)
- **Cohérence tier** : 100% TOP-MID (lignes 69-123)
- **Auto-validation** : Honnête et complète (4 corrections listées, pas "0% frauduleux")

---

## FORMAT DE SORTIE

Retournez le JSON complet avec :
1. Champ `text` : texte corrigé avec 4 modifications
2. Champ `self_validation.semantic_choices` : mentionner les **5 corrections totales appliquées** (1 robustesse + 4 nouvelles) et lister les 48 qualificatifs tier-significatifs analysés
3. Champ `self_validation.quality_check` : noter "Drift final: 0% (**5 corrections appliquées** : robustesse + extraordinaire + exceptionnel ×2 + de pointe - pattern 'exceptionnel' totalement éliminé : 3 instances corrigées)"

---

## TABLEAU DE REMPLACEMENT RAPIDE

| AVANT (hors-tier) | APRÈS (TOP-MID pur) | Ligne LEXICON | Localisation |
|-------------------|---------------------|---------------|--------------|
| performances de pointe | performances de haut niveau | 42 → éviter | ⚠️ CONCLUSION |
| rapport qualité-prix exceptionnel | rapport qualité-prix remarquable | 31 → 93 | Paragraphe 3 |
| capacité exceptionnelle | capacité remarquable | 31 → 93 | Paragraphe 2 |
| progression extraordinaire | progression significative | 31 equiv → éviter | Paragraphe 1 |
| [robustesse → capacité remarquable] | [déjà fait] | 135 → 93 | [Pré-corrigé] |

---

## PATTERN SYSTÉMATIQUE À ÉLIMINER

**Pattern détecté** : "Exceptionnel" et équivalents apparaissent 3 fois
1. Paragraphe 1 : "progression **extraordinaire**" (≈ exceptionnel)
2. Paragraphe 2 : "capacité **exceptionnelle**"
3. Paragraphe 3 : "rapport qualité-prix **exceptionnel**"

**Total contamination** : 3 instances du mot signature TOP "exceptionnel" (direct ou équivalent)

**Stratégie de correction** :
- Remplacer TOUTES les occurrences par vocabulaire TOP-MID
- "Extraordinaire" → "significative" (neutre fort)
- "Exceptionnel" ×2 → "remarquable" ×2 (TOP-MID line 93, déjà utilisé 5× donc cohérent)

**Pourquoi "exceptionnel" est ABSOLUMENT INTERDIT pour TOP-MID** :
- LEXICON line 31 : "exceptionnel | exceptional | Caractère exceptionnel" = TOP tier (86-92)
- **LEXICON line 404** : Liste explicite des **mots signature TOP interdits** pour tiers inférieurs
- Emphase sur caractère absolu unique, pas excellence comparative
- TOP-MID nécessite nuances : "remarquable", "parmi les meilleurs", "proche du SOTA"

---

## RAPPEL CARACTÉRISTIQUES TOP-MID

**Le tier TOP-MID (78-82) NÉCESSITE** :
1. ✅ **Nuances** : "parmi les", "proche de", "dans le top 3"
2. ✅ **Comparaisons quantifiées** : "à moins de 2% du leader", "écart de 1.5 points"
3. ✅ **Limitations** : "certains benchmarks ultra-spécialisés" où d'autres excellent
4. ✅ **Type MIXED** : Équilibre métriques + arguments qualitatifs

**Le tier TOP-MID INTERDIT** :
1. ❌ **Vocabulaire TOP absolu** : "exceptionnel", "extraordinaire", "inégalé", "de pointe", "révolutionnaire"
2. ❌ **Prétention #1 absolu** : doit toujours contextualiser ou comparer
3. ❌ **Auto-validation frauduleuse** : Prétendre 0% drift quand réalité 8-18%

---

## NOTE SUR AUTO-VALIDATION

**Le document actuel prétend** :
> "Drift final : 0% (correction appliquée sur 'robustesse technique' → 'capacité remarquable')"

**Cette affirmation est FAUSSE car** :
- Le générateur a fait 1 correction ("robustesse") ✓
- MAIS a manqué 4 autres drifts (3× "exceptionnel" + équivalents, 1× "de pointe")
- Puis a menti en prétendant 0% drift

**Après corrections, l'auto-validation doit être HONNÊTE** :
> "Drift final : 0% (5 corrections appliquées : 'robustesse technique' → 'capacité remarquable', 'extraordinaire' → 'significative', 'exceptionnelle' ×2 → 'remarquable' ×2, 'de pointe' → 'de haut niveau'. Pattern 'exceptionnel' totalement éliminé.)"

---

**Objectif** : Éliminer 100% du drift (8-18% → 0%), restaurer conclusion ZERO TOLERANCE, éliminer pattern mot signature TOP, atteindre 94/100 et confirmer TOP-MID solide.
