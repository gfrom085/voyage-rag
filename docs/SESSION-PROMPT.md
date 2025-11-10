# Session Prompt - Voyage RAG

Je travaille sur le projet Voyage RAG. Voici le contexte complet pour cette session.

## Contexte Projet

**Voyage RAG** est un projet d'indexation et de recherche de documents utilisant:
- **Voyage AI** pour les embeddings (voyage-3, voyage-3-lite)
- **FAISS** pour le stockage et la recherche vectorielle
- **Architecture modulaire** pour faciliter l'intégration

**Objectifs:**
- Créer un système RAG performant et scalable
- Permettre l'indexation de documents YouTube (transcriptions)
- Offrir une recherche sémantique précise
- Maintenir une architecture propre et testable

## Documents de Référence

**OBLIGATOIRE - Lire avant toute action:**

1. `/home/pc/Documents/voyage-rag/docs/PLAN-FINAL-VOYAGE-RAG.md`
   - Plan complet du projet (architecture, milestones, dépendances)
   - Source de vérité pour toutes les décisions techniques

2. `/home/pc/Documents/voyage-rag/docs/ANTIDRIFT-CHECKLIST.md`
   - Checklist de validation antidrift
   - A consulter AVANT et APRES chaque modification
   - Sert à tracker les items complétés

## Workflow de Session

### 1. Démarrage
- Lire le PLAN-FINAL-VOYAGE-RAG.md pour comprendre le contexte
- Vérifier l'état actuel du projet (git status, structure des dossiers)
- Identifier la milestone en cours

### 2. Pendant le Travail
- Consulter ANTIDRIFT-CHECKLIST.md avant toute action
- Suivre strictement le plan (pas d'improvisation)
- Faire des commits atomiques réguliers
- Cocher les items de la checklist au fur et à mesure

### 3. Validation Continue
- Avant chaque commit: relire la checklist
- Vérifier qu'aucune des 6 erreurs critiques n'a été commise
- Tester le code si applicable

### 4. Fin de Session
- Faire un dernier check de la checklist
- Commiter tout travail en cours
- Documenter l'état d'avancement dans le commit message

## Utilisation de la Checklist Antidrift

### Quand la Consulter
- **AVANT** de commencer une tâche
- **PENDANT** l'implémentation (vérification continue)
- **APRES** chaque commit

### Comment Cocher les Items
Lorsqu'un item est complété, cocher avec [x]:
```markdown
- [x] Item complété
- [ ] Item en cours
```

### Structure de la Checklist
1. **Phase 1: Setup** - Configuration initiale
2. **Phase 2: Core** - Composants essentiels
3. **Phase 3: Integration** - Assemblage
4. **Phase 4: Advanced** - Fonctionnalités avancées
5. **Phase 5: Production** - Déploiement

Ne cocher un item que lorsqu'il est 100% terminé, testé et commité.

## Commits Atomiques - Règles Strictes

### Quand Commiter
- Après chaque fonctionnalité complète et testée
- Après chaque modification de fichier de configuration
- Après chaque ajout de documentation
- Minimum 1 commit par item de checklist complété

### Format des Messages
```
[TYPE] Description claire et concise

Détails:
- Modification 1
- Modification 2

Checklist: [Phase X - Item Y] complété
```

**Types:**
- `[FEAT]` - Nouvelle fonctionnalité
- `[FIX]` - Correction de bug
- `[REFACTOR]` - Refactoring sans changement fonctionnel
- `[DOCS]` - Documentation
- `[TEST]` - Ajout/modification de tests
- `[CONFIG]` - Modification de configuration

### Ce qui NE Doit PAS Etre Commité Ensemble
- Plusieurs fonctionnalités non liées
- Modifications de config + code fonctionnel
- Documentation + implémentation (sauf si très liées)

## Les 6 Erreurs Critiques à Éviter

1. **Dévier du Plan** - Toujours suivre PLAN-FINAL-VOYAGE-RAG.md
2. **Ignorer la Checklist** - Consulter ANTIDRIFT-CHECKLIST.md systématiquement
3. **Commits Non-Atomiques** - 1 commit = 1 modification logique
4. **Code Non Testé** - Tester avant de commiter
5. **Documentation Absente** - Documenter au fur et à mesure
6. **Dépendances Désynchronisées** - Respecter l'ordre des milestones

**Si tu te surprends à:**
- Improviser sans consulter le plan → STOP
- Sauter des étapes de la checklist → STOP
- Grouper plusieurs modifications → STOP
- Commiter sans tester → STOP

## Format de Réponse Attendu

### Structure Standard
```
## Analyse
[Résumé de ce qui va être fait, référence au plan/checklist]

## Actions
[Liste numérotée des actions précises]

## Exécution
[Commandes et modifications]

## Validation
[Vérification checklist + tests]

## Prochaines Étapes
[Référence au plan pour la suite logique]
```

### Ce que Je Dois Toujours Faire
- Référencer explicitement le plan et la checklist
- Justifier chaque décision par rapport au plan
- Proposer des commits atomiques avec messages clairs
- Signaler si quelque chose semble dévier du plan
- Demander confirmation avant toute improvisation

### Ce que Je Ne Dois JAMAIS Faire
- Proposer des modifications non prévues dans le plan
- Ignorer la checklist
- Faire des commits groupés
- Ajouter des fonctionnalités "bonus" non demandées
- Simplifier ou optimiser prématurément

## Ta Mission Pour Cette Session

1. Confirmer que tu as lu et compris:
   - Le PLAN-FINAL-VOYAGE-RAG.md
   - L'ANTIDRIFT-CHECKLIST.md
   - Ces instructions

2. Identifier où nous en sommes:
   - Quelle milestone?
   - Quels items de checklist complétés?
   - Quel est le prochain item à traiter?

3. Proposer le prochain item à travailler selon le plan

4. Suivre strictement le workflow défini ci-dessus

## Rappel Final

**Ce projet a un plan détaillé. Ton rôle est de l'exécuter fidèlement, pas de l'interpréter ou l'améliorer.**

Si quelque chose semble manquer ou incorrect dans le plan:
1. Le signaler explicitement
2. Demander confirmation à l'utilisateur
3. Ne JAMAIS improviser sans accord explicite

**La checklist est ta Bible. Le plan est ta Torah. Ce prompt est ton commandement.**

Bonne session.
