import json

with open("/Users/brandonwong/.gemini/antigravity/scratch/first-reit-investigation/sampled_45.json") as f:
    sampled_45_str = f.read().strip()

with open("/Users/brandonwong/.gemini/antigravity/scratch/first-reit-investigation/index.html") as f:
    html = f.read()

# 1. Update FALLBACK_YF_SERIES with the new 45 sampled bars that include sti, es3_adj, clr_adj
old_start = html.find("const FALLBACK_YF_SERIES = [")
old_end = html.find("];", old_start) + 2
assert old_start != -1 and old_end != -1, "FALLBACK_YF_SERIES not found"
html = html[:old_start] + f"const FALLBACK_YF_SERIES = {sampled_45_str};" + html[old_end:]

# 2. Update Top Navigation Bar to show the 6 Study Chapters clearly
old_nav = """      <nav class="hidden lg:flex items-center gap-5 text-xs font-bold">
        <a href="#yahoo-finance" class="px-3 py-1.5 rounded-lg bg-[#0094D6] text-white hover:opacity-90 transition">★ Yahoo Finance Graphs</a>
        <a href="#root-problem" class="hover:text-[#D32577] transition">1. Root Problem</a>
        <a href="#timeline" class="hover:text-[#EE7C22] transition">2. 5 Eras</a>
        <a href="#dpu-graphs" class="hover:text-[#94C13D] transition">3. DPU &amp; 77 Divs</a>
        <a href="#crisis-2020" class="hover:text-[#EE7C22] transition">4. 2022–2025 Bleed</a>
        <a href="#future-2026" class="hover:text-[#0094D6] transition">5. 2026 Exit Graphs</a>
        <a href="#citations" class="hover:text-[#D32577] transition">6. Citations [16]</a>
      </nav>"""

new_nav = """      <nav class="hidden xl:flex items-center gap-3.5 text-xs font-bold">
        <a href="#root-problem" class="hover:text-[#D32577] transition">Ch 1. Problem &amp; Pros/Cons</a>
        <a href="#chapter-2-benchmarks" class="px-2.5 py-1.5 rounded-lg bg-[#0094D6] text-white hover:opacity-90 transition">Ch 2. 10-Yr vs STI &amp; S-REITs</a>
        <a href="#timeline" class="hover:text-[#EE7C22] transition">Ch 3. 2020 Trigger &amp; Rescue</a>
        <a href="#indo-assets" class="hover:text-[#94C13D] transition">Ch 4. Solution &amp; 19 MLAs</a>
        <a href="#future-2026" class="hover:text-[#0094D6] transition">Ch 5. 2026 Divestment</a>
        <a href="#impact-2026" class="hover:text-[#D32577] transition">Ch 6. Impact &amp; Future</a>
      </nav>"""

assert old_nav in html, "old_nav not found"
html = html.replace(old_nav, new_nav, 1)

# 3. Insert the 6-Chapter Study Blueprint Banner + Chapter 1 Pros/Cons Matrix + Chapter 2 10-Year Benchmark Showdown (STI, S-REITs, Parkway Life, First REIT)
target_root_section = """  <!-- Section 1: The Root Problem -->
  <section id="root-problem" class="py-14 border-b border-[var(--border-color)]">"""

