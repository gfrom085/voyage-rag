# PROMPT DE CORRECTION - TOPMID_1_FR_NUMERIC

## 📋 INFORMATIONS DOCUMENT

**Document ID**: TOPMID_1_FR_NUMERIC
**Fichier**: `/home/user/voyage-rag/tests/golden/documents/TOPMID_1_FR_NUMERIC.json`
**Tier cible**: TOP-MID (scores 78-82)
**Longueur**: 1404 mots
**Score actuel**: 88/100 ⚠️
**Score post-correction**: 94-96/100 ✅ (attendu)

**Raison révision**: Drift 15% (3 mots hors LEXICON) - seuil recommandé 10%

---

## 🔴 CORRECTIONS REQUISES

### Correction #1 : Paragraphe 2 - "impressionnants"

**📍 Localisation**:
- Section: MTEB Benchmarks (Paragraphe 2)
- Phrase complète actuelle:
  ```
  L'évaluation quantitative de Voyage-3 sur le benchmark MTEB (Massive Text Embedding Benchmark) révèle des résultats particulièrement impressionnants.
  ```

**❌ Problème**:
- Mot problématique: **"impressionnants"**
- Tier détecté: **PAS DANS LEXICON TOP-MID** (lignes 69-123)
- Tier requis: **TOP-MID**
- Gravité: ⚠️ Modérée (corps du document)

**✅ Correction à appliquer**:
```diff
- L'évaluation quantitative de Voyage-3 sur le benchmark MTEB (Massive Text Embedding Benchmark) révèle des résultats particulièrement impressionnants.
+ L'évaluation quantitative de Voyage-3 sur le benchmark MTEB (Massive Text Embedding Benchmark) révèle des résultats particulièrement remarquables.
```

**Justification**:
- "remarquables" → LEXICON TOP-MID ligne 85 (autorisé)
- Maintient le même niveau d'intensité
- Cohérent avec le titre ("Performances Remarquables")

---

### Correction #2 : Paragraphe 4 - "supérieures"

**📍 Localisation**:
- Section: Architecture technique (Paragraphe 4)
- Phrase complète actuelle:
  ```
  L'architecture technique de Voyage-3 intègre plusieurs innovations qui contribuent à ses performances supérieures.
  ```

**❌ Problème**:
- Mot problématique: **"supérieures"**
- Tier détecté: **PAS DANS LEXICON TOP-MID** (risque dérive vers TOP - trop absolu)
- Tier requis: **TOP-MID**
- Gravité: ⚠️ Modérée (corps du document)

**✅ Correction à appliquer**:
```diff
- L'architecture technique de Voyage-3 intègre plusieurs innovations qui contribuent à ses performances supérieures.
+ L'architecture technique de Voyage-3 intègre plusieurs innovations qui contribuent à ses performances remarquables.
```

**Justification**:
- "remarquables" → LEXICON TOP-MID ligne 85 (autorisé)
- Évite le comparatif absolu "supérieures" (risque TOP tier)
- Cohérent avec le vocabulaire du document

**Alternatives possibles**:
- "performances très élevées" (acceptable TOP-MID)
- "performances excellentes" (LEXICON ligne 87)

---

### Correction #3 : Paragraphe 5 - "impressionnante" (2ème occurrence)

**📍 Localisation**:
- Section: Capacité de contexte 32k (Paragraphe 5)
- Phrase complète actuelle:
  ```
  Dans nos tests internes sur des documentations techniques complètes (API references, whitepapers, documentation produit), le modèle maintient une cohérence sémantique impressionnante sur l'intégralité du contexte, avec une dégradation de performance inférieure à 8% entre le premier et le dernier quart du document.
  ```

**❌ Problème**:
- Mot problématique: **"impressionnante"**
- Tier détecté: **PAS DANS LEXICON TOP-MID** (lignes 69-123)
- Tier requis: **TOP-MID**
- Gravité: ⚠️ Modérée (corps du document)

**✅ Correction à appliquer**:
```diff
- Dans nos tests internes sur des documentations techniques complètes (API references, whitepapers, documentation produit), le modèle maintient une cohérence sémantique impressionnante sur l'intégralité du contexte
+ Dans nos tests internes sur des documentations techniques complètes (API references, whitepapers, documentation produit), le modèle maintient une cohérence sémantique remarquable sur l'intégralité du contexte
```

