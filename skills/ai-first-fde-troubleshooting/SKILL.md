---
name: ai-first-fde-troubleshooting
description: Use this skill when an AI deployment has a field problem: bad answers, RAG misses, permission leaks, integration failures, latency, cost spikes, user complaints, adoption failure, or production incident.
version: 0.1.0
author: Jackz.ai
license: MIT
metadata:
  hermes:
    category: business
    tags: [jackz-ai, fde, enterprise-ai, east-asia]
---

# Field Troubleshooting


You diagnose AI deployment incidents by layer.

## Incident protocol

1. State the symptom.
2. Define impact and affected users.
3. Contain risk if sensitive data or wrong external output is involved.
4. Reproduce the issue.
5. Identify the likely layer.
6. Gather evidence.
7. Form root cause hypotheses.
8. Apply the safest fix.
9. Verify the fix.
10. Add prevention.

## Layers

- User instruction layer
- Workflow layer
- Data source layer
- Ingestion layer
- Chunking / indexing layer
- Retrieval layer
- Permission layer
- Prompt / policy layer
- Model layer
- Tool/API layer
- UI layer
- Monitoring layer
- Training/adoption layer

## Output

- Incident summary
- Root cause analysis
- Short-term workaround
- Long-term fix
- Verification steps
- Prevention checklist

