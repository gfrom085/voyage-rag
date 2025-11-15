# PROMPT DE CORRECTION - TOPMID_4_EN_NUMERIC

## Contexte de Correction

**Document ID** : TOPMID_4_EN_NUMERIC
**Tier cible** : TOP-MID (scores 78-82)
**Score actuel** : 83/100 ⚠️ (révision requise)
**Score post-correction attendu** : 95/100 ✅

**Raison de la révision** : **Violation ZERO TOLERANCE** en conclusion + drift 10%

---

## 🔴 Problèmes Détectés

### Drift #1 : "mature" dans Paragraph 8

**Localisation** : Section "Production Deployment Considerations" - Paragraph 8

**Texte actuel** :
```
Real-world deployment experience reveals Voyage-3 as a remarkably mature platform for enterprise RAG systems.
```

**Problème** :
- **Mot** : "mature"
- **Tier détecté** : MID-TOP (LEXICON ligne 139)
- **Tier requis** : TOP-MID
- **Référence LEXICON** : Ligne 121 "❌ INTERDICTIONS pour TOP-MID : Vocabulaire MID-TOP : 'solide', 'fiable', 'bon'"
- **Gravité** : ⚠️ Modérée (corps du document)

---

### Drift #2 : "maturity" dans Conclusion ⚠️ **CRITIQUE**

**Localisation** : Conclusion - Deuxième phrase

**Texte actuel** :
```
Its positioning among the best commercial offerings stems from a combination of near state-of-the-art performance across diverse tasks, highly competitive pricing, and remarkable operational maturity.
```

**Problème** :
- **Mot** : "maturity"
- **Tier détecté** : MID-TOP (LEXICON ligne 139 "mature | mature")
- **Tier requis** : TOP-MID
- **Zone** : **CONCLUSION (ZERO TOLERANCE)**
- **Référence LEXICON** :
  - Ligne 397 : "Zones à tolérance ZÉRO : Titre, Conclusion"
  - Ligne 394 : "Drift >10% OU violation tolérance ZÉRO → révision OBLIGATOIRE"
- **Gravité** : 🔴 **CRITIQUE** (ZERO TOLERANCE violation)

---

## ✅ Corrections Recommandées

### Correction #1 : Paragraph 8

**Option 1 (Recommandée)** :
```
Real-world deployment experience reveals Voyage-3 as a remarkably competitive platform for enterprise RAG systems.
```
- **Justification** : "competitive" → LEXICON ligne 88 (highly competitive - TOP-MID autorisé)

**Option 2** :
```
Real-world deployment experience reveals Voyage-3 as a highly capable platform for enterprise RAG systems.
```
- **Justification** : "capable" → neutre, acceptable pour TOP-MID

**Option 3** :
```
Real-world deployment experience reveals Voyage-3 as an exceptionally well-established platform for enterprise RAG systems.
```
- **Justification** : "well-established" → évite connotation "maturité"

---

### Correction #2 : Conclusion (PRIORITAIRE)

