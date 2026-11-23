#!/usr/bin/env python3
"""
Ingest raw literature sources (SRC-001 to SRC-008) for the Reproductive Genetics & Laboratory Wiki.
- Preserves already-ingested immutable raw files (unless --force is passed).
- Fetches official URLs cleanly and uses official NCBI E-utilities APIs (PubMed / PMC JATS XML)
  for verified bibliographic metadata and Open Access full text.
- Computes SHA-256 digests and records honest statuses (ingested / partially_retrieved / failed).
"""

from __future__ import annotations

import hashlib
import html
import json
import re
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "raw"
SOURCES_DIR = RAW_DIR / "sources"
META_DIR = RAW_DIR / "metadata"
LOGS_DIR = ROOT / "logs"

SOURCES = [
    {
        "source_id": "SRC-001",
        "expected_title": "The use of preimplantation genetic testing for aneuploidy: a committee opinion",
        "organization": "ASRM",
        "year": 2024,
        "url": "https://www.asrm.org/practice-guidance/practice-committee-documents/the-use-of-preimplantation-genetic-testing-for-aneuploidy-a-committee-opinion-2024/",
        "pmid": "38762806",
        "pmcid": "",
        "topics": ["PGT-A", "Aneuploidy", "Clinical Evidence", "Limitations"],
    },
    {
        "source_id": "SRC-002",
        "expected_title": "Clinical management of mosaic results from preimplantation genetic testing for aneuploidy of blastocysts: a committee opinion",
        "organization": "ASRM",
        "year": 2023,
        "url": "https://www.asrm.org/practice-guidance/practice-committee-documents/clinical-management-of-mosaic-results-from-preimplantation-genetic-testing-for-aneuploidy-pgt-a-of-blastocysts-a-committee-opinion/",
        "pmid": "37678731",
        "pmcid": "",
        "topics": ["Mosaicism", "PGT-A", "Genetic Counseling", "Clinical Management"],
    },
    {
        "source_id": "SRC-003",
        "expected_title": "Screening for autosomal recessive and X-linked conditions during pregnancy and preconception: a practice resource of the American College of Medical Genetics and Genomics",
        "organization": "ACMG",
        "year": 2021,
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8488021/",
        "pmid": "34285390",
        "pmcid": "PMC8488021",
        "topics": ["ECS", "Autosomal Recessive", "X-linked Inheritance", "Residual Risk", "Genetic Counseling"],
    },
    {
        "source_id": "SRC-004",
        "expected_title": "ESHRE PGT Consortium good practice recommendations for the detection of structural and numerical chromosomal aberrations",
        "organization": "ESHRE",
        "year": 2020,
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7257111/",
        "pmid": "32500102",
        "pmcid": "PMC7257111",
        "topics": ["PGT-A", "PGT-SR", "Copy Number Variation", "NGS", "Quality Control"],
    },
    {
        "source_id": "SRC-005",
        "expected_title": "ESHRE PGT Consortium good practice recommendations for the detection of monogenic disorders",
        "organization": "ESHRE",
        "year": 2020,
        "url": "https://academic.oup.com/hropen/article/2020/3/hoaa018/5848301",
        "pmid": "32500103",
        "pmcid": "PMC7257022",
        "topics": ["PGT-M", "Monogenic Disease", "Haplotyping", "Allele Dropout", "Technical Validation"],
    },
    {
        "source_id": "SRC-006",
        "expected_title": "Indications and management of preimplantation genetic testing for monogenic conditions: a committee opinion",
        "organization": "ASRM",
        "year": 2023,
        "url": "https://www.asrm.org/practice-guidance/practice-committee-documents/indications-and-management-of-preimplantation-genetic-testing-for-monogenic-conditions-a-committee-opinion-2023/",
        "pmid": "37162432",
        "pmcid": "",
        "topics": ["PGT-M", "Indications", "Genetic Counseling", "Clinical Decision Making"],
    },
    {
        "source_id": "SRC-007",
        "expected_title": "ESHRE PGT Consortium good practice recommendations for the organisation of PGT",
        "organization": "ESHRE",
        "year": 2020,
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7257038/",
        "pmid": "32524036",
        "pmcid": "PMC7257038",
        "topics": ["Laboratory Overview", "Quality Management", "Sample Traceability", "PGT Workflow"],
    },
    {
        "source_id": "SRC-008",
        "expected_title": "ESHRE PGT Consortium and SIG Embryology good practice recommendations for polar body and embryo biopsy for PGT",
        "organization": "ESHRE",
        "year": 2020,
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7257009/",
        "pmid": "32500104",
        "pmcid": "PMC7257009",
        "topics": ["Embryo Biopsy", "Trophectoderm Biopsy", "Sample Handling", "Limitations"],
    },
]


