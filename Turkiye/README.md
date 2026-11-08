# Turkiye — playlist IPTV

162 chaînes turques gratuites, 12 catégories (format iptv-org) :
General, News, Business, Sports, Kids, Documentary, Movies & Series, Music, Religious, Education, International, Regional.

Un seul flux par chaîne : flux officiels des diffuseurs en priorité (TRT, Demirören, Ciner, Doğuş, Turkuvaz, Türkmedya…),
relais pirates et serveurs en IP exclus.

Lien IBO Player (type M3U URL) :

```
https://alberttazegul2661.github.io/IPTV/Turkiye/turquie.m3u
```

## Fichiers
- `turquie.m3u` — la playlist à utiliser
- `source-iptv-org.m3u` — liste brute iptv-org (streams/tr.m3u)
- `source-officiels.m3u` — flux officiels ajoutés à la main
- `clean.py` — régénère la playlist : `python3 clean.py source-iptv-org.m3u source-officiels.m3u turquie.m3u`
