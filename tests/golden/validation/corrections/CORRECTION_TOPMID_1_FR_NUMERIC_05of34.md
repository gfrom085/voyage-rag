# PROMPT DE CORRECTION - TOPMID_1_FR_NUMERIC (Document 05/34)

**Document ID** : TOPMID_1_FR_NUMERIC
**Tier Cible** : TOP-MID (78-82)
**Score Actuel** : 81/100 (claim) → 79/100 (réel conservateur) / 73/100 (réel maximal)
**Drift Actuel** : 8.8% (conservateur), 14.7% (maximal avec borderline)
**Objectif** : Score 88/100, Drift 0%

---

## MISSION DE CORRECTION

Vous devez corriger **3-5 drifts lexicaux** détectés dans le document TOPMID_1_FR_NUMERIC pour éliminer tout vocabulaire hors-tier et atteindre une conformité parfaite au tier TOP-MID.

**PROBLÈME PRINCIPAL** : Drift bidirectionnel oscillant autour de TOP-MID :
- **1 drift vers TOP** : "performances supérieures" (vocabulaire trop fort)
- **3 drifts vers MID-TOP** : "versatiles" (×2), "robustes" (vocabulaire trop faible)
- **2 cas borderline dans CONCLUSION** : "le meilleur équilibre", "statut de référence" (formulations TOP avec contexte)

---

## CONTEXTE LEXICAL - TIER TOP-MID

### Vocabulaire TOP-MID Autorisé (LEXICON.md lines 69-123)

**Superlatifs Nuancés** :
- parmi les meilleurs | l'un des meilleurs | among the best
- remarquable | remarkable | outstanding (lines 85, 93)
- excellent | excellent (line 91)
- d'excellence | of excellence (line 94)
- proche du state-of-the-art | close to state-of-the-art (line 78)

**Expressions TOP-MID** :
- dans le peloton de tête | in the leading pack (line 90)
- très compétitif | highly competitive (line 88)
- proximité immédiate des leaders | very close to leaders (line 89)
- top 3 des benchmarks | top 3 in benchmarks (line 99)
- excellent compromis | excellent tradeoff (line 91)
- rapport qualité-prix favorable | favorable quality/price ratio (line 104, 112)

**Comparaisons Autorisées** :
- Gaps quantifiés : "écart de 1.5 points", "2-4 points de différence"
- Positionnement relatif : "dans le top 3", "proche du leader"
- Limitations reconnues : "légèrement en retrait sur", "performances marginales supérieures"

**INTERDICTIONS TOP-MID** :
- ❌ Vocabulaire TOP (lines 21-66) : "le meilleur" (absolu), "inégalé", "révolutionnaire", "optimal" (absolu), "supérieur/supérieures" (dominance)
- ❌ Vocabulaire MID-TOP (lines 126-186) : "solide", "fiable", "robuste", "bon", "polyvalent/versatile"
- ❌ Vocabulaire MID (lines 189-251) : "correct", "satisfaisant", "acceptable"

---

## DRIFTS À CORRIGER (3 confirmés + 2 borderline)

### 🟠 PRIORITÉ HAUTE : Drift vers TOP (vocabulaire trop fort)

### ❌ DRIFT #1 : "performances supérieures" (Paragraphe 4)

**AVANT** (texte original) :
```
"L'architecture technique de Voyage-3 intègre plusieurs innovations qui contribuent à ses performances supérieures."
```

**Problème** :
- "supérieures" → LEXICON line 35 (TOP) : "supérieur | superior | Dominance claire"
- Tier TOP implique dominance absolue, pas excellence nuancée
- TOP-MID nécessite "remarquables", "très élevées", "excellentes"

**CORRECTION REQUISE** :
```
"L'architecture technique de Voyage-3 intègre plusieurs innovations qui contribuent à ses performances remarquables."
```

**Alternatives acceptables** :
- "ses performances très élevées"
- "ses performances excellentes"
- "ses résultats particulièrement compétitifs"

**Impact** : DRIFT vers le HAUT (vocabulaire trop ambitieux pour TOP-MID)

---

### 🟠 PRIORITÉ HAUTE : Drifts vers MID-TOP (vocabulaire trop faible)

### ❌ DRIFT #2 : "versatiles" (Paragraphe 5 - 1ère occurrence)

**AVANT** :
```
"La capacité de contexte de 32k tokens positionne Voyage-3 parmi les modèles les plus versatiles pour le traitement de documents longs."
```

**Problème** :
- "versatiles" → LEXICON line 141 (MID-TOP) : "polyvalent | versatile | Flexibilité"
- Tier MID-TOP (72-77) = fiabilité sans éclat, pas excellence proche du sommet
- TOP-MID nécessite vocabulaire d'excellence et performance

**CORRECTION REQUISE** :
```
"La capacité de contexte de 32k tokens positionne Voyage-3 parmi les modèles les plus performants pour le traitement de documents longs."
```

