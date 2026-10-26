"""Teeb päeva firmade nimekirjast andmefailid (andmed/<slug>.json).

Kasutus: python3 tooriistad/lisa_firmad.py <paev.json>
Sisendi iga rida on kontaktid.csv rida, millele on lisatud "pakett" ("500" või "250"),
"kujundus" (võti kujundused.KUJUNDUSED-is) ja "domeen" (vaba .ee nimi ettepanekuks).
"""
import json, pathlib, re, sys
from sisu import slugify

juur = pathlib.Path(__file__).resolve().parent.parent

MAAKOND = {
    "Harju": "Harjumaa", "Tartu": "Tartumaa", "Ida-Viru": "Ida-Virumaa", "Pärnu": "Pärnumaa",
    "Jõgeva": "Jõgevamaa", "Valga": "Valgamaa", "Järva": "Järvamaa", "Lääne": "Läänemaa",
    "Rapla": "Raplamaa", "Hiiu": "Hiiumaa", "Saare": "Saaremaa", "Viljandi": "Viljandimaa",
    "Võru": "Võrumaa", "Põlva": "Põlvamaa", "Lääne-Viru": "Lääne-Virumaa",
}
LINNAD = {
    "Tallinn": "Tallinnas", "Tartu linn": "Tartus", "Pärnu linn": "Pärnus", "Narva linn": "Narvas",
    "Kohtla-Järve linn": "Kohtla-Järvel", "Haapsalu linn": "Haapsalus", "Valga linn": "Valgas",
    "Maardu linn": "Maardus", "Viljandi linn": "Viljandis", "Rakvere linn": "Rakveres",
    "Kuressaare linn": "Kuressaares", "Võru linn": "Võrus", "Keila linn": "Keilas", "Kärdla linn": "Kärdlas",
    "Narva-Jõesuu linn": "Narva-Jõesuus", "Põlva linn": "Põlvas", "Jõgeva linn": "Jõgeval", "Saue linn": "Sauel", "Sindi linn": "Sindis",
}
SISSEJUHATUS = {
    "43311": "Krohvime ja pahteldame seinu ja lagesid {kus}: korterites, eramutes ja ärihoonetes. Pind jääb värvimiseks või tapeedi alla valmis.",
    "4333": "Paigaldame põrandaid ja plaaditame vannitubasid, kööke ja esikuid {kus}. Aluspind tehakse enne korda, et kate jääks sirge.",
    "4334": "Värvime siseruume ja fassaade {kus}. Enne värvi teeme pinna korda, sest just sellest sõltub, kui kaua tulemus vastu peab.",
    "433": "Teeme siseviimistlust {kus}: pahteldame, värvime, plaaditame ja paigaldame põrandaid. Võid tellida kogu remondi või ainult ühe etapi.",
    "95311": "Hooldame ja remondime autosid {kus}. Enne tööd vaatame auto üle ja ütleme, mida on vaja teha ja mis see maksab.",
    "95311-rehv": "Vahetame, tasakaalustame ja parandame rehve {kus}. Samal käigul vaatame üle ka pidurid ja veermiku.",
    "95311-kere": "Parandame autokeresid ja värvime {kus}. Enne tööd vaatame kahju üle ja lepime hinna kokku.",
    "95311-detail": "Peseme, poleerime ja puhastame autosid {kus}, nii seest kui väljast.",
}


def lyhinimi(nimi):
    n = re.sub(r"\b(OÜ|AS|Osaühing|OSAÜHING|osaühing|Aktsiaselts|AKTSIASELTS)\b", "", nimi).strip(" ,")
    if n.isupper():
        n = " ".join(w.capitalize() if len(w) > 4 else w for w in n.split())
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


def sissejuhatus(emtak, kus):
    if emtak in SISSEJUHATUS:
        return SISSEJUHATUS[emtak].format(kus=kus)
    for n in (5, 4, 3):
        if emtak[:n] in SISSEJUHATUS:
            return SISSEJUHATUS[emtak[:n]].format(kus=kus)
    return SISSEJUHATUS["433"].format(kus=kus)


def main(paev):
    firmad = json.loads(pathlib.Path(paev).read_text(encoding="utf-8"))
    for x in firmad:
        lyhi = x.get("lyhinimi") or lyhinimi(x["nimi"])
        piirkond, piirkond_kus, linn_kus = asukoht(x["aadress"])
        s = x.get("slug") or slugify(lyhi)
        try:
            tootajaid = int(x["tootajaid"] or 0)
        except ValueError:
            tootajaid = 0
        andmed = {
            "nimi": x["nimi"], "lyhinimi": lyhi, "vorm": x.get("vorm", "OÜ"), "registrikood": x["registrikood"],
            "emtak": x["emtak_kood"], "telefonid": [t.strip() for t in x["telefon"].split(";") if t.strip()],
            "email": x["email"].split(";")[0].strip(), "piirkond": piirkond, "piirkond_kus": piirkond_kus,
            "linn_kus": linn_kus, "aasta": (x.get("registreeritud") or "")[-4:], "tootajaid": tootajaid or None,
            "sissejuhatus": sissejuhatus(x.get("teenused_voti") or x["emtak_kood"], piirkond_kus), "pakett": x["pakett"],
            "kategooria": "auto" if x["emtak_kood"].startswith(("9531", "452")) else "viimistlus",
            "teenused_voti": x.get("teenused_voti", ""),
            "kujundus": x["kujundus"], "domeen": x.get("domeen", ""), "kaive": x.get("kaive", ""),
        }
        (juur / "andmed" / f"{s}.json").write_text(json.dumps(andmed, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(s, x["pakett"], x["kujundus"])


if __name__ == "__main__":
    main(sys.argv[1])
