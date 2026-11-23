# Human Clinical & Laboratory Review Queue（分層人工審核、技術驗證與佐證文件需求清單）

- **更新日期**：2026-11-23（Laboratory Technical Verification 補充更新：新增 Thermo Fisher Scientific / Ion Torrent NGS 技術、PGT-A 覆蓋深度常規 `0.005×`／最高 `0.02×`、分產品規格獨立管理與正式佐證文件對應清單）
- **依據規則**：`AGENTS.md` 第 6 節（多層級審核與技術驗證標準）
- **審核分層定義**：
  - `source_verified`：原始文獻或公司官方網頁來源已完成真實擷取與 SHA-256 驗證。
  - `product_spec_verified`：頁面所列產品名稱、官方疾病清單與公開檢驗限制已有官方來源支持。
  - `pending_clinical_review`：臨床適應症、風險溝通與跨指引差異仍待臨床醫師／遺傳諮詢師審核。
  - `pending_technical_verification`：技術規格與性能指標仍待實驗室主管提供正式文件確認（**嚴禁以原廠一般性能代替本實驗室實際驗證結果**）。
  - `approved`：臨床與技術內容均經授權人員完整審核簽核（**目前全站 0 篇升為 `approved`；不得因部分技術資訊確認即自動將 `pending_clinical_review` 改為 `approved`**）。

---

## 一、待正式技術文件佐證之項目清單（Pending Technical Verification — 依所需文件分類）

以下所有尚未確認之規格項目，在未取得對應正式佐證文件前，**全站維持 `Pending Technical Verification` 且不得填入推論數值**：

| 待確認項目 | 適用產品範圍 | 所需正式佐證文件類型 | 備註／禁止事項 |
| :--- | :--- | :--- | :--- |
| **各產品是否共用同一平台、機型、晶片、流程與分析方法** | PGT-A、ECS、PGT-SR、PGT-M | **實驗室 SOP**、設備清冊 | 不可假定四項產品共用相同定序儀、晶片或生資流程 |
| **具體 Ion Torrent 儀器型號與 Read Length（另 PGT-SR / PGT-M 晶片待確認）** | PGT-A、ECS、PGT-SR、PGT-M | **實驗室 SOP**、儀器維護／設備清冊 | **已確認 Chip Type：PGT-A 為 `520`、ECS 為 `530`**（仍建議附 SOP 備查）；不可自行推定具體 Ion Torrent 機型或 PGT-SR / PGT-M 晶片 |
| **PGT-A 覆蓋深度正式文件佐證（已口頭／文字確認常規 `0.005×`、最高 `0.02×`）** | PGT-A | **Validation Report**、**實驗室 SOP** | 已登錄確認數值，仍建議補附正式驗證報告與 SOP 版本號 |
| **ECS、PGT-SR、PGT-M 各自定序 Coverage** | ECS、PGT-SR、PGT-M | **Validation Report**、**實驗室 SOP** | 尚未提供，禁止自 PGT-A 或原廠規格推論 |
| **CNV / Aneuploidy 最小偵測解析度（Mb）** | PGT-A、PGT-SR | **Validation Report**、**正式檢驗報告範本** | 不可引用 Thermo Fisher 原廠性能或 ESHRE 一般範圍取代實測值 |
| **Mosaic / Low-VAF Variant Detection Limit（與揭露政策）** | PGT-A、ECS | **Validation Report**、**臨床報告 SOP** | 需涵蓋鑲嵌比例切點與是否 masking 之院所政策 |
| **各變異類型之 Analytical Sensitivity / Specificity** | PGT-A、ECS、PGT-SR、PGT-M | **Validation Report** | 官網 iGene「檢出率」（76%–99%）不可等同所有變異類型之統一分析敏感度 |
| **PGT-SR 最小偵測片段大小及平衡帶因區分能力** | PGT-SR | **Validation Report**、**實驗室 SOP** | 需明確註記是否支援單倍型分析區分正常與平衡帶因 |
| **PGT-A / PGT-SR / PGT-M / ECS 各自標準報告週期（TAT）** | PGT-A、ECS、PGT-SR、PGT-M | **正式檢驗報告範本**、**服務規範／SOP** | 含 PGT-M 事前客製化建置（Preclinical Work-up）時程 |
| **實驗室有效認證或核准狀態（ISO 15189、LDTs、CAP 等）** | 全實驗室 | **有效認證證書／主管機關核准公文** | 未附有效證明前不得宣稱已取得任何認證或核准 |

---

## 二、已整合 `SRC-009` 與 Ion Torrent NGS 分產品技術邊界之頁面（共 13 篇，維持待審核）

