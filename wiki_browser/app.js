(function () {
  const DATA = window.WIKI_DATA;
  if (!DATA) {
    document.getElementById("main-content").innerHTML =
      "<div class='article-shell'><h1>找不到 Wiki 資料</h1><p>請先執行 <code>python3 workflows/build_browser_data.py</code> 產生 <code>wiki_data.js</code>。</p></div>";
    return;
  }

  const pageMap = new Map(DATA.pages.map((p) => [p.id, p]));
  const sourceMap = new Map(DATA.sources.map((s) => [s.source_id, s]));
  const catMap = new Map(DATA.categories.map((c) => [c.id, c]));

  const sidebarEl = document.getElementById("sidebar");
  const backdropEl = document.getElementById("sidebar-backdrop");
  const menuToggleBtn = document.getElementById("menu-toggle");
  const mainEl = document.getElementById("main-content");
  const searchInput = document.getElementById("search-input");
  const searchDropdown = document.getElementById("search-results");

  function escHtml(str) {
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function resolveRelativePageId(currentPageId, relTarget) {
    const clean = relTarget.split("#")[0].trim();
    if (!clean.endsWith(".md")) return null;
    if (clean === "log.md" || clean === "../log.md") return "__log__";
    if (clean === "index.md" || clean === "../index.md") return "__home__";
    const baseParts = currentPageId ? currentPageId.split("/").slice(0, -1) : [];
    const parts = baseParts.concat(clean.split("/"));
    const stack = [];
    for (const part of parts) {
      if (!part || part === ".") continue;
      if (part === "..") stack.pop();
      else stack.push(part);
    }
    const candidate = stack.join("/");
    return pageMap.has(candidate) ? candidate : null;
  }

  function resolveImagePath(src) {
    // From wiki/<cat>/*.md images look like ../../assets/biolove-6.png; from wiki_browser/index.html they are ../assets/...
    const idx = src.indexOf("assets/");
    if (idx !== -1) {
      return "../" + src.slice(idx);
    }
    return src;
  }

  function formatInline(text, currentPageId) {
    let out = escHtml(text);

    // Inline math $...$
    out = out.replace(/\$([^$\n]+)\$/g, (_, expr) => {
      const clean = expr
        .replace(/\\ge/g, "≥")
        .replace(/\\le/g, "≤")
        .replace(/\\times/g, "×")
        .replace(/\\text\{([^}]+)\}/g, "$1")
        .replace(/\{,\}/g, ",")
        .replace(/\\log_2/g, "log₂");
      return `<em>${clean}</em>`;
    });

    // Inline code
    out = out.replace(/`([^`]+)`/g, "<code>$1</code>");

    // Markdown links [label](href)
    out = out.replace(/\[([^\]]+)\]\(([^)]+)\)/g, (_, label, href) => {
      if (/^https?:\/\//i.test(href)) {
        return `<a href="${href}" target="_blank" rel="noopener noreferrer">${label}</a>`;
      }
      const targetId = resolveRelativePageId(currentPageId, href);
      if (targetId === "__home__") return `<a href="#home">${label}</a>`;
      if (targetId === "__log__") return `<a href="#log">${label}</a>`;
      if (targetId) return `<a href="#page/${targetId}">${label}</a>`;
      return `<a href="${href}">${label}</a>`;
    });

    // Bold & italic
    out = out.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
    out = out.replace(/\*([^*]+)\*/g, "<em>$1</em>");

    // Source citation badges [SRC-XXX]
    out = out.replace(/\[(SRC-\d{3})\]/g, (_, sid) => {
      const s = sourceMap.get(sid);
      const tip = s ? escHtml(`${s.organization} (${s.year}): ${s.retrieved_title || s.expected_title}`) : sid;
      return `<a href="#sources/${sid}" class="cite-tag" title="${tip}">[${sid}]</a>`;
    });

    return out;
  }

  function renderMarkdown(md, currentPageId) {
    const lines = md.replace(/\r\n/g, "\n").split("\n");
    const html = [];
    let i = 0;

    while (i < lines.length) {
      const line = lines[i];

      if (!line.trim()) {
        i++;
        continue;
      }

      // Horizontal rule
      if (/^---+$/.test(line.trim())) {
        html.push("<hr />");
        i++;
        continue;
      }

      // Display math block $$...$$
      if (line.trim().startsWith("$$")) {
        let mathContent = line.trim().slice(2);
        if (mathContent.endsWith("$$")) {
          mathContent = mathContent.slice(0, -2);
        } else {
          i++;
          while (i < lines.length && !lines[i].trim().endsWith("$$")) {
            mathContent += " " + lines[i].trim();
            i++;
          }
          if (i < lines.length) mathContent += " " + lines[i].trim().slice(0, -2);
        }
        const pretty = escHtml(mathContent)
          .replace(/\\text\{([^}]+)\}/g, "$1")
          .replace(/\\times/g, "×")
          .replace(/\\ge/g, "≥");
        html.push(`<div class="math-block">${pretty}</div>`);
        i++;
        continue;
      }

      // Standalone image line ![alt](src) optionally followed by *caption*
      const imgMatch = line.trim().match(/^!\[([^\]]*)\]\(([^)]+)\)$/);
      if (imgMatch) {
        const alt = escHtml(imgMatch[1]);
        const src = resolveImagePath(imgMatch[2]);
        let caption = alt;
        if (i + 1 < lines.length && /^\*[^*].*\*$/.test(lines[i + 1].trim())) {
          caption = formatInline(lines[i + 1].trim().slice(1, -1), currentPageId);
          i++;
        }
        html.push(
          `<figure class="wiki-figure"><img src="${src}" alt="${alt}" loading="lazy" /><figcaption>${caption}</figcaption></figure>`
        );
        i++;
        continue;
      }

      // Headings
      const hMatch = line.match(/^(#{1,4})\s+(.*)$/);
      if (hMatch) {
        const level = hMatch[1].length;
        html.push(`<h${level}>${formatInline(hMatch[2], currentPageId)}</h${level}>`);
        i++;
        continue;
      }

      // Blockquote
      if (line.trim().startsWith(">")) {
        const qLines = [];
        while (i < lines.length && lines[i].trim().startsWith(">")) {
          qLines.push(lines[i].trim().replace(/^>\s?/, ""));
          i++;
        }
        html.push(`<blockquote><p>${formatInline(qLines.join(" "), currentPageId)}</p></blockquote>`);
        continue;
      }

      // Markdown Table
      if (line.includes("|") && i + 1 < lines.length && /^\s*\|?[\s:-]+\|/.test(lines[i + 1])) {
        const headerCells = line
          .trim()
          .replace(/^\||\|$/g, "")
          .split("|")
          .map((c) => c.trim());
        i += 2; // skip separator
        const rows = [];
        while (i < lines.length && lines[i].includes("|") && lines[i].trim() !== "") {
          const cells = lines[i]
            .trim()
            .replace(/^\||\|$/g, "")
            .split("|")
            .map((c) => c.trim());
          rows.push(cells);
          i++;
        }
        let tbl = "<div class='table-wrap'><table><thead><tr>";
        headerCells.forEach((c) => {
          tbl += `<th>${formatInline(c, currentPageId)}</th>`;
        });
        tbl += "</tr></thead><tbody>";
        rows.forEach((r) => {
          tbl += "<tr>";
          r.forEach((c) => {
            tbl += `<td>${formatInline(c.replace(/<br\s*\/?>/gi, "；"), currentPageId)}</td>`;
          });
          tbl += "</tr>";
        });
        tbl += "</tbody></table></div>";
        html.push(tbl);
        continue;
      }

      // Unordered list
      if (/^\s*[-*]\s+/.test(line)) {
        const items = [];
        while (i < lines.length && /^\s*[-*]\s+/.test(lines[i])) {
          items.push(lines[i].replace(/^\s*[-*]\s+/, ""));
          i++;
        }
        html.push("<ul>" + items.map((it) => `<li>${formatInline(it, currentPageId)}</li>`).join("") + "</ul>");
        continue;
      }

      // Ordered list
      if (/^\s*\d+\.\s+/.test(line)) {
        const items = [];
        while (i < lines.length && /^\s*\d+\.\s+/.test(lines[i])) {
          items.push(lines[i].replace(/^\s*\d+\.\s+/, ""));
          i++;
        }
        html.push("<ol>" + items.map((it) => `<li>${formatInline(it, currentPageId)}</li>`).join("") + "</ol>");
        continue;
      }

      // Paragraph
      const pLines = [];
      while (
        i < lines.length &&
        lines[i].trim() !== "" &&
        !/^(#{1,4}\s|>\s?|[-*]\s|\d+\.\s|---+$|\$\$|!\[)/.test(lines[i].trim())
      ) {
        if (lines[i].includes("|") && i + 1 < lines.length && /^\s*\|?[\s:-]+\|/.test(lines[i + 1])) break;
        pLines.push(lines[i].trim());
        i++;
      }
      if (pLines.length) {
        html.push(`<p>${formatInline(pLines.join(" "), currentPageId)}</p>`);
      } else {
        i++;
      }
    }

    return html.join("\n");
  }

  function buildSidebar() {
    const container = document.getElementById("category-nav");
    const fragments = [];
    for (const cat of DATA.categories) {
      const catPages = DATA.pages.filter((p) => p.category === cat.id);
      fragments.push(
        `<div class="cat-heading"><span>${escHtml(cat.label)} · ${escHtml(cat.en)}</span><span class="cat-count">${catPages.length}</span></div>`
      );
      for (const p of catPages) {
        const shortTitle = p.title.replace(/^FAQ：/, "");
        fragments.push(
          `<a href="#page/${p.id}" class="nav-item" data-page-id="${p.id}">${escHtml(shortTitle)}</a>`
        );
      }
    }
    container.innerHTML = fragments.join("\n");
  }

  function setActiveNav(routeKey) {
    document.querySelectorAll(".nav-item").forEach((el) => {
      const match = el.dataset.route === routeKey || el.dataset.pageId === routeKey;
      el.classList.toggle("active", match);
    });
  }

  function closeMobileSidebar() {
    sidebarEl.classList.remove("open");
    backdropEl.classList.add("hidden");
  }

  function renderHome() {
    setActiveNav("home");
    const pendingCount = DATA.pages.filter(
      (p) =>
        p.review_status === "pending_clinical_review" ||
        p.review_status === "pending_technical_verification" ||
        (Array.isArray(p.review_layers) &&
          (p.review_layers.includes("pending_clinical_review") || p.review_layers.includes("pending_technical_verification")))
    ).length;
    const ingestedCount = DATA.sources.filter((s) => s.status === "ingested").length;
    const mainSlugs = new Set(["pgt-a", "ecs", "pgt-sr", "pgt-m"]);
    const products = DATA.pages.filter((p) => p.category === "products" && mainSlugs.has(p.slug));

    const productCards = products
      .map(
        (p) => `
      <a class="product-card" href="#page/${p.id}">
        <span class="product-tag">${escHtml(p.slug.toUpperCase())}</span>
        <h3>${escHtml(p.title.split("（")[0])}</h3>
        <p>${escHtml(p.summary)}</p>
      </a>`
      )
      .join("");

    const catOverview = DATA.categories
      .map((c) => {
        const items = DATA.pages.filter((p) => p.category === c.id);
        const links = items
          .slice(0, 5)
          .map((p) => `<a class="mini-chip" href="#page/${p.id}">${escHtml(p.title.split("（")[0].replace(/^FAQ：/, ""))}</a>`)
          .join("");
        return `
        <div class="category-card">
          <h3>${escHtml(c.label)}（${items.length} 篇）</h3>
          <p>${escHtml(c.desc)}</p>
          <div class="audience-links">${links}</div>
        </div>`;
      })
      .join("");

    mainEl.innerHTML = `
      <section class="hero-card">
        <div>
          <span class="hero-badge">Persistent LLM Wiki · Warm Orange Medical Education</span>
          <h1>Reproductive Genetics &amp; Laboratory Wiki</h1>
          <p>以 Andrej Karpathy 的 Persistent LLM Wiki 架構打造之生殖遺傳檢測與實驗室衛教知識庫，完整整合 ASRM、ESHRE、ACMG 國際指引，維持跨頁交叉連結與可追溯之原始文獻出處。</p>
          <div class="hero-stats">
            <span class="stat-chip">📄 ${DATA.pages.length} 篇整合知識頁</span>
            <span class="stat-chip">📚 ${ingestedCount}/${DATA.sources.length} 篇全文文獻驗證</span>
            <span class="stat-chip">🩺 ${pendingCount} 篇待臨床審核標記</span>
          </div>
        </div>
        <div class="hero-logo-wrap">
          <img src="../assets/biolove-5.png" alt="BiOLOVE 明天的幸福・愛生育" />
        </div>
      </section>

      <h2 class="section-title">四大核心檢測產品入口</h2>
      <section class="card-grid">${productCards}</section>

      <h2 class="section-title">依讀者身分快速導覽</h2>
      <section class="card-grid">
        <div class="audience-card">
          <h3>👤 Patient 一般民眾與患者</h3>
          <p>以白話方式釐清常見迷思、檢測差異與決策注意事項。</p>
          <div class="audience-links">
            <a class="mini-chip" href="#page/faq/faq-pgt-a-vs-pgt-sr-vs-pgt-m.md">PGT 三者差別</a>
            <a class="mini-chip" href="#page/faq/faq-pgt-a-guarantee-pregnancy.md">PGT-A 能保證懷孕嗎</a>
            <a class="mini-chip" href="#page/faq/faq-mosaic-embryo-transfer.md">Mosaic 胚胎可植入嗎</a>
            <a class="mini-chip" href="#page/faq/faq-ecs-negative-risk.md">ECS 陰性殘餘風險</a>
          </div>
        </div>
        <div class="audience-card">
          <h3>🩺 Physician 醫師與遺傳諮詢人員</h3>
          <p>整合多中心 RCT、跨學會指引共識與臨床爭議焦點。</p>
          <div class="audience-links">
            <a class="mini-chip" href="#page/evidence/pgt-a-clinical-evidence.md">PGT-A 臨床實證</a>
            <a class="mini-chip" href="#page/evidence/mosaic-embryo-evidence.md">Mosaic 處置指引</a>
            <a class="mini-chip" href="#page/evidence/ecs-clinical-evidence.md">ECS 四層架構</a>
            <a class="mini-chip" href="#page/evidence/pgt-m-sr-evidence.md">PGT-M/SR 實證整合</a>
          </div>
        </div>
        <div class="audience-card">
          <h3>🔬 Laboratory 實驗室與胚胎師團隊</h3>
          <p>檢視 ESHRE 2020 切片裝管、品質管理、七大見證節點與分子限制。</p>
          <div class="audience-links">
            <a class="mini-chip" href="#page/laboratory/laboratory-overview.md">實驗室概覽</a>
            <a class="mini-chip" href="#page/laboratory/pgt-workflow.md">PGT 作業流程</a>
            <a class="mini-chip" href="#page/laboratory/quality-management.md">品質管理</a>
            <a class="mini-chip" href="#page/laboratory/sample-traceability.md">檢體追溯</a>
          </div>
        </div>
      </section>

      <h2 class="section-title">全站知識分類總覽</h2>
      <section class="card-grid">${catOverview}</section>

      <div class="footer-disclaimer">
        <strong>醫學與合規聲明：</strong>本知識庫內容依據已驗證之國際指引（ASRM / ESHRE / ACMG）整理，標示為「待臨床審核」之頁面尚未經院所醫師或實驗室主管正式簽核，且所有實驗室規格敘述僅屬一般性專業知識，實際檢測規格與醫療決策請以專業醫療人員評估為準。
      </div>
    `;
  }

  function renderReviewBadges(page) {
    const labels = {
      source_verified: ["badge-ok", "✓ 來源已確認"],
      product_spec_verified: ["badge-ok", "✓ 產品規格有據"],
      pending_clinical_review: ["badge-review", "⚠ 待臨床審核"],
      pending_technical_verification: ["badge-tech", "⚙ 技術規格待確認"],
      approved: ["badge-ok", "✓ 已完整核准"],
      auto_compiled: ["badge-ok", "✓ 自動編譯基礎知識"],
      draft: ["badge-review", "✎ 草稿"],
    };
    const layers = Array.isArray(page.review_layers) && page.review_layers.length ? page.review_layers : [page.review_status];
    return layers
      .map((st) => {
        const [cls, txt] = labels[st] || ["badge-review", st];
        return `<span class="badge ${cls}">${escHtml(txt)}</span>`;
      })
      .join("");
  }

  function renderIGeneExplorer(initialQuery) {
    const panel = DATA.igene_panel;
    if (!panel || !Array.isArray(panel.items)) return "";
    const stats = panel.summary_stats || {};
    const catOptions = (stats.primary_category_counts || [])
      .map((c) => `<option value="${escHtml(c.name)}">${escHtml(c.code)}. ${escHtml(c.name)}（${c.disease_count}）</option>`)
      .join("");

    return `
      <section class="igene-explorer" id="igene-explorer-section">
        <div class="igene-explorer-head">
          <div>
            <h3>🧬 iGene 遺傳疾病帶因篩檢 — 完整結構化疾病／基因檢索</h3>
            <p class="igene-explorer-sub">
              官方來源：<a href="${escHtml(panel.source_url)}" target="_blank" rel="noopener noreferrer">iGene 遺傳疾病帶因篩檢列表</a> ·
              <a href="${escHtml(panel.product_intro_url)}" target="_blank" rel="noopener noreferrer">iGene 產品介紹</a>（擷取日期：${escHtml(panel.retrieved_date)}）
            </p>
          </div>
          <span class="badge badge-ok">SRC-009 結構化核對一致</span>
        </div>
        <div class="igene-kpi-row">
          <span class="stat-chip">📋 疾病項目：${stats.extracted_disease_rows || panel.items.length} 筆（官網標示 350 種）</span>
          <span class="stat-chip">🧬 去重獨立基因：${stats.unique_individual_gene_symbols || 351} 個（含 HBA1/HBA2）</span>
          <span class="stat-chip">🗂 疾病大類：${stats.extracted_primary_categories || 15} 大類</span>
          <span class="stat-chip">⚧ X 性聯（XL）：${stats.x_linked_unique_genes_count || 28} 基因</span>
          <span class="stat-chip">AR：${(stats.inheritance_pattern_counts && stats.inheritance_pattern_counts.AR) || 319} · AR/AD：${(stats.inheritance_pattern_counts && stats.inheritance_pattern_counts["AR/AD"]) || 3}</span>
        </div>
        <div class="igene-controls">
          <input type="search" id="igene-q" value="${escHtml(initialQuery || "")}" placeholder="搜尋中文病名、英文病名或基因（如 SMN1、G6PD、HBA1、地中海、CFTR）..." aria-label="搜尋 iGene 疾病或基因" />
          <select id="igene-cat" aria-label="依 15 大疾病分類篩選">
            <option value="">全部疾病分類（15 大類）</option>
            ${catOptions}
          </select>
          <select id="igene-inh" aria-label="依遺傳模式篩選">
            <option value="">全部遺傳模式</option>
            <option value="AR">AR — 體染色體隱性（319）</option>
            <option value="XL">XL — X 染色體性聯（28）</option>
            <option value="AR/AD">AR/AD — 隱性／顯性（3）</option>
          </select>
        </div>
        <div class="igene-status-bar">
          <span id="igene-count-label"></span>
          <span>說明：AR 體染色體隱性 · XL X 染色體性聯 · AR/AD 兼具隱性／顯性模式</span>
        </div>
        <div class="igene-table-scroll">
          <table class="igene-table">
            <thead>
              <tr>
                <th>#</th>
                <th>疾病名稱（中／英）與分類</th>
                <th>基因</th>
                <th>遺傳模式</th>
                <th>適用族群</th>
                <th>帶因率</th>
                <th>檢出率</th>
              </tr>
            </thead>
            <tbody id="igene-tbody"></tbody>
          </table>
        </div>
        <div class="igene-caveat">
          <strong>臨床與資料解讀提醒：</strong>ECS 屬於帶因者篩檢，陰性結果仍存在 <strong>Residual Risk（殘餘風險）</strong>，不可保證生下健康寶寶；表內「檢出率」（76%–99%）不得解讀為所有變異類型之統一分析敏感度。目標區間 NGS 無法偵測大片段缺失／插入／倒轉／重複序列擴增（例如 X 染色體脆折症 <em>FMR1</em> 未列於此清單中），詳細限制請見 <a href="#page/products/ecs.md">ECS 產品主頁</a> 與 <a href="#page/concepts/residual-risk.md">Residual Risk</a>。
        </div>
      </section>
    `;
  }

  function bindIGeneExplorer() {
    const panel = DATA.igene_panel;
    const qInput = document.getElementById("igene-q");
    const catSelect = document.getElementById("igene-cat");
    const inhSelect = document.getElementById("igene-inh");
    const tbody = document.getElementById("igene-tbody");
    const countLabel = document.getElementById("igene-count-label");
    if (!panel || !qInput || !tbody) return;

    function updateTable() {
      const q = qInput.value.trim().toLowerCase();
      const cat = catSelect.value;
      const inh = inhSelect.value;
      const filtered = panel.items.filter((it) => {
        if (cat && it.primary_category !== cat) return false;
        if (inh && it.inheritance_pattern !== inh) return false;
        if (q) {
          const hay = `${it.disease_name_zh} ${it.disease_name_en} ${it.gene_symbol} ${it.disease_category} ${it.inheritance_pattern} ${it.population}`.toLowerCase();
          if (!hay.includes(q)) return false;
        }
        return true;
      });
      countLabel.textContent = `顯示 ${filtered.length} / ${panel.items.length} 筆疾病項目`;
      if (!filtered.length) {
        tbody.innerHTML = `<tr><td colspan="7" style="text-align:center;color:#6D6D70;padding:24px;">查無符合條件之 iGene 疾病或基因項目（例如 FMR1 未收錄於此 350 項 NGS 清單中）</td></tr>`;
        return;
      }
      tbody.innerHTML = filtered
        .map((it) => {
          const inhCls = it.inheritance_pattern === "XL" ? "inh-XL" : it.inheritance_pattern === "AR/AD" ? "inh-ARAD" : "inh-AR";
          return `
          <tr>
            <td>${escHtml(it.row_id)}</td>
            <td>
              <div class="igene-disease-zh">${escHtml(it.disease_name_zh)}</div>
              <div class="igene-disease-en">${escHtml(it.disease_name_en)}</div>
              <div class="igene-cat-small">${escHtml(it.disease_category)}</div>
            </td>
            <td><span class="gene-pill">${escHtml(it.gene_symbol)}</span></td>
            <td><span class="inh-pill ${inhCls}">${escHtml(it.inheritance_pattern)}</span></td>
            <td>${escHtml(it.population)}</td>
            <td>${escHtml(it.carrier_frequency)}</td>
            <td>${escHtml(it.detection_rate)}</td>
          </tr>`;
        })
        .join("");
    }

    qInput.addEventListener("input", updateTable);
    catSelect.addEventListener("change", updateTable);
    inhSelect.addEventListener("change", updateTable);
    updateTable();
  }

  function renderPage(pageId, queryParam) {
    const page = pageMap.get(pageId);
    if (!page) {
      renderHome();
      return;
    }
    setActiveNav(pageId);
    const cat = catMap.get(page.category);
    const reviewBadgesHtml = renderReviewBadges(page);

    const relatedHtml = (page.related_pages || [])
      .map((rid) => {
        const target = pageMap.get(rid);
        if (!target) return "";
        return `<a class="related-chip" href="#page/${rid}">${escHtml(target.title)}</a>`;
      })
      .filter(Boolean)
      .join("");

    const sourcesHtml = (page.source_ids || [])
      .map((sid) => {
        const s = sourceMap.get(sid);
        if (!s) return "";
        return `
        <div class="source-card">
          <div class="source-card-head">
            <span class="source-id-pill">${escHtml(s.source_id)}</span>
            <span class="source-org-pill">${escHtml(s.organization)} · ${escHtml(s.year)}</span>
          </div>
          <div class="source-title">${escHtml(s.retrieved_title || s.expected_title)}</div>
          <div class="source-meta">
            ${s.doi ? `DOI: <code>${escHtml(s.doi)}</code> · ` : ""}狀態: <code>${escHtml(s.status)}</code> · SHA-256: <code>${escHtml((s.sha256 || "").slice(0, 14))}…</code><br />
            <a href="${escHtml(s.url)}" target="_blank" rel="noopener noreferrer">${escHtml(s.url)}</a>
          </div>
        </div>`;
      })
      .join("");

    const showIGeneExplorer = pageId === "products/ecs.md" || pageId === "products/ecs-disease-gene-index.md";
    const explorerHtml = showIGeneExplorer ? renderIGeneExplorer(queryParam) : "";

    mainEl.innerHTML = `
      <article class="article-shell">
        <div class="article-meta-bar">
          <span class="badge badge-cat">${escHtml(cat ? `${cat.label} · ${cat.en}` : page.category)}</span>
          ${reviewBadgesHtml}
          <span class="meta-date">最後更新：${escHtml(page.updated_at)}</span>
        </div>
        <div class="markdown-body">
          ${renderMarkdown(page.markdown, page.id)}
        </div>
        ${explorerHtml}
        ${
          relatedHtml
            ? `<section class="panel-box"><h3>🔗 相關交叉連結頁面</h3><div class="related-chips">${relatedHtml}</div></section>`
            : ""
        }
        ${
          sourcesHtml
            ? `<section class="panel-box"><h3>📚 可追溯原始文獻出處（Raw Sources）</h3><div class="source-list">${sourcesHtml}</div></section>`
            : ""
        }
      </article>
    `;
    if (showIGeneExplorer) {
      bindIGeneExplorer();
      if (queryParam) {
        const sec = document.getElementById("igene-explorer-section");
        if (sec) sec.scrollIntoView({ behavior: "smooth", block: "start" });
        return;
      }
    }
    window.scrollTo({ top: 0, behavior: "instant" });
  }

  function renderSources(highlightSid) {
    setActiveNav("sources");
    const cards = DATA.sources
      .map((s) => {
        const usedBy = DATA.pages
          .filter((p) => (p.source_ids || []).includes(s.source_id))
          .map((p) => `<a class="mini-chip" href="#page/${p.id}">${escHtml(p.title.split("（")[0])}</a>`)
          .join("");
        const hl = highlightSid === s.source_id ? " style='border-color:#EB5F2A;box-shadow:0 0 0 3px rgba(235,95,42,0.16);'" : "";
        return `
        <div class="source-card" id="src-${escHtml(s.source_id)}"${hl}>
          <div class="source-card-head">
            <span class="source-id-pill">${escHtml(s.source_id)}</span>
            <span class="source-org-pill">${escHtml(s.organization)} · ${escHtml(s.year)}</span>
            <span class="badge badge-ok">${escHtml(s.status)}</span>
          </div>
          <div class="source-title">${escHtml(s.retrieved_title || s.expected_title)}</div>
          <div class="source-meta">
            <strong>Journal / Citation:</strong> ${escHtml(s.journal || "N/A")}<br />
            <strong>DOI:</strong> <code>${escHtml(s.doi || "N/A")}</code> · <strong>PMID:</strong> <code>${escHtml(s.pmid || "N/A")}</code> · <strong>字元數:</strong> ${Number(s.char_count || 0).toLocaleString()}<br />
            <strong>SHA-256:</strong> <code>${escHtml(s.sha256 || "N/A")}</code><br />
            <strong>原始檔案:</strong> <code>${escHtml(s.raw_file || "N/A")}</code> · <strong>擷取日期:</strong> ${escHtml(s.retrieved_date || "")}<br />
            <strong>URL:</strong> <a href="${escHtml(s.url)}" target="_blank" rel="noopener noreferrer">${escHtml(s.url)}</a>
            ${s.reason ? `<br /><strong>擷取註記:</strong> ${escHtml(s.reason)}` : ""}
          </div>
          ${usedBy ? `<div style="margin-top:10px;"><strong style="font-size:12.5px;color:#6D6D70;">引用此文獻之 Wiki 頁面：</strong><div class="audience-links" style="margin-top:6px;">${usedBy}</div></div>` : ""}
        </div>`;
      })
      .join("");

    mainEl.innerHTML = `
      <article class="article-shell">
        <div class="article-meta-bar">
          <span class="badge badge-cat">Raw Sources Registry</span>
          <span class="badge badge-ok">${DATA.sources.filter((s) => s.status === "ingested").length} / ${DATA.sources.length} 篇來源全文驗證與 SHA-256 建檔</span>
          <span class="meta-date">資料產生時間：${escHtml(DATA.generated_at.slice(0, 10))}</span>
        </div>
        <h1 style="margin:0 0 12px;font-size:26px;">原始文獻來源庫（Immutable Raw Sources）</h1>
        <p style="color:#6D6D70;margin:0 0 20px;">所有原始擷取文獻皆保存於 <code>raw/sources/</code> 並以 SHA-256 驗證完整性，供 Wiki 條目精準追溯出處。</p>
        <div class="source-list">${cards}</div>
      </article>
    `;

    if (highlightSid) {
      const target = document.getElementById(`src-${highlightSid}`);
      if (target) target.scrollIntoView({ behavior: "smooth", block: "center" });
    } else {
      window.scrollTo({ top: 0, behavior: "instant" });
    }
  }

  function renderLog() {
    setActiveNav("log");
    mainEl.innerHTML = `
      <article class="article-shell">
        <div class="article-meta-bar">
          <span class="badge badge-cat">Persistent Wiki Evolution Log</span>
          <span class="meta-date">檔案位置：wiki/log.md</span>
        </div>
        <div class="markdown-body">${renderMarkdown(DATA.wiki_log || "尚無紀錄。", "")}</div>
      </article>
    `;
    window.scrollTo({ top: 0, behavior: "instant" });
  }

  function handleRoute() {
    closeMobileSidebar();
    const hash = decodeURIComponent(window.location.hash || "#home").replace(/^#/, "");
    if (!hash || hash === "home") {
      renderHome();
    } else if (hash === "sources") {
      renderSources(null);
    } else if (hash.startsWith("sources/")) {
      renderSources(hash.slice("sources/".length));
    } else if (hash === "log") {
      renderLog();
    } else if (hash.startsWith("page/")) {
      const rest = hash.slice("page/".length);
      const qIdx = rest.indexOf("?q=");
      if (qIdx !== -1) {
        renderPage(rest.slice(0, qIdx), rest.slice(qIdx + 3));
      } else {
        renderPage(rest, "");
      }
    } else {
      renderHome();
    }
  }

  // Search handler (Wiki pages + iGene 350 disease/gene entries)
  function runSearch(query) {
    const q = query.trim().toLowerCase();
    if (!q) {
      searchDropdown.classList.add("hidden");
      searchDropdown.innerHTML = "";
      return;
    }
    const pageMatches = [];
    for (const p of DATA.pages) {
      const haystack = `${p.title} ${p.summary} ${p.category} ${(p.source_ids || []).join(" ")} ${p.markdown}`.toLowerCase();
      if (haystack.includes(q)) {
        const titleHit = p.title.toLowerCase().includes(q) ? 2 : 1;
        pageMatches.push({ page: p, score: titleHit });
      }
    }
    pageMatches.sort((a, b) => b.score - a.score);

    const geneMatches = [];
    if (DATA.igene_panel && Array.isArray(DATA.igene_panel.items)) {
      for (const it of DATA.igene_panel.items) {
        const hay = `${it.gene_symbol} ${it.disease_name_zh} ${it.disease_name_en} ${it.inheritance_pattern}`.toLowerCase();
        if (hay.includes(q)) {
          const exactGene = it.gene_symbol.toLowerCase().includes(q) ? 2 : 1;
          geneMatches.push({ item: it, score: exactGene });
        }
      }
      geneMatches.sort((a, b) => b.score - a.score);
    }

    if (!pageMatches.length && !geneMatches.length) {
      searchDropdown.innerHTML = `<div class="search-empty">找不到符合「${escHtml(query)}」的知識頁或 iGene 疾病／基因</div>`;
    } else {
      const chunks = [];
      pageMatches.slice(0, 7).forEach(({ page }) => {
        const cat = catMap.get(page.category);
        chunks.push(`
          <a href="#page/${page.id}" class="search-result-item">
            <div class="search-result-title">${escHtml(page.title)}</div>
            <div class="search-result-meta">${escHtml(cat ? cat.label : page.category)} · ${escHtml(page.summary.slice(0, 75))}…</div>
          </a>`);
      });
      geneMatches.slice(0, 6).forEach(({ item }) => {
        chunks.push(`
          <a href="#page/products/ecs-disease-gene-index.md?q=${encodeURIComponent(item.gene_symbol)}" class="search-result-item">
            <div class="search-result-title">🧬 ${escHtml(item.gene_symbol)} — ${escHtml(item.disease_name_zh)}</div>
            <div class="search-result-meta">iGene 清單 · ${escHtml(item.disease_name_en)} · ${escHtml(item.inheritance_pattern)} · 帶因率 ${escHtml(item.carrier_frequency)}</div>
          </a>`);
      });
      searchDropdown.innerHTML = chunks.join("");
    }
    searchDropdown.classList.remove("hidden");
  }

  searchInput.addEventListener("input", (e) => runSearch(e.target.value));
  searchInput.addEventListener("focus", (e) => {
    if (e.target.value.trim()) runSearch(e.target.value);
  });
  document.addEventListener("click", (e) => {
    if (!e.target.closest(".topbar-search")) {
      searchDropdown.classList.add("hidden");
    }
  });
  searchDropdown.addEventListener("click", () => {
    searchDropdown.classList.add("hidden");
    searchInput.value = "";
  });

  menuToggleBtn.addEventListener("click", () => {
    const opening = !sidebarEl.classList.contains("open");
    sidebarEl.classList.toggle("open", opening);
    backdropEl.classList.toggle("hidden", !opening);
  });
  backdropEl.addEventListener("click", closeMobileSidebar);

  window.addEventListener("hashchange", handleRoute);

  buildSidebar();
  handleRoute();
})();
