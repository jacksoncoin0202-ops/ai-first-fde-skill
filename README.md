# AI FIRST FDT SKILL 🚀

**AI FIRST FDT SKILL** is an open-source, agent-runtime-neutral Skill Suite created by **Jackz.ai** for enterprise AI field deployment in **East Asian organizational contexts**.

這不是普通 prompt，也不是空泛 AI 顧問模板。它是把一位 **AI FIRST Field Deployment Technician** 的工作方式封裝入 agent：先看懂現場，再設計方案，再試點、部署、排障、觀察採用，最後交付可驗收、可維運、可公開安全改寫的成果。

## 🌐 Choose Your Language / 選擇語言 / 言語を選択

| Language | README | Short description |
| --- | --- | --- |
| 🇭🇰 繁體中文 | [`README.zh-Hant.md`](README.zh-Hant.md) | [`docs/descriptions/zh-Hant.md`](docs/descriptions/zh-Hant.md) |
| 🇺🇸 English | [`README.en.md`](README.en.md) | [`docs/descriptions/en.md`](docs/descriptions/en.md) |
| 🇯🇵 日本語 | [`README.ja.md`](README.ja.md) | [`docs/descriptions/ja.md`](docs/descriptions/ja.md) |

## ⚡ Quick Start

Clone the repository:

```bash
git clone https://github.com/jacksoncoin0202-ops/ai-first-fdt-skill.git
cd ai-first-fdt-skill
```

Then tell your agent:

```text
Read skills/ai-first-fdt/SKILL.md first.
If the task needs research, diagnostic interview, architecture, deployment, troubleshooting, or adoption observation,
read the matching skills/ai-first-fdt-* module and skills/ai-first-fdt/references/.
```

中文版本：

```text
請先讀 skills/ai-first-fdt/SKILL.md。
如果任務需要研究、診斷、架構、部署、排障或 adoption observation，
請再讀對應的 skills/ai-first-fdt-* 模組與 skills/ai-first-fdt/references/。
```

## 🧭 One-Line Positioning

A skill suite that turns an AI agent into a front-line AI deployment technician:

1. diagnose the real workflow;
2. map data, permission, owner, risk, and validation;
3. design a safe technical architecture;
4. plan PoC, pilot, rollout, training, troubleshooting, and operations;
5. observe adoption resistance in East Asian enterprise cultures;
6. produce delivery-ready and public-safe documentation.

一句話：

> 讓 Agent 變成「AI 前線部署工程師」：先問清楚、再設計、再試點、再部署、再驗證。

## 💡 Why This Exists

AI 導入最常見的失敗，不是模型不夠強，而是現場根本沒有被看懂。

Many companies begin with the wrong questions:

- Which model should we use?
- Should we build a chatbot?
- Should we connect RAG?
- Which agent platform should we buy?

AI FIRST FDT asks the operational questions first:

- Who uses this workflow every day?
- What work actually happens before and after the AI step?
- Where is the data?
- Who is allowed to see it?
- Which step must remain human-approved?
- What happens if the AI is wrong?
- Who owns the rollback?
- What metric proves adoption is real?
- Why do users say yes in meetings but still return to the old workflow?

Enterprise AI does not become real because a demo works. It becomes real when AI is safely embedded into daily work with known data sources, permission boundaries, approval points, monitoring, rollback, training, and operations ownership.

## 🌏 East Asia Deployment Context

This suite is designed for companies operating in Japan, Taiwan, Hong Kong, Korea, Singapore, mainland China, and culturally adjacent enterprise teams where adoption is shaped by:

- hierarchy and decision layers;
- face-saving culture;
- consensus before formal meetings;
- seniority and role protection;
- risk avoidance;
- hidden resistance behind surface-level agreement;
- informal power centers;
- reluctance to expose workflow failure publicly.

AI FIRST FDT does not treat these as soft side issues. They are deployment variables. If they are ignored, AI stays in demo mode and never enters daily operations.

## 🧩 What Problem It Solves

