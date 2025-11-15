# PROMPT DE CORRECTION - TOPMID_4_EN_NUMERIC

## 📋 INFORMATIONS DOCUMENT

**Document ID** : TOPMID_4_EN_NUMERIC
**Fichier** : `/home/user/voyage-rag/tests/golden/documents/TOPMID_4_EN_NUMERIC.json`
**Tier cible** : TOP-MID (scores 78-82)
**Longueur** : 831 mots
**Score actuel** : 83/100 ⚠️
**Score post-correction** : 95/100 ✅ (attendu)

**Raison révision** : Violation ZERO TOLERANCE (conclusion) + drift 10%

---

## 🔴 CORRECTIONS REQUISES

### Correction #1 : Paragraph 8 - "mature"

**📍 Localisation** :
- Section : "Production Deployment Considerations"
- Paragraph : 8
- Phrase complète actuelle :
  ```
  Real-world deployment experience reveals Voyage-3 as a remarkably mature platform for enterprise RAG systems.
  ```

**❌ Problème** :
- Mot problématique : **"mature"**
- Tier détecté : **MID-TOP** (LEXICON ligne 139)
- Tier requis : **TOP-MID**
- Gravité : ⚠️ Modérée (corps du document)

**✅ Correction à appliquer** :
```diff
- Real-world deployment experience reveals Voyage-3 as a remarkably mature platform for enterprise RAG systems.
+ Real-world deployment experience reveals Voyage-3 as a remarkably competitive platform for enterprise RAG systems.
```

**Justification** :
- "competitive" → LEXICON TOP-MID ligne 88 ("highly competitive" autorisé)
- Maintient le sens sans connotation MID-TOP "maturité"

**Alternatives possibles** :
- "highly capable platform" (neutre, acceptable)
- "exceptionally well-established platform" (évite "maturité")

---

### Correction #2 : Conclusion - "maturity" ⚠️ **PRIORITAIRE**

**📍 Localisation** :
- Section : **Conclusion** (ZERO TOLERANCE ZONE)
- Phrase : Deuxième phrase du dernier paragraphe
- Phrase complète actuelle :
  ```
  Its positioning among the best commercial offerings stems from a combination of near state-of-the-art performance across diverse tasks, highly competitive pricing, and remarkable operational maturity.
  ```

**❌ Problème** :
- Mot problématique : **"maturity"**
- Tier détecté : **MID-TOP** (LEXICON ligne 139)
- Tier requis : **TOP-MID**
- Zone : **CONCLUSION (ZERO TOLERANCE)**
- Gravité : 🔴 **CRITIQUE**
- Référence : LEXICON ligne 397 "Zones à tolérance ZÉRO : Titre, Conclusion"

**✅ Correction à appliquer** :
```diff
- Its positioning among the best commercial offerings stems from a combination of near state-of-the-art performance across diverse tasks, highly competitive pricing, and remarkable operational maturity.
+ Its positioning among the best commercial offerings stems from a combination of near state-of-the-art performance across diverse tasks, highly competitive pricing, and remarkable operational excellence.
```

**Justification** :
- "excellence" → LEXICON TOP-MID ligne 94 ("d'excellence" autorisé)
- Maintient l'intensité de "remarkable operational X"
- Conforme ZERO TOLERANCE

**Alternatives possibles** :
- "remarkable operational performance" (LEXICON ligne 85)
- "outstanding operational reliability" (LEXICON ligne 93)

---

## 📝 CHECKLIST D'APPLICATION (Agent de Correction)

### Étape 1 : Ouvrir le document JSON
```bash
# Fichier à modifier
nano /home/user/voyage-rag/tests/golden/documents/TOPMID_4_EN_NUMERIC.json
```

### Étape 2 : Appliquer Correction #1 (P8)
- [ ] Localiser la section "Production Deployment Considerations"
- [ ] Trouver : `"remarkably mature platform"`
- [ ] Remplacer par : `"remarkably competitive platform"`
- [ ] Vérifier que la phrase reste fluide

### Étape 3 : Appliquer Correction #2 (Conclusion) ⚠️ PRIORITAIRE
- [ ] Localiser le dernier paragraphe (Conclusion)
- [ ] Trouver : `"remarkable operational maturity"`
- [ ] Remplacer par : `"remarkable operational excellence"`
- [ ] Vérifier que la phrase reste fluide

