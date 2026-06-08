# Troubleshooting Runbook

## Common incidents

### RAG misses relevant documents

Check source availability, ingestion status, chunking, metadata, query rewrite, language mismatch, permissions filter, embedding model, and stale index.

### User sees restricted data

Contain immediately. Disable affected retrieval scope. Audit ACL metadata, index filters, citation logic, cache, and logs. Re-test with boundary accounts.

### AI gives confident wrong answer

Check prompt policy, retrieval evidence, model temperature, answer citation requirement, evaluation set, and human review gate.

### Users refuse to use tool

Check whether the tool increases workload, threatens status, lacks manager support, or creates responsibility risk.

## Required incident output

- Symptom
- Impact
- Affected users
- Containment
- Evidence needed
- Likely layer
- Root cause
- Fix
- Verification
- Prevention
