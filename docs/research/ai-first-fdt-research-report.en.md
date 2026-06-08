# AI FIRST FDT SKILL — Research Grounding Report

**Version:** 0.1  
**Maintainer:** Jackz.ai  
**Scope:** Public research grounding for the AI FIRST FDT SKILL  
**Audience:** enterprise AI consultants, internal AI champions, system integrators, AI product teams, and agent workflow builders  
**Public-safety note:** This document only cites public sources. It does not include customer names, private deployment files, credentials, internal URLs, or confidential architecture.

---

## 1. Executive thesis

A company does not become AI First by buying a model, launching a chatbot, or running an impressive demo.

A company becomes AI First when AI is safely embedded into real work:

- the actual workflow is mapped;
- the data sources are known;
- the responsible owner is clear;
- the permission boundary is explicit;
- human review points are designed;
- failure modes and rollback paths exist;
- users are trained in the specific work they actually do;
- adoption is observed after launch;
- value is measured at workflow level, not only demo level.

The AI FIRST FDT SKILL exists because enterprise AI adoption is now broad, but enterprise AI transformation is still uneven. Public research consistently points in the same direction: AI usage is rising quickly, but many organizations are still stuck in pilots, informal employee usage, unclear governance, weak training, and incomplete workflow redesign.

The gap is not only technical. It is operational.

The skill is therefore framed as a **Field Deployment Technician** operating mode: before the agent recommends tools, it diagnoses the workflow; before it writes architecture, it maps data and permission; before it claims transformation, it defines the pilot, adoption plan, validation method, and operational handoff.

---

## 2. Why this needs to exist now

### 2.1 AI adoption has moved from curiosity to normal work

Stanford HAI's 2025 AI Index reports that AI business usage accelerated sharply: **78% of organizations reported using AI in 2024, up from 55% the year before**. Stanford also highlights that AI is increasingly embedded in everyday life, that private AI investment remains high, and that AI performance continues to improve across demanding benchmarks.

Source: Stanford HAI, *The 2025 AI Index Report*  
https://hai.stanford.edu/ai-index/2025-ai-index-report

Microsoft and LinkedIn's 2024 Work Trend Index found that **75% of global knowledge workers use AI at work**, with many starting recently. The same report also states that **78% of AI users are bringing their own AI tools to work**, and that **60% of leaders worry their organization lacks a plan and vision to implement AI**.

Source: Microsoft WorkLab, *AI at Work Is Here. Now Comes the Hard Part*  
https://www.microsoft.com/en-us/worklab/work-trend-index/ai-at-work-is-here-now-comes-the-hard-part

McKinsey's State of AI research similarly shows that AI use is widespread, but scaling is not yet mature. Its 2025 survey reports that **88% of respondents say their organizations are regularly using AI in at least one business function**, but most are still in experimentation or piloting phases rather than scaled enterprise transformation.

Source: McKinsey, *The state of AI in 2025: Agents, innovation, and transformation*  
https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai

The combined implication is straightforward: AI is already inside work, whether the company has a clear plan or not. If leadership does not create a safe operating model, employees will still use AI through unofficial tools, creating data exposure, inconsistent quality, and invisible dependency.

### 2.2 The bottleneck is no longer model access alone

In 2022, enterprise AI conversations often centered on access to foundation models and whether the model was capable enough. By 2024 and 2025, the pattern changed. The public evidence now points toward organizational execution: workflow redesign, adoption, governance, training, and risk management.

McKinsey identifies workflow redesign as a key success factor. It reports that AI high performers are nearly three times as likely as others to fundamentally redesign workflows, and that high performers are more likely to define processes for when model outputs need human validation.

Microsoft's Work Trend Index also points to the organizational nature of the problem: leaders recognize AI as necessary, but many lack a plan. Employees want relief from digital overload and already use AI, but many hide usage or rely on personal tools.

This is exactly the gap that a field-deployment skill should address.

A generic prompt asks, "What AI solution should we build?"

AI FIRST FDT asks:

