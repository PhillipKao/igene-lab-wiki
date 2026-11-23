#!/usr/bin/env python3
"""
Basic quality & integrity linter for the Reproductive Genetics & Laboratory Wiki.
Validates:
1. Raw sources registry, authentic file existence, and live SHA-256 digests
2. YAML frontmatter completeness across all wiki knowledge pages
3. Source ID & in-text [SRC-XXX] citation traceability
4. Internal Markdown links, related_pages paths, and image asset paths
5. Duplicate title/slug detection
6. wiki/index.md coverage of all wiki pages
7. Inventory of pending_clinical_review / draft high-risk pages & queue tracking
Outputs: logs/lint_report.md and logs/lint_report.json
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "raw"
WIKI_DIR = ROOT / "wiki"
LOGS_DIR = ROOT / "logs"

CATEGORIES = ("products", "concepts", "evidence", "laboratory", "faq")
REQUIRED_FIELDS = (
    "title",
    "category",
    "summary",
    "source_ids",
    "created_at",
    "updated_at",
    "review_status",
    "related_pages",
)
VALID_REVIEW_STATUS = {
    "auto_compiled",
    "source_verified",
    "product_spec_verified",
    "pending_clinical_review",
    "pending_technical_verification",
    "draft",
    "approved",
}
VALID_REVIEW_LAYERS = {
    "source_verified",
    "product_spec_verified",
    "pending_clinical_review",
    "pending_technical_verification",
    "approved",
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_frontmatter(text: str) -> tuple[dict, str, str | None]:
    if not text.startswith("---\n"):
        return {}, text, "Missing YAML frontmatter opening '---'"
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text, "Missing YAML frontmatter closing '---'"
    fm_raw = text[4:end]
    body = text[end + 5 :]
    data: dict = {}
    current_list_key: str | None = None
    for raw_line in fm_raw.splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - ") or line.startswith("- "):
            if current_list_key is None:
                return {}, body, f"List item without key: {line}"
            val = line.split("- ", 1)[1].strip().strip('"').strip("'")
            data[current_list_key].append(val)
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            k = k.strip()
            v = v.strip()
            if v == "":
                data[k] = []
                current_list_key = k
            else:
                data[k] = v.strip('"').strip("'")
                current_list_key = None
    return data, body, None


def strip_fragment(target: str) -> str:
    return target.split("#", 1)[0].strip()


def main() -> int:
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    run_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    errors: list[str] = []
    warnings: list[str] = []
    stats: dict = {
        "run_at": run_at,
        "raw_sources_total": 0,
        "raw_sources_ingested": 0,
        "raw_sources_sha256_verified": 0,
        "wiki_pages_total": 0,
        "wiki_pages_by_category": {},
        "internal_links_checked": 0,
        "image_links_checked": 0,
        "citations_checked": 0,
        "pending_review_pages": [],
        "auto_compiled_pages": [],
    }

    # 1. Validate raw/registry.json and SHA-256 digests
    registry_path = RAW_DIR / "registry.json"
    valid_sources: dict[str, dict] = {}
    if not registry_path.exists():
        errors.append("Missing raw/registry.json")
    else:
        reg = json.loads(registry_path.read_text(encoding="utf-8"))
        sources = reg.get("sources", [])
        stats["raw_sources_total"] = len(sources)
        for s in sources:
            sid = s.get("source_id", "")
            status = s.get("status", "")
            valid_sources[sid] = s
            if status == "ingested":
                stats["raw_sources_ingested"] += 1
            if status in ("ingested", "partially_retrieved"):
                raw_rel = s.get("raw_file", "")
                raw_abs = ROOT / raw_rel if raw_rel else None
                if not raw_abs or not raw_abs.exists():
                    errors.append(f"[{sid}] Marked '{status}' but raw_file missing: {raw_rel}")
                else:
                    actual_sha = sha256_file(raw_abs)
                    if actual_sha != s.get("sha256"):
                        errors.append(
                            f"[{sid}] SHA-256 mismatch for {raw_rel}: expected {s.get('sha256')}, got {actual_sha}"
                        )
                    else:
                        stats["raw_sources_sha256_verified"] += 1
                    if raw_abs.stat().st_size < 400:
                        errors.append(f"[{sid}] Raw file too small ({raw_abs.stat().st_size} bytes)")
                for sf in s.get("structured_files", []):
                    sf_rel = sf.get("path", "")
                    sf_abs = ROOT / sf_rel if sf_rel else None
                    if not sf_abs or not sf_abs.exists():
                        errors.append(f"[{sid}] Missing structured file: {sf_rel}")
                    elif sha256_file(sf_abs) != sf.get("sha256"):
                        errors.append(f"[{sid}] SHA-256 mismatch for structured file {sf_rel}")
            else:
                warnings.append(f"[{sid}] Status is '{status}': {s.get('reason', '')}")

        if stats["raw_sources_ingested"] < 5:
            errors.append(
                f"Minimum acceptance threshold not met: only {stats['raw_sources_ingested']} sources ingested (need >= 5)"
            )

    # 2. Scan all wiki pages
    wiki_pages: list[Path] = []
    for cat in CATEGORIES:
        cat_dir = WIKI_DIR / cat
        pages = sorted(cat_dir.glob("*.md")) if cat_dir.exists() else []
        stats["wiki_pages_by_category"][cat] = len(pages)
        if not pages:
            errors.append(f"Category directory wiki/{cat}/ has no Markdown pages")
        wiki_pages.extend(pages)

    stats["wiki_pages_total"] = len(wiki_pages)

    seen_titles: dict[str, str] = {}
    seen_slugs: dict[str, str] = {}

    # Check index.md links too
    index_path = WIKI_DIR / "index.md"
    index_text = index_path.read_text(encoding="utf-8") if index_path.exists() else ""
    if not index_text:
        errors.append("Missing wiki/index.md")

    # Verify links & images in index.md and log.md
    for special in (WIKI_DIR / "index.md", WIKI_DIR / "log.md"):
        if not special.exists():
            errors.append(f"Missing {special.relative_to(ROOT)}")
            continue
        stext = special.read_text(encoding="utf-8")
        for m in re.finditer(r"(!?)\[[^\]]*\]\(([^)]+)\)", stext):
            is_img = m.group(1) == "!"
            raw_target = m.group(2).strip()
            if raw_target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean_target = strip_fragment(raw_target)
            if not clean_target:
                continue
            resolved = (special.parent / clean_target).resolve()
            if is_img:
                stats["image_links_checked"] += 1
            else:
                stats["internal_links_checked"] += 1
            if not resolved.exists():
                errors.append(f"{special.relative_to(ROOT)}: Broken {'image' if is_img else 'link'} -> {raw_target}")

    # Load human_review_queue.md for tracking check
    queue_path = LOGS_DIR / "human_review_queue.md"
    queue_text = queue_path.read_text(encoding="utf-8") if queue_path.exists() else ""
    if not queue_text:
        warnings.append("Missing logs/human_review_queue.md")

    for page in wiki_pages:
        rel = page.relative_to(ROOT).as_posix()
        rel_from_wiki = page.relative_to(WIKI_DIR).as_posix()
        expected_cat = page.parent.name
        text = page.read_text(encoding="utf-8")

        fm, body, fm_err = parse_frontmatter(text)
        if fm_err:
            errors.append(f"{rel}: {fm_err}")
            continue

        # Required frontmatter fields
        for field in REQUIRED_FIELDS:
            val = fm.get(field)
            if val is None or val == "" or (isinstance(val, list) and len(val) == 0):
                errors.append(f"{rel}: Missing or empty frontmatter field '{field}'")

        # Category check
        if fm.get("category") != expected_cat:
            errors.append(f"{rel}: Frontmatter category '{fm.get('category')}' != folder '{expected_cat}'")

        # Review status & optional multi-layer review_layers check
        rstatus = fm.get("review_status", "")
        rlayers = fm.get("review_layers", [])
        if rlayers and isinstance(rlayers, list):
            for layer in rlayers:
                if layer not in VALID_REVIEW_LAYERS:
                    errors.append(f"{rel}: Invalid review_layers value '{layer}'")

        if rstatus not in VALID_REVIEW_STATUS:
            errors.append(f"{rel}: Invalid review_status '{rstatus}'")
        elif rstatus in ("pending_clinical_review", "pending_technical_verification", "draft") or (
            isinstance(rlayers, list)
            and any(l in ("pending_clinical_review", "pending_technical_verification") for l in rlayers)
        ):
            stats["pending_review_pages"].append(
                {
                    "page": rel,
                    "status": rstatus,
                    "layers": rlayers if isinstance(rlayers, list) else [],
                    "title": fm.get("title", ""),
                }
            )
            if queue_text and rel not in queue_text:
                warnings.append(f"{rel}: Requires review ('{rstatus}') but not listed in logs/human_review_queue.md")
        elif rstatus == "auto_compiled":
            stats["auto_compiled_pages"].append({"page": rel, "status": rstatus, "title": fm.get("title", "")})

        # Duplicate title / slug checks
        title_norm = str(fm.get("title", "")).strip().lower()
        if title_norm in seen_titles:
            errors.append(f"{rel}: Duplicate title with {seen_titles[title_norm]} ('{fm.get('title')}')")
        else:
            seen_titles[title_norm] = rel

        slug = page.stem.lower()
        if slug in seen_slugs:
            errors.append(f"{rel}: Duplicate slug '{slug}' with {seen_slugs[slug]}")
        else:
            seen_slugs[slug] = rel

        # Source IDs in frontmatter
        fm_sids = fm.get("source_ids", [])
        if isinstance(fm_sids, list):
            for sid in fm_sids:
                stats["citations_checked"] += 1
                if sid not in valid_sources:
                    errors.append(f"{rel}: Frontmatter source_id '{sid}' not found in raw/registry.json")
                elif valid_sources[sid].get("status") not in ("ingested", "partially_retrieved"):
                    errors.append(f"{rel}: Frontmatter source_id '{sid}' was not successfully retrieved")

        # In-text [SRC-XXX] citations
        body_sids = re.findall(r"\[(SRC-\d{3})\]", body)
        if not body_sids:
            errors.append(f"{rel}: No in-text [SRC-XXX] citations found in page body")
        else:
            for sid in set(body_sids):
                stats["citations_checked"] += 1
                if sid not in valid_sources:
                    errors.append(f"{rel}: In-text citation '[{sid}]' not found in raw/registry.json")
                elif valid_sources[sid].get("status") not in ("ingested", "partially_retrieved"):
                    errors.append(f"{rel}: In-text citation '[{sid}]' refers to non-retrieved source")
                if isinstance(fm_sids, list) and sid not in fm_sids:
                    warnings.append(f"{rel}: In-text citation '[{sid}]' not listed in frontmatter source_ids")

        # related_pages verification
        rel_pages = fm.get("related_pages", [])
        if isinstance(rel_pages, list):
            for rp in rel_pages:
                stats["internal_links_checked"] += 1
                target = (page.parent / rp).resolve()
                if not target.exists():
                    errors.append(f"{rel}: Broken related_pages target '{rp}'")

        # Body Markdown links & image paths
        for m in re.finditer(r"(!?)\[[^\]]*\]\(([^)]+)\)", body):
            is_img = m.group(1) == "!"
            raw_target = m.group(2).strip()
            if raw_target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean_target = strip_fragment(raw_target)
            if not clean_target:
                continue
            resolved = (page.parent / clean_target).resolve()
            if is_img:
                stats["image_links_checked"] += 1
            else:
                stats["internal_links_checked"] += 1
            if not resolved.exists():
                errors.append(f"{rel}: Broken {'image' if is_img else 'link'} -> {raw_target}")

        # Index coverage check
        if index_text and f"({rel_from_wiki})" not in index_text:
            errors.append(f"{rel}: Not linked in wiki/index.md (expected '({rel_from_wiki})')")

    # Write JSON report
    json_report = {
        "status": "PASS" if not errors else "FAIL",
        "stats": stats,
        "errors": errors,
        "warnings": warnings,
    }
    (LOGS_DIR / "lint_report.json").write_text(
        json.dumps(json_report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    # Write Markdown report
    md_lines = [
        "# Wiki Lint & Quality Verification Report",
        "",
        f"- **Run At (UTC)**: `{run_at}`",
        f"- **Overall Status**: **{'PASS (0 Errors)' if not errors else f'FAIL ({len(errors)} Errors)'}**",
        f"- **Warnings**: {len(warnings)}",
        "",
        "## Summary Metrics",
        "",
        f"- Raw Sources Total: **{stats['raw_sources_total']}** (Ingested: **{stats['raw_sources_ingested']}**, SHA-256 Verified: **{stats['raw_sources_sha256_verified']}**)",
        f"- Wiki Knowledge Pages Total: **{stats['wiki_pages_total']}**",
        f"  - `products`: {stats['wiki_pages_by_category'].get('products', 0)}",
        f"  - `concepts`: {stats['wiki_pages_by_category'].get('concepts', 0)}",
        f"  - `evidence`: {stats['wiki_pages_by_category'].get('evidence', 0)}",
        f"  - `laboratory`: {stats['wiki_pages_by_category'].get('laboratory', 0)}",
        f"  - `faq`: {stats['wiki_pages_by_category'].get('faq', 0)}",
        f"- Internal Links Checked: **{stats['internal_links_checked']}**",
        f"- Image Asset Paths Checked: **{stats['image_links_checked']}**",
        f"- Source Citations Checked: **{stats['citations_checked']}**",
        f"- Pending Clinical Review Pages: **{len(stats['pending_review_pages'])}**",
        f"- Auto-Compiled Foundation Pages: **{len(stats['auto_compiled_pages'])}**",
        "",
        "## Errors",
        "",
    ]
    if errors:
        for e in errors:
            md_lines.append(f"- [ERROR] {e}")
    else:
        md_lines.append("- None. All structural, frontmatter, SHA-256, citation, image, and internal link checks passed.")

    md_lines.extend(["", "## Warnings", ""])
    if warnings:
        for w in warnings:
            md_lines.append(f"- [WARN] {w}")
    else:
        md_lines.append("- None.")

    md_lines.extend(["", "## High-Risk Pages Flagged for Human Clinical Review", ""])
    for item in stats["pending_review_pages"]:
        md_lines.append(f"- `{item['page']}` — {item['title']} (`{item['status']}`)")

    (LOGS_DIR / "lint_report.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")

    print(f"Lint Status: {'PASS' if not errors else 'FAIL'}")
    print(
        f"Sources: {stats['raw_sources_ingested']}/{stats['raw_sources_total']} ingested "
        f"(SHA-256 verified: {stats['raw_sources_sha256_verified']})"
    )
    print(
        f"Pages: {stats['wiki_pages_total']} | Links: {stats['internal_links_checked']} | "
        f"Images: {stats['image_links_checked']} | Citations: {stats['citations_checked']}"
    )
    print(f"Errors: {len(errors)} | Warnings: {len(warnings)}")
    if errors:
        for e in errors:
            print("  ERROR:", e)
    if warnings:
        for w in warnings:
            print("  WARN:", w)
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
