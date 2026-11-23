# Phase 2 Git Change Log — ECS Interactive Teaching HTML

- **Working Branch**: `content/ecs-teaching-slides`（branched cleanly from `main` @ `3ee0732`）
- **Date**: `2026-11-23`
- **Commit Message**: `feat(education): build interactive ECS teaching slides from wiki`
- **Merge / Push / Deploy Status**: **僅本機工作分支 Commit**（未 Merge 至 `main`、未 Push 至 GitHub、未啟用 GitHub Pages，等待人工審核批准）。

---

## 1. 新增檔案（Added Files — 9 個檔案）

- `presentations/ecs-teaching-slides/index.html`：11 頁暖橘色 16:9 互動教學 HTML 簡報（《ECS 是什麼？為什麼健康的父母也可能生下患有遺傳疾病的孩子？》）
- `presentations/ecs-teaching-slides/styles.css`：暖橘色醫學衛教樣式表（含桌面 16:9 與行動版響應式修正）
- `presentations/ecs-teaching-slides/app.js`：投影片導覽（含 `G` 鍵雙向目錄切換）、互動式 Punnett Square、X-linked 親代切換、iGene 350 項即時搜尋與 5 題互動測驗邏輯
- `presentations/ecs-teaching-slides/igene_data.js`：由 `workflows/build_ecs_slides_data.py` 自 `raw/structured/igene_disease_list.json` 自動編譯之 350 筆結構化疾病／基因資料
- `workflows/build_ecs_slides_data.py`：可重複執行之結構化資料編譯腳本（確保簡報與 Wiki 單一事實來源同步）
- `logs/phase2/retrieval_log.md`：Wiki-First 檢索紀錄（14 份檔案實時查詢紀錄與 4 項 Knowledge Gaps）
- `logs/phase2/ecs_outline_source_map.md`：11 頁教材大綱、Assets 選用策略與 Wiki／Source ID 對照表
- `logs/phase2/content_validation_log.md`：Slide 1–11 逐頁醫學主張驗證與審核狀態對照紀錄
- `logs/phase2/html_test_log.md`：桌面與行動版雙輪實機瀏覽器 QA 測試、3 項問題修正與重測座標證據
- `logs/phase2/git_change_log.md`：本變更紀錄檔

---

## 2. 修改檔案（Modified Files — 5 個檔案）

- `logs/human_review_queue.md`（+8 行）：新增第五節登錄 `presentations/ecs-teaching-slides/index.html` 待臨床與技術審核項目
- `wiki/log.md`（+9 行）：記錄 Phase 2 教學簡報檢索、建置、雙輪瀏覽器測試與待審狀態
- `logs/lint_report.md` / `logs/lint_report.json`：更新最新一次 Lint 執行時間與 `PASS (0 Errors / 0 Warnings)` 報告
- `wiki_browser/wiki_data.js`：由 `workflows/build_browser_data.py` 自動同步最新 `wiki/log.md`

---

## 3. 安全與品質驗證摘要

- `python3 workflows/lint_wiki.py`：**PASS（0 Errors / 0 Warnings）**
- `git diff --check`：**PASS（0 問題）**
- Secret / PII 掃描：**PASS（0 筆命中）**
- Real Browser QA（Round 1 → Fix → Round 2 Retest）：**ALL PASS**
