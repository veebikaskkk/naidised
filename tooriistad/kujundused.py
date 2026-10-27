"""Kujundused. Iga kujundus on eri idee: oma avaplokk, fondid, värvid ja sektsioonide paigutus.

Avaploki funktsioon saab firma andmed (a) ja kujunduse (d) ning tagastab (html, css).
Värvid on muutujatena; kontroll.py arvutab kontrasti üle.
"""
from sisu import E, teenused, tel_link, tel_lyhike, kat


def nupud(a, hele=False):
    t0 = a["telefonid"][0]
    k = kat(a)
    siht = k.get("nupp_siht") or ("kontakt" if a["pakett"] == "500" else "#kontakt")
    return (f'<div class="nupud"><a class="nupp pea" href="tel:{tel_link(t0)}">Helista {E(tel_lyhike(t0))}</a>'
            f'<a class="nupp teine" href="{siht}">{E(k.get("nupp", "Küsi hinnapakkumist"))}</a></div>')


def lead(a):
    return f'<p class="lead">{E(a["sissejuhatus"])}</p>'


# ---------- Sektsioonide variandid (ühised, värvid muutujatest) ----------
SEKTSIOONI_CSS = """
.plokk-alumine{padding-bottom:104px}
.edasi{margin:36px 0 0}
.lead{font-size:19px;max-width:32em;margin:0 0 30px}
/* teenused */
.t-kaardid{display:grid;grid-template-columns:repeat(4,1fr);gap:20px}
.t-kaardid article{background:var(--surface);padding:26px 22px;border-radius:min(var(--raadius),16px)}
.t-kaardid .t-ikoon{display:block;width:28px;height:28px;border-radius:var(--raadius);background:var(--accent);margin-bottom:18px}
.t-kaardid p,.t-veerud p,.t-numbrid p,.t-plaadid p{margin:0;color:var(--muted);font-size:15.5px}
.t-read{list-style:none;margin:0;padding:0;border-bottom:1px solid var(--line)}
.t-read li{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.3fr);gap:24px;align-items:baseline;padding:26px 0;border-top:1px solid var(--line)}
.t-read .t-nimi{font-family:var(--pea),sans-serif;font-size:clamp(24px,3vw,36px);line-height:1.1;font-weight:var(--pea-kaal);letter-spacing:var(--pea-ls)}
.t-read .t-kirj{color:var(--muted)}
.t-numbrid{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:36px 48px;counter-reset:t}
.t-numbrid li{counter-increment:t;display:grid;grid-template-columns:auto 1fr;gap:0 20px}
.t-numbrid li::before{content:counter(t,decimal-leading-zero);grid-row:span 2;font-family:var(--pea),sans-serif;font-weight:var(--pea-kaal);font-size:44px;line-height:1;color:var(--fg)}
.t-veerud{display:grid;grid-template-columns:repeat(4,1fr);gap:28px}
.t-veerud article{border-left:4px solid var(--accent);padding-left:18px}
.t-plaadid{display:grid;grid-template-columns:repeat(4,1fr);gap:0}
.t-plaadid .plaat{padding:30px 24px 34px;min-height:220px;display:flex;flex-direction:column;justify-content:flex-end}
.t-plaadid .p0{background:var(--dark);color:var(--dark-fg)}.t-plaadid .p0 p{color:var(--dark-fg);opacity:.85}
.t-plaadid .p1{background:var(--accent);color:var(--accent-fg)}.t-plaadid .p1 p{color:var(--accent-fg);opacity:.9}
.t-plaadid .p2{background:var(--surface)}
.t-plaadid .p3{background:var(--bg);box-shadow:inset 0 0 0 2px var(--line)}
/* galerii */
.g-ruudustik{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.g-ruudustik .kohataide{aspect-ratio:4/3;min-height:0}
.g-mosaiik{display:grid;grid-template-columns:2fr 1fr 1fr;grid-auto-rows:200px;gap:14px}
.g-mosaiik .k1{grid-row:span 2}
.g-mosaiik:has(> :nth-child(3):last-child){grid-template-columns:2fr 1fr}
.g-mosaiik .k1,.g-mosaiik .kohataide{min-height:0}
.g-riba{display:grid;grid-template-columns:repeat(6,1fr);gap:10px}
.g-riba .kohataide{aspect-ratio:3/4;min-height:0}
.g-polaroid{display:grid;grid-template-columns:repeat(3,1fr);gap:28px}
.g-polaroid .kohataide{aspect-ratio:1;min-height:0;border:10px solid #fff;box-shadow:0 12px 30px -16px rgba(0,0,0,.45)}
.g-polaroid .k1,.g-polaroid .k5{transform:rotate(-2deg)}.g-polaroid .k2,.g-polaroid .k6{transform:rotate(1.5deg)}
/* töö käik */
.sek-kaik{background:var(--dark);color:var(--dark-fg)}
.sek-kaik .sissejuhatus{color:var(--dark-fg);opacity:.86}
.sek-kaik ol{list-style:none;margin:0;padding:0}
.sek-kaik p{margin:0;opacity:.86;font-size:15.5px}
.sek-kaik .nr{display:block;font-family:var(--pea),sans-serif;font-weight:var(--pea-kaal);font-size:30px;line-height:1;margin-bottom:12px;color:var(--dark-accent)}
.k-rida{display:grid;grid-template-columns:repeat(5,1fr);gap:24px}
.k-rida li{border-top:2px solid var(--dark-accent);padding-top:18px}
.k-ajajoon{position:relative;max-width:760px}
.k-ajajoon li{position:relative;padding:0 0 30px 64px}
.k-ajajoon li::before{content:"";position:absolute;left:18px;top:8px;bottom:-8px;width:2px;background:var(--dark-accent);opacity:.5}
.k-ajajoon li:last-child::before{display:none}
.k-ajajoon .nr{position:absolute;left:0;top:0;width:38px;height:38px;border-radius:50%;background:var(--dark-accent);color:var(--dark);font-size:18px;display:flex;align-items:center;justify-content:center;margin:0}
.k-redel{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;align-items:end}
.k-redel li{background:rgba(255,255,255,.07);padding:22px 18px;border-radius:min(var(--raadius),16px)}
.k-redel li:nth-child(2){margin-bottom:28px}.k-redel li:nth-child(3){margin-bottom:56px}.k-redel li:nth-child(4){margin-bottom:84px}.k-redel li:nth-child(5){margin-bottom:112px}
.k-kaardid{display:grid;grid-template-columns:repeat(5,1fr);gap:14px}
.k-kaardid li{border:1.5px solid rgba(255,255,255,.22);padding:22px 18px;border-radius:min(var(--raadius),16px)}
/* faktid ja kontakt */
.faktid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin:24px 0 0}
.faktid div{border-top:3px solid var(--fg);padding-top:16px}
.faktid dt{font-family:var(--pea),sans-serif;font-weight:var(--pea-kaal);font-size:clamp(26px,3.2vw,40px);letter-spacing:var(--pea-ls);line-height:1.1}
.faktid dd{margin:6px 0 0;color:var(--muted)}
.suur-tel{display:inline-block;font-family:var(--pea),sans-serif;font-weight:var(--pea-kaal);font-size:clamp(34px,6vw,72px);letter-spacing:var(--pea-ls);line-height:1.05;text-decoration:none;margin:0 0 36px;border-bottom:4px solid var(--accent)}
.kontakt-leht{display:grid;grid-template-columns:1fr;gap:40px;padding-bottom:104px}
.kontakt-leht .kontaktid{grid-template-columns:repeat(3,1fr)}
.vormi-ala{background:var(--surface);padding:32px;border-radius:min(var(--raadius),16px)}
.vormi-ala h2{font-size:28px}
@media (max-width:1024px){.t-kaardid,.t-veerud,.t-plaadid{grid-template-columns:1fr 1fr}.k-rida,.k-kaardid{grid-template-columns:repeat(3,1fr)}.k-redel{grid-template-columns:1fr 1fr 1fr}.k-redel li{margin-bottom:0 !important}.g-riba{grid-template-columns:repeat(3,1fr)}}
@media (max-width:768px){.t-read li{grid-template-columns:1fr;gap:6px}.t-numbrid{grid-template-columns:1fr}.k-rida,.k-kaardid,.k-redel{grid-template-columns:1fr}.faktid,.kontakt-leht .kontaktid{grid-template-columns:1fr}.g-mosaiik{grid-template-columns:1fr 1fr;grid-auto-rows:150px}.g-mosaiik .k1{grid-column:span 2;grid-row:auto}.g-ruudustik,.g-polaroid{grid-template-columns:1fr 1fr;gap:12px}.g-polaroid .kohataide{border-width:6px}}
@media (max-width:480px){.t-kaardid,.t-veerud,.t-plaadid{grid-template-columns:1fr}.t-plaadid .plaat{min-height:0}.vormi-ala{padding:22px}}
"""