class ArticleHTMLParser(HTMLParser):
    SKIP_TAGS = {"script", "style", "noscript", "svg", "nav", "footer", "aside", "iframe", "form", "button", "header"}
    BLOCK_TAGS = {"p", "h1", "h2", "h3", "h4", "h5", "h6", "li", "tr", "div", "section", "article", "blockquote", "dd", "dt"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.meta: dict[str, list[str]] = {}
        self.title_chunks: list[str] = []
        self.in_title = False
        self.skip_depth = 0
        self.article_depth = 0
        self.main_depth = 0
        self.all_blocks: list[str] = []
        self.article_blocks: list[str] = []
        self.current_buf: list[str] = []
        self.current_heading: str | None = None

    def _flush(self) -> None:
        text = re.sub(r"\s+", " ", "".join(self.current_buf)).strip()
        self.current_buf = []
        if not text:
            return
        if self.current_heading:
            level = int(self.current_heading[1])
            prefix = "#" * min(max(level, 1), 4) + " "
            text = prefix + text
            self.current_heading = None
        self.all_blocks.append(text)
        if self.article_depth > 0 or self.main_depth > 0:
            self.article_blocks.append(text)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        attr_map = {k.lower(): (v or "") for k, v in attrs}
        if tag == "meta":
            name = (attr_map.get("name") or attr_map.get("property") or "").lower().strip()
            content = attr_map.get("content", "").strip()
            if name and content:
                self.meta.setdefault(name, []).append(content)
            return
        if tag == "title":
            self.in_title = True
            return
        if tag in self.SKIP_TAGS:
            self.skip_depth += 1
            return
        if self.skip_depth > 0:
            return
        if tag == "article":
            self.article_depth += 1
        elif tag == "main":
            self.main_depth += 1
        if tag in {"h1", "h2", "h3", "h4"}:
            self._flush()
            self.current_heading = tag
        elif tag in self.BLOCK_TAGS:
            self._flush()

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "title":
            self.in_title = False
            return
        if tag in self.SKIP_TAGS:
            if self.skip_depth > 0:
                self.skip_depth -= 1
            return
        if self.skip_depth > 0:
            return
        if tag in self.BLOCK_TAGS:
            self._flush()
        if tag == "article" and self.article_depth > 0:
            self.article_depth -= 1
        elif tag == "main" and self.main_depth > 0:
            self.main_depth -= 1

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_chunks.append(data)
            return
        if self.skip_depth > 0:
            return
        self.current_buf.append(data)


def curl_get(url: str, timeout: int = 30) -> tuple[int | None, str, str, str | None]:
    cmd = [
        "/usr/bin/curl",
        "-sS",
        "-L",
        "--max-time",
        str(timeout),
        "-w",
        "\n__CURL_STATUS__:%{http_code}\n__CURL_FINAL_URL__:%{url_effective}",
        url,
    ]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 5)
    except Exception as e:
        return None, url, "", f"{type(e).__name__}: {e}"

    stdout = proc.stdout or ""
    status_match = re.search(r"\n__CURL_STATUS__:(\d+)\n__CURL_FINAL_URL__:(.*)$", stdout, re.S)
    if not status_match:
        err_msg = (proc.stderr or "").strip() or f"curl exited with code {proc.returncode}"
        return None, url, "", err_msg

    status = int(status_match.group(1))
    final_url = status_match.group(2).strip() or url
    body = stdout[: status_match.start()]
    if proc.returncode != 0 and status == 0:
        err_msg = (proc.stderr or "").strip() or f"curl exited with code {proc.returncode}"
        return None, final_url, body, err_msg
    if status != 200:
        return status, final_url, body[:500], f"HTTP {status}"
    return status, final_url, body, None


