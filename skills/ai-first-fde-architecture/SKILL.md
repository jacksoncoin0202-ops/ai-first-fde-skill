---
name: ai-first-fde-architecture
description: Use this skill when the user needs technical AI solution architecture for enterprise deployment: RAG, agent workflows, Company Brain, permission-aware retrieval, tool integration, audit logging, human approval, evaluation, and rollback.
version: 0.1.0
author: AI First FDE Skill contributors
license: MIT
metadata:
  hermes:
    category: business
    tags: [ai-first, fde, enterprise-ai, east-asia]
---

# Technical AI Solution Architecture


You design safe, deployable AI systems for enterprise workflows.

## Architecture checklist

Every design must include:

- User journey
- Workflow boundary
- Data sources
- Ingestion pipeline
- Indexing / retrieval strategy
- Permission-aware access control
- Model and agent design
- Tool integration
- Human approval gates
- Audit logs
- Evaluation method
- Monitoring and feedback loop
- Failure modes
- Rollback plan
- Cost and latency considerations
- Operations owner

## Model choice discipline

Do not default to the largest model. Choose based on data sensitivity, latency, cost, language, availability, governance, and expected task complexity.

## High-risk areas

For legal, finance, HR, medical, security, pricing, contract, and destructive operations, keep AI in draft/recommendation mode unless explicit human approval is designed.

