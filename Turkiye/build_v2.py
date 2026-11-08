"""Playlist v2 : chaînes nationales turques, uniquement des flux hébergés par les
diffuseurs ou leurs CDN officiels. Écrit deux fichiers :
  turquie-v2.m3u       (https, pour VLC / TiviMate…)
  turquie-v2-http.m3u  (http, pour IBO Player)
Usage : python3 build_v2.py
"""
I = "https://i.imgur.com/"
TRT = lambda s: f"https://tv-{s}.medya.trt.com.tr/master.m3u8"
TKV = "https://rnttwmjcin.turknet.ercdn.net/lcpmvefbyo/"
MT = "https://b01c02nl.mediatriple.net/videoonlylive/"
PW = "https://livetv.powerapp.com.tr/"

# (catégorie, nom, tvg-id, logo, url)
CH = [
 # --- Généralistes
 ("General", "TRT 1", "TRT1.tr", I+"j786OLG.png", TRT("trt1")),
 ("General", "TRT 2", "TRT2.tr", I+"lNWrOE2.png", TRT("trt2")),
 ("General", "ATV", "ATV.tr", I+"HyVUwFC.png", TKV+"atv/atv.m3u8", "https"),
 ("General", "ATV 720p", "ATV.tr", I+"HyVUwFC.png", TKV+"atv/atv_720p.m3u8", "https"),
 ("General", "ATV 1080p", "ATV.tr", I+"HyVUwFC.png", TKV+"atv/atv_1080p.m3u8"),
 ("General", "ATV (yedek 1)", "ATV.tr", I+"HyVUwFC.png", "https://trkvz-live.daioncdn.net/atv/atv.m3u8", "https"),
 ("General", "ATV (yedek 2)", "ATV.tr", I+"HyVUwFC.png", "https://trkvz.daioncdn.net/atv/atv.m3u8?app=d1ce2d40-5256-4550-b02e-e73c185a314e", "https"),
 ("General", "Kanal D", "KanalD.tr", I+"9o1atM6.png", "https://demiroren.daioncdn.net/kanald/kanald.m3u8?app=kanald_web&ce=3"),
 ("General", "Show TV", "ShowTV.tr", "", "https://rmtftbjlne.turknet.ercdn.net/bpeytmnqyp/showtv/showtv_1080p.m3u8"),
 ("General", "Show TV (yedek)", "ShowTV.tr", "", "https://showtv.blutv.com/blutv_showtv_live/live.m3u8"),
 ("General", "Show TV (yedek 2)", "ShowTV.tr", "", "https://ciner-live.daioncdn.net/showtv/showtv.m3u8", "https"),
 ("General", "Show Türk", "ShowTurk.tr", "", "https://mn-nl.mncdn.com/blutv_showturk2/live.m3u8"),
 ("General", "Show Türk (yedek)", "ShowTurk.tr", "", "https://showturk.blutv.com/blutv_showturk2/live.m3u8"),
 ("General", "NOW", "NOW.tr", I+"5EYjWK7.png", "https://uycyyuuzyh.turknet.ercdn.net/nphindgytw/nowtv/nowtv.m3u8"),
 ("General", "TV8", "TV8.tr", "", "https://rkhubpaomb.turknet.ercdn.net/fwjkgpasof/tv8/tv8.m3u8"),
 ("General", "TV8 (yedek)", "TV8.tr", "", "https://tv8-live.daioncdn.net/tv8/tv8.m3u8", "https"),
 ("General", "TV8 Int", "TV8International.tr", "", "https://mn-nl.mncdn.com/blutv_tv8_int2/live.m3u8"),
 ("General", "TV8.5", "TV85.tr", "", "https://rkhubpaomb.turknet.ercdn.net/fwjkgpasof/tv8bucuk/tv8bucuk.m3u8"),
 ("General", "TV8.5 (yedek)", "TV85.tr", "", "https://tv85.blutv.com/blutv_tv8_5_live/live.m3u8"),
 ("General", "Teve2", "Teve2.tr", "", "https://demiroren-live.daioncdn.net/teve2/teve2.m3u8"),
 ("General", "Kanal 7", "Kanal7.tr", I+"0gq9xOm.png", "https://kanal7-live.daioncdn.net/kanal7/kanal7.m3u8"),
 ("General", "Beyaz TV", "BeyazTV.tr", I+"uykIdML.png", "https://mn-nl.mncdn.com/blutv_beyaztv2/live.m3u8"),
 ("General", "A2", "A2TV.tr", "", TKV+"a2tv/a2tv.m3u8"),
 ("General", "TV4", "TV4.tr", I+"UpsQsbd.png", "https://turkmedya-live.ercdn.net/tv4/tv4.m3u8"),
 ("General", "TRT Genç", "TRTGenc.tr", "", TRT("trtgenc")),
 ("General", "Euro D", "EuroD.tr", "", "https://live.duhnet.tv/S2/HLS_LIVE/eurodnp/playlist.m3u8"),
 ("General", "Kanal 7 Avrupa", "Kanal7Avrupa.tr", "", "https://livetv.radyotvonline.net/kanal7live/kanal7avr/playlist.m3u8"),
 ("General", "Kanal 7 Avrupa (yedek)", "Kanal7Avrupa.tr", "", "http://live.kanal7.com/live/kanal7AvrupaLive/index.m3u8"),
 ("General", "ATV Avrupa", "ATVAvrupa.tr", "", "https://trkvz-live.ercdn.net/atvavrupa/atvavrupa.m3u8"),
 # --- Info
 ("News", "TRT Haber", "TRTHaber.tr", I+"OVfo8Ab.png", TRT("trthaber")),
 ("News", "NTV", "NTV.tr", "", "https://dogus-live.daioncdn.net/ntv/ntv.m3u8"),
 ("News", "CNN Türk", "CNNTurk.tr", "", "https://live.duhnet.tv/S2/HLS_LIVE/cnnturknp/playlist.m3u8"),
 ("News", "Habertürk", "HaberturkTV.tr", I+"6Tw3rUp.png", "https://ciner-live.daioncdn.net/haberturktv/haberturktv.m3u8"),
 ("News", "Halk TV", "HalkTV.tr", I+"xM0HA30.png", "https://halktv-live.daioncdn.net/halktv/halktv.m3u8"),
 ("News", "TV100", "TV100.tr", "", "https://tv100-live.daioncdn.net/tv100/tv100.m3u8"),
 ("News", "A Haber", "AHaber.tr", "", TKV+"ahaber/ahaber.m3u8"),
 ("News", "24 TV", "24TV.tr", I+"8FO41es.png", "https://turkmedya-live.ercdn.net/tv24/tv24.m3u8"),
 ("News", "360", "360.tr", I+"agn47sQ.png", "https://turkmedya-live.ercdn.net/tv360/tv360.m3u8"),
 ("News", "TGRT Haber", "TGRTHaber.tr", "", "https://canli.tgrthaber.com/tgrt.m3u8"),
 ("News", "TVNET", "TVNET.tr", I+"mQo8yWQ.png", "https://tvnet-live.lg.mncdn.com/tvnet/tvnet/playlist.m3u8"),
 ("News", "Tele 1", "Tele1.tr", "", "https://tele1-live.ercdn.net/tele1/tele1.m3u8"),
 ("News", "TH Türk Haber", "TurkHaberTV.tr", "", "https://edge1.socialsmart.tv/turkhaber/bant1/playlist.m3u8"),
 ("News", "TBMM TV", "TBMMTV.tr", "", "https://meclistv-live.ercdn.net/meclistv/meclistv.m3u8"),
 # --- Économie
 ("Business", "Bloomberg HT", "BloombergHT.tr", I+"bmkXfIE.png", "https://ciner.daioncdn.net/bloomberght/bloomberght.m3u8"),
 ("Business", "CNBC-e", "CNBCe.tr", "", "https://hnpsechtsc.turknet.ercdn.net/xpnvudnlsv/cnbc-e/cnbc-e.m3u8"),
 ("Business", "Ekotürk", "Ekoturk.tr", "", "https://cdn.ekoturk.net/hls/master.m3u8"),
 # --- Sport
 ("Sports", "TRT Spor", "TRTSpor.tr", I+"N2wGZyf.png", "https://tv-trtspor1.medya.trt.com.tr/master.m3u8"),
 ("Sports", "TRT Spor Yıldız", "TRTSporYildiz.tr", I+"ysKteM8.png", "https://tv-trtspor2.medya.trt.com.tr/master.m3u8"),
 ("Sports", "TRT 3", "TRT3.tr", "", "https://tv-trt3.live.trt.com.tr/master.m3u8"),
 ("Sports", "A Spor", "ASpor.tr", I+"ZhkZzLf.png", TKV+"aspor/aspor.m3u8"),
 ("Sports", "HT Spor", "HTSporTV.tr", "", "https://ciner.daioncdn.net/ht-spor/ht-spor.m3u8?app=web"),
 ("Sports", "Ekol Sports", "EkolSports.tr", "", "https://ekoltv-live.ercdn.net/ekolsport/ekolsport_1080p.m3u8"),
 ("Sports", "TJK TV", "TJKTV.tr", "", "https://tjktv-live.tjk.org/tjktv.m3u8"),
 ("Sports", "TJK TV 2", "TJKTV2.tr", "", "https://tjktv-live.tjk.org/tjktv2/tjktv2.m3u8"),
 # --- Jeunesse
 ("Kids", "TRT Çocuk", "TRTCocuk.tr", I+"QLFmD6d.png", TRT("trtcocuk")),
 ("Kids", "TRT Diyanet Çocuk", "TRTDiyanetCocuk.tr", "", TRT("trtdiyanetcocuk")),
 ("Kids", "Minika Çocuk", "MinikaCocuk.tr", "", TKV+"minikago_cocuk/minikago_cocuk.m3u8"),
 ("Kids", "Minika Go", "MinikaGo.tr", "", TKV+"minikago/minikago.m3u8"),
 # --- Documentaires
 ("Documentary", "TRT Belgesel", "TRTBelgesel.tr", I+"MGO87pe.png", TRT("trtbelgesel")),
 ("Documentary", "GZT", "GZT.tr", "", "https://gzttv-live.lg.mncdn.com/gzttv/gzttv/playlist.m3u8"),
 ("Documentary", "TGRT Belgesel", "TGRTBelgesel.tr", "", MT+"mtsxxkzwwuqtglive/broadcast_5fe462afc6a0e.smil/playlist.m3u8"),
 # --- Musique
 ("Music", "TRT Müzik", "TRTMuzik.tr", I+"fIVFCEd.png", TRT("trtmuzik")),
 ("Music", "Kral Pop TV", "KralPopTV.tr", "", "https://dogus-live.daioncdn.net/kralpoptv/playlist.m3u8"),
 ("Music", "Number 1 TV", "Number1TV.tr", "", "https://mn-nl.mncdn.com/blutv_nr12/live.m3u8"),
 ("Music", "Number 1 Türk", "Number1Turk.tr", I+"18zjk3q.png", "https://mn-nl.mncdn.com/blutv_nr1turk2/live.m3u8"),
 ("Music", "Number 1 Aşk", "Number1Ask.tr", "", MT+"mtkgeuihrlfwlive/u_stream_5c9e18f9cea15_1/playlist.m3u8"),
 ("Music", "Number 1 Damar", "Number1Damar.tr", "", MT+"mtkgeuihrlfwlive/u_stream_5c9e198784bdc_1/playlist.m3u8"),
 ("Music", "Number 1 Dance", "Number1Dance.tr", "", MT+"mtkgeuihrlfwlive/u_stream_5c9e2aa8acf44_1/playlist.m3u8"),
 ("Music", "Power TV", "PowerTV.tr", "", PW+"powerTV/powerhd.smil/playlist.m3u8"),
 ("Music", "PowerTürk TV", "PowerTurkTV.tr", "", PW+"powerturkTV/powerturkhd.smil/playlist.m3u8"),
 ("Music", "PowerTürk Taptaze", "PowerTurkTaptaze.tr", "", PW+"pturktaptaze/taptaze.smil/playlist.m3u8"),
 ("Music", "PowerTürk Akustik", "PowerTurkAkustik.tr", "", PW+"pturkakustik/akustik.smil/playlist.m3u8"),
 ("Music", "PowerTürk Slow", "PowerTurkSlow.tr", "", PW+"pturkslow/slow.smil/playlist.m3u8"),
 ("Music", "Power Dance", "PowerDance.tr", "", PW+"dance/dance.smil/playlist.m3u8"),
 ("Music", "Power Love", "PowerLove.tr", "", PW+"plove/love.smil/playlist.m3u8"),
 ("Music", "Dream Türk", "DreamTurk.tr", "", "https://live.duhnet.tv/S2/HLS_LIVE/dreamturknp/playlist.m3u8"),
 # --- Religion
 ("Religious", "Diyanet TV", "DiyanetTV.tr", "", "https://eustr73.mediatriple.net/videoonlylive/mtikoimxnztxlive/broadcast_5e3bf95a47e07.smil/playlist.m3u8"),
 ("Religious", "Semerkand TV", "SemerkandTV.tr", "", MT+"mtisvwurbfcyslive/broadcast_58d915bd40efc.smil/playlist.m3u8"),
 ("Religious", "Lalegül TV", "LalegulTV.tr", "", "https://lbl.netmedya.net/hls/lalegultv.m3u8"),
 ("Religious", "SAT-7 Türk", "Sat7Turk.cy", "", "https://svs.itworkscdn.net/sat7turklive/sat7turk.smil/playlist.m3u8"),
 # --- Éducation
 ("Education", "TRT EBA İlkokul", "TRTEBAIlkokul.tr", I+"wDvZfk8.png", "https://tv-e-okul00.medya.trt.com.tr/master.m3u8"),
 ("Education", "TRT EBA Ortaokul", "TRTEBA.tr", I+"yfPTvRx.png", "https://tv-e-okul01.medya.trt.com.tr/master.m3u8"),
 ("Education", "TRT EBA Lise", "TRTEBALise.tr", I+"IebUZx1.png", "https://tv-e-okul02.medya.trt.com.tr/master.m3u8"),
 # --- International
 ("International", "TRT Türk", "TRTTurk.tr", I+"OSTOQNw.png", TRT("trtturk")),
 ("International", "TRT World", "TRTWorld.tr", I+"JEA2xpv.png", TRT("trtworld")),
 ("International", "TRT Arabi", "TRTArabi.tr", I+"yyhWOZs.png", TRT("trtarabi")),
 ("International", "TRT Avaz", "TRTAvaz.tr", I+"VhTwXu5.png", TRT("trtavaz")),
 ("International", "TRT Kurdî", "TRTKurdi.tr", I+"6BpymfB.png", TRT("trtkurdi")),
]

TR = {"General": "Ulusal", "News": "Haber", "Business": "Ekonomi", "Sports": "Spor",
      "Kids": "Çocuk", "Documentary": "Belgesel", "Music": "Müzik", "Religious": "Dini",
      "Education": "Eğitim", "International": "Uluslararası"}

def write(path, http):
    out = ["#EXTM3U"]
    for g, name, tid, logo, url, *flags in CH:
        if http and "https" in flags:
            continue          # flux https uniquement : inutile pour IBO
        if http and url.startswith("https://"):
            url = "http://" + url[8:]
        logo = f' tvg-logo="{logo}"' if logo else ""
        out.append(f'#EXTINF:-1 tvg-id="{tid}"{logo} group-title="{TR[g]}",{name}')
        out.append(url)
    open(path, "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")

write("turquie-v2.m3u", http=False)
write("turquie-v2-http.m3u", http=True)
print(len(CH), "entrées")
