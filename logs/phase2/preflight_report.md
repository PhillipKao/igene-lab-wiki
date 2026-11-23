# Phase 2 Preflight Verification Report（Layout Preflight + Keyboard Interaction Preflight）

- **Run At (UTC)**: `2026-11-23T12:05:02Z`
- **Script**: `workflows/preflight_slides.py`
- **Target**: `presentations/ecs-teaching-slides/`
- **Overall Status**: **PASS**（7 / 7 項通過）

## 1. 目前修正版檔案實測結果（Improved Workflow v2）

| Check ID | Preflight 項目 | 結果 | 實測細節 |
| :--- | :--- | :---: | :--- |
| `LAYOUT-01` | .slide-head 允許換行（防窄螢幕頁首溢位） | **PASS** | Found `flex-wrap: wrap` in `.slide-head` |
| `LAYOUT-02` | 行動版 @media 內 .slide-head 直向堆疊（防 Logo 右緣裁切） | **PASS** | Mobile @media stacks `.slide-head` via `flex-direction: column` |
| `LAYOUT-03` | 行動版底部保留間距 >= 88px（防固定控制列遮擋頁尾） | **PASS** | Mobile `.deck-shell` bottom padding = 96px (>= 88px) |
| `LAYOUT-04` | 11 頁結構與所有本機圖檔／連結路徑有效 | **PASS** | Slides=11, broken_refs=0 |
| `KEY-01` | 靜態檢查：G 鍵目錄切換未被 modal-open 守衛阻擋 | **PASS** | 'g' handler offset (221) precedes modal-open guard (326) |
| `KEY-02` | 靜態檢查：輸入框聚焦時略過全域快捷鍵（防搜尋誤翻頁） | **PASS** | Input/Textarea/Select focus guard present |
| `KEY-03` | JavaScriptCore 模擬事件驗證（G 雙向開關 / Esc / Input 防誤觸 / 左右翻頁） | **PASS** | {"initialHidden": true, "afterFirstG_open": true, "afterSecondG_closed": true, "afterEsc_closed": true, "arrowInInputBlocked": true, "arrowRightAdvances": true, "arrowLeftRetreats": true} |

## 2. 舊版 Round-1 缺陷攔截驗證（Synthetic Round-1 Regression Proof）

為驗證新前置檢查確實能在啟動瀏覽器 QA 之前提前攔截第一輪 3 項真實問題，腳本於記憶體中還原 Round-1 修正前之 CSS／JS 條件並套用同一組 Preflight 規則：
- **提前攔截之規則編號**：`LAYOUT-01, LAYOUT-02, LAYOUT-03, KEY-01, KEY-03`
- **是否完整攔截第一輪全部 3 項問題（行動頁首裁切、底部間距不足、G 鍵無法關閉）**：**YES**

（註：本段標明為針對已記錄 Round-1 缺陷之還原驗證，以與現行檔案實測結果清楚區分。）
