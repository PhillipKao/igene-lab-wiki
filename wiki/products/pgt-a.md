---
title: "PGT-A（胚胎著床前染色體非整倍體篩檢 / Preimplantation Genetic Testing for Aneuploidy）"
category: "products"
summary: "介紹 PGT-A 的檢測原理、適用對象、臨床效益與爭議、結果解讀（Euploid / Aneuploid / Mosaic）及技術限制，整合 ASRM 2024/2023 與 ESHRE 2020 國際指引。"
source_ids:
  - "SRC-001"
  - "SRC-002"
  - "SRC-004"
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
  - "../concepts/aneuploidy.md"
  - "../concepts/euploidy.md"
  - "../concepts/mosaicism.md"
  - "../concepts/copy-number-variation.md"
  - "../concepts/embryo-biopsy.md"
  - "../concepts/genetic-counseling.md"
  - "../evidence/pgt-a-clinical-evidence.md"
  - "../evidence/mosaic-embryo-evidence.md"
  - "../laboratory/pgt-workflow.md"
  - "../laboratory/ngs-technology.md"
  - "../faq/faq-pgt-a-vs-pgt-sr-vs-pgt-m.md"
  - "../faq/faq-pgt-a-guarantee-pregnancy.md"
  - "../faq/faq-mosaic-embryo-transfer.md"
---

# PGT-A（胚胎著床前染色體非整倍體篩檢）

> **審核狀態提示**：本頁涉及臨床適應症、效益與限制說明，目前為 `pending_clinical_review`。文中關於實驗室實務與檢測規格之敘述係依據國際指引整理之**一般性專業知識**，本實驗室實際檢測平台、解析度與報告門檻**待確認本實驗室實際規格**。

## 1. 檢測介紹

**PGT-A**（Preimplantation Genetic Testing for Aneuploidy，胚胎著床前染色體非整倍體篩檢）是在試管嬰兒（IVF）療程中，於胚胎植入子宮前分析其 24 條染色體（22 對體染色體加上 X、Y 性染色體）的數目狀態，用以篩檢染色體數目異常（即 [Aneuploidy（染色體非整倍體）](../concepts/aneuploidy.md)），並協助優先挑選染色體數目正常的 [Euploidy（染色體整倍體）](../concepts/euploidy.md) 胚胎進行植入 [SRC-001] [SRC-004]。

請注意，PGT-A 與 [PGT-SR](pgt-sr.md)（針對已知染色體結構重排帶因者）及 [PGT-M](pgt-m.md)（針對特定單基因遺傳疾病）的檢測目的與原理不同，彼此不可混淆 [SRC-004] [SRC-006]。

## 2. 適用對象

依據 ASRM 2024 委員會意見，**目前尚未證實 PGT-A 作為所有 IVF 患者的常規全面篩檢（universal screening）具有確定臨床效益** [SRC-001]。是否採用 PGT-A 應經醫師評估與 [Genetic Counseling（遺傳諮詢）](../concepts/genetic-counseling.md) 後，依個別情況共同決策 [SRC-001] [SRC-007]：

- **高齡產婦（Advanced Maternal Age）**：卵子減數分裂錯誤與胚胎非整倍體比率隨女性年齡上升而增加；部分次族群分析（如 STAR 試驗 35–40 歲事後分析）觀察到每次植入之持續懷孕率較高，但 ASRM 2024 指出仍缺乏針對此族群以意向治療分析（ITT）設計的充分實務隨機對照試驗 [SRC-001]。
- **反覆性流產（Recurrent Pregnancy Loss）**：早期流產常見原因與染色體非整倍體有關，具生物學合理性，但現有研究在懷孕率與流產率改善上證據仍有限且尚未一致 [SRC-001]。
- **擬採選擇性單一胚胎植入（eSET）之患者**：部分早期單中心研究指出於預後良好族群中可協助推動 eSET、降低多胞胎妊娠風險，但近年大型多中心 RCT 顯示冷凍週期之整體累積懷孕結局與傳統 IVF 相近 [SRC-001]。
- **合併 PGT-M 週期**：部分臨床情境會考量於 [PGT-M](pgt-m.md) 週期合併評估染色體數目，須權衡可植入胚胎數減少與檢測限制 [SRC-001] [SRC-006]。

## 3. 檢測原理

現代 PGT-A 主要針對囊胚期滋養外胚層切片（[Embryo Biopsy](../concepts/embryo-biopsy.md)）取得之少量細胞（通常約 5–10 個細胞）進行全基因體放大（Whole Genome Amplification, WGA），再透過高通量分析平台進行 24 條染色體 [Copy Number Variation（拷貝數變異）](../concepts/copy-number-variation.md) 評估 [SRC-004] [SRC-008]：

