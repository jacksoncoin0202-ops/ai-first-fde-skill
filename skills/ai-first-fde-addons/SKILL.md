---
name: ai-first-fde-addons
description: Use this optional add-on skill only after the no-dependency AI First FDE core has produced the basic artifact and the user wants advanced diagrams, knowledge graphs, eval harnesses, security scans, slide decks, or other dependency-based specialist outputs. Do not use by default.
version: 0.1.0
author: AI First FDE Skill contributors
license: MIT
metadata:
  hermes:
    category: business
    tags: [ai-first, fde-addons, optional-dependencies, diagrams, knowledge-graph, evals, security, presentations]
---

# AI First FDE Optional Add-ons

This skill is optional. It is not required for the standard AI First FDE workflow.

Use the core `ai-first-fde` skill first. Only use this add-on skill when the user asks for an advanced artifact or when the current runtime already has the specialist capability available.

## Boundary

Do not combine dependency-based add-ons into the core FDE skill.

The core FDE skill must remain:

- Markdown-only;
- no-build;
- usable without Python, Node, Docker, browser automation, external connectors, paid APIs, or heavyweight memory systems;
- able to produce useful artifacts with Markdown, Mermaid, tables, and checklists.

This add-on skill may reference capabilities that require installation, connectors, APIs, local CLIs, or runtime-specific tools. Treat them as optional accelerators, not prerequisites.

## Activation rule

Use an add-on only when all conditions are true:

1. The core artifact is already defined.
2. The add-on improves the artifact materially.
3. The tool is already available, or the user explicitly agrees to install / connect it.
4. The add-on does not expose private client information.
5. The add-on does not slow down the FDE decision loop.

If any condition fails, stay with the core Markdown / Mermaid artifact.

## Add-on packs

| Need | Optional capability | Dependency profile | Output |
|---|---|---|---|
| Professional organization / system diagram | architecture-diagram, diagramming, Excalidraw, Figma | May require local skill, connector, or design tool | Organization Architecture Map, approval route, relationship diagram |
| Knowledge graph / relationship graph | graphify | May require Python package or local graph tooling | Interactive graph, GraphRAG-ready JSON, graph report |
| Enterprise knowledge base | llm-wiki | May require local wiki folder and file conventions | Wiki schema, index, source register, log, contradiction tracking |
| Codebase / system onboarding | codebase-onboarding | May require repo access and language tooling | Architecture overview, entrypoints, conventions, handoff notes |
| Evaluation harness | eval-harness, ai-regression-testing, verification-loop | May require test runner, scripts, or model access | Eval cases, pass criteria, regression checks |
| Security and governance | security-threat-model, security-review, security-scan | May require security tools or repo access | Threat model, permission review, security findings |
| Executive enablement | presentations, baoyu-slide-deck, baoyu-infographic | May require deck tooling, rendering, or image generation | Executive deck, training material, infographic |
| Cost / runtime planning | agent-harness-construction, enterprise-agent-ops, cost-aware-llm-pipeline | May require runtime details and model/provider context | Runtime decision table, context strategy, cost route |

## Install separation

Document add-ons separately from the core skill:

- Core install: clone the repository and read Markdown.
- Add-on install: install or connect only the specific optional capability the user needs.

Do not tell users to install every add-on. The correct default is zero add-ons.

## Output contract

Whenever using an add-on, state:

- add-on used;
- why it is needed;
- whether it was already available or required installation;
- what artifact it produced;
- how to proceed if the add-on is unavailable.

## Fallback

If an add-on is unavailable, produce the artifact with the core method:

- diagrams become Mermaid plus tables;
- knowledge graphs become source registers and relationship tables;
- eval harnesses become manual test cases and pass criteria;
- security scans become threat models and review checklists;
- presentations become Markdown executive briefs.
