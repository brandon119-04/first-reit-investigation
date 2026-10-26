# First REIT (SGX: AW9U) • 20-Year Investigative Case Study (2006–2026)

> **An empirical financial analysis and interactive web platform tracking Singapore's first healthcare REIT from its December 11, 2006 IPO through the 2021 restructuring crisis and the historic 2026 S$766.3M complete Indonesian portfolio divestment.**

🌐 **Live Interactive Website:** [https://brandon119-04.github.io/first-reit-investigation/](https://brandon119-04.github.io/first-reit-investigation/)

---

## 📌 Executive Summary

First REIT listed on the SGX Mainboard in 2006 with an attractive 8.8% annualized distribution yield, backed by 15-year triple-net Master Lease Agreements (MLAs) pegged to Singapore Dollars with 2% annual step-ups. 

While delivering 11 unbroken years of dividend growth (peaking at **8.57¢ DPU** in FY2017), the structure hid a fatal fundamental flaw: **a massive unhedged currency mismatch**. Hospitals collected revenue in Indonesian Rupiah (IDR) while owing contractual lease payments in Singapore Dollars (SGD). As the Rupiah steadily depreciated from ~6,000 to over 14,000 IDR/SGD, the master lease model became insolvent, requiring aggressive subsidies by sponsor PT Lippo Karawaci Tbk (LPKR).

When COVID-19 hit in 2020 and LPKR withdrew its support, First REIT faced a debt cliff on March 1, 2021, forcing an emergency **98-for-100 rights issue at S$0.20** and lease restructuring to IDR. The saga culminated in the **S$766.3M divestment** to Siloam in 2025–2026, dropping gearing to 16.7% and permanently exiting Indonesian risk.

---

## 🚀 Key Interactive Features

1. **Interactive 20-Year Master Timeline (2006–2026):**
   - 10 pivotal milestones filterable across *Master Lease & Debt*, *Sponsor & Governance*, and *Asset Deals*.
   - Embedded journalistic coverage cards from **The Business Times**, **The Edge Singapore**, **Reuters**, and **Singapore Business Review**.

2. **Lippo Karawaci Stake Evolution Visualizer:**
   - Interactive Donut/Pie charts tracking LPKR's deemed unitholding from **21.8% at IPO** (and 33.0% peak) down to **10.6% in 2018**, **5.18% in the 2021 rights dilution**, and below **4%** as OUE consolidated 45.60% majority control.

3. **High-Contrast Financial Grid & Charting Engine:**
   - 6 responsive canvas charts with horizontal/vertical grid lines, tick labels, and Base 100 reference lines:
     - **Graph 01:** Dual-Axis Interactive Yahoo Finance Scrubber.
     - **Graph 02:** FX Depreciation Index (SGD/IDR +142% & SGD/JPY +44%).
     - **Graph 03:** Total Return Divergence (Parkway Life REIT vs First REIT vs Lippo Karawaci).
     - **Graph 04:** 4-Way Peer Benchmark (AW9U vs C2PU vs STI vs S-REITs).
     - **Graph 05:** Annual DPU vs Total Issued Units (104% Dilution Shock).
     - **Graph 06:** 77-Quarter Continuous Cash Distribution History.

4. **Asset Visual Showcase & Interactive Casefiles:**
   - Real architectural photography of the 30-storey **MRCCC Siloam Hospitals Semanggi** (Jakarta CBD).
   - Architectural vector elevations for **Siloam Hospitals Lippo Village**, **Siloam Kebon Jeruk**, **Siloam Bali**, **Japan Eldercare Residences**, and **Lippo Plaza Kupang**.
   - Interactive modal popups with land title info, bed count, GFA, original acquisition cost, and 2026 divestment outcome.

5. **1-Click CSV Data Exports:**
   - Export master dataset, monthly historical prices, 77 dividend distributions, or the 19-property asset audit with one click.

---

## 📊 Datasets Included

| File | Description | Rows / Coverage |
| :--- | :--- | :--- |
| [`first_reit_yahoo_finance_data.csv`](first_reit_yahoo_finance_data.csv) | Monthly close, adjusted close, total return indexes, and FX rates for 11 tickers | 227 Monthly Rows (2006–2026) |
| [`first_reit_indonesian_assets_master_leases.csv`](first_reit_indonesian_assets_master_leases.csv) | Full audit of all 19 Indonesian properties, lease terms, and 2026 divestment status | 19 Properties |
| [`first_reit_dividends_dpu.csv`](first_reit_dividends_dpu.csv) | Complete chronological cash distribution history | 77 Quarters |
| [`yahoo_data.json`](yahoo_data.json) | Raw JSON payload from Yahoo Finance v8 chart API | 11 Tickers |

---

## 💻 How to Run Locally

You don't need any build tools or web servers. Simply double-click `index.html` in your file explorer, or run:

```bash
# Clone the repository
git clone https://github.com/brandon119-04/first-reit-investigation.git
cd first-reit-investigation

# Open in default browser (macOS)
open index.html

# Or serve via a simple local Python server:
python3 -m http.server 8080
```

---

## 📜 Citations & Sources

1. SGX First REIT IPO Prospectus (Dec 2006)
2. SGX Circular on Proposed Acquisition of MRCCC & Siloam Cikarang (Dec 2010)
3. SGX Joint Announcement: OUE & OUELH Acquisition of Bowsprit Capital (Oct 2018)
4. First REIT SGX Announcement on Master Lease Restructuring (Nov 2020)
5. First REIT Renounceable Rights Issue Circular & Results (Dec 2020 – Feb 2021)
6. The Edge Singapore: *"First REIT: Anatomy of a restructuring that left unitholders with a bitter pill"* (Jan 2021)
7. SGX Circular on Proposed Acquisition of 12 Nursing Homes in Japan (Feb 2022)
8. First REIT SGX Announcement: Rental Arrears from Metropolis Propertindo Utama (Jul 2024)
9. First REIT Annual Reports (FY2007 through FY2025)
10. SGX Circular on Proposed Divestment of Indonesian Hospital Portfolio to Siloam (2025–2026)