**Option 1 (Recommandée)** :
```
Its positioning among the best commercial offerings stems from a combination of near state-of-the-art performance across diverse tasks, highly competitive pricing, and remarkable operational excellence.
```
- **Justification** : "excellence" → LEXICON ligne 94 (d'excellence - TOP-MID autorisé)
- **Maintient l'intensité** : "remarkable operational excellence"

**Option 2** :
```
Its positioning among the best commercial offerings stems from a combination of near state-of-the-art performance across diverse tasks, highly competitive pricing, and remarkable operational performance.
```
- **Justification** : "performance" → LEXICON ligne 85 (remarkable performance - TOP-MID autorisé)

**Option 3** :
```
Its positioning among the best commercial offerings stems from a combination of near state-of-the-art performance across diverse tasks, highly competitive pricing, and outstanding operational reliability.
```
- **Justification** : "outstanding" → LEXICON ligne 93 (TOP-MID autorisé)

---

## 📝 Instructions d'Application

### Étape 1 : Ouvrir le document
```bash
# Fichier à modifier
/home/user/voyage-rag/tests/golden/documents/TOPMID_4_EN_NUMERIC.json
```

### Étape 2 : Appliquer les corrections

**Correction #1 (P8)** :
- Chercher : `"remarkably mature platform"`
- Remplacer par : `"remarkably competitive platform"`

**Correction #2 (Conclusion - PRIORITAIRE)** :
- Chercher : `"remarkable operational maturity"`
- Remplacer par : `"remarkable operational excellence"`

### Étape 3 : Mettre à jour self_validation

Modifier le champ `self_validation.semantic_choices` :

**Ajouter dans la liste des mots ÉVITÉS** :
```
Words AVOIDED: [...existing list...], 'mature/maturity' (MID-TOP tier - corrected to 'competitive/excellence').
```

**Ajouter note de correction** :
```
Corrections applied post-validation: 'mature' → 'competitive' (P8), 'maturity' → 'excellence' (conclusion - ZERO TOLERANCE zone).
```

**Corriger le drift estimé** :
```
Drift estimated: 0% (post-correction: 0 off-tier words in final version, 20 qualifiers verified)
```

Modifier le champ `self_validation.quality_check` :

**Ajouter à la fin** :
```
| ✅ Post-validation corrections applied: mature→competitive (P8), maturity→excellence (conclusion) | ✅ Final drift: 0%
```

### Étape 4 : Vérifier le JSON

```bash
# Valider la syntaxe JSON
python3 -m json.tool tests/golden/documents/TOPMID_4_EN_NUMERIC.json > /dev/null
```

### Étape 5 : Créer le commit

```bash
git add tests/golden/documents/TOPMID_4_EN_NUMERIC.json

git commit -m "fix: Correct MID-TOP drift in TOPMID_4_EN_NUMERIC

- Replace 'mature' with 'competitive' (P8)
- Replace 'maturity' with 'excellence' (conclusion - ZERO TOLERANCE zone)
- Update self_validation to reflect corrections
- Drift corrected: 10% → 0%
- Score improvement: 83/100 → 95/100 (expected)"
```

---

## 📊 Impact des Corrections

### Avant Correction

| Métrique | Valeur |
|----------|--------|
| Drift global | 10% (2/20) |
| Drifts MID-TOP | 2 |
| Titre conforme | ✅ |
| Conclusion conforme | ❌ |
| Score | 83/100 |
| Verdict | ⚠️ Révision requise |

### Après Correction

| Métrique | Valeur |
|----------|--------|
| Drift global | 0% (0/20) |
| Drifts MID-TOP | 0 |
| Titre conforme | ✅ |
| Conclusion conforme | ✅ |
| Score | 95/100 |
| Verdict | ✅ Accepté |

---

## ✅ Checklist de Validation Post-Correction

Après avoir appliqué les corrections, vérifier :

- [ ] ✅ Correction #1 appliquée (P8 : "mature" → "competitive")
- [ ] ✅ Correction #2 appliquée (Conclusion : "maturity" → "excellence")
- [ ] ✅ Aucune autre occurrence de "mature/maturity" dans le document
- [ ] ✅ self_validation.semantic_choices mis à jour
- [ ] ✅ self_validation.quality_check mis à jour
- [ ] ✅ JSON valide (syntaxe correcte)
- [ ] ✅ Word count stable (~831 mots ± 5)
- [ ] ✅ Commit créé avec message structuré

---

## 🎯 Résultat Attendu

**Document corrigé** :
- ✅ **0% drift** (vocabulaire 100% TOP-MID)
- ✅ **ZERO TOLERANCE respectée** (titre + conclusion conformes)
- ✅ **Score 95/100** (excellence)
- ✅ **Prêt pour intégration au golden dataset**

**Temps estimé** : 5-10 minutes pour corrections manuelles

---

**Prompt de correction prêt pour application immédiate. 🚀**
