# Veebikase näidised

Näidislehed potentsiaalsetele klientidele. Avaldatakse Cloudflare Workerina aadressil naidis.veebikask.ee.

- `andmed/<slug>.json`: firma andmed (avalik Äriregistri info)
- `tooriistad/mall_*.py`: lehe mallid valdkonna järgi
- `tooriistad/genereeri.py`: ehitab `public/<slug>/` kõigist andmefailidest
- `tooriistad/kontroll.py`: master prompti kontrollnimekiri, peab andma "KÕIK KORRAS"

HTML-i käsitsi ei muudeta. Muuda andmeid või malli ja jooksuta:

    python3 tooriistad/genereeri.py && python3 tooriistad/kontroll.py

Kõik lehed on noindex (`_headers`, `robots.txt`). Juuraadress suunab veebikask.ee peale.
