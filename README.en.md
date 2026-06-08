# AI First FDE Skill

AI First FDE Skill is a Markdown-only, no-build skill suite for enterprise AI field deployment.

It turns an agent into a Forward Deployed Engineer: diagnose the real workflow, map data and permissions, handle stakeholder resistance, design a safe pilot, define rollout gates, and produce delivery-ready artifacts.

## Quick Start

```bash
git clone https://github.com/jacksoncoin0202-ops/ai-first-fde-skill.git
cd ai-first-fde-skill
```

Tell your agent:

```text
Read skills/ai-first-fde/SKILL.md first.
If the task needs research, diagnostic interview, architecture, deployment, troubleshooting, or adoption observation, read the matching skills/ai-first-fde-* module and skills/ai-first-fde/references/.
```

## No Dependency / No Build

You do not need Python, npm, pip, Docker, a compiler, or a binary installer to use the skill.

The skill itself is Markdown. The Python validator is optional maintainer and CI tooling only.

## What It Does

- finds the real business pain before recommending tools;
- maps workflow, owners, data, permissions, risks, and KPIs;
- identifies relationship blockers and informal veto holders;
- designs PoC, pilot, rollout, rollback, and operations gates;
- handles adoption resistance in East Asian enterprise contexts;
- produces public-safe documentation without exposing client details.

## Modules

- `ai-first-fde`: main orchestration skill
- `ai-first-fde-research`: source-grounded research
- `ai-first-fde-diagnostic`: client diagnostic interview
- `ai-first-fde-architecture`: AI solution architecture
- `ai-first-fde-deployment`: PoC, pilot, rollout, operations
- `ai-first-fde-troubleshooting`: incident and field troubleshooting
- `ai-first-fde-adoption-observer`: user resistance and adoption observation

## Operating Flow

1. Name the workflow and business pain.
2. Reconstruct the current process with real artifacts.
3. Map data, permissions, owners, and approval points.
4. Map sponsor, blockers, daily users, reviewers, and staff functions.
5. Choose one narrow, recoverable pilot.
6. Define KPI, human oversight mode, fallback, and stop / continue / expand criteria.
7. Run weekly sponsor review and user feedback loops.
8. Scale only after evidence of real usage, measured value, and operations ownership.

## Standard Deliverables

- Engagement Brief
- Problem Map
- Stakeholder Map
- Data / Permission Model
- Technical Solution Architecture
- PoC Plan
- Pilot Plan
- Deployment Runbook
- Adoption Risk Register
- Troubleshooting Report
- Validation Checklist
- Operations Handbook
- Executive Summary
- Public-safe Case Rewrite

## Use With Any Agent Runtime

The skill can be used by any agent that can read Markdown or project rules, including Claude Code, OpenAI Codex CLI, Cursor, Hermes, OpenCode, Gemini CLI, Cline, Aider, Continue, Devin CLI, and OpenRouter-backed agents.

See [docs/agent-runtime-download-guide.zh-Hant.md](docs/agent-runtime-download-guide.zh-Hant.md) for the runtime download guide.

## Safety

This repository is public. Do not contribute customer names, confidential architecture, contracts, credentials, internal URLs, employee names, or identifiable deployment details.

## Research Base

The skill is informed by enterprise AI deployment practice, East Asian organizational dynamics, responsible AI governance, Stanford Digital Economy Lab's 2026 Enterprise AI Playbook, Stanford HAI / AI Index, NIST, OECD, Microsoft WorkLab, McKinsey, and Japan METI / MIC public materials.

This repository does not claim endorsement by any referenced organization.

## License

MIT License.
