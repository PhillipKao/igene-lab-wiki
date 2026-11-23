---
title: "X-linked Inheritance（X 染色體性聯遺傳）"
category: "concepts"
summary: "說明 X 染色體性聯遺傳疾病的遺傳特性、女性帶因者與男性受影響者的風險差異、ACMG 2021 建議之 16 個 X 性聯篩檢基因標準，以及在 ECS 與 PGT-M 中的應用。"
source_ids:
  - "SRC-003"
  - "SRC-004"
  - "SRC-005"
  - "SRC-006"
  - "SRC-009"
created_at: "2026-11-23"
updated_at: "2026-11-23"
review_status: "pending_clinical_review"
review_layers:
  - "source_verified"
  - "product_spec_verified"
  - "pending_clinical_review"
related_pages:
  - "monogenic-disease.md"
  - "autosomal-recessive.md"
  - "residual-risk.md"
  - "../products/ecs.md"
  - "../products/ecs-disease-gene-index.md"
  - "../products/pgt-m.md"
---

# X-linked Inheritance（X 染色體性聯遺傳）

## Overview

**X-linked Inheritance（X 染色體性聯遺傳）**係指致病基因位於 X 性染色體上的單基因遺傳模式 [SRC-003]。由於男性僅有一條 X 染色體（XY），而女性擁有兩條 X 染色體（XX），X 性聯疾病在男女之間的遺傳機率與臨床表現常呈現明顯差異 [SRC-003]。

## Key Concepts

- **女性帶因者生育風險**：若母親為 X 性聯遺傳疾病帶因者（一條 X 染色體帶有致病變異、另一條正常），每次懷孕皆有 **50%** 機率將帶有變異的 X 染色體遺傳給子代：
  - **男性子代（XY）**：有 50% 機率遺傳致病 X 染色體並表現疾病（因無第二條正常 X 染色體代償）；
  - **女性子代（XX）**：有 50% 機率成為帶因者（依不同疾病與 X 染色體去活化現象，可能無症狀或表現輕重不等之症狀）。
- **毋須男性伴侶同基因帶因**：與 [Autosomal Recessive（體染色體隱性遺傳）](autosomal-recessive.md) 不同，只要女性本身為 X 性聯疾病帶因者，即使男性伴侶正常，子代即面臨顯著遺傳風險 [SRC-003]。

## Detailed Explanation

在 [ECS（擴展性帶因者篩檢）](../products/ecs.md) 實務中，各家檢測實驗室納入的 X 性聯基因差異頗大。ACMG 2021 實務指引針對 X 性聯遺傳疾病訂定透明納入標準，以疾病盛行率 **$1/40{,}000$** 作為基準，並交叉比對 ClinGen 基因－疾病關聯證據，選出 **16 個適合納入 Tier 3 帶因者篩檢的 X 性聯基因**（其中 13/16 具確定性 ClinGen 關聯，涵蓋如 X 染色體脆折症 *FMR1*、裘馨氏肌肉失養症 *DMD* 等代表性疾病）[SRC-003]。

### 跨來源對照：ACMG 2021（16 基因）vs. iGene 官方列表（28 基因）[SRC-009]
- 愛生育銀行／送子鳥生殖中心 iGene 官方列表實際收錄 **28 筆 XL 疾病，對應 28 個去重獨立 X 性聯基因**（包含 `DMD`、`F8`、`F9`、`G6PD`、`GLA`、`IDS`、`MECP2`、`OTC`、`ABCD1` 等，完整清單見 [ECS 疾病與基因索引](../products/ecs-disease-gene-index.md)）[SRC-009]。
- **保留差異與待臨床審核註記**：ACMG 2021 建議的 *FMR1*（X 染色體脆折症）屬於 CGG 三核苷酸重複序列擴增疾病，超出目標區間 NGS 的偵測能力，因此**未列入 iGene 350 項 NGS 清單中**；而 iGene 則額外納入東亞高盛行之 *G6PD*（蠶豆症）等共 28 個基因 [SRC-003] [SRC-009]。臨床衛教應明確說明此差異，由醫師或遺傳諮詢師評估是否需額外搭配 X 染色體脆折症專屬檢測。

此外，在 [PGT-M](../products/pgt-m.md) 中，現代優先策略是直接結合連鎖分析檢測特定 X 性聯致病變異本身，而非僅依賴傳統的胚胎性別篩選（sexing），藉以保留未遺傳致病 X 染色體之健康男性胚胎並避免不必要之胚胎棄置 [SRC-004] [SRC-005]。

## Clinical Relevance

- **女性帶因者自身健康管理**：部分 X 性聯疾病女性帶因者本身亦可能具臨床表現風險（例如 *FMR1* 前突變相關卵巢早衰或神經症狀、*DMD* 帶因者心肌病變風險等），檢出後應接受 [Genetic Counseling（遺傳諮詢）](genetic-counseling.md) 評估自身追蹤與生育規劃 [SRC-003] [SRC-006]。
- **特殊技術考量**：如 *FMR1* 等三核苷酸重複擴增疾病在 PGT-M 上常高度依賴家族連鎖分析（[Haplotyping](haplotyping.md)）[SRC-006]。

## Limitations

- 部分 X 性聯疾病具高比例新發（*de novo*）突變或母體生殖腺鑲嵌現象，帶因者篩檢陰性仍無法將風險降為零（見 [Residual Risk](residual-risk.md)）[SRC-003]。

## Related Pages

- [Monogenic Disease（單基因遺傳疾病）](monogenic-disease.md)
- [Autosomal Recessive（體染色體隱性遺傳）](autosomal-recessive.md)
- [Residual Risk（殘餘風險）](residual-risk.md)
- [ECS 檢測產品頁](../products/ecs.md)
- [PGT-M 檢測產品頁](../products/pgt-m.md)

## Sources

- **[SRC-003]** Gregg AR et al.; ACMG (2021). *Screening for autosomal recessive and X-linked conditions during pregnancy and preconception: a practice resource of the ACMG*.
- **[SRC-004]** ESHRE PGT-SR/PGT-A Working Group (2020). *ESHRE PGT Consortium good practice recommendations for the detection of structural and numerical chromosomal aberrations*.
- **[SRC-005]** ESHRE PGT-M Working Group (2020). *ESHRE PGT Consortium good practice recommendations for the detection of monogenic disorders*.
- **[SRC-006]** ASRM Practice Committee & GCPG (2023). *Indications and management of preimplantation genetic testing for monogenic conditions: a committee opinion*.
- **[SRC-009]** 愛生育銀行／送子鳥生殖中心（2026）. *iGene 遺傳疾病帶因篩檢列表與產品介紹*（`https://www.icryobank.com/gene/igene-disease-list`）。