| 頁面 | 目前審核分層 | 本次已確認納入內容 | 仍待審核／待補正式文件項目 |
| :--- | :--- | :--- | :--- |
| `wiki/laboratory/ngs-technology.md` | `source_verified`, `pending_technical_verification`, `pending_clinical_review` | Thermo Fisher Scientific / Ion Torrent NGS 技術、**Chip Type（PGT-A `520`、ECS `530`）**、PGT-A Coverage（常規 `0.005×`／最高 `0.02×`）、四大產品獨立規格表 | 上述第一節全部 Pending 技術參數之 Validation Report / SOP / 認證文件 |
| `wiki/laboratory/laboratory-overview.md` | `source_verified`, `product_spec_verified`, `pending_clinical_review`, `pending_technical_verification` | Ion Torrent NGS 技術、**Chip Type（PGT-A `520`、ECS `530`）**、PGT-A Coverage、iGene 350 項產品資訊、禁止跨產品推論原則 | 有效認證證書（ISO 15189 / LDTs / CAP）、各產品 SOP 平台對應與品牌授權 |
| `wiki/products/pgt-a.md` | `source_verified`, `pending_clinical_review`, `pending_technical_verification` | Ion Torrent NGS 技術；**Chip Type `520`**；PGT-A 常規 `0.005×`、最高 `0.02×` coverage | Validation Report（解析度、Mosaic 門檻、敏感度／特異度）、正式檢驗報告（TAT）與臨床口徑審核 |
| `wiki/products/ecs.md` | `source_verified`, `product_spec_verified`, `pending_clinical_review`, `pending_technical_verification` | `SRC-009` iGene（350 疾病／15 大類／351 基因含 28 XL）、Ion Torrent 技術與 **Chip Type `530`**（不假定與他項共用流程） | ECS 專屬 SOP／Validation Report（Coverage、Low-VAF、分析敏感度／特異度）、TAT 與臨床口徑審核 |
| `wiki/products/ecs-disease-gene-index.md` | `source_verified`, `product_spec_verified`, `pending_clinical_review`, `pending_technical_verification` | 完整 350 筆結構化統計、`HBA1/HBA2`、`AR/AD` 3 筆、28 XL 基因清單 | 審核不含 *FMR1* 跨來源說明、`AR/AD` 諮詢建議與檢出率限制免責語句 |
| `wiki/products/pgt-sr.md` | `source_verified`, `pending_clinical_review`, `pending_technical_verification` | 獨立技術邊界聲明（不假定共用 PGT-A 儀器／晶片／Coverage／演算法） | PGT-SR 專屬 SOP、Validation Report（最小偵測片段與平衡帶因區分能力）與 TAT |
| `wiki/products/pgt-m.md` | `source_verified`, `pending_clinical_review`, `pending_technical_verification` | 獨立技術邊界聲明（不假定與其他產品共用平台／流程） | PGT-M 專屬 SOP、Validation Report（ADO 控管與敏感度／特異度）、事前開發與報告 TAT 及 ASRM 不建議項目審核 |
| `wiki/evidence/ecs-clinical-evidence.md` | `source_verified`, `product_spec_verified`, `pending_clinical_review`, `pending_technical_verification` | ACMG 2021 vs. iGene 350 項（含 *FMR1* 差異與檢出率 76%–99%）對照 | 審核跨來源差異表述與在地補充文獻需求 |
| `wiki/concepts/autosomal-recessive.md` | `source_verified`, `product_spec_verified`, `pending_clinical_review` | `SRC-009` 319 筆 `AR` 與 3 筆 `AR/AD` 統計與常見項目 | 審核 `AR/AD` 項目表述與風險溝通準確性 |
| `wiki/concepts/x-linked-inheritance.md` | `source_verified`, `product_spec_verified`, `pending_clinical_review` | `SRC-009` 28 個 XL 基因 vs. ACMG 16 基因（不含 *FMR1*）對照 | 審核 X 性聯跨來源差異與 *FMR1* 加選諮詢表述 |
| `wiki/concepts/residual-risk.md` | `source_verified`, `product_spec_verified`, `pending_clinical_review` | `SRC-009` 檢出率（76%–99%）限制、雙族群與 3 筆帶因率 `-` 說明 | 審核殘餘風險與官網檢出率免責用語 |
| `wiki/faq/ecs-faq.md` | `source_verified`, `product_spec_verified`, `pending_clinical_review`, `pending_technical_verification` | Ion Torrent NGS 技術、350 疾病 ≠ 350 基因、不假定跨產品共用流程、新生兒篩檢提醒 | 審核患者衛教語氣與實驗室待確認規格表述 |
| `wiki/faq/faq-ecs-negative-risk.md` | `source_verified`, `product_spec_verified`, `pending_clinical_review` | `SRC-009` 目標區間 NGS 限制與出生後仍建議新生兒篩檢 | 審核白話精準度 |

