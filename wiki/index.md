# Reproductive Genetics & Laboratory Wiki — 全站知識索引

![BiOLOVE 愛生育生物科技 — 明天的幸福・愛生育](../assets/biolove-8.png)
*圖說：Reproductive Genetics & Laboratory Wiki 品牌識別橫幅（來源：`assets/biolove-8.png`）。*

本知識庫採用 **Andrej Karpathy — Persistent LLM Wiki** 架構（`Raw Sources → Persistent Wiki → Knowledge Query`），系統化整合 ASRM、ESHRE、ACMG 國際生殖遺傳指引及公司官方產品資料（`SRC-009` iGene），提供一般民眾與患者（Patient）、醫療專業人員（Physician）及實驗室人員（Laboratory）一致且可追溯原始出處的繁體中文衛教與專業知識。

- **最後更新**：2026-11-23（新增 `SRC-009` iGene 350 項疾病／351 個基因結構化清單與 Thermo Fisher Scientific NGS 平台說明）
- **知識頁總數**：34 篇（Products 5 / Concepts 13 / Evidence 4 / Laboratory 5 / FAQ 7）
- **已驗證原始文獻與官方來源**：9 / 9 篇全文 Ingest 完成（詳見 `raw/registry.json`；結構化 ECS 清單見 `raw/structured/igene_disease_list.csv` / `.json`）
- **編修與演進日誌**：[wiki/log.md](log.md)

---

## 依目標讀者建議閱讀路徑

