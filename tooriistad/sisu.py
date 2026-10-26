"""Näidislehtede sisu: teenused tegevusala järgi, töö käik ja abifunktsioonid.

Ainult üldised kirjeldused. Ei mingeid lubadusi, garantiisid, hindu ega aastaid,
mida firma ise ei ole avaldanud.
"""
import html
import re

E = html.escape

# Teenus: (nimi, lühikirjeldus, pikk kirjeldus teenuste lehele)
TEENUSED = {
    "43311": [
        ("Krohvimine", "Seinte ja lagede tasandamine lubi-, tsement- ja kipskrohviga.",
         "Krohvime seinu ja lagesid nii uusehitistes kui ka vanades majades. Krohvi tüüp valitakse aluspinna ja ruumi järgi: kuiva ruumi jaoks üks, niiske ja vana müüri jaoks teine. Enne tööd vaatame aluspinna üle ja lepime kokku, milline peab tulemus olema."),
        ("Pahteldus", "Sile pind värvimiseks või tapeedi alla.",
         "Pahteldame ja lihvime pinnad kokkulepitud siledusastmeni. Mida rohkem valgust seinale langeb, seda siledam peab pind olema, ja see lepitakse kokku enne tööde algust. Pind jääb valmis värviks või tapeediks."),
        ("Värvimine", "Seinte ja lagede kruntimine ja värvimine.",
         "Krundime ja värvime seinad ja laed, sealhulgas niisked ruumid. Värvi ja läike valime koos tellijaga ruumi kasutuse järgi. Enne värvimist katame põrandad ja mööbli."),
        ("Dekoratiivkrohv", "Struktuur- ja dekoratiivkrohvid.",
         "Kui sein peab olema rohkem kui lihtsalt sile, teeme struktuur- ja dekoratiivkrohvi. Enne suure pinna tegemist teeme väikese proovi, et tellija näeks tekstuuri ja tooni oma silmaga."),
    ],
    "4333": [
        ("Plaatimine", "Põranda- ja seinaplaatide paigaldus.",
         "Paigaldame põranda- ja seinaplaate vannitubadesse, kööki, esikusse ja saunadesse. Plaatide paigutus ja vuugi laius lepitakse kokku enne tööd, et lõiked jääksid sinna, kus neid on kõige vähem näha."),
        ("Niisked ruumid", "Hüdroisolatsioon ja plaatimine duširuumides.",
         "Niiske ruumi puhul on kõige olulisem see osa, mida pärast enam ei näe: hüdroisolatsioon ja põranda kalle trapi suunas. Teeme need enne plaatimist korralikult ära."),
        ("Põrandad", "Parketi, laudise, vinüüli ja laminaadi paigaldus.",
         "Paigaldame puit-, vinüül- ja laminaatpõrandaid koos aluskatte ja liistudega. Enne paigaldust kontrollime aluspinna niiskust ja tasasust."),
        ("Aluspinna tasandamine", "Põranda tasandamine enne katet.",
         "Kõver aluspind paistab läbi igast kattest. Tasandame põranda isetasanduva seguga või vajadusel muul moel, et kate jääks sirge ja kestaks."),
    ],
    "4334": [
        ("Siseviimistlus", "Seinte ja lagede ettevalmistus ja värvimine.",
         "Valmistame seinad ja laed ette, krundime ja värvime. Värvi ja läike valime ruumi kasutuse järgi ning katame enne tööd põrandad ja mööbli."),
        ("Pahteldus", "Pragude parandus ja pinna lihvimine.",
         "Parandame praod ja augud, pahteldame ja lihvime pinna enne värvi. Just ettevalmistusest sõltub, kui ühtlane ja vastupidav värvitud pind lõpuks on."),
        ("Fassaadid", "Puit- ja krohvfassaadide värvimine.",
         "Puhastame, krundime ja värvime puit- ja krohvfassaade. Fassaadi värvime sobiva ilmaga, sest liiga külm või niiske ilm rikub tulemuse."),
        ("Klaasitööd", "Klaaside paigaldus ja vahetus.",
         "Paigaldame ja vahetame klaase akendes, ustes ja vaheseintes. Mõõdame klaasi kohapeal ja lepime kokku paigaldusaja."),
    ],
    "433": [
        ("Pahteldus ja värvimine", "Seinte ja lagede ettevalmistus ja värvimine.",
         "Pahteldame, lihvime ja värvime seinad ja laed. Enne tööd katame põrandad ja mööbli ning pärast koristame enda järelt."),
        ("Plaatimine", "Põranda- ja seinaplaatide paigaldus.",
         "Plaadime vannitubasid, köökide tagaseinu ja esikuid. Niisketes ruumides teeme enne plaatimist hüdroisolatsiooni."),
        ("Põrandad", "Parketi, laminaadi ja vinüüli paigaldus.",
         "Paigaldame põrandakatteid koos aluskatte ja liistudega. Vajadusel tasandame aluspinna enne paigaldust."),
        ("Remondi lõpetamine", "Liistud, uksed ja väiksemad tööd.",
         "Paigaldame liistud, uksed ja muud detailid, mis teevad ruumi valmis. Võid tellida kogu remondi või ainult viimase etapi."),
    ],
}

