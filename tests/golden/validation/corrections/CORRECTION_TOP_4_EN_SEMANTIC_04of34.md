# PROMPT DE CORRECTION - TOP_4_EN_SEMANTIC (Document 04/34)

**Document ID** : TOP_4_EN_SEMANTIC
**Tier Cible** : TOP (86-92)
**Score Actuel** : 86/100 (claim) → 84/100 (réel)
**Drift Actuel** : 3.68% (global), 25% (titre), 2 drifts (conclusion)
**Objectif** : Score 98/100, Drift 0%

---

## MISSION DE CORRECTION

You must correct **6 lexical drifts** detected in the document TOP_4_EN_SEMANTIC to eliminate all out-of-tier vocabulary and achieve perfect TOP tier compliance.

**CRITICAL PROBLEM**: TITLE and CONCLUSION (both ZERO TOLERANCE ZONES) are contaminated:
- **TITLE**: Contains "Excellence" (TOP-MID line 94)
- **CONCLUSION**: Contains "versatility" (MID-TOP line 141) + "excellence" (TOP-MID line 94)
- **SYSTEMATIC PATTERN**: "versatility" used 3 times throughout document (all MID-TOP drifts)

---

## LEXICAL CONTEXT - TOP TIER

### Authorized TOP Vocabulary (LEXICON.md lines 21-66)

**Absolute Superlatives**:
- the best | unmatched | revolutionary | exceptional | without equivalent | incomparable | optimal (absolute) | superior | supremacy

**TOP Expressions**:
- state-of-the-art | unchallenged leader | unmatched performance | absolute reference | breakthrough innovation | dominance

**TOP PROHIBITIONS**:
- ❌ "excellence" (TOP-MID line 94 "of excellence")
- ❌ "outstanding/remarkable" (TOP-MID lines 93, 85)
- ❌ "versatile/versatility" (MID-TOP line 141 "polyvalent | versatile | Flexibilité")
- ❌ "robust/robustness" (MID-TOP line 135)
- ❌ "proven" (MID-TOP line 138)

---

## DRIFTS TO CORRECT (6 occurrences)

### 🔴 ABSOLUTE PRIORITY: TITLE (ZERO TOLERANCE ZONE)

### ❌ DRIFT #1: "Excellence" (TITLE)

**BEFORE** (current title):
```
"Revolutionary Breakthrough in Semantic Embeddings: The Unmatched Standard for RAG Excellence"
```

**Problem**:
- "excellence" → LEXICON line 94 (TOP-MID): "d'excellence | of excellence"
- **CRITICAL ZONE**: Title = ZERO TOLERANCE (LEXICON lines 396-397)
- TOP tier must use "Supremacy", "Superiority", "Dominance", NOT "Excellence"
- Title is the first impression and most visible element

**REQUIRED CORRECTION**:
```
"Revolutionary Breakthrough in Semantic Embeddings: The Unmatched Standard for RAG Supremacy"
```

**Acceptable Alternatives**:
- "The Unmatched Standard for RAG Superiority"
- "The Absolute Reference for RAG Systems"
- "The Undisputed Leader in RAG Technology"
- "The Ultimate Standard in RAG Performance"

**Impact**: **MAXIMUM SEVERITY** - Title contamination disqualifies document per LEXICON zero-tolerance rule.

---

### 🔴 MAXIMUM PRIORITY: CONCLUSION (ZERO TOLERANCE ZONE)

### ❌ DRIFT #2: "standard of excellence" (CONCLUSION - Final sentence)

**BEFORE**:
```
"The technological leap these innovations represent ensures their position as the undisputed leaders in the field. They don't merely meet requirements—they exceed expectations, delivering transformative capabilities that fundamentally outperform all alternatives. This is the new standard of excellence in semantic embeddings."
```

**Problem**:
- "excellence" → LEXICON line 94 (TOP-MID)
- **CRITICAL ZONE**: Conclusion = ZERO TOLERANCE (LEXICON lines 396-397)
- Final sentence of document = last impression = CRITICAL

**REQUIRED CORRECTION**:
```
"This is the new standard of superiority in semantic embeddings."
```