This Skill Suite helps a consultant, internal AI champion, system integrator, or product team break enterprise AI adoption into executable field work:

1. identify the best low-risk workflow to start with;
2. map business process, users, owners, data sources, permissions, and constraints;
3. decide what AI can draft, answer, classify, search, summarize, or execute;
4. decide what must remain human-reviewed;
5. design a secure PoC and pilot;
6. produce technical architecture, data flow, permission model, and operations plan;
7. observe why employees do not adopt the tool;
8. diagnose incidents across prompt, retrieval, model, tool, permission, UI, and data layers;
9. hand off a system that can be validated and maintained;
10. rewrite public case studies without exposing client secrets.

## 👥 Who Should Use This

- Enterprise AI consultants
- Field deployment engineers
- Internal AI champions
- System integrators
- IT service companies
- AI product teams
- Technical service companies
- Agent workflow builders
- Teams bringing AI from slide decks into real company workflows

## 🚫 What This Is Not

AI FIRST FDT is not:

- a generic AI trend-writing prompt;
- a model leaderboard;
- a chatbot template;
- a replacement for legal, medical, financial, security, or compliance professionals;
- an automation layer for high-risk decisions without human approval;
- a way to publish identifiable client information;
- a tool recommendation engine that skips workflow diagnosis.

The skill intentionally slows the agent down at the right moment: before it recommends, it diagnoses; before it deploys, it maps risks; before it publishes, it redacts.

## 🤖 Use With Any Agent Runtime

This suite is not limited to Hermes. It can be used with any agent runtime that can read Markdown instructions, project rules, skills, MCP context, or prompt files.

Supported or relevant runtime categories include:

- Hermes
- Claude Code
- OpenAI Codex CLI
- Cursor
- OpenRouter-backed agents
- OpenCLI workflows
- OpenCode
- Gemini CLI
- GitHub Copilot CLI
- Windsurf
- Cline
- Aider
- Continue
- Devin CLI
- other Markdown-aware agent runtimes

Full guide:

- [`docs/agent-runtime-download-guide.zh-Hant.md`](docs/agent-runtime-download-guide.zh-Hant.md)

## 📦 Download / Install Matrix

Always install from official sources. Do not use random SEO install guides, unknown npm wrappers, or unofficial mobile / desktop wrappers.

