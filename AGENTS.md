# AGENTS.md — Reproductive Genetics & Laboratory Wiki

本文件定義 **Reproductive Genetics & Laboratory Wiki**（採用 Andrej Karpathy 的 Persistent LLM Wiki 架構）之長期維護規則、操作流程、資料夾契約、醫學正確性護欄與品質檢核標準。所有參與本專案的 AI Agent 與人工編修者皆須遵守本規範。

---

## 1. 核心架構原則（Karpathy LLM Wiki Pattern）

本專案**不是**傳統一次性檢索問答（ad-hoc RAG）系統，而是持續累積與交叉連結的持久化知識庫：

```text
Raw Sources (immutable) ──▶ Persistent Wiki (integrated & cross-linked) ──▶ Knowledge Query (wiki-first)
```

1. **Raw Sources（`raw/`）不可任意修改**：原始擷取文獻與詮釋資料一經建立並計算 SHA-256，即視為不可變證據（immutable）。若來源更新，應以新版本記錄或附加補充來源，而非覆寫原檔內容。
2. **Persistent Wiki（`wiki/`）採整合式更新**：Ingest 新來源時，不可僅產出孤立的單篇摘要，必須檢查並更新受影響的產品頁、核心概念頁、臨床證據整合頁、實驗室作業頁、FAQ 與 `wiki/index.md`，維持跨頁交叉連結。
3. **Knowledge Query（查詢優先讀 Wiki）**：回答問題時應先讀取 `wiki/index.md` 定位相關頁面，優先閱讀已整合的 Wiki 知識，必要時再追溯 `raw/` 原始來源，並附上明確 Source ID 引用（如 `[SRC-001]`）。

---

## 2. 目錄結構契約

```text
.
├── AGENTS.md                  # 本規範文件（Agent 運作契約）
├── README.md                  # 專案說明與本機使用指南
├── assets/                    # 視覺與品牌圖檔（不可任意覆寫或篡改科學意義）
├── raw/
│   ├── registry.json          # 原始來源主清單（URL、DOI、SHA-256、狀態、擷取時間）
│   ├── sources/               # 原始擷取文字/節錄檔案（SRC-XXX.md / .txt）
│   └── metadata/              # 每篇來源結構化中繼資料（SRC-XXX.json）
├── wiki/
│   ├── index.md               # 全站知識索引與分類導覽（必先讀取）
│   ├── log.md                 # Persistent Wiki 編修與 Ingest 演進紀錄
│   ├── products/              # 檢測產品頁（PGT-A, ECS, PGT-SR, PGT-M）
│   ├── concepts/              # 生殖遺傳核心概念頁
│   ├── evidence/              # 臨床文獻摘要與跨指引證據整合頁
│   ├── laboratory/            # 實驗室概覽、PGT 流程、品質管理、檢體追溯
│   └── faq/                   # 患者與一般民眾常見問題
├── workflows/
│   ├── ingest_sources.py      # 來源擷取、驗證、SHA-256 計算與 registry 寫入工具
│   ├── lint_wiki.py           # Wiki 結構、Frontmatter、連結、引用與圖片驗證工具
│   └── build_browser_data.py  # 將 wiki/ 與 raw/ 編譯為本機 Wiki Browser 瀏覽資料
├── logs/
│   ├── asset_audit.md         # 圖片資產盤點報告
│   ├── ingest_report.json     # 最近一次 Ingest 執行結果
│   ├── lint_report.md         # 最近一次 Lint 檢核報告
│   └── human_review_queue.md  # 待人工臨床審核項目清單
└── wiki_browser/              # 暖橘色本機 Wiki Browser（非投影片簡報）
    ├── index.html
    ├── styles.css
    ├── app.js
    └── wiki_data.js           # 由 workflows/build_browser_data.py 自動產生
```

---

## 3. 目標讀者分層與語言規範

- **主要語言**：所有解說、Wiki 條目、摘要與介面皆使用**繁體中文**，保留必要且通用的英文專業術語（如 Aneuploidy、Mosaicism、Trophectoderm Biopsy、Allele Dropout、Residual Risk）。
- **一致性與讀者分層**：所有頁面必須維持一致的醫學事實，並依需要於頁面內或相關頁面區分深度：
  - **Patient（一般民眾與患者）**：白話說明、決策注意事項、常見迷思釐清（主要見於 Overview 與 FAQ）。
  - **Physician（醫師與醫療專業人員）**：適應症、臨床證據強度、指引差異與遺傳諮詢重點（主要見於 Clinical Relevance 與 Evidence）。
  - **Laboratory（實驗室人員）**：檢測原理、QC、驗證門檻、檢體追溯與技術限制（主要見於 Laboratory 與技術概念頁）。

---

## 4. 標準 Ingest 作業流程（SOP）

每當新增或更新原始來源（`SRC-XXX`）時，必須依序完成：

