# Persistent Wiki Log — 編修與 Ingest 演進紀錄

本紀錄追蹤 **Reproductive Genetics & Laboratory Wiki** 每次原始文獻 Ingest、跨頁知識整合、差異衝突盤點、Lint 驗證與審核狀態變動，供 Phase 2 稽核與工作流回顧使用。

---

## [2026-11-23] Phase 1 初始建置與第一批 8 篇核心指引 Ingest

### 1. Project & Asset Audit
- 盤點初始 Workspace：僅含 `assets/biolove-1.png` 至 `biolove-8.png` 共 8 張 BiOLOVE（愛生育生物科技）透明 PNG 品牌識別圖檔（非醫學流程圖），無既有 `AGENTS.md`、`wiki/` 或工具腳本。
- 由原圖萃取精確品牌色票 `#EB5F2A` 與 `#717071` / `#6D6D70`，結合 Warm Orange Medical Education 規範建立視覺指引，完整紀錄寫入 `logs/asset_audit.md`。
- 建立 `AGENTS.md` 與 `README.md` 作為專案操作契約。

### 2. Raw Sources Ingest（8 / 8 篇成功全文擷取）
透過 `workflows/ingest_sources.py` 執行正式擷取與 NCBI PubMed/PMC E-utilities 書目核對：
- `SRC-001`（ASRM 2024 PGT-A）：`ingested`，135,702 字元，DOI `10.1016/j.fertnstert.2024.04.013`，SHA-256 `9aed4f31f595...`
- `SRC-002`（ASRM 2023 Mosaicism）：`ingested`，60,499 字元，DOI `10.1016/j.fertnstert.2023.08.969`，SHA-256 `1919d91f50ee...`
- `SRC-003`（ACMG 2021 ECS）：`ingested`，82,547 字元，DOI `10.1038/s41436-021-01203-z`，SHA-256 `fe2db196d3b2...`
- `SRC-004`（ESHRE 2020 PGT-A / PGT-SR）：`ingested`，112,572 字元，DOI `10.1093/hropen/hoaa017`，SHA-256 `2d97ad74b549...`
- `SRC-005`（ESHRE 2020 PGT-M）：`ingested`，82,903 字元，DOI `10.1093/hropen/hoaa018`，SHA-256 `de3d4b9bd313...`（註：原 OUP URL 回傳 HTTP 403，改透過官方 NCBI PMC Open Access `PMC7257022` JATS XML 擷取完整全文並如實記錄）
- `SRC-006`（ASRM 2023 PGT-M）：`ingested`，65,403 字元，DOI `10.1016/j.fertnstert.2023.03.003`，SHA-256 `977b6051334b...`
- `SRC-007`（ESHRE 2020 Organisation of PGT）：`ingested`，67,314 字元，DOI `10.1093/hropen/hoaa021`，SHA-256 `81e9ca54f25b...`（註：初跑時曾偵測到 PMID 對應錯置為 `hoaa016`，經跨檔比對修正為正確 PMID `32524036` 後重新驗證通過）
- `SRC-008`（ESHRE 2020 Embryo Biopsy）：`ingested`，59,894 字元，DOI `10.1093/hropen/hoaa020`，SHA-256 `20e2b43de709...`

### 3. Wiki 多頁整合與交叉連結建立
共新建 **31 篇**知識頁並更新 `wiki/index.md`：
- **新增 Products（4 篇）**：`pgt-a.md`、`ecs.md`、`pgt-sr.md`、`pgt-m.md`
- **新增 Concepts（13 篇）**：`aneuploidy.md`、`euploidy.md`、`mosaicism.md`、`copy-number-variation.md`、`structural-chromosomal-rearrangement.md`、`monogenic-disease.md`、`autosomal-recessive.md`、`x-linked-inheritance.md`、`residual-risk.md`、`embryo-biopsy.md`、`haplotyping.md`、`allele-dropout.md`、`genetic-counseling.md`
- **新增 Evidence（4 篇跨指引整合頁）**：`pgt-a-clinical-evidence.md`、`mosaic-embryo-evidence.md`、`ecs-clinical-evidence.md`、`pgt-m-sr-evidence.md`
- **新增 Laboratory（4 篇）**：`laboratory-overview.md`、`pgt-workflow.md`、`quality-management.md`、`sample-traceability.md`
- **新增 FAQ（6 篇）**：`faq-pgt-a-vs-pgt-sr-vs-pgt-m.md`、`faq-pgt-a-guarantee-pregnancy.md`、`faq-mosaic-embryo-transfer.md`、`faq-ecs-negative-risk.md`、`faq-embryo-biopsy-safety.md`、`faq-prenatal-testing-after-pgt.md`