| Runtime | Type | Official install / download method | How to use FDT |
| --- | --- | --- | --- |
| Hermes | Skill runtime | `hermes skills install skills-sh/jacksoncoin0202-ops/ai-first-fdt-skill/skills/ai-first-fdt` | Native skill install. Install the main skill, then add modules as needed. |
| Claude Code | Terminal coding agent | macOS / Linux / WSL: `curl -fsSL https://claude.ai/install.sh \| sh`; Windows: `irm https://claude.ai/install.ps1 \| iex`; Homebrew: `brew install --cask claude-code`; npm: `npm install -g @anthropic-ai/claude-code` | Start `claude` inside this repo and ask it to read `skills/ai-first-fdt/SKILL.md`. |
| OpenAI Codex CLI | Terminal / IDE / desktop coding agent | macOS / Linux: `curl -fsSL https://chatgpt.com/codex/install.sh \| sh`; Windows: `powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 \| iex"`; npm: `npm install -g @openai/codex`; Homebrew: `brew install --cask codex` | Start `codex` inside this repo and load the FDT skill. |
| Cursor | Agent-first IDE / CLI | Desktop: `https://cursor.com/download`; terminal installer: `curl https://cursor.com/install -fsS \| bash` | Put FDT instructions into Cursor rules or ask the agent to read the skill file. |
| OpenRouter | Model router / API / Agent SDK | API base: `https://openrouter.ai/api/v1`; SDK: `npm install @openrouter/sdk`; Agent SDK: `npm install @openrouter/agent` | OpenRouter is not a standalone FDT runtime. Use it as the model provider for Cline, OpenCode, Aider, custom agents, or OpenAI-compatible clients. |
| OpenCLI, jackwener/opencli | Browser / desktop tool bridge | `npm install -g @jackwener/opencli`; verify with `opencli --version`, `opencli list`, `opencli doctor` | Use as a tool layer so agents can operate browser / desktop / website CLIs. |
| OpenCLI, opencli.co | CLI discovery / work router | Use `https://opencli.co/` to find the right CLI stack for a job | Use during FDT research when choosing command-line tooling for PDF, CSV, email, PR review, notes, or data work. |
| OpenCLI, opencli.run | Local multimodal CLI engine | `brew tap openclirun/opencli`; `brew install opencli` | Useful when a local multimodal capability engine is part of the deployment environment. |
| OpenCode | Open-source coding agent | `curl -fsSL https://opencode.ai/install \| bash`; `npm i -g opencode-ai`; `bun add -g opencode-ai`; `brew install anomalyco/tap/opencode`; desktop beta: `brew install --cask opencode-desktop` | Start OpenCode in the repo and load FDT as project rules / prompt context. |
| Gemini CLI | Google terminal agent | npx: `npx https://github.com/google-gemini/gemini-cli`; npm: `npm install -g @google/gemini-cli`; Homebrew: `brew install gemini-cli` | Start `gemini` in the repo and ask it to read the FDT skill. |
| GitHub Copilot CLI | GitHub-native terminal agent | npm: `npm install -g @github/copilot`; Windows: `winget install GitHub.Copilot`; Homebrew: `brew install copilot-cli`; script: `curl -fsSL https://gh.io/copilot-install \| bash` | Useful for issue, PR, and GitHub workflow tasks using FDT planning and delivery rules. |
| Windsurf | Agentic IDE | Download macOS / Windows / Linux installer from `https://windsurf.com/download` | Add FDT instructions to Windsurf rules / memories or ask Cascade to read the skill file. |
| Cline | IDE extension / CLI / SDK | IDE: install `Cline` from VS Code / Cursor / Windsurf / VSCodium / JetBrains marketplace; CLI: `npm install -g cline`, then `cline auth` | Use with Anthropic, OpenAI, OpenRouter, Gemini, Bedrock, Ollama, or other providers. Load FDT through prompt / rules. |
| Aider | Terminal pair-programming agent | `python -m pip install aider-install`; then `aider-install` | Use FDT as task brief / prompt context for architecture, docs, and delivery package work. |
| Continue | VS Code / JetBrains AI coding platform | Install from Visual Studio Marketplace or JetBrains Marketplace | Use FDT through workspace config, repo rules, or prompt context. |
| Devin CLI | Local CLI with Devin Cloud integration | `curl -fsSL https://cli.devin.ai/install.sh \| bash` | Use FDT as discovery, planning, delivery, and operations playbook. |
| Roo Code | Legacy / sunset VS Code agent extension | Roo Code docs show the extension was shut down on 2026-05-15 | Not recommended as a new default. If an existing team uses it, mark the shutdown status and consider Cline or a maintained alternative. |

## 🛠 Hermes Direct Install

Install the main orchestration skill:

```bash
hermes skills install skills-sh/jacksoncoin0202-ops/ai-first-fdt-skill/skills/ai-first-fdt
```

Install modules as needed:

```bash
hermes skills install skills-sh/jacksoncoin0202-ops/ai-first-fdt-skill/skills/ai-first-fdt-research
hermes skills install skills-sh/jacksoncoin0202-ops/ai-first-fdt-skill/skills/ai-first-fdt-diagnostic
hermes skills install skills-sh/jacksoncoin0202-ops/ai-first-fdt-skill/skills/ai-first-fdt-architecture
hermes skills install skills-sh/jacksoncoin0202-ops/ai-first-fdt-skill/skills/ai-first-fdt-deployment
hermes skills install skills-sh/jacksoncoin0202-ops/ai-first-fdt-skill/skills/ai-first-fdt-troubleshooting
hermes skills install skills-sh/jacksoncoin0202-ops/ai-first-fdt-skill/skills/ai-first-fdt-adoption-observer
```

