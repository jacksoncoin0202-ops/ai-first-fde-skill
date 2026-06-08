# Client Deep Diagnostic Interview

## Objective

Ask until the workflow becomes operationally visible.

## Core question bank

### Business

- What process are we improving?
- Why does it matter now?
- What failure is most expensive?
- What would a good 90-day outcome look like?
- Which pain is the strongest: time, cost, error, rework, risk, delay, lost sale, support burden, or employee frustration?
- Who will say the pilot succeeded?
- Who will say the pilot is not worth continuing?

### Workflow

- What triggers the process?
- What inputs enter the process?
- Who touches it?
- Which step takes the longest?
- Where do errors happen?
- What output is produced?
- Which step has no written SOP?
- Which handoff creates waiting, rework, or blame?
- Which workaround do users actually use outside the official process?
- Which old template, spreadsheet, ticket, email, or chat thread proves the current process?

### Data

- Where does the data live?
- Who owns it?
- How often is it updated?
- What is stale, duplicated, or missing?
- Which documents are authoritative?

### Permissions

- Who can view which information?
- Which fields are sensitive?
- What must never be exposed to another department?
- What requires audit logging?

### People

- Who uses the workflow daily?
- Who approves the output?
- Who will maintain the AI system?
- Who may resist and why?
- Who is the executive sponsor?
- Who removes blockers weekly?
- Who is the workflow owner?
- Who is the data owner?
- Who is the respected reviewer users will trust?
- Which staff function must be involved early: legal, compliance, security, procurement, HR, finance, or IT?
- Which group fears replacement, blame, extra work, or loss of status?
- Who has informal veto power even without a formal title?
- What is the formal organization chart for the workflow?
- Where does real influence differ from the formal organization chart?
- Which senior staff member should become reviewer, trainer, approver, or process owner?
- Which team needs reassurance that this is a transformation effort, not a layoff program?
- Which group will benefit from less overtime, less rework, or less repetitive administration?
- Which manager must privately understand the change before users hear about it formally?

### Organization architecture

- Which departments touch the workflow?
- Which department owns the business result?
- Which department owns the system?
- Which department owns the data?
- Which department owns the risk if the AI output is wrong?
- Which committee, manager, or senior reviewer approves changes?
- Which handoff creates delay, ambiguity, or blame?
- Which escalation path is used when the workflow fails?
- Which role should own AI operations after rollout?
- Which relationship should be drawn as informal influence rather than formal reporting?

### Knowledge / LLM Wiki

- Where does operational knowledge live today: wiki, shared drive, email, chat, spreadsheets, ticket system, SOP, PDF, or individual memory?
- Which source is authoritative?
- Which source is stale, duplicated, or disputed?
- Who owns each knowledge domain?
- Who can approve updates?
- Which knowledge can AI read?
- Which knowledge must remain department-scoped or role-scoped?
- Which contradictions require human review?
- Which pages should exist in an LLM Wiki before retrieval or automation starts?
- What update cadence is required: daily, weekly, monthly, quarterly, or event-based?

### Risk

- What happens if AI gives a wrong answer?
- What happens if AI exposes restricted data?
- Which actions require human approval?

### KPI

- Current time per task?
- Current error or rework rate?
- Current volume?
- Target improvement?
- Current queue size or backlog?
- Current approval cycle time?
- Current adoption or usage rate?
- Current escalation rate?
- Pilot success threshold?
- Stop condition?

## Pain map procedure

1. Ask for the last three real cases.
2. Reconstruct each case step by step.
3. Mark time, rework, waiting, risk, and owner at each step.
4. Identify where AI helps: draft, classify, search, summarize, compare, extract, route, monitor, or execute.
5. Mark where AI must not act without human approval.
6. Select the lowest-risk step with measurable pain.

## Relationship map procedure

Create a table before solution design:

| Role | Person / team | What they care about | What they fear | What they can block | How to involve them |
|---|---|---|---|---|---|
| Executive sponsor | | KPI / roadmap / risk | failed ROI | budget / priority | weekly steering |
| Workflow owner | | throughput / quality | disruption | process access | pilot owner |
| Daily users | | workload / clarity | blame / replacement | adoption | private interviews |
| Security / legal / compliance | | risk control | exposure / policy breach | approval | early design partner |
| IT / data owner | | integration / maintenance | support load | access | scoped data path |
| Senior reviewer | | quality / status | loss of expertise | trust | reviewer role |

Do not write architecture until the relationship map has named blockers and handling actions.

## Organization map procedure

Create an organization architecture map before solution design when more than one department, approver, system owner, or data owner is involved.

Minimum map:

| Node | Type | Formal owner | Real influence | Receives from | Sends to | Risk if skipped |
|---|---|---|---|---|---|---|
| Business department | Department | | | | | |
| Workflow owner | Role | | | | | |
| Data owner | Role / team | | | | | |
| IT / system owner | Team | | | | | |
| Legal / compliance / security | Staff function | | | | | |
| Senior reviewer | Person / role | | | | | |
| Daily users | User group | | | | | |
| Informal veto holder | Person / role | | | | | |

Then produce one of:

- Mermaid organization / relationship diagram;
- large architecture diagram if diagram tooling is available;
- knowledge graph if graph tooling is available;
- Markdown map if no diagram tooling is available.

## LLM Wiki procedure

If knowledge is scattered, do not design retrieval immediately. First produce a wiki handoff:

1. List raw sources.
2. Mark source owner and update owner.
3. Mark permission boundary.
4. Group sources into domains.
5. Create page taxonomy.
6. Identify contradictions and stale sources.
7. Define update cadence.
8. Define what AI may read, cite, summarize, or never expose.
9. Define how new knowledge enters the wiki after pilot.
