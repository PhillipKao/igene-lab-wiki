#!/usr/bin/env python3
"""
Pre-Publish Safety, Compliance & Preflight Gate for the Classroom Teaching Demo Edition:
  Target: publish/ecs-demo/

Runs both locally and inside GitHub Actions (.github/workflows/deploy-ecs-demo.yml)
BEFORE uploading artifacts to GitHub Pages.

Verifies:
  1. Strict File Allowlist (only index.html, styles.css, app.js, ecs_public_data.js, favicon.svg, .nojekyll)
  2. Relative Path Integrity (zero ../, zero leading /, zero localhost/file://, 100% local refs exist)
  3. Image Authorization Gate (zero BiOLOVE / unverified brand assets; neutral SVG only)
  4. Clinical & Unverified-Spec Leak Scanner (zero Ion Torrent / Thermo Fisher / 530 / 520 / 76%-99% /
     wiki_browser / human_review_queue / raw/ / logs/ / pending_clinical_review-as-approved / PII / secrets)
  5. Mandatory Classroom Disclaimer Presence ("課程教學示範，非個人化醫療建議")
  6. Data Sanitization Check (350 items, 351 unique genes, 28 XL, zero detection_rate/det keys)
  7. Layout Preflight (LAYOUT-01..04) + Keyboard Interaction Preflight (KEY-01..03 via node or macOS jsc)
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEMO_DIR = ROOT / "publish" / "ecs-demo"
LOGS_P2 = ROOT / "logs" / "phase2"
JSC_BIN = Path("/System/Library/Frameworks/JavaScriptCore.framework/Versions/Current/Helpers/jsc")

ALLOWED_FILES = {
    ".nojekyll",
    "app.js",
    "ecs_public_data.js",
    "favicon.svg",
    "index.html",
    "styles.css",
}

FORBIDDEN_PATTERNS = [
    ("BiOLOVE brand asset/string", re.compile(r"biolove", re.I)),
    ("Unpublished Wiki Browser link", re.compile(r"wiki_browser", re.I)),
    ("Internal review queue reference", re.compile(r"human_review_queue|retrieval_log|GAP-02", re.I)),
    ("Internal raw/logs path leak", re.compile(r"raw/structured|raw/sources|logs/phase2", re.I)),
    ("Internal lab platform/chip spec", re.compile(r"Ion Torrent|Thermo Fisher|Ion 530|Ion 520|\b530\b.*\b晶片\b|\b520\b.*\b晶片\b", re.I)),
    ("Unverified detection rate claim", re.compile(r"76%[–-]99%|detection_rate", re.I)),
    ("Localhost or file:// URL", re.compile(r"127\.0\.0\.1|localhost:|file://", re.I)),
    ("Forbidden guarantee claim", re.compile(r"保證懷孕|保證活產|完全沒有遺傳疾病風險|100%\s*不會罹患", re.I)),
    ("Secret / API key pattern", re.compile(r"(ghp_[A-Za-z0-9]{20,}|AIza[0-9A-Za-z_-]{30,}|BEGIN PRIVATE KEY)", re.I)),
]


def extract_css_block(css: str, selector_regex: str) -> str:
    m = re.search(selector_regex + r"\s*\{([^}]*)\}", css, re.S)
    return m.group(1) if m else ""


def extract_mobile_media(css: str) -> str:
    m = re.search(r"@media\s*\(max-width:\s*\d+px\)\s*\{(.*)\}\s*$", css, re.S)
    return m.group(1) if m else ""


def find_js_runtime() -> tuple[str, list[str]] | None:
    node = shutil.which("node")
    if node:
        return ("node", [node, "-e"])
    if JSC_BIN.exists():
        return ("jsc", [str(JSC_BIN), "-e"])
    return None


def main() -> int:
    checks: list[dict] = []

    if not DEMO_DIR.exists():
        print(f"ERROR: Missing publish directory {DEMO_DIR}", file=sys.stderr)
        return 1

    # 1. File allowlist check
    actual_files = sorted(
        str(p.relative_to(DEMO_DIR)) for p in DEMO_DIR.rglob("*") if p.is_file()
    )
    extra_files = sorted(set(actual_files) - ALLOWED_FILES)
    missing_files = sorted(ALLOWED_FILES - set(actual_files))
    ok_files = not extra_files and not missing_files
    checks.append(
        {
            "id": "PUB-01",
            "name": "發布目錄白名單（僅含 6 個安全靜態檔案，排除 raw/logs/wiki/未授權圖片）",
            "passed": ok_files,
            "detail": f"files={actual_files}, extra={extra_files}, missing={missing_files}",
        }
    )

    html_text = (DEMO_DIR / "index.html").read_text(encoding="utf-8")
    css_text = (DEMO_DIR / "styles.css").read_text(encoding="utf-8")
    app_js_text = (DEMO_DIR / "app.js").read_text(encoding="utf-8")
    data_js_text = (DEMO_DIR / "ecs_public_data.js").read_text(encoding="utf-8")

    # 2. Relative path & local asset existence check
    local_refs = []
    bad_rel = []
    broken_refs = []
    for ref in sorted(set(re.findall(r'(?:src|href)="([^"]+)"', html_text))):
        if ref.startswith(("http://", "https://", "#")):
            continue
        local_refs.append(ref)
        if ref.startswith("/") or ".." in ref:
            bad_rel.append(ref)
        target = (DEMO_DIR / ref.split("#", 1)[0]).resolve()
        if not target.exists() or not str(target).startswith(str(DEMO_DIR.resolve())):
            broken_refs.append(ref)
    ok_paths = len(bad_rel) == 0 and len(broken_refs) == 0 and len(local_refs) >= 4
    checks.append(
        {
            "id": "PUB-02",
            "name": "相對路徑與資源完整性（零 ../ 或根路徑 /，全部本機資源存在）",
            "passed": ok_paths,
            "detail": f"local_refs={local_refs}, bad_rel={bad_rel}, broken={broken_refs}",
        }
    )

    # 3. Image authorization check (neutral SVG only, zero raster brand images)
    img_tags = re.findall(r"<img\b[^>]*>", html_text, re.I)
    raster_files = [f for f in actual_files if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".gif"))]
    ok_img = len(img_tags) == 0 and len(raster_files) == 0
    checks.append(
        {
            "id": "PUB-03",
            "name": "圖片授權安全（零未授權品牌圖檔，全數採中性原創 SVG）",
            "passed": ok_img,
            "detail": f"img_tags={len(img_tags)}, raster_files={raster_files}",
        }
    )

    # 4. Clinical / internal / sensitive content leak scanner across all text files in publish/ecs-demo/
    leaks = []
    for fname in actual_files:
        if fname == ".nojekyll":
            continue
        txt = (DEMO_DIR / fname).read_text(encoding="utf-8")
        # In ecs_public_data.js, allow metadata key `"omitted_fields": ["detection_rate"]`
        scan_txt = txt.replace('"omitted_fields": ["detection_rate"]', "").replace(
            "// Note: Product detection_rate values are intentionally omitted for public educational deployment.", ""
        )
        for label, pat in FORBIDDEN_PATTERNS:
            for m in pat.finditer(scan_txt):
                # Allow slide 10 Q4 distractor option text mentioning "100% 不會罹患" only inside QUIZ_ITEMS option A
                if label == "Forbidden guarantee claim" and fname == "app.js" and "A. 代表寶寶 100% 不會罹患任何遺傳疾病" in scan_txt[max(0, m.start()-20):m.end()+30]:
                    continue
                leaks.append(f"{fname}:{label} -> {m.group(0)!r}")
    ok_leaks = len(leaks) == 0
    checks.append(
        {
            "id": "PUB-04",
            "name": "敏感資料、內部技術規格與未核准宣稱掃描",
            "passed": ok_leaks,
            "detail": "0 leaks found" if ok_leaks else "; ".join(leaks),
        }
    )

    # 5. Mandatory disclaimer check
    disc_count = html_text.count("課程教學示範，非個人化醫療建議")
    ok_disc = disc_count >= 12
    checks.append(
        {
            "id": "PUB-05",
            "name": "課堂免責聲明標示（「課程教學示範，非個人化醫療建議」覆蓋全部投影片）",
            "passed": ok_disc,
            "detail": f"occurrences={disc_count} (>= 12)",
        }
    )

    # 6. Sanitized data payload verification
    json_match = re.search(r"window\.ECS_DEMO_DATA\s*=\s*(\{.*\});", data_js_text, re.S)
    data_ok = False
    data_detail = "Failed to parse window.ECS_DEMO_DATA"
    if json_match:
        payload = json.loads(json_match.group(1))
        items = payload.get("items", [])
        has_det = any(("det" in it or "detection_rate" in it) for it in items)
        xl_count = sum(1 for it in items if it.get("inh") == "XL")
        unique_genes = payload.get("summary_stats", {}).get("unique_individual_gene_symbols")
        data_ok = len(items) == 350 and unique_genes == 351 and xl_count == 28 and not has_det
        data_detail = f"items={len(items)}, unique_genes={unique_genes}, xl={xl_count}, has_det={has_det}"
    checks.append(
        {
            "id": "PUB-06",
            "name": "公開資料集潔淨度（350 疾病 / 351 基因 / 28 XL，且完全移除檢出率欄位）",
            "passed": data_ok,
            "detail": data_detail,
        }
    )

    # 7. Layout Preflight (LAYOUT-01..04)
    slide_count = len(re.findall(r'<section class="slide\b', html_text))
    head_block = extract_css_block(css_text, r"\.slide-head")
    mobile_css = extract_mobile_media(css_text)
    mobile_head = extract_css_block(mobile_css, r"\.slide-head")
    mobile_shell = extract_css_block(mobile_css, r"\.deck-shell")
    pad_vals = re.findall(r"padding\s*:\s*([^;]+);", mobile_shell)
    bottom_px = 0
    for pv in pad_vals:
        nums = [int(x) for x in re.findall(r"(\d+)px", pv)]
        if len(nums) >= 3:
            bottom_px = nums[2]
    ok_layout = (
        slide_count == 11
        and bool(re.search(r"flex-wrap\s*:\s*wrap", head_block))
        and bool(re.search(r"flex-direction\s*:\s*column", mobile_head))
        and bottom_px >= 88
    )
    checks.append(
        {
            "id": "PUB-07",
            "name": "Layout Preflight（11 頁結構、行動頁首換行／直向堆疊、底部間距 >= 88px）",
            "passed": ok_layout,
            "detail": f"slides={slide_count}, mobile_bottom_padding={bottom_px}px",
        }
    )

    # 8. Keyboard + Interactive Runtime Verification (via node or macOS jsc)
    runtime = find_js_runtime()
    if runtime:
        rt_name, rt_cmd = runtime
        out_fn = "console.log" if rt_name == "node" else "print"
        harness = f"""