1. **真實擷取與驗證**：透過正式連線開啟 URL，驗證文件標題、年份、機構與可取得內容。若遭擋或僅取得部分內容，必須誠實標記 `failed` 或 `partially_retrieved` 並記錄原因，**嚴禁捏造未取得之文獻內容**，也不得將僅有 URL 的紀錄標示為 `ingested`。
2. **保存原始檔案與雜湊值**：將實際取得之原文或合法摘錄寫入 `raw/sources/SRC-XXX.md`，結構化紀錄寫入 `raw/metadata/SRC-XXX.json` 與 `raw/registry.json`，記錄 URL、DOI、作者/機構、年份、擷取日期與 SHA-256。
3. **概念萃取與差異比對**：提取核心醫學概念、適用對象、技術細節與限制，比對既有 Wiki 內容，辨識新增資訊、強化證據或跨指引差異／衝突。
4. **多頁整合與交叉連結**：同步更新受影響之產品頁、概念頁、證據整合頁、實驗室頁與 FAQ，並確保雙向／相關 Markdown 連結有效。
5. **更新索引與紀錄**：更新 `wiki/index.md`、`wiki/log.md` 與 `logs/human_review_queue.md`。
6. **執行品質檢核**：執行 `python3 workflows/lint_wiki.py` 與 `python3 workflows/build_browser_data.py`，確認零致命錯誤並將結果寫入 `logs/`。

---

## 5. Wiki 頁面格式與 YAML Frontmatter 標準

每篇位於 `wiki/` 子目錄的知識頁（`index.md` 與 `log.md` 除外）必須包含完整 YAML Frontmatter：

```yaml
---
title: "頁面標題（繁體中文含英文術語）"
category: "products | concepts | evidence | laboratory | faq"
summary: "1-2 句精準摘要，供索引與搜尋使用"
source_ids:
  - "SRC-001"
created_at: "YYYY-MM-DD"
updated_at: "YYYY-MM-DD"
review_status: "auto_compiled | source_verified | product_spec_verified | pending_clinical_review | pending_technical_verification | draft | approved"
review_layers: # 選填：用於同時標記多層級審核與驗證狀態（向下相容）
  - "source_verified"
  - "product_spec_verified"
  - "pending_clinical_review"
  - "pending_technical_verification"
related_pages:
  - "../concepts/aneuploidy.md"
---
```

- 正文應包含清楚的來源引用（例如 `[SRC-001]`）與 `## Sources` 區塊，追溯至 `raw/registry.json` 中的真實來源。
- 所有內部連結必須使用相對路徑（例如 `[Aneuploidy](../concepts/aneuploidy.md)`），便於 Markdown 閱讀與 Wiki Browser 解析。

---

## 6. 醫學正確性護欄與 Human Review 規則

本知識庫用於生殖遺傳衛教，**嚴格禁止以下錯誤宣稱與未經實證之推論**：

1. **不得憑空捏造或混用統計數值**：不可自行填入文獻未直接提供或各研究定義不一致的數值，特別是 Pregnancy Rate、Live Birth Rate、Clinical Pregnancy Rate、Diagnostic Accuracy、Sensitivity、Specificity 與 Mosaic Threshold。
2. **七大臨床不可逾越原則**：
   - 不得宣稱 PGT-A 能「保證懷孕」或「保證活產」。
   - 不得宣稱 PGT-A 對「所有 IVF 患者」都有確定臨床效益。
   - 不得宣稱 ECS 陰性代表「完全沒有遺傳疾病風險」（必須說明 Residual Risk）。
   - 不得將 Mosaic 切片結果直接等同於整顆胚胎（尤其是內細胞團 ICM）的真實染色體狀態。
   - 不得混淆 PGT-A（非整倍體篩檢）、PGT-SR（染色體結構重排檢測）與 PGT-M（單基因遺傳疾病檢測）的適用範圍與原理。
   - 不得將 ASRM、ESHRE 或 ACMG 的一般性指引直接描述為本實驗室已取得之認證、既有 SOP 或實測規格；缺乏本實驗室實測資料時，必須明確標示「一般性專業知識／待確認本實驗室實際規格」。
   - 不得假設新發表的單一研究必然優於既有國際臨床指引（如 ASRM / ESHRE / ACMG）。
3. **Human Review 分層標記規則**：凡涉及臨床建議、產品效益宣稱、檢測準確率、技術限制、跨文獻衝突、患者決策建議或公司實際產品規格的頁面，未經授權專業人員完整覆核前**不得將整頁標示為 `approved`**，並應依實際驗證程度搭配以下分層狀態（透過 `review_status` 與選填之 `review_layers` 記錄，同步登錄於 `logs/human_review_queue.md`）：
   - `source_verified`：引用之原始文獻或公司官方網頁來源已完成真實擷取與雜湊驗證。
   - `product_spec_verified`：頁面所列產品名稱、項目清單或已公開規格具備可追溯官方來源支持。
   - `pending_clinical_review`：臨床適應症、風險溝通或跨指引差異表述仍待臨床醫師／遺傳諮詢師覆核。
   - `pending_technical_verification`：具體設備型號、晶片、覆蓋深度、解析度、敏感度或報告週期（TAT）等技術規格仍待實驗室主管補充確認。
   - `approved`：僅於臨床與技術內容均經授權人員完整審核簽核後始可啟用。

---

## 7. 基本 Lint 與驗收檢核

