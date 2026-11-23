---
title: "Allele Dropout（等位基因脫落 / ADO）"
category: "concepts"
summary: "說明胚胎單細胞或少量細胞 DNA 擴增時可能發生的等位基因脫落（ADO）現象、造成 PGT-M 誤診的風險機制，以及透過囊胚多細胞切片與雙側單倍型連鎖分析降低風險的防禦策略。"
source_ids:
  - "SRC-005"
  - "SRC-006"
  - "SRC-008"
created_at: "2026-11-23"
updated_at: "2026-11-23"
review_status: "auto_compiled"
related_pages:
  - "haplotyping.md"
  - "embryo-biopsy.md"
  - "monogenic-disease.md"
  - "../products/pgt-m.md"
---

# Allele Dropout（等位基因脫落 / ADO）

## Overview

**Allele Dropout（等位基因脫落，簡稱 ADO）**係指在對單一細胞或極微量 DNA 進行聚合酶連鎖反應（PCR）或全基因體放大（WGA）時，原本異合子（heterozygous，帶有兩個不同等位基因）的檢體中，**其中一個等位基因未能成功擴增或未被偵測到**，導致結果表面上呈現假性同合子（false homozygosity）的技術現象 [SRC-005]。

## Key Concepts

- **為何容易發生在 PGT-M**：[PGT-M](../products/pgt-m.md) 的起始檢體僅來自胚胎切片的單一細胞（極體或分裂期卵裂球）或 5–10 個囊胚滋養外胚層細胞，微量 DNA 擴增本身即存在隨機放大失敗風險 [SRC-005] [SRC-008]。
- **潛在誤診機制**：
  - 在**體染色體顯性遺傳疾病**中，若致病等位基因發生 ADO，帶有致病突變的異合子胚胎可能被誤判為完全正常的同合子胚胎，造成嚴重臨床誤診 [SRC-005]。
  - 在**體染色體隱性遺傳疾病**中，若正常等位基因發生 ADO，無症狀帶因胚胎可能被誤判為罹病胚胎（導致可用胚胎減少）；若複合異合子（compound heterozygous）胚胎中一個致病等位基因脫落，亦可能被誤判為僅為單一帶因者 [SRC-005]。

## Detailed Explanation

依據 ESHRE 2020 PGT-M 技術指引與胚胎切片指引，現代遺傳實驗室透過多層防線控管 ADO 風險 [SRC-005] [SRC-008]：
1. **改採囊胚滋養外胚層切片（TE Biopsy）**：相較於單一卵裂球，囊胚切片取得約 5–10 個細胞，DNA 起始量大幅提升，有助於降低擴增失敗與 ADO 發生率 [SRC-005] [SRC-008]。
2. **結合雙側連鎖單倍型分析（[Haplotyping](haplotyping.md)）**：不單獨仰賴致病點位之直接放大，而是在目標基因上下游同步納入具資訊性的 STR 或 SNP 標記；即使致病位點發生 ADO，周邊連鎖標記仍能揭露高風險染色體的存在並偵測出 ADO 事件 [SRC-005]。
3. **嚴謹的事前驗證與反應管品管**：在臨床前驗證階段使用少量細胞或低濃度 DNA 測試擴增效率與 ADO 率，並於正式檢測時搭配空白對照與陽性對照組，確保結果可靠度 [SRC-005] [SRC-008]。

## Clinical Relevance

- ADO 是為何 [PGT-M](../products/pgt-m.md) 需要花費數週進行客製化事前家族連鎖建置（preclinical work-up），且懷孕後仍建議進行產前確認性診斷的核心技術原因之一 [SRC-005] [SRC-006]。

## Limitations

- 即使合併多點連鎖標記與囊胚切片，ADO 與重組交互發生時仍可能導致極少數胚胎無法作出確定判讀 [SRC-005]。

## Related Pages

- [Haplotyping（單倍型分析）](haplotyping.md)
- [Embryo Biopsy（胚胎切片）](embryo-biopsy.md)
- [PGT-M 檢測產品頁](../products/pgt-m.md)
- [PGT-M 與 PGT-SR 國際指引與技術實證整合](../evidence/pgt-m-sr-evidence.md)

## Sources

- **[SRC-005]** ESHRE PGT-M Working Group (2020). *ESHRE PGT Consortium good practice recommendations for the detection of monogenic disorders*.
- **[SRC-006]** ASRM Practice Committee & GCPG (2023). *Indications and management of preimplantation genetic testing for monogenic conditions: a committee opinion*.
- **[SRC-008]** ESHRE PGT Consortium & SIG-Embryology Biopsy Working Group (2020). *ESHRE PGT Consortium and SIG Embryology good practice recommendations for polar body and embryo biopsy for PGT*.