def v(**k):
    """Kujunduse muutujad. Kõik värvid on siin, et kontroll.py saaks kontrasti arvutada."""
    base = dict(raadius="4px", pea_ls="-0.02em", pea_kaal="800", line_tugev="#9AA1A6")
    base.update(k)
    return ";".join(f"--{x.replace('_', '-')}:{y}" for x, y in base.items())


# ======================================================================
# 500 € kujundused (mitmelehelised)
# ======================================================================

def hero_plaan(a, d):
    aasta = a.get("aasta", "")
    h = f"""<section class="h-plaan" aria-labelledby="pk">
  <div class="wrap h-plaan-sisu">
    <div>
      <p class="h-silt">{E(a["nimi"])}</p>
      <h1 id="pk">{E(d["h1"])}</h1>
      {lead(a)}
      {nupud(a)}
    </div>
    <svg class="h-joonis" viewBox="0 0 400 320" aria-hidden="true" focusable="false">
      <rect x="40" y="40" width="300" height="230" fill="none" stroke="#9FC2E8" stroke-width="2"/>
      <rect x="40" y="40" width="130" height="230" fill="none" stroke="#9FC2E8" stroke-width="1.2"/>
      <path d="M170 160h170M170 200a40 40 0 0 1 40-40" fill="none" stroke="#9FC2E8" stroke-width="1.2"/>
      <path d="M40 20h300M40 14v12M340 14v12M360 40v230M354 40h12M354 270h12" stroke="#D9A441" stroke-width="1.5"/>
      <text x="190" y="14" fill="#D9A441" font-size="13" text-anchor="middle" font-family="sans-serif">{E(aasta)}</text>
    </svg>
  </div>
</section>"""
    c = """.h-plaan{background:#10284A;color:#fff;padding:72px 0 96px;
  background-image:linear-gradient(rgba(159,194,232,.12) 1px,transparent 1px),linear-gradient(90deg,rgba(159,194,232,.12) 1px,transparent 1px),linear-gradient(rgba(159,194,232,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(159,194,232,.06) 1px,transparent 1px);
  background-size:120px 120px,120px 120px,24px 24px,24px 24px}
.h-plaan-sisu{display:grid;grid-template-columns:1.3fr 1fr;gap:48px;align-items:center}
.h-silt{font-size:15px;color:#D9A441;margin:0 0 18px;font-weight:600}
.h-plaan h1{font-size:clamp(42px,6vw,80px);line-height:1;font-weight:700;letter-spacing:-.02em;margin:0 0 24px}
.h-plaan .lead{color:#DCE6F2}
.h-plaan .nupp.teine{color:#fff}
@media (max-width:860px){.h-plaan-sisu{grid-template-columns:1fr}.h-joonis{max-width:320px}}"""
    return h, c


def hero_palett(a, d):
    toonid = ["#3B2DB8", "#E2A33B", "#2F8F6B", "#C8475B", "#1E6FB0", "#7A3E9D", "#E5D9C3"]
    lehed = "".join(f'<span class="h-leht l{i}"></span>' for i in range(len(toonid)))
    h = f"""<section class="h-palett" aria-labelledby="pk">
  <div class="wrap h-palett-sisu">
    <div>
      <h1 id="pk">{E(d["h1"])}</h1>
      {lead(a)}
      {nupud(a)}
    </div>
    <div class="h-lehvik" aria-hidden="true">{lehed}</div>
  </div>
</section>"""
    c = ".h-palett{padding:56px 0 110px;overflow:hidden}\n.h-palett-sisu{display:grid;grid-template-columns:1.1fr 1fr;gap:40px;align-items:center}\n"
    c += ".h-palett h1{font-size:clamp(46px,7.4vw,104px);line-height:.92;font-weight:800;letter-spacing:-.04em;margin:0 0 26px}\n"
    c += ".h-lehvik{position:relative;height:440px}\n.h-leht{position:absolute;left:50%;bottom:0;width:92px;height:400px;margin-left:-46px;border-radius:10px;transform-origin:50% 92%;box-shadow:0 10px 26px -14px rgba(0,0,0,.5)}\n"
    for i, t in enumerate(toonid):
        c += f".h-leht.l{i}{{background:{t};transform:rotate({-42 + i * 14}deg)}}\n"
    c += "@media (max-width:860px){.h-palett-sisu{grid-template-columns:1fr}.h-lehvik{height:300px}.h-leht{height:270px;width:66px;margin-left:-33px}}"
    return h, c


def hero_teip(a, d):
    h = f"""<section class="h-teip" aria-labelledby="pk">
  <div class="h-triibud" aria-hidden="true"></div>
  <div class="wrap">
    <h1 id="pk">{E(d["h1"])}</h1>
    <div class="h-teip-all">{lead(a)}{nupud(a)}</div>
  </div>
  <div class="h-triibud" aria-hidden="true"></div>
</section>"""
    c = """.h-teip{background:#FFD23F;color:#111}
.h-triibud{height:34px;background:repeating-linear-gradient(-45deg,#111 0 22px,#FFD23F 22px 44px)}
.h-teip .wrap{padding-top:64px;padding-bottom:72px}
.h-teip h1{font-size:clamp(40px,7.6vw,112px);line-height:1.06;font-weight:900;letter-spacing:-.03em;text-transform:uppercase;margin:0 0 36px;max-width:12em}
.h-teip-all{display:grid;grid-template-columns:1fr auto;gap:32px;align-items:end}
.h-teip .lead{margin:0}
.h-teip .nupp.pea{background:#111;color:#FFD23F}
@media (max-width:760px){.h-teip-all{grid-template-columns:1fr}}"""
    return h, c


