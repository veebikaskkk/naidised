# Veebikase näidised

Näidislehed potentsiaalsetele klientidele. Avaldatakse Cloudflare Workerina aadressil naidis.veebikask.ee.

- `andmed/<slug>.json`: firma andmed (avalik Äriregistri info), pakett (500 = mitmeleheline, 400 = üheleheline broneerimiskalendriga, 250 = üheleheline päringuvormiga) ja kujundus
- `tooriistad/kujundused*.py`: kujundused valdkonniti (viimistlus, auto, juuks, elekter), igaüks oma avaploki, fontide ja värvidega
- `tooriistad/vahend.py`: palett, mis kontrollib kontrasti juba loomisel
- `tooriistad/kujundus.py`: lehtede ehitaja (sektsioonid, alamlehed, vorm, privaatsus)
- `tooriistad/genereeri.py`: ehitab `public/<slug>/` kõigist andmefailidest
- `tooriistad/kontroll.py`: master prompti kontrollnimekiri, peab andma "KÕIK KORRAS"
- `tooriistad/meilid.py`: eelvaatepildid ja meilid (meilid/ ei lähe reposse)

HTML-i käsitsi ei muudeta. Muuda andmeid või kujundust ja jooksuta:

    python3 tooriistad/genereeri.py && python3 tooriistad/kontroll.py

Kõik lehed on noindex (`_headers`, `robots.txt`). Juuraadress suunab veebikask.ee peale.
Fondid: Google Fonts (SIL Open Font License), majutatud kaustas public/fondid.