TEENUSED.update({
    "95311": [
        ("Hooldus", "Õli- ja filtrivahetus ning korraline hooldus.",
         "Teeme korralise hoolduse tootja nõuete järgi: õli ja filtrid, vedelikud, pidurite ja veermiku ülevaatus. Kui märkame midagi, mis vajab tähelepanu, ütleme enne, kui midagi juurde teeme."),
        ("Diagnostika", "Veakoodide lugemine ja rikke otsimine.",
         "Loeme veakoodid ja otsime rikke põhjuse, enne kui midagi vahetame. Nii maksad ainult selle eest, mis päriselt katki on."),
        ("Remont", "Mootor, veermik, pidurid ja elektrisüsteem.",
         "Remondime mootori, veermiku, pidurite ja elektrisüsteemi rikkeid. Enne töö algust lepime kokku, mida tehakse ja mis see maksab."),
        ("Rehvitööd", "Rehvivahetus ja tasakaalustamine.",
         "Vahetame ja tasakaalustame rehvid ning kontrollime samal ajal pidureid ja veermikku. Hooaja vahetuse ajaks tasub aeg varakult kokku leppida."),
    ],
    "95311-rehv": [
        ("Rehvivahetus", "Suve- ja talverehvide vahetus.",
         "Vahetame rehvid ja kontrollime samal ajal rehvirõhku, mustri sügavust ja velgede seisukorda. Hooaja vahetuse ajaks tasub aeg varakult kokku leppida."),
        ("Tasakaalustamine", "Rataste tasakaalustamine.",
         "Tasakaalustame rattad, et auto ei vibreeriks ja rehvid kuluksid ühtlaselt."),
        ("Rehvide parandus", "Augu parandus ja ventiilide vahetus.",
         "Parandame torke ja vahetame ventiilid. Kui rehvi ei saa enam ohutult parandada, ütleme seda ausalt."),
        ("Hooldus", "Väiksemad hooldus- ja remonditööd.",
         "Samal käigul saab teha ka väiksemaid hooldustöid. Lepime enne kokku, mida tehakse."),
    ],
    "95311-kere": [
        ("Kereremont", "Kereosade parandus ja vahetus.",
         "Parandame ja vahetame kereosi pärast avariid või roostet. Enne tööd vaatame kahju üle ja lepime hinna kokku."),
        ("Värvimine", "Detailide ja terve auto värvimine.",
         "Värvime üksikuid detaile või terve auto. Värvitooni sobitame auto olemasoleva värviga."),
        ("Mõlkide parandus", "Väiksemate mõlkide ja kriimude parandus.",
         "Parandame väiksemad mõlgid ja kriimud, et auto näeks jälle korras välja."),
        ("Kindlustusjuhtumid", "Abi kindlustusjuhtumi remondiga.",
         "Kui kahju hüvitab kindlustus, aitame remondi kalkulatsiooniga ja lepime tööd kokku."),
    ],
    "95311-detail": [
        ("Välispesu", "Põhjalik käsitsipesu.",
         "Peseme auto käsitsi ja puhastame ka kohad, kuhu automaatpesula ei ulatu."),
        ("Poleerimine", "Värvipinna poleerimine.",
         "Poleerime värvipinna, et kriimud ja tuhmus kaoksid ning värv saaks tagasi oma läike."),
        ("Salongi puhastus", "Istmete, põrandate ja paneelide puhastus.",
         "Puhastame salongi: istmed, põrandakatted, paneelid ja aknad seestpoolt."),
        ("Kaitsevaha", "Värvipinna kaitse.",
         "Pärast pesu ja poleerimist kaitseb vaha värvipinda ilmastiku ja mustuse eest."),
    ],
})