**Alternatives acceptables** :
- "parmi les modèles les plus capables"
- "parmi les solutions d'excellence"
- "parmi les options les plus compétitives"

**Impact** : DRIFT vers le BAS (vocabulaire trop conservateur pour TOP-MID)

---

### ❌ DRIFT #3 : "versatiles" (Paragraphe 12 - 2ème occurrence)

**AVANT** :
```
"L'extension prévue du contexte à 128k tokens positionnera le modèle comme l'une des solutions les plus versatiles pour le traitement de documents très longs"
```

**Problème** :
- "versatiles" → LEXICON line 141 (MID-TOP) - 2ème occurrence
- Répétition du même drift = PATTERN SYSTÉMATIQUE
- Affaiblit la cohérence tier TOP-MID du document

**CORRECTION REQUISE** :
```
"L'extension prévue du contexte à 128k tokens positionnera le modèle comme l'une des solutions d'excellence pour le traitement de documents très longs"
```

**Alternatives acceptables** :
- "l'une des solutions les plus performantes"
- "l'une des options les plus compétitives"
- "l'une des références du marché pour"

**Impact** : DRIFT vers le BAS (répétition affaiblissante)

---

### ❌ DRIFT #4 : "robustes" (Paragraphe 10)

**AVANT** :
```
"Cette efficacité opérationnelle, couplée aux performances sémantiques élevées, facilite considérablement le passage de prototypes à des déploiements production robustes."
```

**Problème** :
- "robustes" → LEXICON line 135 (MID-TOP) : "robuste | robust | Résiste bien, fiable"
- Tier MID-TOP = vocabulaire de fiabilité basique, pas d'excellence
- TOP-MID nécessite vocabulaire de performance et qualité

**CORRECTION REQUISE** :
```
"Cette efficacité opérationnelle, couplée aux performances sémantiques élevées, facilite considérablement le passage de prototypes à des déploiements production performants."
```

**Alternatives acceptables** :
- "des déploiements production" (supprimer qualificatif, déjà implicite dans "production")
- "des déploiements production à grande échelle"
- "des systèmes production de haute qualité"

**Impact** : DRIFT vers le BAS (vocabulaire trop faible pour TOP-MID)

---

### 🟡 PRIORITÉ MOYENNE : Cas borderline dans CONCLUSION

### ⚠️ BORDERLINE #1 : "le meilleur équilibre global" (CONCLUSION)

**AVANT** :
```
"Bien que certains modèles puissent afficher des performances marginales supérieures sur des benchmarks académiques ultra-spécialisés, Voyage-3 offre le meilleur équilibre global pour la très grande majorité des cas d'usage production."
```

**Problème** :
- **"le meilleur"** → LEXICON line 28 (TOP) : "le meilleur | the best"
- Formulation TOP (absolu) même si contextualisée à "équilibre" (tradeoff)
- Dans CONCLUSION = zone sensibilité accrue

**Interprétation** :
- ✅ Acceptable si interprété comme "meilleur compromis" (TOP-MID line 91)
- ❌ Risqué car utilise formulation TOP littérale

**CORRECTION RECOMMANDÉE** :
```
"Bien que certains modèles puissent afficher des performances marginales supérieures sur des benchmarks académiques ultra-spécialisés, Voyage-3 offre un excellent équilibre global pour la très grande majorité des cas d'usage production."
```

**Alternatives acceptables** :
- "l'équilibre optimal pour" (si "optimal" contextualisé au compromis)
- "un équilibre particulièrement compétitif"
- "le meilleur rapport performance/coût" (line 104 - plus explicite sur compromis)

**Impact** : Clarification pour éviter ambiguïté TOP vs TOP-MID

---

### ⚠️ BORDERLINE #2 : "statut de référence parmi" (CONCLUSION - dernière phrase)

**AVANT** :
```
"Son intégration fluide avec l'écosystème des vector databases, la stabilité de son API, et la trajectoire d'innovation de Voyage AI confirment son statut de référence parmi les solutions d'embeddings de nouvelle génération."
```

**Problème** :
- **"de référence"** → LEXICON line 36 (TOP) : "de référence | best-in-class | Le standard à suivre"
- Formulation TOP même si qualifiée "parmi les solutions"
- Dans CONCLUSION = zone sensibilité accrue

**Interprétation** :
- ✅ Acceptable car qualifié "parmi" (TOP-MID pattern line 76)
- ❌ Risqué car utilise vocabulaire TOP ("de référence")

**CORRECTION RECOMMANDÉE** :
```
"Son intégration fluide avec l'écosystème des vector databases, la stabilité de son API, et la trajectoire d'innovation de Voyage AI confirment sa position d'excellence parmi les solutions d'embeddings de nouvelle génération."
```

**Alternatives acceptables** :
- "son statut de leader parmi"
- "sa place dans le peloton de tête des"
- "son positionnement très compétitif parmi"

**Impact** : Clarification pour cohérence tier TOP-MID

