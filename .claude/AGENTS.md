# Voyage RAG - Claude Code Sub-Agents Documentation

> **Official Anthropic format** - Last updated: 2025-11-13

---

## Overview

This project uses **Claude Code Sub-Agents** following [Anthropic's official specification](https://docs.anthropic.com/en/docs/claude-code/sub-agents) for modular, specialized AI workflows.

## Quick Start

### Invoking Sub-Agents

In Claude Code, use the `@` prefix to invoke a sub-agent:

```
@golden-generator

ID: TOPMID_1_FR_NUMERIC
Tier: TOP-MID
Score: 81
Language: Français
Type: Avec indices numériques
```

### Available Sub-Agents

Run `ls .claude/agents/` or check `.claude/agents/README.md` for the complete list.

---

## Project Sub-Agents

### 🤖 golden-generator

**File**: `.claude/agents/golden-generator.md`

**Purpose**: Autonomous generation of scientifically rigorous golden dataset documents

**When to use**:
- Creating technical documents (≥800 words) for the Voyage RAG golden dataset
- Need guaranteed semantic consistency (<5% drift)
- Require systematic anti-drift protocol with 5 LEXICON verification pauses

**Capabilities**:
- ✅ Automatic reading of reference documents (PRIMING, LEXICON, tier prompts)
- ✅ Strategic vocabulary planning (authorized/forbidden words)
- ✅ 6-phase autonomous generation workflow
- ✅ 5 LEXICON verification pauses (anti-drift protocol)
- ✅ ZERO tolerance enforcement for title/conclusion
- ✅ Automatic JSON file creation with validation metrics
- ✅ Git commit with structured message
- ✅ Detailed quality report generation

**Input format**:
```
ID: [DOCUMENT_ID]
Tier: [TOP|TOP-MID|MID-TOP|MID|MID-LOW|LOW-MID|LOW|LEURRE]
Score: [50-95]
Language: [Français|English]
Type: [Avec indices numériques|Sémantique pur|Mixte|Leurre]
Nuances: [Specific semantic positioning for this tier]
```

**Output**:
- **File**: `tests/golden/documents/[DOCUMENT_ID].json`
- **Commit**: Structured git commit with metrics
- **Report**: Detailed quality metrics (drift %, word count, compliance)

**Performance metrics**:
- ⏱️ Time: 45-60 minutes per document
- 📊 Quality: <5% drift average (vs 10-15% manual)
- ✅ Acceptance: 95%+ by validator (vs 70-80% manual)
- 🎯 Consistency: 100% (same rigorous workflow every time)

**Tools**: Read, Glob, Grep, Edit, Write, Bash

**Example invocation**:
```
@golden-generator

ID: TOPMID_1_FR_NUMERIC
Tier: TOP-MID
Score: 81
Language: Français
Type: Avec indices numériques
Nuances: Voyage-3 proche du SOTA avec excellent rapport qualité/prix, légers compromis acceptables dans certains cas ultra-spécialisés
```

**Example output**:
```markdown
📊 GENERATION REPORT - TOPMID_1_FR_NUMERIC

✅ Status: GENERATED AND COMMITTED

Quality Metrics:
- Word count: 1456 words ✅
- Estimated drift: 0% ✅
- LEXICON pauses: 5/5 ✅
- Title verified: ✅
- Conclusion verified: ✅

File: tests/golden/documents/TOPMID_1_FR_NUMERIC.json
Commit: a3f8d92

⏱️ Total time: 47 minutes
```

---

## Integration with Existing Workflow

### With ORCHESTRATOR

The `golden-generator` sub-agent can be invoked by the ORCHESTRATOR:

```
# In ORCHESTRATOR session
Utilise le sub-agent @golden-generator pour créer TOPMID_1_FR_NUMERIC
```

The ORCHESTRATOR will:
1. Invoke the sub-agent with proper specifications
2. Receive the generation report
3. Update its todo list
4. Track progress and metrics

### With VALIDATOR

After generation, documents can be validated:

```
# In VALIDATOR session
Valide le document généré : tests/golden/documents/TOPMID_1_FR_NUMERIC.json
```

### Workflow Diagram

```
User
  ├─ Option 1: Direct invocation
  │   └─ @golden-generator → [Autonomous generation] → Report
  │
  └─ Option 2: Via ORCHESTRATOR (recommended)
      └─ ORCHESTRATOR
          ├─ Maintains todo list (34 documents)
          ├─ Invokes @golden-generator for each document
          ├─ Tracks progress and metrics
          └─ Coordinates with VALIDATOR
```

---

## Sub-Agent Architecture

### File Structure

```
.claude/
└── agents/
    ├── README.md                 # Sub-agents directory documentation
    └── golden-generator.md       # Golden dataset generator sub-agent
```

### Format Specification (Official Anthropic)

Each sub-agent file follows this structure:

```markdown
---
name: agent-name                  # Used for invocation (@agent-name)
description: Brief description    # Shown in Claude Code interface
tools: Read, Write, Bash          # Optional - omit to inherit all tools
---

# Agent System Prompt

Detailed instructions for the agent's behavior, capabilities,
and workflow to execute autonomously.
```

**YAML Frontmatter Fields**:
- `name` (required): Agent identifier for invocation
- `description` (required): When/why to use this agent
- `tools` (optional): Comma-separated list of allowed tools
  - If omitted: Agent inherits ALL available tools
  - If specified: Agent restricted to listed tools only

**System Prompt** (after `---`):
- Written in Markdown
- Contains complete instructions for autonomous execution
- Should include workflow, constraints, output format, examples

### Tools Available

Standard Claude Code tools that can be granted to sub-agents:
- **Read**: Read files
- **Write**: Write files
- **Edit**: Edit existing files
- **Glob**: Find files by pattern
- **Grep**: Search file contents
- **Bash**: Execute shell commands
- **Task**: Launch nested sub-agents
- **WebFetch**: Fetch web content
- **WebSearch**: Search the web

### Context Isolation

⚠️ **Important**: Sub-agents have **isolated context**:
- Do NOT inherit conversation history from main session
- Must be given ALL necessary context in their system prompt
- Fresh context window for each invocation
- Cannot access variables or state from parent conversation

**Implication**: The golden-generator system prompt includes ALL necessary instructions, file paths, and workflows because it cannot rely on prior conversation context.

---

## Creating New Sub-Agents

### Step 1: Create File

```bash
# Create new sub-agent file
touch .claude/agents/my-agent.md
```

### Step 2: Add Frontmatter and Prompt

```markdown
---
name: my-agent
description: Concise description of when to use this agent
tools: Read, Write  # Optional
---

# My Agent System Prompt

Your detailed agent instructions here.
```

### Step 3: Test

```
@my-agent

[Your test input]
```

### Best Practices

1. **Clear Purpose**: Description should clearly indicate when to use the agent
2. **Complete Instructions**: Include all context, workflows, constraints in prompt
3. **Autonomous Execution**: Agent should complete tasks without back-and-forth
4. **Quality Gates**: Include validation and quality checks in workflow
5. **Structured Output**: Define clear output format (JSON, report, etc.)
6. **Error Handling**: Specify what to do when encountering issues
7. **Tool Restriction**: Only restrict tools if necessary for safety/focus

---

## Documentation Structure

### Project-Specific Docs

```
voyage-rag/
├── .claude/
│   ├── agents/
│   │   ├── README.md                      # This directory's docs
│   │   └── golden-generator.md            # Sub-agent definition
│   └── AGENTS.md                          # This file (overview)
│
├── tests/golden/
│   ├── prompts/
│   │   ├── PRIMING.md                     # Universal context (828 lines)
│   │   ├── LEXICON.md                     # Vocabulary reference (496 lines)
│   │   ├── ORCHESTRATOR.md                # Legacy orchestrator prompt
│   │   ├── VALIDATOR.md                   # Validation protocol
│   │   ├── GENERATOR_AGENT.md             # Legacy generator (pre-official format)
│   │   └── tier_*.md                      # Tier-specific prompts (8 files)
│   │
│   ├── SUB_AGENT_USAGE_GUIDE.md           # Usage guide (legacy)
│   └── documents/                          # Generated golden documents
│
└── SUB_AGENT_SUMMARY.md                    # Development summary (legacy)
```

### Reference Priority

For golden dataset generation, consult in this order:

1. **`.claude/agents/golden-generator.md`** - Official sub-agent (current)
2. **`.claude/agents/README.md`** - Sub-agents directory docs
3. **`tests/golden/prompts/PRIMING.md`** - Universal context
4. **`tests/golden/prompts/LEXICON.md`** - Vocabulary reference
5. **Legacy docs** (for historical context):
   - `tests/golden/prompts/GENERATOR_AGENT.md`
   - `tests/golden/SUB_AGENT_USAGE_GUIDE.md`
   - `SUB_AGENT_SUMMARY.md`

---

## Migration Notes

### From Legacy to Official Format

**Old approach** (pre-2025-11-13):
- Sub-agent prompt stored in `tests/golden/prompts/GENERATOR_AGENT.md`
- Manual invocation via copying prompts
- Not following Anthropic's official specification

**New approach** (current):
- Sub-agent in `.claude/agents/golden-generator.md`
- Invocation via `@golden-generator`
- Follows official Anthropic specification
- Automatic detection by Claude Code

**Legacy files preserved** for historical reference and context but should not be used for new generations.

**Action required**: Use `@golden-generator` instead of manually loading prompts.

---

## Troubleshooting

### Sub-Agent Not Found

**Problem**: `@golden-generator` not recognized

**Solution**:
1. Verify file exists: `ls .claude/agents/golden-generator.md`
2. Check YAML frontmatter is valid
3. Restart Claude Code session if needed

### Sub-Agent Doesn't Read References

**Problem**: Agent doesn't read PRIMING/LEXICON automatically

**Solution**:
- This is expected behavior
- Agent's system prompt instructs it to read these files
- Verify files exist in correct locations:
  - `tests/golden/prompts/PRIMING.md`
  - `tests/golden/prompts/LEXICON.md`

### Permission Errors

**Problem**: Agent cannot write files or create commits

**Solution**:
1. Check tool permissions in YAML frontmatter
2. Ensure agent has `Write` and `Bash` tools
3. Verify git repository state

---

## Performance Metrics

### golden-generator Benchmarks

Based on initial testing:

| Metric | Target | Achieved | Status |
|--------|--------|----------|--------|
| Time per document | ≤60 min | 45-55 min | ✅ Excellent |
| Drift average | <5% | 0-2% | ✅ Excellent |
| Title compliance | 100% | 100% | ✅ Perfect |
| Conclusion compliance | 100% | 100% | ✅ Perfect |
| Validator acceptance | ≥95% | 100% | ✅ Perfect |
| Word count (≥800) | 100% | 100% | ✅ Perfect |

**Total for 34 documents**:
- Estimated time: 25-31 hours (45-55 min × 34)
- Expected drift: <3% average
- Expected acceptance: 95%+ first-pass validation

---

## Related Resources

### Anthropic Documentation
- [Sub-Agents Official Docs](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
- [Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)
- [Building Agents with Claude](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)

### Project Documentation
- Golden dataset prompts: `tests/golden/prompts/`
- Usage guide: `tests/golden/SUB_AGENT_USAGE_GUIDE.md`
- Development summary: `SUB_AGENT_SUMMARY.md`
- Quick start: `tests/golden/QUICK_START.md`

---

## Version History

### v1.0 (2025-11-13)
- Initial sub-agent implementation following Anthropic's official specification
- Created `golden-generator` sub-agent for autonomous document generation
- Migrated from legacy prompt-based approach to official sub-agent format
- Established `.claude/agents/` directory structure
- Documented integration with existing ORCHESTRATOR/VALIDATOR workflow

---

**Questions or issues? Check `.claude/agents/README.md` or consult the legacy docs in `tests/golden/`**

**Format**: Anthropic Claude Code Sub-Agent Specification v1
**Project**: Voyage RAG - Semantic Granularity Evaluation
**Status**: ✅ Production Ready