1. What work happens every day?
2. Who performs it?
3. What data does it require?
4. Who has permission to see that data?
5. Which parts can AI draft, summarize, classify, search, or automate?
6. Which parts require human approval?
7. What happens if the AI is wrong?
8. Who owns operations after the pilot?
9. What user behavior would prove adoption is real?
10. What metric would show value beyond a demo?

---

## 3. Research base

This section summarizes the public evidence that shaped the skill design.

### 3.1 Stanford HAI / AI Index: AI is increasingly powerful, widespread, and governance-sensitive

The Stanford HAI AI Index is one of the most widely cited public references for tracking AI progress. The 2025 report says its mission is to provide unbiased, rigorously vetted, broadly sourced data for policymakers, researchers, executives, journalists, and the public.

Key points relevant to this skill:

- AI business usage accelerated from 55% to 78% year over year.
- Generative AI attracted significant private investment.
- AI productivity research increasingly shows productivity improvements and skill-gap narrowing.
- Responsible AI remains uneven; Stanford notes that companies still face gaps between recognizing AI risk and acting meaningfully.
- Global AI governance activity increased, with frameworks from organizations such as the OECD, EU, UN, and African Union focused on transparency and trustworthiness.
- AI systems remain imperfect in complex reasoning and high-stakes precision tasks, which reinforces the need for human validation and fallback design.

Deployment implication:

A field-deployment agent should not treat AI capability as unlimited. It must build around verification, bounded scope, human review, and risk aware rollout.

### 3.2 NIST AI Risk Management Framework: trustworthiness must be built into design and use

The U.S. National Institute of Standards and Technology developed the AI Risk Management Framework to help organizations manage risks to individuals, organizations, and society. NIST describes AI RMF 1.0 as a voluntary framework intended to improve the ability to incorporate trustworthiness considerations into the design, development, use, and evaluation of AI products, services, and systems.

NIST also publishes a Generative AI Profile to help organizations identify unique risks posed by generative AI and align risk management actions with their goals.

Source: NIST, *AI Risk Management Framework*  
https://doi.org/10.6028/NIST.AI.100-1

Deployment implication:

The skill should force every technical plan to include:

- intended use and misuse boundaries;
- data flow;
- permission model;
- logging and monitoring;
- accuracy and validation method;
- human approval points;
- incident response;
- rollback;
- ownership after deployment.

This is why AI FIRST FDT does not stop at "architecture." It requires a deployment runbook, troubleshooting plan, validation checklist, adoption risk register, and operations handoff.

### 3.3 OECD AI Principles: trustworthy AI requires human-centered values and accountability

The OECD AI Principles promote AI that is innovative and trustworthy, and that respects human rights and democratic values. The principles include inclusive growth, human rights, transparency, robustness, security, safety, and accountability. They were initially adopted in 2019 and updated in 2024.

Source: OECD.AI, *OECD AI Principles overview*  
https://oecd.ai/en/ai-principles

Deployment implication:

An enterprise AI field deployment process must not be reduced to productivity alone. It must also ask:

- Is the user informed about what AI is doing?
- Can a human challenge or override the output?
- Is responsibility clear?
- Is the system robust enough for the actual use case?
- Are fairness, privacy, and safety considered before release?
- Does the company know who is accountable?

This supports the skill's requirement that every output map to a real workflow, owner, data source, user group, risk, and validation method.

### 3.4 Microsoft Work Trend Index: employees are already using AI, often without company structure

Microsoft and LinkedIn surveyed 31,000 people across 31 countries and analyzed Microsoft 365 productivity signals. Their 2024 report shows a practical tension:

- 75% of knowledge workers use AI at work.
- 78% of AI users bring their own AI tools to work.
- 52% of AI users are reluctant to admit using AI for important tasks.
- 53% worry that using AI for important work makes them look replaceable.
- 79% of leaders agree their company needs AI to stay competitive.
- 60% of leaders worry their organization lacks a plan and vision to implement AI.
- Power users are much more likely to redesign workflows with AI and receive leadership support and training.

Deployment implication:

A company cannot simply tell employees to "use AI more." Without governance, training, and approved workflows, employee usage becomes invisible. Invisible usage creates a blind spot: the company cannot improve it, secure it, or measure it.