def extract_clean_html(html_text: str) -> tuple[str, dict[str, list[str]], str]:
    parser = ArticleHTMLParser()
    parser.feed(html_text)
    parser._flush()
    title = re.sub(r"\s+", " ", "".join(parser.title_chunks)).strip()
    blocks = parser.article_blocks if len(parser.article_blocks) >= 8 else parser.all_blocks
    cleaned: list[str] = []
    for b in blocks:
        b = html.unescape(b).strip()
        if len(b) < 4:
            continue
        if cleaned and cleaned[-1] == b:
            continue
        cleaned.append(b)
    return title, parser.meta, "\n\n".join(cleaned)


def looks_like_bot_block(text: str, page_title: str) -> bool:
    combined = (page_title + " " + text[:1500]).lower()
    markers = [
        "just a moment",
        "verify you are human",
        "attention required",
        "access denied",
        "enable javascript and cookies",
        "bot protection",
    ]
    return any(m in combined for m in markers) and len(text) < 3500


def elem_text(elem: ET.Element | None) -> str:
    if elem is None:
        return ""
    return re.sub(r"\s+", " ", "".join(elem.itertext())).strip()


def fetch_pmc_jats(pmcid: str) -> tuple[dict, str, str | None]:
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id={pmcid}&retmode=xml"
    status, final_url, xml_text, err = curl_get(url, timeout=40)
    if err or status != 200 or not xml_text.strip().startswith("<"):
        return {}, "", err or f"Invalid PMC XML response (status={status})"
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as e:
        return {}, "", f"XML parse error: {e}"

    article = root.find(".//article")
    if article is None:
        return {}, "", "No <article> element in PMC XML"

    title = elem_text(article.find(".//title-group/article-title"))
    journal = elem_text(article.find(".//journal-meta//journal-title"))
    doi = ""
    for aid in article.findall(".//article-meta/article-id"):
        if aid.attrib.get("pub-id-type") == "doi":
            doi = elem_text(aid)
            break

    authors: list[str] = []
    for contrib in article.findall(".//contrib[@contrib-type='author']"):
        surname = elem_text(contrib.find(".//surname"))
        given = elem_text(contrib.find(".//given-names"))
        collab = elem_text(contrib.find(".//collab"))
        if surname:
            authors.append(f"{given} {surname}".strip())
        elif collab:
            authors.append(collab)

    sections: list[str] = []
    abstract = article.find(".//article-meta/abstract")
    if abstract is not None:
        sections.append("## Abstract")
        for p in abstract.findall(".//p"):
            txt = elem_text(p)
            if txt:
                sections.append(txt)

    body = article.find(".//body")
    if body is not None:
        def walk_sec(sec: ET.Element, level: int = 2) -> None:
            t = elem_text(sec.find("title"))
            if t:
                sections.append(f"{'#' * min(level, 4)} {t}")
            for child in sec:
                tag = child.tag.split("}")[-1]
                if tag == "p":
                    txt = elem_text(child)
                    if txt:
                        sections.append(txt)
                elif tag == "list":
                    for item in child.findall(".//list-item"):
                        txt = elem_text(item)
                        if txt:
                            sections.append(f"- {txt}")
                elif tag == "sec":
                    walk_sec(child, level + 1)
                elif tag == "table-wrap":
                    cap = elem_text(child.find("caption"))
                    if cap:
                        sections.append(f"> [Table] {cap}")

        for child in body:
            tag = child.tag.split("}")[-1]
            if tag == "sec":
                walk_sec(child, 2)
            elif tag == "p":
                txt = elem_text(child)
                if txt:
                    sections.append(txt)

    full_text = "\n\n".join(sections).strip()
    meta = {
        "title": title,
        "journal": journal,
        "doi": doi,
        "authors": authors[:30],
        "api_url": final_url,
    }
    return meta, full_text, None


