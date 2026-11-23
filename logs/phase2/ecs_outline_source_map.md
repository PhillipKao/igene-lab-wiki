# Phase 2 教材大綱與 Wiki 來源對照表

- **教材名稱**：ECS 是什麼？為什麼健康的父母也可能生下患有遺傳疾病的孩子？
- **英文副標**：Expanded Carrier Screening: Understanding Hidden Genetic Risks
- **目標對象**：一般民眾及沒有遺傳學背景的學生（10–15 分鐘初學者互動教學）
- **產出位置**：`presentations/ecs-teaching-slides/index.html`（11 頁 16:9 暖橘色互動教學簡報）
- **Assets 採用策略**（依據 `logs/asset_audit.md`，僅挑選與主題與版型相配之品牌識別素材，不硬塞無關變體）：
  - `assets/biolove-5.png`：Slide 1 封面主視覺（直式完整品牌標誌）
  - `assets/biolove-2.png`：Favicon 與精簡徽章
  - `assets/biolove-4.png`：內頁頁首精簡橫式標誌
  - `assets/biolove-8.png`：Slide 11 總結頁品牌橫幅
  - 醫學與遺傳教學視覺：以內嵌標準化 SVG 圖示（基因染色體示意、互動 Punnett Square、X-linked 傳遞圖、NGS 5 步驟流程圖）搭配呈現，確保高解析不變形。

---

## 11 頁教材大綱與來源追溯對照

| Slide ID | 教學主題 | 核心學習目標 | 主要依據 Wiki 頁面 | Source IDs | 目前審核狀態 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Slide 1** | Cover：ECS 是什麼？為什麼健康的父母也可能生下患有遺傳疾病的孩子？ | 建立主題動機、受眾定位與衛教免責／待審標示 | `wiki/products/ecs.md`, `wiki/index.md` | `SRC-003`, `SRC-009` | `pending_clinical_review` |
| **Slide 2** | What Is a Carrier?（基因、變異與無症狀帶因者） | 認識 23 對染色體、基因、致病性變異與為何帶因者多無症狀 | `wiki/concepts/monogenic-disease.md`, `wiki/concepts/autosomal-recessive.md`, `wiki/faq/ecs-faq.md` | `SRC-003`, `SRC-005`, `SRC-006`, `SRC-009` | `pending_clinical_review`（含 `auto_compiled` 基礎定義） |
| **Slide 3** | Autosomal Recessive Inheritance（常染色體隱性遺傳＋互動 Punnett Square） | 理解 `Aa × Aa` 每次懷孕 25% AA / 50% Aa / 25% aa 理論基因型機率，透過互動棋盤操作不同親代組合 | `wiki/concepts/autosomal-recessive.md`, `wiki/products/ecs.md` | `SRC-003`, `SRC-006`, `SRC-009` | `pending_clinical_review` |
| **Slide 4** | X-linked Inheritance（X 染色體性聯遺傳） | 比較母親帶因（`X*X × XY`）與父親帶變異（`XX × X*Y`）之傳遞差異，並提醒不可一概而論臨床表現 | `wiki/concepts/x-linked-inheritance.md` | `SRC-003`, `SRC-009` | `pending_clinical_review` |
| **Slide 5** | What Is ECS?（擴展性帶因者篩檢與 ACMG 分層） | 區分傳統單一／族群篩檢與現代族群中立 ECS（ACMG Tier 1–4）及孕前／孕期考量原因 | `wiki/products/ecs.md`, `wiki/evidence/ecs-clinical-evidence.md` | `SRC-003`, `SRC-009` | `pending_clinical_review` |
| **Slide 6** | How Does ECS Work?（ECS 檢測 5 步驟流程與技術邊界） | 看懂檢體 → DNA → NGS → Variant Interpretation → Report；明確區分一般流程與已確認之 Thermo Fisher Ion Torrent / ECS `530` 晶片 | `wiki/laboratory/ngs-technology.md`, `wiki/products/ecs.md` | `SRC-003`, `SRC-009` | `pending_technical_verification`, `pending_clinical_review` |
| **Slide 7** | iGene ECS Panel（350 疾病 / 351 基因＋完整互動搜尋） | 檢視 iGene 官方 15 大類 350 項疾病、351 獨立基因（含 `HBA1/HBA2`）、28 XL 基因（不含 *FMR1*）並支援 350 筆真實清單即時搜尋 | `wiki/products/ecs-disease-gene-index.md`, `wiki/products/ecs.md` | `SRC-003`, `SRC-009` | `product_spec_verified`, `pending_clinical_review`, `pending_technical_verification` |
| **Slide 8** | Who Should Consider Testing?（誰可以考慮帶因者篩檢？） | 依 ACMG 2021 與官方資料呈現常見情境式教學卡片，強調自願選擇且不提供個人化醫療決策 | `wiki/products/ecs.md`, `wiki/concepts/genetic-counseling.md`, `wiki/evidence/ecs-clinical-evidence.md` | `SRC-003`, `SRC-006`, `SRC-009` | `pending_clinical_review` |
| **Slide 9** | Understanding Results（看懂報告結果與 Residual Risk） | 區分 Carrier Detected（非等同本人發病）、No Reportable Variant Detected、Couple Risk、Residual Risk 永不為零與 Genetic Counseling | `wiki/concepts/residual-risk.md`, `wiki/products/ecs.md`, `wiki/faq/ecs-faq.md` | `SRC-003`, `SRC-006`, `SRC-009` | `pending_clinical_review` |
| **Slide 10** | Interactive Knowledge Quiz（5 題互動觀念測驗） | 以 5 題完整測驗檢核帶因者意義、AR 風險、ECS 目的、陰性殘餘風險與遺傳諮詢重要性，附即時回饋、計分與 Wiki 出處 | `wiki/products/ecs.md`, `wiki/concepts/autosomal-recessive.md`, `wiki/concepts/residual-risk.md`, `wiki/concepts/genetic-counseling.md`, `wiki/faq/ecs-faq.md` | `SRC-003`, `SRC-006`, `SRC-009` | `pending_clinical_review` |
| **Slide 11** | Summary & References（核心總結、Wiki 連結與來源聲明） | 彙整 5 大核心學習重點、Wiki 延伸閱讀連結、完整文獻來源、資料擷取日期（`2026-11-23`）與待臨床審核衛教聲明 | `wiki/index.md`, `wiki/products/ecs.md`, `raw/registry.json` | `SRC-003`, `SRC-006`, `SRC-009` | `source_verified`, `pending_clinical_review` |