**Acceptable Alternatives**:
- "This is the new benchmark of supremacy in semantic embeddings."
- "This represents the absolute reference standard in semantic embeddings."
- "This defines the pinnacle of semantic embedding technology."
- "This establishes the definitive standard for semantic embeddings."

**Impact**: **MAXIMUM SEVERITY** - Conclusion contamination + final word of document = double violation.

---

### ❌ DRIFT #3: "unparalleled versatility" (CONCLUSION - Paragraph 13)

**BEFORE**:
```
"State-of-the-art embedding technologies deliver unmatched semantic precision, exceptional contextual awareness, and unparalleled versatility."
```

**Problem**:
- "versatility" → LEXICON line 141 (MID-TOP): "polyvalent | versatile | Flexibilité"
- **CRITICAL ZONE**: Conclusion = ZERO TOLERANCE
- **CONTRADICTION**: "unparalleled" (TOP) + "versatility" (MID-TOP) = lexical oxymoron
- 3rd occurrence of systematic "versatility" drift

**REQUIRED CORRECTION**:
```
"State-of-the-art embedding technologies deliver unmatched semantic precision, exceptional contextual awareness, and unparalleled adaptability."
```

**Acceptable Alternatives**:
- "and exceptional breadth of capability"
- "and universal applicability"
- "and comprehensive domain coverage"
- "and unmatched scope"

**Impact**: **MAXIMUM SEVERITY** - Conclusion + contradictory TOP+MID-TOP combination.

---

### 🟠 HIGH PRIORITY: Systematic "versatility" pattern

### ❌ DRIFT #4: "versatility" (Paragraph 9)

**BEFORE**:
```
"Their versatility combined with unmatched performance makes them the optimal choice for any serious retrieval-augmented generation implementation."
```

**Problem**:
- "versatility" → LEXICON line 141 (MID-TOP)
- First occurrence of systematic pattern (word appears 3 times total)

**REQUIRED CORRECTION**:
```
"Their exceptional adaptability combined with unmatched performance makes them the optimal choice for any serious retrieval-augmented generation implementation."
```

**Acceptable Alternatives**:
- "Their unmatched breadth"
- "Their universal applicability"
- "Their comprehensive capabilities"

---

### ❌ DRIFT #5: "versatility" (Paragraph 11 - repetition)

**BEFORE**:
```
"This versatility eliminates the traditional tradeoff between specialization and generalization—the best modern embeddings achieve both simultaneously."
```

**Problem**:
- "versatility" → LEXICON line 141 (MID-TOP) - 2nd occurrence
- Repetition of same drift = SYSTEMATIC PATTERN

**REQUIRED CORRECTION**:
```
"This exceptional adaptability eliminates the traditional tradeoff between specialization and generalization—the best modern embeddings achieve both simultaneously."
```

**Acceptable Alternatives**:
- "This universal capability"
- "This comprehensive mastery"
- "This dual supremacy"

---

### 🟠 MEDIUM PRIORITY: Other TOP-MID vocabulary

### ❌ DRIFT #6: "outstanding performance" (Paragraph 11)

**BEFORE**:
```
"They excel not just on the specific domains where they were optimized but demonstrate exceptional transfer learning capabilities, delivering outstanding performance on entirely novel tasks and content types."
```

**Problem**:
- "outstanding" → LEXICON line 93 (TOP-MID): "remarquable | outstanding | Performance notable"
- TOP-MID tier (lines 69-123) = "Nuances Proches du Sommet"
- TOP tier requires "exceptional", "unmatched", "unparalleled"

**REQUIRED CORRECTION**:
```
"delivering exceptional performance on entirely novel tasks and content types."
```

**Acceptable Alternatives**:
- "delivering unmatched performance"
- "delivering unparalleled performance"
- "delivering superior performance"

---

## CORRECTION INSTRUCTIONS

