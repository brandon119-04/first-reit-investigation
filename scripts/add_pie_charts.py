with open("/Users/brandonwong/.gemini/antigravity/scratch/first-reit-investigation/index.html") as f:
    html = f.read()

target_anchor = """      <div id="eraDetailPanel" class="surface-card rounded-2xl p-6 sm:p-8"></div>
    </div>
  </section>"""

pie_section = """      <div id="eraDetailPanel" class="surface-card rounded-2xl p-6 sm:p-8"></div>

      <!-- Chapter 3B: Lippo Karawaci Stake Evolution Pie Charts (2006 IPO to 2026 Today) -->
      <div id="karawaci-stake" class="mt-8 surface-card rounded-2xl p-6 sm:p-8 border-t-4 border-t-[#D32577]">
        <div class="flex flex-wrap items-center justify-between gap-4 mb-6">
          <div>
            <span class="text-xs font-bold uppercase tracking-widest text-[#D32577]">Ownership Evolution • 2006 IPO to October 2026</span>
            <h3 class="text-xl sm:text-2xl font-black mt-1">Lippo Karawaci (LPKR) Equity Stake in First REIT Over Time</h3>
            <p class="muted-text mt-1 text-sm max-w-3xl">
              Track how founding sponsor <strong>PT Lippo Karawaci Tbk (via Bridgewater International Ltd)</strong> went from absolute control (holding up to <strong>35% deemed interest</strong> &amp; 100% of the Manager) to halving its stake in October 2018, suffering passive dilution to <strong>5.18% in the 2021 rights issue</strong>, and falling <strong>below 4%</strong> as OUE consolidated <strong>45.60% control</strong> <a href="#ref-3" class="cite-badge">[3]</a><a href="#ref-5" class="cite-badge">[5]</a>.
            </p>
          </div>
          <div class="flex flex-wrap gap-1.5">
            <button onclick="setStakePieEra('2006')" id="pie-btn-2006" class="px-2.5 py-1.5 rounded-lg text-xs font-bold surface-elevated muted-text">2006 IPO</button>
            <button onclick="setStakePieEra('2010')" id="pie-btn-2010" class="px-2.5 py-1.5 rounded-lg text-xs font-bold surface-elevated muted-text">2010 Peak</button>
            <button onclick="setStakePieEra('2017')" id="pie-btn-2017" class="px-2.5 py-1.5 rounded-lg text-xs font-bold surface-elevated muted-text">2017 Pre-OUE</button>
            <button onclick="setStakePieEra('2018')" id="pie-btn-2018" class="px-2.5 py-1.5 rounded-lg text-xs font-bold surface-elevated muted-text">Oct 2018 Sale</button>
            <button onclick="setStakePieEra('2021')" id="pie-btn-2021" class="px-2.5 py-1.5 rounded-lg text-xs font-bold surface-elevated muted-text">Feb 2021 Rights</button>
            <button onclick="setStakePieEra('2026')" id="pie-btn-2026" class="px-2.5 py-1.5 rounded-lg text-xs font-bold bg-[#D32577] text-white">2026 Today</button>
          </div>
        </div>

        <!-- Main Interactive Donut Pie Chart + Narrative Panel -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-center mb-8 surface-elevated rounded-2xl p-5 sm:p-6">
          <div class="lg:col-span-5 flex flex-col items-center justify-center">
            <div class="relative w-56 h-56 sm:w-64 sm:h-64">
              <canvas id="stakePieCanvas" class="w-full h-full"></canvas>
              <div class="absolute inset-0 flex flex-col items-center justify-center pointer-events-none text-center">
                <span class="text-xs font-bold uppercase text-[#D32577]" id="pieCenterLabel">LPKR Stake</span>
                <span class="text-2xl sm:text-3xl font-black" id="pieCenterPct">&lt; 3.98%</span>
                <span class="text-[11px] muted-text font-semibold" id="pieCenterYear">Oct 2026</span>
              </div>
            </div>
            <div class="flex flex-wrap justify-center gap-3 text-xs font-bold mt-4">
              <span class="inline-flex items-center gap-1.5"><span class="w-3 h-3 rounded-sm bg-[#D32577] inline-block"></span>Lippo Karawaci (LPKR)</span>
              <span class="inline-flex items-center gap-1.5"><span class="w-3 h-3 rounded-sm bg-[#0094D6] inline-block"></span>OUE Group &amp; OUELH</span>
              <span class="inline-flex items-center gap-1.5"><span class="w-3 h-3 rounded-sm bg-[#FECD07] inline-block"></span>Public &amp; Other Unitholders</span>
            </div>
          </div>

          <div class="lg:col-span-7 space-y-3.5" id="pieNarrativeBox"></div>
        </div>

        <!-- 4 Comparative Multi-Era Pie Cards at Key Turning Points -->
        <div class="border-t border-[var(--border-color)] pt-6">
          <div class="text-xs font-bold uppercase tracking-widest text-[#0094D6] mb-3">At-A-Glance • The 4 Inflection Points of Sponsor Ownership</div>
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3.5">
            <!-- Mini Pie 1: 2006 IPO -->
            <div class="surface-card rounded-xl p-4 flex flex-col items-center text-center border-t-4 border-t-[#0094D6]">
              <span class="text-xs font-bold uppercase text-[#0094D6]">1. Dec 2006 IPO</span>
              <div class="w-28 h-28 my-2 relative">
                <canvas id="miniPie1" class="w-full h-full"></canvas>
              </div>
              <div class="font-bold text-xs mt-1 text-[#D32577]">LPKR: 21.8% • OUE: 0.0%</div>
              <p class="text-xs muted-text mt-1">LPKR founds REIT; owns 100% of Manager &amp; 59.4M units <a href="#ref-1" class="cite-badge">[1]</a>.</p>
            </div>

            <!-- Mini Pie 2: Oct 2018 Sale -->
            <div class="surface-card rounded-xl p-4 flex flex-col items-center text-center border-t-4 border-t-[#EE7C22]">
              <span class="text-xs font-bold uppercase text-[#EE7C22]">2. Oct 2018 OUE Sale</span>
              <div class="w-28 h-28 my-2 relative">
                <canvas id="miniPie2" class="w-full h-full"></canvas>
              </div>
              <div class="font-bold text-xs mt-1 text-[#D32577]">LPKR: 10.6% • OUE: 18.0%</div>
              <p class="text-xs muted-text mt-1">LPKR sells Manager + 10.63% units to OUE for S$111.2M cash <a href="#ref-3" class="cite-badge">[3]</a>.</p>
            </div>

            <!-- Mini Pie 3: Feb 2021 Rights -->
            <div class="surface-card rounded-xl p-4 flex flex-col items-center text-center border-t-4 border-t-[#D32577]">
              <span class="text-xs font-bold uppercase text-[#D32577]">3. Feb 2021 Rights</span>
              <div class="w-28 h-28 my-2 relative">
                <canvas id="miniPie3" class="w-full h-full"></canvas>
              </div>
              <div class="font-bold text-xs mt-1 text-[#D32577]">LPKR: 5.2% • OUE: 33.2%</div>
              <p class="text-xs muted-text mt-1">LPKR skips 20¢ rights issue; stake diluted by half from 10.4% to 5.2% <a href="#ref-5" class="cite-badge">[5]</a>.</p>
            </div>

            <!-- Mini Pie 4: 2026 Today -->
            <div class="surface-card rounded-xl p-4 flex flex-col items-center text-center border-t-4 border-t-[#94C13D]">
              <span class="text-xs font-bold uppercase text-[#6fa01e] dark:text-[#94C13D]">4. 2026 Present</span>
              <div class="w-28 h-28 my-2 relative">
                <canvas id="miniPie4" class="w-full h-full"></canvas>
              </div>
              <div class="font-bold text-xs mt-1 text-[#0094D6]">OUE: 45.6% • LPKR: &lt; 4.0%</div>
              <p class="text-xs muted-text mt-1">OUE controls 45.6%; LPKR drops below 5% and completely exits leases in 2026 <a href="#ref-10" class="cite-badge">[10]</a>.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>"""

