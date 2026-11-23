#!/usr/bin/env python3
"""
Compile raw/structured/igene_disease_list.json into presentations/ecs-teaching-slides/igene_data.js
so Slide 7's interactive ECS Gene Search uses 100% authentic, verified SRC-009 data with zero manual duplication.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC_JSON = ROOT / "raw" / "structured" / "igene_disease_list.json"
OUT_DIR = ROOT / "presentations" / "ecs-teaching-slides"
OUT_JS = OUT_DIR / "igene_data.js"


def main() -> int:
    if not SRC_JSON.exists():
        print(f"ERROR: Missing {SRC_JSON}", file=sys.stderr)
        return 1

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    data = json.loads(SRC_JSON.read_text(encoding="utf-8"))

    compact_items = [
        {
            "id": it["row_id"],
            "cat": it["primary_category"],
            "catFull": it["disease_category"],
            "zh": it["disease_name_zh"],
            "en": it["disease_name_en"],
            "gene": it["gene_symbol"],
            "inh": it["inheritance_pattern"],
            "pop": it["population"],
            "freq": it["carrier_frequency"],
            "det": it["detection_rate"],
        }
        for it in data.get("items", [])
    ]

    payload = {
        "source_id": data.get("source_id", "SRC-009"),
        "product_name": data.get("product_name", "iGene 遺傳疾病帶因篩檢"),
        "source_url": data.get("source_url", ""),
        "product_intro_url": data.get("product_intro_url", ""),
        "retrieved_date": data.get("retrieved_date", ""),
        "summary_stats": {
            "official_claimed_diseases": data["summary_stats"]["official_claimed_diseases"],
            "extracted_disease_rows": data["summary_stats"]["extracted_disease_rows"],
            "unique_individual_gene_symbols": data["summary_stats"]["unique_individual_gene_symbols"],
            "extracted_primary_categories": data["summary_stats"]["extracted_primary_categories"],
            "x_linked_unique_genes_count": data["summary_stats"]["x_linked_unique_genes_count"],
            "inheritance_pattern_counts": data["summary_stats"]["inheritance_pattern_counts"],
            "primary_category_counts": data["summary_stats"]["primary_category_counts"],
        },
        "items": compact_items,
    }

    OUT_JS.write_text(
        "// Auto-generated from raw/structured/igene_disease_list.json by workflows/build_ecs_slides_data.py\n"
        "window.IGENE_SLIDE_DATA = "
        + json.dumps(payload, ensure_ascii=False)
        + ";\n",
        encoding="utf-8",
    )
    print(f"Built {OUT_JS.relative_to(ROOT)} ({len(compact_items)} items, retrieved_date={payload['retrieved_date']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
