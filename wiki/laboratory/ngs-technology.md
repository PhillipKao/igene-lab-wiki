---
title: "NGS Technology（次世代定序技術與本實驗室 Ion Torrent 平台分產品規格管理）"
category: "laboratory"
summary: "介紹次世代定序（NGS）一般技術原理與限制，記錄實驗室已確認之 Thermo Fisher Scientific / Ion Torrent NGS 定序技術、晶片規格（PGT-A：520、ECS：530）與 PGT-A 覆蓋深度（常規 0.005×、最高 0.02×），並將四大產品技術規格分開管理與標註 Pending Technical Verification。"
source_ids:
  - "SRC-003"
  - "SRC-004"
  - "SRC-005"
  - "SRC-007"
  - "SRC-009"
created_at: "2026-11-23"
updated_at: "2026-11-23"
review_status: "pending_technical_verification"
review_layers:
  - "source_verified"
  - "pending_technical_verification"
  - "pending_clinical_review"
related_pages:
  - "laboratory-overview.md"
  - "pgt-workflow.md"
  - "quality-management.md"
  - "../products/ecs.md"
  - "../products/ecs-disease-gene-index.md"
  - "../products/pgt-a.md"
  - "../products/pgt-sr.md"
  - "../products/pgt-m.md"
  - "../concepts/copy-number-variation.md"
  - "../faq/ecs-faq.md"
---

# NGS Technology（次世代定序技術與本實驗室 Ion Torrent 平台說明）

> **技術驗證與合規聲明**：本頁依據實驗室技術確認（`2026-11-23`）與國際指引整理，明確區分「已確認資訊」與「`Pending Technical Verification`」。**嚴禁自行推定具體設備型號或晶片型號，亦不得以 Thermo Fisher Scientific 原廠宣傳或一般性能規格代替本實驗室實際驗證報告（Validation Report）之實測結果**。在正式檢驗報告、Validation Report、SOP 與認證文件完成覆核前，本頁不得標示為 `approved`。

## Overview（已確認之本實驗室技術資訊）

1. **定序技術廠牌與系統家族**：本實驗室使用 **Thermo Fisher Scientific** 之 **Ion Torrent NGS** 定序技術（實驗室技術確認，`2026-11-23`）。
2. **各產品分開管理原則**：本知識庫涵蓋 [PGT-A](../products/pgt-a.md)、[ECS（iGene）](../products/ecs.md)、[PGT-SR](../products/pgt-sr.md)、[PGT-M](../products/pgt-m.md) 四項產品，**不可假定所有產品皆共用同一台定序儀、同一款晶片、同一套濕實驗室流程或同一套生物資訊分析方法**。
3. **PGT-A 已確認技術參數**：定序晶片（Chip Type）為 **520（Ion 520）**，覆蓋深度（Coverage）**常規為 `0.005×`，最高為 `0.02×`**（屬低覆蓋全基因體拷貝數分析區間；正式驗證文件與解析度邊界仍待 Validation Report 佐證）。
4. **ECS（iGene）已確認技術與產品資訊**：定序晶片（Chip Type）為 **530（Ion 530）**；對應 **iGene 遺傳疾病帶因篩檢**官方資料 [SRC-009]，涵蓋 15 大類、350 種疾病（351 個去重獨立基因，含 28 個 X 性聯基因），完整清單對接 [ECS Disease & Gene Index](../products/ecs-disease-gene-index.md)。
   （註：PGT-A 與 ECS 採用不同晶片［520 vs. 530］，更印證四大產品須分開管理；具體定序儀機型、PGT-SR 與 PGT-M 晶片／平台均不得自行推定。）

## Key Concepts（國際指引一般性 NGS 技術原理）

以下說明依據 ACMG 2021（[SRC-003]）與 ESHRE 2020（[SRC-004]、[SRC-005]）整理之**一般性專業知識**，不代表特定儀器實測性能：