- **次世代定序（NGS）**：目前最常用之平台，直接讀取基因體定序片段，透過生物資訊演算法量化各染色體區段的定序讀數（read counts），以判斷染色體增減與中間拷貝數訊號 [SRC-002] [SRC-004]。
- **微陣列比較基因體雜交（aCGH）**：將放大後的檢體 DNA 與參考 DNA 標記不同螢光後進行競爭性雜交，利用螢光訊號比值（$\log_2$ ratio）偵測染色體拷貝數異常 [SRC-004]。

> **本實驗室 PGT-A 技術規格現況（已確認 vs. `Pending Technical Verification`）**：
> - **已確認資訊**：本實驗室使用 **Thermo Fisher Scientific / Ion Torrent NGS** 定序技術；**PGT-A 定序晶片（Chip Type）為 `520`（Ion 520）**，**覆蓋深度（Coverage）常規為 `0.005×`，最高為 `0.02×`**（詳見分產品管理頁 [NGS Technology](../laboratory/ngs-technology.md)）。
> - **Pending Technical Verification（尚未確認、不得自行推定或以原廠規格取代）**：具體 Ion Torrent 儀器型號、是否與其他產品共用同一儀器與流程、Read Length、CNV / Aneuploidy 最小偵測解析度、Mosaic / Low-VAF 偵測下限與報告門檻、各變異類型分析靈敏度／特異度、PGT-A 正式報告週期（TAT），以及實驗室有效認證狀態（ISO 15189 / LDTs / CAP 等）。

## 4. 檢測流程

完整流程涉及生殖醫學中心與遺傳檢測實驗室的跨團隊協作（詳見 [PGT 檢測完整作業流程](../laboratory/pgt-workflow.md)）[SRC-007] [SRC-008]：

1. **檢測前遺傳諮詢與知情同意**：說明檢測目的、各類結果（包含 [Mosaicism](../concepts/mosaicism.md) 與無結果）之可能比例、診所植入／儲存政策及不檢測之選項 [SRC-002] [SRC-007]。
2. **IVF 體外受精與囊胚培養**：培養胚胎至囊胚期（通常為第 5–7 天）[SRC-001] [SRC-008]。
3. **囊胚切片（Trophectoderm Biopsy）與裝管（Tubing）**：由受訓胚胎師自滋養外胚層切取約 5–10 個細胞並完成清洗裝管與雙人見證（見 [檢體追溯](../laboratory/sample-traceability.md)）[SRC-007] [SRC-008]。
4. **胚胎玻璃化冷凍（Vitrification）**：因遺傳檢測需要作業時間，切片後多半須進行單顆獨立冷凍保存 [SRC-008]。
5. **WGA 與 NGS / aCGH 拷貝數分析及品管審查**：於遺傳實驗室完成擴增、定序／晶片分析、品管檢核與報告簽核 [SRC-004] [SRC-007]。
6. **檢測後諮詢與解凍植入決策**：依報告結果與胚胎形態評估植入優先順序；若獲妊娠，仍應討論標準產前篩檢或產前診斷選項 [SRC-001] [SRC-002]。

## 5. 結果解讀

依據生物資訊訊號與各實驗室經驗證之判讀門檻，PGT-A 常見報告分類如下（不同實驗室之門檻與是否揭露鑲嵌結果存在差異，不可混用單一數值標準）[SRC-002] [SRC-004]：

| 結果分類 | 一般意義 | 臨床決策注意事項 |
| :--- | :--- | :--- |
| **Euploid（整倍體）** | 切片細胞之 24 條染色體數目符合正常二倍體預期 | 通常列為優先植入選項，但**無法保證懷孕或活產**，亦不能排除單基因病或低比例鑲嵌 [SRC-001] [SRC-002] |
| **Aneuploid（非整倍體）** | 切片檢出明確染色體數目增加（如三體）或缺失（如單體） | 通常不建議植入，與著床失敗、早期流產或染色體異常胎兒相關 [SRC-001] [SRC-004] |
| **Mosaic（鑲嵌型結果）** | 切片 DNA 拷貝數落在整倍體與完全非整倍體之間的中間訊號 | **不等同整顆胚胎（含 ICM）之真實染色體狀態**，可能反映生物學鑲嵌或技術雜訊；考慮植入前應提供專業遺傳諮詢 [SRC-002] |
| **Segmental（節段異常）** | 偵測到部分染色體片段缺失或重複 | 需評估片段大小與實驗室解析度限制，並排除父母為結構重排帶因者之可能 [SRC-004] |
| **No Result / Inconclusive（無結果）** | DNA 擴增失敗或品管未通過 | ESHRE 2020 指出囊胚期切片之無法判讀率預期低於 5%；需由醫師評估是否重切片或依形態決策 [SRC-008] |

## 6. 臨床應用

