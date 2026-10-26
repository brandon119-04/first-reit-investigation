import json

with open("/Users/brandonwong/.gemini/antigravity/scratch/first-reit-investigation/yahoo_data.json") as f:
    raw = json.load(f)

aw_map = {x["date"]: x for x in raw["AW9U.SI"]["series"]}
c2_map = {x["date"]: x for x in raw["C2PU.SI"]["series"]}
lp_map = {x["date"]: x for x in raw["LPKR.JK"]["series"]}
si_map = {x["date"]: x for x in raw["SILO.JK"]["series"]}
idr_map = {x["date"]: x for x in raw["SGDIDR=X"]["series"]}
jpy_map = {x["date"]: x for x in raw["SGDJPY=X"]["series"]}

dates = sorted(list(aw_map.keys()))

aligned_series = []
for dt in dates:
    aw = aw_map.get(dt, {})
    c2 = c2_map.get(dt, {})
    lp = lp_map.get(dt, {})
    si = si_map.get(dt, {})
    idr = idr_map.get(dt, {})
    jpy = jpy_map.get(dt, {})
    aligned_series.append({
        "d": dt,
        "aw": aw.get("close"),
        "aw_adj": aw.get("adjclose"),
        "c2": c2.get("close"),
        "c2_adj": c2.get("adjclose"),
        "lp": lp.get("close"),
        "si": si.get("close"),
        "idr": idr.get("close"),
        "jpy": jpy.get("close")
    })

ticker_meta = {}
for k, v in raw.items():
    ticker_meta[k] = v["meta"]

yahoo_js_payload = json.dumps({
    "fetchedAt": "2026-10-26T13:13:38+08:00",
    "meta": ticker_meta,
    "series": aligned_series,
    "aw9u_dividends_count": len(raw["AW9U.SI"]["dividends"])
}, separators=(",", ":"))

print("Payload size bytes:", len(yahoo_js_payload))

with open("/Users/brandonwong/.gemini/antigravity/scratch/first-reit-investigation/yahoo_payload.js", "w") as f:
    f.write(f"window.YAHOO_FINANCE_DATA = {yahoo_js_payload};\n")
print("Wrote yahoo_payload.js")