AI FIRST FDT therefore treats adoption as a measurable field problem:

- Who is using the tool?
- Which workflow did it replace?
- Where do users still return to Excel, email, chat, or manual copy-paste?
- What fear prevents adoption?
- What training is missing?
- Which manager needs to support the change?
- Which metric proves the tool is part of daily work?

### 3.5 McKinsey State of AI: pilots are common; workflow redesign distinguishes high performers

McKinsey's 2025 State of AI research states that almost all respondents say their organizations use AI, yet most are still early in scaling and capturing enterprise-level value. It reports several key findings:

- Nearly two-thirds of respondents say their organizations have not yet begun scaling AI across the enterprise.
- 62% say their organizations are at least experimenting with AI agents.
- 88% report regular AI use in at least one business function.
- Many organizations have not integrated AI deeply across workflows.
- AI high performers are much more likely to redesign workflows and to scale agentic systems.
- Human validation of model outputs is one of the management practices associated with high performance.

Source: McKinsey, *The state of AI in 2025: Agents, innovation, and transformation*  
https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai

Deployment implication:

The difference between a demo and transformation is not the demo itself. It is whether the organization redesigns the workflow and creates a repeatable operating model.

This directly supports the structure of AI FIRST FDT:

1. research grounding;
2. diagnostic interview;
3. problem map;
4. use-case prioritization;
5. solution architecture;
6. PoC plan;
7. pilot plan;
8. adoption plan;
9. validation plan;
10. operations handoff.

### 3.6 Japan METI / MIC AI Business Guidelines: local governance is converging around unified guidance

Japan's Ministry of Economy, Trade and Industry (METI) and Ministry of Internal Affairs and Communications (MIC) released the AI Business Guidelines Version 1.0 in April 2024. The release consolidated and updated existing Japanese AI development, utilization, and governance guidelines in response to rapid technology changes including generative AI.

Source: METI, *AI Business Guidelines Version 1.0 release*  
https://www.meti.go.jp/press/2024/04/20240419004/20240419004.html

Deployment implication:

For Japan and East Asian enterprise contexts, AI adoption must be framed as governance-aware and locally adapted. A field deployment method should not blindly copy a Western SaaS rollout pattern. It must account for local decision layers, formal and informal consensus, responsibility boundaries, and risk sensitivity.

---

## 4. Why AI FIRST FDT focuses on East Asian enterprise deployment

Enterprise AI adoption is shaped by organizational culture. In many East Asian organizations, the formal org chart is only part of the system.

A deployment can fail even when the model works, the UI is good, and the executive sponsor is enthusiastic.

Common field patterns include:

- Senior staff quietly resist because the tool appears to reduce the value of their accumulated know-how.
- Middle managers worry that AI makes responsibility ambiguous.
- Frontline staff say yes in meetings but continue using old workflows.
- IT teams block rollout because data access, logging, and retention are unclear.
- Executives ask for AI transformation but do not define which workflow should change first.
- Teams avoid reporting failure because it creates loss of face.
- A pilot is judged by demo quality instead of actual usage.

These patterns require a different deployment posture:

- start with a low-risk quick win;
- align managers before formal rollout;
- preserve face and status for experienced users;
- make senior staff reviewers rather than targets of replacement;
- use team-level metrics before individual performance rankings;
- keep human approval for sensitive decisions;
- avoid blaming users for non-adoption;
- treat hidden resistance as diagnostic data.

That is why the skill includes an adoption observer module, not only architecture and deployment modules.

---

## 5. What AI FIRST FDT is not

AI FIRST FDT is not:

- a prompt collection for writing AI strategy posts;
- a chatbot prompt;
- a generic consulting slide generator;
- a model selection checklist;
- a tool recommendation bot;
- a public case-study generator using private client details;
- a system for replacing professional legal, financial, medical, security, or compliance judgment;
- an automation layer for high-risk decisions without human approval.

The skill is designed to make the agent slower at the right moment: before it recommends, it diagnoses; before it deploys, it maps risks; before it publishes, it redacts.

