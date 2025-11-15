# PROMPT DE CORRECTION - TOP_3_EN_NUMERIC (Document 03/23)

**Document ID** : TOP_3_EN_NUMERIC
**Tier Cible** : TOP (86-92)
**Score Actuel** : 90/100 (claim) → 82/100 (réel)
**Drift Actuel** : 3.47-5.7% (global), 10.5% (conclusion - CRITICAL)
**Objectif** : Score 98/100, Drift 0%

---

## MISSION DE CORRECTION

You must correct **5 lexical drifts** detected in the document TOP_3_EN_NUMERIC to eliminate all out-of-tier vocabulary and achieve perfect TOP tier compliance.

**Main Problem**: Double drift in CONCLUSION (ZERO TOLERANCE ZONE): "proven production excellence" combines MID-TOP word (line 138) + TOP-MID word (line 94) in the final sentence.

---

## LEXICAL CONTEXT - TOP TIER

### Authorized TOP Vocabulary (LEXICON.md lines 21-66)

**Absolute Superlatives**:
- the best | unmatched | revolutionary | exceptional | without equivalent | incomparable | optimal (absolute) | superior | reference

**TOP Expressions**:
- state-of-the-art | unchallenged leader | unmatched performance | far exceeds | absolute reference | breakthrough innovation | surpasses all competitors | dominance

**TOP PROHIBITIONS**:
- ❌ "excellence" (TOP-MID line 94 "of excellence")
- ❌ "remarkable/outstanding" (TOP-MID line 85, 93)
- ❌ "robust/robustness" (MID-TOP line 135)
- ❌ "proven" (MID-TOP line 138 "éprouvé | proven | Maturity, track record")
- ❌ "versatile/versatility" (MID-TOP line 141)

---

## DRIFTS TO CORRECT (5 occurrences)

### 🔴 MAXIMUM PRIORITY: Double Drift in CONCLUSION

### ❌ DRIFT #1 & #2: "proven production excellence" (CONCLUSION - Paragraph 6, Sentence 4)

**BEFORE** (original text):
```
"Organizations seeking the best possible outcomes for their RAG implementations have a clear choice: Voyage-3 stands alone as the state-of-the-art solution, combining optimal technical architecture with proven production excellence."
```

**Problems**:
- "proven" → LEXICON line 138 (MID-TOP): "éprouvé | proven | Maturité, track record"
- "excellence" → LEXICON line 94 (TOP-MID): "d'excellence | of excellence"
- **CRITICAL ZONE**: Conclusion = ZERO TOLERANCE (LEXICON lines 396-397)
- **DOUBLE DRIFT**: Single phrase contains 2 out-of-tier words (MID-TOP + TOP-MID)

**REQUIRED CORRECTION**:
```
"Organizations seeking the best possible outcomes for their RAG implementations have a clear choice: Voyage-3 stands alone as the state-of-the-art solution, combining optimal technical architecture with exceptional production performance."
```

**Acceptable Alternatives**:
- "with superior production capability"
- "with unmatched production quality"
- "with validated production superiority"
- "demonstrating exceptional production performance"

---

### 🟠 HIGH PRIORITY: Other "excellence" occurrence

### ❌ DRIFT #3: "technical excellence" (Paragraph 5, Sentence 2)

**BEFORE**:
```
"This widespread adoption reflects not just technical excellence, but the model's proven ability to deliver measurable business value through superior search relevance, reduced development time, and lower operational costs."
```

