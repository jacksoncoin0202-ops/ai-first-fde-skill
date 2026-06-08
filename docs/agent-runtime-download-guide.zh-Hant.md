# Agent / CLI Runtime 下載與使用指南

最後核對日期：2026-06-08

AI FIRST FDT SKILL 不應只綁定 Hermes。它的核心是一套公開安全的 `SKILL.md` 與 references，可以放入任何能讀 Markdown、rules、project memory、skills、MCP 或 prompt context 的 Agent runtime。

## 使用原則

1. 先從官方網站、官方 GitHub、官方 docs 或官方 marketplace 下載。
2. 不要使用 SEO install guide、陌生 npm package、陌生 App Store wrapper，尤其是聲稱「Claude Code / Codex / Gemini / OpenClaw 一鍵破解」的工具。
3. 安裝後先跑 `--version`、`doctor`、`help` 或登入檢查，再把 repo 交給 agent。
4. OpenRouter 是模型路由 API，不是獨立桌面 agent。它通常接到 Cline、OpenCode、Aider、自建 Agent SDK 或其他 OpenAI-compatible client。
5. 如果某個工具已停止維護或改名，要在交付文件中標明狀態，不要當成主要推薦。

## 通用下載與使用流程

```bash
git clone https://github.com/jacksoncoin0202-ops/ai-first-fdt-skill.git
cd ai-first-fdt-skill
```

然後在你的 agent 裡面要求它讀：

```text
請先讀 skills/ai-first-fdt/SKILL.md。
如果任務需要研究、診斷、架構、部署、排障或 adoption observation，
請再讀對應的 skills/ai-first-fdt-* 模組與 skills/ai-first-fdt/references/。
```

如果 agent 支援 project rules 或 memory，可以把 `skills/ai-first-fdt/SKILL.md` 放入該工具的 rules / project instruction / memory。若 agent 支援 native skills，則把 `skills/*` 整個資料夾複製或安裝到該 runtime 的 skills 目錄。

## Agent / CLI 下載矩陣