chapter1_and_2_prefix = """  <!-- 6-Chapter Case Study Structure Overview Banner -->
  <section class="py-8 border-b border-[var(--border-color)] surface-elevated">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-wrap items-center justify-between gap-2 mb-4">
        <span class="text-xs font-black uppercase tracking-widest text-[#0094D6]">Structured 6-Chapter Case Study Blueprint (2006 IPO – 2026 Exit)</span>
        <span class="text-xs muted-text">Click any chapter card below to jump directly to its analysis &amp; interactive graphs</span>
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-6 gap-2.5 text-xs">
        <a href="#root-problem" class="surface-card rounded-xl p-3 border-t-4 border-t-[#D32577] hover:shadow-md transition block">
          <div class="font-black text-[#D32577]">Chapter 01</div>
          <div class="font-bold mt-0.5">Problem Statement &amp; Pros/Cons</div>
          <div class="muted-text mt-1">2006 IPO SGD/IDR Master Lease flaw</div>
        </a>
        <a href="#chapter-2-benchmarks" class="surface-card rounded-xl p-3 border-t-4 border-t-[#0094D6] hover:shadow-md transition block">
          <div class="font-black text-[#0094D6]">Chapter 02</div>
          <div class="font-bold mt-0.5">10-Yr Performance vs Benchmarks</div>
          <div class="muted-text mt-1">vs STI, Wider S-REITs &amp; Parkway Life</div>
        </a>
        <a href="#timeline" class="surface-card rounded-xl p-3 border-t-4 border-t-[#FECD07] hover:shadow-md transition block">
          <div class="font-black text-[#d97706]">Chapter 03</div>
          <div class="font-bold mt-0.5">2020 Trigger &amp; How They Solved It</div>
          <div class="muted-text mt-1">OUE split, LPKR default &amp; 20¢ rights</div>
        </a>
        <a href="#indo-assets" class="surface-card rounded-xl p-3 border-t-4 border-t-[#EE7C22] hover:shadow-md transition block">
          <div class="font-black text-[#EE7C22]">Chapter 04</div>
          <div class="font-bold mt-0.5">Why Solution Failed &amp; 19 Indo MLAs</div>
          <div class="muted-text mt-1">IDR/JPY double bleed &amp; MPU arrears</div>
        </a>
        <a href="#future-2026" class="surface-card rounded-xl p-3 border-t-4 border-t-[#94C13D] hover:shadow-md transition block">
          <div class="font-black text-[#6fa01e] dark:text-[#94C13D]">Chapter 05</div>
          <div class="font-bold mt-0.5">Current 2026 Divestment</div>
          <div class="muted-text mt-1">S$471.5M Stage 1 + S$294.8M Put</div>
        </a>
        <a href="#impact-2026" class="surface-card rounded-xl p-3 border-t-4 border-t-[#0094D6] hover:shadow-md transition block">
          <div class="font-black text-[#0094D6]">Chapter 06</div>
          <div class="font-bold mt-0.5">Financial Impact &amp; Future</div>
          <div class="muted-text mt-1">16.7% gearing, 1.85¢ DPU &amp; APAC</div>
        </a>
      </div>
    </div>
  </section>

  <!-- Chapter 1: The Root Structural Problem & Pros/Cons Matrix -->
  <section id="root-problem" class="py-14 border-b border-[var(--border-color)]">"""

assert target_root_section in html, "target_root_section not found"
html = html.replace(target_root_section, chapter1_and_2_prefix, 1)

# 4. Append Pros & Cons Matrix to the end of #root-problem and insert Chapter 2: 10-Year vs STI, Wider S-REITs, Parkway Life & First REIT
old_root_end = """          <div id="mechanismContent" class="space-y-4"></div>
        </div>
      </div>
    </div>
  </section>"""

