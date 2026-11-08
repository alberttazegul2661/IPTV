"""Nettoie une liste brute iptv-org (streams/tr.m3u) :
un flux par chaîne (le plus fiable), flux pirates retirés, catégories ajoutées.
Usage : python3 clean.py source-iptv-org.m3u source-officiels.m3u turquie.m3u
"""
import re, sys
from urllib.parse import urlparse

*srcs, dst = sys.argv[1:]

# Hébergeurs officiels des diffuseurs (priorité haute)
OFFICIAL = ("medya.trt.com.tr", "daioncdn.net", "ercdn.net", "mncdn.com", "duhnet.tv",
            "radyotvonline", "socialsmart.tv", "powerapp.com.tr", "tmgrup", "turkmedya",
            "dogus", "ciner", "demiroren", "blutv")
# Relais pirates / non fiables (exclus)
BLOCK = ("tecostream", "fulltvizle", "canlitv", "bozztv", "smartplaytv", "darktv",
         "playhd", ".xyz", "tulix", "githubusercontent", "onrender")

CAT = {
 "General": "TRT1 TRT2 ATV KanalD StarTV NOW TV8 Kanal7 BeyazTV A2TV TV4 ShowTV ShowTurk TV85 tv2 EuroD ATVAvrupa Kanal7Avrupa TRTTurk TV1 TempoTV Tivi6 MeltemTV TurksatTanitim",
 "News": "TRTHaber CNNTurk TV100 NTV HaberturkTV HalkTV AHaber 24TV 360 TGRTHaber TVNET TurkHaberTV HaberGlobal FlashHaberTV Tele1 UlkeTV BenguturkTV DHA OlayTurkTV TBMMTV KentTurk LineTV AnadoluNetTV",
 "Business": "BloombergHT CNBCe Ekoturk FinansTurkTV",
 "Sports": "TRTSpor TRTSporYildiz TRT3 ASpor EkolSports HTSporTV FBTV SSport2 TJKTV TJKTV2 BricveSatrancTV",
 "Kids": "TRTCocuk TRTDiyanetCocuk MinikaCocuk MinikaGo CartoonNetwork DisneyJr SpacetoonTurkey ZarokTV",
 "Documentary": "TRTBelgesel GZT TGRTBelgesel NationalGeographic NationalGeographicWild ViasatHistory NaturalTV CiftciTV",
 "Movies & Series": "KanalDDrama MovieSmartTurk FX DreamTurk",
 "Music": "TRTMuzik KralPopTV Number1TV Number1Ask Number1Damar Number1Dance PowerTV PowerTurkTV PowerTurkAkustik PowerTurkSlow PowerTurkTaptaze Number1Turk PowerDance PowerLove MedMuzik DostTV",
 "Religious": "DiyanetTV SemerkandTV LalegulTV Sat7Turk KanalHayat MekameleenTV AlZahraTVTurkic IlkeTV",
 "Education": "TRTEBA TRTEBAIlkokul TRTEBALise TRTGenc",
 "International": "TRTWorld TRTArabi TRTAvaz TRTKurdi LuysTV QafTV AlmahriahTV",
}
ID2CAT = {i: c for c, ids in CAT.items() for i in ids.split()}

LOGO = {
 "TRT1": "j786OLG", "TRT2": "lNWrOE2", "TRTHaber": "OVfo8Ab", "TRTSpor": "N2wGZyf",
 "TRTSporYildiz": "ysKteM8", "TRTCocuk": "QLFmD6d", "TRTMuzik": "fIVFCEd", "TRTBelgesel": "MGO87pe",
 "TRTAvaz": "VhTwXu5", "TRTKurdi": "6BpymfB", "TRTArabi": "yyhWOZs", "TRTWorld": "JEA2xpv",
 "TRTTurk": "OSTOQNw", "TRTEBAIlkokul": "wDvZfk8", "TRTEBA": "yfPTvRx", "TRTEBALise": "IebUZx1",
 "ATV": "HyVUwFC", "KanalD": "9o1atM6", "NOW": "5EYjWK7", "Kanal7": "0gq9xOm", "BeyazTV": "uykIdML",
 "TV4": "UpsQsbd", "HaberturkTV": "6Tw3rUp", "HalkTV": "xM0HA30", "24TV": "8FO41es", "360": "agn47sQ",
 "TVNET": "mQo8yWQ", "BloombergHT": "bmkXfIE", "ASpor": "ZhkZzLf", "Number1Turk": "18zjk3q",
}

def score(url, name, has_opts):
    host = urlparse(url).hostname or ""
    if any(b in url for b in BLOCK) or re.fullmatch(r"[\d.]+", host):
        return None
    s = 0
    if any(o in host or o in url for o in OFFICIAL): s += 100
    if url.startswith("https"): s += 20
    if re.search(r"\.m3u8?(\?|$)", url): s += 10
    if "[Not 24/7]" in name: s -= 15
    if "[Geo-blocked]" in name: s -= 10
    if has_opts: return None      # IBO ne gère pas les en-têtes EXTVLCOPT
    if "sid=" in url: s -= 25     # jeton de session, expire
    m = re.search(r"\((\d+)p\)", name)
    if m: s += int(m.group(1)) // 100
    return s

ALIAS = {"NOWTV": "NOW", "TurkHaber": "TurkHaberTV"}

def clean_name(n):
    n = re.sub(r"\s*\[[^\]]*\]", "", n)
    n = re.sub(r"\s*\(\d+p\)", "", n)
    return n.strip()

lines = [l for f in srcs for l in open(f, encoding="utf-8").read().splitlines()]
best, order, opts = {}, [], []
for ln in lines:
    ln = ln.strip()
    if ln.startswith("#EXTINF"):
        inf, opts = ln, []
    elif ln.startswith("#EXTVLCOPT"):
        opts.append(ln)
    elif ln and not ln.startswith("#"):
        tid = re.search(r'tvg-id="([^"]*)"', inf)
        tid = tid.group(1) if tid else ""
        name = inf.split(",", 1)[1]
        base = tid.split(".")[0] or re.sub(r"\W", "", clean_name(name))
        base = ALIAS.get(base, base)
        sc = score(ln, name, bool(opts))
        if sc is None: continue
        if base not in best: order.append(base)
        if base not in best or sc > best[base][0]:
            best[base] = (sc, tid, name, ln, list(opts))

def clean_name(n):
    n = re.sub(r"\s*\[[^\]]*\]", "", n)
    n = re.sub(r"\s*\(\d+p\)", "", n)
    return n.strip()

GROUPS = list(CAT) + ["Regional"]
out = ["#EXTM3U"]
count = {}
seen_urls = set()
for g in GROUPS:
    for base in sorted(order, key=lambda b: clean_name(best[b][2]).lower()):
        if ID2CAT.get(base, "Regional") != g: continue
        sc, tid, name, url, o = best[base]
        if url in seen_urls: continue
        seen_urls.add(url)
        logo = f' tvg-logo="https://i.imgur.com/{LOGO[base]}.png"' if base in LOGO else ""
        out.append(f'#EXTINF:-1 tvg-id="{tid}"{logo} group-title="{g}",{clean_name(name)}')
        out.extend(o)
        out.append(url)
        count[g] = count.get(g, 0) + 1
open(dst, "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
print(sum(count.values()), "chaînes"); [print(f"  {g}: {n}") for g, n in count.items()]
