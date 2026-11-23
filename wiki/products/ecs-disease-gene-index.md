---
title: "ECS Disease & Gene Index（iGene 350 項遺傳疾病與 351 個基因結構化索引）"
category: "products"
summary: "彙整 SRC-009（iGene 官方疾病列表）完整擷取之 350 筆疾病與 351 個去重獨立基因統計、15 大分類分布、28 個 X 性聯基因、3 筆 AR/AD 項目及族群／檢出率資料解讀限制，並對接結構化 CSV/JSON 與 Wiki Browser 互動搜尋。"
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
  - "pending_technical_verification"
related_pages:
  - "ecs.md"
  - "../concepts/autosomal-recessive.md"
  - "../concepts/x-linked-inheritance.md"
  - "../concepts/residual-risk.md"
  - "../evidence/ecs-clinical-evidence.md"
  - "../laboratory/ngs-technology.md"
  - "../faq/ecs-faq.md"
---

# ECS Disease & Gene Index（iGene 遺傳疾病與基因結構化索引）

> **資料維護架構說明**：為維持 Wiki 頁面精簡與可長期維護性，本頁不將 350 筆完整表格文字直接塞入單一 Markdown 檔案，而是對接經 SHA-256 驗證之不可變結構化資料檔（`raw/structured/igene_disease_list.csv` 與 `raw/structured/igene_disease_list.json`）。在 **Warm Orange Wiki Browser** 瀏覽本頁或 [ECS 產品主頁](ecs.md) 時，可直接使用下方內建的**互動式疾病／基因即時搜尋與篩選清單**查詢全部 350 筆項目。

## 1. 官方清單完整擷取與統計核對（SRC-009）

- **資料來源**：愛生育銀行／送子鳥生殖中心 — iGene 遺傳疾病帶因篩檢列表（`https://www.icryobank.com/gene/igene-disease-list`）[SRC-009]
- **擷取日期**：`2026-11-23`
- **結構化檔案位置**：`raw/structured/igene_disease_list.csv`、`raw/structured/igene_disease_list.json`（均含 10 項完整欄位：疾病分類、中文病名、英文病名、基因名稱、遺傳模式、族群、帶因率、檢出率、來源網址、擷取日期）

| 檢核項目 | 官網宣稱數值 | 實際完整擷取結果 | 核對說明 |
| :--- | :--- | :--- | :--- |
| **篩檢疾病筆數** | 350 種疾病 | **350 筆疾病條目** | **完全一致** [SRC-009] |
| **疾病主分類數** | 15 大類 | **15 大主分類（另含 10 個次分類）** | **完全一致** [SRC-009] |
| **去重後獨立 Gene Symbol 數** | （未以 350 基因宣稱） | **351 個獨立基因**（原始欄位字串去重 350 組） | 第 239 筆甲型地中海型貧血對應複合基因 `HBA1/HBA2`，故**絕不可將 350 種疾病誤寫為 350 個基因** [SRC-009] |
| **同一基因對應多項疾病** | — | **0 個基因** | 目前清單中無單一基因重複出現於多筆不同疾病列 |
| **X 染色體性聯遺傳（XL）** | 28 個性聯遺傳疾病基因 | **28 筆 XL 疾病 / 28 個去重獨立 XL 基因** | **完全一致**；但與 ACMG 2021 建議之 16 個 XL 基因不完全重合（詳見第 4 節）[SRC-003] [SRC-009] |
| **遺傳模式總分布** | — | `AR`：319 筆、`XL`：28 筆、`AR/AD`：3 筆 | 另有 3 筆具雙重 `AR/AD` 模式標示 [SRC-009] |

## 2. 15 大疾病分類統計一覽

| 分類代碼 | 疾病大類名稱 | 收錄疾病數 |
| :--- | :--- | :--- |
| **A** | 先天性代謝異常（含胺基酸/有機酸、尿素循環、碳水化合物、脂肪酸氧化、溶小體儲積症等次分類） | 141 |
| **B** | 腦部或神經系統異常 | 36 |
| **C** | 呼吸循環系統異常（囊狀纖維化 *CFTR*） | 1 |
| **D** | 消化系統異常 | 2 |
| **E** | 腎臟泌尿系統異常 | 13 |
| **F** | 皮膚系統異常 | 14 |
| **G** | 肌肉系統異常 | 16 |
| **H** | 骨骼系統異常 | 9 |
| **I** | 血液系統異常（含甲／乙型地中海型貧血、血友病等） | 13 |
| **J** | 免疫系統異常 | 13 |
| **K** | 內分泌系統異常 | 26 |
| **L** | 眼睛異常 | 20 |
| **M** | 聽力異常 | 12 |
| **N** | DNA 修復異常 | 13 |
| **O** | 其他疾病 | 21 |
| **總計** | **15 大類** | **350 筆** |

## 3. 特殊項目審核註記（多基因欄位與 `AR/AD` 混合遺傳模式）

1. **單筆疾病對應雙基因（1 筆）**：
   - 第 239 筆：**地中海型貧血-甲型（Alpha-Thalassemia）** — 基因欄位為 **`HBA1/HBA2`**（`AR`，一般人種 1/20、東亞 1/8，官網檢出率 90%）[SRC-009]。