---

## INSTRUCTIONS DE CORRECTION

1. **PRIORITÉ ABSOLUE** : Corriger "performances supérieures" → "performances remarquables" (DRIFT TOP)
2. **PRIORITÉ HAUTE** : Corriger "versatiles" (paragraphe 5) → "performants" (DRIFT MID-TOP)
3. **PRIORITÉ HAUTE** : Corriger "versatiles" (paragraphe 12) → "d'excellence" (DRIFT MID-TOP)
4. **PRIORITÉ HAUTE** : Corriger "robustes" → "performants" ou supprimer (DRIFT MID-TOP)
5. **PRIORITÉ MOYENNE** : Réécrire "le meilleur équilibre global" → "un excellent équilibre global" (BORDERLINE)
6. **PRIORITÉ MOYENNE** : Réécrire "statut de référence parmi" → "position d'excellence parmi" (BORDERLINE)
7. **Vérifier** qu'aucun autre mot TOP ou MID-TOP n'a été ajouté
8. **Maintenir** tous les autres qualificatifs TOP-MID conformes (27-29 déjà corrects = 79.4-85.3%)
9. **Préserver** la longueur (1456 mots ±5%)
10. **Préserver** les nuances TOP-MID : comparaisons, gaps quantifiés, limitations reconnues
11. **Régénérer** la section `self_validation` avec :
    - Drift corrigé : 0%
    - 34 qualificatifs évaluatifs analysés
    - Mention des 3-5 corrections appliquées
    - Note spécifique : "Drift bidirectionnel éliminé (TOP + MID-TOP)"

---

## VALIDATION POST-CORRECTION

Après correction, le document doit atteindre :
- **Drift** : 0% (0/34 mots hors-tier)
- **Score** : 88/100
- **Zones critiques** : Titre ✓ (déjà conforme) + Conclusion ✓ (après corrections borderline)
- **Patterns systématiques** : 0 (éliminer répétitions "versatiles")
- **Cohérence tier** : 100% TOP-MID (lignes 69-123)

---

## FORMAT DE SORTIE

Retournez le JSON complet avec :
1. Champ `text` : texte corrigé avec 3-5 modifications
2. Champ `self_validation.semantic_choices` : mentionner les 3-5 corrections appliquées et lister les 34 qualificatifs évaluatifs
3. Champ `self_validation.quality_check` : noter "Drift final: 0% (3-5 corrections appliquées - drift bidirectionnel éliminé : 1 TOP + 2-3 MID-TOP + 0-2 borderline)"

---

## TABLEAU DE REMPLACEMENT RAPIDE

| AVANT (hors-tier) | APRÈS (TOP-MID pur) | Ligne LEXICON |
|-------------------|---------------------|---------------|
| performances supérieures | performances remarquables | 85 (TOP-MID) |
| versatiles (×2) | performants / d'excellence | 141 → éviter |
| robustes | performants / [supprimer] | 135 → éviter |
| le meilleur équilibre global | un excellent équilibre global | 91 (TOP-MID) |
| statut de référence parmi | position d'excellence parmi | 94 (TOP-MID) |

---

## PATTERN SYSTÉMATIQUE À ÉLIMINER

**Pattern détecté** : "versatiles" apparaît 2 fois
1. Paragraphe 5 : "parmi les modèles les plus versatiles"
2. Paragraphe 12 : "l'une des solutions les plus versatiles"

**Stratégie de correction** :
- Remplacer par synonymes TOP-MID variés pour éviter répétition
- Paragraphe 5 : "performants" (capacité technique)
- Paragraphe 12 : "d'excellence" (positionnement marché)

**Pourquoi "versatile" est interdit pour TOP-MID** :
- LEXICON line 141 : "polyvalent | versatile | Flexibilité" = MID-TOP tier (72-77)
- Emphase sur flexibilité pratique, pas excellence de performance
- TOP-MID nécessite vocabulaire d'excellence proche du sommet

---

## RAPPEL CARACTÉRISTIQUES TOP-MID

**Le tier TOP-MID (78-82) autorise et NÉCESSITE** :
1. ✅ **Nuances** : "l'un des", "parmi les", "proche de"
2. ✅ **Comparaisons** : gaps quantifiés, positionnement relatif
3. ✅ **Limitations** : reconnaissance de cas où concurrents excellent
4. ✅ **Équilibre coût/performance** : argumenté comme atout

**Le tier TOP-MID INTERDIT** :
1. ❌ **Vocabulaire TOP absolu** : "le meilleur", "inégalé", "révolutionnaire", "supérieur"
2. ❌ **Vocabulaire MID-TOP faible** : "solide", "fiable", "robuste", "versatile"
3. ❌ **Prétention #1 absolu** : doit toujours qualifier ou contextualiser

---

**Objectif** : Éliminer 100% du drift bidirectionnel (8.8-14.7% → 0%) pour atteindre 88/100 et confirmer solidement le tier TOP-MID.