def hero_ruutmeeter(a, d):
    v_ = ["#0F6B5C", "#DCE4E2", "#C9D6D3", "#F2B544", "#1B3D37", "#E9EEED", "#8FB6AE", "#DCE4E2", "#0F6B5C"]
    ruudud = "".join(f'<span class="r{i}"></span>' for i in range(16))
    h = f"""<section class="h-ruut" aria-labelledby="pk">
  <div class="wrap h-ruut-sisu">
    <div>
      <p class="h-m2" aria-hidden="true">m²</p>
      <h1 id="pk">{E(d["h1"])}</h1>
      {lead(a)}
      {nupud(a)}
    </div>
    <div class="h-mosaiik" aria-hidden="true">{ruudud}</div>
  </div>
</section>"""
    c = ".h-ruut{padding:56px 0 96px}\n.h-ruut-sisu{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center}\n"
    c += ".h-m2{font-family:var(--pea),sans-serif;font-weight:700;font-size:clamp(90px,14vw,200px);line-height:.8;margin:0 0 10px;color:#0F6B5C;letter-spacing:-.06em}\n"
    c += ".h-ruut h1{font-size:clamp(34px,4.6vw,58px);line-height:1.02;font-weight:700;letter-spacing:-.03em;margin:0 0 22px}\n"
    c += ".h-mosaiik{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;background:#fff;padding:6px;aspect-ratio:1}\n.h-mosaiik span{border-radius:2px}\n"
    pal = ["#0F6B5C", "#DCE4E2", "#C9D6D3", "#F2B544", "#1B3D37", "#E9EEED", "#8FB6AE", "#DCE4E2", "#C9D6D3", "#0F6B5C", "#E9EEED", "#8FB6AE", "#DCE4E2", "#1B3D37", "#F2B544", "#C9D6D3"]
    for i, t in enumerate(pal):
        c += f".h-mosaiik .r{i}{{background:{t}}}\n"
    c += "@media (max-width:860px){.h-ruut-sisu{grid-template-columns:1fr}.h-mosaiik{max-width:360px}}"
    return h, c


def hero_horisont(a, d):
    h = f"""<section class="h-horisont" aria-labelledby="pk">
  <div class="wrap">
    <h1 id="pk">{E(d["h1"])}</h1>
  </div>
  <div class="h-meri" aria-hidden="true"></div>
  <div class="h-horisont-all"><div class="wrap">{lead(a)}{nupud(a)}</div></div>
</section>"""
    c = """.h-horisont{background:linear-gradient(#EAF2F8,#D5E5F0);padding-top:80px}
.h-horisont h1{font-size:clamp(48px,8vw,120px);line-height:.95;font-weight:400;letter-spacing:-.02em;margin:0 0 48px;color:#13324A;max-width:11em}
.h-meri{height:120px;background:linear-gradient(#2A6787,#1E4E6E 60%,#173E58);position:relative}
.h-meri::before{content:"";position:absolute;inset:0;background:repeating-linear-gradient(180deg,rgba(255,255,255,.10) 0 2px,transparent 2px 14px)}
.h-horisont-all{background:#173E58;color:#fff;padding:8px 0 64px}
.h-horisont-all .wrap{display:grid;grid-template-columns:1fr auto;gap:32px;align-items:end}
.h-horisont-all .lead{margin:0;color:#E3EEF5}
.h-horisont .nupp.pea{background:#fff;color:#173E58}
.h-horisont .nupp.teine{color:#fff}
@media (max-width:760px){.h-horisont-all .wrap{grid-template-columns:1fr}.h-meri{height:70px}}"""
    return h, c


def hero_pits(a, d):
    h = f"""<section class="h-pits" aria-labelledby="pk">
  <div class="wrap h-pits-sisu">
    <p class="h-koht">{E(a["piirkond"])}</p>
    <h1 id="pk">{E(d["h1"])}</h1>
    {lead(a)}
    {nupud(a)}
  </div>
  <div class="h-pitsiserv" aria-hidden="true"></div>
</section>"""
    c = """.h-pits{background:#3E5B4A;color:#fff;text-align:center;position:relative}
.h-pits-sisu{padding-top:88px;padding-bottom:72px;display:flex;flex-direction:column;align-items:center}
.h-koht{font-family:var(--pea),serif;font-style:italic;font-size:22px;margin:0 0 14px;color:#DDE8DF}
.h-pits h1{font-size:clamp(44px,6.6vw,92px);line-height:1;font-weight:400;font-style:italic;margin:0 0 24px;max-width:13em}
.h-pits .lead{color:#E7EFE9;margin-left:auto;margin-right:auto}
.h-pits .nupp.pea{background:#fff;color:#2D4437}
.h-pits .nupp.teine{color:#fff}
.h-pitsiserv{height:44px;background:radial-gradient(circle at 22px 0,#3E5B4A 21px,transparent 22px) 0 0/44px 44px repeat-x,radial-gradient(circle at 22px 0,transparent 12px,#fff 13px,#fff 14px,transparent 15px) 0 0/44px 44px repeat-x;position:absolute;left:0;right:0;bottom:-44px;z-index:1;pointer-events:none}"""
    return h, c


def hero_kalasaba(a, d):
    h = f"""<section class="h-kalasaba" aria-labelledby="pk">
  <div class="h-muster" aria-hidden="true"></div>
  <div class="wrap h-kalasaba-sisu">
    <div class="h-kaart">
      <h1 id="pk">{E(d["h1"])}</h1>
      {lead(a)}
      {nupud(a)}
    </div>
  </div>
</section>"""
    c = """.h-kalasaba{position:relative;background:#0E4D5C;padding:64px 0}
.h-muster{position:absolute;inset:0;background:
 linear-gradient(45deg,transparent 0 46%,rgba(255,255,255,.55) 46% 50%,transparent 50%) 0 0/60px 60px,
 linear-gradient(-45deg,transparent 0 46%,rgba(255,255,255,.55) 46% 50%,transparent 50%) 30px 0/60px 60px,
 linear-gradient(135deg,#126274,#0E4D5C 50%,#0B3F4C)}
.h-kalasaba-sisu{position:relative}
.h-kaart{background:#FBFCFC;max-width:620px;padding:48px 44px;border-radius:2px;box-shadow:0 30px 60px -30px rgba(0,0,0,.6)}
.h-kaart h1{font-size:clamp(40px,5.4vw,70px);line-height:1;font-weight:400;margin:0 0 22px;color:#0E4D5C}
@media (max-width:600px){.h-kaart{padding:32px 24px}}"""
    return h, c


