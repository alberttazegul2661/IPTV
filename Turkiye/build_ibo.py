"""Version propre pour IBO Player : une entrée par chaîne, flux http uniquement.
Construite à partir de la liste de build_v2.py.  Usage : python3 build_ibo.py
"""
from build_v2 import CH, TR

# Chaînes connues pour ne pas fonctionner en http (testées dans IBO)
SKIP = {"TV8"}
RENAME = {}

out, seen = ["#EXTM3U"], set()
for g, name, tid, logo, url, *flags in CH:
    if "https" in flags or "yedek" in name or name in SKIP:
        continue
    name = RENAME.get(name, name)
    if name in seen:
        continue
    seen.add(name)
    if url.startswith("https://"):
        url = "http://" + url[8:]
    logo = f' tvg-logo="{logo}"' if logo else ""
    out += [f'#EXTINF:-1 tvg-id="{tid}"{logo} group-title="{TR[g]}",{name}', url]
open("turquie-ibo.m3u", "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
print(len(seen), "chaînes")
