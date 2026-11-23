---
title: "FAQ：ECS / iGene 遺傳疾病帶因篩檢與 NGS 實驗室常見問題"
category: "faq"
summary: "整合 ACMG 2021（SRC-003）、iGene 官方產品與疾病列表（SRC-009）及實驗室 Thermo Fisher NGS 平台確認資訊，以白話回答帶因者篩檢常見疑問、350 種疾病與基因數差異、檢驗限制與新生兒篩檢必要性。"
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
  - "../concepts/residual-risk.md"
  - "../concepts/autosomal-recessive.md"
  - "../concepts/x-linked-inheritance.md"
  - "../laboratory/ngs-technology.md"
  - "faq-ecs-negative-risk.md"
---

# FAQ：ECS / iGene 遺傳疾病帶因篩檢與 NGS 實驗室常見問題

> **審核狀態提示**：本頁已整合 `SRC-003`（ACMG 2021）與 `SRC-009`（iGene 官方資料，標記 `source_verified`、`product_spec_verified`），惟涉及患者風險溝通與實驗室細節，整頁仍維持 `pending_clinical_review` 與 `pending_technical_verification`。

## Question

準備懷孕或懷孕初期考慮做 **iGene 擴展性帶因者篩檢（ECS）**，大家最常問哪些問題？包含「350 種疾病是否等於 350 個基因」、「夫妻需不需要同時檢測」、「檢驗有哪些限制」、「驗完陰性還需要做新生兒篩檢嗎」以及「實驗室使用哪種 NGS 平台」？

## Short Answer

- **iGene** 是針對血液檢體 DNA 以次世代定序（NGS）進行的擴展性帶因者篩檢，官網標示涵蓋 **15 大類、350 種遺傳疾病（實測擷取對應 351 個去重獨立基因，內含 28 個 X 性聯遺傳基因）**[SRC-009]。
- **ECS 是帶因者篩檢，不是所有遺傳疾病的完整診斷**，也絕無法「保證生下健康寶寶」；陰性結果仍存在 [Residual Risk（殘餘風險）](../concepts/residual-risk.md)，寶寶出生後仍建議接受常規新生兒篩檢 [SRC-003] [SRC-009]。
- 本實驗室已確認使用 **Thermo Fisher Scientific / Ion Torrent NGS** 定序技術，且 **ECS（iGene）採用 `530`（Ion 530）晶片**（與 PGT-A 採用 `520` 晶片不同），但**不可假定所有產品共用相同定序儀、流程或分析方法**；ECS 之具體設備型號、覆蓋深度、各變異類型分析靈敏度／特異度與報告週期（TAT）等仍列為 `Pending Technical Verification`。

## Detailed Explanation

### Q1：官網說 iGene 篩檢「350 種遺傳疾病」，這等於「350 個基因」嗎？
**不完全等同。** 依據完整擷取自 [SRC-009] 的官方疾病列表，350 筆疾病條目中，第 239 筆甲型地中海型貧血同時對應 `HBA1/HBA2` 兩個基因，因此實際去重後共對應 **351 個獨立基因符號**（詳見 [ECS 疾病與基因索引頁](../products/ecs-disease-gene-index.md)）。此外，基因數或疾病數的多寡本身不代表檢出率 100%，仍需檢視涵蓋哪些關鍵疾病與檢測限制 [SRC-003] [SRC-009]。

### Q2：家族沒有遺傳病史，為什麼還需要討論帶因者篩檢？夫妻需要一起驗嗎？
- 大多數 [Autosomal Recessive（體染色體隱性遺傳）](../concepts/autosomal-recessive.md) 帶因者本身完全健康、沒有任何症狀，因此家族中往往沒有過往病史 [SRC-003] [SRC-009]。
- **建議優先於備孕前（preconception）評估**：ACMG 2021 指出孕前篩檢可保留最完整的生育選項且壓力較低 [SRC-003]。
- **同步 vs. 序貫檢測**：夫妻同時檢測可縮短等待時間（特別是已懷孕或備孕時程較緊時）；若備孕時間充裕，也可由一方先驗，若檢出隱性帶因再請另一半針對對應基因檢測 [SRC-003] [SRC-009]。

