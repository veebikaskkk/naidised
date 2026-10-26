"""Viimistlusfirmade näidislehe mall.

Sisend: andmed/<slug>.json, väljund: public/<slug>/index.html ja public/<slug>/stiil.css.
HTML-i käsitsi ei muudeta, muuda andmeid või seda malli ja jooksuta genereeri.py uuesti.
"""
import html

E = html.escape

# Teenused EMTAK koodi alguse järgi. Ainult üldised kirjeldused, ei mingeid lubadusi.
TEENUSED = {
    "43311": ("Krohv ja pahtel, mis jäävad sirgeks.", "krohv", [
        ("Krohvimine", "Seinte ja lagede tasandamine lubi-, tsement- ja kipskrohviga. Sobib nii uusehitisse kui ka vanasse majja."),
        ("Pahteldus ja lihvimine", "Sile pind värvimiseks või tapeedi alla. Siledusaste lepitakse kokku enne tööde algust."),
        ("Värvimine", "Seinte ja lagede kruntimine ja värvimine, sealhulgas niisked ruumid."),
        ("Dekoratiivkrohv", "Struktuur- ja dekoratiivkrohvid, kui sein peab olema rohkem kui lihtsalt sile."),
    ]),
    "4333": ("Põrandad ja plaadid, mis on paigas.", "plaat", [
        ("Plaatimine", "Põranda- ja seinaplaatide paigaldus vannitubadesse, kööki ja esikusse."),
        ("Niisked ruumid", "Hüdroisolatsioon ja plaatimine duširuumides ja saunades."),
        ("Puitpõrandad", "Parketi, laudise ja laminaadi paigaldus koos liistudega."),
        ("Aluspõrand", "Aluspinna tasandamine, et kate jääks sirge ja kestaks."),
    ]),
    "4334": ("Värv, mis jääb ühtlane.", "varv", [
        ("Siseruumide värvimine", "Seinte ja lagede ettevalmistus, kruntimine ja värvimine."),
        ("Pahteldus", "Pragude ja aukude parandus ning pinna lihvimine enne värvi."),
        ("Fassaadi värvimine", "Puit- ja krohvfassaadide puhastus, kruntimine ja värvimine."),
        ("Klaasitööd", "Klaaside paigaldus ja vahetus akendes, ustes ja vaheseintes."),
    ]),
    "4332": ("Aknad, uksed ja trepid õigesse kohta.", "puit", [
        ("Akende paigaldus", "Uute akende paigaldus ja vanade vahetus koos tihendamise ja palede viimistlusega."),
        ("Uste paigaldus", "Sise- ja välisuste paigaldus ning lengide ja liistude viimistlus."),
        ("Trepid", "Puittreppide ja trepiastmete paigaldus."),
        ("Puusepatööd", "Liistud, aknalauad ja muud viimistluse puusepatööd."),
    ]),
    "433": ("Siseviimistlus algusest lõpuni.", "krohv", [
        ("Pahteldus ja värvimine", "Seinte ja lagede ettevalmistus, pahteldus ja värvimine."),
        ("Plaatimine", "Põranda- ja seinaplaatide paigaldus vannitubadesse ja kööki."),
        ("Põrandad", "Parketi, laminaadi ja muude põrandakatete paigaldus."),
        ("Remondi lõpetamine", "Liistud, uksed ja väiksemad tööd, mis teevad ruumi valmis."),
    ]),
}

SAMMUD = [
    ("Ülevaatus", "Tuleme kohale, vaatame pinnad üle ja mõõdame."),
    ("Hinnapakkumine", "Saad kirjaliku pakkumise koos materjalide ja ajakavaga."),
    ("Ettevalmistus", "Katame põrandad, aknad ja mööbli ning teeme aluspinna korda."),
    ("Töö", "Teeme tööd kokkulepitud kvaliteedi ja ajakava järgi."),
    ("Üleandmine", "Koristame enda järelt ja vaatame tulemuse koos üle."),
]

# Aktsendid: kõigil valge tekst vähemalt 4.5:1 (kontroll.py arvutab üle).
AKTSENDID = ["#2F5F9E", "#2E6B45", "#7A4E8C", "#8C4A2F", "#1F6670", "#5B5F1E"]

