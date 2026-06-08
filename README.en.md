# AI First FDE Skill

AI First FDE Skill is a Markdown-only, no-build skill suite for Forward Deployed Engineer style enterprise AI deployment in East Asian organizations.

It is designed for transformation, not headcount reduction. In many East Asian companies, AI adoption succeeds when it protects expertise, reduces overtime, removes repetitive work, and helps teams move into higher-value roles without humiliating the people who built the current process. That is a product advantage, not a soft footnote: the skill treats trust, face-saving, seniority, consensus, and human transition as first-class deployment constraints.

## Quick Start

```bash
git clone https://github.com/jacksoncoin0202-ops/ai-first-fde-skill.git
cd ai-first-fde-skill
```

Tell your agent:

```text
Read skills/ai-first-fde/SKILL.md first.
If the task needs research, diagnostic interview, architecture, deployment, troubleshooting, adoption observation, organization mapping, or knowledge-base planning, read the matching skills/ai-first-fde-* module and skills/ai-first-fde/references/.
```

You can use this with any agent runtime that can read Markdown project rules: Claude Code, OpenAI Codex CLI, Cursor, Hermes, OpenCode, Gemini CLI, Cline, Aider, Continue, Devin CLI, OpenRouter-backed agents, or similar tools.

## Language

- [English](README.en.md)
- [繁體中文](README.zh-Hant.md)
- [日本語](README.ja.md)

## Why This Exists

Enterprise AI projects rarely fail because nobody can write a prompt. They fail because the deployment surface is messy.

The real blockers are usually hidden in the business process:

- the workflow has no written owner;
- the authoritative data source is unclear;
- approval happens through informal relationships;
- senior reviewers do not trust AI output quality;
- daily users fear blame, extra work, or replacement;
- legal, security, compliance, procurement, or IT are contacted too late;
- the pilot has no measurable KPI;
- the solution is built before the organization structure is understood;
- the knowledge base is scattered across email, spreadsheets, chat, PDFs, ticket systems, and personal memory.

AI First FDE Skill turns those problems into an operating sequence. It tells an agent what to ask, what to map, what to produce, when to stop, and what evidence is required before expanding from PoC to pilot to rollout.

## East Asia Transformation Stance

This skill is intentionally not a Western "replace people with automation" playbook.

For Japan, Hong Kong, Taiwan, Korea, Singapore, and culturally adjacent enterprise teams, the adoption strategy is different:

- Position AI as a way to reduce overtime, rework, context switching, and cognitive load.
- Preserve the role of experienced staff by turning them into reviewers, trainers, approvers, and process owners.
- Avoid making frontline users feel publicly judged by AI metrics.
- Use low-risk pilots before broad rollout.
- Align managers and respected senior users before announcing a workflow change.
- Treat silent resistance as diagnostic information, not disobedience.
- Make transformation humane: people should see a path from repetitive work to higher-value judgment work.

This is both an ethical stance and a practical deployment advantage. A system that threatens status and employment will be resisted. A system that protects expertise and improves working life has a better chance of becoming real operations.

## What It Does

AI First FDE Skill helps an agent work like a field deployment engineer:

- identify the real business pain before recommending tools;
- reconstruct the current workflow from real artifacts;
- map organization structure, decision rights, approval routes, and informal veto points;
- map stakeholders, resistance patterns, relationship risks, and adoption signals;
- design organization architecture diagrams and relationship maps;
- organize scattered enterprise knowledge into an LLM Wiki style structure;
- define data inventory, permission model, security boundaries, audit logs, and human approval gates;
- choose a narrow, recoverable PoC or pilot;
- define KPI, validation method, rollback path, and operations ownership;
- troubleshoot incidents by layer;
- produce public-safe documentation without exposing customer details.

## Operating Model

```mermaid
flowchart LR
  A["Client Request"] --> B["Workflow Pain Diagnostic"]
  B --> C["Current Process Map"]
  C --> D["Organization / Relationship Map"]
  D --> E["Knowledge / LLM Wiki Map"]
  E --> F["Data + Permission Model"]
  F --> G["AI Solution Architecture"]
  G --> H["PoC / Pilot Plan"]
  H --> I["Rollout Gates"]
  I --> J["Operations + Adoption Review"]
  J --> K["Public-safe Case Rewrite"]
```