def hero_kontroll(a, d):
    t = teenused(a.get("teenused_voti") or a["emtak"])
    read = "".join(f'<li><span class="h-linn" aria-hidden="true"></span>{E(n)}</li>' for n, _, _ in t)
    h = f"""<section class="h-kontroll" aria-labelledby="pk">
  <div class="wrap h-kontroll-sisu">
    <div>
      <h1 id="pk">{E(d["h1"])}</h1>
      {lead(a)}
      {nupud(a)}
    </div>
    <div class="h-leht-kaart" aria-hidden="true">
      <p class="h-leht-pk">Tööleht</p>
      <ul>{read}</ul>
    </div>
  </div>
</section>"""
    c = """.h-kontroll{background:#24452F;color:#fff;padding:72px 0 96px}
.h-kontroll-sisu{display:grid;grid-template-columns:1.2fr 1fr;gap:56px;align-items:center}
.h-kontroll h1{font-size:clamp(42px,6vw,82px);line-height:.98;font-weight:800;letter-spacing:-.03em;margin:0 0 24px}
.h-kontroll .lead{color:#E2ECE4}
.h-kontroll .nupp.teine{color:#fff}
.h-kontroll .nupp.pea{background:#E9B44C;color:#1E2B22}
.h-leht-kaart{background:#FFFDF7;color:#1E2B22;padding:28px 30px 34px;border-radius:6px;transform:rotate(2deg);box-shadow:0 30px 50px -24px rgba(0,0,0,.6);border-top:16px solid #E9B44C}
.h-leht-pk{font-family:var(--pea),sans-serif;font-weight:800;font-size:24px;margin:0 0 12px}
.h-leht-kaart ul{list-style:none;margin:0;padding:0}
.h-leht-kaart li{display:flex;gap:14px;align-items:center;padding:12px 0;border-bottom:1px dashed #B9C4BC;font-weight:600}
.h-linn{width:22px;height:22px;border:2px solid #24452F;border-radius:4px;position:relative;flex:none}
.h-linn::after{content:"";position:absolute;left:5px;top:1px;width:7px;height:12px;border:solid #24452F;border-width:0 3px 3px 0;transform:rotate(45deg)}
@media (max-width:860px){.h-kontroll-sisu{grid-template-columns:1fr}.h-leht-kaart{transform:none}}"""
    return h, c


def hero_joonlaud(a, d):
    n = a.get("tootajaid") or ""
    suur = f'<p class="h-arv"><span>{E(str(n))}</span> inimest meeskonnas</p>' if n else ""
    h = f"""<section class="h-joonlaud" aria-labelledby="pk">
  <div class="h-mood" aria-hidden="true"></div>
  <div class="wrap h-joonlaud-sisu">
    <h1 id="pk">{E(d["h1"])}</h1>
    <div>{suur}{lead(a)}{nupud(a)}</div>
  </div>
</section>"""
    c = """.h-joonlaud{background:#E4E4E1;padding-bottom:88px}
.h-mood{height:56px;background:#F2C230;background-image:repeating-linear-gradient(90deg,#1D1D1B 0 2px,transparent 2px 10px),repeating-linear-gradient(90deg,#1D1D1B 0 2px,transparent 2px 50px);background-size:100% 18px,100% 34px;background-repeat:repeat-x;background-position:0 0,0 0}
.h-joonlaud-sisu{display:grid;grid-template-columns:1.4fr 1fr;gap:48px;align-items:end;padding-top:72px}
.h-joonlaud h1{font-size:clamp(48px,8.2vw,124px);line-height:.88;font-weight:900;letter-spacing:-.04em;margin:0}
.h-arv{margin:0 0 20px;font-weight:600}
.h-arv span{display:block;font-family:var(--pea),sans-serif;font-weight:900;font-size:96px;line-height:.9;color:#B23A0E;letter-spacing:-.04em}
@media (max-width:860px){.h-joonlaud-sisu{grid-template-columns:1fr}}"""
    return h, c


def hero_radiaal(a, d):
    h = f"""<section class="h-radiaal" aria-labelledby="pk">
  <div class="h-ringid" aria-hidden="true"></div>
  <div class="wrap h-radiaal-sisu">
    <h1 id="pk">{E(d["h1"])}</h1>
    {lead(a)}
    {nupud(a)}
  </div>
</section>"""
    c = """.h-radiaal{position:relative;background:#17161A;color:#fff;overflow:hidden;padding:96px 0 110px}
.h-ringid{position:absolute;right:-220px;top:50%;width:760px;height:760px;margin-top:-380px;border-radius:50%;
 background:repeating-radial-gradient(circle,#C7773A 0 2px,transparent 2px 38px);opacity:.75}
.h-radiaal-sisu{position:relative;max-width:1180px}
.h-radiaal h1{font-size:clamp(42px,6.4vw,92px);line-height:.98;font-weight:800;letter-spacing:-.03em;margin:0 0 24px;max-width:10em}
.h-radiaal .lead{color:#E9E3DD}
.h-radiaal .nupp.teine{color:#fff}
@media (max-width:760px){.h-ringid{width:480px;height:480px;margin-top:-240px;right:-300px;opacity:.45}}"""
    return h, c


# ======================================================================
# 250 € kujundused (ühelehelised)
# ======================================================================

def hero_kald(a, d):
    h = f"""<section class="h-kald" aria-labelledby="pk">
  <div class="h-kald-vasak">
    <div class="h-kald-tekst">
      <h1 id="pk">{E(d["h1"])}</h1>
      {lead(a)}
      {nupud(a)}
    </div>
  </div>
  <p class="h-kald-sona" aria-hidden="true">{E(a["lyhinimi"].split()[0])}</p>
</section>"""
    c = """.h-kald{display:grid;grid-template-columns:1.15fr 1fr;min-height:560px;background:#F2F4FA;overflow:hidden}
.h-kald-vasak{background:#2340B0;color:#fff;clip-path:polygon(0 0,100% 0,86% 100%,0 100%);display:flex;align-items:center}
.h-kald-tekst{padding:64px 18% 64px max(28px,calc((100vw - 1180px)/2 + 28px))}
.h-kald h1{font-size:clamp(40px,5.6vw,76px);line-height:.98;font-weight:800;letter-spacing:-.03em;margin:0 0 22px}
.h-kald .lead{color:#E3E8FA}
.h-kald .nupp.pea{background:#fff;color:#2340B0}
.h-kald .nupp.teine{color:#fff}
.h-kald-sona{align-self:center;justify-self:center;font-family:var(--pea),sans-serif;font-weight:800;font-size:clamp(80px,14vw,210px);line-height:1;margin:0;color:transparent;-webkit-text-stroke:2px #2340B0;writing-mode:vertical-rl;transform:rotate(180deg);letter-spacing:.02em}
@media (max-width:860px){.h-kald{grid-template-columns:1fr}.h-kald-vasak{clip-path:none}.h-kald-tekst{padding:56px 18px}.h-kald-sona{writing-mode:horizontal-tb;transform:none;font-size:80px;padding:20px 0}}"""
    return h, c


def hero_laudis(a, d):
    h = f"""<section class="h-laudis" aria-labelledby="pk">
  <div class="wrap">
    <div class="h-silt-laud">
      <h1 id="pk">{E(d["h1"])}</h1>
      {lead(a)}
      {nupud(a)}
    </div>
  </div>
</section>"""
    c = """.h-laudis{padding:96px 0;background:
 repeating-linear-gradient(90deg,rgba(0,0,0,.22) 0 2px,transparent 2px 86px),
 repeating-linear-gradient(90deg,#B07A4C 0 86px,#A26E43 86px 172px,#BB8556 172px 258px),#B07A4C}
.h-silt-laud{background:#3B2618;color:#F7EBDD;max-width:680px;padding:52px 48px;border-radius:6px;box-shadow:0 24px 50px -24px rgba(0,0,0,.7)}
.h-silt-laud h1{font-size:clamp(40px,5.6vw,74px);line-height:1;font-weight:900;margin:0 0 22px;letter-spacing:-.02em}
.h-silt-laud .lead{color:#EBDCCB}
.h-laudis .nupp.teine{color:#F7EBDD}
.h-laudis .nupp.pea{background:#F0A35E;color:#2B1C12}
@media (max-width:600px){.h-silt-laud{padding:32px 24px}}"""
    return h, c