### 4. 辨識之跨文獻差異與臨床爭議（已保留於 Evidence 頁）
1. **PGT-A 臨床效益爭議**：早期單中心研究於預後良好族群觀察到初次植入活產優勢，但近年多中心 RCT 顯示冷凍週期整體累積懷孕結局與傳統 IVF 相近；高齡與反覆性流產仍待更嚴謹 ITT RCT 驗證（見 `wiki/evidence/pgt-a-clinical-evidence.md`）。
2. **非男性因素 PGT-A 是否強制 ICSI**：ASRM 2024 認為目前證據不足以支持單純 PGT-A 強制使用 ICSI，但部分實驗室與 PGT-M 流程仍基於防污染實務偏好使用 ICSI。
3. **Mosaic 結果之報告與排序無單一標準**：不同實驗室門檻與是否 masking 差異甚大，且 ASRM 2023 明確指出尚無全球通用之實證模型能精準預測產前／產後個別風險。

### 5. 待人工審核清單（Human Review Queue）
- 共 **21 篇**頁面因涉及臨床適應症、產品效益／限制、患者決策衛教、跨指引爭議或實驗室實務規格，已標示為 `pending_clinical_review` 並登錄於 `logs/human_review_queue.md`。
- 其餘 **10 篇**純基礎遺傳學與分子原理概念頁標示為 `auto_compiled`，仍建議定期檢視。

---

## [2026-11-23] 增量更新：Ingest `SRC-009`（iGene 官方產品與疾病清單）及 Thermo Fisher Scientific NGS 平台規格補充

### 1. 新增官方來源 `SRC-009` 與結構化資料建立
- 透過 `workflows/ingest_src009.py` 真實擷取公司官方網站兩頁：
  - 疾病列表：`https://www.icryobank.com/gene/igene-disease-list`（HTTP 200，368,250 bytes）
  - 產品介紹：`https://www.icryobank.com/gene/igene`（HTTP 200，40,640 bytes）
- 保留 `SRC-001` 至 `SRC-008` 不可變檔案未異動，新增 `raw/sources/SRC-009.md`、`raw/metadata/SRC-009.json`、`raw/structured/igene_disease_list.csv` 與 `raw/structured/igene_disease_list.json`（均含 SHA-256 雜湊驗證並登錄至 `raw/registry.json`）。
- **結構化統計核對結果**：
  - 官網宣稱：350 種遺傳疾病、15 大類、28 個性聯遺傳疾病基因。
  - 實際完整擷取：**350 筆疾病條目**、**15 大主分類（含 10 次分類）**、**28 筆 XL 項目（28 個獨立 XL 基因）**（與官網標示一致）。
  - **重要基因數差異**：表格原始基因字串去重為 350（無單一基因對應多筆疾病），但第 239 筆甲型地中海型貧血為雙基因欄位 `HBA1/HBA2`，故**去重後獨立 Gene Symbol 總數為 351 個**（明確區分疾病數與基因數）。
  - 遺傳模式分布：`AR` 319 筆、`XL` 28 筆、`AR/AD` 3 筆（`RTEL1`、`COL7A1`、`GH1`）；雙族群列 60 筆；帶因率 `-` 共 3 筆；檢出率範圍 76%–99%。

### 2. 更新前後差異摘要（Before → After）
- **治理與 Lint 規則**：`AGENTS.md` 與 `workflows/lint_wiki.py` 由單一 `review_status` 向下相容擴充至五層審核架構（`source_verified`、`product_spec_verified`、`pending_clinical_review`、`pending_technical_verification`、`approved`），並新增結構化 CSV/JSON SHA-256 驗證。
- **Wiki 頁面總數**：由 **31 篇 → 34 篇**（新建 `laboratory/ngs-technology.md`、`products/ecs-disease-gene-index.md`、`faq/ecs-faq.md`）。
- **跨頁整合更新（8 篇既有頁）**：
  - `products/ecs.md`：由純 ACMG 一般性 ECS 頁 → 整合 iGene 產品規格（350 項疾病／351 基因）、Thermo Fisher NGS 廠牌與結構化清單索引。
  - `products/pgt-a.md`、`laboratory/laboratory-overview.md`：新增實驗室主管確認之 **Thermo Fisher Scientific NGS 定序平台**廠牌資訊，並將未提供之 9 項技術規格明確鎖定為 `Pending Technical Verification`。
  - `concepts/autosomal-recessive.md`、`concepts/x-linked-inheritance.md`、`concepts/residual-risk.md`：原為 `auto_compiled` 基礎頁 → 整合 `SRC-009` 實測資料與跨來源差異（如 iGene 28 XL 基因不含 *FMR1* vs. ACMG 16 XL 基因含 *FMR1*），升級納管至 `pending_clinical_review`。
  - `evidence/ecs-clinical-evidence.md`、`faq/faq-ecs-negative-risk.md`：補入 `SRC-009` 跨來源比對與官方檢驗限制（含出生後仍建議新生兒篩檢）。