- **Patient（一般民眾與患者）**：建議從 [FAQ 常見問題](#faq患者與一般民眾常見問題)、[ECS / iGene 產品主頁](products/ecs.md) 與 [ECS 疾病與基因索引](products/ecs-disease-gene-index.md) 切入。
- **Physician（醫師與遺傳諮詢專業人員）**：建議優先閱讀 [Evidence 臨床證據整合](#evidence臨床證據與跨指引整合)、[Genetic Counseling（生殖遺傳諮詢）](concepts/genetic-counseling.md) 與各產品頁之「適用對象／檢測限制」。
- **Laboratory（實驗室與胚胎師團隊）**：建議優先閱讀 [Laboratory 實驗室與技術流程](#laboratory實驗室概覽與作業規範)、[NGS Technology](laboratory/ngs-technology.md)、[Embryo Biopsy](concepts/embryo-biopsy.md)、[Haplotyping](concepts/haplotyping.md) 與 [Allele Dropout](concepts/allele-dropout.md)。

---

## Products（核心檢測產品與結構化清單）

| 頁面 | 簡介 | 主要來源 | 審核狀態 |
| :--- | :--- | :--- | :--- |
| [PGT-A（胚胎著床前染色體非整倍體篩檢）](products/pgt-a.md) | 24 條染色體數目篩檢、ASRM 2024 立場、Euploid/Mosaic 判讀與 NGS 平台現況 | `SRC-001`, `SRC-002`, `SRC-004`, `SRC-006`–`SRC-008` | `pending_clinical_review` / `pending_technical_verification` |
| [ECS（擴展性帶因者篩檢 / iGene）](products/ecs.md) | 整合 ACMG 2021 與 iGene（350 項疾病、15 大類、351 基因含 28 個 XL 基因）、Thermo Fisher NGS 與殘餘風險 | `SRC-003`, `SRC-006`, `SRC-009` | `product_spec_verified` / `pending_clinical_review` / `pending_technical_verification` |
| [ECS Disease & Gene Index（iGene 350 項疾病與 351 個基因索引）](products/ecs-disease-gene-index.md) | 結構化統計、15 大類明細、28 個 XL 基因、`HBA1/HBA2` 與 `AR/AD` 審核註記，支援 Wiki Browser 互動搜尋 | `SRC-003`, `SRC-009` | `product_spec_verified` / `pending_clinical_review` / `pending_technical_verification` |
| [PGT-SR（胚胎著床前染色體結構重排檢測）](products/pgt-sr.md) | 平衡轉位／羅伯遜轉位事前評估、NGS/aCGH/SNP array/FISH 解析度比較 | `SRC-002`, `SRC-004`, `SRC-005`, `SRC-007`, `SRC-008` | `pending_clinical_review` |
| [PGT-M（胚胎著床前單基因遺傳疾病檢測）](products/pgt-m.md) | 適應症與不建議項目、客製化家族連鎖建置、ADO 風險與產前確認原則 | `SRC-001`, `SRC-005`, `SRC-006`, `SRC-007`, `SRC-008` | `pending_clinical_review` |

---

## Concepts（生殖遺傳與分子技術核心概念）

| 頁面 | 簡介 | 主要來源 | 審核狀態 |
| :--- | :--- | :--- | :--- |
| [Aneuploidy（染色體非整倍體）](concepts/aneuploidy.md) | 染色體數目異常之減數／有絲分裂成因、年齡關聯與早期流產機制 | `SRC-001`, `SRC-002`, `SRC-004`, `SRC-008` | `auto_compiled` |
| [Euploidy（染色體整倍體）](concepts/euploidy.md) | 正常二倍體 46 條染色體定義與 PGT-A 整倍體判讀之臨床意涵 | `SRC-001`, `SRC-002`, `SRC-004` | `auto_compiled` |
| [Mosaicism（染色體鑲嵌型）](concepts/mosaicism.md) | 胚胎鑲嵌生物學成因、切片中間訊號不等同 ICM 狀態與植入風險評估 | `SRC-002`, `SRC-004`, `SRC-008` | `pending_clinical_review` |
| [Copy Number Variation（拷貝數變異 / CNV）](concepts/copy-number-variation.md) | 染色體劑量分析、NGS/aCGH/SNP array 一般解析度參考與偵測限制 | `SRC-004`, `SRC-006` | `auto_compiled` |
| [Structural Chromosomal Rearrangement（染色體結構重排）](concepts/structural-chromosomal-rearrangement.md) | 相互轉位、羅伯遜轉位、倒位與減數分裂不平衡分離風險 | `SRC-004`, `SRC-007` | `auto_compiled` |
| [Monogenic Disease（單基因遺傳疾病）](concepts/monogenic-disease.md) | 孟德爾單基因與粒線體遺傳模式，銜接 ECS 與 PGT-M 應用 | `SRC-003`–`SRC-006` | `auto_compiled` |
| [Autosomal Recessive（體染色體隱性遺傳）](concepts/autosomal-recessive.md) | 雙方帶因 25% 罹病機率、ACMG Tier 3 門檻與 iGene 319 項 `AR` / 3 項 `AR/AD` 涵蓋現況 | `SRC-003`, `SRC-006`, `SRC-009` | `product_spec_verified` / `pending_clinical_review` |
| [X-linked Inheritance（X 染色體性聯遺傳）](concepts/x-linked-inheritance.md) | 女性帶因風險、ACMG 16 個 XL 基因 vs. iGene 28 個 XL 基因（不含 *FMR1*）跨來源比對 | `SRC-003`–`SRC-006`, `SRC-009` | `product_spec_verified` / `pending_clinical_review` |
| [Residual Risk（殘餘風險）](concepts/residual-risk.md) | 篩檢陰性殘餘風險公式、iGene 官網檢出率（76%–99%）解讀限制與目標區間 NGS 邊界 | `SRC-003`, `SRC-009` | `product_spec_verified` / `pending_clinical_review` |
| [Embryo Biopsy（胚胎切片）](concepts/embryo-biopsy.md) | 囊胚滋養外胚層切片（TE Biopsy）、Tubing 防污染清洗與單顆冷凍規範 | `SRC-001`, `SRC-002`, `SRC-004`, `SRC-005`, `SRC-007`, `SRC-008` | `pending_clinical_review` |
| [Haplotyping（單倍型分析／連鎖分析）](concepts/haplotyping.md) | STR/SNP 上下游連鎖標記定相原理與無法建立家族連鎖之困難情境 | `SRC-004`, `SRC-005`, `SRC-006` | `auto_compiled` |
| [Allele Dropout（等位基因脫落 / ADO）](concepts/allele-dropout.md) | 微量 DNA 擴增單側等位基因漏檢之誤診機制與多點連鎖防禦策略 | `SRC-005`, `SRC-006`, `SRC-008` | `auto_compiled` |
| [Genetic Counseling（生殖遺傳諮詢）](concepts/genetic-counseling.md) | 跨指引檢前／檢後諮詢重點、自主選擇權與診所／實驗室諮詢師協作 | `SRC-001`–`SRC-007` | `pending_clinical_review` |

---

## Evidence（臨床證據與跨指引整合）

| 頁面 | 簡介 | 整合來源 | 審核狀態 |
| :--- | :--- | :--- | :--- |
| [PGT-A 臨床證據與跨指引整合](evidence/pgt-a-clinical-evidence.md) | 彙整 ASRM 2024 與 ESHRE 2020 對高齡、反覆流產、累積活產與 ICSI 的共識及差異 | `SRC-001`, `SRC-002`, `SRC-004`, `SRC-005`, `SRC-008` | `pending_clinical_review` |
| [Mosaic 胚胎臨床處置與風險評估證據整合](evidence/mosaic-embryo-evidence.md) | 整合 ASRM 2023 與 ESHRE 2020 對 MET 結局、風險排序限制與產前追蹤建議 | `SRC-002`, `SRC-004`, `SRC-008` | `pending_clinical_review` |
| [ECS 分層架構與臨床實證整合](evidence/ecs-clinical-evidence.md) | 彙整 ACMG 2021 Tier 1–4 基準並對照 iGene 官方 350 項清單（含 *FMR1* 差異） | `SRC-003`, `SRC-006`, `SRC-009` | `product_spec_verified` / `pending_clinical_review` |
| [PGT-M 與 PGT-SR 國際指引與技術實證整合](evidence/pgt-m-sr-evidence.md) | 對照 ASRM 2023 與 ESHRE 2020 在適應症邊界、高難度基因與平台解析度上的互補規範 | `SRC-004`, `SRC-005`, `SRC-006`, `SRC-007` | `pending_clinical_review` |

---

## Laboratory（實驗室概覽與作業規範）

> 本實驗室已確認使用 **Thermo Fisher Scientific / Ion Torrent NGS** 定序技術，並確認 **PGT-A 覆蓋深度常規為 `0.005×`、最高 `0.02×`**；各產品技術規格分開管理，不可假定所有產品共用相同機型、晶片、流程或分析方法。其餘未提供規格與認證狀態均維持 `pending_technical_verification`。

| 頁面 | 簡介 | 主要來源 | 審核狀態 |
| :--- | :--- | :--- | :--- |
| [Laboratory Overview（實驗室概覽）](laboratory/laboratory-overview.md) | 多專業團隊架構、分子防污染分區、Ion Torrent NGS 技術與分產品規格邊界 | `SRC-003`–`SRC-009` | `product_spec_verified` / `pending_clinical_review` / `pending_technical_verification` |
| [NGS Technology（次世代定序技術與 Ion Torrent 平台）](laboratory/ngs-technology.md) | Thermo Fisher Scientific / Ion Torrent NGS 技術、PGT-A 覆蓋深度（常規 0.005×／最高 0.02×）與四大產品獨立規格矩陣 | `SRC-003`, `SRC-004`, `SRC-005`, `SRC-007`, `SRC-009` | `pending_technical_verification` / `pending_clinical_review` |
| [PGT Workflow（PGT 端到端標準作業流程）](laboratory/pgt-workflow.md) | 檢前收案、事前建置、囊胚切片、冷凍、分析判讀至妊娠追蹤七大階段 | `SRC-002`, `SRC-004`–`SRC-008` | `pending_clinical_review` |
| [Quality Management（實驗室品質管理與風險控管）](laboratory/quality-management.md) | ISO 15189 一般標準、IQA/EQA、臨床前方法驗證、獨立訓練與 CAPA | `SRC-002`, `SRC-004`–`SRC-008` | `pending_clinical_review` |
| [Sample Traceability（檢體標示、雙人見證與全程追溯）](laboratory/sample-traceability.md) | 雙重病人識別碼標示、七大關鍵雙人見證節點與 Transport PGT 協議 | `SRC-004`, `SRC-005`, `SRC-007`, `SRC-008` | `pending_clinical_review` |

---

## FAQ（患者與一般民眾常見問題）

| 頁面 | 核心問題 | 主要來源 | 審核狀態 |
| :--- | :--- | :--- | :--- |
| [ECS / iGene 遺傳疾病帶因篩檢與 NGS 實驗室常見問題](faq/ecs-faq.md) | iGene 350 項疾病與 351 基因差異、夫妻檢測策略、NGS 限制、新生兒篩檢與實驗室平台說明 | `SRC-003`, `SRC-006`, `SRC-009` | `product_spec_verified` / `pending_clinical_review` / `pending_technical_verification` |
| [ECS 結果陰性，代表寶寶不會得遺傳病嗎？](faq/faq-ecs-negative-risk.md) | 白話解說 Residual Risk、iGene NGS 限制與出生後仍建議新生兒篩檢 | `SRC-003`, `SRC-009` | `product_spec_verified` / `pending_clinical_review` |
| [PGT-A、PGT-SR 與 PGT-M 有什麼差別？](faq/faq-pgt-a-vs-pgt-sr-vs-pgt-m.md) | 三種胚胎著床前檢測的遺傳層級與適用族群比較 | `SRC-001`, `SRC-004`, `SRC-005`, `SRC-006` | `pending_clinical_review` |
| [做 PGT-A 可以保證懷孕或降低流產率嗎？](faq/faq-pgt-a-guarantee-pregnancy.md) | 釐清 PGT-A 無法保證懷孕／活產與 ASRM 2024 最新臨床實證 | `SRC-001`, `SRC-002` | `pending_clinical_review` |
| [胚胎報告顯示 Mosaic（鑲嵌型），還能植入嗎？](faq/faq-mosaic-embryo-transfer.md) | 說明切片訊號不等同整顆胚胎狀態、胎兒確認率 < 1% 與植入前諮詢 | `SRC-002`, `SRC-008` | `pending_clinical_review` |
| [胚胎切片會傷害胚胎嗎？為何要先冷凍？](faq/faq-embryo-biopsy-safety.md) | 說明囊胚滋養外胚層切片避開 ICM 與切片後玻璃化冷凍原因 | `SRC-001`, `SRC-007`, `SRC-008` | `pending_clinical_review` |
| [做完 PGT 懷孕後還需要產前檢查嗎？](faq/faq-prenatal-testing-after-pgt.md) | 說明為何所有 PGT 懷孕仍建議討論標準或確認性產前檢查 | `SRC-001`, `SRC-002`, `SRC-004`, `SRC-006`, `SRC-007`, `SRC-008` | `pending_clinical_review` |

---

## Raw Source Registry 總覽

| Source ID | 機構 / 年份 | 文獻或來源標題 | DOI / 類型 | 擷取狀態 |
| :--- | :--- | :--- | :--- | :--- |
| `SRC-001` | ASRM / 2024 | The use of preimplantation genetic testing for aneuploidy: a committee opinion | `10.1016/j.fertnstert.2024.04.013` | `ingested` |
| `SRC-002` | ASRM / 2023 | Clinical management of mosaic results from preimplantation genetic testing for aneuploidy of blastocysts: a committee opinion | `10.1016/j.fertnstert.2023.08.969` | `ingested` |
| `SRC-003` | ACMG / 2021 | Screening for autosomal recessive and X-linked conditions during pregnancy and preconception: a practice resource of the ACMG | `10.1038/s41436-021-01203-z` | `ingested` |
| `SRC-004` | ESHRE / 2020 | ESHRE PGT Consortium good practice recommendations for the detection of structural and numerical chromosomal aberrations | `10.1093/hropen/hoaa017` | `ingested` |
| `SRC-005` | ESHRE / 2020 | ESHRE PGT Consortium good practice recommendations for the detection of monogenic disorders | `10.1093/hropen/hoaa018` | `ingested` |
| `SRC-006` | ASRM / 2023 | Indications and management of preimplantation genetic testing for monogenic conditions: a committee opinion | `10.1016/j.fertnstert.2023.03.003` | `ingested` |
| `SRC-007` | ESHRE / 2020 | ESHRE PGT Consortium good practice recommendations for the organisation of PGT | `10.1093/hropen/hoaa021` | `ingested` |
| `SRC-008` | ESHRE / 2020 | ESHRE PGT Consortium and SIG Embryology good practice recommendations for polar body and embryo biopsy for PGT | `10.1093/hropen/hoaa020` | `ingested` |
| `SRC-009` | 愛生育銀行／送子鳥生殖中心 / 2026 | iGene 遺傳疾病帶因篩檢官方產品頁與完整疾病列表（含 350 筆 CSV/JSON 結構化資料） | `Official Company Website` | `ingested` |
