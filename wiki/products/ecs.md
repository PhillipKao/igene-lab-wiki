---
title: "ECS（擴展性帶因者篩檢 / iGene 遺傳疾病帶因篩檢）"
category: "products"
summary: "整合 ACMG 2021 實務指引（SRC-003）與愛生育銀行／送子鳥生殖中心 iGene 官方產品及疾病列表（SRC-009），介紹 ECS / iGene（350 項疾病、15 大類、351 個去重獨立基因含 28 個 X 性聯基因）、Thermo Fisher Scientific NGS 平台確認資訊、殘餘風險與檢測限制。"
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
  - "ecs-disease-gene-index.md"
  - "../concepts/autosomal-recessive.md"
  - "../concepts/x-linked-inheritance.md"
  - "../concepts/monogenic-disease.md"
  - "../concepts/residual-risk.md"
  - "../concepts/genetic-counseling.md"
  - "../evidence/ecs-clinical-evidence.md"
  - "../laboratory/ngs-technology.md"
  - "pgt-m.md"
  - "../faq/ecs-faq.md"
  - "../faq/faq-ecs-negative-risk.md"
---

# ECS（擴展性帶因者篩檢 / iGene 遺傳疾病帶因篩檢）

> **分層審核與驗證狀態**：本頁已整合官方來源 [SRC-009]（`source_verified`、`product_spec_verified`）與實驗室主管確認之定序平台廠牌（Thermo Fisher Scientific NGS），惟臨床風險表述仍屬 `pending_clinical_review`，且具體儀器型號、晶片、覆蓋深度、變異偵測下限與報告週期（TAT）保留為 `pending_technical_verification`，未經完整審核前不得標示為 `approved`。

## 1. 檢測介紹

**ECS**（Expanded Carrier Screening，擴展性帶因者篩檢）係於**孕前（preconception）或懷孕初期**以高通量定序技術同步篩檢數十至數百種 [Autosomal Recessive（體染色體隱性遺傳）](../concepts/autosomal-recessive.md) 及 [X-linked Inheritance（X 染色體性聯遺傳）](../concepts/x-linked-inheritance.md) 相關 [Monogenic Disease（單基因遺傳疾病）](../concepts/monogenic-disease.md) 的帶因狀態 [SRC-003]。

### 本實驗室／機構對應產品：iGene 遺傳疾病帶因篩檢（SRC-009）
依據愛生育銀行／送子鳥生殖中心官方產品頁與完整疾病列表 [SRC-009]：
- **產品名稱**：**iGene 遺傳疾病帶因篩檢**（愛基因）
- **檢測類型**：擴展性帶因者篩檢（ECS）
- **檢測方式與檢體**：萃取周邊血液樣本 DNA，採用 **次世代定序（NGS）** 搭配生物資訊分析軟體針對目標疾病基因進行分析 [SRC-009]；本實驗室已確認使用 **Thermo Fisher Scientific / Ion Torrent NGS** 定序技術（惟不可假定 ECS 與 PGT-A/SR/M 共用相同定序儀、晶片、流程或分析方法，詳見 [NGS Technology](../laboratory/ngs-technology.md)）。
- **官方篩檢範圍與結構化核對**：
  - 官網標示：**15 大類、350 種遺傳疾病、包含 28 個性聯遺傳疾病基因** [SRC-009]。
  - 完整表格擷取核對（`2026-11-23`）：實際擷取 **350 筆疾病條目**、**15 大主分類（含 10 次分類）**、**28 筆 XL 項目（28 個獨立 XL 基因）**，與官網宣稱完全一致；另因第 239 筆甲型地中海型貧血同時涵蓋 `HBA1/HBA2` 兩個基因，**去重後獨立 Gene Symbol 總數為 351 個**（切勿將 350 種疾病誤寫為 350 個基因）[SRC-009]。
  - 遺傳模式分布：`AR` 319 筆、`XL` 28 筆、`AR/AD` 3 筆（`RTEL1`、`COL7A1`、`GH1`）[SRC-009]。
  - 詳細分類統計與結構化清單請參閱 **[ECS Disease & Gene Index（iGene 350 項疾病與 351 個基因索引）](ecs-disease-gene-index.md)**（原始結構化檔：`raw/structured/igene_disease_list.csv` / `.json`）[SRC-009]。

