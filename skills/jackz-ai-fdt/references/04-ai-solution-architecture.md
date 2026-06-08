# AI Solution Architecture

## Architecture decision tree

- If the problem is knowledge lookup with changing documents: prefer RAG with permission-aware retrieval.
- If the problem is repetitive structured task execution: consider workflow automation with human approval gates.
- If the problem is document transformation: use extraction, validation, and review pipeline.
- If the problem is customer-facing response: keep AI in draft mode until enough quality data exists.
- If the problem is domain judgment: use AI as assistant, not autonomous decision-maker.

## Required architecture sections

- User flow
- System flow
- Data source list
- Ingestion and refresh cadence
- Metadata schema
- ACL / permission model
- Retrieval strategy
- Model routing
- Tool registry
- Human approval points
- Logging and audit
- Evaluation suite
- Monitoring dashboard
- Failure and rollback
