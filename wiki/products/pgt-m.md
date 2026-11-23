---
title: "PGT-M（胚胎著床前單基因遺傳疾病檢測 / Preimplantation Genetic Testing for Monogenic Conditions）"
category: "products"
summary: "介紹 PGT-M 的臨床適應症與不建議項目、客製化事前探針建立（Preclinical Work-up）、單倍型分析（Haplotyping）、等位基因脫落（ADO）風險控管與產前確認原則，整合 ASRM 2023 與 ESHRE 2020 指引。"
source_ids:
  - "SRC-001"
  - "SRC-005"
  - "SRC-006"
  - "SRC-007"
  - "SRC-008"
created_at: "2026-11-23"
updated_at: "2026-11-23"
review_status: "pending_clinical_review"
review_layers:
  - "source_verified"
  - "pending_clinical_review"
  - "pending_technical_verification"
related_pages:
  - "../concepts/monogenic-disease.md"
  - "../concepts/autosomal-recessive.md"
  - "../concepts/x-linked-inheritance.md"
  - "../concepts/haplotyping.md"
  - "../concepts/allele-dropout.md"
  - "../concepts/embryo-biopsy.md"
  - "../concepts/genetic-counseling.md"
  - "../evidence/pgt-m-sr-evidence.md"
  - "ecs.md"
  - "../laboratory/pgt-workflow.md"
  - "../laboratory/ngs-technology.md"
  - "../faq/faq-pgt-a-vs-pgt-sr-vs-pgt-m.md"
  - "../faq/faq-prenatal-testing-after-pgt.md"
---

# PGT-M（胚胎著床前單基因遺傳疾病檢測）

> **審核狀態提示**：本頁涉及 PGT-M 臨床適應症、爭議性與不建議項目、技術驗證與患者決策建議，目前為 `pending_clinical_review`。文中關於檢測策略與驗證流程為依據 ASRM 2023 與 ESHRE 2020 指引整理之**一般性專業知識**，本實驗室實際 PGT-M 客製化開發週期與技術平台**待確認本實驗室實際規格**。

## 1. 檢測介紹

**PGT-M**（Preimplantation Genetic Testing for Monogenic Conditions，胚胎著床前單基因遺傳疾病檢測）是針對已知帶有特定 [Monogenic Disease（單基因遺傳疾病）](../concepts/monogenic-disease.md) 致病變異的家庭，於試管嬰兒（IVF）胚胎植入前檢測目標基因位點及周邊遺傳標記，以降低子代遺傳特定單基因疾病的風險 [SRC-005] [SRC-006]。

PGT-M 屬於高度客製化之單基因檢測，通常須於進入 IVF 週期前先由遺傳實驗室完成個案審核與專屬檢測設計（preclinical work-up），與篩檢整條染色體數目的 [PGT-A](pgt-a.md) 及針對染色體結構重排的 [PGT-SR](pgt-sr.md) 截然不同 [SRC-005] [SRC-006]。

## 2. 適用對象

依據 ASRM 2023 委員會意見，當確認存在**顯著單基因遺傳疾病生育風險**時，應提供 PGT-M 作為自願選擇項目之一（患者可自由決定是否接受）[SRC-006]：

- **傳統／兒童期發病之嚴重單基因疾病**：包含體染色體隱性（雙方帶因，見 [Autosomal Recessive](../concepts/autosomal-recessive.md)）、體染色體顯性及 [X-linked Inheritance（X 染色體性聯遺傳）](../concepts/x-linked-inheritance.md) 疾病（如透過 [ECS](ecs.md) 或家族診斷確認之明確致病變異）[SRC-006]。
- **嚴重成人期發病疾病與遺傳性癌症易感症候群**：如部分高外顯率神經退化疾病或遺傳性癌症基因變異，需充分討論外顯率、發病年齡與倫理考量（部分情況亦涉及不揭露檢測／exclusion testing）[SRC-005] [SRC-006]。
- **特殊臨床情境**：如人類白血球抗原（HLA）配對需求、粒線體 DNA 致病變異或新發（*de novo*）突變等，需依據 ESHRE 2020 特殊規範個別評估可行性 [SRC-005]。
- **ASRM 2023 明確不建議提供 PGT-M 的情境**：
  - 僅為排除**無臨床表現之體染色體隱性帶因狀態**（carrier status without manifestations of symptoms）；
  - 與疾病無關之變異組合；
  - 偽缺乏等位基因（pseudodeficiency alleles）；
  - 僅存於體細胞之非生殖系變異（somatic-only variants）[SRC-006]。

