# Changelog

## 0.1.4 - Split dependency add-ons from no-dependency core

- Added `ai-first-fde-addons` as a separate optional skill for dependency-based advanced outputs.
- Kept `ai-first-fde` as the no-dependency Markdown / Mermaid / table / checklist core.
- Removed heavyweight runtime references from the FDE stitching path because they are not directly required.
- Updated README workbench tables to separate core usage from optional add-ons.
- Added the add-on skill to `skills.sh.json`.

## 0.1.3 - Solidified specialist stitching into main skill

- Moved the specialist stitching workbench into `skills/ai-first-fde/SKILL.md` so the main skill file is self-contained for personal and agent runtime use.
- Removed the separate adjacent stitching reference file to avoid splitting the operating rules across multiple files.
- Narrowed stitching guidance to specialist capabilities that materially improve FDE deliverables and are not usually installed by default.
- Clarified that ordinary communication and office tools are input sources, not specialist dependencies.
- Updated all README language pages to summarize the specialist workbench while pointing agents to the main skill file for the full rules.

## 0.1.2 - Default English README and Simplified Chinese README

- Changed the root `README.md` from a short language gateway into a full English default README so the GitHub landing page has complete content immediately.
- Added `README.zh-CN.md` as a full Simplified Chinese README.
- Updated all language selectors to include English, Traditional Chinese, Simplified Chinese, and Japanese.
- Updated the validator to require the Simplified Chinese README.

## 0.1.1 - East Asia transformation and skill stitching expansion

- Expanded English, Traditional Chinese, and Japanese README files into full standalone language pages.
- Added the East Asia transformation stance: AI adoption should reduce overtime, rework, and repetitive administration while preserving human expertise instead of framing deployment around layoffs.
- Added organization architecture, stakeholder relationship, approval route, workflow handoff, and escalation mapping to the main FDE operating loop.
- Added LLM Wiki / knowledge graph handoff guidance for scattered enterprise knowledge.
- Added adjacent skill stitching guidance so FDE can use diagram, wiki, graph, agent runtime, research, deployment, governance, and documentation skills as optional accelerators.
- Added organization architecture and LLM Wiki templates.

## 0.1.0 - Initial public release

- Created AI First FDE Skill.
- Added main orchestrator skill and six focused subskills.
- Added templates, references, checklists, eval cases, validation script, and multilingual README files.