The order matters. Do not jump straight to model selection. The skill makes the organization legible first, then designs the technical system around the real workflow.

## Core Capabilities

### 1. Workflow and Pain Diagnosis

The skill starts with the real process, not a generic AI use case list. It asks for recent cases, tickets, spreadsheets, documents, chat threads, approvals, manual workarounds, waiting points, rework loops, and failure examples.

The output is a Problem Map that names:

- the pain type: time, error, rework, risk, queue, cost, lost revenue, employee frustration;
- the workflow owner;
- the daily users;
- the approval path;
- the current evidence;
- the steps where AI can safely help;
- the steps that must remain human-approved.

### 2. Organization Architecture and Relationship Mapping

Enterprise AI deployment needs a picture of the organization, not just the software stack.

The skill now includes an organization mapping layer that can produce:

- organization architecture map;
- stakeholder relationship map;
- decision and approval route;
- informal veto map;
- workflow handoff map;
- data ownership map;
- escalation path;
- AI operating responsibility map.

When diagram tooling is available, the map can be turned into a large professional architecture diagram or relationship graph. When diagram tooling is not available, the skill still produces Mermaid and Markdown outputs that can be used directly in GitHub, Notion, Obsidian, internal wikis, slide decks, or agent context.

### 3. LLM Wiki and Enterprise Knowledge Structure

Many companies do not have a single knowledge problem. They have a source-of-truth problem.

AI First FDE Skill treats enterprise knowledge as a deployment surface:

- What is the authoritative source?
- Which documents are stale?
- Which team owns each knowledge domain?
- Which pages can be read by AI?
- Which content must remain private or department-scoped?
- Which contradictions need human review?
- Which knowledge updates should be logged?
- Which topics should become reusable wiki pages?

The skill can produce an LLM Wiki handoff plan with a domain taxonomy, source register, owner matrix, permission matrix, update cadence, contradiction log, and retrieval boundaries.

### 4. Data, Permission, and Governance Model

The skill requires every architecture plan to include:

- data sources;
- ingestion path;
- permission boundaries;
- sensitive fields;
- audit logging;
- human approval gates;
- failure modes;
- fallback workflow;
- rollback plan;
- operations owner.

This prevents the common failure mode where a demo works, but production cannot pass security, compliance, or operational review.

### 5. PoC, Pilot, Rollout, and Operations

The skill separates proof from deployment:

- PoC: prove that a narrow task can work with real artifacts.
- Pilot: prove that real users can use it safely in a controlled workflow.
- Rollout: expand only after measured value, repeated usage, and owner readiness.
- Operations: define monitoring, support, access review, cost review, quality review, incident response, and knowledge refresh.

## Skill Stitching Workbench

AI First FDE Skill is designed to act as the control layer for a larger agent workspace. If your local environment has additional skills, use them as specialist engines inside the FDE operating loop.

The idea is simple: keep the FDE method as the spine, then attach the right specialist skill at the right phase.

| FDE phase | Adjacent skill family | What it upgrades |
|---|---|---|
| Research grounding | browse, search, arXiv, market research, competitive analysis | Turns vague claims into sourced context. |
| Deep diagnostic | meeting analysis, ticket triage, enterprise consulting, spreadsheet analysis | Turns interviews and support logs into pain clusters. |
| Organization visualization | architecture diagram, diagramming, graphify, Figma, Excalidraw, infographic | Turns org structure and influence into visible maps. |
| Knowledge architecture | LLM Wiki, graphify, document processing, notes, spreadsheets | Turns scattered knowledge into a maintainable source-of-truth system. |
| Agent runtime planning | Codex, Claude Code, Hermes, OpenViking, OpenRouter, agent harness, eval harness | Turns runtime choice into an operating model. |
| Technical architecture | API design, backend, frontend, database, Docker, security patterns | Turns workflow design into implementable architecture. |
| Deployment validation | deployment patterns, e2e testing, regression testing, verification loop | Turns pilots into controlled rollout gates. |
| Governance and safety | security review, threat model, audit, public-safe checklist | Keeps data, permissions, and public material safe. |
| Documentation and enablement | article writing, docs, presentations, internal communications, translation | Turns deployment work into executive summaries, training, README, and public-safe cases. |

This makes the skill feel like an enterprise AI deployment workbench rather than a single prompt. The user does not need to understand every specialist tool. The FDE agent selects the right adjacent skill when the deliverable requires it.

