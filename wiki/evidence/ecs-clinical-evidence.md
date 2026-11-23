---
title: "擴展性帶因者篩檢（ECS）分層架構與臨床實證整合（ACMG 2021）"
category: "evidence"
summary: "整合 ACMG 2021 帶因者篩檢實務指引（SRC-003），說明為何以不分族群四層分級架構（Tier 1–4）取代傳統種族篩檢與模糊的 ECS 名稱、X 性聯基因篩選標準、殘餘風險與檢前／檢後諮詢原則。"
source_ids:
  - "SRC-003"
  - "SRC-006"
  - "SRC-009"
created_at: "2026-11-23"
updated_at: "2026-11-23"
review_status: "pending_clinical_review"
review_layers:
  - "source_verified"
  - "product_spec_verified"
  - "pending_clinical_review"
  - "pending_technical_verification"
related_pages:
  - "../products/ecs.md"
  - "../products/ecs-disease-gene-index.md"
  - "../concepts/autosomal-recessive.md"
  - "../concepts/x-linked-inheritance.md"
  - "../concepts/residual-risk.md"
  - "../concepts/genetic-counseling.md"
  - "../faq/ecs-faq.md"
  - "../faq/faq-ecs-negative-risk.md"
---

# 擴展性帶因者篩檢（ECS）分層架構與臨床實證整合

> **審核狀態提示**：本頁整理 ACMG 2021 臨床篩檢分層建議與風險溝通原則，目前為 `pending_clinical_review`。

## Overview

過去五十年來，帶因者篩檢從針對特定高盛行族群的單一疾病篩檢（如阿什肯納茲猶太族群之 Tay–Sachs 病、非裔族群之鐮刀型貧血），逐步演進至囊性纖維化（CF）與脊髓性肌肉萎縮症（SMA）的不分族群篩檢 [SRC-003]。隨著次世代定序（NGS）普及，各實驗室推出基因數差異極大的「擴展性帶因者篩檢（ECS）」套組，導致臨床名詞與基因納入標準缺乏一致性 [SRC-003]。

**ACMG 2021 實務指引（[SRC-003]）** 提出以**透明、族群中立、頻率導向之四層分級（Tier 1–4）**取代模糊的「ECS」與種族導向篩檢模式。

## Key Concepts（ACMG 2021 四層篩檢分級架構）

| 層級 | 定義與納入基準（ACMG 2021） | 臨床提供立場 |
| :--- | :--- | :--- |
| **Tier 1** | CF、SMA 加上依個人／家族病史與檢查風險評估決定之項目（承襲既往 ACMG/ACOG 建議）[SRC-003] | 基礎族群中立篩檢門檻 |
| **Tier 2** | 在任一族群中帶因頻率 $\ge 1/100$ 之體染色體隱性遺傳疾病（包含 Tier 1）[SRC-003] | 過渡層級，涵蓋較高頻率疾病 |
| **Tier 3（核心建議層級）** | 在任一族群中帶因頻率 **$\ge 1/200$** 之體染色體隱性遺傳疾病，加上依疾病盛行率 **$1/40{,}000$** 標準與 ClinGen 證據篩選出的 **16 個 X 性聯遺傳基因**（包含 Tier 1 與 Tier 2）[SRC-003] | **ACMG 建議向所有備孕及懷孕患者提供**，且應以族群中立方式實施 [SRC-003] |
| **Tier 4** | 帶因頻率低於 $1/200$（無下限）之更罕見基因，各實驗室清單差異大 [SRC-003] | **不建議常規提供**；主要於**近親聯姻（consanguinity）**或明確個人／家族病史時審慎評估 [SRC-003] |

## Detailed Explanation

### 1. X 染色體性聯遺傳基因納入標準
ACMG 2021 指出，市面上部分帶因套組納入盛行率高至 $1/3{,}500$、亦或罕見至低於 $1/1{,}000{,}000$ 的 X 性聯基因，缺乏一致透明準則 [SRC-003]。ACMG 透過明確納入條件（以 $1/40{,}000$ 疾病盛行率為門檻）選出 **16 個 X 性聯基因**，其中 13/16（81%）於 ClinGen 具有確定性（definitive）基因－疾病關聯證據，並要求任何實驗室皆須公開其基因納入與排除之透明標準 [SRC-003]。

### 2. 為何不建議常規採用無限擴張的 Tier 4？
雖然低於 $1/200$ 帶因頻率的基因中確實存在嚴重遺傳疾病且能額外辨識少數高風險伴侶，但 ACMG 2021 提醒 Tier 4 面臨顯著臨床與實驗室挑戰：許多極罕見疾病缺乏自然病程資料，加上基因多效性（pleiotropy）、位點異質性、變異判讀困難與基因型－表現型關聯薄弱，可能反而增加臨床諮詢負擔與焦慮 [SRC-003]。