**Problem**:
- "excellence" → LEXICON line 94 (TOP-MID)
- **DOUBLE DRIFT**: This sentence also contains "proven" (see DRIFT #4)

**REQUIRED CORRECTION**:
```
"This widespread adoption reflects not just exceptional technical capability, but the model's demonstrated ability to deliver measurable business value through superior search relevance, reduced development time, and lower operational costs."
```

**Acceptable Alternatives**:
- "technical superiority"
- "superior technical design"
- "unparalleled technical performance"
- "exceptional technical architecture"

---

### 🟠 HIGH PRIORITY: Other "proven" occurrence

### ❌ DRIFT #4: "proven ability" (Paragraph 5, Sentence 2)

**BEFORE**:
```
"This widespread adoption reflects not just technical excellence, but the model's proven ability to deliver measurable business value through superior search relevance, reduced development time, and lower operational costs."
```

**Problem**:
- "proven" → LEXICON line 138 (MID-TOP): "éprouvé | proven | Maturité, pas innovation"
- Contradicts TOP tier focus on "revolutionary" and "breakthrough"
- **DOUBLE DRIFT**: Sentence also contains "excellence" (DRIFT #3)

**REQUIRED CORRECTION**:
```
"This widespread adoption reflects not just exceptional technical capability, but the model's demonstrated ability to deliver measurable business value through superior search relevance, reduced development time, and lower operational costs."
```

**Acceptable Alternatives**:
- "validated ability" (neutral - acceptable)
- "unmatched ability"
- Simply remove "proven" (redundant with metrics throughout document)

---

### 🟠 MEDIUM PRIORITY: MID-TOP vocabulary

### ❌ DRIFT #5: "robustness" (Paragraph 4, Sentence 3)

**BEFORE**:
```
"The model's robustness under diverse query patterns is equally impressive: precision@5 remains above 0.92 even with intentionally ambiguous queries, while recall@100 consistently exceeds 0.95 across document collections ranging from 10,000 to 10 million items."
```

**Problem**:
- "robustness" → LEXICON line 135 (MID-TOP): "robuste | robust | Résiste bien, fiable"
- MID-TOP tier vocabulary emphasizes "Fiabilité sans éclat" (reliability without brilliance)
- TOP tier requires absolute superlatives

**REQUIRED CORRECTION**:
```
"The model's exceptional reliability under diverse query patterns is equally impressive: precision@5 remains above 0.92 even with intentionally ambiguous queries, while recall@100 consistently exceeds 0.95 across document collections ranging from 10,000 to 10 million items."
```

**Acceptable Alternatives**:
- "unmatched stability"
- "superior resilience"
- "exceptional consistency"
- "unparalleled reliability"

---

## CORRECTION INSTRUCTIONS

1. **ABSOLUTE PRIORITY**: Correct "proven production excellence" in CONCLUSION → "exceptional production performance"
2. **HIGH PRIORITY**: Correct "technical excellence" (paragraph 5) → "exceptional technical capability"
3. **HIGH PRIORITY**: Correct "proven ability" (paragraph 5) → "demonstrated ability"
4. **MEDIUM PRIORITY**: Correct "robustness" (paragraph 4) → "exceptional reliability"
5. **Verify** no other TOP-MID or MID-TOP words were added
6. **Maintain** all other TOP-compliant qualifiers (72 already correct)
7. **Preserve** document length (890 words ±5%)
8. **Regenerate** `self_validation` section with:
   - Corrected drift: 0%
   - 144 qualifiers analyzed (not 15)
   - Mention of 5 corrections applied

---

## POST-CORRECTION VALIDATION

After correction, the document must achieve:
- **Drift**: 0% (0/144 out-of-tier words)
- **Score**: 98/100
- **Critical Zones**: Title ✓ + Conclusion ✓ (100% TOP compliant)
- **Prohibited words**: 0 (no "excellence", "proven", "robustness", "remarkable")

---

## OUTPUT FORMAT

Return complete JSON with:
1. `text` field: corrected text with 5 modifications
2. `self_validation.semantic_choices`: mention 5 corrections applied and list 144 qualifiers analyzed
3. `self_validation.quality_check`: note "Final drift: 0% (5 corrections applied on 144 qualifiers analyzed, including 2 CRITICAL corrections in CONCLUSION)"

---

## QUICK REPLACEMENT TABLE

| BEFORE (out-of-tier) | AFTER (TOP pure) |
|----------------------|------------------|
| proven production excellence | exceptional production performance |
| technical excellence | exceptional technical capability |
| proven ability | demonstrated ability |
| robustness | exceptional reliability |

---

## CRITICAL REMINDER

**ZERO TOLERANCE ZONE VIOLATED**: The conclusion currently contains 2 drifts (10.5%). This is the HIGHEST PRIORITY correction to restore TOP tier compliance.

**Drift breakdown**:
- Title: 0% ✓
- Body (paragraphs 1-5): 2.5% ✓
- **Conclusion: 10.5% ❌ CRITICAL VIOLATION**

After correction:
- Title: 0% ✓
- Body: 0% ✓
- Conclusion: 0% ✓

---

**Objective**: Eliminate 100% of drift (3.47-5.7% → 0%) to raise score from 82/100 to 98/100 and confirm TOP tier classification.
