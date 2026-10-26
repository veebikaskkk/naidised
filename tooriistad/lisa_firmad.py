"""Teeb päeva firmade nimekirjast (kontaktid.csv read JSON-ina) andmefailid ja meilid.

Kasutus: python3 tooriistad/lisa_firmad.py <paev.json> <mall>
Kirjutab andmed/<slug>.json ja meilid/<kuupäev>.csv (meilid ei lähe veebi).
"""
import csv, hashlib, json, pathlib, re, sys

juur = pathlib.Path(__file__).resolve().parent.parent
VEEB = "https://naidised.veebikask.workers.dev"
KAIVE_PIIR = 40000

MAAKOND = {
    "Harju": "Harjumaa", "Tartu": "Tartumaa", "Ida-Viru": "Ida-Virumaa", "Pärnu": "Pärnumaa",
    "Jõgeva": "Jõgevamaa", "Valga": "Valgamaa", "Järva": "Järvamaa", "Lääne": "Läänemaa",
    "Rapla": "Raplamaa", "Hiiu": "Hiiumaa", "Saare": "Saaremaa", "Viljandi": "Viljandimaa",
    "Võru": "Võrumaa", "Põlva": "Põlvamaa", "Lääne-Viru": "Lääne-Virumaa",
}
# Linn: (nimi, seesütlev). Ainult linnad, mille käänet tean kindlalt.
LINNAD = {
    "Tallinn": "Tallinnas", "Tartu linn": "Tartus", "Pärnu linn": "Pärnus", "Narva linn": "Narvas",
    "Kohtla-Järve linn": "Kohtla-Järvel", "Haapsalu linn": "Haapsalus", "Valga linn": "Valgas",
    "Maardu linn": "Maardus", "Viljandi linn": "Viljandis", "Rakvere linn": "Rakveres",
    "Kuressaare linn": "Kuressaares", "Võru linn": "Võrus", "Keila linn": "Keilas",
}


def lyhinimi(nimi):
    n = re.sub(r"\b(OÜ|AS|Osaühing|OSAÜHING|osaühing|Aktsiaselts|AKTSIASELTS)\b", "", nimi).strip(" ,")
    if n.isupper():
        n = " ".join(w.capitalize() if len(w) > 2 else w for w in n.split())
    return n


def asukoht(aadress):
    osad = [o.strip() for o in aadress.split(",")]
    maak = osad[0].replace(" maakond", "") if osad and osad[0] else "Harju"
    maa = MAAKOND.get(maak, maak + "maa")
    linn = next((o for o in osad[1:3] if o in LINNAD), None)
    if linn:
        lnimi = linn.replace(" linn", "")
        return f"{lnimi} ja {maa}", f"{LINNAD[linn]} ja {maa}l", LINNAD[linn]
    return maa, maa + "l", maa + "l"


def slug(lyhi, kood):
    s = lyhi.lower()
    for a, b in (("õ", "o"), ("ä", "a"), ("ö", "o"), ("ü", "u"), ("š", "s"), ("ž", "z")):
        s = s.replace(a, b)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return f"{s}-{hashlib.sha1(kood.encode()).hexdigest()[:4]}"


def main(paev, mall):
    firmad = json.loads(pathlib.Path(paev).read_text(encoding="utf-8"))
    kuupaev = re.search(r"\d{4}-\d{2}-\d{2}", paev).group(0)
    (juur / "meilid").mkdir(exist_ok=True)
    w = csv.writer(open(juur / "meilid" / f"{kuupaev}.csv", "w", newline="", encoding="utf-8"))
    w.writerow(["email", "firma", "pealkiri", "keha", "link", "pakett", "kaive"])
    paletid = ["sinine", "kirss", "sammal", "petrool", "ploom"]
    for i, x in enumerate(firmad):
        lyhi = lyhinimi(x["nimi"])
        piirkond, piirkond_kus, linn_kus = asukoht(x["aadress"])
        s = slug(lyhi, x["registrikood"])
        tel = [t.strip() for t in x["telefon"].split(";") if t.strip()]
        email = x["email"].split(";")[0].strip()
        try:
            tootajaid = int(x["tootajaid"] or 0)
        except ValueError:
            tootajaid = 0
        andmed = {
            "mall": mall, "nimi": x["nimi"], "lyhinimi": lyhi, "registrikood": x["registrikood"],
            "emtak": x["emtak_kood"], "telefonid": tel, "email": email, "piirkond": piirkond,
            "piirkond_kus": piirkond_kus, "linn_kus": linn_kus,
            "aasta": (x.get("registreeritud") or "")[-4:], "tootajaid": tootajaid or None,
            "palett": paletid[i % len(paletid)],
        }
        (juur / "andmed" / f"{s}.json").write_text(json.dumps(andmed, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        kaive = int(x["kaive"]) if x.get("kaive") else 0
        if kaive >= KAIVE_PIIR:
            pakett, hind = "500", ("Hind on 500 € ühekordselt. Selle eest saate mitmelehelise kodulehe, kus on eraldi lehed teenuste, "
                                  "tehtud tööde ja hinnapäringu vormiga. Majutus ja haldus maksab 100 € aastas, nii et teie ei pea "
                                  "tehnilise poole pärast muretsema.")
        else:
            pakett, hind = "250", ("Hind on 250 € ühekordselt. Lehe majutus ja haldus maksab 75 € aastas, nii et teie ei pea "
                                  "tehnilise poole pärast muretsema.")
        link = f"{VEEB}/{s}/"
        al, le = ("AS-il", "AS-ile") if x.get("vorm") == "AS" else ("OÜ-l", "OÜ-le")
        keha = (f"Tere!\n\nMärkasin, et {lyhi} {al} pole veel oma kodulehte ja tegin teile proovimiseks ühe valmis:\n{link}\n\n"
                f"Seal on teie teenused ja kontaktid ning see töötab ka telefonis. Kui see meeldib, paneme selle teie oma "
                f"aadressile üles ja lisame pildid teie päris töödest.\n\n{hind}\n\n"
                f"Kui see teid ei huvita, vastake lihtsalt ei ja ma rohkem ei kirjuta.")
        w.writerow([email, x["nimi"], f"Tegin {lyhi} {le} näidis-kodulehe", keha, link, pakett, kaive])
        print(s, pakett, piirkond)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