### 3. 殘餘風險（Residual Risk）之實證聲明
ACMG 2021 提出三項不可忽視之核心立場（詳見 [Residual Risk](../concepts/residual-risk.md)）[SRC-003]：
- 陰性結果可降低但**絕不會消除**成為受檢疾病帶因者的風險，**任何疾病的殘餘風險永遠不為零**；
- 單一疾病殘餘風險公式為 $\text{Population Carrier Frequency} \times (1 - \text{Detection Rate})$；
- 對多基因同步篩檢（multiplex screening）之整體陰性結果，**實務上無法計算精確的單一整體殘餘風險**，因並非所有受檢罕見疾病皆具明確族群帶因頻率與檢測率。

### 4. 與本機構 iGene 產品規格之跨來源對照（SRC-003 vs. SRC-009）
將 ACMG 2021 分層建議 [SRC-003] 與愛生育銀行／送子鳥生殖中心 iGene 官方 350 項清單 [SRC-009] 對照如下（保留雙方差異並標記 `pending_clinical_review`）：
- **規模對應**：iGene 涵蓋 15 大類、350 筆疾病（對應 351 個去重獨立基因，含 *SMN1*、*CFTR*、*HBA1/HBA2*、*HBB*、*GJB2* 等），涵蓋範圍已跨入 Tier 3 並納入部分罕見疾病；另有 3 筆具 `AR/AD` 雙重模式標示（`RTEL1`、`COL7A1`、`GH1`）[SRC-009]。
- **X 性聯基因差異**：iGene 包含 **28 個 XL 基因**（含 *DMD*、*F8*、*F9*、*G6PD* 等），高於 ACMG Tier 3 建議之 16 個基因數，但因目標區間 NGS 無法偵測三核苷酸重複序列，**未納入 ACMG 建議之 *FMR1*（X 染色體脆折症）** [SRC-003] [SRC-009]。
- **檢出率與殘餘風險一致性**：iGene 官網檢出率介於 76%–99%、3 筆帶因率為 `-`，正好印證 ACMG 2021 強調「陰性結果殘餘風險永不為零、多基因套組無法給予單一整合殘餘風險」之立場 [SRC-003] [SRC-009]。

### 5. 與 PGT-M 適應症之銜接（整合 ASRM 2023）
透過 ECS 檢出雙方同基因體染色體隱性帶因或女性 X 性聯帶因者，可於孕前銜接 [PGT-M](../products/pgt-m.md) 評估 [SRC-003] [SRC-006]。然而 ASRM 2023 補充提醒，**不應針對僅為無症狀體染色體隱性帶因狀態、偽缺乏等位基因或非致病變異組合執行 PGT-M** [SRC-006]。

## Clinical Relevance & Limitations

- **時機建議**：備孕前（preconception）進行帶因篩檢優於懷孕後，因可提供完整生育選項且心理壓力較低 [SRC-003]。
- **諮詢模式創新**：考量傳統一對一遺傳諮詢耗時費力，ACMG 2021 指出應同步培訓非遺傳專科醫療人員，並發展衛教影片、數位學習或互動輔助工具以協助患者理解與確認知情同意 [SRC-003]。

## Related Pages

- [ECS 檢測產品頁](../products/ecs.md)
- [Autosomal Recessive（體染色體隱性遺傳）](../concepts/autosomal-recessive.md)
- [X-linked Inheritance（X 染色體性聯遺傳）](../concepts/x-linked-inheritance.md)
- [Residual Risk（殘餘風險）](../concepts/residual-risk.md)
- [FAQ：擴展性帶因者篩檢（ECS）結果陰性，代表寶寶完全不會得遺傳病嗎？](../faq/faq-ecs-negative-risk.md)

## Sources

- **[SRC-003]** Gregg AR, Aarabi M, Klugman S, et al.; ACMG (2021). *Screening for autosomal recessive and X-linked conditions during pregnancy and preconception: a practice resource of the ACMG*. Genetics in Medicine, 23(10):1793–1806.
- **[SRC-006]** Practice Committees of ASRM & GCPG (2023). *Indications and management of preimplantation genetic testing for monogenic conditions: a committee opinion*. Fertility and Sterility, 120(1):61–71.
- **[SRC-009]** 愛生育銀行／送子鳥生殖中心（2026）. *iGene 遺傳疾病帶因篩檢列表與產品介紹*（`https://www.icryobank.com/gene/igene-disease-list`、`https://www.icryobank.com/gene/igene`）。