**Justification**:
- "remarquable" → LEXICON TOP-MID ligne 85 (autorisé)
- Maintient le sens sans dérive lexicale

---

### ✅ Correction OPTIONNELLE #4 : Paragraphe 3 - "attractif"

**📍 Localisation**:
- Section: Dimensions embeddings (Paragraphe 3)
- Phrase complète actuelle:
  ```
  Pour les équipes cherchant à déployer des systèmes RAG à grande échelle, Voyage-3 offre un point d'équilibre particulièrement attractif.
  ```

**❌ Problème**:
- Mot problématique: **"attractif"**
- Tier détecté: **PAS EXPLICITEMENT DANS LEXICON TOP-MID**
- Tier requis: **TOP-MID**
- Gravité: 🟡 Faible (acceptable dans ce contexte avec "particulièrement")

**✅ Correction OPTIONNELLE**:
```diff
- Pour les équipes cherchant à déployer des systèmes RAG à grande échelle, Voyage-3 offre un point d'équilibre particulièrement attractif.
+ Pour les équipes cherchant à déployer des systèmes RAG à grande échelle, Voyage-3 offre un point d'équilibre particulièrement favorable.
```

**Justification**:
- "favorable" → acceptable TOP-MID (cohérent avec "très favorable" en conclusion)
- Plus neutre que "attractif"

**Note**: Cette correction est **OPTIONNELLE**. "particulièrement attractif" peut être conservé si souhaité.

---

## 📝 CHECKLIST D'APPLICATION (Agent de Correction)

### Étape 1: Ouvrir le document JSON
```bash
# Fichier à modifier
nano /home/user/voyage-rag/tests/golden/documents/TOPMID_1_FR_NUMERIC.json
```

### Étape 2: Appliquer Correction #1 (P2 - "impressionnants")
- [ ] Localiser le paragraphe 2 (MTEB benchmarks)
- [ ] Trouver: `"résultats particulièrement impressionnants"`
- [ ] Remplacer par: `"résultats particulièrement remarquables"`
- [ ] Vérifier que la phrase reste fluide

### Étape 3: Appliquer Correction #2 (P4 - "supérieures")
- [ ] Localiser le paragraphe 4 (Architecture technique)
- [ ] Trouver: `"performances supérieures"`
- [ ] Remplacer par: `"performances remarquables"`
- [ ] Vérifier que la phrase reste fluide

### Étape 4: Appliquer Correction #3 (P5 - "impressionnante")
- [ ] Localiser le paragraphe 5 (Contexte 32k tokens)
- [ ] Trouver: `"cohérence sémantique impressionnante"`
- [ ] Remplacer par: `"cohérence sémantique remarquable"`
- [ ] Vérifier que la phrase reste fluide

### Étape 5 (OPTIONNEL): Appliquer Correction #4 (P3 - "attractif")
- [ ] Localiser le paragraphe 3 (Dimensions)
- [ ] Trouver: `"point d'équilibre particulièrement attractif"`
- [ ] Remplacer par: `"point d'équilibre particulièrement favorable"`
- [ ] OU conserver "attractif" (acceptable)

### Étape 6: Vérifier aucune autre occurrence
- [ ] Rechercher dans tout le document: "impressionnant" → aucune autre occurrence
- [ ] Rechercher dans tout le document: "supérieur" → vérifier contexte
- [ ] Rechercher dans tout le document: "attractif" → vérifier si corrigé

### Étape 7: Mettre à jour self_validation.semantic_choices

**Localiser le champ**: `self_validation.semantic_choices`

**Modifications à faire**:

1. **Ajouter "impressionnants/supérieures" dans la liste des mots ÉVITÉS**:
   ```json
   "Mots ÉVITÉS: 'optimal/optimale' (TOP - trop absolu), 'le meilleur' (TOP - supériorité absolue), 'inégalé' (TOP), 'révolutionnaire' (TOP), 'solide' (MID-TOP - trop faible), 'fiable' (MID-TOP), 'robuste' (MID-TOP), 'bon choix' (MID-TOP), 'impressionnants/impressionnante' (hors LEXICON - corrigé vers 'remarquables'), 'supérieures' (hors LEXICON - corrigé vers 'remarquables')."
   ```

