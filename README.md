# Reproductive Genetics & Laboratory Wiki

以 **Andrej Karpathy — LLM Wiki** 概念打造的持久化生殖遺傳檢測與實驗室衛教知識庫（Phase 1）。

## 專案架構

- `AGENTS.md`：Agent 操作契約、Ingest SOP、醫學正確性護欄與審查規則。
- `assets/`：品牌視覺素材（BiOLOVE 愛生育生物科技）。
- `raw/`：不可變原始文獻摘錄、詮釋資料與 SHA-256 驗證紀錄（`SRC-001` 至 `SRC-008`）。
- `wiki/`：整合式 Markdown 知識庫，涵蓋 `products/`、`concepts/`、`evidence/`、`laboratory/`、`faq/`，以及全站索引 `wiki/index.md` 與演進日誌 `wiki/log.md`。
- `workflows/`：可重複執行的 Python 工具（來源擷取、品質 Lint、Wiki Browser 資料建置）。
- `logs/`：Asset Audit、Ingest 報告、Lint 報告與人工臨床待審清單。
- `wiki_browser/`：暖橘色醫學衛教風格之本機 Wiki 瀏覽介面（非教學投影片）。

## 核心檢測產品

1. **PGT-A**：胚胎著床前染色體非整倍體篩檢
2. **ECS**：擴展性帶因者篩檢（Expanded Carrier Screening）
3. **PGT-SR**：胚胎著床前染色體結構重排檢測
4. **PGT-M**：胚胎著床前單基因遺傳疾病檢測

## 本機操作與瀏覽

### 1. 執行品質檢查（Lint）

```bash
python3 workflows/lint_wiki.py
```

### 2. 更新 Wiki Browser 資料並啟動本機預覽

```bash
python3 workflows/build_browser_data.py
python3 -m http.server 8765
```

接著在瀏覽器開啟 `http://localhost:8765/wiki_browser/`（或直接開啟 `wiki_browser/index.html`）即可瀏覽完整 Wiki。

## 醫學免責與審核狀態

本知識庫依據 ASRM、ESHRE、ACMG 等國際臨床指引與技術建議整理而成。凡涉及臨床決策建議、產品效益、技術限制與實驗室實務規格之內容皆標示為 `pending_clinical_review`，詳見 `logs/human_review_queue.md`，請經生殖醫學／遺傳諮詢專業人員覆核後方可作為正式臨床衛教發布。
