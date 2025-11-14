# Claude Code Sub-Agents

This directory contains custom sub-agents for the Voyage RAG project, following [Anthropic's official sub-agent specification](https://docs.anthropic.com/en/docs/claude-code/sub-agents).

## Available Sub-Agents

### 🤖 golden-generator

**Purpose**: Autonomous generation of golden dataset documents with anti-drift protocol

**When to use**: Creating high-quality technical documents (800+ words) for the Voyage RAG golden dataset with guaranteed semantic consistency (<5% drift).

**How to invoke**:

```
@golden-generator

ID: TOPMID_1_FR_NUMERIC
Tier: TOP-MID
Score: 81
Language: Français
Type: Avec indices numériques
Nuances: Excellence proche du SOTA avec excellent rapport qualité/prix
```

**What it does automatically**:
1. Reads PRIMING, LEXICON, and tier-specific prompts
2. Plans vocabulary (authorized/forbidden words)
3. Writes document with 5 LEXICON verification pauses
4. Creates JSON file with validation metrics
5. Creates git commit
6. Generates detailed quality report

**Expected output**:
- Document: `tests/golden/documents/[DOCUMENT_ID].json`
- Commit: Structured message with metrics
- Report: Quality metrics (drift %, word count, compliance)

**Performance**:
- Time: 45-60 minutes per document
- Quality: <5% drift average
- Acceptance rate: 95%+ by validator

**Tools available**: Read, Glob, Grep, Edit, Write, Bash

---

## Directory Structure

```
.claude/
└── agents/
    ├── README.md              # This file
    └── golden-generator.md    # Golden dataset document generator
```

## How Sub-Agents Work

Sub-agents are specialized AI assistants that:
- Have their own context window (isolated from main conversation)
- Follow custom system prompts defined in their `.md` files
- Can access specific tools (or all tools if not restricted)
- Are invoked with `@agent-name` in Claude Code

## Creating New Sub-Agents

To create a new sub-agent:

1. Create a new `.md` file in this directory
2. Add YAML frontmatter with required fields:

```markdown
---
name: my-agent
description: Brief description of when to use this agent
tools: Read, Write, Bash  # Optional - omit to inherit all tools
---

Your agent's system prompt goes here.
```

3. Write detailed instructions for the agent's behavior

## Best Practices

- **Specificity**: Make agent descriptions clear about when to use them
- **Autonomy**: Agents should execute complete workflows independently
- **Tools**: Only restrict tools if necessary for safety/focus
- **Context**: Agents start fresh - provide all necessary context in prompt
- **Validation**: Include quality checks and validation in agent workflows

## Related Documentation

- **Main golden dataset docs**: `tests/golden/prompts/`
- **Usage guide**: `tests/golden/SUB_AGENT_USAGE_GUIDE.md`
- **Development summary**: `SUB_AGENT_SUMMARY.md`
- **Anthropic docs**: https://docs.anthropic.com/en/docs/claude-code/sub-agents

## Testing Sub-Agents

To test the golden-generator:

```
@golden-generator

ID: TEST_DOC
Tier: TOP-MID
Score: 80
Language: Français
Type: Test document
Nuances: Test generation workflow
```

Verify output in `tests/golden/documents/TEST_DOC.json`

---

**Project**: Voyage RAG - Semantic Search with Voyage AI Embeddings
**Last Updated**: 2025-11-13
**Format**: Anthropic Claude Code Sub-Agent Specification v1
