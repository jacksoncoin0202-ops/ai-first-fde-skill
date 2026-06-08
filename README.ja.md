# AI First FDE Skill

AI First FDE Skill は、企業 AI の現場導入を支援する Markdown-only / no-build の Skill Suite です。

Agent を Forward Deployed Engineer として動かし、実際の業務フロー、データ、権限、関係者、抵抗、PoC、Pilot、Rollout、運用引き継ぎまでを扱います。

## Quick Start

```bash
git clone https://github.com/jacksoncoin0202-ops/ai-first-fde-skill.git
cd ai-first-fde-skill
```

Agent に次のように指示します。

```text
まず skills/ai-first-fde/SKILL.md を読んでください。
調査、診断、アーキテクチャ、デプロイ、トラブルシューティング、採用観察が必要な場合は、対応する skills/ai-first-fde-* モジュールと skills/ai-first-fde/references/ を読んでください。
```

## 依存関係なし / ビルド不要

この Skill を使うために Python、npm、pip、Docker、compiler、binary installer は不要です。

Skill 本体は Markdown です。Python validator はメンテナンスと CI 用の任意ツールであり、利用者には不要です。

## 何をするか

- ツール選定の前に、本当の業務課題を特定する。
- 業務フロー、owner、データ、権限、リスク、KPI を整理する。
- sponsor、阻害要因、日常利用者、senior reviewer、informal veto holder を可視化する。
- PoC、Pilot、Rollout、Rollback、Operations gate を設計する。
- 東アジア企業に多い階層、面子、合意形成、リスク回避、表向きの同意を扱う。
- レビュー可能、運用可能、公開時に安全な成果物を作る。

## モジュール

- `ai-first-fde`：メイン orchestration skill
- `ai-first-fde-research`：公開情報と根拠の確認
- `ai-first-fde-diagnostic`：顧客深掘り診断
- `ai-first-fde-architecture`：AI ソリューションアーキテクチャ
- `ai-first-fde-deployment`：PoC、Pilot、Rollout、Operations
- `ai-first-fde-troubleshooting`：現場トラブル対応
- `ai-first-fde-adoption-observer`：利用者抵抗と採用状況の観察

## 実行フロー

1. 対象 workflow と業務課題を定義する。
2. 実際の文書、ticket、表、email、log で現行プロセスを再構成する。
3. データ、権限、owner、承認ポイント、リスクを整理する。
4. sponsor、阻害要因、daily users、reviewers、legal / security / compliance / IT を整理する。
5. 狭く、安全で、測定可能な pilot を選ぶ。
6. KPI、人間の監視モード、fallback、stop / continue / expand 条件を決める。
7. 週次 sponsor review と user feedback loop を回す。
8. 実利用、KPI 改善、operations owner が確認できてから scale する。

## 標準成果物

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

## 任意の Agent Runtime で利用可能

Markdown または project rules を読める agent であれば利用できます。Claude Code、OpenAI Codex CLI、Cursor、Hermes、OpenCode、Gemini CLI、Cline、Aider、Continue、Devin CLI、OpenRouter-backed agents などで利用できます。

Agent / CLI ダウンロードガイド：[docs/agent-runtime-download-guide.zh-Hant.md](docs/agent-runtime-download-guide.zh-Hant.md)

## 公開安全方針

このリポジトリは公開されています。顧客名、内部アーキテクチャ、契約、credential、内部 URL、社員名、識別可能な導入詳細を含めないでください。

## 研究基盤

本 Skill は、企業 AI 導入実務、東アジア組織文化、責任ある AI ガバナンス、Stanford Digital Economy Lab 2026 Enterprise AI Playbook、Stanford HAI / AI Index、NIST、OECD、Microsoft WorkLab、McKinsey、日本 METI / MIC の公開資料を参考にしています。

本 repo は、引用された組織による承認や提携を意味しません。

## License

MIT License.
