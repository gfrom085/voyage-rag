#!/bin/bash
# Commandes d'Hydratation Validateur - Copy-Paste Rapide

echo "======================================"
echo "HYDRATATION AGENT VALIDATEUR"
echo "======================================"
echo ""

# Fetch les branches nécessaires
echo "📥 Étape 1/6 : Fetch branches..."
git fetch origin claude/add-lexicon-reference-011CV4KmvWuWCs9q8hKCKwep
git fetch origin claude/generate-topmid-french-document-011CV4npDa2o81rx4NgG83Bt
echo "✅ Branches fetchées"
echo ""

# PRIMING.md
echo "📄 Étape 2/6 : PRIMING.md (Contexte Projet)"
echo "--------------------------------------------"
git show origin/claude/add-lexicon-reference-011CV4KmvWuWCs9q8hKCKwep:tests/golden/prompts/PRIMING.md
echo ""
echo "✅ PRIMING.md affiché - Copier dans Claude Code"
echo ""

# LEXICON.md
echo "📚 Étape 3/6 : LEXICON.md (Référence Vocabulaire) ⚠️ CRITIQUE"
echo "----------------------------------------------------------------"
git show origin/claude/add-lexicon-reference-011CV4KmvWuWCs9q8hKCKwep:tests/golden/prompts/LEXICON.md
echo ""
echo "✅ LEXICON.md affiché - Copier dans Claude Code"
echo ""

# VALIDATOR.md
echo "🔍 Étape 4/6 : VALIDATOR.md (Protocole de Validation)"
echo "------------------------------------------------------"
git show origin/claude/add-lexicon-reference-011CV4KmvWuWCs9q8hKCKwep:tests/golden/prompts/VALIDATOR.md
echo ""
echo "✅ VALIDATOR.md affiché - Copier dans Claude Code"
echo ""

# Prompt TOPMID_1
echo "📋 Étape 5/6 : Prompt TOPMID_1_FR_NUMERIC"
echo "------------------------------------------"
git show origin/claude/add-lexicon-reference-011CV4KmvWuWCs9q8hKCKwep:tests/golden/prompts/tier_TOP-MID.md | sed -n '/## 📋 PROMPT 1\/6 : TOPMID_1_FR_NUMERIC/,/^## 📋 PROMPT 2/p' | head -n -2
echo ""
echo "✅ Prompt TOPMID_1 affiché - Copier dans Claude Code"
echo ""

# Document JSON
echo "📄 Étape 6/6 : Document TOPMID_1_FR_NUMERIC.json"
echo "-------------------------------------------------"
git show origin/claude/generate-topmid-french-document-011CV4npDa2o81rx4NgG83Bt:tests/golden/datasets/documents.json
echo ""
echo "✅ Document affiché - Extraire le premier document du tableau 'documents'"
echo ""

echo "======================================"
echo "✅ HYDRATATION COMPLÈTE"
echo "======================================"
echo ""
echo "📝 Maintenant dans Claude Code, envoie ce prompt :"
echo ""
echo "---"
echo "Tu es l'agent VALIDATEUR. Tu as reçu :"
echo "- PRIMING.md"
echo "- LEXICON.md"
echo "- VALIDATOR.md"
echo "- Prompt TOPMID_1_FR_NUMERIC"
echo "- Document JSON à valider"
echo ""
echo "Applique RIGOUREUSEMENT le PROTOCOLE D'EXTRACTION SYSTÉMATIQUE."
echo "Produis le tableau avec 10-15 qualificatifs."
echo "Détecte 'Optimale' (titre) et 'solide' (conclusion)."
echo "Calcule le drift %."
echo ""
echo "Commence maintenant !"
echo "---"
