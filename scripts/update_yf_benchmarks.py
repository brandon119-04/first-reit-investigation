import urllib.request, urllib.parse, json, datetime, csv

with open("/Users/brandonwong/.gemini/antigravity/scratch/first-reit-investigation/yahoo_data.json") as f:
    raw = json.load(f)

def fetch_yf_full(symbol):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(symbol)}?range=20y&interval=1mo&includeAdjustedClose=true"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=12) as resp:
        res = json.load(resp)["chart"]["result"][0]
    meta = res["meta"]
    ts = res["timestamp"]
    q = res["indicators"]["quote"][0]
    adj = res["indicators"].get("adjclose", [{}])[0].get("adjclose", q["close"])
    series = []
    for t, c, a in zip(ts, q["close"], adj):
        if c is not None:
            dt = datetime.datetime.fromtimestamp(t, datetime.timezone.utc).strftime("%Y-%m")
            series.append({
                "date": dt,
                "close": round(c, 4),
                "adjclose": round(a if a is not None else c, 4)
            })
    return {
        "meta": {
            "symbol": meta.get("symbol", symbol),
            "currency": meta.get("currency", "SGD"),
            "regularMarketPrice": meta.get("regularMarketPrice"),
            "shortName": meta.get("shortName", symbol)
        },
        "series": series,
        "dividends": []
    }

for sym in ["^STI", "ES3.SI", "CLR.SI"]:
    print("Fetching", sym, "...")
    raw[sym] = fetch_yf_full(sym)

with open("/Users/brandonwong/.gemini/antigravity/scratch/first-reit-investigation/yahoo_data.json", "w") as f:
    json.dump(raw, f, indent=2)

aw_map = {x["date"]: x for x in raw["AW9U.SI"]["series"]}
c2_map = {x["date"]: x for x in raw["C2PU.SI"]["series"]}
sti_map = {x["date"]: x for x in raw["^STI"]["series"]}
es3_map = {x["date"]: x for x in raw["ES3.SI"]["series"]}
clr_map = {x["date"]: x for x in raw["CLR.SI"]["series"]}
lp_map = {x["date"]: x for x in raw["LPKR.JK"]["series"]}
si_map = {x["date"]: x for x in raw["SILO.JK"]["series"]}
idr_map = {x["date"]: x for x in raw["SGDIDR=X"]["series"]}
jpy_map = {x["date"]: x for x in raw["SGDJPY=X"]["series"]}

dates = sorted(list(aw_map.keys()))
aligned = []
for dt in dates:
    aligned.append({
        "d": dt,
        "aw": aw_map.get(dt, {}).get("close"),
        "aw_adj": aw_map.get(dt, {}).get("adjclose"),
        "c2": c2_map.get(dt, {}).get("close"),
        "c2_adj": c2_map.get(dt, {}).get("adjclose"),
        "sti": sti_map.get(dt, {}).get("close"),
        "es3_adj": es3_map.get(dt, {}).get("adjclose"),
        "clr_adj": clr_map.get(dt, {}).get("adjclose"),
        "lp": lp_map.get(dt, {}).get("close"),
        "si": si_map.get(dt, {}).get("close"),
        "idr": idr_map.get(dt, {}).get("close"),
        "jpy": jpy_map.get(dt, {}).get("close")
    })

payload = json.dumps({
    "fetchedAt": "2026-10-26T23:16:00+08:00",
    "meta": {k: v["meta"] for k, v in raw.items()},
    "series": aligned
}, separators=(",", ":"))

with open("/Users/brandonwong/.gemini/antigravity/scratch/first-reit-investigation/yahoo_payload.js", "w") as f:
    f.write(f"window.YAHOO_FINANCE_DATA = {payload};\n")

# Also update first_reit_yahoo_finance_data.csv
base_aw = aligned[0]["aw_adj"]
base_c2 = aligned[0]["c2_adj"]
base_sti = aligned[0]["sti"]
with open("/Users/brandonwong/.gemini/antigravity/scratch/first-reit-investigation/first_reit_yahoo_finance_data.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Date","AW9U_Close_SGD","AW9U_AdjClose_SGD","AW9U_TotalReturn_Idx","C2PU_Close_SGD","C2PU_AdjClose_SGD","C2PU_TotalReturn_Idx","STI_Index","ES3_STI_ETF_AdjClose","CLR_SREIT_ETF_AdjClose","LPKR_Close_IDR","SILO_Close_IDR","SGDIDR_Rate","SGDJPY_Rate"])
    for r in aligned:
        w.writerow([
            r["d"], r["aw"] or "", r["aw_adj"] or "",
            round((r["aw_adj"]/base_aw)*100, 2) if r["aw_adj"] else "",
            r["c2"] or "", r["c2_adj"] or "",
            round((r["c2_adj"]/base_c2)*100, 2) if r["c2_adj"] else "",
            r["sti"] or "", r["es3_adj"] or "", r["clr_adj"] or "",
            r["lp"] or "", r["si"] or "", r["idr"] or "", r["jpy"] or ""
        ])

# Print 45 sampled bars for inline HTML fallback
sampled = []
for i, r in enumerate(aligned):
    if i == 0 or i == len(aligned) - 1 or r["d"].endswith("-06") or r["d"].endswith("-12") or r["d"] in ["2013-05","2015-05","2018-09","2021-02","2026-04","2026-09"]:
        sampled.append(r)
with open("/Users/brandonwong/.gemini/antigravity/scratch/first-reit-investigation/sampled_45.json", "w") as f:
    json.dump(sampled, f, separators=(",", ":"))
print("Updated yahoo_data.json, yahoo_payload.js, CSV, and sampled_45.json! Sampled count:", len(sampled))
