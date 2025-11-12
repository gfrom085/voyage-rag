# TIER LEURRES - Prompts de Tâches (6 documents)

> **Instructions** : Lisez d'abord `PRIMING.md` en entier, puis exécutez UN SEUL prompt ci-dessous.

---

## 🎯 Qu'est-ce qu'un LEURRE ?

Les **LEURRES** sont des documents avec des **contradictions internes intentionnelles** pour tester comment Voyage AI pondère différents signaux sémantiques conflictuels.

### Objectifs des Tests Leurres

1. **Pondération titre vs contenu** : Voyage se fie-t-il plus au titre ou au corps du texte ?
2. **Pondération début vs fin** : Le début du document a-t-il plus de poids que la fin ?
3. **Signaux numériques vs sémantiques** : Un score élevé peut-il surpasser un texte négatif ?
4. **Détection de contradictions subtiles** : Voyage détecte-t-il les incohérences ?
5. **Robustesse aux documents adversariaux** : Peut-on "tromper" le système ?

### Types de Contradictions

- **Titre/Contenu** : Titre positif + contenu négatif (ou inverse)
- **Structure** : Début positif + fin négative (ou inverse)
- **Numérique/Sémantique** : Score élevé + description faible (ou inverse)
- **Intensité** : Subtile (léger désalignement) vs Flagrante (contradiction évidente)

---

## 📋 PROMPT 1/6 : LEURRE_1_TITRE_VS_CONTENU_FR

### Spécifications
- **ID** : `LEURRE_1_TITRE_VS_CONTENU_FR`
- **Tier** : LEURRES
- **Score** : 78 (TOP-MID sur le papier)
- **Langue** : Français
- **Type** : Contradiction titre/contenu

### Objectif du Document
Créez un document avec un **titre évoquant l'excellence/premium** mais dont le **contenu décrit des limitations et performances moyennes**.

### Contradiction Intentionnelle
- **Titre** : Doit suggérer TOP ou TOP-MID ("Solution d'Excellence", "Performance Exceptionnelle", etc.)
- **Contenu** : Doit décrire une solution MID-TOP ou MID (limitations notables, performances acceptables mais pas remarquables)

### Test Visé
Si Voyage classe ce document en TOP/TOP-MID → il se fie davantage au titre.
Si Voyage classe ce document en MID-TOP/MID → il se fie davantage au contenu.

### Output Attendu
Produisez un JSON avec :
- Un **titre** évocateur d'excellence
- Un **contenu de minimum 800 mots** décrivant honnêtement des performances moyennes
- Vocabulaire contradictoire entre titre et texte
- **self_validation.semantic_choices** : Expliquez précisément la contradiction et son intensité

**RAPPEL** : Aucune génération de code autorisée. Travail manuel uniquement.

---

## 📋 PROMPT 2/6 : LEURRE_2_DEBUT_VS_FIN_EN

### Spécifications
- **ID** : `LEURRE_2_DEBUT_VS_FIN_EN`
- **Tier** : LEURRES
- **Score** : 65 (MID sur le papier)
- **Language** : English
- **Type** : Structural contradiction (beginning vs end)

### Document Objective
Create a document that **begins very positively** (TOP-tier vocabulary) but **progressively reveals limitations** and **ends with significant weaknesses** (MID-LOW vocabulary).

### Intentional Contradiction
- **First 200-300 words** : Highly positive, excellent performance, strong capabilities
- **Middle 300-400 words** : Gradual introduction of nuances and caveats
- **Last 200-300 words** : Significant limitations, constraints, disappointing real-world performance

### Test Objective
If Voyage ranks this document high → it weights the beginning more heavily.
If Voyage ranks this document low → it weights the end more heavily or considers the overall sentiment.

### Expected Output
Produce a JSON with:
- Content of **minimum 800 words** with clear progression from positive to negative
- Vocabulary shift: TOP → TOP-MID → MID-TOP → MID-LOW throughout the text
- **self_validation.semantic_choices**: Explain precisely the contradiction and the sentiment progression

**REMINDER**: No code generation allowed. Manual work only.

---

## 📋 PROMPT 3/6 : LEURRE_3_SCORE_VS_TEXT_FR

### Spécifications
- **ID** : `LEURRE_3_SCORE_VS_TEXT_FR`
- **Tier** : LEURRES
- **Score** : 88 (TOP sur le papier)
- **Langue** : Français
- **Type** : Contradiction score numérique élevé vs texte négatif

### Objectif du Document
Créez un document qui **mentionne explicitement un score élevé (88)** dans le texte, mais dont le **contenu sémantique décrit une solution LOW ou LOW-MID** (budget, entry-level, limitations majeures).

### Contradiction Intentionnelle
- **Signal numérique** : "score de 88", "performance de 88%", "classé 88 sur 100"
- **Signal sémantique** : Vocabulaire LOW (budget, basique, limité, contraintes majeures, économique)

### Test Visé
Si Voyage classe ce document en TOP → il se fie davantage aux chiffres explicites.
Si Voyage classe ce document en LOW/LOW-MID → il se fie davantage au langage sémantique.

