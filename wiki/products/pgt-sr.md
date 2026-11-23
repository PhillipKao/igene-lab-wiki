---
title: "PGT-SR（胚胎著床前染色體結構重排檢測 / Preimplantation Genetic Testing for Structural Rearrangements）"
category: "products"
summary: "介紹 PGT-SR 的檢測對象、平衡轉位與羅伯遜轉位等結構重排之減數分裂風險、NGS / aCGH / SNP array / FISH 檢測原理、解析度限制與產前確認原則，整合 ESHRE 2020 指引。"
source_ids:
  - "SRC-002"
  - "SRC-004"
  - "SRC-005"
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
  - "../concepts/structural-chromosomal-rearrangement.md"
  - "../concepts/copy-number-variation.md"
  - "../concepts/aneuploidy.md"
  - "../concepts/embryo-biopsy.md"
  - "../concepts/haplotyping.md"
  - "../concepts/genetic-counseling.md"
  - "../evidence/pgt-m-sr-evidence.md"
  - "../laboratory/pgt-workflow.md"
  - "../laboratory/ngs-technology.md"
  - "../faq/faq-pgt-a-vs-pgt-sr-vs-pgt-m.md"
  - "../faq/faq-prenatal-testing-after-pgt.md"
---

# PGT-SR（胚胎著床前染色體結構重排檢測）

> **審核狀態提示**：本頁涉及染色體結構重排之臨床適用性、解析度與技術限制，目前為 `pending_clinical_review`。文中關於各平台解析度與作業規格為依據 ESHRE 2020 指引整理之**一般性專業知識**，本實驗室實際使用之 PGT-SR 平台、最小偵測片段大小與是否具區分平衡帶因能力**待確認本實驗室實際規格**。

## 1. 檢測介紹

**PGT-SR**（Preimplantation Genetic Testing for Structural Rearrangements，胚胎著床前染色體結構重排檢測）專為**夫妻任一方已知帶有染色體結構異常**（詳見 [Structural Chromosomal Rearrangement（染色體結構重排）](../concepts/structural-chromosomal-rearrangement.md)）所設計，目的是在胚胎植入前辨識因減數分裂異常分離所產生的**染色體不平衡（unbalanced）胚胎**，並優先挑選染色體劑量平衡（正常或平衡重排帶因）的胚胎進行植入 [SRC-004]。

PGT-SR 的重點是針對**已知家族性結構重排片段**進行風險評估與偵測，與全面篩檢偶發整條染色體數目異常的 [PGT-A](pgt-a.md) 及針對單基因致病變異的 [PGT-M](pgt-m.md) 有明確區隔 [SRC-004] [SRC-007]。

## 2. 適用對象

- **平衡性相互轉位（Reciprocal Translocation）帶因者**：帶因者本人通常無明顯臨床症狀，但生殖細胞減數分裂時易產生染色體片段缺失或重複的不平衡配子 [SRC-004]。
- **羅伯遜轉位（Robertsonian Translocation）帶因者**：涉及近端著絲粒染色體（第 13、14、15、21、22 號）之融合重排 [SRC-004]。
- **染色體倒位（Inversion）、插入（Insertion）或已知大片段缺失／重複帶因者**：須由遺傳實驗室於檢測前評估所有可能不平衡產物的片段大小是否在平台可偵測範圍內 [SRC-004]。
- **具染色體結構重排相關之反覆流產、不孕或曾生育染色體不平衡胎兒病史之伴侶** [SRC-004] [SRC-007]。

## 3. 檢測原理

依據 ESHRE 2020 技術指引，PGT-SR 依結構重排的片段大小與臨床需求，可選用不同分子細胞遺傳學技術 [SRC-004]：