| Runtime | 類型 | 官方下載方法 | FDT 使用方法 |
| --- | --- | --- | --- |
| Hermes | Skill runtime | `hermes skills install skills-sh/jacksoncoin0202-ops/ai-first-fdt-skill/skills/ai-first-fdt` | 原生安裝主控 skill，其他模組可逐個 install 或複製 `skills/*`。 |
| Claude Code | Terminal coding agent | macOS / Linux / WSL: `curl -fsSL https://claude.ai/install.sh \| sh`; Windows: `irm https://claude.ai/install.ps1 \| iex`; Homebrew: `brew install --cask claude-code`; npm: `npm install -g @anthropic-ai/claude-code` | 在 repo 內啟動 `claude`，要求它先讀 `skills/ai-first-fdt/SKILL.md`。可把指令摘要放入 `CLAUDE.md`。 |
| OpenAI Codex CLI | Terminal / IDE / desktop coding agent | macOS / Linux: `curl -fsSL https://chatgpt.com/codex/install.sh \| sh`; Windows: `powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 \| iex"`; npm: `npm install -g @openai/codex`; Homebrew: `brew install --cask codex` | 在 repo 內啟動 `codex`，要求它讀 `skills/ai-first-fdt/SKILL.md`。Codex 亦可透過 ChatGPT plan 或 API key 登入。 |
| Cursor | Agent-first IDE / CLI | Desktop: `https://cursor.com/download`; terminal installer: `curl https://cursor.com/install -fsS \| bash` | 開啟 repo，把 FDT instruction 放入 Cursor rules，或在任務 prompt 指定讀 `skills/ai-first-fdt/SKILL.md`。 |
| OpenRouter | Model router / API / Agent SDK | 建立 OpenRouter key，使用 `https://openrouter.ai/api/v1` 或安裝 SDK：`npm install @openrouter/sdk`、`npm install @openrouter/agent` | 不直接「下載 FDT」。把 OpenRouter 作為模型供應商接入 Cline、OpenCode、Aider、自建 agent 或 OpenAI-compatible client，再載入 FDT skill。 |
| OpenCLI, jackwener/opencli | Browser / desktop tool bridge for agents | `npm install -g @jackwener/opencli`; 驗證：`opencli --version`、`opencli list`、`opencli doctor` | 不是 FDT 主 runtime，而是讓 agent 操作 browser / desktop / website CLI 的工具層。可配合 Claude Code、Cursor、Codex 等使用。 |
| OpenCLI, opencli.co | CLI discovery / work-router site | 使用 `https://opencli.co/` 查找任務所需 CLI stack | 作為研究入口，幫 FDT 找到適合處理 PDF、CSV、PR review、email search 等任務的 CLI。 |
| OpenCLI, opencli.run | Local multimodal CLI engine | macOS: `brew tap openclirun/opencli` 後 `brew install opencli` | 偏向本機 multimodal capability engine。若要用，先確認是否符合 Apple Silicon / MLX / local model 場景。 |
| OpenCode | Open-source terminal / desktop / IDE coding agent | Terminal: `curl -fsSL https://opencode.ai/install \| bash`; npm: `npm i -g opencode-ai`; bun: `bun add -g opencode-ai`; Homebrew: `brew install anomalyco/tap/opencode`; desktop beta: `brew install --cask opencode-desktop` | 在 OpenCode session 讀 `skills/ai-first-fdt/SKILL.md`，或把 FDT 原則放入 project rules。 |
| Gemini CLI | Google terminal agent | npx: `npx https://github.com/google-gemini/gemini-cli`; npm: `npm install -g @google/gemini-cli`; Homebrew: `brew install gemini-cli` | 在 repo 內啟動 `gemini`，要求它讀 FDT skill。可用 Google login 或組織授權。 |
| GitHub Copilot CLI | GitHub-native terminal agent | npm: `npm install -g @github/copilot`; Windows: `winget install GitHub.Copilot`; Homebrew: `brew install copilot-cli`; script: `curl -fsSL https://gh.io/copilot-install \| bash` | 適合 issue / PR / GitHub workflow。把 FDT 作為 planning / discovery / deployment rules 載入。 |
| Windsurf | Agentic IDE | 官方 download page 提供 macOS、Windows、Linux installer | 開啟 repo，將 FDT instruction 放入 Windsurf rules / memories，或在 Cascade 任務 prompt 指定讀 `skills/ai-first-fdt/SKILL.md`。 |
| Cline | IDE extension / CLI / SDK | IDE extension: 在 VS Code / Cursor / Windsurf / VSCodium / JetBrains marketplace 搜尋 `Cline`; CLI: `npm install -g cline`，再 `cline auth` | Cline 可接 Anthropic、OpenAI、OpenRouter、Gemini、Bedrock、Ollama 等 provider。將 FDT 放入 prompt / rules。 |
| Aider | Terminal pair-programming agent | `python -m pip install aider-install`，再 `aider-install` | Aider 主要做 git-first coding。可把 FDT 作為 task brief 或 prompt context，用於文件、架構與交付包生成。 |
| Continue | VS Code / JetBrains AI coding platform | 從 Visual Studio Marketplace 或 JetBrains Marketplace 安裝 Continue extension | 適合 BYO model、repo rules、codebase chat。把 FDT instruction 加入 workspace config 或 prompt。 |
| Devin CLI | Local CLI with Devin Cloud integration | `curl -fsSL https://cli.devin.ai/install.sh \| bash` | 若團隊使用 Devin，將 FDT 作為 discovery / delivery playbook 交給 Devin session。 |
| Roo Code | VS Code agent extension | 官方 docs 顯示 Roo Code Extension 已於 2026-05-15 shut down；舊 extension 仍有 marketplace / Open VSX 入口 | 不建議當新導入首選。若既有團隊仍使用，需標明 shutdown 狀態，並考慮 Cline 或社群 fork。 |

## FDT 研究方法：怎樣查一個 Agent 能否使用

對每個候選 agent，都記錄以下欄位：

- 官方來源：download page、GitHub repo、docs、marketplace。
- 安裝命令：macOS、Linux、Windows 是否不同。
- 驗證命令：`--version`、`doctor`、`help`、登入檢查。
- 身份驗證：API key、OAuth、ChatGPT plan、Claude Enterprise、GitHub Copilot subscription、Google login、OpenRouter key。
- Skill 載入方式：native skill、project rules、AGENTS.md / CLAUDE.md / GEMINI.md、IDE rules、prompt context、MCP。
- 權限與風險：能否改檔、跑 shell、上網、讀瀏覽器登入狀態、連 SaaS、寫 GitHub PR。
- 是否仍維護：release notes、docs 更新日期、shutdown notice、repo archived 狀態。
- 企業適配：SSO、audit log、policy control、data retention、model provider choice、offline / local model 支援。

## 官方來源清單

- Claude Code: https://support.claude.com/en/articles/14552382-your-first-day-in-claude-code
- OpenAI Codex CLI: https://github.com/openai/codex
- Cursor download: https://cursor.com/download
- OpenRouter quickstart: https://openrouter.ai/docs/quickstart
- OpenCLI, jackwener/opencli: https://opencli.info/docs/guide/installation.html
- OpenCLI work router: https://opencli.co/
- OpenCLI local engine: https://www.opencli.run/
- OpenCode download: https://opencode.ai/download
- Gemini CLI: https://google-gemini.github.io/gemini-cli/
- GitHub Copilot CLI: https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli
- Windsurf download: https://windsurf.com/download
- Cline install: https://docs.cline.bot/getting-started/installing-cline
- Aider: https://aider.chat/
- Continue install: https://docs.continue.dev/getting-started/install
- Devin CLI: https://cli.devin.ai/
- Roo Code docs: https://docs.roocode.com/