### Output Attendu
Produisez un JSON avec :
- Un contenu de **minimum 800 mots**
- Mention explicite du score "88" plusieurs fois
- Vocabulaire LOW/LOW-MID dominant
- **self_validation.semantic_choices** : Expliquez la contradiction chiffre vs langage

**RAPPEL** : Aucune génération de code autorisée. Travail manuel uniquement.

---

## 📋 PROMPT 4/6 : LEURRE_4_SUBTIL_EN

### Spécifications
- **ID** : `LEURRE_4_SUBTIL_EN`
- **Tier** : LEURRES
- **Score** : 80 (TOP-MID/MID-TOP frontière)
- **Language** : English
- **Type** : Subtle contradiction

### Document Objective
Create a document with **subtle inconsistencies** that are not immediately obvious. The document should oscillate between TOP-MID and MID-TOP signals without clear resolution.

### Intentional Contradiction
- Mix of **near-excellent** and **merely good** vocabulary
- Some paragraphs suggest TOP-MID, others suggest MID-TOP
- No single dominant signal, ambiguous overall positioning

### Test Objective
Test Voyage's ability to handle ambiguous/mixed signals. Where does it position this document when signals are not clear?

### Expected Output
Produce a JSON with:
- Content of **minimum 800 words** with oscillating quality signals
- No dominant tier, balanced mix of TOP-MID and MID-TOP indicators
- **self_validation.semantic_choices**: Explain the subtle ambiguities and mixed signals

**REMINDER**: No code generation allowed. Manual work only.

---

## 📋 PROMPT 5/6 : LEURRE_5_FLAGRANT_FR

### Spécifications
- **ID** : `LEURRE_5_FLAGRANT_FR`
- **Tier** : LEURRES
- **Score** : 92 (TOP sur le papier)
- **Langue** : Français
- **Type** : Contradiction flagrante (multiple)

### Objectif du Document
Créez un document avec des **contradictions multiples et évidentes** :
- Titre TOP + contenu LOW
- Début très positif + milieu négatif + fin positive
- Mentions de chiffres élevés + vocabulaire budget/entry-level

### Contradiction Intentionnelle
Accumulez plusieurs types de contradictions pour créer un document **volontairement incohérent**.

### Test Visé
Test de robustesse extrême : Voyage peut-il être "trompé" par un document adversarial évident ?

### Output Attendu
Produisez un JSON avec :
- Un contenu de **minimum 800 mots** avec multiples contradictions
- Accumulation de signaux conflictuels
- **self_validation.semantic_choices** : Listez toutes les contradictions intentionnelles

**RAPPEL** : Aucune génération de code autorisée. Travail manuel uniquement.

---

## 📋 PROMPT 6/6 : LEURRE_6_INVERSE_EN

### Spécifications
- **ID** : `LEURRE_6_INVERSE_EN`
- **Tier** : LEURRES
- **Score** : 55 (LOW-MID sur le papier)
- **Language** : English
- **Type** : Inverse contradiction (low score, high-quality text)

### Document Objective
Create a document that is the **inverse of typical lures**: assigned a **low score (55)** but with **content describing an excellent, high-performing solution** (TOP/TOP-MID vocabulary).

### Intentional Contradiction
- **Assigned score** : 55 (LOW-MID)
- **Text content** : TOP/TOP-MID quality signals (excellent, state-of-the-art, superior, etc.)
- Optional: mention "score of 55" in text to reinforce the numeric signal

### Test Objective
Test if numeric indicators (low score) can override strong positive semantic signals. Does Voyage follow the number or the language?

### Expected Output
Produce a JSON with:
- Content of **minimum 800 words** with TOP/TOP-MID vocabulary
- Assigned score of 55 creating contradiction
- Optional: explicit mention of "score 55" in text
- **self_validation.semantic_choices**: Explain the inverse contradiction

**REMINDER**: No code generation allowed. Manual work only.

---

## 🔍 Conseils pour la Création de Leurres

### Authenticité des Contradictions

Les contradictions doivent sembler **naturelles** ou du moins **plausibles** :
- ✅ Marketing excessif (titre pompeux) vs réalité technique (performances moyennes)
- ✅ Début prometteur (early results) vs déception à l'usage (limitations réelles)
- ✅ Benchmark spécifique élevé vs performance générale faible
- ❌ Contradictions absurdes qui n'existeraient jamais dans un vrai document

### Intensité des Contradictions

- **Subtile** : Nécessite une lecture attentive pour détecter l'incohérence
- **Modérée** : Contradiction perceptible mais pas choquante
- **Flagrante** : Incohérence évidente, document "cassé"

Variez l'intensité selon les prompts pour tester différents niveaux de sensibilité.

### Objectif Scientifique

Ces leurres ne sont **pas** pour "piéger" Voyage AI, mais pour **comprendre sa pondération interne** :
- Titre vs contenu : quel poids relatif ?
- Position dans le document : début vs milieu vs fin ?
- Signaux numériques vs sémantiques : lesquels dominent ?
- Robustesse : détecte-t-il les incohérences ?

**Les résultats guideront vos décisions architecturales** :
- Si titre > contenu → strategy de chunking différente
- Si début > fin → inclure résumés finaux dans les embeddings
- Si chiffres > sémantique → attention aux benchmarks trompeurs

---

**Sélectionnez UN prompt ci-dessus et produisez le document correspondant.**