- **待人工審核頁面數**：由 21 篇增至 **27 篇**（新增 3 篇新頁 + 3 篇納入 `SRC-009` 產品比較之概念頁），尚無頁面升為 `approved`，詳見 `logs/human_review_queue.md`。
- **Wiki Browser 升級**：`workflows/build_browser_data.py` 自動將 `raw/structured/igene_disease_list.json` 編譯進 `wiki_browser/wiki_data.js`，`wiki_browser/app.js` 新增 iGene 350 項疾病／基因即時搜尋與多條件篩選介面（支援疾病名稱、基因名稱、15 大分類與遺傳模式篩選）。

---

## [2026-11-23] Laboratory Technical Verification 更新：Ion Torrent NGS 技術、PGT-A Coverage 與分產品技術規格獨立管理

### 1. 本次已確認之實驗室技術資訊
- 確認本實驗室使用 **Thermo Fisher Scientific / Ion Torrent NGS** 定序技術（不推定具體設備型號或晶片型號，不以原廠性能取代本實驗室實測驗證報告）。
- 確認 **PGT-A 覆蓋深度（Coverage）常規為 `0.005×`，最高為 `0.02×`**（僅登錄於 PGT-A，不推論至 ECS、PGT-SR 或 PGT-M）。
- 確立 **PGT-A、ECS、PGT-SR、PGT-M 技術規格完全分開管理**原則，不假定四項產品共用相同定序儀、晶片、實驗流程或分析方法。

### 2. 更新頁面與佐證文件追蹤
- 更新 `wiki/laboratory/ngs-technology.md` 與 `wiki/laboratory/laboratory-overview.md`：改採四大產品獨立技術規格管理表。
- 更新 `wiki/products/pgt-a.md`、`wiki/products/ecs.md`、`wiki/products/pgt-sr.md`、`wiki/products/pgt-m.md`、`wiki/faq/ecs-faq.md` 與 `wiki/index.md`：補入 Ion Torrent 技術、PGT-A 覆蓋深度與各產品獨立之 `Pending Technical Verification` 邊界；全站維持 **0 篇 `approved`**（不因部分技術確認即自動改為核准）。
- 更新 `logs/human_review_queue.md`：明確列出各項待確認規格所需之正式佐證文件（正式檢驗報告、Validation Report、實驗室 SOP、有效認證證書）。

---

## [2026-11-23] Laboratory Technical Verification 補充：定序晶片（Chip Type）確認

- 確認定序晶片規格：**PGT-A 使用 `520`（Ion 520）晶片**、**ECS（iGene）使用 `530`（Ion 530）晶片**（未推定具體 Ion Torrent 儀器型號，亦未推論 PGT-SR / PGT-M 晶片或 ECS Coverage）。
- 同步更新：`wiki/laboratory/ngs-technology.md`、`wiki/laboratory/laboratory-overview.md`、`wiki/products/pgt-a.md`、`wiki/products/ecs.md`、`wiki/faq/ecs-faq.md`、`logs/human_review_queue.md` 與 `wiki_browser/wiki_data.js`；全站維持 **0 篇 `approved`**。

---

## [2026-11-23] Git Workflow 基礎設定與 Initial Commit 準備

- 初始化本機 Git Repository（主分支：`main`），建立 `.gitignore` 並於 `AGENTS.md` 增訂第 8 節 Git Workflow 規範（分支策略、Conventional Commits、待審頁面管控與資安／著作權防護）。
- 安全與著作權檢查通過：無 API Keys、密碼或患者個資；第三方受版權或 CC BY-NC 4.0 限制之全文檔（`raw/sources/SRC-001.md` 至 `SRC-008.md`）保留於本機供 SHA-256 驗證但不納入 Git 追蹤，其餘 `raw/registry.json`、`raw/metadata/`、`raw/sources/SRC-009.md`、`raw/structured/`、`wiki/`、`logs/`、`assets/`、`workflows/` 與 `wiki_browser/` 均納入版控。
