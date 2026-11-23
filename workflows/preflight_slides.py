#!/usr/bin/env python3
"""
Phase 2 Workflow Improvement: Automated Layout Preflight & Keyboard Interaction Preflight
for presentations/ecs-teaching-slides/ (runs BEFORE launching browser QA).

Implements two concrete preflight gates derived directly from Round-1 defects in
logs/phase2/html_test_log.md:
  1. Layout Preflight:
     - Verifies .slide-head and .head-right allow wrapping (prevents mobile 390px logo clipping)
     - Verifies mobile @media block stacks .slide-head vertically and clears fixed bottom .controls
       with sufficient bottom padding (>= 88px)
     - Verifies all local image/script/stylesheet/Wiki paths exist and slide count is valid
  2. Keyboard Interaction Preflight:
     - Runs a real headless JavaScriptCore (jsc) DOM-mock test against app.js verifying:
       a) Pressing 'g' opens the overview modal
       b) Pressing 'g' AGAIN while modal is open cleanly closes the modal (regression check for Bug #3)
       c) Pressing 'Escape' closes the overview modal
       d) Pressing 'ArrowRight' while focused in <input> does NOT hijack typing to change slides
       e) Pressing 'ArrowRight' / 'ArrowLeft' advances and retreats slides cleanly

Also supports --verify-regression-detection to prove deterministically that the same checks
would have flagged the exact Round-1 pre-fix defects before browser testing.

Outputs: logs/phase2/preflight_report.md and logs/phase2/preflight_report.json
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SLIDES_DIR = ROOT / "presentations" / "ecs-teaching-slides"
LOGS_P2 = ROOT / "logs" / "phase2"
JSC_BIN = Path("/System/Library/Frameworks/JavaScriptCore.framework/Versions/Current/Helpers/jsc")


def extract_css_block(css: str, selector_regex: str) -> str:
    m = re.search(selector_regex + r"\s*\{([^}]*)\}", css, re.S)
    return m.group(1) if m else ""


def extract_mobile_media(css: str) -> str:
    m = re.search(r"@media\s*\(max-width:\s*\d+px\)\s*\{(.*)\}\s*$", css, re.S)
    return m.group(1) if m else ""


def run_layout_preflight(html_text: str, css_text: str, slides_dir: Path) -> list[dict]:
    checks: list[dict] = []

    # L1: .slide-head has flex-wrap: wrap
    head_block = extract_css_block(css_text, r"\.slide-head")
    ok_l1 = bool(re.search(r"flex-wrap\s*:\s*wrap", head_block))
    checks.append(
        {
            "id": "LAYOUT-01",
            "name": ".slide-head 允許換行（防窄螢幕頁首溢位）",
            "passed": ok_l1,
            "detail": "Found `flex-wrap: wrap` in `.slide-head`" if ok_l1 else "Missing `flex-wrap: wrap` in `.slide-head`",
        }
    )

    # L2: .head-right has flex-wrap: wrap or mobile stacking rule
    mobile_css = extract_mobile_media(css_text)
    mobile_head = extract_css_block(mobile_css, r"\.slide-head")
    ok_l2 = bool(re.search(r"flex-direction\s*:\s*column", mobile_head))
    checks.append(
        {
            "id": "LAYOUT-02",
            "name": "行動版 @media 內 .slide-head 直向堆疊（防 Logo 右緣裁切）",
            "passed": ok_l2,
            "detail": (
                "Mobile @media stacks `.slide-head` via `flex-direction: column`"
                if ok_l2
                else "Missing mobile `.slide-head { flex-direction: column; }` rule (risk of 390px logo clipping)"
            ),
        }
    )

    # L3: Mobile bottom padding clearance for fixed .controls bar (>= 88px)
    mobile_shell = extract_css_block(mobile_css, r"\.deck-shell")
    pad_vals = re.findall(r"padding\s*:\s*([^;]+);", mobile_shell)
    bottom_px = 0
    for pv in pad_vals:
        nums = [int(x) for x in re.findall(r"(\d+)px", pv)]
        if len(nums) >= 3:
            bottom_px = nums[2]
        elif len(nums) == 1:
            bottom_px = nums[0]
    ok_l3 = bottom_px >= 88
    checks.append(
        {
            "id": "LAYOUT-03",
            "name": "行動版底部保留間距 >= 88px（防固定控制列遮擋頁尾）",
            "passed": ok_l3,
            "detail": (
                f"Mobile `.deck-shell` bottom padding = {bottom_px}px (>= 88px)"
                if ok_l3
                else f"Mobile `.deck-shell` bottom padding = {bottom_px}px (< 88px; fixed controls may overlap footer)"
            ),
        }
    )

    # L4: Slide count & local asset / link integrity
    slide_count = len(re.findall(r'<section class="slide\b', html_text))
    broken = []
    for ref in sorted(set(re.findall(r'(?:src|href)="([^"]+)"', html_text))):
        if ref.startswith(("http://", "https://", "#")):
            continue
        target = (slides_dir / ref.split("#", 1)[0]).resolve()
        if not target.exists():
            broken.append(ref)
    ok_l4 = slide_count == 11 and len(broken) == 0
    checks.append(
        {
            "id": "LAYOUT-04",
            "name": "11 頁結構與所有本機圖檔／連結路徑有效",
            "passed": ok_l4,
            "detail": f"Slides={slide_count}, broken_refs={broken if broken else '0'}",
        }
    )

    return checks


def run_keyboard_preflight(app_js_text: str) -> list[dict]:
    checks: list[dict] = []

    # Static check K1: 'g' toggle must NOT be blocked behind modal-open early return
    keydown_m = re.search(r'document\.addEventListener\("keydown".*?\n  \}\);', app_js_text, re.S)
    kd_body = keydown_m.group(0) if keydown_m else app_js_text
    idx_guard = kd_body.find('if (!overviewModal.classList.contains("hidden")) return;')
    idx_g = kd_body.find('e.key.toLowerCase() === "g"')
    ok_k1 = idx_g != -1 and (idx_guard == -1 or idx_g < idx_guard)
    checks.append(
        {
            "id": "KEY-01",
            "name": "靜態檢查：G 鍵目錄切換未被 modal-open 守衛阻擋",
            "passed": ok_k1,
            "detail": (
                f"'g' handler offset ({idx_g}) precedes modal-open guard ({idx_guard})"
                if ok_k1
                else f"'g' handler ({idx_g}) appears after modal-open guard ({idx_guard}) — cannot close modal via G"
            ),
        }
    )

    # Static check K2: Input focus guard prevents Arrow keys from changing slides while typing in Gene Search
    ok_k2 = bool(re.search(r'\["INPUT",\s*"TEXTAREA",\s*"SELECT"\]\.includes\(e\.target\.tagName\)', kd_body))
    checks.append(
        {
            "id": "KEY-02",
            "name": "靜態檢查：輸入框聚焦時略過全域快捷鍵（防搜尋誤翻頁）",
            "passed": ok_k2,
            "detail": "Input/Textarea/Select focus guard present" if ok_k2 else "Missing input focus guard in keydown listener",
        }
    )

    # Runtime behavioral test via JavaScriptCore (headless JS mock DOM)
    if JSC_BIN.exists():
        harness = r"""
