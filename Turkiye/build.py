import sys
G = {
 "gen":"Turquie | Généralistes","info":"Turquie | Info","eco":"Turquie | Économie",
 "sport":"Turquie | Sport","kids":"Turquie | Jeunesse","doc":"Turquie | Documentaires",
 "music":"Turquie | Musique","edu":"Turquie | Éducation","intl":"Turquie | International & Langues",
}
I="https://i.imgur.com/"; T="http://assets.tvcdn.net/"; TRT="medya.trt.com.tr/master.m3u8"
ch = [
# Généralistes
("gen","TRT 1","TRT1.tr",I+"j786OLG.png","https://tv-trt1."+TRT),
("gen","TRT 2","TRT2.tr",I+"lNWrOE2.png","https://tv-trt2."+TRT),
("gen","ATV","ATV.tr",I+"HyVUwFC.png","https://rnttwmjcin.turknet.ercdn.net/lcpmvefbyo/atv/atv_1080p.m3u8"),
("gen","Kanal D","KanalD.tr",I+"9o1atM6.png","https://demiroren.daioncdn.net/kanald/kanald.m3u8?app=kanald_web&ce=3"),
("gen","Show TV","ShowTV.tr",T+"9d873881-bb5e-40f0-88db-8c47aa215e5a.png","https://ciner-live.daioncdn.net/showtv/showtv.m3u8"),
("gen","Star TV","StarTV.tr",T+"0c5204fb-e613-4084-b300-8cdcc46309f9.png","https://dogus-live.daioncdn.net/startv/startv.m3u8"),
("gen","NOW","NOWTV.tr",I+"5EYjWK7.png","https://uycyyuuzyh.turknet.ercdn.net/nphindgytw/nowtv/nowtv.m3u8"),
("gen","TV8","TV8.tr",T+"f91342d2-bcae-4ee0-a6f8-76a8d32b891b.png","https://tv8-live.daioncdn.net/tv8/tv8.m3u8"),
("gen","TV8.5","TV85.tr","https://i.ibb.co/dgj3MTh/tv85.png","https://tv8-live.daioncdn.net/tv8bucuk/tv8bucuk.m3u8"),
("gen","Teve2","tv2.tr",I+"rsoSLih.png","https://demiroren-live.daioncdn.net/teve2/teve2.m3u8"),
("gen","Kanal 7","Kanal7.tr",I+"0gq9xOm.png","https://livetv.radyotvonline.net/kanal7live/kanal7avr/playlist.m3u8"),
("gen","Beyaz TV","BeyazTV.tr",I+"uykIdML.png","https://beyaztv.daioncdn.net/beyaztv/beyaztv.m3u8?app=fcd5c66b-da9d-44ba-a410-4f34805c397d&ce=3"),
("gen","A2","A2TV.tr","https://iatv.tmgrup.com.tr/site/v2/a2tv/i/a2tv-logo.png","https://rnttwmjcin.turknet.ercdn.net/lcpmvefbyo/a2tv/a2tv.m3u8"),
("gen","TV4","TV4.tr",I+"UpsQsbd.png","https://turkmedya-live.ercdn.net/tv4/tv4.m3u8"),
# Info
("info","TRT Haber","TRTHaber.tr",I+"OVfo8Ab.png","https://tv-trthaber."+TRT),
("info","NTV","NTV.tr",T+"b2aa3114-53bd-4ff5-81ed-af75a28e651f.png","https://dogus-live.daioncdn.net/ntv/ntv.m3u8"),
("info","CNN Türk","CNNTurk.tr","","https://live.duhnet.tv/S2/HLS_LIVE/cnnturknp/playlist.m3u8"),
("info","Habertürk","HaberturkTV.tr",I+"6Tw3rUp.png","https://ciner-live.daioncdn.net/haberturktv/haberturktv.m3u8"),
("info","Halk TV","HalkTV.tr",I+"xM0HA30.png","https://halktv-live.daioncdn.net/halktv/halktv.m3u8"),
("info","TV100","TV100.tr",T+"d7741078-ccce-47d8-ba1c-a041b659bad6.png","https://tv100-live.daioncdn.net/tv100/tv100.m3u8"),
("info","A Haber","AHaber.tr","https://upload.wikimedia.org/wikipedia/commons/7/7c/Ahaber_Logo.png","https://rnttwmjcin.turknet.ercdn.net/lcpmvefbyo/ahaber/ahaber.m3u8"),
("info","24 TV","24TV.tr",I+"8FO41es.png","https://turkmedya-live.ercdn.net/tv24/tv24.m3u8"),
("info","360","360.tr",I+"agn47sQ.png","https://turkmedya-live.ercdn.net/tv360/tv360.m3u8"),
("info","TGRT Haber","TGRTHaber.tr","","https://tgrthaber-live.daioncdn.net/tgrthaber/tgrthaber.m3u8"),
("info","TVNET","TVNET.tr",I+"mQo8yWQ.png","https://mn-nl.mncdn.com/tvnet/tvnet/playlist.m3u8"),
("info","TH Türk Haber","TurkHaber.tr","","https://edge1.socialsmart.tv/turkhaber/bant1/playlist.m3u8"),
# Économie
("eco","Bloomberg HT","BloombergHT.tr",I+"bmkXfIE.png","https://ciner.daioncdn.net/bloomberght/bloomberght.m3u8"),
# Sport
("sport","TRT Spor","TRTSpor.tr",I+"N2wGZyf.png","https://tv-trtspor1."+TRT),
("sport","TRT Spor Yıldız","TRTSporYildiz.tr",I+"ysKteM8.png","https://tv-trtspor2."+TRT),
("sport","A Spor","ASpor.tr",I+"ZhkZzLf.png","https://rnttwmjcin.turknet.ercdn.net/lcpmvefbyo/aspor/aspor.m3u8"),
("sport","Ekol Sports","EkolSports.tr","","https://ekoltv-live.ercdn.net/ekolsport/ekolsport_1080p.m3u8"),
# Jeunesse
("kids","TRT Çocuk","TRTCocuk.tr",I+"QLFmD6d.png","https://tv-trtcocuk."+TRT),
# Documentaires
("doc","TRT Belgesel","TRTBelgesel.tr",I+"MGO87pe.png","https://tv-trtbelgesel-dai."+TRT),
("doc","GZT","GZT.tr","https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/GZT_logo.svg/960px-GZT_logo.svg.png","https://gzttv-live.lg.mncdn.com/gzttv/gzttv/playlist.m3u8"),
# Musique
("music","TRT Müzik","TRTMuzik.tr",I+"fIVFCEd.png","https://tv-trtmuzik."+TRT),
("music","Number 1 Türk","Number1Turk.tr",I+"18zjk3q.png","https://mn-nl.mncdn.com/blutv_nr1turk2/live.m3u8"),
("music","Dream Türk","DreamTurk.tr","","https://live.duhnet.tv/S2/HLS_LIVE/dreamturknp/playlist.m3u8"),
("music","Power Türk Taptaze","PowerTurkTaptaze.tr","","https://livetv.powerapp.com.tr/pturktaptaze/taptaze.smil/playlist.m3u8"),
# Éducation
("edu","TRT EBA İlkokul","TRTEBAIlkokul.tr",I+"wDvZfk8.png","https://tv-e-okul00."+TRT),
("edu","TRT EBA Ortaokul","TRTEBA.tr",I+"yfPTvRx.png","https://tv-e-okul01."+TRT),
("edu","TRT EBA Lise","TRTEBALise.tr",I+"IebUZx1.png","https://tv-e-okul02."+TRT),
# International & langues
("intl","TRT Türk","TRTTurk.tr",I+"OSTOQNw.png","https://tv-trtturk."+TRT),
("intl","TRT World","TRTWorld.tr",I+"JEA2xpv.png","https://tv-trtworld."+TRT),
("intl","TRT Arabi","TRTArabi.tr",I+"yyhWOZs.png","https://tv-trtarabi."+TRT),
("intl","TRT Avaz","TRTAvaz.tr",I+"VhTwXu5.png","https://tv-trtavaz."+TRT),
("intl","TRT Kurdî","TRTKurdi.tr",I+"6BpymfB.png","https://tv-trtkurdi."+TRT),
]
out=['#EXTM3U']
for n,(g,name,tid,logo,url) in enumerate(ch,1):
    out.append(f'#EXTINF:-1 tvg-name="{name}" tvg-logo="{logo}" tvg-id="{tid}" tvg-chno="{n}" tvg-country="TR" group-title="{G[g]}",{name}')
    out.append(url)
open(sys.argv[1],"w",encoding="utf-8").write("\n".join(out)+"\n")
print(len(ch),"chaînes")
