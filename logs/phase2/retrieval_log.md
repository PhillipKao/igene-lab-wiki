# Phase 2 Retrieval Log — ECS Interactive Teaching HTML

- **Task**: 製作 11 頁初學者導向互動式教學簡報《ECS 是什麼？為什麼健康的父母也可能生下患有遺傳疾病的孩子？》
- **Git Branch**: `content/ecs-teaching-slides`
- **Retrieval Timestamp (Local)**: `2026-11-23 19:33:25–19:33:37 +08:00`
- **Retrieval Strategy**: Wiki-First（先讀 `wiki/index.md` 定位所有 ECS 關聯頁面，再讀取整合頁面與 `raw/metadata/` 確認原始來源與結構化資料）

---

## 1. 實際檢索紀錄表

| 序號 | 查詢時間 (+08:00) | 查詢檔案路徑 | 查詢主題 | 使用之 Source IDs | 頁面目前審核狀態 |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | 2026-11-23 19:33:25 | `wiki/index.md` | 全站索引定位 ECS、遺傳概念、實驗室與 FAQ 頁面 | `SRC-001`–`SRC-009` | Index |
| 2 | 2026-11-23 19:33:26 | `wiki/products/ecs.md` | ECS 定義、iGene 產品範圍、適用對象、流程、結果解讀與限制 | `SRC-003`, `SRC-006`, `SRC-009` | `source_verified`, `product_spec_verified`, `pending_clinical_review`, `pending_technical_verification` |
| 3 | 2026-11-23 19:33:26 | `wiki/products/ecs-disease-gene-index.md` | 350 種疾病 / 351 獨立基因、15 大類、28 XL 基因、`AR/AD` 3 筆、檢出率限制 | `SRC-003`, `SRC-009` | `source_verified`, `product_spec_verified`, `pending_clinical_review`, `pending_technical_verification` |
| 4 | 2026-11-23 19:33:26 | `wiki/concepts/autosomal-recessive.md` | 體染色體隱性遺傳定義、無症狀帶因者、Aa × Aa 25%/50%/25% 機率 | `SRC-003`, `SRC-006`, `SRC-009` | `source_verified`, `product_spec_verified`, `pending_clinical_review` |
| 5 | 2026-11-23 19:33:26 | `wiki/concepts/x-linked-inheritance.md` | X-linked 遺傳特性、母親帶因傳遞機率、ACMG 16 vs. iGene 28 基因差異 | `SRC-003`–`SRC-006`, `SRC-009` | `source_verified`, `product_spec_verified`, `pending_clinical_review` |
| 6 | 2026-11-23 19:33:27 | `wiki/concepts/residual-risk.md` | Residual Risk 定義、計算公式、為何永不為零、官網檢出率解讀限制 | `SRC-003`, `SRC-009` | `source_verified`, `product_spec_verified`, `pending_clinical_review` |
| 7 | 2026-11-23 19:33:27 | `wiki/faq/ecs-faq.md` | 白話問答（350 疾病 ≠ 350 基因、夫妻檢測、NGS 限制、新生兒篩檢） | `SRC-003`, `SRC-006`, `SRC-009` | `source_verified`, `product_spec_verified`, `pending_clinical_review`, `pending_technical_verification` |
| 8 | 2026-11-23 19:33:27 | `wiki/laboratory/ngs-technology.md` | NGS 一般流程 vs. 已確認 Ion Torrent / ECS 530 晶片與待驗證規格邊界 | `SRC-003`, `SRC-004`, `SRC-005`, `SRC-007`, `SRC-009` | `source_verified`, `pending_technical_verification`, `pending_clinical_review` |
| 9 | 2026-11-23 19:33:27 | `raw/metadata/SRC-003.json` | 核對 ACMG 2021 DOI、URL、擷取日期與 SHA-256 | `SRC-003` | `ingested` |
| 10 | 2026-11-23 19:33:28 | `raw/metadata/SRC-009.json` | 核對 iGene 官方 URL、結構化 CSV/JSON SHA-256 與擷取日期 | `SRC-009` | `ingested` |
| 11 | 2026-11-23 19:33:36 | `wiki/concepts/monogenic-disease.md` | 單基因疾病與致病變異基本定義 | `SRC-003`–`SRC-006` | `auto_compiled` |
| 12 | 2026-11-23 19:33:36 | `wiki/concepts/genetic-counseling.md` | 檢前／檢後遺傳諮詢重點與自主選擇權 | `SRC-001`–`SRC-007` | `pending_clinical_review` |
| 13 | 2026-11-23 19:33:36 | `wiki/evidence/ecs-clinical-evidence.md` | ACMG 2021 Tier 1–4 分級架構與 iGene 跨來源對照 | `SRC-003`, `SRC-006`, `SRC-009` | `source_verified`, `product_spec_verified`, `pending_clinical_review`, `pending_technical_verification` |
| 14 | 2026-11-23 19:33:36 | `logs/asset_audit.md` | 檢視 8 張 BiOLOVE PNG 規格、用途與色票 | Assets Audit | Verified |

---

## 2. 檢索過程中發現之 Knowledge Gaps 與處置策略

| Gap 編號 | 缺少或未完全定案之知識 | 影響投影片 | 實務處置與補充建議 |
| :--- | :--- | :--- | :--- |
| **GAP-01** | Wiki 尚未建立獨立的零基礎「DNA／染色體／基因／變異」白話概念頁（目前分散於 `monogenic-disease.md` 與 `SRC-009` 產品介紹頁） | Slide 2 | 嚴格援引 `monogenic-disease.md`、`autosomal-recessive.md` 與 `SRC-009` 之基礎定義撰寫，不自行發明額外分子統計數字；建議後續於 `wiki/concepts/` 補建 `gene-and-variant-basics.md`（可參考 MedlinePlus Genetics 官方公開教材）。 |
| **GAP-02** | `wiki/concepts/x-linked-inheritance.md` 詳述母親帶因（`X*X × XY`）傳遞機率，但未另立「父親受影響（`XX × X*Y`）」之孟德爾傳遞小節 | Slide 4 | 簡報以母親帶因（ECS 主要篩檢對象）為主情境，並以簡潔孟德爾配對概念對照「父親帶致病 X 染色體」之性染色體傳遞機制，同時明確標示不同 X-linked 疾病之表現度差異不可一概而論；建議後續於 `x-linked-inheritance.md` 補充該對照段。 |
| **GAP-03** | 本實驗室 ECS 具體 Ion Torrent 機型、ECS Coverage、Read Length、各變異類型分析靈敏度／特異度、TAT 與認證狀態均為 `Pending Technical Verification` | Slide 6, Slide 7 | 嚴格區分「一般 NGS 檢測流程」與「本實驗室已確認項目（Thermo Fisher Scientific / Ion Torrent NGS、ECS `530` 晶片、iGene 官方 350 項清單）」，**絕不填入任何未確認數值**。 |
| **GAP-04** | 所有 ECS 相關 Wiki 頁面目前為 `pending_clinical_review`（全站 0 篇 `approved`） | Slide 1–11 | 依規範全份簡報標示為「衛教教學草稿｜待臨床審核」，不提供個人化醫療決策，並保留所有爭議／跨來源差異（如 *FMR1* 未收錄於 iGene 350 項 NGS 清單）供人工審核。 |
