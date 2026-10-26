"""Näidislehtede ehitaja.

Iga firma saab andmefailis oma kujunduse ("kujundus": võti KUJUNDUSED-is). Kujundus
määrab fondid, värvid, avaploki (iga avaplokk on eri ideega) ja sektsioonide
paigutuse. 500 € pakett on mitmeleheline (avaleht, teenused, tööd, kontakt,
privaatsus), 250 € pakett on üheleheline.

HTML-i käsitsi ei muudeta. Muuda andmeid või seda faili ja jooksuta genereeri.py.
"""
from fondid import font_face
from sisu import E, SAMMUD, teenused, tel_link, tel_ilus, tel_lyhike, kat, sammud
import kujundused as K
import kujundused_auto
K.KUJUNDUSED.update(kujundused_auto.K)

BASE_CSS = """
*{box-sizing:border-box}
[hidden]{display:none !important}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{animation:none !important;transition:none !important}}
html,body{overflow-x:clip}
body{margin:0;background:var(--bg);color:var(--fg);font-family:var(--keha),system-ui,sans-serif;font-size:17px;line-height:1.6}
img,svg{display:block;max-width:100%}
a{color:inherit;text-underline-offset:4px}
:focus-visible{outline:3px solid var(--fookus);outline-offset:3px}
h1,h2,h3{font-family:var(--pea),system-ui,sans-serif;margin:0}
h2{font-size:clamp(30px,4vw,48px);line-height:1.05;margin:0 0 14px;font-weight:var(--pea-kaal);letter-spacing:var(--pea-ls)}
h3{font-size:20px;line-height:1.25;margin:0 0 8px}
p{margin:0 0 1em}
.wrap{max-width:1180px;margin:0 auto;padding:0 28px}
.plokk{padding:104px 0}
.sissejuhatus{max-width:36em;color:var(--muted);margin:0 0 48px;font-size:18px}
.teip{background:#15181B;color:#fff;font-family:system-ui,sans-serif;font-size:14px;line-height:1.4}
.teip .wrap{display:flex;gap:16px;justify-content:space-between;align-items:center;padding-top:9px;padding-bottom:9px;flex-wrap:wrap}
.teip a{color:#fff;font-weight:600}
.nupp{display:inline-flex;align-items:center;justify-content:center;min-height:52px;padding:0 26px;font-weight:600;font-size:16px;text-decoration:none;border-radius:var(--raadius);border:2px solid transparent;cursor:pointer;font-family:var(--keha),sans-serif}
.nupp.pea{background:var(--accent);color:var(--accent-fg)}
.nupp.pea:hover{filter:brightness(1.08)}
.nupp.teine{border-color:currentColor}
.nupud{display:flex;gap:12px;flex-wrap:wrap}
.kohataide{display:flex;align-items:center;justify-content:center;padding:12px;min-height:180px;border-radius:min(var(--raadius),12px);
  background:repeating-linear-gradient(135deg,var(--surface) 0 14px,var(--line) 14px 28px)}
.kohataide span{background:var(--bg);color:var(--muted);padding:4px 10px;font-size:13.5px;overflow-wrap:anywhere;border-radius:2px}
.pais{position:relative;z-index:5}
.pais .wrap{display:flex;justify-content:space-between;align-items:center;gap:20px;min-height:84px;flex-wrap:wrap}
.logo{font-family:var(--pea),sans-serif;font-weight:var(--pea-kaal);font-size:22px;text-decoration:none;letter-spacing:var(--pea-ls);display:inline-flex;align-items:center;gap:10px;min-height:44px}
.menuu{display:flex;flex-wrap:wrap;gap:4px}
.menuu a{display:inline-flex;align-items:center;min-height:44px;padding:0 12px;font-weight:600;font-size:15px;text-decoration:none;border-radius:var(--raadius)}
.menuu a:hover,.menuu a[aria-current="page"]{text-decoration:underline;text-decoration-thickness:2px}
.jalus{padding:36px 0;font-size:14px;color:var(--muted);border-top:1px solid var(--line)}
.jalus .wrap{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}
.jalus p{margin:0}
.kontaktid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:0}
.kontaktid div{padding:22px;border-radius:min(var(--raadius),16px);background:var(--surface)}
.kontaktid dt{color:var(--muted);font-size:15px;margin-bottom:6px}
.kontaktid dd{margin:0;font-weight:600;font-size:18px;overflow-wrap:anywhere}
.kontaktid a{display:inline-block;min-height:44px;line-height:44px}
.vorm{display:grid;gap:16px;max-width:640px}
.vorm label{display:block;font-weight:600;font-size:15px;margin-bottom:6px}
.vorm input,.vorm select,.vorm textarea{width:100%;font:inherit;font-size:16px;padding:12px 14px;border:1.5px solid var(--line-tugev);background:var(--bg);color:var(--fg);border-radius:min(var(--raadius),12px)}
.vorm textarea{min-height:130px;resize:vertical}
.vorm .markus{font-size:14px;color:var(--muted);margin:0}
.lehe-pais{padding:72px 0 40px}
.lehe-pais h1{font-size:clamp(40px,6vw,76px);line-height:1;font-weight:var(--pea-kaal);letter-spacing:var(--pea-ls);margin:0 0 16px}
.lehe-pais p{max-width:36em;color:var(--muted);font-size:18px;margin:0}
.teenus-pikk{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.6fr);gap:40px;padding:40px 0;border-top:1px solid var(--line)}
.teenus-pikk h2{font-size:clamp(24px,2.6vw,34px);overflow-wrap:anywhere;hyphens:auto}
.teenus-pikk p{max-width:38em}
.galerii-suur{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.galerii-suur .kohataide{aspect-ratio:4/3;min-height:0}
.tekst-leht{max-width:44em}
.tekst-leht h2{font-size:26px;margin-top:32px}
@media (max-width:900px){.kontaktid{grid-template-columns:1fr}.teenus-pikk{grid-template-columns:1fr;gap:8px}.galerii-suur{grid-template-columns:1fr 1fr}}
@media (max-width:480px){body{font-size:16px}.wrap{padding:0 18px}.plokk{padding:72px 0}.galerii-suur{gap:10px}.kohataide span{font-size:12px}}
"""

