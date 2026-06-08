# AI First FDE Skill

AI First FDE Skill 是一套 Markdown-only、no-build 的前線部署工程師 Skill Suite，用於企業 AI 現場導入。

它不是顧問式空泛提示詞，而是讓 agent 像 Forward Deployed Engineer 一樣工作：先找真實痛點，再拆流程、資料、權限、關係阻力、PoC、Pilot、Rollout、驗收與維運。

## Quick Start

```bash
git clone https://github.com/jacksoncoin0202-ops/ai-first-fde-skill.git
cd ai-first-fde-skill
```

然後對 agent 說：

```text
請先讀 skills/ai-first-fde/SKILL.md。
如果任務需要研究、診斷、架構、部署、排障或 adoption observation，請再讀對應的 skills/ai-first-fde-* 模組與 skills/ai-first-fde/references/。
```

## 無依賴 / 不需要編譯

使用這套 Skill 不需要 Python、npm、pip、Docker、compiler 或 binary installer。

Skill 本身是 Markdown。Python validator 只給維護者和 CI 使用，終端使用者不用安裝。

## 它做什麼

- 先找真正業務痛點，再談工具；
- 盤點流程、owner、資料、權限、風險與 KPI；
- 找出 sponsor、阻力來源、日常使用者、senior reviewer 與 informal veto holder；
- 設計 PoC、Pilot、Rollout、Rollback 與 Operations gate；
- 處理東亞企業常見的面子、階層、共識、風險迴避與表面同意；
- 產出可驗收、可維運、可公開安全改寫的文件。

## 模組

- `ai-first-fde`：主控 Skill
- `ai-first-fde-research`：來源驗證與研究
- `ai-first-fde-diagnostic`：客戶深度診斷
- `ai-first-fde-architecture`：AI 技術方案架構
- `ai-first-fde-deployment`：PoC、Pilot、Rollout、Operations
- `ai-first-fde-troubleshooting`：現場排障
- `ai-first-fde-adoption-observer`：使用者阻力與採用觀察

## 執行流程

1. 定義 workflow 與業務痛點。
2. 用真實文件、ticket、表格、email、log 重建現有流程。
3. 盤點資料、權限、owner、審批點與風險。
4. 畫出 sponsor、阻力來源、daily users、reviewers、legal / security / compliance / IT。
5. 選一個窄範圍、可回復、可量度的 pilot。
6. 定義 KPI、人工審批模式、fallback、stop / continue / expand 條件。
7. 每週做 sponsor review 與 user feedback loop。
8. 只有在真實使用、KPI 有改善、operations owner 明確後才 scale。

## 標準交付物

- Engagement Brief
- Problem Map
- Stakeholder Map
- Data / Permission Model
- Technical Solution Architecture
- PoC Plan
- Pilot Plan
- Deployment Runbook
- Adoption Risk Register
- Troubleshooting Report
- Validation Checklist
- Operations Handbook
- Executive Summary
- Public-safe Case Rewrite

## 可配合任何 Agent Runtime

只要 agent 能讀 Markdown 或 project rules，就可以使用這套 Skill，例如 Claude Code、OpenAI Codex CLI、Cursor、Hermes、OpenCode、Gemini CLI、Cline、Aider、Continue、Devin CLI，以及 OpenRouter-backed agents。

Agent / CLI 下載指南見：[docs/agent-runtime-download-guide.zh-Hant.md](docs/agent-runtime-download-guide.zh-Hant.md)

## 公開安全

這是公開 repo。不要提交客戶名稱、內部架構、合約、credential、內部 URL、員工姓名或可識別的部署細節。

## 研究基礎

本 Skill 參考企業 AI 落地實務、東亞組織文化、負責任 AI 治理、Stanford Digital Economy Lab 2026 Enterprise AI Playbook、Stanford HAI / AI Index、NIST、OECD、Microsoft WorkLab、McKinsey、日本 METI / MIC 等公開資料。

本 repo 不代表任何引用機構背書。

## License

MIT License.
