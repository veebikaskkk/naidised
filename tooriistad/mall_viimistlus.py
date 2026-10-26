"""Viimistlusfirmade näidislehe mall.

Sisend: andmed/<slug>.json, väljund: public/<slug>/index.html ja public/<slug>/stiil.css.
HTML-i käsitsi ei muudeta, muuda andmeid või seda malli ja jooksuta genereeri.py uuesti.

Kujunduse eripära: avaplokk on värviline krohvisein, mille peal on pahteldatud
sile paneel, ja selle alumises servas on teenused värvikaartidena. Iga firma saab
registrikoodi järgi ühe palettidest, nii et kaks naabrit ei näe ühesugused välja.
"""
import html

E = html.escape

# Teenused EMTAK koodi alguse järgi. Ainult üldised kirjeldused, ei mingeid lubadusi.
TEENUSED = {
    "43311": ("Krohv ja pahtel, mis jäävad sirgeks.", "krohv", "Krohvime ja pahteldame seinu ja lagesid {piirkond_kus}: korterites, eramutes ja ärihoonetes. Pind jääb värvimiseks või tapeedi alla valmis.", [
        ("Krohvimine", "Seinte ja lagede tasandamine lubi-, tsement- ja kipskrohviga. Sobib nii uusehitisse kui ka vanasse majja."),
        ("Pahteldus", "Sile pind värvimiseks või tapeedi alla. Siledusaste lepitakse kokku enne tööde algust."),
        ("Värvimine", "Seinte ja lagede kruntimine ja värvimine, sealhulgas niisked ruumid."),
        ("Dekoratiivkrohv", "Struktuur- ja dekoratiivkrohvid, kui sein peab olema rohkem kui lihtsalt sile."),
    ]),
    "4333": ("Põrandad ja plaadid, mis on paigas.", "plaat", "Paigaldame põrandaid ja plaaditame vannitubasid, kööke ja esikuid {piirkond_kus}. Aluspind tehakse enne korda, et kate jääks sirge.", [
        ("Plaatimine", "Põranda- ja seinaplaatide paigaldus vannitubadesse, kööki ja esikusse."),
        ("Niisked ruumid", "Hüdroisolatsioon ja plaatimine duširuumides ja saunades."),
        ("Puitpõrandad", "Parketi, laudise ja laminaadi paigaldus koos liistudega."),
        ("Aluspõrand", "Aluspinna tasandamine, et kate jääks sirge ja kestaks."),
    ]),
    "4334": ("Värv, mis jääb ühtlane.", "varv", "Värvime siseruume ja fassaade {piirkond_kus}. Enne värvi teeme pinna korda, sest just sellest sõltub, kui kaua tulemus vastu peab.", [
        ("Siseviimistlus", "Seinte ja lagede ettevalmistus, kruntimine ja värvimine."),
        ("Pahteldus", "Pragude ja aukude parandus ning pinna lihvimine enne värvi."),
        ("Fassaadid", "Puit- ja krohvfassaadide puhastus, kruntimine ja värvimine."),
        ("Klaasitööd", "Klaaside paigaldus ja vahetus akendes, ustes ja vaheseintes."),
    ]),
    "4332": ("Aknad, uksed ja trepid õigesse kohta.", "puit", "Paigaldame aknaid, uksi ja treppe {piirkond_kus} ning viimistleme palged ja liistud nii, et paigaldusest jälge ei jääks.", [
        ("Aknad", "Uute akende paigaldus ja vanade vahetus koos tihendamise ja palede viimistlusega."),
        ("Uksed", "Sise- ja välisuste paigaldus ning lengide ja liistude viimistlus."),
        ("Trepid", "Puittreppide ja trepiastmete paigaldus."),
        ("Puusepatööd", "Liistud, aknalauad ja muud viimistluse puusepatööd."),
    ]),
    "433": ("Siseviimistlus algusest lõpuni.", "krohv", "Teeme siseviimistlust {piirkond_kus}: pahteldame, värvime, plaaditame ja paigaldame põrandaid. Võid tellida kogu remondi või ainult ühe etapi.", [
        ("Värvimine", "Seinte ja lagede ettevalmistus, pahteldus ja värvimine."),
        ("Plaatimine", "Põranda- ja seinaplaatide paigaldus vannitubadesse ja kööki."),
        ("Põrandad", "Parketi, laminaadi ja muude põrandakatete paigaldus."),
        ("Viimistlus", "Liistud, uksed ja väiksemad tööd, mis teevad ruumi valmis."),
    ]),
}