---

## 6. The AI FIRST FDT operating model

The skill turns an agent into a field operator with six modes.

### 6.1 Research mode

Purpose: ground the engagement in public evidence, industry constraints, and safe assumptions.

Outputs:

- research brief;
- public source list;
- claim confidence table;
- do-not-publish claims;
- local context notes that must not be cited publicly.

Why it matters:

AI transformation claims are easy to overstate. The research mode helps prevent fake authority and unsupported promises.

### 6.2 Diagnostic mode

Purpose: understand the real business workflow before solution design.

Questions include:

- What department and workflow are in scope?
- Who owns the workflow?
- Who uses it daily?
- What data sources are involved?
- What systems must be integrated?
- What can AI draft, answer, classify, search, or execute?
- What must remain human-approved?
- What is the 30/60/90-day success metric?
- What is the adoption risk?
- What information must remain confidential?

Why it matters:

Most bad AI projects skip diagnosis and jump directly to tooling. This creates a demo that looks good but does not survive contact with operations.

### 6.3 Architecture mode

Purpose: design a technical plan that can be reviewed by IT, security, business owners, and operations.

Required components:

- system boundary;
- user roles;
- data flow;
- permission model;
- model/tool choices;
- retrieval and knowledge source design;
- approval points;
- logging and audit trail;
- failure modes;
- fallback path;
- deployment environment;
- operations owner.

Why it matters:

Architecture is not only a diagram. It is a responsibility map.

### 6.4 Deployment mode

Purpose: convert the design into PoC, pilot, rollout, and operations execution.

Required components:

- PoC plan;
- pilot group;
- timeline;
- data readiness checklist;
- acceptance criteria;
- training plan;
- rollout plan;
- rollback plan;
- operations handoff.

Why it matters:

A good pilot should be small enough to be safe and real enough to test daily work.

### 6.5 Troubleshooting mode

Purpose: diagnose field incidents after launch.

Layers:

- user input;
- prompt / instruction;
- retrieval;
- model behavior;
- tool execution;
- permissions;
- integration;
- latency;
- logging;
- human review;
- organizational handoff.

Why it matters:

AI failures are rarely one-layer failures. A wrong answer may come from data freshness, missing permission, bad retrieval, unclear prompt, or a user expectation mismatch.

### 6.6 Adoption observer mode

Purpose: observe whether the tool is actually entering work.

Signals:

- users still copy-paste into old tools;
- managers do not mention the tool in review meetings;
- frontline users say it is useful but do not return;
- senior staff correct outputs privately but do not trust them publicly;
- IT support tickets increase after rollout;
- users avoid the tool for important work;
- the workflow owner cannot name the adoption metric.

Why it matters:

Enterprise AI value only appears when behavior changes.

---

## 7. The core field checklist

A company is not ready for AI First work until it can answer these questions.

### 7.1 Workflow

- What work is repeated every day?
- Which steps are slow, error-prone, or coordination-heavy?
- Which steps require judgment?
- Which steps are currently done through Excel, email, chat, PDF, or manual copy-paste?
- What would change if AI worked well?

### 7.2 Data

- Where is the data?
- Is it structured, unstructured, or scattered?
- Who can access it?
- Is the data current?
- Can it be used in an AI system legally and contractually?
- What should never be sent to an external model?

### 7.3 Permission

- Who can ask the AI?
- What can the AI see?
- What can the AI do?
- Can the AI write back to systems?
- What requires approval?
- Who reviews logs?

### 7.4 Risk

- What happens if the AI is wrong?
- What happens if the AI refuses?
- What happens if the AI reveals sensitive information?
- What happens if the AI is slow?
- What happens if the integration breaks?
- What is the rollback path?

### 7.5 Adoption

- Who is the first user group?
- Why would they use it daily?
- What fear might stop them?
- Who is the respected internal champion?
- What manager script is needed?
- What metric proves real adoption?

### 7.6 Value

- What is the baseline before AI?
- What is the target after 30 days?
- What is the target after 60 days?
- What is the target after 90 days?
- Is the goal time saved, error reduction, throughput, response quality, risk reduction, or revenue?