## 2. 適用對象

依據 ACMG 2021 實務指引（[SRC-003]）與 iGene 官方適用說明（[SRC-009]），帶因者篩檢屬**自願性選擇（optional）**，以**備孕前（preconception）優先於孕期**，因可保有最完整的生育選擇且心理壓力較低：

- **所有婚前、孕前或孕期之伴侶或個人**：ACMG 2021 建議以族群中立原則提供 Tier 3 等級帶因者篩檢 [SRC-003] [SRC-009]。
- **血緣較近（近親聯姻）或具家族遺傳病史／曾生育先天異常子代之夫妻**：應搭配專業遺傳諮詢評估是否需更廣範圍篩檢或針對性基因診斷 [SRC-003] [SRC-009]。
- **準備接受人工生殖技術（IVF）或卵子／精子捐受贈評估者** [SRC-009]。
- **配偶／伴侶共同評估**：若時間充裕可先由一方檢測、陽性再追蹤伴侶；若時程較緊或已懷孕，夫妻同步檢測可縮短等待時間 [SRC-003] [SRC-009]。

## 3. 檢測原理與規格確認邊界

- **核心技術原理**：iGene 萃取血液 DNA 後，透過目標區間 **NGS** 同步定序清單所列疾病基因之目標區域並進行生物資訊變異判讀 [SRC-003] [SRC-009]。
- **國際分層架構對照（ACMG 2021）**：ACMG 將帶因篩檢分為 Tier 1（CF/SMA 與家族史評估）、Tier 2（$\ge 1/100$）、Tier 3（任一族群帶因頻率 $\ge 1/200$ 及 16 個 X 性聯基因，建議常規提供）與 Tier 4（$< 1/200$ 罕見項目，保留於近親聯姻或家族史評估）[SRC-003]。iGene 收錄 350 種疾病與 28 個 X 性聯基因，涵蓋範疇超過 Tier 3 基準，但須留意部分需特殊分子方法之項目（如 *FMR1* 三核苷酸重複擴增）並未列於此份 NGS 清單中（詳見 [ECS 疾病與基因索引](ecs-disease-gene-index.md)）[SRC-003] [SRC-009]。
- **本實驗室 ECS 技術規格狀態（與其他產品分開管理）**：
  - **已確認**：對應 **iGene** 官方 15 大類 350 種疾病（351 個去重獨立基因，含 28 個 X 性聯基因）與血液 DNA 目標區間 NGS [SRC-009]；本實驗室採用 Thermo Fisher Scientific / Ion Torrent NGS 定序技術，**ECS 定序晶片（Chip Type）為 `530`（Ion 530）**。
  - **Pending Technical Verification（尚未提供，不得推論或引用原廠一般規格代替本實驗室驗證結果）**：具體 Ion Torrent 儀器型號、ECS 是否與其他產品共用同一儀器或分析流程、ECS 定序 Coverage、Read Length、Low-VAF 偵測下限、各變異類型 Analytical Sensitivity / Specificity、ECS 報告週期（TAT），以及實驗室有效認證狀態（ISO 15189 / LDTs / CAP 等）（見 [NGS Technology](../laboratory/ngs-technology.md)）。

## 4. 檢測流程

