---
title: "Haplotyping（單倍型分析／連鎖分析）"
category: "concepts"
summary: "介紹單倍型分析（Haplotyping / Linkage Analysis）在 PGT-M 與高階 PGT-SR 中的分子原理、家族定相（Phase Determination）、資訊性標記（STR / SNP）選擇與技術限制。"
source_ids:
  - "SRC-004"
  - "SRC-005"
  - "SRC-006"
created_at: "2026-11-23"
updated_at: "2026-11-23"
review_status: "auto_compiled"
related_pages:
  - "allele-dropout.md"
  - "monogenic-disease.md"
  - "structural-chromosomal-rearrangement.md"
  - "../products/pgt-m.md"
  - "../products/pgt-sr.md"
---

# Haplotyping（單倍型分析／連鎖分析）

## Overview

**Haplotyping（單倍型分析）**，臨床亦常稱為**連鎖分析（Linkage Analysis）**，是指透過分析目標基因（或染色體重排斷裂點）上下游緊密連鎖的多態性遺傳標記（如短串聯重複序列 STR 或單核苷酸多態性 SNP），追蹤特定高風險與低風險染色體片段在家族中的遺傳去向 [SRC-005]。

## Key Concepts

- **為何在 PGT-M 中至關重要**：胚胎切片僅含單一或少量細胞，直接擴增致病突變位點時容易發生 [Allele Dropout（等位基因脫落 / ADO）](allele-dropout.md)；同時追蹤目標基因兩側的連鎖單倍型，可在直接檢測失敗或出現 ADO 時提供交叉驗證，並偵測外源 DNA 污染、染色體拷貝數異常與基因重組 [SRC-005]。
- **定相（Phase Determination）**：於事前建置（preclinical work-up）階段，實驗室須比對夫妻及已知遺傳狀態之親屬（通常至少需一位一等親）DNA，確認哪一組上下游標記組合與致病變異位於同一條染色體上（即高風險單倍型）[SRC-005] [SRC-006]。
- **標記資訊性（Informativity）**：
  - **完全資訊性（Fully Informative）**：父母四條染色體對偶基因的標記型別皆可區分，最能明確判定胚胎基因型並偵測 ADO、污染與重組 [SRC-005]。
  - **部分資訊性／無資訊性**：無法區分所有胚胎基因型，偵錯能力相對受限 [SRC-005]。

## Detailed Explanation

### 1. STR 多重 PCR 連鎖 vs. SNP Array / NGS 單倍型
- **STR 標記**：選擇緊鄰目標基因上下游（flanking）之多態性 STR 標記進行多重 PCR，但雙核苷酸重複（dinucleotide repeats）之 STR 可能出現 stutter 訊號而增加判讀難度 [SRC-005]。
- **SNP Array / NGS 單倍型**：經由全基因體放大（WGA）後分析全基因體或目標區段數十萬個 SNP 標記，建構高密度單倍型（如 Karyomapping 或 NGS-based haplotyping），可減少個別疾病重複設計引子的時間，且於特定 [PGT-SR](../products/pgt-sr.md) 案例中有機會進一步區分「正常胚胎」與「平衡重排帶因胚胎」[SRC-004] [SRC-005]。

### 2. 無法建立傳統家族連鎖的困難情境
依據 ASRM 2023 與 ESHRE 2020 指引，以下情況可能導致事前無法建立家族單倍型相位，大幅提高 PGT-M 技術難度 [SRC-005] [SRC-006]：
- 無法取得已知遺傳狀態親屬之 DNA 檢體；
- 致病變異屬於新發突變（*de novo*）；
- 受檢者為體細胞鑲嵌／嵌合體或曾接受骨髓移植；
- 父母雙方攜帶相同變異或存在近親聯姻（consanguinity）導致同合子區段多、具資訊性標記稀少；
- 非預期生物血緣關係（nonparentage）[SRC-006]。

部分情境若能直接偵測致病變異，實驗室可能於檢測階段利用受檢胚胎本身之切片資料推算定相，但成功判讀常仰賴足夠數量的胚胎呈現突變單倍型 [SRC-006]。

## Clinical Relevance

- 對於三核苷酸重複擴增疾病（如 *FMR1* 脆折症、*HTT* 亨丁頓舞蹈症、*DMPK*/*CNBP* 強直性肌營養不良）或大型基因缺失，直接定量重複次數常面臨技術限制，**高度依賴家族單倍型連鎖分析**完成 [PGT-M](../products/pgt-m.md) [SRC-006]。

## Limitations

- 若減數分裂過程中在目標基因與連鎖標記之間發生**染色體互換重組（recombination）**，且缺乏另一側資訊性標記或直接位點結果佐證，可能導致胚胎判讀為「無法確定（inconclusive）」[SRC-005]。

## Related Pages

- [Allele Dropout（等位基因脫落）](allele-dropout.md)
- [Monogenic Disease（單基因遺傳疾病）](monogenic-disease.md)
- [PGT-M 檢測產品頁](../products/pgt-m.md)
- [PGT-SR 檢測產品頁](../products/pgt-sr.md)
- [PGT-M 與 PGT-SR 國際指引與技術實證整合](../evidence/pgt-m-sr-evidence.md)

## Sources

- **[SRC-004]** ESHRE PGT-SR/PGT-A Working Group (2020). *ESHRE PGT Consortium good practice recommendations for the detection of structural and numerical chromosomal aberrations*.
- **[SRC-005]** ESHRE PGT-M Working Group (2020). *ESHRE PGT Consortium good practice recommendations for the detection of monogenic disorders*.
- **[SRC-006]** ASRM Practice Committee & GCPG (2023). *Indications and management of preimplantation genetic testing for monogenic conditions: a committee opinion*.
