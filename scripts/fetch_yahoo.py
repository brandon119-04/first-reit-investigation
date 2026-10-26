import urllib.request
import json
import datetime

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}
tickers = ["AW9U.SI", "C2PU.SI", "LPKR.JK", "SILO.JK", "LJ3.SI", "5WA.SI", "SGDIDR=X", "SGDJPY=X"]

output = {}

for t in tickers:
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?range=max&interval=1mo&events=div,split"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            res = data["chart"]["result"][0]
            meta = res["meta"]
            ts = res.get("timestamp", [])
            quotes = res["indicators"]["quote"][0]
            closes = quotes.get("close", [])
            adjcloses = res["indicators"].get("adjclose", [{}])[0].get("adjclose", [])
            volumes = quotes.get("volume", [])
            
            series = []
            for i in range(len(ts)):
                if closes[i] is not None:
                    dt = datetime.datetime.fromtimestamp(ts[i]).strftime("%Y-%m")
                    series.append({
                        "date": dt,
                        "close": round(closes[i], 4),
                        "adjclose": round(adjcloses[i], 4) if i < len(adjcloses) and adjcloses[i] is not None else None,
                        "volume": volumes[i]
                    })
            
            divs_raw = res.get("events", {}).get("dividends", {})
            divs = []
            for k, v in sorted(divs_raw.items(), key=lambda x: int(x[0])):
                dt = datetime.datetime.fromtimestamp(v["date"]).strftime("%Y-%m-%d")
                divs.append({"date": dt, "amount": round(v["amount"], 5)})
                
            cur = meta.get("currency")
            rmp = meta.get("regularMarketPrice")
            hi52 = meta.get("fiftyTwoWeekHigh")
            lo52 = meta.get("fiftyTwoWeekLow")
            first_pt = series[0] if series else None
            last_pt = series[-1] if series else None
            print(f"{t}: currency={cur}, price={rmp}, 52w={lo52}-{hi52}, points={len(series)}, first={first_pt}, last={last_pt}, divs={len(divs)}")
            
            output[t] = {
                "meta": {
                    "symbol": meta.get("symbol"),
                    "shortName": meta.get("shortName") or meta.get("longName") or t,
                    "currency": cur,
                    "regularMarketPrice": rmp,
                    "fiftyTwoWeekHigh": hi52,
                    "fiftyTwoWeekLow": lo52,
                    "exchangeName": meta.get("exchangeName"),
                },
                "series": series,
                "dividends": divs
            }
    except Exception as e:
        print(f"{t}: ERROR {e}")

with open("/Users/brandonwong/.gemini/antigravity/scratch/first-reit-investigation/yahoo_data.json", "w") as f:
    json.dump(output, f, indent=2)
print("Saved yahoo_data.json successfully.")
