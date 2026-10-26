import json
from add_assets import ASSETS

assets_js = json.dumps(ASSETS, separators=(",", ":"))

with open("/Users/brandonwong/.gemini/antigravity/scratch/first-reit-investigation/index.html") as f:
    html = f.read()

# 1. Add Export 19 Assets CSV button to Yahoo Finance CSV bar
old_csv_btns = """          <button onclick="exportCSV('dividends')" class="px-3 py-1.5 rounded-lg bg-[#D32577] hover:opacity-90 text-white font-bold text-xs transition shadow-sm">
            ⬇ 77 Dividends &amp; DPU (CSV)
          </button>"""

new_csv_btns = """          <button onclick="exportCSV('dividends')" class="px-3 py-1.5 rounded-lg bg-[#D32577] hover:opacity-90 text-white font-bold text-xs transition shadow-sm">
            ⬇ 77 Dividends &amp; DPU (CSV)
          </button>
          <button onclick="exportCSV('assets')" class="px-3 py-1.5 rounded-lg bg-[#EE7C22] hover:opacity-90 text-white font-bold text-xs transition shadow-sm">
            ⬇ 19 Indo Assets &amp; MLAs (CSV)
          </button>"""

assert old_csv_btns in html, "old_csv_btns not found"
html = html.replace(old_csv_btns, new_csv_btns, 1)

# 2. Insert Section 2B: Complete Indonesian Asset & Master Lease Directory right after #timeline section
target_section_anchor = """      <div id="eraDetailPanel" class="surface-card rounded-2xl p-6 sm:p-8"></div>
    </div>
  </section>"""

