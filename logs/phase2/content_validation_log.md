# Phase 2 Content Validation Log — ECS Interactive Teaching HTML

- **Artifact Under Review**: `presentations/ecs-teaching-slides/index.html`（11 頁互動教學簡報）
- **Validation Date**: `2026-11-23`
- **Git Branch**: `content/ecs-teaching-slides`
- **Medical QA Policy**: 所有重要醫學敘述均須追溯至現有 Wiki 與已驗證之 `raw/` 來源；不將 `pending_clinical_review` 誤當成 `approved`；不得宣稱未經確認之儀器型號、Coverage、解析度、分析敏感度或 TAT；不得保證排除遺傳疾病風險。

---

## 逐頁醫學內容驗證與來源對照表（Slide 1–11）

| Slide ID | 教學主題 | Supporting Claim（關鍵醫學／規格敘述） | Supporting Wiki Page | Supporting Source | Validation Result | Review Status | 修正與護欄處置 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Slide 1** | Cover | 呈現初學者衛教主題《ECS 是什麼？為什麼健康的父母也可能生下患有遺傳疾病的孩子？》，並標明「衛教教學草稿｜待臨床審核」與不取代專業醫療評估 | `wiki/products/ecs.md`, `wiki/index.md` | `SRC-003`, `SRC-009` | **PASS** | `pending_clinical_review` | 明確加註待審徽章與免責聲明，避免被誤視為已核准臨床發布版 |
| **Slide 2** | What Is a Carrier? | 人類除生殖細胞外含 23 對（46 條）染色體；隱性帶因者僅單一等位基因帶致病變異，另一正常副本多足維持功能，故本人通常健康無症狀、家族史常空白 | `wiki/concepts/monogenic-disease.md`, `wiki/concepts/autosomal-recessive.md`, `wiki/faq/ecs-faq.md` | `SRC-003`, `SRC-005`, `SRC-009` | **PASS** | `pending_clinical_review` | 對應 `GAP-01`，僅使用 Wiki 與 `SRC-009` 已載明之基礎定義，無未驗證統計數字 |
| **Slide 3** | Autosomal Recessive Inheritance | `Aa × Aa` 標準模型下每次懷孕理論機率為 25% AA、50% Aa、25% aa（不分性別、每次獨立）；互動 Punnett Square 明確標示僅適用單基因 AR 模型，不代表所有 ECS 疾病實際臨床發病率 | `wiki/concepts/autosomal-recessive.md`, `wiki/products/ecs.md` | `SRC-003`, `SRC-009` | **PASS** | `pending_clinical_review` | 強制於棋盤旁明示「理論基因型機率前提」與模型適用範圍限制 |
| **Slide 4** | X-linked Inheritance | 母親帶因（`X*X × XY`）每次懷孕 50% 傳遞變異 X（男嬰常受影響、女嬰為帶因者）；另附父親帶變異（`XX × X*Y`）孟德爾傳遞對照，並明示不同 X-linked 疾病表現度與 X 去活化差異不可一概而論 | `wiki/concepts/x-linked-inheritance.md` | `SRC-003`, `SRC-009` | **PASS（附 GAP-02 註記）** | `pending_clinical_review` | 對應 `GAP-02`，於情境 B 明確註記為基礎孟德爾補充並避免概括女性帶因者均無症狀 |
| **Slide 5** | What Is ECS? | 定義 ECS 以 NGS 同步篩檢多種 AR/XL 單基因帶因狀態；區分傳統種族篩檢與 ACMG 2021 族群中立四層架構（Tier 3：≥ 1/200 ＋ 16 個 XL 基因），並說明孕前優先於孕期 | `wiki/products/ecs.md`, `wiki/evidence/ecs-clinical-evidence.md` | `SRC-003` | **PASS** | `pending_clinical_review` | 準確呈現 ACMG 2021 Tier 1–4 門檻，未誇大為強制篩檢 |
| **Slide 6** | How Does ECS Work? | 呈現五步驟（檢體 → DNA → NGS → Variant Interpretation → Report）；明確區分一般 NGS 流程與本實驗室已確認項目（Thermo Fisher Scientific / Ion Torrent NGS、ECS `530` 晶片），未確認參數全列為 `Pending Technical Verification` | `wiki/laboratory/ngs-technology.md`, `wiki/products/ecs.md` | `SRC-003`, `SRC-009` | **PASS** | `pending_technical_verification`, `pending_clinical_review` | 嚴格零推論：未填入具體儀器型號、ECS Coverage、Read Length、分析靈敏度／特異度、TAT 或認證狀態 |
| **Slide 7** | iGene ECS Panel | 由 `raw/structured/igene_disease_list.json` 自動編譯全部 350 筆資料；官網標示 350 種疾病、15 大類、28 個 XL 基因，實測核對為 350 筆疾病與 **351 個去重獨立基因**（含雙基因 `HBA1/HBA2`）、AR 319 / XL 28 / AR/AD 3；揭露 *FMR1* 未收錄差異與檢出率（76%–99%）非統一敏感度 | `wiki/products/ecs-disease-gene-index.md`, `wiki/products/ecs.md` | `SRC-003`, `SRC-009` | **PASS** | `product_spec_verified`, `pending_clinical_review`, `pending_technical_verification` | 搜尋 `FMR1` 回傳 0 筆並主動揭露未收錄原因，絕不把 350 種疾病誤寫為 350 基因 |
| **Slide 8** | Who Should Consider Testing? | 呈現 4 種常見教學情境（一般備孕、家族史／近親聯姻、IVF／捐受贈、已懷孕中），強調帶因篩檢屬自願選項、非所有人都必須做，不提供個人化醫療決策 | `wiki/products/ecs.md`, `wiki/concepts/genetic-counseling.md`, `wiki/evidence/ecs-clinical-evidence.md` | `SRC-003`, `SRC-006`, `SRC-009` | **PASS** | `pending_clinical_review` | 納入 ASRM 2023 倫理邊界（不為無症狀帶因執行 PGT-M）與婉拒受檢權利 |
| **Slide 9** | Understanding Results | 明確區分 Carrier Detected（不等同本人罹病）、No Reportable Variant Detected、Couple Risk、Residual Risk（公式 `族群帶因率 × (1 − 檢測率)`、永不為零）、NGS 四大限制、Genetic Counseling 與新生兒篩檢必要性 | `wiki/concepts/residual-risk.md`, `wiki/products/ecs.md`, `wiki/faq/ecs-faq.md` | `SRC-003`, `SRC-006`, `SRC-009` | **PASS** | `pending_clinical_review` | 強化紅框警示「ECS 陰性無法保證排除風險，且不取代產檢與新生兒篩檢」 |
| **Slide 10** | Interactive Knowledge Quiz | 5 題測驗覆蓋帶因者意義、Aa × Aa 風險、ECS 定位、陰性 Residual Risk 與遺傳諮詢重要性，每題解析均與教材一致並標明 Wiki 頁面與 Source IDs | `wiki/products/ecs.md`, `wiki/concepts/autosomal-recessive.md`, `wiki/concepts/residual-risk.md`, `wiki/concepts/genetic-counseling.md`, `wiki/faq/ecs-faq.md` | `SRC-003`, `SRC-006`, `SRC-009` | **PASS** | `pending_clinical_review` | 題幹與選項均無誘導性醫療承諾，全數具對應 Wiki 出處 |
| **Slide 11** | Summary & References | 彙整 5 大核心學習重點，提供 4 條本機 Wiki Browser 連結、3 篇原始來源（含 DOI / URL / 擷取日 `2026-11-23`）及待臨床審核衛教聲明 | `wiki/index.md`, `wiki/products/ecs.md`, `raw/registry.json` | `SRC-003`, `SRC-006`, `SRC-009` | **PASS** | `source_verified`, `pending_clinical_review` | 明確區分「資料擷取日期」與「審核狀態」，未將未審內容標為核准 |

---

## Medical Content QA 總檢核

- [x] 所有醫學主張皆可追溯至現有 Wiki 頁面與 `SRC-003` / `SRC-006` / `SRC-009`。
- [x] 未將任何 `pending_clinical_review` 或 `pending_technical_verification` 頁面誤標為 `approved`。
- [x] 常染色體隱性百分比皆明示 `Aa × Aa` 單基因理論前提；X-linked 避免不當概括所有臨床表現。
- [x] Residual Risk、檢出率（76%–99%）非統一敏感度、*FMR1* 未收錄、新生兒篩檢必要性皆明確揭露。
- [x] 350 種疾病 vs. 351 個去重獨立基因（含 `HBA1/HBA2`）核對無誤，無未確認實驗室產品宣稱。
