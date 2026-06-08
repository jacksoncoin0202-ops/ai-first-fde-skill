# Adjacent Skill Stitching Matrix

## Objective

Turn AI First FDE Skill into an operator hub. When the runtime has other skills, use them to strengthen the current phase instead of treating FDE as a single isolated prompt.

The FDE skill remains Markdown-only and no-build. Adjacent skills are optional accelerators.

## Rule

Do not load every available skill at once.

1. Identify the current FDE phase.
2. Select one or two adjacent skills that improve the deliverable.
3. Produce the artifact.
4. Return to the FDE operating loop.

## Capability chains

### Research chain

Use when the project needs public grounding, competitor context, policy references, academic references, or industry evidence.

Useful skill types:

- browse;
- web search;
- arxiv;
- market-research;
- competitive-ads-extractor;
- content-research-writer;
- deep-research.

FDE output:

- source pack;
- industry constraints;
- benchmark table;
- public-safe citations;
- research brief.

### Diagnostic chain

Use when the client problem is vague or meetings / tickets / support logs need synthesis.

Useful skill types:

- meeting-notes-and-actions;
- meeting-insights-analyzer;
- support-ticket-triage;
- enterprise-ai-consulting;
- company-kyb-document-management;
- spreadsheet analysis.

FDE output:

- diagnostic interview plan;
- pain cluster;
- workflow evidence table;
- stakeholder questions;
- current-state process map.

### Organization visualization chain

Use when there are many departments, approvers, informal blockers, handoffs, or unclear ownership.

Useful skill types:

- architecture-diagram;
- diagramming;
- graphify;
- excalidraw;
- figma;
- baoyu-infographic;
- codebase-onboarding, when the organization map must connect to system architecture.

FDE output:

- organization architecture map;
- relationship graph;
- decision route;
- approval map;
- escalation path;
- AI operations responsibility map.

### Knowledge architecture chain

Use when knowledge is scattered across files, chats, tickets, email, shared drives, PDFs, or personal memory.

Useful skill types:

- llm-wiki;
- graphify;
- apple-notes;
- documents;
- spreadsheets;
- codebase-onboarding;
- content-hash-cache-pattern.

FDE output:

- LLM Wiki schema;
- source register;
- domain taxonomy;
- owner matrix;
- permission matrix;
- contradiction log;
- knowledge refresh cadence.

### Agent runtime chain

Use when the user asks which agent runtime to use or how to operate the skill across Claude Code, Codex, Cursor, Hermes, OpenRouter, OpenCode / OpenCLI, or other agents.

Useful skill types:

- codex;
- claude-code;
- hermes-agent;
- connect-apps;
- openviking workflow;
- agent-harness-construction;
- enterprise-agent-ops;
- cost-aware-llm-pipeline;
- eval-harness.

FDE output:

- runtime selection table;
- agent operating model;
- context strategy;
- tool boundary;
- evaluation plan;
- cost / latency route.

### Engineering architecture chain

Use when the FDE output must turn into a technical implementation plan.

Useful skill types:

- api-design;
- backend-patterns;
- frontend-patterns;
- database-migrations;
- docker-patterns;
- postgres-patterns;
- clickhouse-io;
- security-best-practices.

FDE output:

- technical solution architecture;
- API contract;
- data model;
- integration plan;
- permission model;
- logging and audit plan.

### Deployment and validation chain

Use when moving from idea to PoC, pilot, rollout, or operations.

Useful skill types:

- deployment-patterns;
- cloudflare-deploy;
- vercel-deploy;
- netlify-deploy;
- e2e-testing;
- webapp-testing;
- ai-regression-testing;
- eval-harness;
- verification-loop.

FDE output:

- PoC plan;
- pilot plan;
- deployment runbook;
- validation checklist;
- rollback plan;
- operations handoff;
- regression test plan.

### Governance and safety chain

Use when dealing with confidential data, public release, regulated workflows, security review, or cross-department permissions.

Useful skill types:

- security-review;
- security-scan;
- security-threat-model;
- careful;
- audit;
- validation;
- public-release-safety checklist.

FDE output:

- risk model;
- permission review;
- threat model;
- public-safe boundary;
- data exposure prevention;
- go / no-go gate.

### Documentation and enablement chain

Use when the output must become a README, internal memo, executive summary, training deck, public case study, social post, or multilingual material.

Useful skill types:

- article-writing;
- doc;
- presentations;
- baoyu-slide-deck;
- brand-voice;
- internal-comms;
- baoyu-translate;
- content-engine.

FDE output:

- executive summary;
- training plan;
- internal announcement;
- FAQ;
- README;
- public-safe case rewrite;
- slide deck.

## Stop conditions

Stop stitching and return to the core FDE loop if:

- the adjacent skill adds presentation polish but no operational evidence;
- it introduces dependencies the user did not ask for;
- it risks exposing private client details;
- it makes the plan harder to execute;
- it turns an operator guide into abstract consulting language.