1. **全基因體淺層定序拷貝數分析（WGA + Low-pass NGS — 一般應用於 PGT-A / PGT-SR）**：
   - 胚胎切片取得約 5–10 個囊胚滋養外胚層細胞後進行全基因體放大（WGA），再以 NGS 讀取基因體片段並依各染色體區間讀數分布量化 [Copy Number Variation（拷貝數變異）](../concepts/copy-number-variation.md) [SRC-004]。
   - 標準無基因分型拷貝數分析無法偵測單基因點突變、平衡性轉位、低於驗證解析度之微缺失微重複或部分倍數性異常 [SRC-004]。
2. **目標區間定序（Targeted Panel NGS — 一般應用於 ECS / 部分 PGT-M）**：
   - 針對目標疾病基因編碼區與關鍵區域進行富集定序，偵測單核苷酸變異（SNV）及小型插入／缺失（Indel）[SRC-003] [SRC-009]。
   - 如 [SRC-009] 與 [SRC-003] 所述，常規目標區間 NGS 無法偵測大片段基因缺失、插入、倒轉、重複性擴增（如三核苷酸重複序列）、複雜結構重排、非目標區間及深層內含子（intron）變異。

## 分產品技術規格管理矩陣（已確認 vs. Pending Technical Verification）

為避免跨產品混用平台假設，以下將四大產品之技術規格**完全分開管理**：

### 1. PGT-A 技術規格狀態
| 規格項目 | 目前狀態 | 內容說明／所需佐證文件 |
| :--- | :--- | :--- |
| **實驗室 NGS 技術確認** | 已確認技術家族（機型與流程待核） | 實驗室採用 Thermo Fisher Scientific / Ion Torrent NGS 技術；具體設備型號屬 `Pending Technical Verification` |
| **定序晶片型號（Chip Type）** | **已確認（實驗室提供，2026-11-23）** | **520（Ion 520 晶片）**（後續建議附 SOP / 驗證文件備查） |
| **定序覆蓋深度（Coverage）** | **已確認（實驗室提供，2026-11-23）** | **常規 `0.005×`，最高 `0.02×`**（後續建議附 Validation Report / SOP 佐證） |
| **具體設備型號 / Read Length** | `Pending Technical Verification` | 未提供，不得自行推定具體 Ion Torrent 儀器型號；需設備清冊／SOP 佐證 |
| **CNV / Aneuploidy 最小偵測解析度** | `Pending Technical Verification` | 需本實驗室內部 Validation Report（不可引用原廠一般規格代替） |
| **Mosaic / Low-VAF 偵測下限與揭露政策** | `Pending Technical Verification` | 需本實驗室驗證報告與正式臨床報告政策文件 |
| **分析靈敏度／特異度 / TAT** | `Pending Technical Verification` | 需 Validation Report 與正式檢驗報告範本／SOP |

### 2. ECS（iGene）技術規格狀態
| 規格項目 | 目前狀態 | 內容說明／所需佐證文件 |
| :--- | :--- | :--- |
| **產品名稱與官方疾病清單** | `product_spec_verified` [SRC-009] | **iGene 遺傳疾病帶因篩檢**，15 大類 350 種疾病（351 個去重獨立基因，含 28 個 X 性聯基因），採血液 DNA 目標區間 NGS [SRC-009] |
| **定序晶片型號（Chip Type）** | **已確認（實驗室提供，2026-11-23）** | **530（Ion 530 晶片）**（與 PGT-A 之 520 晶片不同；後續建議附 SOP / 驗證文件備查） |
| **具體設備型號及與他項流程共用狀態** | `Pending Technical Verification` | 不得自行推定具體 Ion Torrent 儀器型號或假定與其他產品共用完整實驗／分析流程；需實驗室 SOP 確認 |
| **ECS 定序 Coverage / Read Length** | `Pending Technical Verification` | 尚未提供，不得填入未確認數值；需 Validation Report 佐證 |
| **各變異類型 Analytical Sensitivity / Specificity** | `Pending Technical Verification` | 官網「檢出率」（76%–99%）不可解讀為所有變異類型之統一分析敏感度 [SRC-003] [SRC-009]；需 Validation Report 佐證 |
| **Low-VAF / 輔助檢測方法（如 *SMN1*、*HBA1/HBA2*）與 TAT** | `Pending Technical Verification` | 需本實驗室 SOP 與正式檢驗報告範本確認 |