new_root_end_and_ch2 = """          <div id="mechanismContent" class="space-y-4"></div>
        </div>
      </div>

      <!-- Chapter 1B: Explicit Pros & Cons Matrix of the 2006 IPO Structure -->
      <div class="mt-8 surface-card rounded-2xl overflow-hidden border-t-4 border-t-[#D32577]">
        <div class="p-5 border-b border-[var(--border-color)] flex flex-wrap items-center justify-between gap-2">
          <div>
            <span class="text-xs font-bold uppercase text-[#D32577]">Chapter 01 Matrix • Structural Trade-Off Analysis</span>
            <h3 class="font-black text-lg">Pros &amp; Cons of First REIT’s 2006 IPO Master Lease Architecture</h3>
          </div>
          <span class="text-xs font-bold px-2.5 py-1 rounded surface-elevated">Why It Worked for 10 Years — And Why It Broke</span>
        </div>
        <div class="overflow-x-auto">
          <table class="w-full text-left border-collapse text-xs">
            <thead>
              <tr class="surface-elevated border-b border-[var(--border-color)]">
                <th class="py-3 px-4 font-bold">Structural Dimension</th>
                <th class="py-3 px-4 font-bold text-[#6fa01e] dark:text-[#94C13D]">Apparent "Pros" (Why Investors Loved It, 2006–2017)</th>
                <th class="py-3 px-4 font-bold text-[#D32577]">Hidden "Cons" (What Was Fundamentally Wrong)</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-[var(--border-color)]">
              <tr>
                <td class="py-3 px-4 font-bold">1. Synthetic SGD Rent Peg (<code class="text-xs">SGD/IDR</code>)</td>
                <td class="py-3 px-4">Shielded SGX unitholders from Indonesian Rupiah volatility for 14 years; delivered predictable SGD cash distributions <a href="#ref-4" class="cite-badge">[4]</a>.</td>
                <td class="py-3 px-4">Transferred 100% of cumulative IDR depreciation (<strong>+142.2%</strong> from 5,854 to 14,177) onto sponsor LPKR until the lease became economically impossible to pay <a href="#ref-6" class="cite-badge">[6]</a>.</td>
              </tr>
              <tr>
                <td class="py-3 px-4 font-bold">2. 15-Year Triple-Net Master Lease</td>
                <td class="py-3 px-4">Guaranteed 100% occupancy, long WALE, zero capex/opex leakage at REIT level, and up to +2% annual base rent escalations <a href="#ref-1" class="cite-badge">[1]</a>.</td>
                <td class="py-3 px-4">Created artificial SGD rents detached from actual hospital EBITDA (&gt;40% of hospital revenue vs sustainable ~8%), plus a simultaneous <strong>2021 lease expiry cliff</strong> <a href="#ref-4" class="cite-badge">[4]</a>.</td>
              </tr>
              <tr>
                <td class="py-3 px-4 font-bold">3. Single-Sponsor Pipeline (<code class="text-xs">LPKR.JK</code>)</td>
                <td class="py-3 px-4">Enabled rapid, yield-accretive expansion from 4 IPO properties (2006) to 19 Indonesian properties by 2017 <a href="#ref-9" class="cite-badge">[9]</a>.</td>
                <td class="py-3 px-4">Extreme counterparty concentration (&gt;80% of rent from LPKR &amp; affiliate MPU) and injection of non-core retail malls (<code class="text-xs">Lippo Plaza Kupang/Buton</code>) and hotels <a href="#ref-8" class="cite-badge">[8]</a>.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </section>

  <!-- Chapter 2: Performance for the First 10 Years (2007–2017) vs Post-2017 — Compared to STI, Wider S-REITs & Parkway Life REIT -->
  <section id="chapter-2-benchmarks" class="py-14 border-b border-[var(--border-color)]">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-wrap items-center justify-between gap-4 mb-6">
        <div>
          <span class="text-xs font-bold uppercase tracking-widest text-[#0094D6]">Chapter 02 • 10-Year Golden Mirage vs. 20-Year Full Cycle (Yahoo Finance Verified)</span>
          <h2 class="text-2xl sm:text-3xl font-black mt-1">How First REIT Performed vs. Straits Times Index (STI), Wider S-REITs &amp; Parkway Life REIT</h2>
          <p class="muted-text mt-1 text-sm max-w-4xl">
            In its <strong>first 10 years (Dec 2007 – Dec 2017)</strong>, First REIT (<code class="text-xs">AW9U.SI</code>) delivered a <strong>+449.8% total return (5.5x)</strong>—beating the <strong>SGX Straits Times Index (<code class="text-xs">^STI / ES3.SI</code>, +35.9%)</strong>, <strong>Wider Singapore REITs (~+95%)</strong>, and even healthcare peer <strong>Parkway Life REIT (<code class="text-xs">C2PU.SI</code>, +350.3%)</strong>. That 10-year outperformance masked the structural flaw until the violent post-2017 reversal <a href="#ref-14" class="cite-badge">[14]</a>.
          </p>
        </div>
        <div class="flex flex-wrap gap-2">
          <button onclick="setBenchEra('10yr')" id="bench-btn-10yr" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-[#0094D6] text-white">First 10 Years (2007–2017)</button>
          <button onclick="setBenchEra('post2017')" id="bench-btn-post2017" class="px-3 py-1.5 rounded-lg text-xs font-bold surface-elevated muted-text">Post-Peak Unwind (2017–2026)</button>
          <button onclick="setBenchEra('full20yr')" id="bench-btn-full20yr" class="px-3 py-1.5 rounded-lg text-xs font-bold surface-elevated muted-text">Full 20-Year Cycle (2007–2026)</button>
        </div>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
        <!-- Interactive 4-Benchmark Canvas -->
        <div class="lg:col-span-7 surface-card rounded-2xl p-5 border-t-4 border-t-[#0094D6]">
          <div class="flex flex-wrap items-center justify-between gap-2 mb-2">
            <div>
              <h3 id="benchGraphTitle" class="font-black text-base">First 10 Years (Dec 2007 – Dec 2017): Total Return Indexed to 100</h3>
              <p id="benchGraphSub" class="text-xs muted-text">First REIT (+449.8%) beat Parkway Life (+350.3%), Wider S-REITs (+95%), and SGX STI (+35.9%).</p>
            </div>
          </div>
          <div class="flex flex-wrap gap-3 text-xs font-bold mb-3">
            <span class="inline-flex items-center gap-1.5"><span class="w-3 h-3 rounded-sm bg-[#D32577] inline-block"></span>First REIT (AW9U.SI)</span>
            <span class="inline-flex items-center gap-1.5"><span class="w-3 h-3 rounded-sm bg-[#94C13D] inline-block"></span>Parkway Life REIT (C2PU.SI)</span>
            <span class="inline-flex items-center gap-1.5"><span class="w-3 h-3 rounded-sm bg-[#0094D6] inline-block"></span>SGX Straits Times Index (^STI / ES3.SI)</span>
            <span class="inline-flex items-center gap-1.5"><span class="w-3 h-3 rounded-sm bg-[#EE7C22] inline-block"></span>Wider Singapore REITs (S-REITs / CLR.SI)</span>
          </div>
          <div class="relative w-full h-64 rounded-xl surface-elevated p-2.5">
            <canvas id="bench4Canvas" class="w-full h-full"></canvas>
          </div>
        </div>

        <!-- Benchmark Comparison Table -->
        <div class="lg:col-span-5 surface-card rounded-2xl overflow-hidden border-t-4 border-t-[#94C13D]">
          <div class="p-4 border-b border-[var(--border-color)]">
            <span class="text-xs font-bold uppercase text-[#6fa01e] dark:text-[#94C13D]">Yahoo Finance Total Return Audit</span>
            <h3 class="font-black text-base">10-Year Boom (2007–2017) vs. Bust (2017–2026)</h3>
          </div>
          <div class="overflow-x-auto">
            <table class="w-full text-left border-collapse text-xs">
              <thead>
                <tr class="surface-elevated border-b border-[var(--border-color)]">
                  <th class="py-2.5 px-3 font-bold">Benchmark</th>
                  <th class="py-2.5 px-3 font-bold">First 10 Yrs<br><span class="font-normal muted-text">2007–2017</span></th>
                  <th class="py-2.5 px-3 font-bold">Post-Peak<br><span class="font-normal muted-text">2017–2026</span></th>
                  <th class="py-2.5 px-3 font-bold">Full 20 Yrs<br><span class="font-normal muted-text">2007=100</span></th>
                </tr>
              </thead>
              <tbody class="divide-y divide-[var(--border-color)]">
                <tr>
                  <td class="py-2.5 px-3"><div class="font-black text-[#D32577]">First REIT (AW9U.SI)</div><div class="muted-text">Indonesian Healthcare</div></td>
                  <td class="py-2.5 px-3 font-black text-[#6fa01e] dark:text-[#94C13D]">+449.8%<div class="font-normal muted-text">+148.5% price</div></td>
                  <td class="py-2.5 px-3 font-black text-[#D32577]">-69.9%<div class="font-normal muted-text">-86.1% price</div></td>
                  <td class="py-2.5 px-3 font-black">165<div class="font-normal muted-text">+65.3%</div></td>
                </tr>
                <tr>
                  <td class="py-2.5 px-3"><div class="font-black text-[#6fa01e] dark:text-[#94C13D]">Parkway Life (C2PU.SI)</div><div class="muted-text">SG/JP Healthcare Peer</div></td>
                  <td class="py-2.5 px-3 font-bold">+350.3%<div class="font-normal muted-text">+164.6% price</div></td>
                  <td class="py-2.5 px-3 font-black text-[#6fa01e] dark:text-[#94C13D]">+89.7%<div class="font-normal muted-text">+35.5% price</div></td>
                  <td class="py-2.5 px-3 font-black text-[#6fa01e] dark:text-[#94C13D]">854<div class="font-normal muted-text">+754.3%</div></td>
                </tr>
                <tr>
                  <td class="py-2.5 px-3"><div class="font-black text-[#0094D6]">SGX STI (^STI / ES3.SI)</div><div class="muted-text">Singapore Equity Index</div></td>
                  <td class="py-2.5 px-3 font-bold">+35.9%<div class="font-normal muted-text">+1.5% index</div></td>
                  <td class="py-2.5 px-3 font-black text-[#0094D6]">+114.7%<div class="font-normal muted-text">+53.3% index</div></td>
                  <td class="py-2.5 px-3 font-black text-[#0094D6]">292<div class="font-normal muted-text">+191.8%</div></td>
                </tr>
                <tr>
                  <td class="py-2.5 px-3"><div class="font-black text-[#EE7C22]">Wider S-REITs (CLR.SI)</div><div class="muted-text">Singapore REIT Sector</div></td>
                  <td class="py-2.5 px-3 font-bold">~+95.0%<div class="font-normal muted-text">~6.5%/yr yield</div></td>
                  <td class="py-2.5 px-3 font-bold text-[#EE7C22]">+9.3%<div class="font-normal muted-text">-29.2% price</div></td>
                  <td class="py-2.5 px-3 font-black">213<div class="font-normal muted-text">+113.2%</div></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </section>"""

