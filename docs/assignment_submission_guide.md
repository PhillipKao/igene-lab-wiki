# 課程作業正式繳交指南 — Reproductive Genetics Persistent LLM Wiki & ECS 互動教學簡報

> **交付範圍說明**：本文件彙整本次作業所需之全部交付項目（A–F），並清楚區隔「完整專案 Repository（含 Persistent LLM Wiki 與開發紀錄）」與「GitHub Pages 課堂教學展示版（僅公開去識別、去未驗證規格、去未授權品牌圖檔之 11 頁 ECS 互動教材）」。

---

## A. LLM Wiki GitHub Repository 連結

- **Repository URL**：https://github.com/PhillipKao/igene-lab-wiki
- **主要架構**：採用 Andrej Karpathy Persistent LLM Wiki 模式（`raw/` 不可變證據 → `wiki/` 整合式跨頁知識庫 → `workflows/` 驗證與建置管線 → `logs/` 執行與人工審核紀錄）。

## B. ECS 教學 HTML 簡報公開網址（GitHub Pages 課堂教學展示版）

- **預計公開網址（採用 GitHub Actions 獨立部署 `publish/ecs-demo/`）**：
  https://phillipkao.github.io/igene-lab-wiki/
- **安全隔離說明**：透過 `.github/workflows/deploy-ecs-demo.yml` 僅將 `publish/ecs-demo/`（共 6 個靜態檔）打包發布至 GitHub Pages，**完全不公開**專案根目錄、`raw/`、`logs/`、`human_review_queue.md`、`wiki/`、`wiki_browser/`、內部技術規格或未授權品牌圖片。

## C. Workflow Graph 與 Reflection 文件連結

- **GitHub 檢視連結（原生渲染 Mermaid Graph）**：
  https://github.com/PhillipKao/igene-lab-wiki/blob/main/docs/phase2_workflow_reflection.md
- **自動化前置檢查腳本**：
  - Phase 2 簡報 Preflight：[`workflows/preflight_slides.py`](../workflows/preflight_slides.py)
  - 課堂公開版安全發布閘門：[`workflows/verify_demo_publish.py`](../workflows/verify_demo_publish.py)

## D. 9 篇來源的 Ingest 成果與來源清單（100% 真實擷取與 SHA-256 驗證）

所有來源均透過真實 HTTP/API 連線擷取並計算 SHA-256（詳見 `raw/registry.json` 與 `raw/metadata/`；第三方受版權／CC BY-NC 限制之原始全文依 `.gitignore` 僅保留於本機供雜湊驗證，不違法再散布）：

