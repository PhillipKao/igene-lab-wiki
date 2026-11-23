---
title: "Residual Risk（殘餘風險）"
category: "concepts"
summary: "說明帶因者篩檢陰性後仍然存在的殘餘風險（Residual Risk）定義、基本計算公式、多基因篩檢無法提供單一整合殘餘風險之原因，以及檢測前後遺傳諮詢的必談重點。"
source_ids:
  - "SRC-003"
  - "SRC-009"
created_at: "2026-11-23"
updated_at: "2026-11-23"
review_status: "pending_clinical_review"
review_layers:
  - "source_verified"
  - "product_spec_verified"
  - "pending_clinical_review"
related_pages:
  - "autosomal-recessive.md"
  - "x-linked-inheritance.md"
  - "genetic-counseling.md"
  - "../products/ecs.md"
  - "../products/ecs-disease-gene-index.md"
  - "../evidence/ecs-clinical-evidence.md"
  - "../faq/ecs-faq.md"
  - "../faq/faq-ecs-negative-risk.md"
---

# Residual Risk（殘餘風險）

## Overview

**Residual Risk（殘餘風險）**係指受檢者在接受帶因者篩檢並獲得**陰性結果**後，仍然可能為該遺傳疾病帶因者的剩餘機率 [SRC-003]。依據 ACMG 2021 實務指引，**任何帶因者篩檢的陰性結果都只能「降低」風險，絕不會消除所有風險；任何疾病的殘餘風險永遠不會是零** [SRC-003]。

## Key Concepts

- **基本計算公式（ACMG 2021）**：對於單一已知族群帶因頻率與檢測率的疾病，個體篩檢陰性後的殘餘帶因風險可估算為：
  $$\text{Residual Risk} = \text{Population Carrier Frequency} \times (1 - \text{Detection Rate})$$
  [SRC-003]
- **為何殘餘風險永遠不為零**：
  1. 任何分子檢測方法皆無法達到 100% 檢出率（部分深內含子變異、複雜結構重排、偽基因同源區或新發現罕見變異可能無法偵測）；
  2. 存在尚未被分類為致病性之意義不明變異（VUS）；
  3. 篩檢套組無法涵蓋人類所有數千種遺傳疾病，亦無法偵測新發突變（*de novo*）或非單基因異常 [SRC-003]。

## Detailed Explanation

在傳統針對單一高盛行率疾病的篩檢中，因族群帶因頻率與檢出率研究完整，實驗室常可計算出具體的殘餘風險數值 [SRC-003]。然而，當臨床採行同時分析數十至數百個基因的 [ECS（擴展性帶因者篩檢）](../products/ecs.md) 時，許多罕見疾病在各族群中的精確帶因頻率與真實檢測率尚未完全確立。

因此，ACMG 2021 明確指出：**在多基因同步篩檢（multiplex screening）獲得陰性結果後，實務上無法針對整組套組計算出一個精確的「整體殘餘風險」數值**，切忌以未經實證的單一百分比誤導受檢者 [SRC-003]。

### 解讀 iGene 官方表格「族群、帶因率與檢出率」的注意事項（SRC-009）
檢視愛生育銀行／送子鳥生殖中心 iGene 350 項疾病列表 [SRC-009] 可見實務上殘餘風險的具體來源：
- 表格所列單項檢出率介於 **76% 至 99%**（例如 *SMN1* 91%、*HBA1/HBA2* 90%、*DMD* 93%），顯示每項疾病篩檢陰性後皆存在不等程度之殘餘風險；
- **嚴禁將官網欄位之「檢出率」解讀為所有變異類型之統一分析敏感度**：官網檢驗限制已明示目標區間 NGS 無法偵測大片段基因缺失、插入、倒轉、重複性擴增、複雜結構異常、非目標區間、內含子與重複序列區域變異，亦無法排除新發突變與鑲嵌／體細胞突變 [SRC-009]；
- 清單中 284 筆採「一般人種」數據、60 筆並列雙族群、3 筆帶因率為 `-`，顯示跨族群帶因頻率與殘餘風險估算仍存在資料不完整性 [SRC-003] [SRC-009]。

## Clinical Relevance

- **檢前與檢後衛教核心**：醫療人員與遺傳諮詢師在解說 ECS 報告時，必須明確向受檢者傳達「陰性不等於零風險」，避免患者因誤解「檢測正常就完全不會生出遺傳病寶寶」而忽略必要的產前追蹤或家族史評估 [SRC-003]。
- **單方陽性、伴侶陰性之溝通**：當伴侶一方檢出為某體染色體隱性基因帶因者而另一方該基因篩檢陰性時，雖然胎兒罹病機率已顯著下降，仍應依該特定基因已知之檢出率與殘餘風險進行個別化 [Genetic Counseling（遺傳諮詢）](genetic-counseling.md) [SRC-003]。

## Limitations

- 不同種族與混血族群的基礎帶因頻率差異大，進一步限制了跨族群單一殘餘風險估計值的精準度 [SRC-003]。

## Related Pages

- [ECS 檢測產品頁](../products/ecs.md)
- [ECS 臨床實證與分層架構整合](../evidence/ecs-clinical-evidence.md)
- [Autosomal Recessive（體染色體隱性遺傳）](autosomal-recessive.md)
- [X-linked Inheritance（X 染色體性聯遺傳）](x-linked-inheritance.md)
- [FAQ：擴展性帶因者篩檢（ECS）結果陰性，代表寶寶完全不會得遺傳病嗎？](../faq/faq-ecs-negative-risk.md)

## Sources

- **[SRC-003]** Gregg AR et al.; ACMG (2021). *Screening for autosomal recessive and X-linked conditions during pregnancy and preconception: a practice resource of the ACMG*.
- **[SRC-009]** 愛生育銀行／送子鳥生殖中心（2026）. *iGene 遺傳疾病帶因篩檢列表與產品介紹*（`https://www.icryobank.com/gene/igene-disease-list`、`https://www.icryobank.com/gene/igene`）。