SKRIPT = """document.addEventListener('submit',function(e){
  var f=e.target; if(!f.matches('[data-mailto]'))return; e.preventDefault();
  var v=function(n){var el=f.elements[n];return el?el.value:''};
  var keha='Nimi: '+v('nimi')+'\\nKontakt: '+v('kontakt')+'\\nTöö: '+v('too')+'\\n\\n'+v('kirjeldus');
  location.href='mailto:'+f.getAttribute('data-mailto')+'?subject='+encodeURIComponent('Hinnapäring: '+v('too'))+'&body='+encodeURIComponent(keha);
});
"""


# ---------- Sektsioonid ----------

def sek_teenused(a, d, link=None):
    t = teenused(a.get("teenused_voti") or a["emtak"])
    stiil = d["teenused"]
    if stiil == "read":
        sisu = "\n".join(f'<li><span class="t-nimi">{E(n)}</span><span class="t-kirj">{E(k)}</span></li>' for n, k, _ in t)
        sisu = f'<ul class="t-read">{sisu}</ul>'
    elif stiil == "numbrid":
        sisu = "\n".join(f'<li><h3>{E(n)}</h3><p>{E(k)}</p></li>' for n, k, _ in t)
        sisu = f'<ol class="t-numbrid">{sisu}</ol>'
    elif stiil == "veerud":
        sisu = "\n".join(f'<article><h3>{E(n)}</h3><p>{E(p.split(". ")[0])}.</p></article>' for n, _, p in t)
        sisu = f'<div class="t-veerud">{sisu}</div>'
    elif stiil == "plaadid":
        sisu = "\n".join(f'<article class="plaat p{i}"><h3>{E(n)}</h3><p>{E(k)}</p></article>' for i, (n, k, _) in enumerate(t))
        sisu = f'<div class="t-plaadid">{sisu}</div>'
    else:  # kaardid
        sisu = "\n".join(f'<article><span class="t-ikoon" aria-hidden="true"></span><h3>{E(n)}</h3><p>{E(k)}</p></article>' for n, k, _ in t)
        sisu = f'<div class="t-kaardid">{sisu}</div>'
    lisa = f'<p class="edasi"><a class="nupp teine" href="{link}">Kõik teenused</a></p>' if link else ""
    return f"""<section id="teenused" class="plokk sek-teenused" aria-labelledby="teenused-pk">
  <div class="wrap">
    <h2 id="teenused-pk">{E(d.get("teenused_pk", "Teenused"))}</h2>
    <p class="sissejuhatus">Võid tellida kogu töö või ainult ühe etapi.</p>
    {sisu}
    {lisa}
  </div>
</section>"""