# Üldise viimistluse pealkiri vaheldub, et naaberfirmade lehed ei kordaks üksteist.
VAHELDUS = {"Siseviimistlus algusest lõpuni.": ["Siseviimistlus algusest lõpuni.", "Seinad, laed ja põrandad korda."]}

SAMMUD = [
    ("Ülevaatus", "Tuleme kohale, vaatame pinnad üle ja mõõdame."),
    ("Hinnapakkumine", "Saad kirjaliku pakkumise koos materjalide ja ajakavaga."),
    ("Ettevalmistus", "Katame põrandad, aknad ja mööbli ning teeme aluspinna korda."),
    ("Töö", "Teeme töö kokkulepitud kvaliteedi ja ajakava järgi."),
    ("Üleandmine", "Koristame enda järelt ja vaatame tulemuse koos üle."),
]

# Paletid: tume, keskmine, hele, toon (taust), kiir (väike aktsent).
# Valge tekst tumedal ja keskmisel, tume tekst helel ja toonil (kontroll.py arvutab üle).
PALETID = {
    "sinine": ("#1C3D87", "#3A62B5", "#A9BFE8", "#EAF0FA", "#F2B630"),
    "sammal": ("#22553A", "#3B7A53", "#A3CCAE", "#E8F3EB", "#F2B630"),
    "ploom": ("#55286B", "#7E4A98", "#CBB0D9", "#F3ECF7", "#F2B630"),
    "petrool": ("#11585E", "#22737A", "#9DCFD2", "#E5F3F3", "#F2B630"),
    "kirss": ("#842234", "#AE4255", "#E8B3BC", "#F9ECEE", "#F2B630"),
}

TEKSTUURID = {
    "krohv": ('0.012 0.03', 5, 7, 3.2),
    "plaat": ('0.05 0.05', 3, 4, 1.4),
    "varv": ('0.002 0.05', 3, 9, 1.6),
    "puit": ('0.004 0.12', 4, 2, 2.2),
}


def teenused_koodi_jargi(emtak):
    for pikkus in (5, 4, 3):
        if emtak[:pikkus] in TEENUSED:
            return TEENUSED[emtak[:pikkus]]
    return TEENUSED["433"]


def tel_link(t):
    return "+" + "".join(c for c in t if c.isdigit())


def tel_ilus(t):
    d = "".join(c for c in t if c.isdigit())
    if d.startswith("372"):
        d = d[3:]
        return "+372 " + (d[:4] + " " + d[4:] if len(d) == 8 else d[:3] + " " + d[3:])
    return t


def palett(a):
    nimed = sorted(PALETID)
    return a.get("palett") or nimed[int(a["registrikood"]) % len(nimed)]