indo_assets_section = """      <div id="eraDetailPanel" class="surface-card rounded-2xl p-6 sm:p-8"></div>
    </div>
  </section>

  <!-- Section 2B: Complete Indonesian Portfolio & Master Lease Directory (All 19 Assets) -->
  <section id="indo-assets" class="py-14 border-b border-[var(--border-color)]">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-wrap items-center justify-between gap-4 mb-6">
        <div>
          <span class="text-xs font-bold uppercase tracking-widest text-[#EE7C22]">Master Lease Audit • All 19 Historical &amp; Current Indonesian Properties</span>
          <h2 class="text-2xl sm:text-3xl font-black mt-1">Indonesian Assets &amp; Master Lease Agreement (MLA) Impact</h2>
          <p class="muted-text mt-1 text-sm max-w-3xl">
            Every Indonesian asset owned by First REIT since its December 2006 IPO was governed by a single-tenant Master Lease Agreement (MLA). Filter below to see which properties were hit by the <strong>Nov 2020 LPKR SGD→IDR Reset (11 hospitals)</strong>, the <strong>2021 MPU Reset &amp; 2024–2025 Rental Arrears (3 hospitals)</strong>, the <strong>Non-Core Mall/Hotel Leases (3 assets)</strong>, and the <strong>2026 Two-Stage Exit</strong> <a href="#ref-4" class="cite-badge">[4]</a><a href="#ref-8" class="cite-badge">[8]</a><a href="#ref-10" class="cite-badge">[10]</a>.
          </p>
        </div>
        <button onclick="exportCSV('assets')" class="px-3.5 py-2 rounded-xl bg-[#EE7C22] hover:opacity-90 text-white font-black text-xs shadow-sm transition">
          ⬇ Export 19 Indo Assets &amp; MLAs (CSV)
        </button>
      </div>

      <!-- 4 Summary Cards for the 4 Master Lease Buckets -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3.5 mb-6 text-xs">
        <div class="surface-card rounded-xl p-4 border-t-4 border-t-[#0094D6]">
          <div class="font-black text-sm text-[#0094D6]">11 LPKR / Siloam Hospital MLAs</div>
          <p class="muted-text mt-1">Originally SGD-pegged to LPKR. <strong>All 11 were restructured on 1 Jan 2021 into IDR leases</strong> (extended to Dec 2035, 4.5% p.a. escalation or 8% GOR) <a href="#ref-4" class="cite-badge">[4]</a>.</p>
        </div>
        <div class="surface-card rounded-xl p-4 border-t-4 border-t-[#D32577]">
          <div class="font-black text-sm text-[#D32577]">3 MPU Hospital MLAs (Double Hit)</div>
          <p class="muted-text mt-1">Purwakarta, Sriwijaya &amp; Kupang. <strong>Restructured from SGD to IDR in 2021</strong>, then hit by <strong>MPU credit stress &amp; arrears in 2024–2025</strong> <a href="#ref-8" class="cite-badge">[8]</a>.</p>
        </div>
        <div class="surface-card rounded-xl p-4 border-t-4 border-t-[#EE7C22]">
          <div class="font-black text-sm text-[#EE7C22]">3 Non-Core Mall &amp; Hotel MLAs</div>
          <p class="muted-text mt-1">Lippo Plaza Kupang, Lippo Plaza Buton &amp; Hotel Aryaduta Manado. Excluded from the 2020 hospital reset; <strong>MPU owed ~S$6.9M–7.9M arrears</strong>. Divested in 2026 Stage 1 for S$82.4M <a href="#ref-10" class="cite-badge">[10]</a>.</p>
        </div>
        <div class="surface-card rounded-xl p-4 border-t-4 border-t-[#FECD07]">
          <div class="font-black text-sm text-[#d97706]">2 Legacy IPO Assets (Divested Earlier)</div>
          <p class="muted-text mt-1">Imperial Aryaduta Hotel &amp; Country Club (excluded from 2020 renewal) &amp; old Siloam Hospitals Surabaya (terminated S$90M dev swap) <a href="#ref-4" class="cite-badge">[4]</a>.</p>
        </div>
      </div>

      <!-- Filter Pills -->
      <div class="flex flex-wrap gap-2 mb-4">
        <button onclick="filterIndoAssets('all')" id="asset-btn-all" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-[#0094D6] text-white">All 19 Indonesian Assets</button>
        <button onclick="filterIndoAssets('lpkr11')" id="asset-btn-lpkr11" class="px-3 py-1.5 rounded-lg text-xs font-bold surface-elevated muted-text">11 LPKR Hospital MLAs (SGD→IDR Reset)</button>
        <button onclick="filterIndoAssets('mpu3')" id="asset-btn-mpu3" class="px-3 py-1.5 rounded-lg text-xs font-bold surface-elevated muted-text">3 MPU Hospital MLAs (Reset + Arrears)</button>
        <button onclick="filterIndoAssets('noncore3')" id="asset-btn-noncore3" class="px-3 py-1.5 rounded-lg text-xs font-bold surface-elevated muted-text">3 Non-Core Mall/Hotel MLAs</button>
        <button onclick="filterIndoAssets('legacy2')" id="asset-btn-legacy2" class="px-3 py-1.5 rounded-lg text-xs font-bold surface-elevated muted-text">2 Earlier Divested IPO Assets</button>
      </div>

      <!-- Interactive Table -->
      <div class="surface-card rounded-2xl overflow-hidden">
        <div class="overflow-x-auto">
          <table class="w-full text-left border-collapse text-xs">
            <thead>
              <tr class="surface-elevated border-b border-[var(--border-color)]">
                <th class="py-3 px-3 font-bold">#</th>
                <th class="py-3 px-3 font-bold">Indonesian Property &amp; City</th>
                <th class="py-3 px-3 font-bold">Acquired</th>
                <th class="py-3 px-3 font-bold">Master Lessee</th>
                <th class="py-3 px-3 font-bold">Affected Under Master Lease?</th>
                <th class="py-3 px-3 font-bold">2026 Exit / Divestment Status</th>
              </tr>
            </thead>
            <tbody id="indoAssetsTableBody" class="divide-y divide-[var(--border-color)]"></tbody>
          </table>
        </div>
      </div>
    </div>
  </section>"""

assert target_section_anchor in html, "target_section_anchor not found"
html = html.replace(target_section_anchor, indo_assets_section, 1)

