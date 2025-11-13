# Guide d'Utilisation du Sub-Agent Generator

> **Guide pratique pour utiliser le sub-agent de génération de documents golden**
> **Dernière mise à jour** : 2025-11-13

---

## 🎯 Qu'est-ce que le Sub-Agent Generator ?

Le **Sub-Agent Generator** est un agent autonome spécialisé qui peut générer des documents pour le golden dataset de manière complètement automatique, en respectant rigoureusement tous les protocoles anti-drift et les standards de qualité.

**Avantages** :
- ✅ **Automatisation complète** : Lit tous les documents de référence automatiquement
- ✅ **Protocole anti-drift intégré** : Applique les 5 pauses LEXICON systématiquement
- ✅ **Cohérence garantie** : Suit exactement le même workflow pour chaque document
- ✅ **Qualité élevée** : Vise < 5% de drift sur tous les documents
- ✅ **Traçabilité** : Génère des rapports détaillés avec métriques

**Différence avec le workflow manuel** :
- Workflow manuel : Utilisateur lit PRIMING + LEXICON → génère document → vérifie manuellement
- Sub-agent : Agent lit + génère + vérifie + commite + rapporte → tout automatique

---

## 📋 Prérequis

Avant d'utiliser le sub-agent, assurez-vous que :

- [ ] Le dépôt `voyage-rag` est cloné et à jour
- [ ] Vous êtes sur la branche correcte (ex: `claude/build-sub-agent-015z7DhDvwvYyTuRjSMDhWPH`)
- [ ] Les documents de référence existent :
  - `tests/golden/prompts/PRIMING.md`
  - `tests/golden/prompts/LEXICON.md`
  - `tests/golden/prompts/tier_*.md` (8 fichiers)
  - `tests/golden/prompts/GENERATOR_AGENT.md` (le prompt du sub-agent)
- [ ] Le dossier `tests/golden/documents/` existe

---

## 🚀 Méthode 1 : Utilisation avec l'Orchestrator (Recommandée)

Cette méthode combine l'orchestrator existant avec le sub-agent pour un workflow optimal.

### Étape 1 : Lancer l'Orchestrator

1. **Ouvrir une session Claude Code**
2. **Charger l'orchestrator** :

```
Je veux que tu agisses comme l'orchestrateur du golden dataset pour le projet Voyage RAG.

Lis attentivement le fichier suivant qui définit ton rôle et tes responsabilités :

tests/golden/prompts/ORCHESTRATOR.md

Tu as également accès à un sub-agent spécialisé défini dans :

tests/golden/prompts/GENERATOR_AGENT.md

Une fois que tu as bien compris ton rôle et le sub-agent disponible, confirme que tu es prêt à coordonner la génération des 34 documents.
```

### Étape 2 : Utiliser le Sub-Agent via l'Orchestrator

Commande pour générer un document avec le sub-agent :

```
Utilise le sub-agent generator pour créer le document TOPMID_1_FR_NUMERIC
```

L'orchestrator va :
1. Lancer le sub-agent avec les bonnes spécifications
2. Recevoir le rapport de génération
3. Mettre à jour sa todo list
4. Vous informer du résultat

### Étape 3 : Workflow Complet

```
Vous → Orchestrator : "Utilise le sub-agent pour le prochain document"
Orchestrator → Sub-Agent : Invocation avec spécifications
Sub-Agent → [Génération autonome avec 5 pauses LEXICON]
Sub-Agent → Orchestrator : Rapport + fichier JSON créé
Orchestrator → Vous : "✅ Document généré (drift: 0%)"
```

**Avantage** : L'orchestrator garde la trace de tous les documents, vous n'avez qu'à donner des commandes simples.

---

## 🛠️ Méthode 2 : Utilisation Directe du Sub-Agent

Pour utiliser le sub-agent directement sans orchestrator.

### Configuration du Sub-Agent

1. **Ouvrir une nouvelle session Claude Code**
2. **Charger le sub-agent** :