def ehita(a):
    pealkiri, tekstuur, sissejuhatus, teenused = teenused_koodi_jargi(a["emtak"])
    if pealkiri in VAHELDUS:
        pealkiri = VAHELDUS[pealkiri][int(a["registrikood"]) % len(VAHELDUS[pealkiri])]
    pal = palett(a)
    tume, kesk, hele, toon, kiir = PALETID[pal]
    nimi = a["nimi"]
    lyhinimi = a.get("lyhinimi", nimi)
    tel = a["telefonid"]
    piirkond = a["piirkond"]
    sissejuhatus = a.get("sissejuhatus") or sissejuhatus.format(piirkond_kus=a["piirkond_kus"])
    bf, okt, seed, sk = TEKSTUURID[tekstuur]

    kaardivarvid = ["k1", "k2", "k3", "k4"]
    kaardid_html = "\n".join(
        f'        <a class="kaart {kaardivarvid[i]}" href="#teenused"><span class="kaart-varv"></span><span class="kaart-nimi">{E(t)}</span></a>'
        for i, (t, _) in enumerate(teenused)
    )
    teenuste_html = "\n".join(
        f'      <article class="teenus {kaardivarvid[i]}"><div class="teenus-varv" aria-hidden="true"></div><h3>{E(t)}</h3><p>{E(k)}</p></article>'
        for i, (t, k) in enumerate(teenused)
    )
    sammud_html = "\n".join(
        f'      <li><span class="nr">{i}</span><h3>{E(t)}</h3><p>{E(k)}</p></li>'
        for i, (t, k) in enumerate(SAMMUD, 1)
    )
    pildid_html = "\n".join(
        f'      <div class="kohataide" role="img" aria-label="Kohatäide: teie töö foto {i}"><span>pildid/too-{i:02d}.webp</span></div>'
        for i in range(1, 7)
    )
    faktid = []
    if a.get("aasta"):
        faktid.append((a["aasta"], "asutamise aasta"))
    if a.get("tootajaid"):
        faktid.append((str(a["tootajaid"]), "inimest meeskonnas"))
    faktid.append((piirkond, "tööpiirkond"))
    faktid_html = "\n".join(f'      <div><dt>{E(v)}</dt><dd>{E(s)}</dd></div>' for v, s in faktid)
    telefonid_html = "<br>".join(f'<a href="tel:{tel_link(t)}">{E(tel_ilus(t))}</a>' for t in tel)

    index = f"""<!doctype html>
<html lang="et">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{E(lyhinimi)} – {E(teenused[0][0].lower())} {E(a["linn_kus"])}</title>
<meta name="description" content="{E(nimi)}: {E(", ".join(t[0].lower() for t in teenused[:3]))}. Tööpiirkond {E(piirkond)}.">
<meta name="theme-color" content="{tume}">
<link rel="preload" href="/fondid/interdisplay-extrabold.woff" as="font" type="font/woff" crossorigin>
<link rel="stylesheet" href="stiil.css">
</head>
<body>

<div class="teip" role="note">
  <div class="wrap">
    <span>See on näidisleht, mille tegi Veebikask firmale {E(nimi)}. Sisu põhineb avalikel andmetel.</span>
    <a href="https://veebikask.ee">veebikask.ee</a>
  </div>
</div>

<header class="top">
  <div class="wrap">
    <a class="logo" href="#algus"><span class="logo-mark" aria-hidden="true"></span>{E(lyhinimi)}</a>
    <nav aria-label="Peamenüü">
      <a href="#teenused">Teenused</a>
      <a href="#tood">Tööd</a>
      <a class="nav-nupp" href="#kontakt">Kontakt</a>
    </nav>
  </div>
</header>

<main id="algus">
<section class="sein" aria-labelledby="pealkiri">
  <svg class="tekstuur" aria-hidden="true" focusable="false" preserveAspectRatio="none">
    <filter id="pind" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="{bf}" numOctaves="{okt}" seed="{seed}"/><feDiffuseLighting surfaceScale="{sk}" lighting-color="{kesk}"><feDistantLight azimuth="200" elevation="40"/></feDiffuseLighting></filter>
    <rect width="100%" height="100%" filter="url(#pind)"/>
  </svg>
  <div class="paneel">
    <div class="paneel-sisu">
      <p class="ettevote">{E(nimi)}</p>
      <h1 id="pealkiri">{E(pealkiri)}</h1>
      <p class="lead">{E(sissejuhatus)}</p>
      <div class="nupud">
        <a class="nupp pea" href="tel:{tel_link(tel[0])}">Helista {E(tel_ilus(tel[0]).replace("+372 ", ""))}</a>
        <a class="nupp teine" href="#kontakt">Küsi hinnapakkumist</a>
      </div>
    </div>
  </div>
  <div class="kaardid-rida">
    <div class="wrap">
      <div class="kaardid">
{kaardid_html}
      </div>
    </div>
  </div>
</section>

<section id="teenused" class="plokk" aria-labelledby="teenused-pealkiri">
  <div class="wrap">
    <h2 id="teenused-pealkiri">Teenused</h2>
    <p class="sissejuhatus">Võid tellida kogu töö või ainult ühe etapi.</p>
    <div class="teenused">
{teenuste_html}
    </div>
  </div>
</section>

<section id="tood" class="plokk tood" aria-labelledby="tood-pealkiri">
  <div class="wrap">
    <h2 id="tood-pealkiri">Tehtud tööd</h2>
    <p class="sissejuhatus">Siia tulevad teie enda tööde fotod. Pildid müüvad viimistlustööd paremini kui ükski tekst.</p>
    <div class="galerii">
{pildid_html}
    </div>
  </div>
</section>

<section class="plokk kaik" aria-labelledby="kaik-pealkiri">
  <div class="wrap">
    <h2 id="kaik-pealkiri">Kuidas töö käib</h2>
    <p class="sissejuhatus">Enne alustamist tead, mida teeme, kui kaua see võtab ja mis see maksab.</p>
    <ol class="sammud">
{sammud_html}
    </ol>
  </div>
</section>

<section class="plokk miks" aria-labelledby="miks-pealkiri">
  <div class="wrap">
    <h2 id="miks-pealkiri">{E(lyhinimi)} lühidalt</h2>
    <dl class="faktid">
{faktid_html}
    </dl>
  </div>
</section>

<section id="kontakt" class="plokk kontakt" aria-labelledby="kontakt-pealkiri">
  <div class="wrap">
    <h2 id="kontakt-pealkiri">Küsi hinnapakkumist</h2>
    <p class="sissejuhatus">Helista või kirjuta. Kirjelda lühidalt, mis ruumiga on tegu ja kui suurt pinda töö puudutab.</p>
    <a class="suur-tel" href="tel:{tel_link(tel[0])}">{E(tel_ilus(tel[0]))}</a>
    <dl class="kontaktid">
      <div><dt>Telefon</dt><dd>{telefonid_html}</dd></div>
      <div><dt>E-post</dt><dd><a href="mailto:{E(a["email"])}">{E(a["email"])}</a></dd></div>
      <div><dt>Piirkond</dt><dd>{E(piirkond)}</dd></div>
    </dl>
  </div>
</section>
</main>

<footer>
  <div class="wrap">
    <p>{E(nimi)}, registrikood {E(a["registrikood"])}<br>Tööpiirkond {E(piirkond)}<br><a href="tel:{tel_link(tel[0])}">{E(tel_ilus(tel[0]))}</a>, <a href="mailto:{E(a["email"])}">{E(a["email"])}</a></p>
    <p>Näidisleht: <a href="https://veebikask.ee">Veebikask</a></p>
  </div>
</footer>
</body>
</html>
"""
    css = (STIIL.replace("__TUME__", tume).replace("__KESK__", kesk).replace("__HELE__", hele)
           .replace("__TOON__", toon).replace("__KIIR__", kiir))
    return index, css