## 🧱 Skill Modules

This is a suite, not a single thin instruction file.

- `ai-first-fdt`: main orchestrator; routes the task, selects modules, integrates deliverables.
- `ai-first-fdt-research`: source-grounded discovery, public evidence, claim safety, market and industry context.
- `ai-first-fdt-diagnostic`: deep client interview protocol; asks through business, workflow, data, people, risk, and KPI.
- `ai-first-fdt-architecture`: technical AI solution architecture; data flow, permissions, retrieval, tools, approvals, logging, rollback.
- `ai-first-fdt-deployment`: PoC, pilot, rollout, training, acceptance criteria, operations handoff.
- `ai-first-fdt-troubleshooting`: field incident response; diagnoses failures by layer and produces containment, fix, validation, prevention.
- `ai-first-fdt-adoption-observer`: East Asian adoption resistance observation; identifies hidden blockers and safer rollout tactics.

## 🔁 Operating Model

When a user asks for help, the main skill routes the work into one or more modes:

1. **Research grounding**: collect public evidence, industry constraints, safe assumptions, and source notes.
2. **Diagnostic interview**: understand the real workflow before solution design.
3. **Problem map**: identify user groups, pain points, data gaps, permission risks, and operational bottlenecks.
4. **Use case prioritization**: choose low-risk, high-signal workflows before touching core process risk.
5. **Solution architecture**: design system boundary, data flow, permissions, tools, model choices, approvals, logging, and rollback.
6. **Deployment planning**: convert design into PoC, pilot, rollout, training, acceptance criteria, and operations handoff.
7. **Troubleshooting**: diagnose prompt, retrieval, model, tool, permission, UI, data, and adoption failures.
8. **Adoption observation**: watch what users actually do after launch, especially where they politely agree but do not adopt.
9. **Validation**: define 30/60/90-day metrics, acceptance checks, and evidence that the workflow improved.
10. **Public-safe summary**: rewrite outputs for public sharing without exposing client identity or internal details.

## ✅ Mandatory FDT Principles

The skill instructs the agent to:

- ask before prescribing when the workflow is unclear;
- never recommend tools before process, data, permission, and user context are understood;
- map every output to a real workflow, owner, data source, user group, risk, and validation method;
- include data flow, permission model, logging, human approval, failure mode, rollback, and operations ownership in technical plans;
- design East Asian adoption around face-saving, manager alignment, low-risk pilots, senior reviewers, and no-blame learning;
- never expose customer secrets or write public cases with identifiable internal details;
- split complex tasks into research, diagnostic, architecture, deployment, troubleshooting, and adoption observation;
- prefer practical deliverables over abstract discussion.

## 🔎 Diagnostic Questions

When the environment is unclear, FDT starts with the smallest set of questions that unlock the next step:

1. What company, department, and workflow are in scope?
2. Who owns the workflow?
3. Who uses it daily?
4. What data sources are involved?
5. What systems must be integrated?
6. What can AI answer, draft, classify, search, summarize, or execute?
7. What must remain human-approved?
8. What is the 30/60/90-day success metric?
9. What is the adoption risk?
10. What information must remain confidential?

## 📋 Standard Deliverables

A complete FDT engagement should produce:

- Engagement Brief
- Client Discovery Report
- Problem Map
- Stakeholder Map
- Use Case Prioritization Matrix
- Data Inventory
- Permission and Risk Model
- Technical Solution Architecture
- PoC Plan
- Pilot Plan
- Deployment Runbook
- Training Plan
- Adoption Risk Register
- Troubleshooting / Incident Plan
- Validation Checklist
- Operations Handbook
- KPI Dashboard Specification
- Executive Summary
- Public-safe Case Rewrite, if the user wants public promotion

## 🌱 East Asia Adoption Defaults

Use these defaults unless the user says otherwise:

