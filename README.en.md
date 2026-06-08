# AI FIRST FDT SKILL

Created by **Jackz.ai**, this public agent-runtime-neutral skill suite is designed for AI deployment inside **East Asian enterprise organizations**.

It turns an AI agent into a front-line AI FIRST Field Deployment Technician: someone who investigates the real workflow, interviews the client deeply, designs technical architecture, executes PoC and pilot plans, troubleshoots incidents, observes user resistance, and produces delivery-ready documents.

## Why this exists

Most enterprise AI failures are not model failures. They are workflow, data, permission, ownership, governance, and adoption failures.

In East Asian organizations, additional dynamics often matter:

- hierarchy and decision layers
- face-saving culture
- consensus before formal meetings
- risk avoidance
- seniority and role protection
- informal power centers
- reluctance to expose failure publicly
- adoption resistance hidden behind surface-level agreement

This skill suite is built for that reality.

## Modules

- `ai-first-fdt`: main orchestration skill
- `ai-first-fdt-research`: research and source-grounded discovery
- `ai-first-fdt-diagnostic`: deep client diagnostic interview
- `ai-first-fdt-architecture`: AI solution architecture
- `ai-first-fdt-deployment`: PoC, pilot, rollout, operations
- `ai-first-fdt-troubleshooting`: field incident response
- `ai-first-fdt-adoption-observer`: East Asian user resistance and adoption observation

## Core deliverables

- Engagement Brief
- Client Discovery Report
- Problem Map
- Stakeholder Map
- Use Case Prioritization Matrix
- Data / Permission Model
- Technical Solution Architecture
- PoC / Pilot / Rollout Plan
- Deployment Runbook
- Adoption Risk Register
- Training Plan
- Troubleshooting Report
- Validation Checklist
- Operations Handbook
- Executive Summary
- Public-safe Case Rewrite

## Installation

This suite is not only for Hermes. You can use it with Claude Code, OpenAI Codex CLI, Cursor, OpenRouter-backed agents, OpenCLI workflows, OpenCode, Gemini CLI, GitHub Copilot CLI, Windsurf, Cline, Aider, Continue, Devin CLI, and other agents that can read Markdown project instructions.

- Agent / CLI download guide: [`docs/agent-runtime-download-guide.zh-Hant.md`](docs/agent-runtime-download-guide.zh-Hant.md)

Manual setup for most agents:

```bash
git clone https://github.com/jacksoncoin0202-ops/ai-first-fdt-skill.git
cd ai-first-fdt-skill
```

Then tell the agent:

```text
Read skills/ai-first-fdt/SKILL.md first.
Use the relevant ai-first-fdt-* module for research, diagnostic, architecture, deployment, troubleshooting, or adoption observation work.
```

Hermes direct install:

```bash
hermes skills install skills-sh/jacksoncoin0202-ops/ai-first-fdt-skill/skills/ai-first-fdt
```

## Safety

This repository is public. Do not contribute customer names, confidential architecture, contracts, credentials, internal URLs, employee names, or identifiable deployment details.

## Research note

The suite is informed by enterprise AI deployment practice, East Asian organizational dynamics, responsible AI governance, and public research such as Stanford HAI / AI Index materials. It is not endorsed by Stanford.