TEENUSED["96211"] = [
    ("Lõikus", "Naiste, meeste ja laste juukselõikus.",
     "Lõikame naiste, meeste ja laste juukseid. Enne lõikust räägime läbi, mida soovid, ja vaatame, mis sinu juustele ja näokujule sobib. Kui sul on pilt soovitud soengust, too see kaasa."),
    ("Värvimine", "Toonimine, värvimine ja triibud.",
     "Värvime ja toonime juukseid ning teeme triipe. Tooni valime koos sinuga ja räägime enne läbi, kui palju aega töö võtab ja kuidas värvi hiljem hoida."),
    ("Soengud", "Pidulikud ja igapäevased soengud.",
     "Teeme soenguid pidupäevaks, pulmaks ja tavaliseks päevaks. Pidulikule soengule on hea tulla puhaste ja kuivade juustega."),
    ("Juuksehooldus", "Hooldused kuivadele ja kahjustatud juustele.",
     "Teeme juuksehooldusi ja soovitame, kuidas juukseid kodus hoida. Ütleme ausalt, milline hooldus sinu juustele päriselt vajalik on."),
]
TEENUSED["96211-meeste"] = [
    ("Meeste lõikus", "Kääride ja masinaga lõikus.",
     "Lõikame meeste juukseid kääride ja masinaga. Enne lõikust räägime läbi, kui lühikeseks ja mis kujuga, et tulemus oleks just selline, nagu soovid."),
    ("Masinalõikus", "Kiire ja ühtlane lõikus masinaga.",
     "Kui soovid lihtsat ja kiiret lõikust, teeme selle masinaga ühtlase pikkusega või üleminekuga."),
    ("Habe", "Habeme piiramine ja kujundamine.",
     "Piirame ja kujundame habet, et see sobiks näokuju ja soenguga kokku."),
    ("Laste lõikus", "Juukselõikus lastele.",
     "Lõikame ka laste juukseid. Võtame aega, et lapsel oleks toolis rahulik olla."),
]
TEENUSED["43211"] = [
    ("Elektripaigaldus", "Juhtmestik majadesse, korteritesse ja äripindadele.",
     "Ehitame uut elektripaigaldist ja uuendame vana: juhtmestik, pistikupesad, lülitid ja ühendused. Enne tööd vaatame objekti üle ja lepime kokku, kuhu mis tuleb."),
    ("Elektrikilbid", "Kilpide paigaldus ja vahetus.",
     "Paigaldame ja vahetame elektrikilpe ning kaitselüliteid. Vana kilbi vahetus on sageli esimene samm, kui maja elekter vajab uuendamist."),
    ("Valgustus", "Sise- ja välisvalgustuse paigaldus.",
     "Paigaldame laevalgustid, süvisvalgustid, LED-ribad ja välisvalgustuse. Valgustuse asukohad lepime kokku enne, kui seinad kinni pannakse."),
    ("Rikked ja remont", "Rikete otsimine ja parandus.",
     "Kui kaitse lööb välja või midagi ei tööta, otsime rikke põhjuse üles ja parandame selle. Ütleme enne parandust, mida on vaja teha."),
]

SAMMUD_JUUKSUR = [
    ("Broneering", "Vali kalendrist teenus ja sobiv aeg või helista."),
    ("Kinnitus", "Kinnitame aja telefoni või e-posti teel."),
    ("Jutuajamine", "Enne tööd räägime läbi, mida soovid."),
    ("Töö", "Teeme kokkulepitud töö rahulikult ja hoolikalt."),
    ("Nõuanne", "Soovitame, kuidas tulemust kodus hoida."),
]
SAMMUD_ELEKTER = [
    ("Ülevaatus", "Vaatame objekti üle ja kuulame, mida on vaja."),
    ("Pakkumine", "Saad pakkumise koos töömahu ja ajakavaga."),
    ("Töö", "Teeme töö kokkulepitud ajal ja koristame enda järelt."),
    ("Kontroll", "Kontrollime enne üleandmist, et kõik töötab."),
    ("Üleandmine", "Anname töö üle ja räägime läbi, mida tehti."),
]