- **協助胚胎挑選與單一胚胎植入**：在擁有多顆可用囊胚時，PGT-A 可提供染色體資訊作為胚胎挑選參考，但需與囊胚形態學與患者整體預後一併評估 [SRC-001]。
- **重要實證立場（ASRM 2024）**：
  - **PGT-A 無法保證懷孕或保證活產** [SRC-001]。
  - **並非所有 IVF 患者皆能從 PGT-A 獲得確定效益**：多中心隨機對照試驗顯示，在具有可用囊胚的族群中，PGT-A 與傳統 IVF 的整體累積懷孕結局大致相近 [SRC-001]。
  - PGT-A 降低臨床流產率的實際效益，因現有研究存在重要方法學限制，目前仍不明確 [SRC-001]。
  - 完整跨指引實證比較請參閱 [PGT-A 臨床證據與跨指引整合](../evidence/pgt-a-clinical-evidence.md)。

## 7. 檢測限制

1. **取樣代表性限制**：切片僅取樣滋養外胚層（未來發育為胎盤）之少數細胞，未必完全代表內細胞團（ICM，未來發育為胎兒）的染色體狀態 [SRC-002] [SRC-008]。
2. **無法偵測之變異類型**：標準拷貝數分析（未合併基因分型時）無法偵測單基因致病變異、微小片段缺失／重複（低於平台解析度）、平衡性染色體轉位、部分單親二體（UPD）或特定倍數性異常（如平衡三倍體）[SRC-004]。
3. **技術雜訊與假陽性／假陰性**：WGA 擴增偏差、細胞裂解或生物資訊演算法雜訊可能導致鑲嵌型誤判或無法判讀，進而造成具發育潛力之胚胎被錯誤棄置之風險 [SRC-001] [SRC-002] [SRC-004]。
4. **切片與再冷凍之潛在影響**：胚胎切片屬侵入性操作，需高度熟練技術；若進行解凍後重切片與二次冷凍，須考量對胚胎存活與發育之潛在風險 [SRC-001] [SRC-008]。
5. **無法取代產前檢查**：PGT-A 屬於篩檢而非最終診斷，成功懷孕後仍應依標準產科指引討論產前篩檢或產前診斷 [SRC-001] [SRC-002]。

## 8. 相關衛教 FAQ

- [PGT-A、PGT-SR 與 PGT-M 有什麼差別？我需要做哪一種？](../faq/faq-pgt-a-vs-pgt-sr-vs-pgt-m.md)
- [做 PGT-A 可以保證懷孕或一定能降低流產率嗎？](../faq/faq-pgt-a-guarantee-pregnancy.md)
- [胚胎報告顯示 Mosaic（鑲嵌型），還能植入嗎？](../faq/faq-mosaic-embryo-transfer.md)
- [胚胎切片（Embryo Biopsy）會傷害胚胎嗎？為什麼切片後通常要先冷凍？](../faq/faq-embryo-biopsy-safety.md)
- [已經做了 PGT-A、PGT-SR 或 PGT-M，懷孕後還需要做產前檢查嗎？](../faq/faq-prenatal-testing-after-pgt.md)

## 9. 相關文獻（Sources）

- **[SRC-001]** Practice Committees of ASRM & SART (2024). *The use of preimplantation genetic testing for aneuploidy: a committee opinion*. Fertility and Sterility, 122(3):421–434. DOI: `10.1016/j.fertnstert.2024.04.013`
- **[SRC-002]** Practice Committees of ASRM & Genetic Counseling Professional Group (2023). *Clinical management of mosaic results from preimplantation genetic testing for aneuploidy of blastocysts: a committee opinion*. Fertility and Sterility, 120(5):973–982. DOI: `10.1016/j.fertnstert.2023.08.969`
- **[SRC-004]** ESHRE PGT-SR/PGT-A Working Group, Coonen E et al. (2020). *ESHRE PGT Consortium good practice recommendations for the detection of structural and numerical chromosomal aberrations*. Human Reproduction Open, 2020(3):hoaa017. DOI: `10.1093/hropen/hoaa017`
- **[SRC-007]** ESHRE PGT Consortium Steering Committee, Carvalho F et al. (2020). *ESHRE PGT Consortium good practice recommendations for the organisation of PGT*. Human Reproduction Open, 2020(3):hoaa021. DOI: `10.1093/hropen/hoaa021`
- **[SRC-008]** ESHRE PGT Consortium and SIG-Embryology Biopsy Working Group, Kokkali G et al. (2020). *ESHRE PGT Consortium and SIG Embryology good practice recommendations for polar body and embryo biopsy for PGT*. Human Reproduction Open, 2020(3):hoaa020. DOI: `10.1093/hropen/hoaa020`

## 10. 最後更新日期

- **最後更新**：2026-11-23（初次整合 `SRC-001`、`SRC-002`、`SRC-004`、`SRC-007`、`SRC-008`）