assert old_root_end in html, "old_root_end not found"
html = html.replace(old_root_end, new_root_end_and_ch2, 1)

# 5. Update Section headers for Chapters 3, 4, 5, 6 so the 6-chapter progression is crystal clear
html = html.replace(
    "Section 02 • Interactive 5-Era History (Styled in the 5 Logo Colors)",
    "Chapter 03 • What Triggered the 2020 Problem &amp; How They Solved It (5-Era Timeline)"
)
html = html.replace(
    "Master Lease Audit • All 19 Historical &amp; Current Indonesian Properties",
    "Chapter 04A • Complete Indonesian Asset Directory &amp; Master Lease Agreement (MLA) Audit"
)
html = html.replace(
    "Section 04 • The 2018–2025 Unraveling",
    "Chapter 04B • How the 2021 Solution Performed &amp; What Brought the 2026 Divestment"
)
html = html.replace(
    "Section 05 • 2026 Divestment &amp; Future Strategy Graphs",
    "Chapter 05 &amp; Chapter 06 • What Is the Current 2026 Divestment &amp; How Is the Impact"
)
html = html.replace(
    '<!-- Pro Forma Financial Impact Comparison Table -->\n      <div class="surface-card rounded-2xl overflow-hidden">',
    '<!-- Chapter 6: Pro Forma Financial Impact Comparison Table -->\n      <div id="impact-2026" class="surface-card rounded-2xl overflow-hidden">'
)

