# Commandes d'Hydratation pour Agent Validateur

## 🎯 Objectif
Fournir TOUT le contexte nécessaire au nouvel agent validateur pour valider TOPMID_1_FR_NUMERIC avec le protocole mis à jour.

---

## 📋 Ordre des Commandes (Copier-Coller dans Claude Code)

### Étape 1 : Récupérer les Fichiers de Contexte

```bash
# 1. Fetch la branche avec LEXICON + VALIDATOR mis à jour
git fetch origin claude/add-lexicon-reference-011CV4KmvWuWCs9q8hKCKwep

# 2. Fetch la branche avec le document à valider
git fetch origin claude/generate-topmid-french-document-011CV4npDa2o81rx4NgG83Bt
```

### Étape 2 : Afficher PRIMING.md (Contexte Projet)

```bash
git show origin/claude/add-lexicon-reference-011CV4KmvWuWCs9q8hKCKwep:tests/golden/prompts/PRIMING.md
```

**Instructions pour l'agent** : "Lis attentivement ce contexte projet complet."

---

### Étape 3 : Afficher LEXICON.md (Référence Vocabulaire) ⚠️ CRITIQUE

```bash
git show origin/claude/add-lexicon-reference-011CV4KmvWuWCs9q8hKCKwep:tests/golden/prompts/LEXICON.md
```

**Instructions pour l'agent** : "Lis le LEXICON complet. Tu DEVRAS le consulter pendant la validation pour vérifier chaque qualificatif."

**Sections clés à retenir** :
- Tableau TOP → LOW avec tous les synonymes
- Mots "signature" par tier
- Exemples de drift par tier

---

### Étape 4 : Afficher VALIDATOR.md (Ton Prompt de Rôle) 🔍

```bash
git show origin/claude/add-lexicon-reference-011CV4KmvWuWCs9q8hKCKwep:tests/golden/prompts/VALIDATOR.md
```

**Instructions pour l'agent** : "Ceci est TON rôle. Lis-le en entier. Tu devras appliquer le PROTOCOLE D'EXTRACTION SYSTÉMATIQUE (section après B1)."

**Section critique** :
- Lignes 159-227 : Protocole d'extraction OBLIGATOIRE
- Exemple concret avec tableau montrant détection de "Optimale" ET "solide"

---

### Étape 5 : Afficher le Prompt de Tâche Spécifique (TOPMID_1)

```bash
git show origin/claude/add-lexicon-reference-011CV4KmvWuWCs9q8hKCKwep:tests/golden/prompts/tier_TOP-MID.md | sed -n '/## 📋 PROMPT 1\/6 : TOPMID_1_FR_NUMERIC/,/^## 📋 PROMPT 2/p' | head -n -2
```

**Instructions pour l'agent** : "Ceci est le prompt exact qui a été donné au générateur pour créer TOPMID_1_FR_NUMERIC."

---

### Étape 6 : Afficher le Document à Valider

```bash
git show origin/claude/generate-topmid-french-document-011CV4npDa2o81rx4NgG83Bt:tests/golden/datasets/documents.json | jq '.documents[0]'
```

**Instructions pour l'agent** : "Voici le document JSON à valider. Applique le protocole d'extraction systématique."

**Alternative si jq n'est pas disponible** :
```bash
git show origin/claude/generate-topmid-french-document-011CV4npDa2o81rx4NgG83Bt:tests/golden/datasets/documents.json
```
(Puis copier manuellement le premier document du tableau)

---

## 🎯 Prompt Final pour l'Agent Validateur

Après avoir exécuté toutes les commandes ci-dessus, donnez ce prompt à l'agent :

```markdown
Tu es l'agent VALIDATEUR du golden dataset Voyage RAG.

Tu as reçu :
✅ PRIMING.md - Contexte projet
✅ LEXICON.md - Référence lexicale exhaustive
✅ VALIDATOR.md - Ton rôle et protocole
✅ Prompt TOPMID_1_FR_NUMERIC - Prompt de tâche
✅ Document JSON - À valider

## Mission

Valide le document TOPMID_1_FR_NUMERIC en appliquant **RIGOUREUSEMENT** le protocole d'extraction systématique (section 🔍 PROTOCOLE D'EXTRACTION SYSTÉMATIQUE du VALIDATOR.md).

### Impératifs

1. **Créer le tableau d'extraction obligatoire** :
   - 10-15 qualificatifs minimum
   - Position exacte (Titre, Ligne X, Conclusion)
   - Tier détecté pour chaque mot
   - Verdict ✅/❌ pour chaque mot

2. **Vérifications CRITIQUES** :
   - ⚠️ Titre : Vérifier "Optimale" (TOP vocabulary dans doc TOP-MID ?)
   - ⚠️ Conclusion : Chercher "solide" (MID-TOP vocabulary dans doc TOP-MID ?)
   - ⚠️ Calculer drift % : (hors-tier / total) × 100

3. **Consulter LEXICON.md** :
   - Section TOP-MID : Vocabulaire autorisé
   - Section TOP : Vocabulaire interdit pour TOP-MID
   - Section MID-TOP : Vocabulaire interdit pour TOP-MID

4. **Produire un rapport structuré** :
   - Sections A, B, C, D
   - Tableau d'extraction complet
   - Score /100
   - Verdict : ACCEPTÉ / À RÉVISER / REJETÉ

### Critères de Succès

- [ ] Détection de "Optimale" dans titre (drift TOP)
- [ ] Détection de "solide" dans conclusion (drift MID-TOP)
- [ ] Calcul du drift % (attendu : ~20%)
- [ ] Verdict : À RÉVISER (score ~83/100)

Commence ta validation maintenant !
```

---

## 🔍 Vérification Rapide

Pour vérifier que toutes les commandes fonctionnent avant de lancer l'agent :

```bash
# Test 1 : LEXICON accessible ?
git show origin/claude/add-lexicon-reference-011CV4KmvWuWCs9q8hKCKwep:tests/golden/prompts/LEXICON.md | head -50

# Test 2 : VALIDATOR accessible ?
git show origin/claude/add-lexicon-reference-011CV4KmvWuWCs9q8hKCKwep:tests/golden/prompts/VALIDATOR.md | grep "PROTOCOLE D'EXTRACTION"

# Test 3 : Document accessible ?
git show origin/claude/generate-topmid-french-document-011CV4npDa2o81rx4NgG83Bt:tests/golden/datasets/documents.json | grep "TOPMID_1_FR_NUMERIC"
```

Si les 3 tests affichent du contenu → ✅ Prêt à lancer le validateur

---

## 📝 Notes Importantes

1. **L'ordre est important** : PRIMING → LEXICON → VALIDATOR → Prompt → Document
2. **Le LEXICON est CRITIQUE** : Sans lui, le validateur ne peut pas vérifier le vocabulaire
3. **Le protocole d'extraction est OBLIGATOIRE** : Le tableau doit être produit
4. **Deux drifts à détecter** :
   - "Optimale" (titre) → TOP
   - "solide" (conclusion) → MID-TOP

---

## ✅ Résultat Attendu

Score validation v3 : **83-85/100**
Statut : **À RÉVISER**
Drifts détectés : **2 critiques** (Optimale + solide)
Drift % : **~20%** (seuil révision obligatoire dépassé)

---

**Prêt à lancer l'agent validateur !**