- Start with a low-risk quick win.
- Select respected, approachable champions, not only the most technical users.
- Let senior staff review and improve AI outputs, preserving status and ownership.
- Avoid public blame when users do not adopt.
- Treat hidden resistance as a diagnostic signal, not disobedience.
- Use manager scripts and informal alignment before formal rollout.
- Frame AI as reducing rework, overtime, and cognitive load, not replacing people.
- Keep fallback to the existing workflow during the pilot.
- Use team-level metrics before individual ranking.
- Preserve human approval for important decisions.

## 💬 Example Prompts

Use the full FDT mode:

```text
Use Jackz.ai FDT mode to design an AI First adoption plan for a 200-person technical service company.
Start with workflow diagnosis before recommending tools.
```

Use diagnostic mode only:

```text
Use FDT diagnostic mode. Interview this client deeply about their AI adoption needs.
Do not write a solution yet.
```

Use troubleshooting and adoption observation:

```text
Our internal knowledge-base AI gives inaccurate answers and employees are not using it.
Use FDT troubleshooting and adoption observer mode to diagnose the issue.
```

Use the skill for public-safe case writing:

```text
Rewrite this internal deployment story as a public-safe case study.
Remove customer identifiers, internal URLs, credentials, exact architecture details, and political details.
```

## 🗺 Repository Map

```text
skills/
  ai-first-fdt/
    SKILL.md
    references/
    templates/
    checklists/
    evals/
  ai-first-fdt-research/
  ai-first-fdt-diagnostic/
  ai-first-fdt-architecture/
  ai-first-fdt-deployment/
  ai-first-fdt-troubleshooting/
  ai-first-fdt-adoption-observer/

docs/
  agent-runtime-download-guide.zh-Hant.md
  research/ai-first-fdt-research-report.en.md
  source-notes.md
  descriptions/
```

## 🔬 Agent Runtime Research Method

When researching whether a market agent can use this skill, record:

- official source: download page, GitHub repo, docs, marketplace;
- install command: macOS, Linux, Windows, npm, Homebrew, pip, desktop installer, extension marketplace;
- verification command: `--version`, `doctor`, `help`, login check, first-run prompt;
- authentication: API key, OAuth, ChatGPT plan, Claude Enterprise, GitHub Copilot subscription, Google login, OpenRouter key, local model, SSO;
- skill loading method: native skill, project rules, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, IDE rules, prompt context, MCP, SDK;
- permission model: file edit, shell execution, network access, browser session reuse, SaaS access, GitHub issue / PR access, approval mode;
- maintenance status: release notes, docs update date, shutdown notice, archived repo;
- enterprise fit: data retention, audit log, policy control, model provider choice, offline / local support.

## 🔐 Public Safety

This repository is public. Do not contribute:

- real customer names;
- employee names;
- confidential architecture;
- private contracts;
- credentials, API keys, tokens, or secrets;
- internal URLs;
- private pricing or commercial terms;
- identifiable deployment details;
- unapproved internal politics;
- unpublished security weaknesses.

For public GitHub, X.com, decks, articles, or case studies:

- anonymize real cases;
- rewrite examples into patterns;
- cite public sources for public claims;
- do not cite private memory or internal files as public evidence;
- do not imply endorsement by Stanford, NIST, OECD, Microsoft, McKinsey, METI, MIC, or any referenced organization.

## 📚 Research Grounding

The suite is informed by public research and governance materials, including:

- Stanford HAI / AI Index
- NIST AI Risk Management Framework
- NIST Generative AI Profile
- OECD AI Principles
- Microsoft Work Trend Index
- McKinsey State of AI
- Japan METI / MIC AI Business Guidelines

The research thesis is simple:

AI use is rising quickly, but enterprise transformation remains uneven. The hard part is workflow redesign, permission, ownership, governance, training, adoption, validation, and operations. AI FIRST FDT exists to make agents handle those field realities instead of jumping straight to tool recommendations.

Read more:

- Full research report: [`docs/research/ai-first-fdt-research-report.en.md`](docs/research/ai-first-fdt-research-report.en.md)
- Source notes: [`docs/source-notes.md`](docs/source-notes.md)

## 📄 License

MIT License.