assert target_anchor in html, "target_anchor not found"
html = html.replace(target_anchor, pie_section, 1)

# Add JavaScript for Stake Pie Charts
js_stake_code = """
    const STAKE_PIE_DATA = {
      '2006': {
        year: 'Dec 2006 (IPO)',
        totalUnits: '273.0M units',
        slices: [
          { label: 'Lippo Karawaci (Bridgewater)', pct: 21.8, color: '#D32577', units: '59.4M' },
          { label: 'OUE Group', pct: 0.0, color: '#0094D6', units: '0.0M' },
          { label: 'Public & Institutional', pct: 78.2, color: '#FECD07', units: '213.6M' }
        ],
        center: { label: 'LPKR Stake', pct: '21.8%', year: 'Dec 2006' },
        manager: '100% Owned by PT Lippo Karawaci Tbk (Bowsprit Capital Corporation Limited)',
        summary: 'At IPO, Lippo Karawaci established First REIT with 4 Indonesian properties, holding a 21.8% direct/deemed stake and total control of the REIT Manager, creating the initial 15-year SGD master lease framework.'
      },
      '2010': {
        year: 'Dec 2010 (Peak Sponsor Stake)',
        totalUnits: '622.0M units',
        slices: [
          { label: 'Lippo Karawaci (Deemed)', pct: 33.0, color: '#D32577', units: '205.3M' },
          { label: 'OUE Group', pct: 0.0, color: '#0094D6', units: '0.0M' },
          { label: 'Public & Institutional', pct: 67.0, color: '#FECD07', units: '416.7M' }
        ],
        center: { label: 'LPKR Peak', pct: '33.0%', year: 'Dec 2010' },
        manager: '100% Owned by PT Lippo Karawaci Tbk (Bowsprit Capital)',
        summary: 'To fund the acquisition of MRCCC and Siloam Hospitals Lippo Cikarang, First REIT executed a major rights issue. LPKR took consideration units, pushing its deemed equity stake to a peak of ~33.0%–35.0%.'
      },
      '2017': {
        year: 'Dec 2017 (Pre-OUE Acquisition Peak)',
        totalUnits: '779.95M units',
        slices: [
          { label: 'Lippo Karawaci (Bridgewater)', pct: 21.44, color: '#D32577', units: '167.19M' },
          { label: 'OUE Group', pct: 0.0, color: '#0094D6', units: '0.0M' },
          { label: 'Public & Institutional', pct: 78.56, color: '#FECD07', units: '612.76M' }
        ],
        center: { label: 'LPKR Stake', pct: '21.4%', year: 'Dec 2017' },
        manager: '100% Owned by PT Lippo Karawaci Tbk (Bowsprit Capital)',
        summary: 'Bridgewater held exactly 167,187,367 units (21.44%). Portfolio had expanded to 19 Indonesian assets, with DPU reaching 8.57¢, supported by LPKR corporate guarantees.'
      },
      '2018': {
        year: 'Oct 2018 (The OUE Manager Buyout)',
        totalUnits: '788.48M units',
        slices: [
          { label: 'Lippo Karawaci (Bridgewater)', pct: 10.60, color: '#D32577', units: '83.59M' },
          { label: 'OUE Group & OUELH', pct: 18.00, color: '#0094D6', units: '141.9M' },
          { label: 'Public & Institutional', pct: 71.40, color: '#FECD07', units: '562.99M' }
        ],
        center: { label: 'LPKR Halved', pct: '10.6%', year: 'Oct 2018' },
        manager: 'Transferred 100% to OUE Limited (60%) & OUE Lippo Healthcare (40%)',
        summary: 'Facing cash burn in Indonesia, LPKR sold REIT Manager Bowsprit Capital to OUE/OUELH for S$99M, and sold 83,593,683 units (10.63%) to OUELH for S$111.2M cash. LPKR was cut in half and lost control of the Manager.'
      },
      '2021': {
        year: 'Feb 2021 (Post-Rights Dilution)',
        totalUnits: '1,613.3M units',
        slices: [
          { label: 'Lippo Karawaci (Bridgewater)', pct: 5.18, color: '#D32577', units: '83.59M' },
          { label: 'OUE Group & OUELH', pct: 33.20, color: '#0094D6', units: '535.6M' },
          { label: 'Public & Institutional', pct: 61.62, color: '#FECD07', units: '994.1M' }
        ],
        center: { label: 'LPKR Diluted', pct: '5.18%', year: 'Feb 2021' },
        manager: '60% OUE Limited / 40% OUE Healthcare Limited',
        summary: 'In the S$0.20 emergency rights issue, OUE backstopped the offering while LPKR refused to inject fresh capital. LPKR’s remaining 83.59M units were diluted from 10.4% down to 5.18%.'
      },
      '2026': {
        year: 'Oct 2026 (Present Day & Complete Exit)',
        totalUnits: '2,098.0M units',
        slices: [
          { label: 'Lippo Karawaci (Residual)', pct: 3.98, color: '#D32577', units: '< 83.59M' },
          { label: 'OUE Group & OUELH', pct: 45.60, color: '#0094D6', units: '956.7M' },
          { label: 'Public & Institutional', pct: 50.42, color: '#FECD07', units: '1,057.7M' }
        ],
        center: { label: 'LPKR Residual', pct: '< 4.0%', year: 'Oct 2026' },
        manager: '60% OUE Limited / 40% OUE Healthcare Limited',
        summary: 'Following the 2022 Japan acquisition, LPKR fell below the 5% substantial unitholder threshold (<4.0%), while OUE expanded to 45.60%. The 2026 S$766.3M divestment completely severs LPKR master leases.'
      }
    };

    let currentStakeEra = '2026';

    function setStakePieEra(era) {
      currentStakeEra = era;
      ['2006', '2010', '2017', '2018', '2021', '2026'].forEach(e => {
        const b = document.getElementById('pie-btn-' + e);
        if (b) b.className = e === era ? 'px-2.5 py-1.5 rounded-lg text-xs font-bold bg-[#D32577] text-white' : 'px-2.5 py-1.5 rounded-lg text-xs font-bold surface-elevated muted-text';
      });
      drawMainStakePie();
      updateStakeNarrative();
    }

    function drawDonut(canvasId, slices, cutoutRatio = 0.58) {
      const canvas = document.getElementById(canvasId);
      if (!canvas) return;
      const rect = canvas.parentElement.getBoundingClientRect();
      canvas.width = Math.max(100, rect.width);
      canvas.height = Math.max(100, rect.height);
      const ctx = canvas.getContext('2d');
      const W = canvas.width, H = canvas.height;
      ctx.clearRect(0, 0, W, H);
      const cx = W / 2, cy = H / 2;
      const radius = Math.min(cx, cy) - 4;
      let startAngle = -Math.PI / 2;

      slices.forEach(s => {
        if (s.pct <= 0) return;
        const sliceAngle = (s.pct / 100) * 2 * Math.PI;
        ctx.beginPath();
        ctx.arc(cx, cy, radius, startAngle, startAngle + sliceAngle);
        ctx.arc(cx, cy, radius * cutoutRatio, startAngle + sliceAngle, startAngle, true);
        ctx.closePath();
        ctx.fillStyle = s.color;
        ctx.fill();
        startAngle += sliceAngle;
      });
    }

    function drawMainStakePie() {
      const data = STAKE_PIE_DATA[currentStakeEra];
      if (!data) return;
      drawDonut('stakePieCanvas', data.slices, 0.65);
      document.getElementById('pieCenterLabel').textContent = data.center.label;
      document.getElementById('pieCenterPct').textContent = data.center.pct;
      document.getElementById('pieCenterYear').textContent = data.center.year;
    }

    function updateStakeNarrative() {
      const d = STAKE_PIE_DATA[currentStakeEra];
      if (!d) return;
      document.getElementById('pieNarrativeBox').innerHTML = `
        <div class="p-4 rounded-xl surface-card border-l-4 border-l-[#D32577]">
          <div class="flex flex-wrap items-center justify-between gap-1 mb-1">
            <h4 class="font-black text-base">${d.year}</h4>
            <span class="text-xs font-bold px-2 py-0.5 rounded bg-[#0094D6]/15 text-[#0094D6]">Total Units: ${d.totalUnits}</span>
          </div>
          <p class="text-xs muted-text leading-relaxed">${d.summary}</p>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5 text-xs">
          ${d.slices.map(s => `
            <div class="p-3 rounded-xl surface-card" style="border-top: 3px solid ${s.color}">
              <div class="muted-text font-bold truncate">${s.label}</div>
              <div class="text-lg font-black mt-0.5" style="color:${s.color === '#FECD07' ? '#d97706' : s.color}">${s.pct.toFixed(1)}%</div>
              <div class="muted-text">${s.units}</div>
            </div>
          `).join('')}
        </div>
        <div class="p-3 rounded-xl surface-card border-l-4 border-l-[#0094D6] text-xs">
          <strong class="text-[#0094D6]">REIT Manager Ownership:</strong> <span class="muted-text">${d.manager}</span>
        </div>
      `;
    }

    function drawAllMiniPies() {
      drawDonut('miniPie1', STAKE_PIE_DATA['2006'].slices, 0.55);
      drawDonut('miniPie2', STAKE_PIE_DATA['2018'].slices, 0.55);
      drawDonut('miniPie3', STAKE_PIE_DATA['2021'].slices, 0.55);
      drawDonut('miniPie4', STAKE_PIE_DATA['2026'].slices, 0.55);
    }
"""

html = html.replace("    function drawAllGraphs() {", js_stake_code + "\n    function drawAllGraphs() {\n      drawMainStakePie();\n      drawAllMiniPies();", 1)
html = html.replace("initYfScrubber();", "initYfScrubber();\n    setStakePieEra('2026');", 1)

with open("/Users/brandonwong/.gemini/antigravity/scratch/first-reit-investigation/index.html", "w") as f:
    f.write(html)
print("Successfully added interactive Lippo Karawaci Stake Pie Charts to index.html!")
