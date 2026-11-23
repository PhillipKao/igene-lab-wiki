---
title: "Copy Number Variation（拷貝數變異 / CNV）"
category: "concepts"
summary: "說明基因體拷貝數變異（CNV）與染色體劑量分析的原理，以及在 PGT-A 與 PGT-SR 中透過 NGS、aCGH 與 SNP Array 偵測染色體增減時的解析度與技術限制。"
source_ids:
  - "SRC-004"
  - "SRC-006"
created_at: "2026-11-23"
updated_at: "2026-11-23"
review_status: "auto_compiled"
related_pages:
  - "aneuploidy.md"
  - "structural-chromosomal-rearrangement.md"
  - "../products/pgt-a.md"
  - "../products/pgt-sr.md"
---

# Copy Number Variation（拷貝數變異 / CNV）

## Overview

**Copy Number Variation（拷貝數變異，簡稱 CNV）**係指基因體特定 DNA 片段相較於正常二倍體參考序列出現**拷貝數增加（重複，duplication / gain）**或**拷貝數減少（缺失，deletion / loss）**的變異 [SRC-004]。在胚胎著床前遺傳檢測中，拷貝數分析（Copy Number Analysis）是 [PGT-A](../products/pgt-a.md) 與 [PGT-SR](../products/pgt-sr.md) 偵測整條染色體非整倍體及染色體節段不平衡的核心技術基礎 [SRC-004]。

## Key Concepts

- **全染色體 vs. 節段性拷貝數改變**：整條染色體增減屬於全染色體 [Aneuploidy](aneuploidy.md)；若僅涉及染色體某一段落之缺失或重複，則為節段性拷貝數變異（segmental CNV / imbalance），可能源於偶發事件或父母的 [Structural Chromosomal Rearrangement（染色體結構重排）](structural-chromosomal-rearrangement.md) [SRC-004]。
- **偵測技術與解析度差異（ESHRE 2020 一般參考）**：
  - **NGS**：依據各基因體區間（bin）的定序讀數分布量化拷貝數 [SRC-004]。
  - **寡核苷酸 aCGH**：利用檢體與參考 DNA 的螢光比值（$\log_2$ ratio），商業平台一般解析度約 **5–10 Mb** [SRC-004]。
  - **SNP Array**：商業平台一般解析度約 **2.4–5 Mb**，並額外提供基因分型資訊 [SRC-004]。
  - 在單基因大型缺失情境（ASRM 2023 提及通常需至少大於 **3–5 Mb**），部分實驗室才可能透過 PGT-A/PGT-SR 拷貝數方法直接偵測，否則須依靠 [PGT-M](../products/pgt-m.md) 連鎖分析 [SRC-006]。

## Detailed Explanation

於胚胎切片檢體執行拷貝數分析前，必須先經細胞裂解與全基因體放大（Whole Genome Amplification, WGA），將極微量的細胞 DNA 擴增至足以進行晶片雜交或 NGS 建庫的濃度 [SRC-004]。WGA 過程的均勻度直接影響拷貝數圖譜的訊雜比（signal-to-noise ratio），因此實驗室必須針對各步驟建立標準實驗條件並以已知基因型細胞完成臨床前準確度驗證 [SRC-004]。

## Clinical Relevance

- 拷貝數分析讓實驗室能在單一測試中全面掃描 24 條染色體，相較於傳統僅能檢測少數探針位點的 FISH 技術，大幅提高染色體結構重排與數目異常的評估廣度 [SRC-004]。
- 當 PGT-A 意外發現重複出現於多顆胚胎的相同節段性 CNV 時，臨床上應評估父母是否為未知的平衡性染色體結構重排帶因者 [SRC-004]。

## Limitations

- **解析度下限**：小於實驗室驗證門檻之微缺失／微重複無法穩定檢出 [SRC-004]。
- **僅偵測「劑量改變」**：標準無基因分型之拷貝數分析無法偵測無 DNA 淨增減之平衡性轉位、倒位、單基因點突變或單親二體（UPD）[SRC-004]。

## Related Pages

- [Aneuploidy（染色體非整倍體）](aneuploidy.md)
- [Structural Chromosomal Rearrangement（染色體結構重排）](structural-chromosomal-rearrangement.md)
- [PGT-A 檢測產品頁](../products/pgt-a.md)
- [PGT-SR 檢測產品頁](../products/pgt-sr.md)

## Sources

- **[SRC-004]** ESHRE PGT-SR/PGT-A Working Group (2020). *ESHRE PGT Consortium good practice recommendations for the detection of structural and numerical chromosomal aberrations*.
- **[SRC-006]** ASRM Practice Committee & GCPG (2023). *Indications and management of preimplantation genetic testing for monogenic conditions: a committee opinion*.