---

## 8. Why the skill uses modular sub-skills

A single prompt cannot handle enterprise AI deployment well because the work naturally splits into different disciplines:

- research;
- diagnostic questioning;
- architecture;
- deployment planning;
- troubleshooting;
- adoption observation;
- public-safe communication.

AI FIRST FDT is therefore a suite, not a single thin instruction file.

The main skill routes the task. The modules force the agent to adopt the right posture for the current stage.

For example:

- If the user asks for a market-backed proposal, start with research.
- If the user gives vague client needs, start with diagnostic.
- If the user asks for a solution diagram, require architecture mode.
- If the system is already live and failing, use troubleshooting.
- If usage is low despite good demos, use adoption observer.
- If the user wants to publish a case study, use public-safe boundaries.

This makes the agent more useful because it stops treating every request as a writing task.

---

## 9. Public claim boundary

The repo can safely claim:

- The skill is designed by Jackz.ai.
- The skill is an open-source, agent-runtime-neutral skill suite that can be used with Hermes, Claude Code, Codex, Cursor, OpenRouter-backed agents, OpenCLI workflows, and other Markdown-aware agent runtimes.
- The skill is intended for enterprise AI field deployment.
- The skill is optimized for East Asian enterprise adoption realities.
- The skill is informed by public research from Stanford HAI / AI Index, NIST, OECD, Microsoft WorkLab, McKinsey, and Japan METI / MIC guidelines.
- The skill does not claim endorsement by any referenced organization.

The repo should not claim:

- Stanford, NIST, OECD, Microsoft, McKinsey, METI, or MIC endorsement.
- Guaranteed ROI.
- Guaranteed productivity gains for every company.
- Replacement of legal, compliance, security, medical, or financial professionals.
- Customer results unless anonymized and approved.
- Private deployment experience as public fact.

---

## 10. Source register

### Stanford HAI — The 2025 AI Index Report

- URL: https://hai.stanford.edu/ai-index/2025-ai-index-report
- Used for: AI adoption, investment, productivity, responsible AI, AI governance, public opinion, model capability and limitations.
- Key relevance: shows broad AI adoption and the need for thoughtful development and governance.

### NIST — AI Risk Management Framework

- URL: https://doi.org/10.6028/NIST.AI.100-1
- Used for: risk management, trustworthiness, design/development/use/evaluation framing, generative AI risk profile.
- Key relevance: supports the skill's emphasis on risk, validation, human review, logging, and operations ownership.

### OECD — AI Principles

- URL: https://oecd.ai/en/ai-principles
- Used for: trustworthy AI principles, accountability, transparency, robustness, safety, human-centered governance.
- Key relevance: supports public-safe and governance-aware deployment framing.

### Microsoft WorkLab — 2024 Work Trend Index

- URL: https://www.microsoft.com/en-us/worklab/work-trend-index/ai-at-work-is-here-now-comes-the-hard-part
- Used for: employee AI usage, BYOAI, leadership plan gap, training, workflow redesign, power-user behavior.
- Key relevance: supports the claim that informal AI usage is already happening and must be turned into structured adoption.

### McKinsey — The State of AI in 2025

- URL: https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
- Used for: pilot-to-scale gap, agentic AI experimentation, workflow redesign as success factor, human validation, leadership ownership.
- Key relevance: supports the skill's field-deployment focus rather than demo-only AI strategy.

### Japan METI / MIC — AI Business Guidelines Version 1.0

- URL: https://www.meti.go.jp/press/2024/04/20240419004/20240419004.html
- Used for: Japan AI governance context and unified business guidelines.
- Key relevance: supports East Asia / Japan-aware deployment framing.

---

## 11. Final positioning

AI FIRST FDT SKILL is built around one belief:

> AI transformation is not a model choice. It is a field deployment problem.

A good AI agent should not only answer questions. It should help a company safely change the way work is done.

That requires research, diagnosis, workflow mapping, architecture, pilot design, governance, troubleshooting, adoption observation, and public-safe communication.

That is the job of AI FIRST FDT SKILL.
