# Phase 2 HTML Functional & Visual Test Log

- **Tested URL**: `http://127.0.0.1:8765/presentations/ecs-teaching-slides/`
- **Test Date**: `2026-11-23`
- **Test Environment**: 本機靜態伺服器（`python3 -m http.server 8765 --bind 127.0.0.1`）＋真實瀏覽器自動化測試代理（`browser` subagent，桌面 `1280×800` 與行動 `390×844` 雙視窗實測）＋靜態 JavaScriptCore 語法檢查

---

## 第一輪實測結果與發現問題（Round 1）

| 測試類別 | 測試項目 | 第一輪結果 | 實測數據／發現問題 |
| :--- | :--- | :---: | :--- |
| **Static QA** | HTML 投影片數、相對資源路徑、JS 語法（JavaScriptCore） | **PASS** | 11 頁投影片、全部本機圖片與連結存在，`igene_data.js` 與 `app.js` 零語法錯誤 |
| **Network & Console** | Console Errors 與 HTTP 請求狀態 | **PASS** | `0` Console Errors；50 筆請求全部成功（`0` 筆 `>= 400`）；所有 BiOLOVE PNG（12 處 `<img>`）皆正常載入無變形 |
| **Desktop 16:9 Visual** | `.stage` 比例與 11 頁垂直邊界檢查（`1280×800`） | **PASS** | `.stage` 實測 `1228.80 × 691.20 px`（精確 `16:9` = `1.778`）；全數 11 頁所有子元素均位於投影片內（`0` 頁垂直溢出） |
| **Navigation** | 上／下一頁按鈕、鍵盤 `←`/`→`、頁碼、進度條、目錄總覽 | **PARTIAL** | 翻頁、頁碼（`1 / 11`–`11 / 11`）、進度條（`100%`）與目錄跳轉皆通過；**發現問題 #3**：開啟目錄後再次按 `G` 鍵無法關閉（僅能點關閉或按 `Esc`） |
| **Interactive A** | Slide 3 Punnett Square 計算與預設切換 | **PASS** | 預設 `Aa × Aa`（25% / 50% / 25%）→ 切換 `Aa × AA` 即時更新為 50% / 50% / 0% → 切回 `Aa × Aa` 正常 |
| **Interactive B** | Slide 4 X-linked 親代情境切換 | **PASS** | 切換「父親帶變異 X（`XX × X*Y`）」時 SVG 圖示與說明卡片正確同步更新 |
| **Interactive C** | Slide 7 iGene 350 項即時搜尋與篩選 | **PASS** | 初始 `350 / 350`；搜 `SMN1` → `1 / 350`（#168）；搜 `HBA1` → `1 / 350`（#239 `HBA1/HBA2`）；篩選 `XL` → `28 / 350`；點 `FMR1` → `0 / 350` 並顯示未收錄說明；重設回 `350 / 350` |
| **Interactive D** | Slide 10 5 題互動測驗與計分 | **PASS** | 依序作答 Q1(B)、Q2(C)、Q3(A)、Q4(B)、Q5(B) 均正確顯示解析與 Wiki 出處，分數更新為 `已作答 5 / 5｜正確 5 題`，點重設歸零 `0 / 5` |
| **Mobile Visual (`390×844`)** | Slide 1、Slide 3、Slide 7 響應式版面 | **FAIL（發現 2 項問題）** | **發現問題 #1**：Slide 7 `.slide-head` 未換行，`.head-right` 寬 `303.1 px` 將 `biolove-4.png` 推至 `x: 321.8..401.7` 超出 `390px` 視窗遭裁切，且左側 `.kicker` 被壓縮至 `59 px`。<br>**發現問題 #2**：行動版底部固定控制列遮擋長頁底緣，捲動預留空間偏緊。 |

---

## 修正紀錄與重測原因（Fixes Applied）

因第一輪實機瀏覽器測試抓出 3 項真實缺陷，進行以下修改後觸發第二輪重測：
1. **修正問題 #1（`presentations/ecs-teaching-slides/styles.css`）**：為 `.slide-head` 與 `.head-right` 加入 `flex-wrap: wrap` 與 `max-width: 100%`，並於 `@media (max-width: 860px)` 調整 `.slide-head` 為直向堆疊（`flex-direction: column; align-items: flex-start;`）、`.head-right` 滿寬左右對齊及允許 `.status-badge` 自動換行。
2. **修正問題 #2（`presentations/ecs-teaching-slides/styles.css`）**：於行動版將 `.deck-shell` 底部內距由 `76px` 增加至 `96px`，並收斂 `.controls` 與 `.ctrl-btn` 行動版間距及讓 `.slide-foot` 改為直向排布。
3. **修正問題 #3（`presentations/ecs-teaching-slides/app.js`）**：將鍵盤 `G` 鍵監聽移至 `overviewModal` 開啟阻擋判斷之前，使其可雙向切換開／關目錄總覽。

---

## 第二輪重測結果（Round 2 Re-test — Cache-Bypass Reload）

| 重測項目 | 重測結果 | 實機量測證據 |
| :--- | :---: | :--- |
| **Mobile (`390×844`) Slide 7 `.slide-head` 零裁切** | **PASS** | `.kicker` 佔滿第一列 `width = 339 px`（零壓縮）；`.head-right` 位於第二列 `width = 339 px`；`biolove-4.png` 位於 `x = 284.63..364.5`（**`right = 364.5 px ≤ 390 px`**，零裁切） |
| **Mobile (`390×844`) 底部 `.slide-foot` 與控制列間距** | **PASS** | 捲動至底時 `.slide-foot` 底緣 `y = 726.46`，固定控制列頂緣 `y = 792`，保有 **`65.54 px`** 清楚安全間距 |
| **Mobile 水平捲動檢查** | **PASS** | `bodyWidth = 390`（`<= 390`），無全頁水平溢位 |
| **Desktop (`1280×800`) Slide 7 16:9 回歸檢查** | **PASS** | `.stage` 維持 `1228.80 × 691.20`（`16:9`），`.slide-foot` 完整於投影片內（`footInsideSlide = true`） |
| **鍵盤 `G` 雙向切換目錄總覽** | **PASS** | `false → 按 G → true → 再按 G → false` 正常切換 |
| **Console Errors** | **PASS** | `0` 錯誤 |