TEKSTUURID = {
    "krohv": '<feTurbulence type="fractalNoise" baseFrequency="0.012 0.03" numOctaves="5" seed="7"/><feDiffuseLighting surfaceScale="3.2" lighting-color="#F2F3F2"><feDistantLight azimuth="200" elevation="38"/></feDiffuseLighting>',
    "plaat": '<feTurbulence type="fractalNoise" baseFrequency="0.4" numOctaves="2" seed="4"/><feDiffuseLighting surfaceScale="0.6" lighting-color="#EEF0EF"><feDistantLight azimuth="210" elevation="60"/></feDiffuseLighting>',
    "varv": '<feTurbulence type="fractalNoise" baseFrequency="0.002 0.05" numOctaves="3" seed="9"/><feDiffuseLighting surfaceScale="1.4" lighting-color="#F1F2F1"><feDistantLight azimuth="180" elevation="50"/></feDiffuseLighting>',
    "puit": '<feTurbulence type="fractalNoise" baseFrequency="0.004 0.12" numOctaves="4" seed="2"/><feDiffuseLighting surfaceScale="2" lighting-color="#E9E3D9"><feDistantLight azimuth="190" elevation="45"/></feDiffuseLighting>',
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
        return "+372 " + (d[:4] + " " + d[4:] if len(d) == 8 else d)
    return t


def ehita(a):
    pealkiri, tekstuur, teenused = teenused_koodi_jargi(a["emtak"])
    aktsent = AKTSENDID[int(a["registrikood"]) % len(AKTSENDID)]
    nimi = a["nimi"]
    lyhinimi = a.get("lyhinimi", nimi)
    tel = a["telefonid"]
    piirkond = a["piirkond"]

    teenuste_html = "\n".join(
        f'      <article class="teenus"><h3>{E(t)}</h3><p>{E(k)}</p></article>' for t, k in teenused
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
<title>{E(lyhinimi)} – {E(teenused[0][0].lower())} {E(a["linn_seesytlev"])}</title>
<meta name="description" content="{E(nimi)}: {E(", ".join(t[0].lower() for t in teenused[:3]))}. Tööpiirkond {E(piirkond)}.">
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
    <a class="logo" href="#algus">{E(lyhinimi)}<small>{E(a.get("logo_alarida", nimi))}</small></a>
    <nav aria-label="Peamenüü">
      <a href="#teenused">Teenused</a>
      <a href="#tood">Tööd</a>
      <a href="#kontakt">Kontakt</a>
    </nav>
  </div>
</header>

<main id="algus">
<section class="sein" aria-labelledby="pealkiri">
  <svg class="tekstuur" aria-hidden="true" focusable="false" preserveAspectRatio="none">
    <filter id="pind" x="0" y="0" width="100%" height="100%">{TEKSTUURID[tekstuur]}</filter>
    <rect width="100%" height="100%" filter="url(#pind)"/>
  </svg>
  <div class="pahtel" aria-hidden="true"></div>
  <div class="wrap">
    <div class="tekst">
      <h1 id="pealkiri">{E(pealkiri)}</h1>
      <p class="lead">{E(a["sissejuhatus"])}</p>
      <div class="nupud">
        <a class="nupp pea" href="tel:{tel_link(tel[0])}">Helista {E(tel_ilus(tel[0]).replace("+372 ", ""))}</a>
        <a class="nupp teine" href="#kontakt">Küsi hinnapakkumist</a>
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
    css = STIIL.replace("__AKTSENT__", aktsent)
    return index, css


STIIL = """@font-face{font-family:"Inter";src:url("/fondid/inter-regular.woff") format("woff");font-weight:400;font-display:swap}
@font-face{font-family:"Inter";src:url("/fondid/inter-semibold.woff") format("woff");font-weight:600;font-display:swap}
@font-face{font-family:"Inter Display";src:url("/fondid/interdisplay-extrabold.woff") format("woff");font-weight:800;font-display:swap}
:root{
  --pind:#E4E6E5;
  --taust:#F7F8F7;
  --tekst:#24282C;
  --vaiketekst:#4A5157;
  --aktsent:__AKTSENT__;
  --tume:#24282C;
  --joon:#C9CDCD;
  --paise-korgus:80px;
}
*{box-sizing:border-box}
[hidden]{display:none !important}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{margin:0;background:var(--taust);color:var(--tekst);font-family:"Inter",system-ui,sans-serif;font-size:17px;line-height:1.55}
a{color:inherit;text-underline-offset:4px}
:focus-visible{outline:3px solid var(--aktsent);outline-offset:3px}
.wrap{max-width:1120px;margin:0 auto;padding:0 24px}
section[id]{scroll-margin-top:16px}
h1,h2{font-family:"Inter Display","Inter",system-ui,sans-serif;font-weight:800;letter-spacing:-.025em}

.teip{background:var(--aktsent);color:#fff;font-size:14px;line-height:1.4;position:relative;z-index:3;clip-path:polygon(0 0,100% 0,99.4% 50%,100% 100%,0 100%,.6% 50%)}
.teip .wrap{display:flex;gap:16px;justify-content:space-between;align-items:center;padding-top:9px;padding-bottom:9px;flex-wrap:wrap}
.teip a{color:#fff;font-weight:600}

header.top{position:absolute;left:0;right:0;z-index:2}
header.top .wrap{display:flex;justify-content:space-between;align-items:center;min-height:var(--paise-korgus)}
.logo{font-family:"Inter Display","Inter",sans-serif;font-weight:800;font-size:21px;letter-spacing:-.01em;text-decoration:none;line-height:1.15}
.logo small{display:block;font-family:"Inter",sans-serif;font-weight:400;font-size:12.5px;color:var(--vaiketekst);letter-spacing:0}
nav a{display:inline-flex;align-items:center;min-height:44px;padding:0 10px;font-weight:600;font-size:15px;text-decoration:none}
nav a:hover{text-decoration:underline}

.sein{position:relative;min-height:min(92vh,760px);display:flex;align-items:flex-end;overflow:hidden;background:var(--pind)}
.sein svg.tekstuur{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}
.sein .pahtel{position:absolute;inset:0;pointer-events:none;background:linear-gradient(105deg,transparent 0 46%,rgba(247,248,247,.94) 46.2% 100%)}
.sein .wrap{position:relative;width:100%;padding-bottom:72px;padding-top:calc(var(--paise-korgus) + 60px);display:grid;grid-template-columns:1fr 1fr;gap:40px}
.sein .tekst{grid-column:2}
h1{font-size:clamp(38px,5.8vw,72px);line-height:1;margin:0 0 22px}
.lead{font-size:19px;max-width:30em;margin:0 0 30px;color:#363C41}
.nupud{display:flex;gap:14px;flex-wrap:wrap}
.nupp{display:inline-flex;align-items:center;min-height:52px;padding:0 24px;font-weight:600;font-size:16px;text-decoration:none;border-radius:2px}
.nupp.pea{background:var(--tume);color:#fff}
.nupp.pea:hover{background:#000}
.nupp.teine{border:2px solid var(--tume)}
.nupp.teine:hover{background:var(--tume);color:#fff}

.plokk{padding:96px 0}
h2{font-size:clamp(28px,3.4vw,40px);line-height:1.05;margin:0 0 14px}
.sissejuhatus{max-width:36em;color:var(--vaiketekst);margin:0 0 44px}
.teenused{display:grid;grid-template-columns:repeat(4,1fr);gap:32px;border-top:2px solid var(--tekst)}
.teenus{padding-top:20px}
.teenus h3{font-size:19px;font-weight:600;margin:0 0 8px}
.teenus p{margin:0;font-size:15.5px;color:var(--vaiketekst)}

.tood{background:var(--pind)}
.galerii{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.kohataide{aspect-ratio:4/3;display:flex;align-items:center;justify-content:center;padding:12px;
  background:repeating-linear-gradient(135deg,#D3D7D7 0 14px,#DDE0E0 14px 28px);border:1px dashed #9AA2A6}
.kohataide span{background:var(--taust);padding:4px 10px;font-size:14px;color:var(--vaiketekst);overflow-wrap:anywhere}

.kaik{background:var(--tume);color:#E9ECEC}
.kaik .sissejuhatus{color:#B4BCC1}
.sammud{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(5,1fr);border-top:2px solid #4A5157}
.sammud li{padding:22px 22px 0 0;position:relative}
.sammud li::before{content:"";position:absolute;top:-2px;left:0;height:2px;width:40%;background:#9DB4D6}
.sammud .nr{font-family:"Inter Display","Inter",sans-serif;font-weight:800;font-size:15px;color:#B9CBE6;display:block;margin-bottom:10px}
.sammud h3{font-size:18px;font-weight:600;margin:0 0 6px;color:#fff}
.sammud p{margin:0;font-size:15px;color:#B4BCC1}

.faktid{display:grid;grid-template-columns:repeat(3,1fr);gap:32px;margin:28px 0 0}
.faktid div{border-top:2px solid var(--tekst);padding-top:16px}
.faktid dt{font-family:"Inter Display","Inter",sans-serif;font-weight:800;font-size:clamp(26px,3vw,36px);letter-spacing:-.02em;line-height:1.1}
.faktid dd{margin:6px 0 0;color:var(--vaiketekst)}

.kontakt{padding-top:24px}
.kontaktid{display:grid;grid-template-columns:repeat(3,1fr);gap:32px;margin:0}
.kontaktid div{background:var(--pind);padding:22px}
.kontaktid dt{color:var(--vaiketekst);font-size:15px;margin-bottom:6px}
.kontaktid dd{margin:0;font-weight:600;font-size:18px;overflow-wrap:anywhere}
.kontaktid a{display:inline-block;min-height:44px;line-height:44px}

footer{border-top:1px solid var(--joon);padding:28px 0;font-size:14px;color:var(--vaiketekst)}
footer .wrap{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}
footer p{margin:0}

@media (max-width:1024px){
  .teenused{grid-template-columns:repeat(2,1fr)}
  .sammud{grid-template-columns:repeat(3,1fr);row-gap:28px}
}
@media (max-width:768px){
  .sein .wrap{grid-template-columns:1fr}
  .sein .tekst{grid-column:1}
  .sein .pahtel{background:linear-gradient(180deg,transparent 0 22%,rgba(247,248,247,.95) 40% 100%)}
  .galerii{grid-template-columns:repeat(2,1fr)}
  .sammud{grid-template-columns:1fr;border-top:0}
  .sammud li{padding:18px 0;border-top:2px solid #4A5157}
  .faktid,.kontaktid{grid-template-columns:1fr;gap:16px}
  nav a:not(:last-child){display:none}
}
@media (max-width:480px){
  body{font-size:16px}
  .wrap{padding:0 16px}
  .plokk{padding:72px 0}
  .teenused{grid-template-columns:1fr;gap:0}
  .teenus{padding:18px 0;border-bottom:1px solid var(--joon)}
  .galerii{grid-template-columns:1fr 1fr;gap:10px}
  .kohataide span{font-size:12px}
}
"""