KATEGOORIAD = {
    "viimistlus": dict(
        tood="Siia tulevad teie enda tööde fotod. Viimistlustööd müüvad pildid paremini kui ükski tekst.",
        kontakt="Helista või kirjuta. Kirjelda lühidalt, mis ruumiga on tegu ja kui suurt pinda töö puudutab.",
        vorm_naide="Näiteks: kahetoaline korter, seinad umbes 120 m²",
        teeb="teeb siseviimistlust",
        sammud="viimistlus"),
    "auto": dict(
        tood="Siia tulevad teie töökoja ja tehtud tööde fotod. Puhas töökoda ja korras autod räägivad enda eest.",
        kontakt="Helista või kirjuta. Ütle auto mark, mudel ja aasta ning kirjelda lühidalt, mis mure on.",
        vorm_naide="Näiteks: Toyota Avensis 2012, pidurid kriuksuvad",
        teeb="hooldab ja remondib autosid",
        sammud="auto"),
    "juuksur": dict(
        tood="Siia tulevad teie tehtud soengute ja salongi fotod. Juuksuri juurde tullakse piltide järgi.",
        kontakt="Helista, kirjuta või broneeri aeg kalendrist.",
        vorm_naide="",
        teeb="lõikab, värvib ja teeb soenguid",
        sammud="juuksur", kontakt_pk="Kontakt", nupp="Broneeri aeg", nupp_siht="#broneeri", tiitel="juuksur",
        teenused_sissejuhatus="Vali teenus ja broneeri aeg otse kalendrist.",
        kaik_sissejuhatus="Aja saad broneerida kalendrist, telefoni teel või kirjutades."),
    "elekter": dict(
        tood="Siia tulevad teie tehtud tööde fotod: kilbid, valgustus ja objektid.",
        kontakt="Helista või kirjuta. Kirjelda lühidalt, mis objektiga on tegu ja mida on vaja teha.",
        vorm_naide="Näiteks: eramaja, vaja vahetada elektrikilp ja lisada pistikupesi",
        teeb="teeb elektritöid",
        sammud="elekter", tiitel="elektritööd"),
}

SAMMUD_AUTO = [
    ("Aeg", "Helista või kirjuta ja lepime kokku sobiva aja."),
    ("Ülevaatus", "Vaatame auto üle ja leiame mure põhjuse."),
    ("Kooskõlastus", "Enne remonti ütleme, mida on vaja teha ja mis see maksab."),
    ("Töö", "Teeme kokkulepitud töö ja ei lisa midagi ilma sinu nõusolekuta."),
    ("Üleandmine", "Anname auto üle ja räägime läbi, mida tehti."),
]


def kat(a):
    return KATEGOORIAD[a.get("kategooria", "viimistlus")]


def sammud(a):
    return {"auto": SAMMUD_AUTO, "juuksur": SAMMUD_JUUKSUR, "elekter": SAMMUD_ELEKTER}.get(kat(a)["sammud"], SAMMUD)


SAMMUD = [
    ("Ülevaatus", "Tuleme kohale, vaatame pinnad üle ja mõõdame."),
    ("Pakkumine", "Saad kirjaliku pakkumise koos materjalide ja ajakavaga."),
    ("Ettevalmistus", "Katame põrandad, aknad ja mööbli ning teeme aluspinna korda."),
    ("Töö", "Teeme töö kokkulepitud kvaliteedi ja ajakava järgi."),
    ("Üleandmine", "Koristame enda järelt ja vaatame tulemuse koos üle."),
]


def teenused(emtak):
    if emtak in TEENUSED:
        return TEENUSED[emtak]
    for n in (5, 4, 3):
        if emtak[:n] in TEENUSED:
            return TEENUSED[emtak[:n]]
    return TEENUSED["433"]


def tel_link(t):
    return "+" + "".join(c for c in t if c.isdigit())


def tel_ilus(t):
    d = "".join(c for c in t if c.isdigit())
    if d.startswith("372"):
        d = d[3:]
        return "+372 " + (d[:4] + " " + d[4:] if len(d) == 8 else d[:3] + " " + d[3:])
    return t


def tel_lyhike(t):
    return tel_ilus(t).replace("+372 ", "")


def slugify(s):
    s = s.lower()
    for a, b in (("õ", "o"), ("ä", "a"), ("ö", "o"), ("ü", "u"), ("š", "s"), ("ž", "z")):
        s = s.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")