1. **檢測前遺傳諮詢（Pretest Counseling）**：說明篩檢為自願性、涵蓋 15 大類 350 項疾病範圍、陰性仍具 [Residual Risk（殘餘風險）](../concepts/residual-risk.md) 及目標區間 NGS 之檢驗限制 [SRC-003] [SRC-009]。
2. **血液檢體採集與 DNA 萃取**：依實驗室標準採集周邊血液檢體並萃取基因體 DNA [SRC-009]。
3. **NGS 目標區間定序與生物資訊分析**：依本實驗室驗證之目標區間 NGS 流程執行分析與變異判讀（ECS 專屬定序儀／晶片、Coverage 與分析 SOP 屬 `Pending Technical Verification`）[SRC-009]。
4. **檢測後諮詢與伴侶追蹤（Post-test Counseling）**：
   - 若為體染色體隱性基因單方帶因，建議伴侶接受對應基因檢測 [SRC-003] [SRC-009]。
   - 若檢出伴侶雙方同為體染色體隱性帶因、女性為 X 性聯帶因或檢出 `AR/AD` 變異，應轉介 [Genetic Counseling（遺傳諮詢）](../concepts/genetic-counseling.md) 討論完整生育選項 [SRC-003] [SRC-009]。

## 5. 結果解讀

| 結果情境 | 遺傳與生殖意義 | 後續建議 |
| :--- | :--- | :--- |
| **陰性（未檢出目標致病變異）** | 大幅降低成為套組內受檢疾病帶因者的機率，但**絕非零風險，亦不能保證生下健康寶寶** | 必須理解 [Residual Risk（殘餘風險）](../concepts/residual-risk.md)；本篩檢不涵蓋套組外疾病、新發突變或染色體異常，寶寶出生後仍建議接受新生兒篩檢 [SRC-003] [SRC-009] |
| **單方為體染色體隱性（`AR`）帶因者** | 本人多數健康無症狀，每次懷孕有 50% 機率將該變異遺傳給子女 | 建議另一半接受同一基因檢測；若伴侶陰性，子代罹病風險顯著下降但仍受殘餘風險影響 [SRC-003] [SRC-009] |
| **雙方為同一 `AR` 基因帶因者** | 每次懷孕子代有 **25%** 機率罹病、**50%** 為帶因者、**25%** 未帶因 | 轉介遺傳諮詢，評估自然懷孕合併產前診斷、IVF 結合 [PGT-M](pgt-m.md)、配子受贈或領養等選項 [SRC-003] [SRC-006] [SRC-009] |
| **女性為 `XL`（X 性聯）疾病帶因者** | 每次懷孕有 **50%** 機率將帶有變異的 X 染色體傳給子代（男性子代常表現疾病，女性子代為帶因者或具不等程度表型） | 轉介遺傳諮詢，討論產前診斷或 [PGT-M](pgt-m.md) 規劃，並評估帶因者自身健康追蹤 [SRC-003] [SRC-006] [SRC-009] |
| **檢出 `AR/AD` 相關基因變異（`RTEL1`、`COL7A1`、`GH1`）** | 該基因兼具隱性與顯性相關疾病表現，風險視具體變異位點而定 | 必須由遺傳專科醫師或遺傳諮詢師針對特定變異之致病機制與外顯率進行個別評估 [SRC-003] [SRC-009] |

## 6. 臨床應用

- **孕前風險辨識與生育自主決策**：協助無明顯家族史之無症狀帶因伴侶及早發現單基因隱性或 X 性聯風險，從容規劃自然懷孕搭配產前檢查、IVF 合併 [PGT-M](pgt-m.md) 或配子受贈等選項 [SRC-003] [SRC-009]。
- **銜接 PGT-M 適應症邊界**：依據 ASRM 2023 指引，確認顯著罹病風險後可評估 [PGT-M](pgt-m.md)，但**不應僅為排除「無症狀體染色體隱性帶因狀態」或偽缺乏等位基因而執行 PGT-M** [SRC-006]。

## 7. 檢測限制