| 技術平台 | 原理概要 | 一般解析度參考（ESHRE 2020） | 主要特色與適用情境 |
| :--- | :--- | :--- | :--- |
| **NGS（次世代定序）** | 經 WGA 後讀取基因體片段並量化各染色體區段讀數以偵測 [Copy Number Variation](../concepts/copy-number-variation.md) | 依平台定序深度與實驗室驗證規格而定 | 可同時評估結構重排相關片段與其餘 24 條染色體之非整倍體；標準無基因分型 NGS 無法區分「完全正常」與「平衡帶因」 [SRC-004] |
| **aCGH（微陣列比較基因體雜交）** | 檢體與參考 DNA 螢光標記競爭雜交，計算 $\log_2$ 螢光比值 | 商業寡核苷酸 aCGH 約 **5–10 Mb** [SRC-004] | 對轉位區段具多點量測，並可同時檢查非重排染色體，較 FISH 可靠 [SRC-004] |
| **SNP Array（單核苷酸多態性晶片）** | 結合拷貝數與 SNP 基因分型／[Haplotyping](../concepts/haplotyping.md) 分析 | 商業 SNP array 約 **2.4–5 Mb** [SRC-004] | 若有合適家族檢體可建立單倍型相位，有機會在特定條件下區分正常胚胎與平衡重排帶因胚胎 [SRC-004] [SRC-005] |
| **FISH（螢光原位雜交）** | 使用針對特定染色體斷裂點周邊設計的螢光探針於細胞核上目視判讀訊號 | 適用於極小片段或端粒附近（如 **< 10 Mb** 且其他平台難以偵測之區段）[SRC-004] | 僅能檢測探針涵蓋之特定位點，易受訊號重疊或 DNA 完整度影響 [SRC-004] |

> **本實驗室 PGT-SR 技術規格現況（獨立管理，`Pending Technical Verification`）**：雖然本實驗室已確認採用 Thermo Fisher Scientific / Ion Torrent NGS 技術，但**不可假定 PGT-SR 與 PGT-A 或其他產品共用相同定序儀、晶片、覆蓋深度、實驗流程或分析方法**（詳見 [NGS Technology](../laboratory/ngs-technology.md)）。PGT-SR 之實際採用平台、Coverage、最小偵測片段大小（Mb）、平衡帶因區分能力、分析靈敏度／特異度、正式報告週期（TAT）與實驗室認證狀態均列為 **`Pending Technical Verification`**。

## 4. 檢測流程

1. **事前遺傳評估與核型確認（Preclinical Work-up）**：核對夫妻雙方染色體核型報告（karyotype）及必要時之分子定位資料，模擬減數分裂配對與分離後所有可能產生的不平衡重排片段，並確認所選技術平台可偵測所有預期不平衡產物 [SRC-004] [SRC-007]。
2. **檢測前遺傳諮詢與風險告知**：若預期轉位片段中僅部分可被偵測，必須於事前評估報告與諮詢中明確告知無法偵測特定不平衡產物所帶來之風險（如存活不平衡胎兒、早期流產或死產風險）[SRC-004]。
3. **IVF 囊胚培養、切片與冷凍**：以囊胚期滋養外胚層切片（[Embryo Biopsy](../concepts/embryo-biopsy.md)）取得約 5–10 個細胞、清洗裝管並單顆玻璃化冷凍保存 [SRC-008]。
4. **實驗室 WGA 與拷貝數／基因分型分析**：執行經驗證之 PGT-SR 流程、內部品管檢核與獨立審核簽發報告 [SRC-004] [SRC-007]。
5. **結果諮詢、植入與產前確認**：挑選染色體平衡之胚胎植入，懷孕後討論確認性產前診斷（如羊膜穿刺核型／晶片檢查）[SRC-004] [SRC-007]。

## 5. 結果解讀