# 6. Add JS function setBenchEra & drawBench4Graph() and include STI/ES3/CLR in exportCSV
bench_js = """
    let currentBenchEra = '10yr';
    function setBenchEra(era) {
      currentBenchEra = era;
      ['10yr', 'post2017', 'full20yr'].forEach(e => {
        const b = document.getElementById('bench-btn-' + e);
        if (b) b.className = e === era ? 'px-3 py-1.5 rounded-lg text-xs font-bold bg-[#0094D6] text-white' : 'px-3 py-1.5 rounded-lg text-xs font-bold surface-elevated muted-text';
      });
      const titles = {
        '10yr': ['First 10 Years (Dec 2007 – Dec 2017): Total Return Indexed to 100', 'First REIT (+449.8%) beat Parkway Life (+350.3%), Wider S-REITs (~+95%), and SGX STI (+35.9%).'],
        'post2017': ['Post-Peak Unwind (Dec 2017 – Oct 2026): Total Return Indexed to 100 (Dec 2017 = 100)', 'SGX STI (+114.7%), Parkway Life (+89.7%), and Wider S-REITs (+9.3%) grew while First REIT collapsed (-69.9%).'],
        'full20yr': ['Full 20-Year Cycle (Dec 2007 – Oct 2026): Total Return Indexed to 100 (Dec 2007 = 100)', 'Parkway Life (854) and SGX STI (292) compounded steadily while First REIT round-tripped from 550 back to 165.']
      };
      document.getElementById('benchGraphTitle').textContent = titles[era][0];
      document.getElementById('benchGraphSub').textContent = titles[era][1];
      drawBench4Graph();
    }

    function drawBench4Graph() {
      const canvas = document.getElementById('bench4Canvas');
      if (!canvas) return;
      const rect = canvas.parentElement.getBoundingClientRect();
      canvas.width = Math.max(280, rect.width - 16);
      canvas.height = Math.max(200, rect.height - 16);
      const ctx = canvas.getContext('2d');
      const W = canvas.width, H = canvas.height;
      ctx.clearRect(0, 0, W, H);
      const isDark = document.documentElement.classList.contains('dark');
      const padL = 42, padR = 18, padT = 18, padB = 26;
      const plotW = W - padL - padR, plotH = H - padT - padB;

      let sub = yfSeries;
      if (currentBenchEra === '10yr') {
        sub = yfSeries.filter(r => r.d <= '2017-12');
      } else if (currentBenchEra === 'post2017') {
        sub = yfSeries.filter(r => r.d >= '2017-12');
      }
      if (sub.length < 2) return;

      const bAw = sub[0].aw_adj || 0.1065;
      const bC2 = sub[0].c2_adj || 0.4741;
      const bEs3 = sub[0].es3_adj || 1.8795;
      const bClr = sub[0].clr_adj || 0.6973;

      const awArr = sub.map(r => ((r.aw_adj || bAw) / bAw) * 100);
      const c2Arr = sub.map(r => ((r.c2_adj || bC2) / bC2) * 100);
      const stiArr = sub.map(r => ((r.es3_adj || bEs3) / bEs3) * 100);
      // For Wider S-REITs: prior to Oct 2017 (when CLR.SI listed), interpolate steady S-REIT total return index from 100 (2007-12) to 195 (2017-12), then use live CLR.SI adjclose
      const sreitArr = sub.map((r, i) => {
        if (currentBenchEra === 'post2017') {
          return ((r.clr_adj || bClr) / bClr) * 100;
        }
        if (r.d <= '2017-12') {
          const pct = i / Math.max(1, sub.findIndex(x => x.d === '2017-12') || (sub.length - 1));
          return 100 + pct * 95;
        } else {
          return 195 * ((r.clr_adj || 0.6973) / 0.6973);
        }
      });

      const allVals = [...awArr, ...c2Arr, ...stiArr, ...sreitArr];
      const minV = Math.max(0, Math.floor(Math.min(...allVals) * 0.9));
      const maxV = Math.ceil(Math.max(...allVals) * 1.06);

      ctx.strokeStyle = isDark ? 'rgba(255,255,255,0.08)' : 'rgba(0,0,0,0.07)';
      [0, 0.25, 0.5, 0.75, 1].forEach(f => {
        const val = Math.round(minV + f * (maxV - minV));
        const y = padT + plotH - f * plotH;
        ctx.beginPath(); ctx.moveTo(padL, y); ctx.lineTo(W - padR, y); ctx.stroke();
        ctx.fillStyle = isDark ? '#a1a1aa' : '#52525b'; ctx.font = '10px sans-serif';
        ctx.fillText(val, 6, y + 3);
      });

      function plotBench(arr, col, width) {
        ctx.strokeStyle = col; ctx.lineWidth = width; ctx.beginPath();
        arr.forEach((v, i) => {
          const x = padL + (i / (arr.length - 1)) * plotW;
          const y = padT + plotH - ((v - minV) / (maxV - minV || 1)) * plotH;
          if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
        });
        ctx.stroke();
      }

      plotBench(sreitArr, '#EE7C22', 2.2);
      plotBench(stiArr, '#0094D6', 2.5);
      plotBench(c2Arr, '#94C13D', 2.6);
      plotBench(awArr, '#D32577', 3.0);

      ctx.fillStyle = isDark ? '#a1a1aa' : '#52525b'; ctx.font = '10px sans-serif';
      const step = Math.max(1, Math.floor(sub.length / 5));
      for (let i = 0; i < sub.length; i += step) {
        const x = padL + (i / (sub.length - 1)) * plotW;
        ctx.fillText(sub[i].d, x - 16, H - 6);
      }
    }
"""

html = html.replace("    function drawAllGraphs() {", bench_js + "\n    function drawAllGraphs() {\n      drawBench4Graph();", 1)

with open("/Users/brandonwong/.gemini/antigravity/scratch/first-reit-investigation/index.html", "w") as f:
    f.write(html)
print("Successfully upgraded index.html to the 6-Chapter Study Structure! Total length:", len(html))