## 3. 檢測原理

由於胚胎切片僅含單一或少量細胞（囊胚滋養外胚層約 5–10 個細胞），DNA 起始量極低，單獨直接偵測致病變異點容易因 [Allele Dropout（等位基因脫落 / ADO）](../concepts/allele-dropout.md) 導致誤診 [SRC-005]。因此，現代 PGT-M 的核心原則是**結合直接變異偵測與間接連鎖分析（[Haplotyping / 單倍型分析](../concepts/haplotyping.md)）** [SRC-005] [SRC-006]：

- **多重 PCR 結合 STR 標記（Multiplex PCR + STR）**：同步擴增致病位點（或單純連鎖）與位於基因上下游具資訊性的短串聯重複序列（STR）標記，以追蹤高風險與低風險單倍型，並偵測 ADO、基因重組（recombination）及外源 DNA 污染 [SRC-005]。
- **全基因體放大（WGA）結合 SNP Array 或 NGS 連鎖分析**：透過高密度 SNP 標記建構父母與家族之單倍型相位（karyomapping / SNP haplotyping / targeted NGS），於部分平台亦可同時評估非整倍體 [SRC-005]。
- **粒線體 DNA 疾病例外**：因粒線體遺傳特性無法單靠核基因連鎖，必須直接檢測致病變異與異質性（heteroplasmy）比例 [SRC-005]。

> **本實驗室 PGT-M 技術規格現況（獨立管理，`Pending Technical Verification`）**：本實驗室已確認使用 Thermo Fisher Scientific / Ion Torrent NGS 定序技術，但**不可假定 PGT-M 與 PGT-A、PGT-SR 或 ECS 共用相同定序儀、晶片、流程或分析方法**（詳見 [NGS Technology](../laboratory/ngs-technology.md)）。PGT-M 實際採用平台（如 PCR/STR、SNP Array 或 Targeted NGS）、Coverage（若採 NGS）、分析靈敏度／特異度、事前客製化開發週期與報告週期（TAT）均列為 **`Pending Technical Verification`**。

## 4. 檢測流程

1. **個案審核與檢測前遺傳諮詢（Pretest Counseling）**：確認致病變異報告之臨床致病性（pathogenic / likely pathogenic）、遺傳模式與完整生育選項（含自然懷孕搭配產前診斷、配子捐贈等）[SRC-006] [SRC-007]。
2. **客製化事前建置與家族連鎖分析（Preclinical Work-up）**：收集伴侶及必要親屬（如已確診家人或雙方父母）DNA 檢體，進行標記資訊性測試、建立高／低風險單倍型相位並完成實驗室驗證；**應於啟動 IVF 療程前完成** [SRC-005] [SRC-006]。
3. **IVF 療程、胚胎切片與冷凍**：完成受精與囊胚培養後進行滋養外胚層切片（[Embryo Biopsy](../concepts/embryo-biopsy.md)）、嚴格防污染清洗裝管（Tubing）及玻璃化冷凍 [SRC-008]。（註：ASRM 2024 提及許多實驗室在 PGT-M 採行單一精蟲顯微注射 ICSI 以降低殘留精蟲 DNA 污染疑慮 [SRC-001] [SRC-008]。）
4. **胚胎檢體基因分析與品管審查**：同步判讀致病位點與上下游連鎖標記，確認無 ADO、污染或重組干擾，經獨立複核簽發報告 [SRC-005] [SRC-007]。
5. **檢測後諮詢、胚胎植入與產前確認**：依結果挑選未受影響之胚胎植入；懷孕後強烈建議討論確認性產前診斷 [SRC-006] [SRC-007]。

## 5. 結果解讀

- **Unaffected / Non-carrier（未罹病且未帶因）**：未遺傳高風險單倍型與致病變異，通常列為優先植入考量 [SRC-005] [SRC-006]。
- **Unaffected Carrier（未罹病之隱性帶因胚胎）**：對於體染色體隱性遺傳疾病，僅帶有單一等位基因變異之胚胎通常不會發病，臨床上常視為可植入選項（須於檢測前與夫妻達成共識）[SRC-006]。
- **Affected（預期罹病／帶有高風險單倍型）**：遺傳致病變異組合，通常不建議植入 [SRC-005] [SRC-006]。
- **Inconclusive / Recombination / ADO（無法判讀或檢出重組）**：若在目標基因附近發生染色體互換重組、嚴重等位基因脫落或外源污染，可能無法確認真實基因型，須經遺傳諮詢個別評估 [SRC-005]。

