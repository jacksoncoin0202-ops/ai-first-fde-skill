# Research and Discovery

## Research goal

Before designing a solution, gather enough evidence to understand the business, technical, regulatory, and adoption context.

## Source tiers

1. Public authoritative sources: government, standards bodies, reputable research organizations, official vendor docs.
2. Public market sources: credible media, company pages, benchmark reports.
3. User-provided internal materials: use for private reasoning only unless approved for public disclosure.
4. Assumptions: clearly labeled and never published as fact.

## Agent runtime and download research

When researching how a user can run AI FIRST FDT on the market's agent tools, do not stop at Hermes. Check the broader agent/runtime landscape, including:

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
- sunset or legacy tools such as Roo Code, if the user specifically mentions them

For each candidate runtime, record:

- Official source: download page, official docs, official GitHub repo, or official marketplace listing.
- Install method: macOS, Linux, Windows, npm, Homebrew, pip, extension marketplace, desktop installer, or curl script.
- Verification command: `--version`, `doctor`, `help`, login check, or first-run prompt.
- Authentication method: API key, OAuth, ChatGPT plan, Claude Enterprise, GitHub Copilot subscription, Google login, OpenRouter key, local model, or organization SSO.
- Skill loading method: native skill install, Markdown prompt, project rules, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, IDE rules, MCP, or SDK integration.
- Permission model: file edits, shell execution, network access, browser session reuse, SaaS access, GitHub issue/PR access, and approval mode.
- Maintenance status: release notes, docs update date, shutdown notice, archived repo, or vendor migration notice.
- Enterprise fit: data retention, audit logs, provider choice, policy controls, SSO, and local/offline support.

Use [`docs/agent-runtime-download-guide.zh-Hant.md`](../../../docs/agent-runtime-download-guide.zh-Hant.md) as the public-safe starting checklist, but refresh official links before giving time-sensitive install advice.

## Stanford grounding note

Stanford HAI / AI Index is useful for broad AI trend, adoption, productivity, governance, and public opinion framing. It should be cited as public research context only. Do not imply partnership or endorsement.

Public references:

- Stanford HAI 2025 AI Index Report: https://hai.stanford.edu/ai-index/2025-ai-index-report
- Stanford HAI homepage and human-centered AI mission: https://hai.stanford.edu/

## Output format

- Research question
- Public evidence
- What it means for deployment
- East Asia adaptation note
- Claims safe to use publicly
- Claims requiring approval
- Unknowns