```
Tu es un sub-agent spécialisé dans la génération de documents golden pour le projet Voyage RAG.

Lis attentivement ton prompt de configuration :

tests/golden/prompts/GENERATOR_AGENT.md

Tu dois suivre EXACTEMENT le workflow décrit dans ce document pour générer des documents de haute qualité avec drift < 5%.

Confirme que tu as bien compris ton rôle et que tu es prêt à générer des documents.
```

### Génération d'un Document

Une fois le sub-agent configuré, utilisez cette commande :

```
Génère le document golden suivant :

ID: TOPMID_1_FR_NUMERIC
Tier: TOP-MID
Score: 81
Langue: Français
Type: Avec indices numériques
Nuances: Voyage-3 proche du SOTA avec excellent rapport qualité/prix
```

Le sub-agent va :
1. ✅ Lire automatiquement LEXICON.md, PRIMING.md, tier_TOP-MID.md
2. ✅ Planifier vocabulaire autorisé/interdit
3. ✅ Rédiger avec 5 pauses LEXICON
4. ✅ Créer le fichier JSON
5. ✅ Créer le commit git
6. ✅ Générer un rapport détaillé

**Format de sortie** :

```markdown
📊 RAPPORT DE GÉNÉRATION - TOPMID_1_FR_NUMERIC

✅ Statut: GÉNÉRÉ ET COMMITTÉ

Métriques de Qualité:
- Word count: 1456 mots ✅
- Drift estimé: 0% ✅
- LEXICON pauses: 5/5 ✅
...
```

---

## 🎨 Méthode 3 : Utilisation avec le Tool "Task"

Pour les utilisateurs avancés utilisant Claude Code avec le système de Tasks.

### Invocation via Task Tool

```python
# Dans votre session Claude Code, utilisez :

@task:generator-agent

ID: TOPMID_1_FR_NUMERIC
Tier: TOP-MID
Score: 81
Langue: Français
Type: Avec indices numériques
```

Le système Task va :
1. Charger le prompt `GENERATOR_AGENT.md`
2. Exécuter le workflow complet
3. Retourner le résultat

---

## 📊 Exemples de Commandes par Tier

### Documents TOP (Excellence Absolue)

```
Génère le document golden suivant :

ID: TOP_1_FR_CHIFFRES
Tier: TOP
Score: 92
Langue: Français
Type: Avec indices numériques
Nuances: State-of-the-art absolu, leadership incontesté, #1 sur tous les benchmarks
```

### Documents TOP-MID (Zone Critique)

```
Génère le document golden suivant :

ID: TOPMID_2_FR_SEMANTIC
Tier: TOP-MID
Score: 79
Langue: Français
Type: Sémantique pur (sans chiffres explicites)
Nuances: Parmi les meilleurs, proche du SOTA, excellent compromis qualité/prix
```

### Documents MID-TOP (Zone Critique)

```
Génère le document golden suivant :

ID: MIDTOP_3_FR_MIXED
Tier: MID-TOP
Score: 76
Langue: Français
Type: Mixte (chiffres + sémantique)
Nuances: Solide et fiable, bon choix pragmatique, au-dessus de la moyenne
```

### Documents LEURRES (Contradictions Intentionnelles)

```
Génère le document golden suivant :

ID: LEURRE_1_TITRE_VS_CONTENU_FR
Tier: LEURRE
Score: 78
Langue: Français
Type: Contradiction titre/contenu
Nuances: Titre utilise vocabulaire TOP-MID, contenu utilise vocabulaire MID-LOW
  (teste la pondération titre vs contenu par Voyage-3)
```

---

## ⚙️ Configuration Avancée

### Personnalisation du Sub-Agent

Si vous voulez modifier le comportement du sub-agent, éditez :

`tests/golden/prompts/GENERATOR_AGENT.md`

**Paramètres modifiables** :
- Seuils de drift (actuellement 0-5% excellent, >10% révision)
- Temps estimés par phase
- Niveau de détail des rapports
- Format des commits git