def hero_lubivarv(a, d):
    h = f"""<section class="h-lubi" aria-labelledby="pk">
  <div class="wrap h-lubi-sisu">
    <h1 id="pk">{E(d["h1"])}</h1>
    <div class="h-lubi-all">{lead(a)}{nupud(a)}</div>
  </div>
</section>"""
    c = """.h-lubi{color:#fff;padding:110px 0 96px;background:
 radial-gradient(ellipse at 20% 30%,rgba(255,255,255,.14),transparent 45%),
 radial-gradient(ellipse at 75% 65%,rgba(0,0,0,.25),transparent 50%),
 radial-gradient(ellipse at 60% 15%,rgba(255,255,255,.08),transparent 40%),
 radial-gradient(ellipse at 10% 90%,rgba(0,0,0,.2),transparent 45%),#5B2E4E}
.h-lubi h1{font-size:clamp(52px,9vw,140px);line-height:.9;font-weight:400;font-style:italic;letter-spacing:-.02em;margin:0 0 48px;max-width:9em}
.h-lubi-all{display:grid;grid-template-columns:1fr auto;gap:32px;align-items:end;border-top:1px solid rgba(255,255,255,.4);padding-top:28px}
.h-lubi .lead{margin:0;color:#F1E6EE}
.h-lubi .nupp.pea{background:#fff;color:#5B2E4E}
.h-lubi .nupp.teine{color:#fff}
@media (max-width:760px){.h-lubi-all{grid-template-columns:1fr}}"""
    return h, c


def hero_pintsel(a, d):
    h = f"""<section class="h-pintsel" aria-labelledby="pk">
  <svg class="h-tomme" viewBox="0 0 1200 360" preserveAspectRatio="none" aria-hidden="true" focusable="false">
    <defs><linearGradient id="siid" x1="0" x2="1"><stop offset="0" stop-color="#B3262E"/><stop offset=".55" stop-color="#D9545A"/><stop offset="1" stop-color="#F0A8A5"/></linearGradient></defs>
    <path d="M-20 250C180 120 360 300 560 190S900 60 1220 150L1220 230C930 150 760 300 560 270S200 260-20 330Z" fill="url(#siid)"/>
    <path d="M-20 280C200 170 380 330 560 230S920 110 1220 190" fill="none" stroke="#fff" stroke-opacity=".35" stroke-width="3"/>
  </svg>
  <div class="wrap h-pintsel-sisu">
    <h1 id="pk">{E(d["h1"])}</h1>
    {lead(a)}
    {nupud(a)}
  </div>
</section>"""
    c = """.h-pintsel{position:relative;padding:80px 0 230px;overflow:hidden}
.h-tomme{position:absolute;left:0;right:0;bottom:0;width:100%;height:240px}
.h-pintsel-sisu{position:relative}
.h-pintsel h1{font-size:clamp(56px,10vw,150px);line-height:.88;font-weight:400;margin:0 0 26px;color:#7E1A21}
.h-pintsel .lead{max-width:28em}
@media (max-width:600px){.h-tomme{height:140px}.h-pintsel{padding-bottom:150px}}"""
    return h, c


def hero_raps(a, d):
    h = f"""<section class="h-raps" aria-labelledby="pk">
  <div class="wrap h-raps-sisu">
    <h1 id="pk">{E(d["h1"])}</h1>
    {lead(a)}
    {nupud(a)}
  </div>
  <div class="h-pold" aria-hidden="true"></div>
</section>"""
    c = """.h-raps{background:linear-gradient(#DCEBF6,#EEF5FA 70%);padding-top:80px}
.h-raps h1{font-size:clamp(44px,7vw,100px);line-height:.95;font-weight:800;letter-spacing:-.03em;margin:0 0 24px;max-width:11em}
.h-raps-sisu{padding-bottom:56px}
.h-pold{height:150px;background:
 repeating-linear-gradient(100deg,rgba(255,255,255,.18) 0 3px,transparent 3px 40px),
 linear-gradient(#F2C300,#E3AE00);clip-path:polygon(0 30%,30% 12%,62% 22%,100% 0,100% 100%,0 100%)}"""
    return h, c


def hero_rullitriibud(a, d):
    h = f"""<section class="h-rull" aria-labelledby="pk">
  <div class="h-triip t1" aria-hidden="true"></div><div class="h-triip t2" aria-hidden="true"></div><div class="h-triip t3" aria-hidden="true"></div>
  <div class="wrap h-rull-sisu">
    <h1 id="pk">{E(d["h1"])}</h1>
    {lead(a)}
    {nupud(a)}
  </div>
</section>"""
    c = """.h-rull{position:relative;overflow:hidden;padding:90px 0 100px;background:#F4F7F2}
.h-triip{position:absolute;top:-10%;bottom:-10%;width:150px;border-radius:75px;transform:rotate(14deg)}
.h-triip.t1{right:16%;background:#2F6B3A}.h-triip.t2{right:5%;background:#7BAF6B}.h-triip.t3{right:-6%;background:#C9DFA8}
.h-rull-sisu{position:relative}
.h-rull h1{font-size:clamp(44px,6.2vw,86px);line-height:.95;font-weight:800;letter-spacing:-.03em;margin:0 0 24px;max-width:8.5em}
.h-rull .lead{max-width:24em;background:rgba(244,247,242,.92);padding:4px 0}
.h-rull .wrap{position:relative;z-index:1}
@media (max-width:760px){.h-triip{width:80px;opacity:.3}.h-rull h1{font-size:clamp(32px,9vw,44px)}}"""
    return h, c


def hero_tellis(a, d):
    h = f"""<section class="h-tellis" aria-labelledby="pk">
  <svg class="h-tellised" aria-hidden="true" focusable="false"><defs><pattern id="tellis" width="120" height="88" patternUnits="userSpaceOnUse">
    <rect width="120" height="88" fill="#E7D6CC"/>
    <rect x="1.5" y="1.5" width="117" height="41" fill="#9C3D2B"/><rect x="-58.5" y="45.5" width="117" height="41" fill="#A84634"/><rect x="61.5" y="45.5" width="117" height="41" fill="#8F3726"/>
  </pattern></defs><rect width="100%" height="100%" fill="url(#tellis)"/></svg>
  <div class="wrap h-tellis-wrap">
    <div class="h-tellis-kast">
      <h1 id="pk">{E(d["h1"])}</h1>
      {lead(a)}
      {nupud(a)}
    </div>
  </div>
</section>"""
    c = """.h-tellis{position:relative;padding:96px 0;background:#9C3D2B}
.h-tellised{position:absolute;inset:0;width:100%;height:100%}
.h-tellis-wrap{position:relative}
.h-tellis-kast{background:#fff;max-width:700px;padding:48px 44px;border-left:12px solid #9C3D2B}
.h-tellis-kast h1{font-size:clamp(40px,5.6vw,76px);line-height:.98;font-weight:900;letter-spacing:-.03em;margin:0 0 22px}
@media (max-width:600px){.h-tellis-kast{padding:32px 22px}}"""
    return h, c