2. **標示為 `AR/AD` 兼具體染色體隱性與顯性遺傳模式（3 筆）**：
   - 第 197 筆：**先天性角化不全症-RTEL1型**（*Dyskeratosis Congenita, RTEL1-Related*，`RTEL1`，一般人種 1/500，99%）
   - 第 208 筆：**營養失養型表皮分解性水皰症**（*Dystrophic Epidermolysis Bullosa, COL7A1-Related*，`COL7A1`，一般人種 1/196，97%）
   - 第 269 筆：**生長激素缺乏-第1A/2型**（*Isolated growth hormone deficiency, Type IA/II*，`GH1`，一般人種 1/126，95%）
   - 臨床提醒：若檢出 `AR/AD` 相關基因變異，需由遺傳諮詢師依具體變異位點與臨床文獻評估該變異屬隱性或顯性致病機制 [SRC-003] [SRC-009]。

## 4. 28 個 X 染色體性聯遺傳（XL）基因清單與跨來源比對

iGene 官方列表包含以下 **28 個 XL 基因**：
`ABCD1`、`ATP7A`、`ATRX`、`BTK`、`CHM`、`COL4A5`、`CYBB`、`DKC1`、`DMD`、`EDA`、`EMD`、`F8`、`F9`、`G6PD`、`GJB1`、`GLA`、`IDS`、`IL2RG`、`MECP2`、`MTM1`、`NR0B1`、`OCRL`、`OTC`、`PDHA1`、`PRPS1`、`RS1`、`SLC6A8`、`WAS` [SRC-009]。

> **跨來源差異標記（待臨床審核）**：ACMG 2021 實務指引（[SRC-003]）以 $1/40{,}000$ 疾病盛行率基準列出 16 個建議 X 性聯篩檢基因（包含 X 染色體脆折症 *FMR1*）。本份 iGene 350 項 NGS 列表中**未包含 *FMR1***（因 *FMR1* 屬 CGG 三核苷酸重複序列擴增，超出常規目標區間 NGS 偵測範疇），同時納入東亞常見之 *G6PD*（蠶豆症）等共 28 個 XL 基因 [SRC-003] [SRC-009]。若臨床需篩檢 X 染色體脆折症，應確認是否須另行加選專屬檢測，此跨指引差異標記為 `pending_clinical_review`。

## 5. 族群、帶因率與檢出率欄位之資料限制

依據 [SRC-009] 原始表格與 ACMG 2021 [SRC-003] 規範，解讀表內統計數值時須注意以下限制：
1. **檢出率不等於所有變異類型的統一分析敏感度**：官網表格列示之「檢出率」（定義為「帶因且被檢出的機率」）範圍介於 **76% 至 99%**（例如 *SMN1* 為 91%、*HBA1/HBA2* 為 90%、*DMD* 為 93%），屬於目標區間 NGS 對已知致病變異之估計檢出率，**不可解讀為對大片段缺失／重複、結構重排、內含子或重複序列區域皆具同等分析敏感度** [SRC-003] [SRC-009]。
2. **適用族群差異與缺值**：350 筆中共有 **284 筆**僅列「一般人種」、**60 筆**並列雙族群數值（如「一般人種 / 東亞」、「一般人種 / 台灣」、「阿什肯納茲猶太人 / 一般人種」等），另有 **3 筆**帶因率標示為 `-`（無明確估算值）[SRC-009]。不同族群帶因率差異顯著，且個別罕見疾病之亞洲／台灣本土帶因率研究可能仍在累積中 [SRC-003]。
3. **殘餘風險永不為零**：檢出率低於 100% 即代表篩檢陰性後必然存在 [Residual Risk（殘餘風險）](../concepts/residual-risk.md)，且本清單亦無法涵蓋套組以外之遺傳病與新發突變 [SRC-003] [SRC-009]。

## Related Pages

- [ECS（擴展性帶因者篩檢 / iGene）產品主頁](ecs.md)
- [Autosomal Recessive（體染色體隱性遺傳）](../concepts/autosomal-recessive.md)
- [X-linked Inheritance（X 染色體性聯遺傳）](../concepts/x-linked-inheritance.md)
- [Residual Risk（殘餘風險）](../concepts/residual-risk.md)
- [NGS Technology（次世代定序技術與平台）](../laboratory/ngs-technology.md)
- [FAQ：ECS / iGene 與 NGS 實驗室常見問題](../faq/ecs-faq.md)

## Sources

- **[SRC-003]** Gregg AR et al.; ACMG (2021). *Screening for autosomal recessive and X-linked conditions during pregnancy and preconception: a practice resource of the ACMG*.
- **[SRC-009]** 愛生育銀行／送子鳥生殖中心（2026）. *iGene 遺傳疾病帶因篩檢列表與產品介紹*（`https://www.icryobank.com/gene/igene-disease-list`、`https://www.icryobank.com/gene/igene`；結構化檔 `raw/structured/igene_disease_list.csv` / `.json`）。