def fetch_pubmed_meta(pmid: str) -> tuple[dict, str, str | None]:
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&retmode=xml"
    status, final_url, xml_text, err = curl_get(url, timeout=30)
    if err or status != 200 or not xml_text.strip().startswith("<"):
        return {}, "", err or f"Invalid PubMed XML response (status={status})"
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as e:
        return {}, "", f"PubMed XML parse error: {e}"

    art = root.find(".//PubmedArticle")
    if art is None:
        return {}, "", "No <PubmedArticle> found"

    title = elem_text(art.find(".//ArticleTitle"))
    journal = elem_text(art.find(".//Journal/Title"))
    vol = elem_text(art.find(".//JournalIssue/Volume"))
    issue = elem_text(art.find(".//JournalIssue/Issue"))
    pages = elem_text(art.find(".//Pagination/MedlinePgn"))
    pub_year = elem_text(art.find(".//JournalIssue/PubDate/Year"))

    doi = ""
    for aid in art.findall(".//ArticleIdList/ArticleId"):
        if aid.attrib.get("IdType") == "doi":
            doi = elem_text(aid)
            break

    authors: list[str] = []
    for au in art.findall(".//AuthorList/Author"):
        collab = elem_text(au.find("CollectiveName"))
        last = elem_text(au.find("LastName"))
        fore = elem_text(au.find("ForeName"))
        if collab:
            authors.append(collab)
        elif last:
            authors.append(f"{fore} {last}".strip())

    abs_parts: list[str] = []
    for ab in art.findall(".//Abstract/AbstractText"):
        label = ab.attrib.get("Label", "").strip()
        txt = elem_text(ab)
        if txt:
            abs_parts.append(f"**{label}**: {txt}" if label else txt)

    citation = f"{journal} ({pub_year}); {vol}({issue}):{pages}".strip()
    meta = {
        "title": title,
        "journal": journal,
        "citation": citation,
        "doi": doi,
        "authors": authors[:30],
        "api_url": final_url,
    }
    return meta, "\n\n".join(abs_parts), None


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    force = "--force" in sys.argv
    SOURCES_DIR.mkdir(parents=True, exist_ok=True)
    META_DIR.mkdir(parents=True, exist_ok=True)
    LOGS_DIR.mkdir(parents=True, exist_ok=True)

    retrieved_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    retrieved_date = datetime.now().strftime("%Y-%m-%d")

    registry_entries = []
    report = {
        "run_at": retrieved_at,
        "total": len(SOURCES),
        "ingested": 0,
        "partially_retrieved": 0,
        "failed": 0,
        "results": [],
    }

    for src in SOURCES:
        sid = src["source_id"]
        meta_path = META_DIR / f"{sid}.json"
        raw_path = SOURCES_DIR / f"{sid}.md"

        # Preserve immutable already-ingested raw sources unless --force
        if not force and meta_path.exists() and raw_path.exists():
            existing = json.loads(meta_path.read_text(encoding="utf-8"))
            if existing.get("status") == "ingested" and existing.get("sha256") == sha256_file(raw_path):
                print(f"[{sid}] Preserving immutable ingested file ({existing.get('char_count')} chars, sha256={existing['sha256'][:12]}...)", flush=True)
                report["ingested"] += 1
                registry_entries.append(existing)
                report["results"].append(
                    {
                        "source_id": sid,
                        "status": existing["status"],
                        "http_status": existing.get("http_status"),
                        "char_count": existing.get("char_count", 0),
                        "doi": existing.get("doi", ""),
                        "sha256": existing.get("sha256", ""),
                        "reason": existing.get("reason", ""),
                    }
                )
                continue

        url = src["url"]
        print(f"[{sid}] Fetching primary URL: {url} ...", flush=True)
        status_code, final_url, body, err = curl_get(url)
        time.sleep(0.4)

        record = {
            "source_id": sid,
            "expected_title": src["expected_title"],
            "retrieved_title": "",
            "organization": src["organization"],
            "year": src["year"],
            "authors": [],
            "journal": "",
            "doi": "",
            "pmid": src.get("pmid", ""),
            "pmcid": src.get("pmcid", ""),
            "url": url,
            "final_url": final_url,
            "retrieval_method": "primary_url",
            "http_status": status_code,
            "retrieved_at": retrieved_at,
            "retrieved_date": retrieved_date,
            "topics": src["topics"],
            "status": "failed",
            "reason": "",
            "raw_file": "",
            "sha256": "",
            "char_count": 0,
        }

        primary_text = ""
        primary_title = ""
        primary_note = ""
        if not err and status_code == 200 and body:
            page_title, html_meta, clean_text = extract_clean_html(body)
            if not looks_like_bot_block(clean_text, page_title):
                primary_title = (
                    html_meta.get("citation_title")
                    or html_meta.get("dc.title")
                    or html_meta.get("og:title")
                    or [page_title]
                )[0].strip()
                primary_text = clean_text
            else:
                primary_note = f"Primary URL served anti-bot page (title='{page_title}')."
        else:
            primary_note = f"Primary URL returned {err or status_code}."

        # Strategy 1: If primary URL already yielded substantial full text (>= 3000 chars)
        content_sections: list[str] = []
        if len(primary_text) >= 3000:
            record["retrieved_title"] = primary_title or src["expected_title"]
            content_sections.append(primary_text)
            record["status"] = "ingested"
            record["reason"] = "Full or substantial article text retrieved directly from primary URL."
            record["retrieval_method"] = "primary_url"

        # Strategy 2: Official NCBI PMC E-utilities JATS XML for Open Access PMC articles
        if record["status"] != "ingested" and src.get("pmcid"):
            pmcid = src["pmcid"]
            print(f"  -> Querying official NCBI PMC E-utilities for {pmcid} ...", flush=True)
            pmc_meta, pmc_text, pmc_err = fetch_pmc_jats(pmcid)
            time.sleep(0.5)
            if not pmc_err and len(pmc_text) >= 2500:
                record["retrieved_title"] = pmc_meta.get("title") or src["expected_title"]
                record["authors"] = pmc_meta.get("authors") or []
                record["journal"] = pmc_meta.get("journal") or ""
                record["doi"] = pmc_meta.get("doi") or ""
                record["final_url"] = pmc_meta.get("api_url") or final_url
                record["retrieval_method"] = "ncbi_pmc_eutilities_jats_xml"
                content_sections = [pmc_text]
                record["status"] = "ingested"
                record["reason"] = (
                    f"{primary_note} Full Open Access JATS XML retrieved via official NCBI PMC E-utilities ({pmcid})."
                ).strip()
            else:
                primary_note = f"{primary_note} PMC E-utilities error: {pmc_err}".strip()

        # Always enrich bibliographic metadata (DOI, journal, authors, abstract) from official PubMed E-utilities if PMID known
        pubmed_abstract = ""
        if src.get("pmid"):
            print(f"  -> Verifying metadata via official NCBI PubMed E-utilities (PMID {src['pmid']}) ...", flush=True)
            pm_meta, pm_abs, pm_err = fetch_pubmed_meta(src["pmid"])
            time.sleep(0.4)
            if not pm_err:
                if not record["retrieved_title"]:
                    record["retrieved_title"] = pm_meta.get("title") or src["expected_title"]
                if not record["authors"]:
                    record["authors"] = pm_meta.get("authors") or []
                if not record["journal"]:
                    record["journal"] = pm_meta.get("citation") or pm_meta.get("journal") or ""
                if not record["doi"]:
                    record["doi"] = pm_meta.get("doi") or ""
                pubmed_abstract = pm_abs

        # Fallback for non-OA articles (e.g., ASRM primary URL + PubMed abstract)
        if record["status"] != "ingested":
            combined_parts: list[str] = []
            if pubmed_abstract:
                combined_parts.append("## Official PubMed Abstract\n\n" + pubmed_abstract)
            if len(primary_text) >= 300:
                combined_parts.append("## Official Publisher Page Excerpt\n\n" + primary_text)
            if combined_parts:
                content_sections = combined_parts
                total_len = sum(len(x) for x in content_sections)
                if len(primary_text) >= 3000:
                    record["status"] = "ingested"
                else:
                    record["status"] = "partially_retrieved"
                    record["retrieval_method"] = "pubmed_eutilities_and_primary_excerpt"
                    record["reason"] = (
                        f"{primary_note} Official PubMed bibliographic metadata and abstract verified (PMID {src['pmid']}); full text not completely available from public HTML."
                    ).strip()
            else:
                record["status"] = "failed"
                record["reason"] = primary_note or "No retrievable content."

        final_content = "\n\n".join(content_sections).strip()
        record["char_count"] = len(final_content)

        if record["status"] in ("ingested", "partially_retrieved"):
            header = [
                f"# {sid}: {record['retrieved_title'] or src['expected_title']}",
                "",
                f"- **Source ID**: `{sid}`",
                f"- **Organization**: {src['organization']}",
                f"- **Year**: {src['year']}",
                f"- **Authors**: {', '.join(record['authors'][:15]) if record['authors'] else 'Not listed'}",
                f"- **Journal / Citation**: {record['journal'] or 'Not listed'}",
                f"- **DOI**: {record['doi'] or 'Not listed'}",
                f"- **PMID**: {record['pmid'] or 'N/A'}",
                f"- **PMCID**: {record['pmcid'] or 'N/A'}",
                f"- **Original URL**: {url}",
                f"- **Final / API URL**: {record['final_url']}",
                f"- **Retrieval Method**: `{record['retrieval_method']}`",
                f"- **Retrieved At (UTC)**: {retrieved_at}",
                f"- **Retrieval Status**: `{record['status']}`",
                f"- **Character Count**: {len(final_content)}",
                f"- **Notes**: {record['reason']}",
                "",
                "---",
                "",
                "## Retrieved Content (Immutable Raw Extract)",
                "",
                final_content,
                "",
            ]
            raw_path.write_text("\n".join(header), encoding="utf-8")
            record["raw_file"] = f"raw/sources/{sid}.md"
            record["sha256"] = sha256_file(raw_path)

        if record["status"] == "ingested":
            report["ingested"] += 1
        elif record["status"] == "partially_retrieved":
            report["partially_retrieved"] += 1
        else:
            report["failed"] += 1

        print(
            f"  -> {record['status'].upper()} ({record['char_count']} chars, DOI={record['doi'] or 'n/a'}, sha256={record['sha256'][:12] if record['sha256'] else 'n/a'})",
            flush=True,
        )

        meta_path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        registry_entries.append(record)
        report["results"].append(
            {
                "source_id": sid,
                "status": record["status"],
                "http_status": record["http_status"],
                "char_count": record["char_count"],
                "doi": record["doi"],
                "sha256": record["sha256"],
                "reason": record["reason"],
            }
        )

    registry_path = RAW_DIR / "registry.json"
    registry_path.write_text(
        json.dumps({"updated_at": retrieved_at, "sources": registry_entries}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    report_path = LOGS_DIR / "ingest_report.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(
        f"\nSummary: ingested={report['ingested']}, partially_retrieved={report['partially_retrieved']}, failed={report['failed']}",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