## 6. 臨床應用

- 協助具明確單基因遺傳疾病風險的家庭大幅降低子代罹患目標遺傳疾病的機率 [SRC-006]。
- 透過生殖中心駐點遺傳諮詢師與 PGT 實驗室遺傳諮詢師的跨團隊合作，可提升複雜個案（如新發突變、三核苷酸重複疾病或大型基因缺失）的流程順暢度與患者決策品質 [SRC-006]。

## 7. 檢測限制

1. **並非所有變異皆具技術可行性**：以下情境可能使家族連鎖難以建立或檢測設計高度困難，甚至無法執行 PGT-M [SRC-005] [SRC-006]：
   - 缺乏可配合採檢之關鍵親屬（無法定相）；
   - 致病變異為新發突變（*de novo*）或受檢者為體細胞鑲嵌／嵌合體／曾接受骨髓移植；
   - 父母雙方攜帶相同變異或有近親聯姻、非預期血緣關係；
   - 特殊基因結構：如**三核苷酸重複擴增疾病**（*FMR1* 脆折症、*HTT* 亨丁頓舞蹈症、*DMPK*/*CNBP* 強直性肌營養不良等，常須高度依賴家族連鎖）、**大型基因缺失**、偽基因（pseudogene）干擾或 GC 含量極高區域 [SRC-006]。
2. **微誤診風險無法完全歸零**：受限於 [Allele Dropout](../concepts/allele-dropout.md)、基因重組、外源 DNA 污染或胚胎鑲嵌等生物與技術因素，仍存在極低誤診可能 [SRC-005] [SRC-006]。
3. **只針對指定單基因**：單純 PGT-M 不涵蓋其他未指定之單基因疾病、偶發染色體非整倍體（除非合併 [PGT-A](pgt-a.md)）或非遺傳性先天結構異常 [SRC-006]。
4. **必須提供產前確認檢測**：ASRM 2023 明確建議，經由 PGT-M 懷孕者皆應提供產前診斷檢測，以確認胚胎檢測結果並篩檢其他與 PGT-M 適應症無關之胎兒異常 [SRC-006]。

## 8. 相關衛教 FAQ

- [PGT-A、PGT-SR 與 PGT-M 有什麼差別？我需要做哪一種？](../faq/faq-pgt-a-vs-pgt-sr-vs-pgt-m.md)
- [胚胎切片（Embryo Biopsy）會傷害胚胎嗎？為什麼切片後通常要先冷凍？](../faq/faq-embryo-biopsy-safety.md)
- [已經做了 PGT-A、PGT-SR 或 PGT-M，懷孕後還需要做產前檢查嗎？](../faq/faq-prenatal-testing-after-pgt.md)

## 9. 相關文獻（Sources）

- **[SRC-005]** ESHRE PGT-M Working Group, Carvalho F et al. (2020). *ESHRE PGT Consortium good practice recommendations for the detection of monogenic disorders*. Human Reproduction Open, 2020(3):hoaa018. DOI: `10.1093/hropen/hoaa018`
- **[SRC-006]** Practice Committees of ASRM & Genetic Counseling Professional Group (2023). *Indications and management of preimplantation genetic testing for monogenic conditions: a committee opinion*. Fertility and Sterility, 120(1):61–71. DOI: `10.1016/j.fertnstert.2023.03.003`
- **[SRC-007]** ESHRE PGT Consortium Steering Committee, Carvalho F et al. (2020). *ESHRE PGT Consortium good practice recommendations for the organisation of PGT*. Human Reproduction Open, 2020(3):hoaa021. DOI: `10.1093/hropen/hoaa021`
- **[SRC-008]** ESHRE PGT Consortium and SIG-Embryology Biopsy Working Group, Kokkali G et al. (2020). *ESHRE PGT Consortium and SIG Embryology good practice recommendations for polar body and embryo biopsy for PGT*. Human Reproduction Open, 2020(3):hoaa020. DOI: `10.1093/hropen/hoaa020`

## 10. 最後更新日期

- **最後更新**：2026-11-23（初次整合 `SRC-005`、`SRC-006`、`SRC-007`、`SRC-008`）