### 3. PGT-SR 技術規格狀態
| 規格項目 | 目前狀態 | 內容說明／所需佐證文件 |
| :--- | :--- | :--- |
| **使用平台與是否共用 PGT-A 流程** | `Pending Technical Verification` | 不可假定與 PGT-A 共用相同儀器、晶片或分析演算法；需實驗室 SOP 確認 |
| **定序 Coverage / 最小偵測片段大小（Mb）** | `Pending Technical Verification` | 需本實驗室 Validation Report（ESHRE 2020 [SRC-004] 僅作一般背景參考） |
| **是否具備區分正常胚胎與平衡重排帶因能力** | `Pending Technical Verification` | 需實驗室確認是否結合單倍型分析及提供 Validation Report |
| **分析靈敏度／特異度 / TAT** | `Pending Technical Verification` | 需 Validation Report 與正式檢驗報告範本 |

### 4. PGT-M 技術規格狀態
| 規格項目 | 目前狀態 | 內容說明／所需佐證文件 |
| :--- | :--- | :--- |
| **使用平台（PCR/STR、SNP Array 或 Targeted NGS）** | `Pending Technical Verification` | 不可假定與其他產品共用平台或流程；需實驗室 SOP 確認 |
| **Coverage（若採 NGS）/ 連鎖標記設計規格** | `Pending Technical Verification` | 需本實驗室臨床前驗證（Preclinical Work-up）SOP 與 Validation Report |
| **各變異類型 Analytical Sensitivity / Specificity / ADO 控管指標** | `Pending Technical Verification` | 需本實驗室內部驗證資料（ESHRE 2020 [SRC-005] 僅作一般背景參考） |
| **事前建置週期與檢測 TAT** | `Pending Technical Verification` | 需正式服務規範／SOP 佐證 |

### 5. 實驗室整體認證與法規核准狀態
- **ISO 15189、LDTs、CAP 或其他衛生主管機關核准狀態**：目前全數列為 **`Pending Technical Verification`**，必須取得本實驗室有效認證證書或核准公文影本／編號後方可記載 [SRC-007]。

## Related Pages

- [Laboratory Overview（實驗室概覽）](laboratory-overview.md)
- [PGT Workflow（PGT 檢測作業流程）](pgt-workflow.md)
- [Quality Management（實驗室品質管理）](quality-management.md)
- [PGT-A 檢測產品頁](../products/pgt-a.md)
- [ECS（擴展性帶因者篩檢 / iGene）](../products/ecs.md)
- [PGT-SR 檢測產品頁](../products/pgt-sr.md)
- [PGT-M 檢測產品頁](../products/pgt-m.md)
- [FAQ：ECS / iGene 與 NGS 實驗室常見問題](../faq/ecs-faq.md)

## Sources

- **[SRC-003]** Gregg AR et al.; ACMG (2021). *Screening for autosomal recessive and X-linked conditions during pregnancy and preconception: a practice resource of the ACMG*.
- **[SRC-004]** ESHRE PGT-SR/PGT-A Working Group (2020). *ESHRE PGT Consortium good practice recommendations for the detection of structural and numerical chromosomal aberrations*.
- **[SRC-005]** ESHRE PGT-M Working Group (2020). *ESHRE PGT Consortium good practice recommendations for the detection of monogenic disorders*.
- **[SRC-007]** ESHRE PGT Consortium Steering Committee (2020). *ESHRE PGT Consortium good practice recommendations for the organisation of PGT*.
- **[SRC-009]** 愛生育銀行／送子鳥生殖中心（2026）. *iGene 遺傳疾病帶因篩檢官方產品頁與完整疾病列表*（`https://www.icryobank.com/gene/igene`、`https://www.icryobank.com/gene/igene-disease-list`）；另含實驗室技術確認資訊（Thermo Fisher Scientific / Ion Torrent NGS 技術；PGT-A 常規 0.005×、最高 0.02× coverage）。