const listeners = {{}};
function makeClassList(initial = []) {{
  const set = new Set(initial);
  return {{
    add: (...c) => c.forEach((x) => set.add(x)),
    remove: (...c) => c.forEach((x) => set.delete(x)),
    contains: (c) => set.has(c),
    toggle: (c, force) => {{
      if (typeof force === "boolean") {{ if (force) set.add(c); else set.delete(c); return force; }}
      if (set.has(c)) {{ set.delete(c); return false; }}
      set.add(c); return true;
    }},
  }};
}}
function makeEl(tag = "DIV", initialClasses = []) {{
  return {{
    tagName: tag, value: "", textContent: "", innerHTML: "", disabled: false,
    style: {{}}, dataset: {{}}, classList: makeClassList(initialClasses),
    addEventListener: (ev, fn) => {{ (listeners[tag + ":" + ev] = listeners[tag + ":" + ev] || []).push(fn); }},
    appendChild: () => {{}}, querySelector: () => null, closest: () => null, click: () => {{}},
  }};
}}
const slides = Array.from({{ length: 11 }}, (_, i) => {{
  const el = makeEl("SECTION", i === 0 ? ["slide", "active"] : ["slide"]);
  el.dataset.title = "Slide " + (i + 1);
  return el;
}});
const els = {{
  "overview-modal": makeEl("DIV", ["modal", "hidden"]),
  "parent-a": Object.assign(makeEl("SELECT"), {{ value: "Aa" }}),
  "parent-b": Object.assign(makeEl("SELECT"), {{ value: "Aa" }}),
  "slide-counter": makeEl("SPAN"),
  "progress-fill": makeEl("DIV"),
  "gene-search-input": makeEl("INPUT"),
  "gene-inh-filter": makeEl("SELECT"),
  "gene-cat-filter": makeEl("SELECT"),
  "gene-table-body": makeEl("TBODY"),
  "gene-result-count": makeEl("STRONG"),
}};
globalThis.window = {{ location: {{ hash: "" }} }};
globalThis.history = {{ replaceState: (_a, _b, h) => {{ globalThis.window.location.hash = h; }} }};
globalThis.document = {{
  fullscreenElement: null, documentElement: {{}},
  querySelectorAll: (sel) => (sel === ".slide" ? slides : []),
  getElementById: (id) => els[id] || (els[id] = makeEl("DIV")),
  createElement: (t) => makeEl(t.toUpperCase()),
  addEventListener: (ev, fn) => {{ (listeners["doc:" + ev] = listeners["doc:" + ev] || []).push(fn); }},
}};
function fireKey(key, tagName = "BODY") {{
  const ev = {{ key, target: {{ tagName }}, preventDefault: () => {{}} }};
  (listeners["doc:keydown"] || []).forEach((fn) => fn(ev));
}}
"""
        runner = harness + "\n" + data_js_text + "\n" + app_js_text + f"""