def hero_dolomiit(a, d):
    h = f"""<section class="h-dolo" aria-labelledby="pk">
  <div class="wrap h-dolo-sisu">
    <h1 id="pk">{E(d["h1"])}</h1>
    {lead(a)}
    {nupud(a)}
  </div>
  <div class="h-kihid" aria-hidden="true"><span></span><span></span><span></span><span></span></div>
</section>"""
    c = """.h-dolo{background:#EEEBE4;padding-top:84px}
.h-dolo h1{font-size:clamp(44px,7vw,100px);line-height:.95;font-weight:800;letter-spacing:-.03em;margin:0 0 24px;color:#2E4A3A;max-width:10em}
.h-dolo-sisu{padding-bottom:56px}
.h-kihid span{display:block;height:22px}
.h-kihid span:nth-child(1){background:#D9D3C7;height:14px}.h-kihid span:nth-child(2){background:#C8C0B1}.h-kihid span:nth-child(3){background:#B3AA99;height:30px}.h-kihid span:nth-child(4){background:#2E4A3A;height:40px}"""
    return h, c


def hero_kangelane(a, d):
    h = f"""<section class="h-kangel" aria-labelledby="pk">
  <div class="wrap h-kangel-sisu">
    <div class="h-plahvatus" aria-hidden="true"><span>{E(a["lyhinimi"].upper())}</span></div>
    <div>
      <h1 id="pk">{E(d["h1"])}</h1>
      {lead(a)}
      {nupud(a)}
    </div>
  </div>
</section>"""
    c = """.h-kangel{background:#1D3FB8;color:#fff;padding:72px 0 88px;background-image:radial-gradient(rgba(255,255,255,.14) 2px,transparent 2px);background-size:18px 18px}
.h-kangel-sisu{display:grid;grid-template-columns:1fr 1.1fr;gap:40px;align-items:center}
.h-plahvatus{aspect-ratio:1;background:#FFD02E;display:flex;align-items:center;justify-content:center;clip-path:polygon(50% 0,61% 22%,85% 8%,78% 34%,100% 40%,80% 55%,95% 78%,68% 72%,62% 100%,48% 78%,28% 96%,28% 70%,2% 74%,18% 52%,0 32%,26% 30%,18% 6%,40% 22%)}
.h-plahvatus span{font-family:var(--pea),sans-serif;font-weight:900;font-size:clamp(18px,2.9vw,40px);color:#1D3FB8;transform:rotate(-8deg);letter-spacing:-.02em}
.h-kangel h1{font-size:clamp(40px,5.6vw,78px);line-height:.98;font-weight:900;letter-spacing:-.03em;margin:0 0 22px}
.h-kangel .lead{color:#E3E9FB}
.h-kangel .nupp.pea{background:#FFD02E;color:#14286E}
.h-kangel .nupp.teine{color:#fff}
@media (max-width:860px){.h-kangel-sisu{grid-template-columns:1fr}.h-plahvatus{max-width:300px}}"""
    return h, c


def hero_ok(a, d):
    h = f"""<section class="h-ok" aria-labelledby="pk">
  <div class="wrap h-ok-sisu">
    <svg class="h-linnuke" viewBox="0 0 200 160" aria-hidden="true" focusable="false"><path d="M14 86l52 52L186 18" fill="none" stroke="#fff" stroke-width="26" stroke-linecap="round" stroke-linejoin="round"/></svg>
    <div>
      <h1 id="pk">{E(d["h1"])}</h1>
      {lead(a)}
      {nupud(a)}
    </div>
  </div>
</section>"""
    c = """.h-ok{background:#1E7A45;color:#fff;padding:80px 0 96px}
.h-ok-sisu{display:grid;grid-template-columns:auto 1fr;gap:56px;align-items:center}
.h-linnuke{width:clamp(140px,22vw,300px);height:auto}
.h-ok h1{font-size:clamp(48px,8vw,116px);line-height:.92;font-weight:800;letter-spacing:-.04em;margin:0 0 24px}
.h-ok .lead{color:#E2F2E8}
.h-ok .nupp.pea{background:#fff;color:#155B33}
.h-ok .nupp.teine{color:#fff}
@media (max-width:760px){.h-ok-sisu{grid-template-columns:1fr;gap:28px}.h-linnuke{width:120px}}"""
    return h, c


# ======================================================================
# Kujunduste register
# ======================================================================

