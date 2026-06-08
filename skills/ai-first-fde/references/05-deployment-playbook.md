# Deployment Playbook

## Phase 0: Readiness

- Confirm executive sponsor.
- Confirm workflow owner.
- Confirm data owner.
- Confirm IT/security owner.
- Confirm pilot users.
- Confirm success metrics.
- Confirm current workflow evidence: SOP, tickets, emails, forms, spreadsheets, logs, screenshots, or recordings.
- Confirm relationship map: sponsor, blockers, daily users, senior reviewers, and staff functions.
- Confirm no-blame experiment framing.
- Confirm fallback workflow.
- Confirm stop / continue / expand criteria.

Do not enter PoC if there is no sponsor, no workflow owner, no data access path, or no KPI.

## Phase 1: PoC

- Use narrow scope.
- Use limited data.
- Avoid destructive actions.
- Measure answer quality, latency, cost, and user comprehension.
- Choose a recoverable task with visible pain.
- Use real artifacts, not invented examples.
- Decide oversight mode:
  - Escalation: AI handles routine cases, humans review exceptions and samples.
  - Approval: AI drafts, humans approve every action before execution.
  - Collaboration: human and AI work together on high-judgment tasks.
- Log failures as process/data/training evidence, not blame.

## Phase 2: Pilot

- Select representative users.
- Provide training.
- Collect daily feedback.
- Keep fallback workflow active.
- Track KPI weekly.
- Run weekly sponsor review.
- Track adoption by team before individual ranking.
- Record why users avoid the tool.
- Fix workflow, data, permission, and training issues before adding features.
- Keep legal, security, compliance, and IT in the loop if they can block scale.

## Phase 3: Rollout

- Expand only after quality and adoption pass threshold.
- Publish SOP.
- Assign operations owner.
- Establish incident path.
- Expand by workflow, team, region, or risk tier. Do not jump to company-wide rollout.
- Reconfirm permission boundaries and logging.
- Publish support path and rollback path.
- Move senior staff into reviewer / quality-owner roles where useful.

## Phase 4: Operations

- Monthly quality review.
- Knowledge refresh owner.
- Access review.
- Cost review.
- New use case intake.
- KPI review.
- Adoption review.
- Incident review.
- Model / provider review for cost, latency, accuracy, and redundancy.
- Backlog review for next workflow.

## Scale gate

Scale only when all checks are true:

- The system is used in the real workflow.
- At least one KPI moved in the right direction.
- Daily users understand when to use it and when not to use it.
- The workflow owner accepts the new SOP.
- Security / legal / compliance blockers are closed or explicitly accepted.
- Operations owner is named.
- Support and rollback path are tested.
- The next rollout group has a clear relationship plan.