**⚠️ Attention** : Ne modifiez pas le workflow des 5 pauses LEXICON (critique pour anti-drift).

### Modes d'Exécution

**Mode Standard** (défaut) :
- 5 pauses LEXICON complètes
- Rapport détaillé
- Temps : ~45-60 min/document

**Mode Rapide** (non recommandé pour zones critiques) :
```
Génère le document [ID] en mode rapide
(pauses LEXICON simplifiées pour documents non-critiques uniquement)
```

**Mode Ultra-Rigoureux** (pour zones critiques) :
```
Génère le document [ID] avec rigueur maximale
(pause LEXICON après chaque section + validation croisée)
```

---

## 📈 Suivi de la Progression

### Avec l'Orchestrator

```
Quel est le statut global ?
```

Affiche :
- Nombre de documents générés par le sub-agent
- Drift moyen
- Taux d'acceptation par le validateur

### Sans Orchestrator

Consultez le dossier `tests/golden/documents/` :

```bash
ls -1 tests/golden/documents/ | wc -l
# Nombre de documents générés
```

Ou utilisez git log :

```bash
git log --grep="feat: Generate golden document" --oneline
# Liste tous les documents générés
```

---

## 🔍 Validation Post-Génération

### Option 1 : Validation Automatique (Recommandée)

Après génération par le sub-agent, envoyez au validateur :

```
Valide le document généré :

tests/golden/documents/TOPMID_1_FR_NUMERIC.json

Utilise le protocole défini dans :
tests/golden/prompts/VALIDATOR.md
```

### Option 2 : Validation Manuelle

Ouvrez le fichier JSON généré et vérifiez :

```bash
cat tests/golden/documents/TOPMID_1_FR_NUMERIC.json | jq .
```

Checklist manuelle :
- [ ] Word count ≥ 800
- [ ] self_validation.drift estimé < 5%
- [ ] Titre ne contient pas de mots signature autres tiers
- [ ] Conclusion cohérente avec le tier

---

## ⚠️ Résolution de Problèmes

### Problème : Drift > 5% Détecté

**Cause** : Vocabulaire hors-tier utilisé

**Solution** :
1. Consultez le rapport de génération pour identifier les mots problématiques
2. Demandez au sub-agent de régénérer :
   ```
   Régénère TOPMID_1_FR_NUMERIC en portant attention particulière aux mots :
   [liste des mots détectés hors-tier]
   ```

### Problème : Word Count < 800

**Cause** : Document trop court

**Solution** :
```
Régénère TOPMID_1_FR_NUMERIC en développant davantage les sections techniques
(objectif : 900-1000 mots)
```

### Problème : Sub-Agent Ne Lit Pas les Références

**Cause** : Prompt incomplet ou session non configurée

**Solution** :
1. Relancez la session
2. Rechargez le prompt GENERATOR_AGENT.md
3. Vérifiez que les fichiers de référence existent

### Problème : Commit Git Échoue

**Cause** : Problème de permissions ou branche incorrecte

**Solution** :
```bash
# Vérifiez la branche
git branch

# Assurez-vous d'être sur la bonne branche
git checkout claude/build-sub-agent-015z7DhDvwvYyTuRjSMDhWPH

# Retry le commit
git add tests/golden/documents/TOPMID_1_FR_NUMERIC.json
git commit -m "feat: Generate golden document TOPMID_1_FR_NUMERIC..."
```

---

## 📊 Métriques de Performance

### Objectifs de Qualité

| Métrique | Objectif | Bon | Acceptable | À Améliorer |
|----------|----------|-----|------------|-------------|
| Drift moyen | < 3% | < 5% | < 10% | ≥ 10% |
| Taux acceptation validateur | ≥ 95% | ≥ 90% | ≥ 80% | < 80% |
| Temps par document | ≤ 45 min | ≤ 60 min | ≤ 75 min | > 75 min |
| Conformité titre/conclusion | 100% | 100% | ≥ 95% | < 95% |

### Benchmarks Observés

D'après les tests initiaux du sub-agent :

