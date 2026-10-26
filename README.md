# Veebikase näidised

Näidislehed potentsiaalsetele klientidele. Avaldatakse Cloudflare Workerina aadressil naidised.veebikask.workers.dev.

- `andmed/<slug>.json`: firma andmed (avalik Äriregistri info), pakett (500 = mitmeleheline, 250 = üheleheline) ja kujundus
- `tooriistad/kujundused.py`: kujundused, igaüks oma avaploki, fontide ja värvidega
- `tooriistad/kujundus.py`: lehtede ehitaja (sektsioonid, alamlehed, vorm, privaatsus)
- `tooriistad/genereeri.py`: ehitab `public/<slug>/` kõigist andmefailidest
- `tooriistad/kontroll.py`: master prompti kontrollnimekiri, peab andma "KÕIK KORRAS"
- `tooriistad/meilid.py`: eelvaatepildid ja meilid (meilid/ ei lähe reposse)

HTML-i käsitsi ei muudeta. Muuda andmeid või kujundust ja jooksuta:

    python3 tooriistad/genereeri.py && python3 tooriistad/kontroll.py

Kõik lehed on noindex (`_headers`, `robots.txt`). Juuraadress suunab veebikask.ee peale.
Fondid: Google Fonts (SIL Open Font License), majutatud kaustas public/fondid.