---

## 三、其餘尚待臨床與實驗室審核頁面（共 14 篇，維持待審狀態）

| 頁面 | 目前審核分層 | 具體待審核／待補佐證文件項目 |
| :--- | :--- | :--- |
| `wiki/laboratory/pgt-workflow.md` | `source_verified`, `pending_clinical_review`, `pending_technical_verification` | 核對一般性七階段流程與本實驗室實際 SOP 與報告時程 |
| `wiki/laboratory/quality-management.md` | `source_verified`, `pending_clinical_review`, `pending_technical_verification` | 補充有效認證證書（ISO 15189 / LDTs / CAP）、EQA 計畫與內部 KPI |
| `wiki/laboratory/sample-traceability.md` | `source_verified`, `pending_clinical_review`, `pending_technical_verification` | 補充本實驗室條碼／電子見證 SOP 與 Transport PGT 溫控運送規範 |
| `wiki/evidence/pgt-a-clinical-evidence.md` | `source_verified`, `pending_clinical_review` | 審核高齡、反覆流產、累積活產結局與 ICSI 爭議表述 |
| `wiki/evidence/mosaic-embryo-evidence.md` | `source_verified`, `pending_clinical_review` | 審核 MET 胎兒確認異常率（`< 1%`）、CPM/UPD 與產前追蹤建議 |
| `wiki/evidence/pgt-m-sr-evidence.md` | `source_verified`, `pending_clinical_review` | 審核 ASRM 2023 與 ESHRE 2020 適應症邊界與技術限制對照 |
| `wiki/concepts/mosaicism.md` | `source_verified`, `pending_clinical_review` | 審核 TE/ICM 差異與非單一門檻原則說明 |
| `wiki/concepts/embryo-biopsy.md` | `source_verified`, `pending_clinical_review` | 審核 TE 切片操作、無結果率（`< 5%`）與再冷凍風險敘述 |
| `wiki/concepts/genetic-counseling.md` | `source_verified`, `pending_clinical_review` | 審核檢前／檢後諮詢重點與院所轉介路徑 |
| `wiki/faq/faq-pgt-a-vs-pgt-sr-vs-pgt-m.md` | `source_verified`, `pending_clinical_review` | 審核三種 PGT 比喻與限制溝通 |
| `wiki/faq/faq-pgt-a-guarantee-pregnancy.md` | `source_verified`, `pending_clinical_review` | 審核 PGT-A 效益預期管理用語 |
| `wiki/faq/faq-mosaic-embryo-transfer.md` | `source_verified`, `pending_clinical_review` | 審核 Mosaic 胚胎植入決策語氣與諮詢提醒 |
| `wiki/faq/faq-embryo-biopsy-safety.md` | `source_verified`, `pending_clinical_review` | 審核切片安全性與冷凍必要性白話說明 |
| `wiki/faq/faq-prenatal-testing-after-pgt.md` | `source_verified`, `pending_clinical_review` | 審核與本地產檢／產前診斷銜接說明 |

---

## 四、純基礎概念頁（`auto_compiled`，共 7 篇）

- `wiki/concepts/aneuploidy.md`
- `wiki/concepts/euploidy.md`
- `wiki/concepts/copy-number-variation.md`
- `wiki/concepts/structural-chromosomal-rearrangement.md`
- `wiki/concepts/monogenic-disease.md`
- `wiki/concepts/haplotyping.md`
- `wiki/concepts/allele-dropout.md`

---

## 五、Phase 2 衍生互動教學 HTML 簡報待審項目

| 產出路徑 | 目前審核分層 | 依據之 Wiki 與來源 | 具體待審核項目 |
| :--- | :--- | :--- | :--- |
| `presentations/ecs-teaching-slides/index.html` | `source_verified`, `product_spec_verified`, `pending_clinical_review`, `pending_technical_verification` | `wiki/products/ecs.md`、`ecs-disease-gene-index.md`、`concepts/monogenic-disease.md`、`autosomal-recessive.md`、`x-linked-inheritance.md`、`residual-risk.md`、`genetic-counseling.md`、`evidence/ecs-clinical-evidence.md`、`laboratory/ngs-technology.md`、`faq/ecs-faq.md`（`SRC-003`, `SRC-006`, `SRC-009`） | 1. 覆核 11 頁初學者衛教口徑、Aa × Aa 互動棋盤說明、X-linked 親代對照（含 `GAP-02` 父親傳遞補充）與 5 題測驗解析。<br>2. 確認 *FMR1* 未收錄於 iGene 350 項清單之衛教提醒表述。<br>3. 待實驗室補齊正式 ECS Coverage、分析靈敏度／特異度、TAT 與有效認證文件後，由授權醫師／實驗室主管核准方可合併至 `main` 或對外發布。 |