每次更新 Wiki 後執行：

```bash
python3 workflows/lint_wiki.py
```

檢核項目包含：
- Raw Source 是否確實擷取成功且 SHA-256 吻合檔案內容
- 每篇 Wiki 頁面的 YAML Frontmatter 必填欄位是否齊全
- 所有 `source_ids` 與正文 `[SRC-XXX]` 引用是否存在於 `raw/registry.json` 且非空
- 所有 Wiki 內部相對連結與圖片路徑是否有效（無死連結）
- 是否有重複標題／slug 頁面
- 列出所有 `pending_clinical_review` / `draft` 高風險待審頁面
- 確認 `wiki/index.md` 是否涵蓋所有 Wiki 知識頁

---

## 8. Git Workflow 與版本控制規範

本專案以 **Git** 管理檔案版本，並以 `wiki/log.md` 記錄知識庫演進事件。**兩者職責互補且均須保留**：
- **Git 歷史**：追蹤檔案差異（Diff）、分支開發、Code/Content Review 與版本回溯。
- **Wiki Log（`wiki/log.md`）**：記錄文獻 Ingest 摘要、跨頁知識整合、差異衝突、Lint 檢核與人工審核事件。

### 8.1 分支策略（Branching Strategy）

- **`main`**：經過檢查且作為正式 Wiki 基準之主分支。未經人工核准，不得將含高風險臨床宣稱之未審修改直接合併入正式發布版本。
- **`source/*`**：新增或更新原始文獻與官方產品資料（例如 `source/igene-ecs`、`source/asrm-2025-pgta`）。
- **`content/*`**：產品介紹、核心概念、臨床證據整合、實驗室規格與衛教 FAQ 內容修訂（例如 `content/ecs-faq-update`）。
- **`fix/*`**：修復排版錯誤、壞連結、遺漏引用或腳本 Bug（例如 `fix/broken-citations`）。

### 8.2 高風險與待審頁面之 Git 管控原則

針對標示為 `pending_clinical_review` 或 `pending_technical_verification` 的頁面：
1. 可於 `source/*`、`content/*` 或 `fix/*` 工作分支進行編輯與提交。
2. **嚴禁 AI Agent 或未授權人員自行將 `review_status` 改為 `approved`**。
3. **不得未經人工臨床／技術確認即合併高風險臨床宣稱至正式對外發布分支**。
4. 所有修改必須保留明確 `Source ID`、更新 `logs/human_review_queue.md` 與 `wiki/log.md`。

### 8.3 Commit 規範（Conventional Commits）

所有 Commit 須遵守 Conventional Commits 格式（禁止使用 `update files` 等籠統訊息）：
- `docs(pgta): update PGT-A clinical evidence`
- `docs(ecs): ingest iGene disease list`
- `docs(lab): add Thermo Fisher Ion Torrent NGS platform`
- `fix(wiki): repair broken citations`
- `chore(lint): validate wiki index`
- `chore(git): initialize repository and workflow rules`

每次完成新來源 Ingest 後，建議建立獨立且具描述性的 Commit。

### 8.4 安全與著作權入庫紅線（`.gitignore` 防護）

- **禁止提交至 Git**：API Keys、密碼與 Token、患者個資、未去識別化臨床資料、敏感內部機密文件、未獲再散布授權或具非商業限制（NC）之第三方原始文獻全文（如 `raw/sources/SRC-001.md` 至 `SRC-008.md` 與 `*.pdf`），以及暫存／快取檔案（`.DS_Store`、`__pycache__`）。
- **明確保留於 Git**：`AGENTS.md`、`README.md`、`wiki/`、`raw/registry.json`、`raw/metadata/`、可合法保存之公司官方 `raw/sources/SRC-009.md` 與 `raw/structured/`、`logs/`（不可排除整個 `logs/` 目錄）、獲授權之 `assets/`、`workflows/` 與 `wiki_browser/`。
- **遠端 Repository 政策**：優先使用 **Private Repository**（目標名稱：`reproductive-lab-wiki`）；**未取得專案負責人明確確認前，不得自行建立公開 Repository 或公開 Push 醫學衛教內容**。

### 8.5 Ingest 與 Git 整合標準作業流程

每次新增或更新來源時依序執行：
1. 由 `main` 建立工作分支（`source/*`、`content/*` 或 `fix/*`）。
2. 保存原始來源、結構化資料與 `raw/metadata/`、`raw/registry.json`（並確認第三方受版權保護全文未被誤加入 Git）。
3. 整合更新相關 Wiki 頁面與交叉連結。
4. 更新 `wiki/index.md`、`logs/human_review_queue.md` 與 `wiki/log.md`。
5. 執行 `python3 workflows/build_browser_data.py` 與 `python3 workflows/lint_wiki.py`，確認 0 致命錯誤。
6. 檢視 `git status` 與 `git diff`，確認無敏感資料或受限全文外洩。
7. 建立符合 Conventional Commits 規範之描述性 Commit。
8. 保留高風險頁面之 `pending_clinical_review` / `pending_technical_verification` 狀態，待授權人員人工審核核准後方合併至正式分支。