def sek_tood(a, d, n=6, link=None):
    pildid = "\n".join(f'<div class="kohataide k{i}" role="img" aria-label="Kohatäide: teie töö foto {i}"><span>pildid/too-{i:02d}.webp</span></div>'
                       for i in range(1, n + 1))
    lisa = f'<p class="edasi"><a class="nupp teine" href="{link}">Vaata kõiki töid</a></p>' if link else ""
    return f"""<section id="tood" class="plokk sek-tood" aria-labelledby="tood-pk">
  <div class="wrap">
    <h2 id="tood-pk">Tehtud tööd</h2>
    <p class="sissejuhatus">{E(kat(a)["tood"])}</p>
    <div class="g-{d['galerii']}">{pildid}</div>
    {lisa}
  </div>
</section>"""


def sek_kaik(a, d):
    sammud_html = "\n".join(f'<li><span class="nr">{i}</span><h3>{E(t)}</h3><p>{E(k)}</p></li>' for i, (t, k) in enumerate(sammud(a), 1))
    return f"""<section class="plokk sek-kaik" aria-labelledby="kaik-pk">
  <div class="wrap">
    <h2 id="kaik-pk">Kuidas töö käib</h2>
    <p class="sissejuhatus">Enne alustamist tead, mida teeme, kui kaua see võtab ja mis see maksab.</p>
    <ol class="k-{d['kaik']}">{sammud_html}</ol>
  </div>
</section>"""


def sek_faktid(a, d):
    f = []
    if a.get("aasta"):
        f.append((a["aasta"], "asutamise aasta"))
    if a.get("tootajaid"):
        f.append((str(a["tootajaid"]), "inimest meeskonnas"))
    f.append((a["piirkond"], "tööpiirkond"))
    sisu = "\n".join(f'<div><dt>{E(v)}</dt><dd>{E(s)}</dd></div>' for v, s in f)
    return f"""<section class="plokk sek-faktid" aria-labelledby="faktid-pk">
  <div class="wrap">
    <h2 id="faktid-pk">{E(a["lyhinimi"])} lühidalt</h2>
    <dl class="faktid">{sisu}</dl>
  </div>
</section>"""


def kontakt_dl(a):
    tel = "<br>".join(f'<a href="tel:{tel_link(t)}">{E(tel_ilus(t))}</a>' for t in a["telefonid"])
    return f"""<dl class="kontaktid">
      <div><dt>Telefon</dt><dd>{tel}</dd></div>
      <div><dt>E-post</dt><dd><a href="mailto:{E(a["email"])}">{E(a["email"])}</a></dd></div>
      <div><dt>Piirkond</dt><dd>{E(a["piirkond"])}</dd></div>
    </dl>"""


def sek_kontakt(a, d, link=None):
    t0 = a["telefonid"][0]
    lisa = f'<p class="edasi"><a class="nupp pea" href="{link}">Saada hinnapäring</a></p>' if link else ""
    return f"""<section id="kontakt" class="plokk sek-kontakt" aria-labelledby="kontakt-pk">
  <div class="wrap">
    <h2 id="kontakt-pk">Küsi hinnapakkumist</h2>
    <p class="sissejuhatus">{E(kat(a)["kontakt"])}</p>
    <a class="suur-tel" href="tel:{tel_link(t0)}">{E(tel_ilus(t0))}</a>
    {kontakt_dl(a)}
    {lisa}
  </div>
</section>"""


def jalus(a, privaatsus=False):
    t0 = a["telefonid"][0]
    priv = '<br><a href="privaatsus">Privaatsus</a>' if privaatsus else ""
    return f"""<footer class="jalus">
  <div class="wrap">
    <p>{E(a["nimi"])}, registrikood {E(a["registrikood"])}<br>Tööpiirkond {E(a["piirkond"])}<br><a href="tel:{tel_link(t0)}">{E(tel_ilus(t0))}</a>, <a href="mailto:{E(a["email"])}">{E(a["email"])}</a>{priv}</p>
    <p>Näidisleht: <a href="https://veebikask.ee">Veebikask</a></p>
  </div>
</footer>"""


