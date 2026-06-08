# AI FIRST FDT SKILL

這是 **Jackz.ai** 創造的公開 Hermes / Claude-style Skill Suite，專門針對**東亞文化脈絡下的公司組織**進行 AI 導入、技術落地與現場排障。

它不是一般 AI 顧問提示詞，也不是單純寫方案的模板。它的定位是：

> 讓 Agent 變成一位 AI FIRST Field Deployment Technician，進入企業現場後，能夠問到底、查清楚、設計方案、執行落地、排查問題、觀察使用者反應，最後交付可驗收、可維運、可公開安全改寫的成果。

## 為什麼 Jackz.ai 要做這個 Skill？

東亞企業導入 AI 的問題，通常不是「不知道 ChatGPT 是什麼」。真正的阻力在於：

- 高階主管想推 AI，但一線不知道怎麼用。
- IT 部門擔心資安、權限、維運負擔。
- 中階主管擔心流程被繞過、責任變模糊。
- 資深員工擔心 know-how 被抽走，影響地位。
- 一線員工表面配合，實際仍回到舊流程。
- 公司文化重視面子、共識、階層、風險迴避，不適合直接套用美式 SaaS adoption 模板。

因此這個 Skill 的核心不是「推銷 AI」，而是協助企業完成：

1. 業務拆解
2. 流程改造
3. 工具選型
4. 權限與資料治理
5. 技術架構設計
6. 小範圍 PoC
7. Pilot 上線
8. 使用者訓練
9. 現場排障
10. 反應觀察
11. 驗收與維運交接

## 適用對象

- AI 導入顧問
- 前線部署工程師
- 企業內部 AI champion
- 系統整合商
- IT 服務公司
- 技術服務公司
- 日本、台灣、香港、韓國、新加坡、中國大陸等東亞文化脈絡下的企業團隊
- 需要把 AI 從簡報帶到現場流程的人

## 不適用範圍

此 Skill 不適合用於：

- 未經授權蒐集客戶機密
- 自動化高風險決策而無人工審批
- 取代法務、財務、醫療、資安專業責任
- 將未匿名化的真實客戶案例公開發布
- 只想產生空泛 AI 趨勢文章的情境

## Skill 結構

這是一個 Skill Suite，不是單一薄文件。

- `ai-first-fdt`：主控 Skill，負責判斷任務、選擇模組、整合交付。
- `ai-first-fdt-research`：查詢研究與來源驗證。
- `ai-first-fdt-diagnostic`：客戶深度盤問，打破沙盆問到底。
- `ai-first-fdt-architecture`：AI 技術方案與系統架構。
- `ai-first-fdt-deployment`：PoC、Pilot、Rollout、Operations。
- `ai-first-fdt-troubleshooting`：現場疑難排解。
- `ai-first-fdt-adoption-observer`：使用者反應與東亞企業導入阻力觀察。

## 基本使用方式

對 Agent 說：

```text
使用 Jackz.ai FDT 模式，幫我為一家 200 人技術服務公司設計 AI First 導入方案。
```

或：

```text
使用 FDT diagnostic，幫我盤問這個客戶的 AI 導入需求，不要直接寫方案。
```

或：

```text
我們的內部知識庫 AI 回答不準，而且員工不願意用。請用 FDT troubleshooting 和 adoption observer 幫我診斷。
```

## 標準輸出

完成一次 FDT 任務後，理想交付包包含：

- Engagement Brief
- Client Discovery Report
- Problem Map
- Stakeholder Map
- Use Case Prioritization Matrix
- Data / Permission Model
- Technical Solution Architecture
- PoC Plan
- Pilot Plan
- Deployment Runbook
- Adoption Risk Register
- Training Plan
- Troubleshooting Report
- Validation Checklist
- Operations Handbook
- Executive Summary
- Public-safe Case Rewrite

## 東亞企業導入原則

這個 Skill 預設採用以下原則：

- 先理解組織脈絡，再談工具。
- 先找低風險 quick win，再碰核心流程。
- 不公開羞辱低使用者。
- 不把 AI 包裝成裁員工具。
- 讓資深員工成為 reviewer，而不是被替代者。
- 用團隊指標，而非一開始做個人排行榜。
- 正式會議前先做非正式對齊。
- 重要流程保留人工審批與回退方案。
- 每個 deployment 都要有權限、紀錄、驗收、維運責任。

## 研究基礎

本 Skill 參考了企業 AI 落地經驗、東亞職場導入脈絡、負責任 AI 治理原則，以及 Stanford HAI / AI Index 等公開研究方向。公開 repo 不包含任何客戶私密資料，也不代表 Stanford 對本 Skill 背書。

## 公開安全

若你要提交案例，請先匿名化：

- 移除真實公司名稱
- 移除員工姓名
- 移除內部系統網址
- 移除 API key / token / credential
- 移除私有報價與合約
- 移除可識別的內部政治細節
- 移除未公開資安架構弱點

## License

MIT License.