STIIL = """@font-face{font-family:"Inter";src:url("/fondid/inter-regular.woff") format("woff");font-weight:400;font-display:swap}
@font-face{font-family:"Inter";src:url("/fondid/inter-semibold.woff") format("woff");font-weight:600;font-display:swap}
@font-face{font-family:"Inter Display";src:url("/fondid/interdisplay-extrabold.woff") format("woff");font-weight:800;font-display:swap}
:root{
  --tume:__TUME__;
  --kesk:__KESK__;
  --hele:__HELE__;
  --toon:__TOON__;
  --kiir:__KIIR__;
  --taust:#FBFBFA;
  --tekst:#1F2328;
  --vaiketekst:#4A5157;
  --paise-korgus:84px;
}
*{box-sizing:border-box}
[hidden]{display:none !important}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{margin:0;background:var(--taust);color:var(--tekst);font-family:"Inter",system-ui,sans-serif;font-size:17px;line-height:1.55}
a{color:inherit;text-underline-offset:4px}
:focus-visible{outline:3px solid var(--kiir);outline-offset:3px}
.wrap{max-width:1160px;margin:0 auto;padding:0 24px}
section[id]{scroll-margin-top:16px}
h1,h2{font-family:"Inter Display","Inter",system-ui,sans-serif;font-weight:800;letter-spacing:-.025em}

.teip{background:var(--tekst);color:#fff;font-size:14px;line-height:1.4;position:relative;z-index:3}
.teip .wrap{display:flex;gap:16px;justify-content:space-between;align-items:center;padding-top:9px;padding-bottom:9px;flex-wrap:wrap}
.teip a{color:#fff;font-weight:600}

header.top{position:absolute;left:0;right:0;z-index:2;color:#fff}
header.top .wrap{display:flex;justify-content:space-between;align-items:center;min-height:var(--paise-korgus)}
.logo{display:inline-flex;align-items:center;gap:10px;font-family:"Inter Display","Inter",sans-serif;font-weight:800;font-size:22px;letter-spacing:-.01em;text-decoration:none;min-height:44px}
.logo-mark{width:22px;height:22px;border-radius:5px;background:linear-gradient(135deg,var(--kiir) 0 50%,#fff 50% 100%)}
nav a{display:inline-flex;align-items:center;min-height:44px;padding:0 12px;font-weight:600;font-size:15px;text-decoration:none}
nav a:hover{text-decoration:underline}
.nav-nupp{background:#fff;color:var(--tume);border-radius:999px;margin-left:8px;padding:0 18px}
.nav-nupp:hover{text-decoration:none;background:var(--kiir);color:var(--tekst)}

/* Avaplokk: värviline krohvisein ja pahteldatud paneel */
.sein{position:relative;background:var(--tume);color:var(--tekst);padding-top:calc(var(--paise-korgus) + 48px);overflow:hidden}
.sein svg.tekstuur{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;opacity:.9}
.paneel{position:relative;max-width:1160px;margin:0 auto;padding:0 24px}
.paneel-sisu{background:var(--taust);max-width:640px;margin-left:auto;margin-bottom:32px;padding:48px 48px 56px;border-radius:4px;
  box-shadow:0 30px 60px -30px rgba(0,0,0,.45)}
.ettevote{margin:0 0 14px;font-weight:600;font-size:15px;color:var(--tume)}
h1{font-size:clamp(38px,5.4vw,66px);line-height:1;margin:0 0 20px;color:var(--tume)}
.lead{font-size:18.5px;max-width:32em;margin:0 0 30px;color:#363C41}
.nupud{display:flex;gap:12px;flex-wrap:wrap}
.nupp{display:inline-flex;align-items:center;min-height:52px;padding:0 24px;font-weight:600;font-size:16px;text-decoration:none;border-radius:999px}
.nupp.pea{background:var(--tume);color:#fff}
.nupp.pea:hover{background:var(--tekst)}
.nupp.teine{border:2px solid var(--tume);color:var(--tume)}
.nupp.teine:hover{background:var(--toon)}

/* Värvikaardid avaploki allservas */
.kaardid-rida{position:relative;background:linear-gradient(var(--tume) 0 44px,var(--taust) 44px)}
.kaardid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;padding:0}
.kaart{display:flex;flex-direction:column;text-decoration:none;background:#fff;border-radius:4px;overflow:hidden;min-height:44px;box-shadow:0 10px 24px -14px rgba(0,0,0,.35)}
.kaart{padding:5px 5px 0}
.kaart-varv{display:block;height:60px;border-radius:2px}
.kaart-nimi{padding:11px 9px 12px;font-weight:600;font-size:15px}
.kaart:hover .kaart-nimi{text-decoration:underline}
.k1 .kaart-varv,.k1 .teenus-varv{background:var(--tume)}
.k2 .kaart-varv,.k2 .teenus-varv{background:var(--kesk)}
.k3 .kaart-varv,.k3 .teenus-varv{background:var(--hele)}
.k4 .kaart-varv,.k4 .teenus-varv{background:var(--kiir)}

.plokk{padding:96px 0}
h2{font-size:clamp(28px,3.4vw,42px);line-height:1.05;margin:0 0 14px;color:var(--tume)}
.sissejuhatus{max-width:36em;color:var(--vaiketekst);margin:0 0 44px}

.teenused{display:grid;grid-template-columns:repeat(4,1fr);gap:24px}
.teenus{background:#fff;border:1px solid #E1E4E6;border-radius:4px;overflow:hidden;padding:0 22px 26px}
.teenus-varv{height:120px;margin:0 -22px 20px}
.teenus h3{font-size:19px;font-weight:600;margin:0 0 8px}
.teenus p{margin:0;font-size:15.5px;color:var(--vaiketekst)}

.tood{background:var(--toon)}
.galerii{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.kohataide{aspect-ratio:4/3;display:flex;align-items:center;justify-content:center;padding:12px;border-radius:4px;
  background:repeating-linear-gradient(135deg,rgba(255,255,255,.55) 0 14px,rgba(255,255,255,.15) 14px 28px),var(--hele)}
.kohataide span{background:#fff;padding:4px 10px;font-size:14px;color:var(--vaiketekst);overflow-wrap:anywhere;border-radius:2px}

.kaik{background:var(--tume);color:#fff}
.kaik h2{color:#fff}
.kaik .sissejuhatus{color:#fff;opacity:.88}
.sammud{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(5,1fr);gap:14px}
.sammud li{background:rgba(255,255,255,.08);border-top:4px solid var(--kiir);padding:22px 20px 24px;border-radius:0 0 4px 4px}
.sammud .nr{font-family:"Inter Display","Inter",sans-serif;font-weight:800;font-size:28px;line-height:1;color:var(--kiir);display:block;margin-bottom:12px}
.sammud h3{font-size:18px;font-weight:600;margin:0 0 6px}
.sammud p{margin:0;font-size:15px;opacity:.88}

.faktid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin:28px 0 0}
.faktid div{background:var(--toon);padding:24px;border-radius:4px}
.faktid dt{font-family:"Inter Display","Inter",sans-serif;font-weight:800;font-size:clamp(26px,3vw,38px);letter-spacing:-.02em;line-height:1.1;color:var(--tume)}
.faktid dd{margin:6px 0 0;color:var(--vaiketekst)}

.kontakt{background:var(--kesk);color:#fff}
.kontakt h2{color:#fff}
.kontakt .sissejuhatus{color:#fff;opacity:.92}
.suur-tel{display:inline-block;font-family:"Inter Display","Inter",sans-serif;font-weight:800;font-size:clamp(36px,6vw,72px);letter-spacing:-.03em;line-height:1.05;text-decoration:none;margin:0 0 36px;border-bottom:4px solid var(--kiir)}
.suur-tel:hover{border-bottom-color:#fff}
.kontaktid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:0}
.kontaktid div{background:rgba(255,255,255,.12);padding:20px 22px;border-radius:4px}
.kontaktid dt{font-size:15px;margin-bottom:6px;opacity:.9}
.kontaktid dd{margin:0;font-weight:600;font-size:18px;overflow-wrap:anywhere}
.kontaktid a{display:inline-block;min-height:44px;line-height:44px}

footer{padding:28px 0;font-size:14px;color:var(--vaiketekst)}
footer .wrap{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}
footer p{margin:0}

@media (max-width:1024px){
  .teenused{grid-template-columns:repeat(2,1fr)}
  .sammud{grid-template-columns:repeat(3,1fr)}
}
@media (max-width:768px){
  .paneel-sisu{padding:32px 24px 40px;margin-left:0}
  .kaardid{grid-template-columns:repeat(2,1fr)}
  .galerii{grid-template-columns:repeat(2,1fr)}
  .sammud{grid-template-columns:1fr}
  .faktid,.kontaktid{grid-template-columns:1fr;gap:12px}
  nav a:not(.nav-nupp){display:none}
}
@media (max-width:480px){
  body{font-size:16px}
  .wrap,.paneel{padding:0 16px}
  .sein{padding-top:calc(var(--paise-korgus) + 16px)}
  .paneel-sisu{padding:28px 20px 34px}
  .plokk{padding:72px 0}
  .teenused{grid-template-columns:1fr}
  .teenus-varv{height:72px}
  .kaart-varv{height:40px}
  .kohataide span{font-size:12px}
}
"""