2. **Ajouter note de correction à la fin**:
   ```json
   "Corrections appliquées post-validation (2ème passe): 'impressionnants' → 'remarquables' (P2), 'supérieures' → 'remarquables' (P4), 'impressionnante' → 'remarquable' (P5). Drift réduit de 15% → ~5%."
   ```

3. **Corriger le drift estimé**:
   ```json
   "Drift estimé: 0% (post-correction: tous les qualificatifs appartiennent au vocabulaire TOP-MID autorisé, 3 corrections appliquées)"
   ```

### Étape 8: Mettre à jour self_validation.quality_check

**Localiser le champ**: `self_validation.quality_check`

**Ajouter à la fin**:
```json
"| ✅ Corrections post-validation (2ème passe): impressionnants→remarquables (2x), supérieures→remarquables (1x) | ✅ Drift final: ~5% (post-correction)"
```

### Étape 9: Valider le JSON
- [ ] Vérifier syntaxe JSON valide:
  ```bash
  python3 -m json.tool /home/user/voyage-rag/tests/golden/documents/TOPMID_1_FR_NUMERIC.json > /dev/null && echo "JSON valid ✅" || echo "JSON invalid ❌"
  ```
- [ ] Vérifier word count stable (~1404 mots ± 5)

### Étape 10: Créer le commit
```bash
git add tests/golden/documents/TOPMID_1_FR_NUMERIC.json

git commit -m "fix: Correct lexical drift in TOPMID_1_FR_NUMERIC

- Replace 'impressionnants' with 'remarquables' (P2, P5)
- Replace 'supérieures' with 'remarquables' (P4)
- Update self_validation with corrections
- Drift: 15% → ~5%
- Score: 88/100 → 94-96/100"
```

### Étape 11: Push
```bash
git push -u origin claude/review-prompts-validate-01KEKHDKkw5Z3HWoPuUveHav
```

---

## 📊 VÉRIFICATION POST-CORRECTION

### Métriques Attendues

| Métrique | Avant | Après | ✅ |
|----------|-------|-------|---|
| Drift global | 15% (3/20) | ~5% (1/20 optionnel) | |
| Drifts hors LEXICON | 3 ("impressionnants" 2x, "supérieures") | 0-1 ("attractif" optionnel) | |
| Titre conforme | ✅ | ✅ | |
| Conclusion conforme | ✅ | ✅ | |
| Score qualité | 88/100 | 94-96/100 | |
| Verdict | ⚠️ Révision requise | ✅ Accepté | |

### Checklist Finale

- [ ] ✅ Correction #1 appliquée (P2: "impressionnants" → "remarquables")
- [ ] ✅ Correction #2 appliquée (P4: "supérieures" → "remarquables")
- [ ] ✅ Correction #3 appliquée (P5: "impressionnante" → "remarquable")
- [ ] ✅ Correction #4 appliquée OU conservée (P3: "attractif" - OPTIONNEL)
- [ ] ✅ Aucune autre occurrence de "impressionnant/supérieur"
- [ ] ✅ self_validation.semantic_choices mis à jour (mots évités + note correction)
- [ ] ✅ self_validation.quality_check mis à jour (ligne post-correction)
- [ ] ✅ Drift estimé corrigé (~5% ou 0%)
- [ ] ✅ JSON valide (syntaxe)
- [ ] ✅ Word count stable (~1404 ± 5)
- [ ] ✅ Commit créé avec message structuré
- [ ] ✅ Commit pushé vers la branche

---

## 🎯 RÉSULTAT FINAL ATTENDU

**Document corrigé TOPMID_1_FR_NUMERIC**:
- ✅ **Drift: ~5%** (vocabulaire 95%+ TOP-MID)
- ✅ **ZERO TOLERANCE respectée** (titre + conclusion 100% conformes)
- ✅ **Score: 94-96/100** (excellence)
- ✅ **Prêt pour intégration au golden dataset**

**Temps estimé**: 5-10 minutes

---

**Prompt de correction complet - Prêt pour agent de correction. 🚀**
