# AI First FDE Skill

**Jackz.ai** が作成した公開 Agent-runtime-neutral Skill Suite です。東アジアの企業文化を持つ組織における AI 導入、技術設計、現場展開、トラブルシューティング、利用定着を支援するために設計されています。

これは一般的な AI コンサルティング用プロンプトではありません。AI エージェントを、現場で動ける AI First Forward Deployed Engineer（FDE）として運用するためのスキル群です。

## 目的

企業 AI 導入の失敗要因は、多くの場合モデル性能だけではありません。実際には、業務フロー、データ品質、権限、責任分界、ガバナンス、現場利用者の心理的抵抗が重要です。

特に東アジア企業では、以下の要素を考慮する必要があります。

- 階層的な意思決定
- 面子と責任回避
- 公式会議前の非公式合意形成
- 失敗を避ける文化
- 年功序列と役割保護
- 表向きの賛成と実際の不使用
- 部門間の情報共有抵抗

## モジュール

- `ai-first-fde`: メイン統合 Skill
- `ai-first-fde-research`: 調査と情報源確認
- `ai-first-fde-diagnostic`: 顧客ヒアリングと深掘り診断
- `ai-first-fde-architecture`: AI 技術アーキテクチャ設計
- `ai-first-fde-deployment`: PoC、Pilot、本番展開、運用
- `ai-first-fde-troubleshooting`: 現場トラブル対応
- `ai-first-fde-adoption-observer`: 利用者反応と導入抵抗の観察

## Agent / CLI での利用

この Skill Suite は Hermes だけに限定されません。Claude Code、OpenAI Codex CLI、Cursor、OpenRouter-backed agents、OpenCLI workflows、OpenCode、Gemini CLI、GitHub Copilot CLI、Windsurf、Cline、Aider、Continue、Devin CLI など、Markdown instruction や project rules を読める agent runtime で利用できます。

- Agent / CLI download guide: [`docs/agent-runtime-download-guide.zh-Hant.md`](docs/agent-runtime-download-guide.zh-Hant.md)

## 安全方針

このリポジトリは公開されています。実在顧客名、内部システム URL、契約情報、認証情報、社員名、未公開の導入詳細を含めないでください。

## 研究メモ

本 Skill Suite は、企業 AI 導入実務、東アジア組織文化、責任ある AI ガバナンス、および Stanford HAI / AI Index などの公開研究を参考にしています。Stanford による承認や提携を意味するものではありません。