### Étape 4 : Vérifier aucune autre occurrence
- [ ] Rechercher dans tout le document : "mature" → aucune autre occurrence
- [ ] Rechercher dans tout le document : "maturity" → aucune autre occurrence

### Étape 5 : Mettre à jour self_validation.semantic_choices

**Localiser le champ** : `self_validation.semantic_choices`

**Modifications à faire** :

1. **Ajouter "mature/maturity" dans la liste des mots ÉVITÉS** :
   ```json
   "Words AVOIDED: 'the best' (TOP tier - too absolute), 'unmatched' (TOP tier), 'state-of-the-art' without 'near' qualifier (TOP tier), 'optimal' in absolute sense (TOP tier), 'revolutionary' (TOP tier), 'solid' (MID-TOP tier - too weak), 'reliable' (MID-TOP tier - too weak), 'robust' (MID-TOP tier - too weak), 'mature/maturity' (MID-TOP tier - corrected to 'competitive/excellence')."
   ```

2. **Ajouter note de correction à la fin** :
   ```json
   "Corrections applied post-validation: 'mature' → 'competitive' (P8), 'maturity' → 'excellence' (conclusion - ZERO TOLERANCE zone)."
   ```

3. **Corriger le drift estimé** :
   ```json
   "Drift estimated: 0% (post-correction: 0 off-tier words in final version, 20 qualifiers verified)"
   ```

### Étape 6 : Mettre à jour self_validation.quality_check

**Localiser le champ** : `self_validation.quality_check`

**Ajouter à la fin** :
```json
"| ✅ Post-validation corrections applied: mature→competitive (P8), maturity→excellence (conclusion) | ✅ Final drift: 0%"
```

### Étape 7 : Valider le JSON
- [ ] Vérifier syntaxe JSON valide :
  ```bash
  python3 -m json.tool /home/user/voyage-rag/tests/golden/documents/TOPMID_4_EN_NUMERIC.json > /dev/null && echo "JSON valid ✅" || echo "JSON invalid ❌"
  ```
- [ ] Vérifier word count stable (~831 mots ± 5)

### Étape 8 : Créer le commit
```bash
git add tests/golden/documents/TOPMID_4_EN_NUMERIC.json

git commit -m "fix: Correct MID-TOP drift in TOPMID_4_EN_NUMERIC

- Replace 'mature' with 'competitive' (P8)
- Replace 'maturity' with 'excellence' (conclusion - ZERO TOLERANCE)
- Update self_validation with corrections
- Drift: 10% → 0%
- Score: 83/100 → 95/100"
```

### Étape 9 : Push
```bash
git push -u origin claude/review-prompts-validate-01KEKHDKkw5Z3HWoPuUveHav
```

---

## 📊 VÉRIFICATION POST-CORRECTION

### Métriques Attendues

| Métrique | Avant | Après | ✅ |
|----------|-------|-------|---|
| Drift global | 10% (2/20) | 0% (0/20) | |
| Drifts MID-TOP | 2 | 0 | |
| Titre conforme | ✅ | ✅ | |
| Conclusion conforme | ❌ | ✅ | |
| Score qualité | 83/100 | 95/100 | |
| Verdict | ⚠️ Révision requise | ✅ Accepté | |

### Checklist Finale

- [ ] ✅ Correction #1 appliquée (P8 : "mature" → "competitive")
- [ ] ✅ Correction #2 appliquée (Conclusion : "maturity" → "excellence")
- [ ] ✅ Aucune autre occurrence de "mature/maturity"
- [ ] ✅ self_validation.semantic_choices mis à jour (mots évités + note correction)
- [ ] ✅ self_validation.quality_check mis à jour (ligne post-correction)
- [ ] ✅ Drift estimé corrigé (0%)
- [ ] ✅ JSON valide (syntaxe)
- [ ] ✅ Word count stable (~831 ± 5)
- [ ] ✅ Commit créé avec message structuré
- [ ] ✅ Commit pushé vers la branche

---

## 🎯 RÉSULTAT FINAL ATTENDU

**Document corrigé TOPMID_4_EN_NUMERIC** :
- ✅ **Drift : 0%** (vocabulaire 100% TOP-MID)
- ✅ **ZERO TOLERANCE respectée** (titre + conclusion conformes)
- ✅ **Score : 95/100** (excellence)
- ✅ **Prêt pour intégration au golden dataset**

**Temps estimé** : 5-10 minutes

---

**Prompt de correction complet - Prêt pour agent de correction. 🚀**