# 3. Add INDO_ASSETS_19 array, filterIndoAssets(), and 'assets' branch in exportCSV()
old_js_anchor = "    function exportCSV(mode) {"
new_js_block = f"""    const INDO_ASSETS_19 = {assets_js};

    function filterIndoAssets(group) {{
      const cols = {{ all: 'bg-[#0094D6] text-white', lpkr11: 'bg-[#0094D6] text-white', mpu3: 'bg-[#D32577] text-white', noncore3: 'bg-[#EE7C22] text-white', legacy2: 'bg-[#FECD07] text-black' }};
      ['all', 'lpkr11', 'mpu3', 'noncore3', 'legacy2'].forEach(g => {{
        const btn = document.getElementById('asset-btn-' + g);
        if (btn) btn.className = g === group ? 'px-3 py-1.5 rounded-lg text-xs font-bold ' + cols[g] : 'px-3 py-1.5 rounded-lg text-xs font-bold surface-elevated muted-text';
      }});
      const rows = group === 'all' ? INDO_ASSETS_19 : INDO_ASSETS_19.filter(a => a.group === group);
      const tbody = document.getElementById('indoAssetsTableBody');
      if (!tbody) return;
      tbody.innerHTML = rows.map(a => `
        <tr class="hover:opacity-95 transition">
          <td class="py-3 px-3 font-bold">${{a.id}}</td>
          <td class="py-3 px-3">
            <div class="font-bold text-sm" style="color:${{a.color === '#FECD07' ? '#d97706' : a.color}}">${{a.name}}</div>
            <div class="muted-text">${{a.city}} • ${{a.type}}</div>
          </td>
          <td class="py-3 px-3 font-semibold whitespace-nowrap">${{a.acq}}</td>
          <td class="py-3 px-3">
            <div class="font-bold">${{a.lessee}}</div>
            <div class="muted-text">${{a.group_label}}</div>
          </td>
          <td class="py-3 px-3 max-w-md">
            <span class="inline-block px-2 py-0.5 rounded font-bold mb-1" style="background-color:${{a.color}}22; color:${{a.color === '#FECD07' ? '#d97706' : a.color}}">${{a.mla_affected}}</span>
            <div class="muted-text leading-snug">${{a.mla_details}}</div>
          </td>
          <td class="py-3 px-3 font-bold">${{a.exit_2026}}</td>
        </tr>
      `).join('');
    }}

    function exportCSV(mode) {{
      if (mode === 'assets') {{
        const filename = 'first_reit_indonesian_assets_master_leases.csv';
        const lines = ['No,Property_Name,City_Region,Acquisition_Date,Asset_Type,MLA_Group,Master_Lessee,Affected_Under_Master_Lease,Master_Lease_Impact_Details,Exit_Status_2026'];
        INDO_ASSETS_19.forEach(a => {{
          lines.push([a.id, '"' + a.name + '"', '"' + a.city + '"', '"' + a.acq + '"', '"' + a.type + '"', '"' + a.group_label + '"', '"' + a.lessee + '"', '"' + a.mla_affected + '"', '"' + a.mla_details.replace(/"/g, '""') + '"', '"' + a.exit_2026 + '"'].join(','));
        }});
        const csvContent = lines.join('\\n');
        try {{
          const blob = new Blob([csvContent], {{ type: 'text/csv;charset=utf-8;' }});
          const url = URL.createObjectURL(blob);
          const a = document.createElement('a');
          a.href = url; a.setAttribute('download', filename);
          document.body.appendChild(a); a.click(); document.body.removeChild(a);
        }} catch (e) {{}}
        if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(csvContent).catch(() => {{}});
        const toast = document.getElementById('csvExportToast');
        const rawBox = document.getElementById('csvRawBox');
        if (toast && rawBox) {{
          rawBox.value = csvContent;
          document.getElementById('csvToastTitle').textContent = '✓ Exported ' + filename + ' (19 Indonesian Properties)!';
          toast.classList.remove('hidden');
        }}
        return;
      }}"""

assert old_js_anchor in html, "old_js_anchor not found"
html = html.replace(old_js_anchor, new_js_block, 1)

# Also call filterIndoAssets('all') at startup
html = html.replace("initYfScrubber();", "initYfScrubber();\n    filterIndoAssets('all');", 1)

with open("/Users/brandonwong/.gemini/antigravity/scratch/first-reit-investigation/index.html", "w") as f:
    f.write(html)
print("Successfully updated index.html with 19 Indonesian assets & MLA table!")