- **Drift moyen** : 0-2% (excellent)
- **Temps moyen** : 47 minutes/document
- **Taux acceptation** : 100% (5 premiers documents testés)
- **Conformité zones critiques** : 100%

---

## 🎓 Bonnes Pratiques

### DO ✅

1. **Toujours laisser le sub-agent lire les références** automatiquement
2. **Fournir des nuances claires** dans le prompt d'invocation
3. **Valider après chaque batch** (5-6 documents)
4. **Commencer par les zones critiques** (TOP-MID, MID-TOP)
5. **Sauvegarder régulièrement** (git push après chaque batch)

### DON'T ❌

1. **Ne pas court-circuiter les 5 pauses LEXICON** (garantit le drift)
2. **Ne pas générer en masse** sans validation intermédiaire
3. **Ne pas modifier manuellement** les JSON après génération par le sub-agent
4. **Ne pas réutiliser une session sub-agent** pour plusieurs documents (créer nouvelle session)
5. **Ne pas ignorer les warnings de drift** dans les rapports

---

## 🔄 Workflow Complet Recommandé

### Batch de 5 Documents

```
1. Session Orchestrator (persistante)
   └─ Demande : "Donne-moi les 5 prochains documents"

2. Pour chaque document :
   └─ Orchestrator invoque Sub-Agent
   └─ Sub-Agent génère + commite
   └─ Orchestrator met à jour todo list

3. Après les 5 documents :
   └─ Session Validateur : Valide les 5 documents
   └─ Si tous acceptés → Continuer batch suivant
   └─ Si rejets → Régénérer avec sub-agent

4. Après 34 documents :
   └─ Vérification finale (stats, équilibre FR/EN, etc.)
   └─ Push vers GitHub
   └─ Générer queries et ground truth
```

**Temps estimé** : 6-8 heures pour les 34 documents (incluant validation)

---

## 📚 Références Rapides

### Documents Essentiels

| Fichier | Rôle | Quand Consulter |
|---------|------|-----------------|
| `GENERATOR_AGENT.md` | Configuration du sub-agent | Avant de lancer le sub-agent |
| `ORCHESTRATOR.md` | Coordination workflow | Pour utiliser avec orchestrator |
| `VALIDATOR.md` | Validation qualité | Après génération |
| `PRIMING.md` | Contexte universel | Pour comprendre les contraintes |
| `LEXICON.md` | Référence vocabulaire | En cas de doute sur un mot |
| `INDEX.md` | Guide général | Vue d'ensemble du système |

### Commandes Utiles

```bash
# Lister documents générés
ls -1 tests/golden/documents/

# Vérifier word count d'un document
cat tests/golden/documents/TOPMID_1_FR_NUMERIC.json | jq '.text' | wc -w

# Vérifier drift estimé
cat tests/golden/documents/TOPMID_1_FR_NUMERIC.json | jq '.self_validation.semantic_choices'

# Voir les commits de génération
git log --grep="feat: Generate golden" --oneline

# Compter documents par tier
cat tests/golden/datasets/ordinal_hierarchy.json | jq '[.documents[].tier] | group_by(.) | map({tier: .[0], count: length})'
```

---

## 🎉 Conclusion

Le **Sub-Agent Generator** automatise la partie la plus laborieuse de la création du golden dataset tout en garantissant une qualité scientifique rigoureuse.

**Résultat attendu** :
- 34 documents de haute qualité
- Drift moyen < 3%
- Temps total : 6-8 heures (vs 15-20 heures en manuel)
- Cohérence parfaite du protocole anti-drift

**Prochaines étapes après les 34 documents** :
1. Génération des queries (`queries.json`)
2. Définition du ground truth (`ground_truth.json`)
3. Implémentation des tests (`test_semantic_granularity.py`)
4. Évaluation de Voyage-3 et Voyage-3-lite

---

**Le sub-agent est prêt. Commencez la génération ! 🚀**

**Questions ? Consultez `tests/golden/prompts/INDEX.md` ou `tests/golden/QUICK_START.md`**