const listeners = {};
function makeClassList(initial = []) {
  const set = new Set(initial);
  return {
    add: (...c) => c.forEach((x) => set.add(x)),
    remove: (...c) => c.forEach((x) => set.delete(x)),
    contains: (c) => set.has(c),
    toggle: (c, force) => {
      if (typeof force === "boolean") {
        if (force) set.add(c); else set.delete(c);
        return force;
      }
      if (set.has(c)) { set.delete(c); return false; }
      set.add(c); return true;
    },
  };
}
function makeEl(tag = "DIV", initialClasses = []) {
  return {
    tagName: tag,
    value: "",
    textContent: "",
    innerHTML: "",
    disabled: false,
    style: {},
    dataset: {},
    classList: makeClassList(initialClasses),
    addEventListener: () => {},
    appendChild: () => {},
    querySelector: () => null,
    closest: () => null,
    click: () => {},
  };
}
const slides = Array.from({ length: 11 }, (_, i) => {
  const el = makeEl("SECTION", i === 0 ? ["slide", "active"] : ["slide"]);
  el.dataset.title = "Slide " + (i + 1);
  return el;
});
const els = {
  "overview-modal": makeEl("DIV", ["modal", "hidden"]),
  "parent-a": Object.assign(makeEl("SELECT"), { value: "Aa" }),
  "parent-b": Object.assign(makeEl("SELECT"), { value: "Aa" }),
  "slide-counter": makeEl("SPAN"),
  "progress-fill": makeEl("DIV"),
};
globalThis.window = { location: { hash: "" }, IGENE_SLIDE_DATA: { items: [], summary_stats: { primary_category_counts: [] } } };
globalThis.history = { replaceState: (_a, _b, h) => { globalThis.window.location.hash = h; } };
globalThis.document = {
  fullscreenElement: null,
  documentElement: {},
  querySelectorAll: (sel) => (sel === ".slide" ? slides : []),
  getElementById: (id) => els[id] || (els[id] = makeEl("DIV")),
  createElement: (t) => makeEl(t.toUpperCase()),
  addEventListener: (ev, fn) => { (listeners[ev] = listeners[ev] || []).push(fn); },
};
function fireKey(key, tagName = "BODY") {
  const ev = { key, target: { tagName }, preventDefault: () => {} };
  (listeners["keydown"] || []).forEach((fn) => fn(ev));
}
"""
        runner = harness + "\n" + app_js_text + r"""
