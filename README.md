# AI FIRST FDT SKILL

A public Hermes / Claude-style skill suite created by **Jackz.ai** for deploying AI inside **East Asian enterprise organizations**.

This is not a generic AI consulting prompt. It is an operating system for front-line AI deployment: discovery, diagnostic interviews, technical architecture, pilot execution, troubleshooting, adoption observation, governance, and public-safe delivery documentation.

## Languages

Full README files:

- 繁體中文：[`README.zh-Hant.md`](README.zh-Hant.md)
- English: [`README.en.md`](README.en.md)
- 日本語：[`README.ja.md`](README.ja.md)

Short public descriptions for sharing on GitHub / X / docs:

- 繁體中文：[`docs/descriptions/zh-Hant.md`](docs/descriptions/zh-Hant.md)
- English: [`docs/descriptions/en.md`](docs/descriptions/en.md)
- 日本語：[`docs/descriptions/ja.md`](docs/descriptions/ja.md)

## Install with Hermes

Install the main orchestration skill:

```bash
hermes skills install skills-sh/jacksoncoin0202-ops/ai-first-fdt-skill/skills/ai-first-fdt
```

Install the full suite manually by copying the `skills/*` folders into your Hermes skills directory, or install each module as needed:

```bash
hermes skills install skills-sh/jacksoncoin0202-ops/ai-first-fdt-skill/skills/ai-first-fdt-research
hermes skills install skills-sh/jacksoncoin0202-ops/ai-first-fdt-skill/skills/ai-first-fdt-diagnostic
hermes skills install skills-sh/jacksoncoin0202-ops/ai-first-fdt-skill/skills/ai-first-fdt-architecture
hermes skills install skills-sh/jacksoncoin0202-ops/ai-first-fdt-skill/skills/ai-first-fdt-deployment
hermes skills install skills-sh/jacksoncoin0202-ops/ai-first-fdt-skill/skills/ai-first-fdt-troubleshooting
hermes skills install skills-sh/jacksoncoin0202-ops/ai-first-fdt-skill/skills/ai-first-fdt-adoption-observer
```

## Skill modules

- `ai-first-fdt`: main orchestrator skill
- `ai-first-fdt-research`: research and source-grounded discovery
- `ai-first-fdt-diagnostic`: client deep diagnostic interview protocol
- `ai-first-fdt-architecture`: technical AI solution architecture
- `ai-first-fdt-deployment`: PoC, pilot, rollout, operations execution
- `ai-first-fdt-troubleshooting`: incident response and field debugging
- `ai-first-fdt-adoption-observer`: East Asian adoption resistance observation

## Public safety

This repository is public. Do not contribute customer names, confidential architecture, private contracts, credentials, internal URLs, employee names, or identifiable deployment details. Use anonymized cases only.

## Research grounding

The suite is informed by enterprise AI deployment practice, East Asian organizational culture, responsible AI governance, and public research references including Stanford HAI / AI Index, NIST AI RMF, OECD AI Principles, Microsoft Work Trend Index, McKinsey State of AI, and Japan METI / MIC AI Business Guidelines materials.

- Full research grounding report: [`docs/research/ai-first-fdt-research-report.en.md`](docs/research/ai-first-fdt-research-report.en.md)
- Source notes: [`docs/source-notes.md`](docs/source-notes.md)

This repository does not claim endorsement by any referenced organization.