### Q3：如果檢出夫妻同基因帶因，或女性為 X 性聯疾病帶因者怎麼辦？
應先接受專業 [Genetic Counseling（遺傳諮詢）](../concepts/genetic-counseling.md)，依個人價值觀與家庭狀況評估多元選擇，包含：
- **備孕前**：自然懷孕搭配產前診斷、透過試管嬰兒（IVF）結合客製化 [PGT-M（單基因胚胎檢測）](../products/pgt-m.md)、配子（卵子／精子）受贈或領養等 [SRC-003] [SRC-006] [SRC-009]；
- **已懷孕中**：討論絨毛採樣或羊膜穿刺等確認性產前基因檢測 [SRC-003] [SRC-009]。

### Q4：iGene（NGS）有哪些檢驗限制？為什麼不能偵測所有遺傳疾病？
依據 ACMG 2021（[SRC-003]）與 iGene 官方檢驗限制說明（[SRC-009]）：
1. **特定變異類型限制**：目標區間 NGS **無法偵測大片段基因缺失、插入、倒轉、重複性擴增（如三核苷酸重複疾病 *FMR1* X 染色體脆折症，亦未列於 iGene 350 項清單中）或其他複雜結構異常** [SRC-003] [SRC-009]。
2. **非目標區間與內含子變異**：若致病變異位於檢測列表目標區間以外或深層內含子（intron）區域，可能無法檢出 [SRC-009]。
3. **無法篩檢新發突變與鑲嵌突變**：無法偵測受精後才發生的新發突變（*de novo*）、鑲嵌細胞或體細胞突變，亦不等同染色體數目篩檢（[PGT-A](../products/pgt-a.md)）[SRC-003] [SRC-009]。
4. **檢出率非 100%**：官方列表標示之單項檢出率介於 76%–99%，陰性結果僅代表風險大幅降低而非零風險（另見 [ECS 陰性殘餘風險專題 FAQ](faq-ecs-negative-risk.md)）[SRC-003] [SRC-009]。

### Q5：夫妻雙方都做完 ECS 且陰性，寶寶出生後還需要做新生兒篩檢嗎？
**仍然強烈建議進行。** 即使套組涵蓋多數常見先天性代謝異常，仍無法排除未在套組內的遺傳病、新發突變或檢測技術限制範圍內的變異，因此出生後常規新生兒篩檢不可或缺 [SRC-003] [SRC-009]。

### Q6：實驗室是使用哪一種 NGS 設備進行檢測？
已確認本實驗室使用 **Thermo Fisher Scientific** 之 **Ion Torrent NGS** 定序技術，其中 **ECS（iGene）使用 `530`（Ion 530）晶片**、**PGT-A 使用 `520`（Ion 520）晶片**（詳見分產品技術管理頁 [NGS Technology](../laboratory/ngs-technology.md)）。需特別說明的是，不同檢測產品（ECS、PGT-A、PGT-SR、PGT-M）**不可假定共用相同機型、實驗流程或分析方法**，亦不得以原廠一般性能規格取代本實驗室實際驗證結果；具體儀器型號、ECS 定序覆蓋深度、各變異類型分析靈敏度／特異度、Low-VAF 偵測下限、報告週期（TAT）及認證狀態均仍屬 `Pending Technical Verification`。

## Related Topics

- [ECS（擴展性帶因者篩檢 / iGene）產品主頁](../products/ecs.md)
- [ECS 疾病與基因結構化索引（350 項疾病 / 351 個基因）](../products/ecs-disease-gene-index.md)
- [FAQ：ECS 結果陰性代表零風險嗎？](faq-ecs-negative-risk.md)
- [Residual Risk（殘餘風險）](../concepts/residual-risk.md)
- [NGS Technology（次世代定序技術與平台）](../laboratory/ngs-technology.md)

## Sources

- **[SRC-003]** Gregg AR, Aarabi M, Klugman S, et al.; ACMG (2021). *Screening for autosomal recessive and X-linked conditions during pregnancy and preconception: a practice resource of the ACMG*. Genetics in Medicine, 23(10):1793–1806.
- **[SRC-006]** Practice Committees of ASRM & GCPG (2023). *Indications and management of preimplantation genetic testing for monogenic conditions: a committee opinion*.
- **[SRC-009]** 愛生育銀行／送子鳥生殖中心（2026）. *iGene 遺傳疾病帶因篩檢官方產品頁與完整疾病列表*（`https://www.icryobank.com/gene/igene`、`https://www.icryobank.com/gene/igene-disease-list`）。

## Last Updated

- **2026-11-23**