1. **ABSOLUTE PRIORITY**: Correct "Excellence" in TITLE → "Supremacy"
2. **ABSOLUTE PRIORITY**: Correct "standard of excellence" in CONCLUSION → "standard of superiority"
3. **ABSOLUTE PRIORITY**: Correct "unparalleled versatility" in CONCLUSION → "unparalleled adaptability"
4. **HIGH PRIORITY**: Eliminate ALL 3 occurrences of "versatility" → "exceptional adaptability"
5. **HIGH PRIORITY**: Correct "outstanding performance" → "exceptional performance"
6. **Verify**: No other TOP-MID or MID-TOP words added
7. **Maintain**: All other TOP-compliant qualifiers (157 already correct - 96.32%)
8. **Preserve**: Document length (894 words ±5%)
9. **Preserve**: SEMANTIC purity (NO numeric metrics - already compliant ✓)
10. **Regenerate**: `self_validation` section with:
    - Corrected drift: 0%
    - 163 qualifiers analyzed (not 15)
    - Mention of 6 corrections applied
    - Specific note: "TITLE and CONCLUSION corrected to achieve zero-tolerance compliance"

---

## POST-CORRECTION VALIDATION

After correction, the document must achieve:
- **Drift**: 0% (0/163 out-of-tier words)
- **Score**: 98/100
- **Critical Zones**: Title ✓ (0% drift, 4/4 TOP) + Conclusion ✓ (0% drift, 100% TOP)
- **Prohibited words**: 0 (no "excellence", "versatility", "outstanding", "remarkable")
- **Systematic patterns**: 0 (no repetition of out-of-tier vocabulary)

---

## OUTPUT FORMAT

Return complete JSON with:
1. `title` field: corrected title WITHOUT "excellence"
2. `text` field: corrected text with 5 modifications (3× "versatility", 1× "outstanding", 1× "excellence")
3. `self_validation.semantic_choices`: mention 6 corrections applied (including TITLE) and list 163 qualifiers analyzed
4. `self_validation.quality_check`: note "Final drift: 0% (6 corrections applied on 163 qualifiers analyzed, including 3 CRITICAL corrections in ZERO TOLERANCE ZONES: title + conclusion)"

---

## QUICK REPLACEMENT TABLE

| BEFORE (out-of-tier) | AFTER (TOP pure) | Location |
|----------------------|------------------|----------|
| Excellence | Supremacy | TITLE (CRITICAL) |
| standard of excellence | standard of superiority | Conclusion final sentence |
| unparalleled versatility | unparalleled adaptability | Conclusion paragraph 13 |
| Their versatility | Their exceptional adaptability | Paragraph 9 |
| This versatility | This exceptional adaptability | Paragraph 11 |
| outstanding performance | exceptional performance | Paragraph 11 |

---

## SYSTEMATIC PATTERN ELIMINATION

**Pattern detected**: "versatility" appears 3 times
1. Paragraph 9: "Their versatility combined"
2. Paragraph 11: "This versatility eliminates"
3. Paragraph 13 (CONCLUSION): "unparalleled versatility"

**Correction strategy**: Replace ALL instances with "exceptional adaptability" or context-appropriate TOP-tier synonym.

**Why "versatility" is forbidden**:
- LEXICON line 141: "polyvalent | versatile | Flexibilité" = MID-TOP tier (scores 72-77)
- Emphasizes "Flexibilité" (flexibility) not "Supériorité absolue" (absolute superiority)
- TOP tier requires absolute superlatives, not practical flexibility

---

## CRITICAL REMINDER

**ZERO TOLERANCE ZONES VIOLATED**:
- **TITLE**: 1 drift (25% of title qualifiers) ❌
- **CONCLUSION**: 2 drifts (in zero-tolerance zone) ❌

**Current status**:
- Global drift: 3.68% ✓ (below 10% threshold)
- BUT critical zones contaminated = **BLOCKING ISSUES**

**After correction**:
- Global drift: 0% ✓
- Title drift: 0% ✓
- Conclusion drift: 0% ✓
- Score: 84 → 98/100 ✓

---

## PARADOX RESOLUTION

**Current situation**:
- 96.32% of vocabulary is TOP-compliant (excellent)
- BUT the 3.68% drift is concentrated in the most visible zones (title + conclusion)
- Perceptual impact >> statistical impact

**Solution**:
- Eliminate the 6 strategic drifts (especially in title + conclusion)
- Preserve the 157 correct TOP qualifiers
- Result: 100% TOP compliance with minimal changes (6 words out of 894)

---

**Objective**: Eliminate 100% of drift (3.68% → 0%), restore title and conclusion to zero-tolerance compliance, raise score from 84/100 to 98/100, and confirm TOP tier classification.