Default rule: stitch for output quality, but do not create dependency bloat. If the adjacent tool is unavailable, produce the same artifact in Markdown and Mermaid.

## Modules

- `ai-first-fde`: main orchestration skill
- `ai-first-fde-research`: source-grounded research
- `ai-first-fde-diagnostic`: client diagnostic interview
- `ai-first-fde-architecture`: AI solution architecture
- `ai-first-fde-deployment`: PoC, pilot, rollout, operations
- `ai-first-fde-troubleshooting`: incident and field troubleshooting
- `ai-first-fde-adoption-observer`: user resistance and adoption observation

## Standard Deliverables

| Deliverable | Purpose |
|---|---|
| Engagement Brief | Define client, department, workflow, sponsor, limits, 30/60/90-day goals. |
| Problem Map | Make pain, workflow, data, permissions, and quick wins visible. |
| Stakeholder Map | Identify sponsor, workflow owner, users, reviewers, staff functions, blockers. |
| Organization Architecture Map | Show departments, owners, approval routes, handoffs, and escalation paths. |
| Relationship Diagram | Make formal and informal influence visible before rollout. |
| LLM Wiki Handoff | Convert scattered knowledge into maintainable wiki structure. |
| Data / Permission Model | Define source of truth, access boundaries, logging, sensitive fields. |
| Technical Solution Architecture | Design AI, agents, tools, integrations, human gates, failure handling. |
| PoC Plan | Prove a narrow task with real artifacts. |
| Pilot Plan | Test with real users, KPI, feedback, fallback, and sponsor review. |
| Deployment Runbook | Control rollout, rollback, training, support, and acceptance gates. |
| Adoption Risk Register | Track resistance, fear, manager alignment, and usage signals. |
| Troubleshooting Report | Diagnose incidents by layer and prevent recurrence. |
| Operations Handbook | Assign monitoring, access review, knowledge refresh, cost review, support. |
| Executive Summary | Explain decision, plan, risk, and next step for leadership. |
| Public-safe Case Rewrite | Turn confidential deployment work into anonymized public material. |

## Example Engagement Flow

1. Ask what workflow is in scope.
2. Ask for the last three real cases.
3. Reconstruct the current process.
4. Identify pain, risk, delay, and rework.
5. Map sponsor, workflow owner, daily users, reviewers, IT, security, legal, compliance, and hidden blockers.
6. Draw the organization architecture and relationship map.
7. Create the LLM Wiki structure for scattered knowledge.
8. Define the minimum viable dataset and permission boundary.
9. Choose one low-risk pilot.
10. Define KPI, human oversight, logging, fallback, stop criteria, and rollout gate.
11. Run sponsor review and user feedback loop.
12. Scale only after measured value and operations ownership.

## No Dependency / No Build

You do not need Python, npm, pip, Docker, a compiler, or a binary installer to use the skill.

The skill itself is Markdown. The Python validator is optional maintainer and CI tooling only. A normal user can clone the repo, open the Markdown files, and tell any capable agent to follow them.

Optional diagram or wiki tools can improve presentation quality, but they are not required for the core skill to work.

## Runtime Download Guide

For agent and CLI installation methods, see:

[docs/agent-runtime-download-guide.zh-Hant.md](docs/agent-runtime-download-guide.zh-Hant.md)

The guide covers common runtimes and agent surfaces such as Claude Code, Codex, Cursor, OpenRouter-backed agents, OpenCode / OpenCLI-style tools, Hermes, and adjacent CLI-based workflows.

## Public Safety

This repository is public. Do not contribute customer names, confidential architecture, contracts, credentials, internal URLs, employee names, or identifiable deployment details.

When writing public material:

- anonymize company and department names;
- remove internal paths, URLs, screenshots, credentials, and architecture specifics;
- turn real examples into reusable patterns;
- cite only public sources;
- never present private memory or local files as public evidence.

## Research Base

The skill is informed by enterprise AI deployment practice, East Asian organizational dynamics, responsible AI governance, Stanford Digital Economy Lab's 2026 Enterprise AI Playbook, Stanford HAI / AI Index, NIST, OECD, Microsoft WorkLab, McKinsey, Japan METI / MIC public materials, and field experience patterns from enterprise AI adoption.

This repository does not claim endorsement by any referenced organization.

## License

MIT License.
