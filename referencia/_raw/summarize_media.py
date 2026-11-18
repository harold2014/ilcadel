import json
import os

base = os.path.dirname(os.path.abspath(__file__))
items = []
for fn in ["media-1.json", "media-2.json"]:
    with open(os.path.join(base, fn), encoding="utf-8") as f:
        items += json.load(f)

print("count", len(items))
mimes = {}
for i in items:
    m = i.get("mime_type")
    mimes[m] = mimes.get(m, 0) + 1
print("mimes", mimes)

rows = []
for i in items:
    md = i.get("media_details") or {}
    name = (i.get("source_url") or "").split("/")[-1]
    rows.append((md.get("filesize") or 0, i.get("mime_type"), md.get("width"), md.get("height"), name, i.get("id")))

rows.sort(reverse=True)
total = sum(r[0] for r in rows)
print("total_mb", round(total / 1024 / 1024, 1))
print("--- ALL ---")
for r in rows:
    print(f"{r[5]}|{r[1]}|{r[2]}x{r[3]}|{r[0]//1024}KB|{r[4]}")
