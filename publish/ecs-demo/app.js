(function () {
  const slides = Array.from(document.querySelectorAll(".slide"));
  const totalSlides = slides.length;
  let currentSlide = 0;

  const btnPrev = document.getElementById("btn-prev");
  const btnNext = document.getElementById("btn-next");
  const btnOverview = document.getElementById("btn-overview");
  const btnCloseOverview = document.getElementById("btn-close-overview");
  const btnFullscreen = document.getElementById("btn-fullscreen");
  const progressFill = document.getElementById("progress-fill");
  const counterEl = document.getElementById("slide-counter");
  const overviewModal = document.getElementById("overview-modal");
  const thumbGrid = document.getElementById("thumb-grid");

  function escHtml(str) {
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  /* ======================================================================
   * 1. SLIDE NAVIGATION & OVERVIEW
   * ====================================================================== */
  function renderOverview() {
    thumbGrid.innerHTML = slides
      .map((s, idx) => {
        const title = s.dataset.title || `Slide ${idx + 1}`;
        return `
          <button class="thumb-btn ${idx === currentSlide ? "current" : ""}" data-jump="${idx}">
            <div class="thumb-num">SLIDE ${String(idx + 1).padStart(2, "0")}</div>
            <div class="thumb-title">${escHtml(title)}</div>
          </button>`;
      })
      .join("");
  }

  function goToSlide(idx) {
    const target = Math.max(0, Math.min(totalSlides - 1, idx));
    slides[currentSlide].classList.remove("active");
    currentSlide = target;
    slides[currentSlide].classList.add("active");

    btnPrev.disabled = currentSlide === 0;
    btnNext.disabled = currentSlide === totalSlides - 1;
    counterEl.textContent = `${currentSlide + 1} / ${totalSlides}`;
    progressFill.style.width = `${((currentSlide + 1) / totalSlides) * 100}%`;

    const desiredHash = `#slide-${currentSlide + 1}`;
    if (window.location.hash !== desiredHash) {
      history.replaceState(null, "", desiredHash);
    }
    renderOverview();
  }

  function toggleOverview(force) {
    const open = typeof force === "boolean" ? force : overviewModal.classList.contains("hidden");
    overviewModal.classList.toggle("hidden", !open);
    if (open) renderOverview();
  }

  btnPrev.addEventListener("click", () => goToSlide(currentSlide - 1));
  btnNext.addEventListener("click", () => goToSlide(currentSlide + 1));
  btnOverview.addEventListener("click", () => toggleOverview());
  btnCloseOverview.addEventListener("click", () => toggleOverview(false));
  btnFullscreen.addEventListener("click", () => {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen && document.documentElement.requestFullscreen();
    } else {
      document.exitFullscreen && document.exitFullscreen();
    }
  });

  overviewModal.addEventListener("click", (e) => {
    if (e.target === overviewModal) toggleOverview(false);
    const btn = e.target.closest("[data-jump]");
    if (btn) {
      goToSlide(Number(btn.dataset.jump));
      toggleOverview(false);
    }
  });

  document.addEventListener("keydown", (e) => {
    if (e.target && ["INPUT", "TEXTAREA", "SELECT"].includes(e.target.tagName)) return;
    if (e.key === "Escape") {
      toggleOverview(false);
      return;
    }
    if (e.key.toLowerCase() === "g") {
      e.preventDefault();
      toggleOverview();
      return;
    }
    if (!overviewModal.classList.contains("hidden")) return;
    if (e.key === "ArrowRight" || e.key === "PageDown") {
      e.preventDefault();
      goToSlide(currentSlide + 1);
    } else if (e.key === "ArrowLeft" || e.key === "PageUp") {
      e.preventDefault();
      goToSlide(currentSlide - 1);
    } else if (e.key === "Home") {
      e.preventDefault();
      goToSlide(0);
    } else if (e.key === "End") {
      e.preventDefault();
      goToSlide(totalSlides - 1);
    } else if (e.key.toLowerCase() === "f") {
      e.preventDefault();
      btnFullscreen.click();
    }
  });

  /* ======================================================================
   * 2. INTERACTIVE PUNNETT SQUARE (SLIDE 3 — AUTOSOMAL RECESSIVE)
   * ====================================================================== */
  const parentASelect = document.getElementById("parent-a");
  const parentBSelect = document.getElementById("parent-b");

  function normalizeGeno(a1, a2) {
    return a1 === "A" || a2 === "A" ? (a1 === "A" && a2 === "A" ? "AA" : "Aa") : "aa";
  }

  function genoLabel(g) {
    if (g === "AA") return "未帶因";
    if (g === "Aa") return "帶因者";
    return "雙變異";
  }

  function updatePunnett() {
    const gA = parentASelect.value;
    const gB = parentBSelect.value;
    const aAlleles = [gA[0], gA[1]];
    const bAlleles = [gB[0], gB[1]];

    document.getElementById("row-h1").textContent = `父：${aAlleles[0]}`;
    document.getElementById("row-h2").textContent = `父：${aAlleles[1]}`;
    document.getElementById("col-h1").textContent = `母：${bAlleles[0]}`;
    document.getElementById("col-h2").textContent = `母：${bAlleles[1]}`;

    const counts = { AA: 0, Aa: 0, aa: 0 };
    for (let r = 0; r < 2; r++) {
      for (let c = 0; c < 2; c++) {
        const g = normalizeGeno(aAlleles[r], bAlleles[c]);
        counts[g]++;
        const cell = document.getElementById(`cell-${r}${c}`);
        cell.className = `punnett-cell geno-${g}`;
        cell.innerHTML = `${g}<small>${genoLabel(g)}</small>`;
      }
    }

    const pAA = counts.AA * 25;
    const pAa = counts.Aa * 25;
    const paa = counts.aa * 25;

    document.getElementById("bar-AA").style.width = `${pAA}%`;
    document.getElementById("bar-Aa").style.width = `${pAa}%`;
    document.getElementById("bar-aa").style.width = `${paa}%`;
    document.getElementById("pct-AA").textContent = `${pAA}%`;
    document.getElementById("pct-Aa").textContent = `${pAa}%`;
    document.getElementById("pct-aa").textContent = `${paa}%`;

    const explainEl = document.getElementById("punnett-explain");
    if (gA === "Aa" && gB === "Aa") {
      explainEl.innerHTML =
        "<strong>標準雙帶因案例（Aa × Aa）：</strong>每次懷孕理論上有 <strong>25% AA</strong>（未帶因）、<strong>50% Aa</strong>（無症狀帶因者）與 <strong>25% aa</strong>（同時遺傳雙致病副本，可能罹病）。";
    } else if (paa === 0 && pAa > 0) {
      explainEl.innerHTML =
        `<strong>目前組合（${gA} × ${gB}）：</strong>子代理論上 <strong>0%</strong> 為雙變異（aa），但有 <strong>${pAa}%</strong> 機率成為無症狀帶因者（Aa）；實務仍須考量檢驗殘餘風險。`;
    } else if (paa === 0 && pAa === 0) {
      explainEl.innerHTML =
        "<strong>目前組合（AA × AA）：</strong>在已知雙方均無該變異的理論模型下，子代皆為 AA（0% 帶因）；臨床篩檢陰性仍須留意殘餘風險與新發突變。";
    } else {
      explainEl.innerHTML =
        `<strong>目前組合（${gA} × ${gB}）：</strong>每次懷孕理論上有 <strong>${paa}% aa</strong>（雙變異）、<strong>${pAa}% Aa</strong>（帶因者）與 <strong>${pAA}% AA</strong>（未帶因）。`;
    }

    document.querySelectorAll("[data-preset]").forEach((btn) => {
      btn.classList.toggle("active", btn.dataset.preset === `${gA},${gB}`);
    });
  }

  parentASelect.addEventListener("change", updatePunnett);
  parentBSelect.addEventListener("change", updatePunnett);
  document.querySelectorAll("[data-preset]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const [a, b] = btn.dataset.preset.split(",");
      parentASelect.value = a;
      parentBSelect.value = b;
      updatePunnett();
    });
  });

  /* ======================================================================
   * 3. X-LINKED INTERACTIVE SCENARIOS (SLIDE 4)
   * ====================================================================== */
  const X_MODES = {
    mother: {
      svg: `
        <h3>母親為 X-linked 帶因者（X*X × XY）</h3>
        <svg viewBox="0 0 420 154" width="100%" aria-label="母親帶因之X性聯遺傳圖解">
          <rect x="86" y="8" width="102" height="32" rx="8" fill="#ECF7EF" stroke="#225E38" stroke-width="1.5"/>
          <text x="137" y="29" text-anchor="middle" font-size="12.5" font-weight="700" fill="#225E38">父：正常 (XY)</text>
          <rect x="232" y="8" width="104" height="32" rx="8" fill="#FFEAE4" stroke="#EB5F2A" stroke-width="1.6"/>
          <text x="284" y="29" text-anchor="middle" font-size="12.5" font-weight="700" fill="#B93516">母：帶因 (X*X)</text>
          <line x1="137" y1="40" x2="210" y2="62" stroke="#B95F2B" stroke-width="1.5"/>
          <line x1="284" y1="40" x2="210" y2="62" stroke="#B95F2B" stroke-width="1.5"/>
          <line x1="56" y1="62" x2="364" y2="62" stroke="#B95F2B" stroke-width="1.5"/>
          <line x1="56" y1="62" x2="56" y2="82" stroke="#B95F2B" stroke-width="1.5"/>
          <line x1="160" y1="62" x2="160" y2="82" stroke="#B95F2B" stroke-width="1.5"/>
          <line x1="262" y1="62" x2="262" y2="82" stroke="#B95F2B" stroke-width="1.5"/>
          <line x1="364" y1="62" x2="364" y2="82" stroke="#B95F2B" stroke-width="1.5"/>
          <rect x="8" y="82" width="96" height="62" rx="9" fill="#ECF7EF" stroke="#225E38" stroke-width="1.5"/>
          <text x="56" y="104" text-anchor="middle" font-size="12.5" font-weight="800" fill="#225E38">25% 女兒</text>
          <text x="56" y="122" text-anchor="middle" font-size="11.5" fill="#352B25">XX 未帶因</text>
          <rect x="112" y="82" width="96" height="62" rx="9" fill="#FFF3E3" stroke="#E88A42" stroke-width="1.5"/>
          <text x="160" y="104" text-anchor="middle" font-size="12.5" font-weight="800" fill="#B95F2B">25% 女兒</text>
          <text x="160" y="122" text-anchor="middle" font-size="11.5" fill="#352B25">X*X 帶因</text>
          <text x="160" y="137" text-anchor="middle" font-size="9.5" fill="#6D6D70">症狀依疾病而異</text>
          <rect x="214" y="82" width="96" height="62" rx="9" fill="#ECF7EF" stroke="#225E38" stroke-width="1.5"/>
          <text x="262" y="104" text-anchor="middle" font-size="12.5" font-weight="800" fill="#225E38">25% 兒子</text>
          <text x="262" y="122" text-anchor="middle" font-size="11.5" fill="#352B25">XY 未遺傳</text>
          <rect x="316" y="82" width="96" height="62" rx="9" fill="#FFEAE4" stroke="#EB5F2A" stroke-width="1.8"/>
          <text x="364" y="104" text-anchor="middle" font-size="12.5" font-weight="800" fill="#B93516">25% 兒子</text>
          <text x="364" y="122" text-anchor="middle" font-size="11.5" fill="#B93516">X*Y 受影響</text>
          <text x="364" y="137" text-anchor="middle" font-size="9.5" fill="#B93516">無另一條 X 代償</text>
        </svg>`,
      text: `
        <h3>📌 情境 A 重點（ECS 主要篩檢對象）</h3>
        <ul>
          <li><strong>無須父親同基因帶因：</strong>只要母親為 X 性聯疾病帶因者，每次懷孕即有 <strong>50%</strong> 機率將變異 X 染色體傳給子代 <span class="cite">SRC-003</span>。</li>
          <li><strong>男性子代（XY）：</strong>有 50% 機率遺傳變異 X 並表現疾病（因男性僅有一條 X 染色體）<span class="cite">SRC-003</span>。</li>
          <li><strong>女性子代（XX）：</strong>有 50% 機率成為帶因者，臨床上可能無症狀或依特定疾病與 X 去活化呈現輕重不等表型 <span class="cite">SRC-003</span>。</li>
          <li><strong>自身健康追蹤：</strong>部分 X 性聯基因女性帶因者本身亦需評估健康管理（如 <em>DMD</em> 帶因者心肌追蹤）<span class="cite">SRC-003</span>。</li>
        </ul>`,
    },
    father: {
      svg: `
        <h3>父親帶有變異 X 染色體（XX × X*Y）</h3>
        <svg viewBox="0 0 420 154" width="100%" aria-label="父親帶變異X染色體之性聯遺傳圖解">
          <rect x="86" y="8" width="104" height="32" rx="8" fill="#FFEAE4" stroke="#EB5F2A" stroke-width="1.6"/>
          <text x="138" y="29" text-anchor="middle" font-size="12.5" font-weight="700" fill="#B93516">父：變異 (X*Y)</text>
          <rect x="232" y="8" width="102" height="32" rx="8" fill="#ECF7EF" stroke="#225E38" stroke-width="1.5"/>
          <text x="283" y="29" text-anchor="middle" font-size="12.5" font-weight="700" fill="#225E38">母：正常 (XX)</text>
          <line x1="138" y1="40" x2="210" y2="62" stroke="#B95F2B" stroke-width="1.5"/>
          <line x1="283" y1="40" x2="210" y2="62" stroke="#B95F2B" stroke-width="1.5"/>
          <line x1="108" y1="62" x2="312" y2="62" stroke="#B95F2B" stroke-width="1.5"/>
          <line x1="108" y1="62" x2="108" y2="82" stroke="#B95F2B" stroke-width="1.5"/>
          <line x1="312" y1="62" x2="312" y2="82" stroke="#B95F2B" stroke-width="1.5"/>
          <rect x="28" y="82" width="160" height="62" rx="9" fill="#FFF3E3" stroke="#E88A42" stroke-width="1.6"/>
          <text x="108" y="104" text-anchor="middle" font-size="13" font-weight="800" fill="#B95F2B">所有女兒（100%）</text>
          <text x="108" y="123" text-anchor="middle" font-size="11.5" fill="#352B25">必遺傳父親 X*（X*X）</text>
          <text x="108" y="138" text-anchor="middle" font-size="9.5" fill="#6D6D70">成為帶因者（表現依疾病異）</text>
          <rect x="232" y="82" width="160" height="62" rx="9" fill="#ECF7EF" stroke="#225E38" stroke-width="1.5"/>
          <text x="312" y="104" text-anchor="middle" font-size="13" font-weight="800" fill="#225E38">所有兒子（100%）</text>
          <text x="312" y="123" text-anchor="middle" font-size="11.5" fill="#352B25">遺傳父親 Y（XY）</text>
          <text x="312" y="138" text-anchor="middle" font-size="9.5" fill="#225E38">不會遺傳父親的 X*</text>
        </svg>`,
      text: `
        <h3>📌 情境 B 重點（性染色體傳遞對照）</h3>
        <ul>
          <li><strong>無男傳男現象：</strong>父親必將 Y 染色體傳給兒子，因此兒子不會從父親遺傳 X 性聯變異。</li>
          <li><strong>所有女兒均承接父親 X 染色體：</strong>若父親帶有 X 性聯致病變異，其女兒理論上 100% 會遺傳該變異 X 染色體（成為帶因者，表型視具體疾病而異）。</li>
          <li><strong>教學備註：</strong>此情境為孟德爾性染色體基本傳遞原則對照；臨床上嚴重早發型 X 性聯疾病多由女性無症狀帶因者透過孕前 ECS 辨識 <span class="cite">SRC-003</span>。</li>
        </ul>`,
    },
  };

  function renderXMode(key) {
    const m = X_MODES[key];
    if (!m) return;
    document.getElementById("xlinked-diagram-card").innerHTML = m.svg;
    document.getElementById("xlinked-text-card").innerHTML = m.text;
    document.querySelectorAll("[data-xmode]").forEach((btn) => {
      btn.classList.toggle("active", btn.dataset.xmode === key);
    });
  }

  document.querySelectorAll("[data-xmode]").forEach((btn) => {
    btn.addEventListener("click", () => renderXMode(btn.dataset.xmode));
  });

  /* ======================================================================
   * 4. PUBLIC ECS 350-DISEASE / 351-GENE LIVE SEARCH (SLIDE 7 — SRC-009)
   *    Note: Unverified product performance metrics are omitted in this demo.
   * ====================================================================== */
  const demoData = window.ECS_DEMO_DATA;
  const searchInput = document.getElementById("gene-search-input");
  const inhFilter = document.getElementById("gene-inh-filter");
  const catFilter = document.getElementById("gene-cat-filter");
  const geneTbody = document.getElementById("gene-table-body");
  const geneCountEl = document.getElementById("gene-result-count");

  function initGeneSearch() {
    if (!demoData || !Array.isArray(demoData.items)) {
      geneTbody.innerHTML =
        "<tr><td colspan='6' style='text-align:center;padding:18px;color:#B93516;'>無法載入公開教學資料集（ecs_public_data.js）。</td></tr>";
      return;
    }
    const cats = (demoData.summary_stats && demoData.summary_stats.primary_category_counts) || [];
    cats.forEach((c) => {
      const opt = document.createElement("option");
      opt.value = c.name;
      opt.textContent = `${c.code}. ${c.name} (${c.disease_count})`;
      catFilter.appendChild(opt);
    });
    renderGeneRows();
  }

  function renderGeneRows() {
    if (!demoData) return;
    const q = searchInput.value.trim().toLowerCase();
    const inh = inhFilter.value;
    const cat = catFilter.value;

    const matches = demoData.items.filter((it) => {
      if (inh && it.inh !== inh) return false;
      if (cat && it.cat !== cat) return false;
      if (q) {
        const hay = `${it.zh} ${it.en} ${it.gene} ${it.inh} ${it.catFull} ${it.pop}`.toLowerCase();
        if (!hay.includes(q)) return false;
      }
      return true;
    });

    geneCountEl.textContent = `符合 ${matches.length} / ${demoData.items.length} 筆`;

    if (!matches.length) {
      const extraHint =
        q.includes("fmr1") || q.includes("脆折")
          ? "<br /><span style='color:#B93516;font-weight:700;'>說明：FMR1（X 染色體脆折症）屬 CGG 三核苷酸重複擴增，未收錄於此 350 項目標區間 NGS 公開範例清單中 [SRC-003] [SRC-009]。</span>"
          : "";
      geneTbody.innerHTML = `<tr><td colspan="6" style="text-align:center;padding:18px;color:#6D6D70;">查無符合「${escHtml(searchInput.value)}」之項目（本表僅呈現公開範例資料集之 350 筆資料，不虛構項目）${extraHint}</td></tr>`;
      return;
    }

    geneTbody.innerHTML = matches
      .map((it) => {
        const cls = it.inh === "XL" ? "inh-XL" : it.inh === "AR/AD" ? "inh-ARAD" : "inh-AR";
        return `
          <tr>
            <td>${escHtml(it.id)}</td>
            <td><strong>${escHtml(it.zh)}</strong><div style="font-size:10.8px;color:#6D6D70;">${escHtml(it.en)} · ${escHtml(it.cat)}</div></td>
            <td><code>${escHtml(it.gene)}</code></td>
            <td><span class="inh-tag ${cls}">${escHtml(it.inh)}</span></td>
            <td>${escHtml(it.pop)}</td>
            <td>${escHtml(it.freq)}</td>
          </tr>`;
      })
      .join("");
  }

  searchInput.addEventListener("input", renderGeneRows);
  inhFilter.addEventListener("change", renderGeneRows);
  catFilter.addEventListener("change", renderGeneRows);
  document.querySelectorAll("[data-q]").forEach((btn) => {
    btn.addEventListener("click", () => {
      searchInput.value = btn.dataset.q;
      inhFilter.value = "";
      catFilter.value = "";
      renderGeneRows();
    });
  });

  /* ======================================================================
   * 5. INTERACTIVE 5-QUESTION KNOWLEDGE QUIZ (SLIDE 10)
   * ====================================================================== */
  const QUIZ_ITEMS = [
    {
      topic: "1. 帶因者的意義",
      q: "Q1. 關於體染色體隱性遺傳的「帶因者（Carrier）」，下列哪一項敘述最正確？",
      options: [
        "A. 只要檢出為帶因者，就代表受檢者本人一定已經罹患該遺傳疾病。",
        "B. 帶因者通常僅有一個等位基因帶有致病變異，本人多數健康無症狀，但可能將該變異傳給下一代。",
        "C. 只要家族過去沒有遺傳病史，就不可能是任何隱性遺傳疾病的帶因者。",
        "D. 只有女性會成為體染色體隱性遺傳疾病的帶因者。",
      ],
      answer: 1,
      feedback:
        "正確答案為 B。體染色體隱性帶因者因另一條染色體上仍有正常基因副本，絕大多數完全健康無症狀，因此常無家族病史；男女皆可能為體染色體隱性帶因者。",
      source: "公開來源參考：ACMG 2021 Practice Resource [SRC-003]、公開疾病清單 [SRC-009]",
    },
    {
      topic: "2. 常染色體隱性遺傳風險",
      q: "Q2. 在單基因常染色體隱性遺傳模型（Aa × Aa）下，當父母雙方皆為同一基因帶因者時，每次懷孕之理論子代基因型機率為何？",
      options: [
        "A. 100% 必定罹患該遺傳疾病。",
        "B. 50% 罹病（aa）、50% 完全未帶因（AA）。",
        "C. 25% 未帶因（AA）、50% 帶因者（Aa）、25% 雙變異罹病風險（aa）。",
        "D. 只有男寶寶會有 25% 罹病機率，女寶寶不會罹病。",
      ],
      answer: 2,
      feedback:
        "正確答案為 C。在 Aa × Aa 理論模型下，每次懷孕（不分胎兒性別且各自獨立）為 25% AA、50% Aa、25% aa；此為特定模型之理論基因型機率，不等同所有 ECS 疾病的實際臨床發病率。",
      source: "公開來源參考：ACMG 2021 Practice Resource [SRC-003]",
    },
    {
      topic: "3. ECS 檢測目的與範圍邊界",
      q: "Q3. 關於擴展性帶因者篩檢（ECS）的檢測目的與套組邊界，下列何者正確？",
      options: [
        "A. 透過高通量定序於孕前或孕期同步評估多種隱性與 X 性聯單基因帶因狀態，協助伴侶提早了解生育風險。",
        "B. 只要做過 ECS，就等同完成胚胎 24 條染色體檢查（PGT-A）與所有先天異常診斷。",
        "C. 公開範例清單標示 350 種疾病，代表正好檢測 350 個基因且涵蓋所有人類遺傳病。",
        "D. 國際指引規定所有育齡民眾都「強制必須」在懷孕前接受 ECS。",
      ],
      answer: 0,
      feedback:
        "正確答案為 A。ECS 屬於自願性帶因風險評估工具（非強制），無法取代染色體檢查或完整臨床診斷；且 350 種疾病範例對應 351 個去重獨立基因（含雙基因 HBA1/HBA2），亦未涵蓋所有遺傳病（如不含重複擴增型 FMR1）。",
      source: "公開來源參考：ACMG 2021 [SRC-003]、公開 ECS 範例清單 [SRC-009]",
    },
    {
      topic: "4. ECS 陰性結果與 Residual Risk",
      q: "Q4. 若夫妻雙方 ECS 篩檢結果皆為「陰性（No Reportable Variant Detected）」，應如何正確解讀？",
      options: [
        "A. 代表寶寶 100% 不會罹患任何遺傳疾病，未來可省略新生兒篩檢。",
        "B. 大幅降低成為受檢疾病帶因者的機率，但殘餘風險（Residual Risk）永遠不為零，孕期產檢與出生後新生兒篩檢仍建議進行。",
        "C. 代表已排除所有大片段缺失、三核苷酸重複擴增與懷孕中發生的胎兒新發突變。",
        "D. 代表已完全排除任何單基因與染色體異常之可能。",
      ],
      answer: 1,
      feedback:
        "正確答案為 B。ACMG 2021 明確強調陰性結果僅能降低風險、任何疾病的 Residual Risk 永遠不為零；目標區間 NGS 亦無法排除結構重排、重複序列擴增、套組外疾病與新發突變，出生後仍建議接受新生兒篩檢。",
      source: "公開來源參考：ACMG 2021 Practice Resource [SRC-003]",
    },
    {
      topic: "5. 遺傳諮詢的重要性",
      q: "Q5. 為什麼國際指引強調 ECS 應搭配「檢測前與檢測後遺傳諮詢（Genetic Counseling）」？",
      options: [
        "A. 只有在檢出陽性之後才需要遺傳諮詢，檢測前不需要了解限制與選項。",
        "B. 遺傳諮詢能確保受檢者在了解檢測效益、限制與殘餘風險後自主決定；檢出高風險伴侶時則協助討論產前診斷、IVF 合併 PGT-M 等多元生育選項。",
        "C. 遺傳諮詢的目的是替患者直接決定一定要做試管嬰兒與 PGT-M。",
        "D. 遺傳諮詢可以完全消除檢測的不確定性與殘餘風險。",
      ],
      answer: 1,
      feedback:
        "正確答案為 B。ACMG 2021 與 ASRM 2023 皆強調檢前與檢後遺傳諮詢缺一不可：協助民眾充分知情並自主選擇（含選擇不檢測），並在檢出共同風險或複雜變異時完整討論各種生育規劃選項。",
      source: "公開來源參考：ACMG 2021 [SRC-003]、ASRM 2023 [SRC-006]",
    },
  ];

  let activeQ = 0;
  const userAnswers = new Array(QUIZ_ITEMS.length).fill(null);

  const quizTabsEl = document.getElementById("quiz-tabs");
  const quizScoreEl = document.getElementById("quiz-score");
  const quizQuestionEl = document.getElementById("quiz-question");
  const quizOptionsEl = document.getElementById("quiz-options");
  const quizFeedbackEl = document.getElementById("quiz-feedback");
  const quizPrevBtn = document.getElementById("quiz-prev");
  const quizNextBtn = document.getElementById("quiz-next");
  const quizResetBtn = document.getElementById("quiz-reset");

  function renderQuiz() {
    const item = QUIZ_ITEMS[activeQ];
    const chosen = userAnswers[activeQ];

    const answeredCount = userAnswers.filter((v) => v !== null).length;
    const correctCount = userAnswers.filter((v, idx) => v === QUIZ_ITEMS[idx].answer).length;
    quizScoreEl.textContent = `已作答 ${answeredCount} / ${QUIZ_ITEMS.length}｜正確 ${correctCount} 題`;

    quizTabsEl.innerHTML = QUIZ_ITEMS.map((_, idx) => {
      let cls = "q-tab";
      if (idx === activeQ) cls += " active";
      if (userAnswers[idx] !== null) {
        cls += userAnswers[idx] === QUIZ_ITEMS[idx].answer ? " done-ok" : " done-wrong";
      }
      return `<button class="${cls}" data-qidx="${idx}">Q${idx + 1}</button>`;
    }).join("");

    quizQuestionEl.textContent = item.q;
    quizOptionsEl.innerHTML = item.options
      .map((opt, idx) => {
        let cls = "quiz-opt";
        if (chosen !== null) {
          if (idx === item.answer) cls += " is-correct";
          else if (idx === chosen && chosen !== item.answer) cls += " is-wrong";
        }
        return `<button class="${cls}" data-opt="${idx}">${escHtml(opt)}</button>`;
      })
      .join("");

    if (chosen === null) {
      quizFeedbackEl.className = "quiz-feedback-box";
      quizFeedbackEl.innerHTML = `<strong>主題：${escHtml(item.topic)}</strong> — 請點選上方選項查看即時解析與公開文獻參考。`;
    } else if (chosen === item.answer) {
      quizFeedbackEl.className = "quiz-feedback-box ok";
      quizFeedbackEl.innerHTML = `<strong>✅ 答對了！</strong>${escHtml(item.feedback)}<br /><small>${escHtml(item.source)}</small>`;
    } else {
      quizFeedbackEl.className = "quiz-feedback-box warn";
      quizFeedbackEl.innerHTML = `<strong>💡 再確認一下：</strong>${escHtml(item.feedback)}<br /><small>${escHtml(item.source)}</small>`;
    }

    quizPrevBtn.disabled = activeQ === 0;
    quizNextBtn.disabled = activeQ === QUIZ_ITEMS.length - 1;
  }

  quizTabsEl.addEventListener("click", (e) => {
    const btn = e.target.closest("[data-qidx]");
    if (btn) {
      activeQ = Number(btn.dataset.qidx);
      renderQuiz();
    }
  });

  quizOptionsEl.addEventListener("click", (e) => {
    const btn = e.target.closest("[data-opt]");
    if (btn) {
      userAnswers[activeQ] = Number(btn.dataset.opt);
      renderQuiz();
    }
  });

  quizPrevBtn.addEventListener("click", () => {
    if (activeQ > 0) {
      activeQ--;
      renderQuiz();
    }
  });

  quizNextBtn.addEventListener("click", () => {
    if (activeQ < QUIZ_ITEMS.length - 1) {
      activeQ++;
      renderQuiz();
    }
  });

  quizResetBtn.addEventListener("click", () => {
    userAnswers.fill(null);
    activeQ = 0;
    renderQuiz();
  });

  /* ======================================================================
   * 6. INITIALIZE
   * ====================================================================== */
  updatePunnett();
  renderXMode("mother");
  initGeneSearch();
  renderQuiz();

  const hashMatch = window.location.hash.match(/^#slide-(\d+)$/);
  const initialIdx = hashMatch ? Number(hashMatch[1]) - 1 : 0;
  goToSlide(initialIdx);
})();
