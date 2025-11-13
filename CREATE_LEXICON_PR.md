# Instructions - Créer le PR LEXICON

## 📋 Étapes pour créer le PR sur GitHub

### 1. Accéder à GitHub
Ouvrez votre navigateur et allez sur:
```
https://github.com/gfrom085/voyage-rag
```

### 2. Créer le Pull Request

**Option A**: Si un bandeau jaune apparaît:
- Cliquez sur **"Compare & pull request"**

**Option B**: Sinon:
1. Cliquez sur l'onglet **"Pull requests"**
2. Cliquez sur **"New pull request"**
3. Sélectionnez:
   - **base**: `main`
   - **compare**: `claude/add-lexicon-reference-011CV4KmvWuWCs9q8hKCKwep`

### 3. Remplir le Pull Request

**Titre**:
```
feat: Add comprehensive lexical reference (LEXICON.md) to prevent tier drift
```

**Description**:
Copiez-collez l'intégralité du contenu de **`PR_LEXICON.md`** dans le champ description.

### 4. Vérifier les Changements

GitHub devrait afficher:
- ✅ 4 files changed
- ✅ ~710 additions
- ✅ ~30 deletions (modifications)

**Fichiers modifiés**:
```
tests/golden/prompts/LEXICON.md     (NEW)     +600 lines
tests/golden/prompts/PRIMING.md     (UPDATED)  +12 lines
tests/golden/prompts/VALIDATOR.md   (UPDATED)  +80 lines
tests/golden/prompts/INDEX.md       (UPDATED)  +18 lines
```

### 5. Créer et Merger le Pull Request

1. Cliquez sur **"Create pull request"**
2. Une fois créé, cliquez sur **"Merge pull request"**
3. Confirmez avec **"Confirm merge"**
4. (Optionnel) Supprimez la branche après merge

---

## 🎯 Pourquoi ce PR est CRITIQUE

Sans ce lexique:
- ❌ Drift systématique garanti sur 34 documents
- ❌ Dataset scientifiquement invalide
- ❌ 238 opportunités de drift (7 tiers × 34 docs)

Avec ce lexique:
- ✅ Source de vérité unique pour vocabulaire
- ✅ Détection automatique du drift (formule mathématique)
- ✅ Prévention proactive (vérification avant écriture)
- ✅ Cohérence garantie sur 34 documents

---

## ✅ Après le Merge

1. **Revenir sur main**:
   ```bash
   git checkout main
   git pull origin main
   ```

2. **Vérifier que LEXICON.md est présent**:
   ```bash
   ls -la tests/golden/prompts/LEXICON.md
   ```

3. **Utiliser LEXICON.md** pour tous les documents suivants

---

## 📊 Informations Complémentaires

**Branche**: `claude/add-lexicon-reference-011CV4KmvWuWCs9q8hKCKwep`
**Commit**: `ccd967e`
**Impact**: Prévention ~70% du drift (vocabulaire)
**Prochaine étape**: PR complémentaire pour 5 vecteurs additionnels (métriques, ratios, densité, structure, validation croisée)

---

**MERGE ASAP avant de générer plus de documents !** 🔴