1. **ECS 是帶因者篩檢，不等同所有遺傳疾病的完整診斷**：無法排除套組以外之數千種遺傳病、多因子先天異常或染色體數目／結構異常（後者屬 [PGT-A](pgt-a.md) / [PGT-SR](pgt-sr.md) 範疇）[SRC-003] [SRC-009]。
2. **陰性結果仍存在 Residual Risk（永不為零）**：ACMG 2021 指出多基因篩檢難以計算單一整體殘餘風險；且 iGene 官方清單各疾病檢出率分布介於 **76%–99%**，**不得將官網檢出率解讀為所有變異類型之統一分析敏感度**，亦不得宣稱所有疾病皆可完全檢出 [SRC-003] [SRC-009]。
3. **目標區間 NGS 結構與區域限制（SRC-009 官方明示）**：
   - 無法偵測**大片段基因缺失（deletion）、插入（insertion）、倒轉（inversion）、重複性擴增（duplication / repeat expansion）或其他複雜性結構異常**；
   - 僅針對列表基因之目標區間分析，位於**非目標區間、內含子（intron）及重複序列區域**之變異可能無法檢出（例如 X 染色體脆折症 *FMR1* 未包含於此 350 項清單中）；
   - 無法篩檢受精後發生之**新發突變、鑲嵌細胞（mosaicism）及體細胞突變** [SRC-003] [SRC-009]。
4. **族群資料限制**：官方清單中多數條目採「一般人種」估計（284 筆），60 筆並列雙族群（含東亞、台灣等），另有 3 筆帶因率為 `-`，跨族群風險估算應由遺傳諮詢師綜合家族史解讀 [SRC-003] [SRC-009]。
5. **無法取代新生兒篩檢與產前檢查**：即便夫妻雙方篩檢皆陰性，孕期仍應配合標準產檢，且寶寶出生後仍建議接受新生兒篩檢 [SRC-003] [SRC-009]。

## 8. 相關衛教 FAQ 與互動查詢

- **[ECS Disease & Gene Index（iGene 350 項疾病與 351 個基因結構化索引）](ecs-disease-gene-index.md)**（Wiki Browser 支援即時搜尋疾病名稱、基因名稱與遺傳模式）
- [FAQ：ECS / iGene 遺傳疾病帶因篩檢與 NGS 實驗室常見問題](../faq/ecs-faq.md)
- [FAQ：擴展性帶因者篩檢（ECS）結果陰性，代表寶寶完全不會得遺傳病嗎？](../faq/faq-ecs-negative-risk.md)
- [FAQ：PGT-A、PGT-SR 與 PGT-M 有什麼差別？](../faq/faq-pgt-a-vs-pgt-sr-vs-pgt-m.md)

## 9. 相關文獻與官方來源（Sources）

- **[SRC-003]** Gregg AR, Aarabi M, Klugman S, et al.; ACMG Professional Practice and Guidelines Committee (2021). *Screening for autosomal recessive and X-linked conditions during pregnancy and preconception: a practice resource of the American College of Medical Genetics and Genomics (ACMG)*. Genetics in Medicine, 23(10):1793–1806. DOI: `10.1038/s41436-021-01203-z`
- **[SRC-006]** Practice Committees of ASRM & Genetic Counseling Professional Group (2023). *Indications and management of preimplantation genetic testing for monogenic conditions: a committee opinion*. Fertility and Sterility, 120(1):61–71. DOI: `10.1016/j.fertnstert.2023.03.003`
- **[SRC-009]** 愛生育銀行／送子鳥生殖中心（2026）. *iGene 遺傳疾病帶因篩檢官方產品頁與完整疾病列表*（[官方疾病列表](https://www.icryobank.com/gene/igene-disease-list)、[官方產品介紹](https://www.icryobank.com/gene/igene)，擷取日期：`2026-11-23`；結構化清單：`raw/structured/igene_disease_list.csv` / `.json`）。

## 10. 最後更新日期

- **最後更新**：2026-11-23（整合 `SRC-009` 官方 iGene 350 項疾病／351 個基因結構化清單與實驗室 Thermo Fisher Scientific NGS 平台廠牌確認資訊）