| Source ID | 機構與年份 | 文件標題 | 識別碼（DOI / PMC / URL） | 狀態 | 擷取字元數 |
| :--- | :--- | :--- | :--- | :---: | ---: |
| **SRC-001** | ASRM (2024) | The use of preimplantation genetic testing for aneuploidy: a committee opinion (2024) | DOI `10.1016/j.fertnstert.2024.04.013` / PMID `38762806` | `ingested` | 135,702 |
| **SRC-002** | ASRM (2023) | Clinical management of mosaic results from PGT-A of blastocysts: a committee opinion (2023) | DOI `10.1016/j.fertnstert.2023.08.969` / PMID `37678731` | `ingested` | 60,499 |
| **SRC-003** | ACMG (2021) | Screening for autosomal recessive and X-linked conditions during pregnancy and preconception: a practice resource | DOI `10.1038/s41436-021-01203-z` / [PMC8488021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8488021/) | `ingested` | 82,547 |
| **SRC-004** | ESHRE (2020) | Good practice recommendations for the detection of structural and numerical chromosomal aberrations | DOI `10.1093/hropen/hoaa017` / [PMC7257111](https://pmc.ncbi.nlm.nih.gov/articles/PMC7257111/) | `ingested` | 112,572 |
| **SRC-005** | ESHRE (2020) | Good practice recommendations for the detection of monogenic disorders | DOI `10.1093/hropen/hoaa018` / [PMC7257022](https://pmc.ncbi.nlm.nih.gov/articles/PMC7257022/) | `ingested` | 82,903 |
| **SRC-006** | ASRM (2023) | Indications and management of PGT-M: a committee opinion (2023) | DOI `10.1016/j.fertnstert.2023.03.003` / PMID `37162432` | `ingested` | 65,403 |
| **SRC-007** | ESHRE (2020) | Good practice recommendations for the organisation of PGT | DOI `10.1093/hropen/hoaa021` / [PMC7257038](https://pmc.ncbi.nlm.nih.gov/articles/PMC7257038/) | `ingested` | 67,314 |
| **SRC-008** | ESHRE (2020) | Good practice recommendations for polar body and embryo biopsy for PGT | DOI `10.1093/hropen/hoaa020` / [PMC7257009](https://pmc.ncbi.nlm.nih.gov/articles/PMC7257009/) | `ingested` | 59,894 |
| **SRC-009** | iGene 官方公開網站 (2026) | iGene 遺傳疾病帶因篩檢列表（350 種疾病、351 個唯一基因、15 大分類） | [icryobank.com/gene/igene-disease-list](https://www.icryobank.com/gene/igene-disease-list) | `ingested` | 4,250 + 350 rows |

- **Wiki 整合成果**：共建立 **34 頁**繁體中文知識頁（產品、核心概念、臨床證據、實驗室品質與 FAQ）、**602 條**內部交叉連結與 **266 處**來源引用，通過 `python3 workflows/lint_wiki.py`（**0 Errors / 0 Warnings**），並嚴格保留高風險頁面之 `pending_clinical_review` / `pending_technical_verification` 狀態（0 頁擅自改為 `approved`）。

## E. 實際執行與修正紀錄摘要

1. **Phase 1 — 來源擷取與 Lint 除錯**：
   - 解決 macOS Python SSL 憑證問題（改用系統 `curl` 擷取）；`SRC-005` 遇 OUP HTTP 403 改以官方 NCBI PMC E-utilities 取得 Open Access JATS XML；修正 `SRC-007` PMID 對應錯誤（`32524036`）。
   - 修復 16 項 Frontmatter `source_ids` 遺漏警告，使全站 Lint 達 `0 Errors / 0 Warnings`。
   - 解析 `SRC-009` 實證發現「350 種疾病對應 **351 個獨立基因**（含雙基因 `HBA1/HBA2`）」，並揭露 ACMG 建議之 *FMR1* 未收錄於目標區間 NGS 清單之重要差異。
2. **Phase 2 — 互動教材實測、修復與 Workflow 改進**：
   - 第一輪實機瀏覽器測試（桌面 `1280×800` + 行動 `390×844`）抓出 3 項真實缺陷：① 行動版 Slide 7 頁首溢位裁切（`right = 401.7px > 390px`）；② 行動版底部固定控制列安全間距偏緊；③ 目錄總覽開啟時按 `G` 鍵無法關閉。
   - 修復後第二輪實機重測 100% 通過（頁首 `right = 364.5px ≤ 390px`、底部保留 `65.54px` 安全間距、`G` 鍵雙向正常切換）。
   - 將 3 項缺陷抽象為自動化前置閘門 `workflows/preflight_slides.py`（Layout Preflight + JavaScriptCore Keyboard Preflight，**7/7 PASS**），並以合成 Round-1 還原驗證證明可於進入瀏覽器 QA 前攔截全部 3 項歷史錯誤。
3. **部署階段 — 課堂教學展示版安全隔離**：
   - 建立獨立發布目錄 `publish/ecs-demo/`（6 個檔案），以原創中性 DNA SVG 取代未確認公開授權之 BiOLOVE 圖檔、移除個別產品檢出率與未驗證實驗室規格（Coverage/TAT/晶片/儀器型號/認證）、將未公開 Wiki Browser 連結替換為公開文獻連結，並加上全頁「課程教學示範，非個人化醫療建議」標示與自動化發布前掃描閘門 `workflows/verify_demo_publish.py`（**8/8 PASS**）。

## F. 課堂繳交用繁體中文說明文字（可直接複製提交）

> **作業題目：基於 Persistent LLM Wiki 架構之生殖遺傳知識庫與 ECS 互動式衛教簡報**
>
> 本專案採用 Andrej Karpathy 的 Persistent LLM Wiki 架構，從 9 篇真實擷取且經 SHA-256 雜湊驗證之國際臨床指引與公開資料來源（ASRM、ACMG 2021、ESHRE 2020 與公開 350 項 ECS 疾病清單）出發，建置包含 34 篇跨頁連結知識頁與自動化 Lint 驗證機制的生殖遺傳知識庫，並以「Wiki-first（先檢索知識庫、逐項追溯文獻、嚴格遵守醫學正確性護欄）」流程開發 11 頁互動式初學者衛教簡報《ECS 是什麼？為什麼健康的父母也可能生下患有遺傳疾病的孩子？》。
>
> 簡報內建常染色體隱性遺傳互動 Punnett Square、X-linked 親代傳遞圖解切換、350 項公開疾病／基因即時檢索（含 `HBA1/HBA2` 雙基因差異與 *FMR1* 未收錄揭露）及 5 題觀念測驗。在開發與驗證過程中，第一輪實機瀏覽器測試於行動裝置 `390×844` 與鍵盤互動階段揭露 3 項缺陷（頁首裁切、底部間距不足與 `G` 鍵無法雙向關閉目錄）；除完成修復與第二輪實測驗證外，我們更進一步實作 `Layout Preflight` 與 `Keyboard Interaction Preflight` 兩道自動化前置檢查，將原本需進瀏覽器才發現的錯誤提前於本機毫秒級攔截。
>
> 考量醫療衛教之嚴謹性與圖片著作權合規，本次 GitHub Pages 採 GitHub Actions 獨立部署「課堂教學展示版（`publish/ecs-demo/`）」，僅公開一般性遺傳衛教、公開文獻來源連結與原創中性 SVG 圖形，完整隔離尚未完成臨床審核之知識頁、內部實驗室參數、未驗證產品性能數值與品牌商標圖檔，並於各頁明確標註「課程教學示範，非個人化醫療建議」。
>
> - **GitHub Repository**：https://github.com/PhillipKao/igene-lab-wiki
> - **ECS 互動教學簡報（課堂展示版）**：https://phillipkao.github.io/igene-lab-wiki/
> - **Workflow Graph 與 Reflection 報告**：https://github.com/PhillipKao/igene-lab-wiki/blob/main/docs/phase2_workflow_reflection.md