KUJUNDUSED = {
    "plaan": dict(hero=hero_plaan, pea="Fraunces", keha="Manrope", theme="#10284A", h1="Viimistlus, mis peab plaanist kinni.",
                  teenused="read", galerii="mosaiik", kaik="ajajoon", pais="tume",
                  vars=v(pea="'Fraunces'", keha="'Manrope'", pea_kaal="700", bg="#F6F8FA", fg="#13233A", muted="#4A5568", surface="#E7EDF3", line="#CBD5E1",
                         accent="#D9A441", accent_fg="#10284A", dark="#10284A", dark_fg="#FFFFFF", dark_accent="#D9A441", fookus="#D9A441"),
                  css=".pais-tume{background:#10284A;color:#fff}.pais-tume .logo-mark{width:18px;height:18px;border:2px solid #D9A441}"),
    "palett": dict(hero=hero_palett, pea="Syne", keha="Manrope", theme="#3B2DB8", h1="Iga toon omal kohal.",
                   teenused="plaadid", galerii="polaroid", kaik="rida", pais="hele",
                   vars=v(pea="'Syne'", keha="'Manrope'", pea_ls="-0.03em", bg="#FFFFFF", fg="#1B1B1F", muted="#4D4D57", surface="#F1EFFA", line="#DCD8EE",
                          accent="#3B2DB8", accent_fg="#FFFFFF", dark="#1B1B1F", dark_fg="#FFFFFF", dark_accent="#E2A33B", fookus="#3B2DB8", raadius="10px"),
                   css=".pais-hele .logo-mark{width:22px;height:22px;border-radius:50%;background:conic-gradient(#3B2DB8 0 25%,#E2A33B 0 50%,#2F8F6B 0 75%,#C8475B 0)}"),
    "teip": dict(hero=hero_teip, pea="Unbounded", keha="Inter", theme="#111111", h1="Remont tehtud. Tööplats korras.",
                 teenused="numbrid", galerii="ruudustik", kaik="redel", pais="must",
                 vars=v(pea="'Unbounded'", keha="'Inter'", pea_kaal="900", pea_ls="-0.03em", bg="#FAFAF7", fg="#111111", muted="#4A4A45", surface="#EFEEE8", line="#D8D6CC",
                        accent="#111111", accent_fg="#FFD23F", dark="#111111", dark_fg="#FFFFFF", dark_accent="#FFD23F", fookus="#E0A800", raadius="0px"),
                 css=".pais-must{background:#111;color:#fff}.pais-must .logo-mark{width:20px;height:20px;background:repeating-linear-gradient(-45deg,#FFD23F 0 4px,#111 4px 8px)}"),
    "ruutmeeter": dict(hero=hero_ruutmeeter, pea="Space Grotesk", keha="Space Grotesk", theme="#0F6B5C", h1="Iga ruutmeeter paigas.",
                       teenused="veerud", galerii="ruudustik", kaik="kaardid", pais="hele",
                       vars=v(pea="'Space Grotesk'", keha="'Space Grotesk'", pea_kaal="700", pea_ls="-0.03em", bg="#F5F7F7", fg="#16211F", muted="#46524F", surface="#E4EBEA", line="#C9D6D3",
                              accent="#0F6B5C", accent_fg="#FFFFFF", dark="#1B3D37", dark_fg="#FFFFFF", dark_accent="#F2B544", fookus="#0F6B5C", raadius="2px"),
                       css=".pais-hele .logo-mark{width:22px;height:22px;background:linear-gradient(90deg,#0F6B5C 50%,#F2B544 50%) 0 0/11px 11px}"),
    "horisont": dict(hero=hero_horisont, pea="Instrument Serif", keha="Familjen Grotesk", theme="#173E58", h1="Rahulik remont, sirge tulemus.",
                     teenused="read", galerii="riba", kaik="rida", pais="taevas",
                     vars=v(pea="'Instrument Serif'", keha="'Familjen Grotesk'", pea_kaal="400", pea_ls="-0.01em", bg="#FBFCFD", fg="#13324A", muted="#4A5F70", surface="#EAF2F8", line="#C9DBE7",
                            accent="#173E58", accent_fg="#FFFFFF", dark="#173E58", dark_fg="#FFFFFF", dark_accent="#9FD0EA", fookus="#2A6787", raadius="999px"),
                     css=".pais-taevas{background:#EAF2F8}.pais-taevas .logo-mark{width:24px;height:12px;border-radius:12px 12px 0 0;background:#2A6787}"),
    "pits": dict(hero=hero_pits, pea="Fraunces", keha="Manrope", theme="#3E5B4A", h1="Hoolikas viimistlus Läänemaa majadele.",
                 teenused="kaardid", galerii="mosaiik", kaik="ajajoon", pais="pits",
                 vars=v(pea="'Fraunces'", keha="'Manrope'", pea_kaal="400", pea_ls="0", bg="#FFFFFF", fg="#22322A", muted="#4F5E55", surface="#EDF2EE", line="#CFDBD2",
                        accent="#3E5B4A", accent_fg="#FFFFFF", dark="#2D4437", dark_fg="#FFFFFF", dark_accent="#C9DCCD", fookus="#3E5B4A", raadius="8px"),
                 css=".pais-pits{background:#3E5B4A;color:#fff}.pais-pits .logo{font-style:italic}.pais-pits .logo-mark{width:20px;height:20px;border-radius:50%;border:2px dotted #fff}.sek-teenused{padding-top:140px}"),
    "kalasaba": dict(hero=hero_kalasaba, pea="DM Serif Display", keha="Manrope", theme="#0E4D5C", h1="Plaat, vuuk ja nurk, mis klapivad.",
                     teenused="veerud", galerii="ruudustik", kaik="rida", pais="hele",
                     vars=v(pea="'DM Serif Display'", keha="'Manrope'", pea_kaal="400", pea_ls="0", bg="#FBFCFC", fg="#132A30", muted="#475B60", surface="#E6EFF1", line="#C7D7DB",
                            accent="#0E4D5C", accent_fg="#FFFFFF", dark="#0E4D5C", dark_fg="#FFFFFF", dark_accent="#E7C86A", fookus="#0E4D5C", raadius="2px"),
                     css=".pais-hele .logo-mark{width:22px;height:22px;background:linear-gradient(45deg,#0E4D5C 45%,#fff 45% 55%,#0E4D5C 55%)}"),
    "kontroll": dict(hero=hero_kontroll, pea="Bricolage Grotesque", keha="Manrope", theme="#24452F", h1="Hooldus ja viimistlus ühe kõnega.",
                     teenused="numbrid", galerii="polaroid", kaik="kaardid", pais="tume",
                     vars=v(pea="'Bricolage Grotesque'", keha="'Manrope'", pea_ls="-0.03em", bg="#FFFDF7", fg="#1E2B22", muted="#4E5A51", surface="#EEF2EC", line="#D3DCD2",
                            accent="#24452F", accent_fg="#FFFFFF", dark="#24452F", dark_fg="#FFFFFF", dark_accent="#E9B44C", fookus="#24452F", raadius="6px"),
                     css=".pais-tume{background:#24452F;color:#fff}.pais-tume .logo-mark{width:20px;height:20px;border-radius:4px;background:#E9B44C}"),
    "joonlaud": dict(hero=hero_joonlaud, pea="Archivo", keha="Archivo", theme="#1D1D1B", h1="Üks töö korraga, korralikult.",
                     teenused="read", galerii="riba", kaik="redel", pais="betoon",
                     vars=v(pea="'Archivo'", keha="'Archivo'", pea_kaal="900", pea_ls="-0.03em", bg="#F7F7F5", fg="#1D1D1B", muted="#4C4C48", surface="#E4E4E1", line="#CFCFCA",
                            accent="#B23A0E", accent_fg="#FFFFFF", dark="#1D1D1B", dark_fg="#FFFFFF", dark_accent="#F2C230", fookus="#B23A0E", raadius="0px"),
                     css=".pais-betoon{background:#E4E4E1}.pais-betoon .logo-mark{width:26px;height:10px;background:#F2C230;border:2px solid #1D1D1B}"),
    "radiaal": dict(hero=hero_radiaal, pea="Epilogue", keha="Epilogue", theme="#17161A", h1="Ida-Virumaa viimistlus aastast 2003.",
                    teenused="kaardid", galerii="mosaiik", kaik="ajajoon", pais="must",
                    vars=v(pea="'Epilogue'", keha="'Epilogue'", pea_ls="-0.03em", bg="#FAF8F6", fg="#17161A", muted="#4E4A47", surface="#F0EAE4", line="#DCD2C9",
                           accent="#9A5524", accent_fg="#FFFFFF", dark="#17161A", dark_fg="#FFFFFF", dark_accent="#D9884A", fookus="#9A5524", raadius="999px"),
                    css=".pais-must{background:#17161A;color:#fff}.pais-must .logo-mark{width:22px;height:22px;border-radius:50%;background:repeating-radial-gradient(circle,#D9884A 0 2px,transparent 2px 5px)}.t-kaardid .t-ikoon{border-radius:50%}"),

    "kald": dict(hero=hero_kald, pea="Archivo", keha="Inter", theme="#2340B0", h1="Narva remont algusest lõpuni.",
                 teenused="kaardid", galerii="ruudustik", kaik="rida", pais="hele",
                 vars=v(pea="'Archivo'", keha="'Inter'", pea_ls="-0.03em", bg="#FFFFFF", fg="#121A33", muted="#4A5168", surface="#EEF1FA", line="#D3D9EE",
                        accent="#2340B0", accent_fg="#FFFFFF", dark="#121A33", dark_fg="#FFFFFF", dark_accent="#8EA2F0", fookus="#2340B0", raadius="4px"),
                 css=".pais-hele .logo-mark{width:20px;height:20px;background:#2340B0;clip-path:polygon(0 0,100% 0,70% 100%,0 100%)}"),
    "laudis": dict(hero=hero_laudis, pea="Fraunces", keha="Familjen Grotesk", theme="#3B2618", h1="Soe puit ja korralik viimistlus.",
                   teenused="numbrid", galerii="polaroid", kaik="ajajoon", pais="puit",
                   vars=v(pea="'Fraunces'", keha="'Familjen Grotesk'", pea_kaal="900", bg="#FBF6F0", fg="#2B1C12", muted="#5B4A3E", surface="#F1E6DA", line="#DDCBB8",
                          accent="#3B2618", accent_fg="#FFFFFF", dark="#3B2618", dark_fg="#FFFFFF", dark_accent="#F0A35E", fookus="#B5652A", raadius="6px"),
                   css=".pais-puit{background:#3B2618;color:#F7EBDD}.pais-puit .logo-mark{width:22px;height:22px;border-radius:50%;background:repeating-radial-gradient(circle,#B07A4C 0 2px,#8A5A35 2px 4px)}"),
    "lubivarv": dict(hero=hero_lubivarv, pea="Instrument Serif", keha="Manrope", theme="#5B2E4E", h1="Seinad, mis näevad välja nagu plaanitud.",
                     teenused="read", galerii="mosaiik", kaik="rida", pais="hele",
                     vars=v(pea="'Instrument Serif'", keha="'Manrope'", pea_kaal="400", pea_ls="-0.01em", bg="#FCFAFB", fg="#2A1825", muted="#5A4954", surface="#F2EAF0", line="#DDCFD8",
                            accent="#5B2E4E", accent_fg="#FFFFFF", dark="#2A1825", dark_fg="#FFFFFF", dark_accent="#E7B8D6", fookus="#5B2E4E", raadius="999px"),
                     css=".pais-hele .logo{font-style:italic}.pais-hele .logo-mark{width:22px;height:22px;border-radius:50%;background:radial-gradient(circle at 30% 30%,#9A5C86,#5B2E4E)}"),
    "pintsel": dict(hero=hero_pintsel, pea="DM Serif Display", keha="Familjen Grotesk", theme="#B3262E", h1="Sile nagu siid.",
                    teenused="veerud", galerii="riba", kaik="kaardid", pais="hele",
                    vars=v(pea="'DM Serif Display'", keha="'Familjen Grotesk'", pea_kaal="400", pea_ls="0", bg="#FFFFFF", fg="#2A1416", muted="#5C4A4B", surface="#FBEDEC", line="#EBCFCD",
                           accent="#B3262E", accent_fg="#FFFFFF", dark="#2A1416", dark_fg="#FFFFFF", dark_accent="#F0A8A5", fookus="#B3262E", raadius="999px"),
                    css=".pais-hele .logo-mark{width:30px;height:10px;border-radius:10px;background:linear-gradient(90deg,#B3262E,#F0A8A5)}"),
    "raps": dict(hero=hero_raps, pea="Bricolage Grotesque", keha="Inter", theme="#E3AE00", h1="Raplamaa remont, korralikult.",
                 teenused="plaadid", galerii="ruudustik", kaik="redel", pais="taevas",
                 vars=v(pea="'Bricolage Grotesque'", keha="'Inter'", pea_ls="-0.03em", bg="#FFFFFF", fg="#1E2A33", muted="#4D5964", surface="#FFF4CC", line="#EADFB0",
                        accent="#1E2A33", accent_fg="#F2C300", dark="#1E2A33", dark_fg="#FFFFFF", dark_accent="#F2C300", fookus="#B38600", raadius="8px"),
                 css=".pais-taevas{background:#DCEBF6}.pais-taevas .logo-mark{width:22px;height:22px;border-radius:50%;background:#F2C300}"),
    "rullitriibud": dict(hero=hero_rullitriibud, pea="Syne", keha="Inter", theme="#2F6B3A", h1="Värv peale, triip sirge.",
                         teenused="kaardid", galerii="polaroid", kaik="rida", pais="hele",
                         vars=v(pea="'Syne'", keha="'Inter'", pea_ls="-0.03em", bg="#FBFCFA", fg="#18261B", muted="#4A584C", surface="#EAF2E5", line="#CFDFC7",
                                accent="#2F6B3A", accent_fg="#FFFFFF", dark="#18261B", dark_fg="#FFFFFF", dark_accent="#C9DFA8", fookus="#2F6B3A", raadius="999px"),
                         css=".pais-hele .logo-mark{width:12px;height:24px;border-radius:6px;background:#2F6B3A;box-shadow:8px 0 0 #7BAF6B,16px 0 0 #C9DFA8;margin-right:16px}.t-kaardid .t-ikoon{border-radius:999px;width:56px;height:14px}"),
    "tellis": dict(hero=hero_tellis, pea="Archivo", keha="Archivo", theme="#9C3D2B", h1="Tartu korteritele ja majadele.",
                   teenused="veerud", galerii="mosaiik", kaik="kaardid", pais="hele",
                   vars=v(pea="'Archivo'", keha="'Archivo'", pea_kaal="900", pea_ls="-0.03em", bg="#FFFFFF", fg="#2A1A16", muted="#5A4A45", surface="#F6ECE7", line="#E3CFC6",
                          accent="#9C3D2B", accent_fg="#FFFFFF", dark="#2A1A16", dark_fg="#FFFFFF", dark_accent="#E9A08C", fookus="#9C3D2B", raadius="0px"),
                   css=".pais-hele .logo-mark{width:26px;height:14px;background:#9C3D2B;box-shadow:inset 0 -3px 0 #E7D6CC}"),
    "dolomiit": dict(hero=hero_dolomiit, pea="Epilogue", keha="Manrope", theme="#2E4A3A", h1="Saaremaa maalritööd.",
                     teenused="numbrid", galerii="riba", kaik="ajajoon", pais="kivi",
                     vars=v(pea="'Epilogue'", keha="'Manrope'", pea_ls="-0.03em", bg="#FAF9F6", fg="#1F2B24", muted="#4F5A53", surface="#EEEBE4", line="#D6D0C4",
                            accent="#2E4A3A", accent_fg="#FFFFFF", dark="#2E4A3A", dark_fg="#FFFFFF", dark_accent="#D9D3C7", fookus="#2E4A3A", raadius="3px"),
                     css=".pais-kivi{background:#EEEBE4}.pais-kivi .logo-mark{width:24px;height:20px;background:linear-gradient(#C8C0B1 0 33%,#B3AA99 33% 66%,#2E4A3A 66%)}"),
    "kangelane": dict(hero=hero_kangelane, pea="Unbounded", keha="Inter", theme="#1D3FB8", h1="Krohvman tuleb appi.",
                      teenused="plaadid", galerii="ruudustik", kaik="kaardid", pais="sinine",
                      vars=v(pea="'Unbounded'", keha="'Inter'", pea_kaal="900", pea_ls="-0.03em", bg="#FFFFFF", fg="#14286E", muted="#47507A", surface="#FFF6D6", line="#E8DDB0",
                             accent="#1D3FB8", accent_fg="#FFFFFF", dark="#14286E", dark_fg="#FFFFFF", dark_accent="#FFD02E", fookus="#1D3FB8", raadius="6px"),
                      css=".pais-sinine{background:#14286E;color:#fff}.pais-sinine .logo-mark{width:22px;height:22px;background:#FFD02E;clip-path:polygon(50% 0,62% 35%,100% 38%,70% 60%,80% 100%,50% 76%,20% 100%,30% 60%,0 38%,38% 35%)}"),
    "ok": dict(hero=hero_ok, pea="Syne", keha="Manrope", theme="#1E7A45", h1="Okei. Teeme ära.",
               teenused="read", galerii="mosaiik", kaik="redel", pais="hele",
               vars=v(pea="'Syne'", keha="'Manrope'", pea_ls="-0.04em", bg="#FFFFFF", fg="#132A1C", muted="#4A5C50", surface="#E8F4EC", line="#CBE3D3",
                      accent="#1E7A45", accent_fg="#FFFFFF", dark="#132A1C", dark_fg="#FFFFFF", dark_accent="#7FD39E", fookus="#1E7A45", raadius="999px"),
               css=".pais-hele .logo-mark{width:22px;height:22px;border-radius:50%;background:#1E7A45;box-shadow:inset 0 0 0 5px #E8F4EC}"),
}