def teip(a):
    return f"""<div class="teip" role="note">
  <div class="wrap">
    <span>See on näidisleht, mille tegi Veebikask firmale {E(a["nimi"])}. Sisu põhineb avalikel andmetel.</span>
    <a href="https://veebikask.ee">veebikask.ee</a>
  </div>
</div>"""


def pais(a, d, lehed=None, aktiivne=None):
    if lehed:
        lingid = "".join(
            f'<a href="{h}"{" aria-current=\"page\"" if h == aktiivne else ""}>{E(n)}</a>' for n, h in lehed)
    else:
        lingid = '<a href="#teenused">Teenused</a><a href="#tood">Tööd</a><a href="#kontakt">Kontakt</a>'
    logo_href = "./" if lehed else "#algus"
    return f"""<header class="pais pais-{d['pais']}">
  <div class="wrap">
    <a class="logo" href="{logo_href}"><span class="logo-mark" aria-hidden="true"></span>{E(a["lyhinimi"])}</a>
    <nav class="menuu" aria-label="Peamenüü">{lingid}</nav>
  </div>
</header>"""


def lehekylg(a, d, pealkiri, kirjeldus, keha):
    return f"""<!doctype html>
<html lang="et">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{E(pealkiri)}</title>
<meta name="description" content="{E(kirjeldus)}">
<meta name="theme-color" content="{d['theme']}">
<link rel="icon" href="data:,">
<link rel="stylesheet" href="stiil.css">
<script src="/skript.js" defer></script>
</head>
<body>
{teip(a)}
{keha}
</body>
</html>
"""