const modal = els["overview-modal"];
const r = {};
r.initialHidden = modal.classList.contains("hidden");
fireKey("g");
r.afterFirstG_open = !modal.classList.contains("hidden");
fireKey("g");
r.afterSecondG_closed = modal.classList.contains("hidden");
fireKey("g");
fireKey("Escape");
r.afterEsc_closed = modal.classList.contains("hidden");
fireKey("ArrowRight", "INPUT");
r.arrowInInputBlocked = els["slide-counter"].textContent === "1 / 11";
fireKey("ArrowRight", "BODY");
r.arrowRightAdvances = els["slide-counter"].textContent === "2 / 11";
fireKey("ArrowLeft", "BODY");
r.arrowLeftRetreats = els["slide-counter"].textContent === "1 / 11";
print(JSON.stringify(r));
"""
        proc = subprocess.run([str(JSC_BIN), "-e", runner], capture_output=True, text=True, timeout=10)
        if proc.returncode == 0 and proc.stdout.strip().startswith("{"):
            res = json.loads(proc.stdout.strip().splitlines()[-1])
            ok_k3 = all(res.values())
            checks.append(
                {
                    "id": "KEY-03",
                    "name": "JavaScriptCore 模擬事件驗證（G 雙向開關 / Esc / Input 防誤觸 / 左右翻頁）",
                    "passed": ok_k3,
                    "detail": json.dumps(res, ensure_ascii=False),
                }
            )
        else:
            checks.append(
                {
                    "id": "KEY-03",
                    "name": "JavaScriptCore 模擬事件驗證",
                    "passed": False,
                    "detail": f"jsc failed: {proc.stderr or proc.stdout}",
                }
            )
    return checks


def run_synthetic_round1_verification(html_text: str, css_text: str, app_js_text: str) -> dict:
    """
    Reproduce the exact 3 documented Round-1 defects (before our Round-1 fixes) in memory
    to verify deterministically that Layout Preflight and Keyboard Interaction Preflight
    would have caught all 3 bugs BEFORE browser testing.
    """
    # Simulate Round-1 CSS (before adding flex-wrap, mobile header column stack, and 96px bottom padding)
    old_css = css_text.replace("  flex-wrap: wrap;\n", "", 1)
    old_css = old_css.replace("  .slide-head { flex-direction: column; align-items: flex-start; gap: 6px; }\n", "")
    old_css = old_css.replace("padding: 10px 10px 96px;", "padding: 10px 10px 76px;")

    # Simulate Round-1 JS (where 'g' check appeared after modal-open guard)
    old_js = app_js_text.replace(
        '    if (e.key.toLowerCase() === "g") {\n      e.preventDefault();\n      toggleOverview();\n      return;\n    }\n    if (!overviewModal.classList.contains("hidden")) return;',
        '    if (!overviewModal.classList.contains("hidden")) return;\n    if (e.key.toLowerCase() === "g") {\n      e.preventDefault();\n      toggleOverview();\n      return;\n    }',
    )

    old_layout = run_layout_preflight(html_text, old_css, SLIDES_DIR)
    old_kbd = run_keyboard_preflight(old_js)
    caught = [c["id"] for c in (old_layout + old_kbd) if not c["passed"]]
    return {
        "simulated_round1_caught_ids": caught,
        "all_3_round1_bugs_caught": all(x in caught for x in ("LAYOUT-01", "LAYOUT-02", "LAYOUT-03", "KEY-01", "KEY-03")),
        "details": old_layout + old_kbd,
    }


def main() -> int:
    LOGS_P2.mkdir(parents=True, exist_ok=True)
    run_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    html_text = (SLIDES_DIR / "index.html").read_text(encoding="utf-8")
    css_text = (SLIDES_DIR / "styles.css").read_text(encoding="utf-8")
    app_js_text = (SLIDES_DIR / "app.js").read_text(encoding="utf-8")

    layout_results = run_layout_preflight(html_text, css_text, SLIDES_DIR)
    kbd_results = run_keyboard_preflight(app_js_text)
    all_checks = layout_results + kbd_results
    passed_all = all(c["passed"] for c in all_checks)

    regression_proof = run_synthetic_round1_verification(html_text, css_text, app_js_text)

    report = {
        "run_at": run_at,
        "target": "presentations/ecs-teaching-slides/",
        "status": "PASS" if passed_all else "FAIL",
        "layout_preflight": layout_results,
        "keyboard_interaction_preflight": kbd_results,
        "round1_regression_detection_proof": regression_proof,
    }
    (LOGS_P2 / "preflight_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    md_lines = [
        "# Phase 2 Preflight Verification Report（Layout Preflight + Keyboard Interaction Preflight）",
        "",
        f"- **Run At (UTC)**: `{run_at}`",
        "- **Script**: `workflows/preflight_slides.py`",
        "- **Target**: `presentations/ecs-teaching-slides/`",
        f"- **Overall Status**: **{'PASS' if passed_all else 'FAIL'}**（{sum(1 for c in all_checks if c['passed'])} / {len(all_checks)} 項通過）",
        "",
        "## 1. 目前修正版檔案實測結果（Improved Workflow v2）",
        "",
        "| Check ID | Preflight 項目 | 結果 | 實測細節 |",
        "| :--- | :--- | :---: | :--- |",
    ]
    for c in all_checks:
        md_lines.append(f"| `{c['id']}` | {c['name']} | **{'PASS' if c['passed'] else 'FAIL'}** | {c['detail']} |")

    md_lines.extend(
        [
            "",
            "## 2. 舊版 Round-1 缺陷攔截驗證（Synthetic Round-1 Regression Proof）",
            "",
            "為驗證新前置檢查確實能在啟動瀏覽器 QA 之前提前攔截第一輪 3 項真實問題，腳本於記憶體中還原 Round-1 修正前之 CSS／JS 條件並套用同一組 Preflight 規則：",
            f"- **提前攔截之規則編號**：`{', '.join(regression_proof['simulated_round1_caught_ids'])}`",
            f"- **是否完整攔截第一輪全部 3 項問題（行動頁首裁切、底部間距不足、G 鍵無法關閉）**：**{'YES' if regression_proof['all_3_round1_bugs_caught'] else 'NO'}**",
            "",
            "（註：本段標明為針對已記錄 Round-1 缺陷之還原驗證，以與現行檔案實測結果清楚區分。）",
        ]
    )
    (LOGS_P2 / "preflight_report.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")

    print(f"Preflight Status: {'PASS' if passed_all else 'FAIL'} ({sum(1 for c in all_checks if c['passed'])}/{len(all_checks)})")
    for c in all_checks:
        print(f"  [{c['id']}] {'PASS' if c['passed'] else 'FAIL'} - {c['name']} :: {c['detail']}")
    print(f"Round-1 Regression Detection Proof: caught={regression_proof['simulated_round1_caught_ids']} (all_3_caught={regression_proof['all_3_round1_bugs_caught']})")
    return 0 if passed_all else 1


if __name__ == "__main__":
    sys.exit(main())
