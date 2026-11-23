# Classroom Teaching Demo — Pre-Publish Verification Report

- **Run At (UTC)**: `2026-11-23T14:50:14Z`
- **Publish Directory**: `publish/ecs-demo/`
- **Overall Status**: **PASS**（8 / 8 項通過）

## 發布檔案清單

| File | Size (Bytes) | Role |
| :--- | ---: | :--- |
| `publish/ecs-demo/.nojekyll` | 0 | 停用 GitHub Pages Jekyll 轉換，直接提供靜態檔 |
| `publish/ecs-demo/app.js` | 27,989 | 互動核心（Punnett Square、X-linked、350 項搜尋、5 題測驗、快捷鍵） |
| `publish/ecs-demo/ecs_public_data.js` | 89,329 | 由 SRC-009 編譯之 350 疾病／351 基因公開參考集（已移除檢出率欄位） |
| `publish/ecs-demo/favicon.svg` | 1,170 | 原創中性 DNA 雙股螺旋 SVG 圖示 |
| `publish/ecs-demo/index.html` | 44,336 | 11 頁 ECS 課堂教學展示版主頁（零未授權圖片、零內部規格） |
| `publish/ecs-demo/styles.css` | 19,753 | Warm Orange 教學樣式（含行動版 390px 安全排版） |

## 安全、合規與 Preflight 檢核結果

| Check ID | 檢核項目 | 結果 | 細節 |
| :--- | :--- | :---: | :--- |
| `PUB-01` | 發布目錄白名單（僅含 6 個安全靜態檔案，排除 raw/logs/wiki/未授權圖片） | **PASS** | `files=['.nojekyll', 'app.js', 'ecs_public_data.js', 'favicon.svg', 'index.html', 'styles.css'], extra=[], missing=[]` |
| `PUB-02` | 相對路徑與資源完整性（零 ../ 或根路徑 /，全部本機資源存在） | **PASS** | `local_refs=['app.js', 'ecs_public_data.js', 'favicon.svg', 'styles.css'], bad_rel=[], broken=[]` |
| `PUB-03` | 圖片授權安全（零未授權品牌圖檔，全數採中性原創 SVG） | **PASS** | `img_tags=0, raster_files=[]` |
| `PUB-04` | 敏感資料、內部技術規格與未核准宣稱掃描 | **PASS** | `0 leaks found` |
| `PUB-05` | 課堂免責聲明標示（「課程教學示範，非個人化醫療建議」覆蓋全部投影片） | **PASS** | `occurrences=23 (>= 12)` |
| `PUB-06` | 公開資料集潔淨度（350 疾病 / 351 基因 / 28 XL，且完全移除檢出率欄位） | **PASS** | `items=350, unique_genes=351, xl=28, has_det=False` |
| `PUB-07` | Layout Preflight（11 頁結構、行動頁首換行／直向堆疊、底部間距 >= 88px） | **PASS** | `slides=11, mobile_bottom_padding=96px` |
| `PUB-08` | JS 執行期互動驗證（jsc：G 雙向切換 / Esc / Input 防護 / 350 筆初始載入 / Punnett） | **PASS** | `{"initialHidden": true, "afterFirstG_open": true, "afterSecondG_closed": true, "afterEsc_closed": true, "arrowInInputBlocked": true, "arrowRightAdvances": true, "arrowLeftRetreats": true, "initialGeneCount": true, "punnettDefault": true}` |