def ehita(a):
    d = K.KUJUNDUSED[a["kujundus"]]
    t = teenused(a.get("teenused_voti") or a["emtak"])
    lyhi = a["lyhinimi"]
    kirj = f'{a["nimi"]}: {", ".join(x[0].lower() for x in t[:3])}. Tööpiirkond {a["piirkond"]}.'
    hero_html, hero_css = d["hero"](a, d)
    css = "\n".join([font_face(d["pea"], d["keha"]), ":root{" + d["vars"] + "}", BASE_CSS, K.SEKTSIOONI_CSS, d["css"], hero_css])
    failid = {"stiil.css": css}

    if a["pakett"] == "500":
        lehed = [("Avaleht", "./"), ("Teenused", "teenused"), ("Tööd", "tood"), ("Kontakt", "kontakt")]
        avaleht = "\n".join([
            pais(a, d, lehed, "./"), f'<main id="algus">', hero_html,
            sek_teenused(a, d, link="teenused"), sek_tood(a, d, n=3, link="tood"), sek_kaik(a, d),
            sek_faktid(a, d), sek_kontakt(a, d, link="kontakt"), "</main>", jalus(a, True)])
        failid["index.html"] = lehekylg(a, d, f"{lyhi} – {t[0][0].lower()} {a['linn_kus']}", kirj, avaleht)

        pikk = "\n".join(f'<article class="teenus-pikk" id="t{i}"><h2>{E(n)}</h2><div><p>{E(p)}</p>'
                         f'<a class="nupp teine" href="kontakt">Küsi pakkumist</a></div></article>'
                         for i, (n, _, p) in enumerate(t, 1))
        teen = "\n".join([pais(a, d, lehed, "teenused"), '<main>',
                          f'<div class="lehe-pais"><div class="wrap"><h1>Teenused</h1><p>{E(lyhi)} {E(kat(a)["teeb"])} {E(a["piirkond_kus"])}. Võid tellida kogu töö või ainult ühe etapi.</p></div></div>',
                          f'<div class="wrap">{pikk}</div>', sek_kaik(a, d), '</main>', jalus(a, True)])
        failid["teenused.html"] = lehekylg(a, d, f"Teenused – {lyhi}", f"{lyhi} teenused: " + ", ".join(x[0].lower() for x in t) + ".", teen)

        pildid = "\n".join(f'<div class="kohataide" role="img" aria-label="Kohatäide: teie töö foto {i}"><span>pildid/too-{i:02d}.webp</span></div>' for i in range(1, 10))
        tood = "\n".join([pais(a, d, lehed, "tood"), '<main>',
                          '<div class="lehe-pais"><div class="wrap"><h1>Tehtud tööd</h1><p>Siia tulevad teie tööde fotod koos lühikirjeldusega: mis objekt, mis tehti ja kus.</p></div></div>',
                          f'<div class="wrap plokk-alumine"><div class="galerii-suur">{pildid}</div></div>', '</main>', jalus(a, True)])
        failid["tood.html"] = lehekylg(a, d, f"Tehtud tööd – {lyhi}", f"{lyhi} tehtud tööd {a['piirkond_kus']}.", tood)

        valikud = "".join(f"<option>{E(n)}</option>" for n, _, _ in t) + "<option>Mitu tööd korraga</option>"
        vorm = f"""<form class="vorm" data-mailto="{E(a["email"])}" aria-labelledby="vorm-pk">
      <h2 id="vorm-pk">Hinnapäring</h2>
      <div><label for="nimi">Nimi</label><input id="nimi" name="nimi" autocomplete="name" required></div>
      <div><label for="kontakt-v">Telefon või e-post</label><input id="kontakt-v" name="kontakt" required></div>
      <div><label for="too">Töö</label><select id="too" name="too">{valikud}</select></div>
      <div><label for="kirjeldus">Kirjeldus</label><textarea id="kirjeldus" name="kirjeldus" placeholder="{E(kat(a)["vorm_naide"])}"></textarea></div>
      <button class="nupp pea" type="submit">Saada hinnapäring</button>
      <p class="markus">Päring avaneb sinu e-posti programmis valmis kirjana. Loe, kuidas andmeid kasutame: <a href="privaatsus">privaatsus</a>.</p>
    </form>"""
        kont = "\n".join([pais(a, d, lehed, "kontakt"), '<main>',
                          f'<div class="lehe-pais"><div class="wrap"><h1>Kontakt</h1><p>Helista, kirjuta või saada hinnapäring. {E(kat(a)['kontakt'].split('. ',1)[1])}</p></div></div>',
                          f'<div class="wrap kontakt-leht">{kontakt_dl(a)}<div class="vormi-ala">{vorm}</div></div>', '</main>', jalus(a, True)])
        failid["kontakt.html"] = lehekylg(a, d, f"Kontakt – {lyhi}", f"{lyhi} kontaktid ja hinnapäring.", kont)

        priv = f"""<div class="lehe-pais"><div class="wrap"><h1>Privaatsus</h1></div></div>
<div class="wrap tekst-leht plokk-alumine">
<p>Hinnapäringu vorm avab sinu e-posti programmi ja saadab kirja otse aadressile {E(a["email"])}. Lehel ei salvestata vormi andmeid.</p>
<h2>Mis andmeid saame</h2><p>Nime, kontaktandmed ja töö kirjelduse, mille ise kirja paned.</p>
<h2>Milleks</h2><p>Ainult sinu päringule vastamiseks ja hinnapakkumise tegemiseks.</p>
<h2>Kui kaua hoiame</h2><p>Kirjavahetust hoiame seni, kuni see on pakkumise või töö jaoks vajalik.</p>
<h2>Sinu õigused</h2><p>Võid igal ajal küsida enda kohta käivaid andmeid ja paluda need kustutada. Kirjuta {E(a["email"])}.</p>
<p>Vastutav töötleja: {E(a["nimi"])}, registrikood {E(a["registrikood"])}.</p>
</div>"""
        failid["privaatsus.html"] = lehekylg(a, d, f"Privaatsus – {lyhi}", f"{lyhi} privaatsuspõhimõtted.",
                                             "\n".join([pais(a, d, lehed, None), "<main>", priv, "</main>", jalus(a, True)]))
    else:
        keha = "\n".join([pais(a, d), '<main id="algus">', hero_html, sek_teenused(a, d), sek_tood(a, d),
                          sek_kaik(a, d), sek_faktid(a, d), sek_kontakt(a, d), "</main>", jalus(a)])
        failid["index.html"] = lehekylg(a, d, f"{lyhi} – {t[0][0].lower()} {a['linn_kus']}", kirj, keha)
    return failid