- **Balanced / Normal（染色體平衡／未見結構重排相關不平衡）**：未偵測到該已知結構重排所導致之染色體片段缺失或重複。**重要提醒**：使用標準 NGS 或 aCGH（未合併單倍型連鎖分析）時，**通常無法區分胚胎是「完全正常核型」還是「與父母相同的平衡性重排帶因者」** [SRC-004]。
- **Unbalanced（染色體不平衡）**：檢出與父母結構重排相符之染色體片段缺失／重複（或相關整條染色體三體／單體），具高流產或胎兒先天異常風險，通常不建議植入 [SRC-004]。
- **合併非重排染色體異常／鑲嵌型結果**：使用全基因體平台（NGS / aCGH / SNP array）時，可能同時檢出與原結構重排無關之其他染色體 [Aneuploidy](../concepts/aneuploidy.md) 或 [Mosaicism](../concepts/mosaicism.md)，需經遺傳諮詢綜合評估 [SRC-002] [SRC-004]。

## 6. 臨床應用

- 協助染色體平衡轉位、羅伯遜轉位、倒位等結構重排帶因伴侶，在胚胎著床前篩除染色體不平衡胚胎，藉以降低因不平衡重排所引起的早期流產、胎死腹中或生育染色體異常胎兒的風險 [SRC-004]。
- 依據全基因體平台特性，亦可在同一次檢測中同步評估非重排染色體的數目狀態 [SRC-004]。

## 7. 檢測限制

1. **片段大小與解析度門檻限制**：若結構重排所涉及的不平衡區段小於所採平台之驗證解析度（例如極小端粒片段），可能導致漏檢；若僅能偵測轉位兩個區段中的其中一段，測試降低不平衡子代與流產風險的效力會受限，須於事前報告明確揭露 [SRC-004]。
2. **一般無法區分正常與平衡帶因**：未結合單倍型分析（[Haplotyping](../concepts/haplotyping.md)）之標準拷貝數檢測無法區分胚胎是否遺傳了與父母相同的平衡性轉位（平衡帶因者多數表型正常，但未來生育時同樣面臨結構重排風險）[SRC-004]。
3. **取樣與技術誤差**：與所有囊胚期切片相同，受限於滋養外胚層取樣代表性、WGA 偏差及約低於 5% 的無結果風險 [SRC-004] [SRC-008]。
4. **無法檢測單基因病與其他未涵蓋異常**：PGT-SR 不會檢出單基因點突變，且懷孕後仍建議接受產前遺傳諮詢與產前診斷確認 [SRC-004] [SRC-007]。

## 8. 相關衛教 FAQ

- [PGT-A、PGT-SR 與 PGT-M 有什麼差別？我需要做哪一種？](../faq/faq-pgt-a-vs-pgt-sr-vs-pgt-m.md)
- [胚胎切片（Embryo Biopsy）會傷害胚胎嗎？為什麼切片後通常要先冷凍？](../faq/faq-embryo-biopsy-safety.md)
- [已經做了 PGT-A、PGT-SR 或 PGT-M，懷孕後還需要做產前檢查嗎？](../faq/faq-prenatal-testing-after-pgt.md)

## 9. 相關文獻（Sources）

- **[SRC-004]** ESHRE PGT-SR/PGT-A Working Group, Coonen E et al. (2020). *ESHRE PGT Consortium good practice recommendations for the detection of structural and numerical chromosomal aberrations*. Human Reproduction Open, 2020(3):hoaa017. DOI: `10.1093/hropen/hoaa017`
- **[SRC-007]** ESHRE PGT Consortium Steering Committee, Carvalho F et al. (2020). *ESHRE PGT Consortium good practice recommendations for the organisation of PGT*. Human Reproduction Open, 2020(3):hoaa021. DOI: `10.1093/hropen/hoaa021`
- **[SRC-008]** ESHRE PGT Consortium and SIG-Embryology Biopsy Working Group, Kokkali G et al. (2020). *ESHRE PGT Consortium and SIG Embryology good practice recommendations for polar body and embryo biopsy for PGT*. Human Reproduction Open, 2020(3):hoaa020. DOI: `10.1093/hropen/hoaa020`

## 10. 最後更新日期

- **最後更新**：2026-11-23（初次整合 `SRC-004`、`SRC-007`、`SRC-008`）