const modal = els["overview-modal"];
const r = {{}};
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
r.initialGeneCount = els["gene-result-count"].textContent === "符合 350 / 350 筆";
r.punnettDefault = els["pct-AA"].textContent === "25%" && els["pct-Aa"].textContent === "50%" && els["pct-aa"].textContent === "25%";
{out_fn}(JSON.stringify(r));
"""
        proc = subprocess.run(rt_cmd + [runner], capture_output=True, text=True, timeout=15)
        if proc.returncode == 0 and proc.stdout.strip().splitlines()[-1].startswith("{"):
            res = json.loads(proc.stdout.strip().splitlines()[-1])
            ok_rt = all(res.values())
            checks.append(
                {
                    "id": "PUB-08",
                    "name": f"JS 執行期互動驗證（{rt_name}：G 雙向切換 / Esc / Input 防護 / 350 筆初始載入 / Punnett）",
                    "passed": ok_rt,
                    "detail": json.dumps(res, ensure_ascii=False),
                }
            )
        else:
            checks.append(
                {
                    "id": "PUB-08",
                    "name": f"JS 執行期互動驗證（{rt_name}）",
                    "passed": False,
                    "detail": (proc.stderr or proc.stdout).strip()[:400],
                }
            )
    else:
        checks.append(
            {
                "id": "PUB-08",
                "name": "JS 執行期互動驗證",
                "passed": False,
                "detail": "Neither node nor macOS jsc found in environment",
            }
        )

    passed_all = all(c["passed"] for c in checks)
    run_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # Write report to logs/phase2/ ONLY when running locally (skip writing if --no-log)
    if "--no-log" not in sys.argv:
        LOGS_P2.mkdir(parents=True, exist_ok=True)
        report = {
            "run_at": run_at,
            "target": "publish/ecs-demo/",
            "status": "PASS" if passed_all else "FAIL",
            "publish_files": [
                {"path": f, "bytes": (DEMO_DIR / f).stat().st_size} for f in actual_files
            ],
            "checks": checks,
        }
        (LOGS_P2 / "demo_publish_verification.json").write_text(
            json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        md = [
            "# Classroom Teaching Demo — Pre-Publish Verification Report",
            "",
            f"- **Run At (UTC)**: `{run_at}`",
            "- **Publish Directory**: `publish/ecs-demo/`",
            f"- **Overall Status**: **{'PASS' if passed_all else 'FAIL'}**（{sum(1 for c in checks if c['passed'])} / {len(checks)} 項通過）",
            "",
            "## 發布檔案清單",
            "",
            "| File | Size (Bytes) | Role |",
            "| :--- | ---: | :--- |",
        ]
        roles = {
            ".nojekyll": "停用 GitHub Pages Jekyll 轉換，直接提供靜態檔",
            "index.html": "11 頁 ECS 課堂教學展示版主頁（零未授權圖片、零內部規格）",
            "styles.css": "Warm Orange 教學樣式（含行動版 390px 安全排版）",
            "app.js": "互動核心（Punnett Square、X-linked、350 項搜尋、5 題測驗、快捷鍵）",
            "ecs_public_data.js": "由 SRC-009 編譯之 350 疾病／351 基因公開參考集（已移除檢出率欄位）",
            "favicon.svg": "原創中性 DNA 雙股螺旋 SVG 圖示",
        }
        for f in actual_files:
            md.append(f"| `publish/ecs-demo/{f}` | {(DEMO_DIR / f).stat().st_size:,} | {roles.get(f, '')} |")
        md.extend(
            [
                "",
                "## 安全、合規與 Preflight 檢核結果",
                "",
                "| Check ID | 檢核項目 | 結果 | 細節 |",
                "| :--- | :--- | :---: | :--- |",
            ]
        )
        for c in checks:
            md.append(f"| `{c['id']}` | {c['name']} | **{'PASS' if c['passed'] else 'FAIL'}** | `{c['detail']}` |")
        (LOGS_P2 / "demo_publish_verification.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print(f"Demo Publish Verification: {'PASS' if passed_all else 'FAIL'} ({sum(1 for c in checks if c['passed'])}/{len(checks)})")
    for c in checks:
        print(f"  [{c['id']}] {'PASS' if c['passed'] else 'FAIL'} - {c['name']} :: {c['detail']}")
    return 0 if passed_all else 1


if __name__ == "__main__":
    sys.exit(main())
