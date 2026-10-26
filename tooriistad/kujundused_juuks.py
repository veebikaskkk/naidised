"""Juuksurite kujundused (400 € pakett broneerimiskalendriga).

15 avaploki ideed juuksuri maailmast. Iga firma saab oma paleti, fondid, sektsioonide
paigutuse ja pealkirja, nii et ka sama ideega lehed näevad välja erinevad.
"""
from sisu import E
from kujundused import nupud, lead
from vahend import pal, baas, pais_css, mix

K = {}


def _sisu(a, d):
    return f'<h1 id="pk">{E(d["h1"])}</h1>{lead(a)}{nupud(a)}'


def _koht(tekst, cls="h-foto"):
    return f'<div class="kohataide {cls}" role="img" aria-label="Kohatäide: {tekst.lower()}"><span>{E(tekst)}</span></div>'


def hero_kamm(a, d):
    P = d["p"]
    hambad = "".join(f'<rect x="{8 + i * 11}" y="30" width="6" height="{78 if i % 2 else 64}" rx="3"/>' for i in range(35))
    h = f"""<section class="h-kamm" aria-labelledby="pk">
  <div class="wrap h-kamm-sisu">{_sisu(a, d)}</div>
  <svg class="h-kamm-svg" viewBox="0 0 400 120" aria-hidden="true" focusable="false" fill="{P['ha']}"><rect x="0" y="0" width="400" height="36" rx="12"/>{hambad}</svg>
</section>"""
    c = baas("h-kamm", P, "96px 0 180px") + """.h-kamm-sisu{position:relative;z-index:1}.h-kamm h1{max-width:11em}
.h-kamm-svg{position:absolute;right:-40px;bottom:-24px;width:min(560px,70vw);transform:rotate(-8deg);opacity:.9}"""
    return h, c


def hero_kaarid(a, d):
    P = d["p"]
    h = f"""<section class="h-kaar" aria-labelledby="pk">
  <div class="wrap h-kaar-sisu"><div>{_sisu(a, d)}</div>
  <svg class="h-kaar-svg" viewBox="0 0 340 300" aria-hidden="true" focusable="false">
    <path d="M118 182 L318 22 L330 38 L136 198Z" fill="{P['ha']}"/><path d="M150 206 L330 96 L336 116 L160 222Z" fill="{mix(P['ha'], P['hb'], .7)}"/>
    <circle cx="82" cy="214" r="44" fill="none" stroke="{P['hf']}" stroke-width="14"/><circle cx="168" cy="250" r="40" fill="none" stroke="{P['hf']}" stroke-width="14"/>
    <circle cx="150" cy="196" r="9" fill="{P['hf']}"/>
  </svg></div>
</section>"""
    c = baas("h-kaar", P) + """.h-kaar-sisu{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:48px;align-items:center}
.h-kaar-svg{width:100%;max-width:380px;justify-self:end}
@media (max-width:820px){.h-kaar-sisu{grid-template-columns:minmax(0,1fr)}.h-kaar-svg{max-width:220px;justify-self:start;order:-1}}"""
    return h, c


def hero_peegel(a, d):
    P = d["p"]
    h = f"""<section class="h-peegel" aria-labelledby="pk">
  <div class="wrap h-peegel-sisu"><div>{_sisu(a, d)}</div><div class="h-raam">{_koht("Salongi foto")}</div></div>
</section>"""
    c = baas("h-peegel", P, "72px 0 88px") + f""".h-peegel-sisu{{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,1fr);gap:56px;align-items:center}}
.h-raam{{border:12px solid {P['ha']};border-radius:50%;padding:10px;aspect-ratio:3/4;max-width:380px;justify-self:end;width:100%}}
.h-raam .kohataide{{height:100%;border-radius:50%;min-height:0}}
@media (max-width:820px){{.h-peegel-sisu{{grid-template-columns:minmax(0,1fr)}}.h-raam{{max-width:220px;justify-self:start;order:-1;border-width:8px}}}}"""
    return h, c


def hero_lokid(a, d):
    P = d["p"]
    jooned = "".join(f'<path d="M-20 {40 + i * 46} C 120 {i * 46}, 220 {80 + i * 46}, 360 {40 + i * 46} S 600 {i * 46}, 740 {40 + i * 46} S 980 {80 + i * 46}, 1220 {40 + i * 46}"/>' for i in range(9))
    h = f"""<section class="h-lokk" aria-labelledby="pk">
  <svg class="h-lokk-svg" viewBox="0 0 1200 440" preserveAspectRatio="none" aria-hidden="true" focusable="false" fill="none" stroke="{P['ha']}" stroke-width="3">{jooned}</svg>
  <div class="wrap h-lokk-sisu">{_sisu(a, d)}</div>
</section>"""
    c = baas("h-lokk", P, "112px 0 120px") + f""".h-lokk-svg{{position:absolute;inset:0;width:100%;height:100%;opacity:.28}}
.h-lokk-sisu{{position:relative;text-align:center;display:flex;flex-direction:column;align-items:center}}
.h-lokk h1{{max-width:12em}}.h-lokk .lead{{margin-left:auto;margin-right:auto}}.h-lokk .nupud{{justify-content:center}}"""
    return h, c


def hero_post(a, d):
    P = d["p"]
    h = f"""<section class="h-post" aria-labelledby="pk">
  <div class="wrap h-post-sisu"><div>{_sisu(a, d)}</div><div class="h-post-sammas" aria-hidden="true"><span></span></div></div>
</section>"""
    c = baas("h-post", P, "72px 0 80px") + f""".h-post-sisu{{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:64px;align-items:center}}
.h-post-sammas{{width:96px;height:380px;border-radius:48px;padding:10px;background:{P['hf']}}}
.h-post-sammas span{{display:block;height:100%;border-radius:40px;background:repeating-linear-gradient(-35deg,{P['ha']} 0 22px,{P['hb']} 22px 34px,{mix(P['ha'], P['hf'], .5)} 34px 56px,{P['hb']} 56px 68px)}}
@media (max-width:760px){{.h-post-sisu{{grid-template-columns:minmax(0,1fr) 44px;gap:20px}}.h-post-sammas{{width:44px;height:240px;padding:6px}}}}"""
    return h, c


def hero_toonid(a, d):
    P = d["p"]
    toonid = ["#2B1B12", "#5A3825", "#8A5A3B", "#B98451", "#D9B47A", "#EAD5A8", "#9E3A2A", "#6B2A3A"]
    ringid = "".join(f'<span class="t{i}"></span>' for i in range(len(toonid)))
    tcss = "".join(f".h-toon-rida .t{i}{{background:{x}}}" for i, x in enumerate(toonid))
    h = f"""<section class="h-toon" aria-labelledby="pk">
  <div class="wrap">{_sisu(a, d)}<div class="h-toon-rida" aria-hidden="true">{ringid}</div></div>
</section>"""
    c = baas("h-toon", P, "88px 0 72px") + f""".h-toon h1{{max-width:11em}}
.h-toon-rida{{display:flex;margin-top:56px}}
.h-toon-rida span{{width:clamp(44px,9vw,104px);aspect-ratio:1;border-radius:50%;border:4px solid {P['hb']};margin-right:-14px}}
{tcss}"""
    return h, c


def hero_salgud(a, d):
    P = d["p"]
    salgud = "".join(f'<path d="M{-60 + i * 34} -20 C {200 + i * 20} {120 + i * 8}, {80 + i * 30} {300 - i * 6}, {420 + i * 26} 520" stroke-width="{2 + (i % 4)}"/>' for i in range(16))
    h = f"""<section class="h-salk" aria-labelledby="pk">
  <svg class="h-salk-svg" viewBox="0 0 900 500" preserveAspectRatio="xMaxYMid slice" aria-hidden="true" focusable="false" fill="none" stroke="{P['ha']}">{salgud}</svg>
  <div class="wrap h-salk-sisu">{_sisu(a, d)}</div>
</section>"""
    c = baas("h-salk", P, "104px 0 112px") + f""".h-salk-svg{{position:absolute;right:0;top:0;height:100%;width:62%;opacity:.55}}
.h-salk-sisu{{position:relative}}.h-salk h1{{max-width:10em}}
@media (max-width:760px){{.h-salk-svg{{width:100%;opacity:.18}}}}"""
    return h, c


def hero_kalender(a, d):
    P = d["p"]
    ajad = "".join(f'<span class="{"v" if x == "12:00" else ""}">{x}</span>' for x in ("10:00", "11:00", "12:00", "14:00", "15:00", "17:00"))
    h = f"""<section class="h-kal" aria-labelledby="pk">
  <div class="wrap h-kal-sisu"><div>{_sisu(a, d)}</div>
  <div class="h-kal-kaart" aria-hidden="true"><b>Vali aeg</b><div class="h-kal-p"><span>E</span><span>T</span><span class="v">K</span><span>N</span><span>R</span><span>L</span></div><div class="h-kal-ajad">{ajad}</div></div></div>
</section>"""
    kb = P["bg"]
    c = baas("h-kal", P) + f""".h-kal-sisu{{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,1fr);gap:56px;align-items:center}}
.h-kal-kaart{{background:{kb};color:{P['fg']};border-radius:20px;padding:28px;box-shadow:0 24px 60px rgba(0,0,0,.18);transform:rotate(2deg);max-width:380px;justify-self:end;width:100%}}
.h-kal-kaart b{{display:block;font-family:var(--pea),sans-serif;font-size:22px;margin-bottom:16px}}
.h-kal-p,.h-kal-ajad{{display:grid;grid-template-columns:repeat(6,1fr);gap:6px;margin-bottom:12px}}
.h-kal-ajad{{grid-template-columns:repeat(3,1fr);margin:0}}
.h-kal-p span,.h-kal-ajad span{{text-align:center;padding:8px 0;border-radius:8px;border:1.5px solid {mix(P['fg'], kb, .25)};font-weight:600;font-size:14px}}
.h-kal-kaart .v{{background:{P['acc']};color:{P['acc_fg']};border-color:{P['acc']}}}
@media (max-width:820px){{.h-kal-sisu{{grid-template-columns:minmax(0,1fr)}}.h-kal-kaart{{justify-self:start;transform:none}}}}"""
    return h, c


def hero_foon(a, d):
    P = d["p"]
    h = f"""<section class="h-foon" aria-labelledby="pk">
  <div class="wrap h-foon-sisu"><div>{_sisu(a, d)}</div>
  <svg class="h-foon-svg" viewBox="0 0 360 300" aria-hidden="true" focusable="false">
    <g stroke="{P['ha']}" stroke-width="5" stroke-linecap="round" stroke-dasharray="14 12"><line x1="20" y1="70" x2="96" y2="70"/><line x1="8" y1="104" x2="96" y2="104"/><line x1="20" y1="138" x2="96" y2="138"/></g>
    <rect x="104" y="72" width="70" height="64" rx="10" fill="{mix(P['hf'], P['hb'], .55)}"/>
    <circle cx="232" cy="104" r="76" fill="{P['hf']}"/><circle cx="232" cy="104" r="34" fill="{P['ha']}"/>
    <path d="M214 172 L250 172 L272 290 L232 290Z" fill="{P['hf']}"/>
  </svg></div>
</section>"""
    c = baas("h-foon", P) + """.h-foon-sisu{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:40px;align-items:center}
.h-foon-svg{width:100%;max-width:360px;justify-self:end}
@media (max-width:820px){.h-foon-sisu{grid-template-columns:minmax(0,1fr)}.h-foon-svg{max-width:200px;justify-self:start;order:-1}}"""
    return h, c


def hero_ajakiri(a, d):
    P = d["p"]
    aasta = f"Aastast {a['aasta']}" if a.get("aasta") else a["piirkond"]
    h = f"""<section class="h-ajak" aria-labelledby="pk">
  <div class="wrap"><div class="h-ajak-rida" aria-hidden="true"><span>{E(a['lyhinimi'])}</span><span>{E(aasta)}</span></div>
  <div class="h-ajak-sisu">{_sisu(a, d)}</div><div class="h-ajak-rida alumine" aria-hidden="true"><span>Lõikus</span><span>Värv</span><span>Soeng</span></div></div>
</section>"""
    c = baas("h-ajak", P, "56px 0 64px", "clamp(40px,8vw,128px)", "font-style:italic") + f""".h-ajak-rida{{display:flex;justify-content:space-between;gap:16px;border-top:2px solid {P['hf']};border-bottom:1px solid {P['hf']};padding:10px 0;font-size:13px;letter-spacing:.18em;text-transform:uppercase;font-weight:600}}
.h-ajak-rida.alumine{{margin-top:48px}}
.h-ajak-sisu{{padding-top:48px}}
.h-ajak h1{{max-width:10em}}"""
    return h, c


def hero_kaar(a, d):
    P = d["p"]
    h = f"""<section class="h-kaarus" aria-labelledby="pk">
  <div class="wrap h-kaarus-sisu"><div>{_sisu(a, d)}</div><div class="h-kaared">{_koht("Salongi foto", "h-k1")}{_koht("Töö foto", "h-k2")}</div></div>
</section>"""
    c = baas("h-kaarus", P, "72px 0 0") + f""".h-kaarus-sisu{{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:48px;align-items:end}}
.h-kaarus-sisu>div:first-child{{padding-bottom:88px}}
.h-kaared{{display:grid;grid-template-columns:1fr 1fr;gap:16px;align-items:end}}
.h-kaared .kohataide{{border-radius:999px 999px 0 0;min-height:0;aspect-ratio:1/1.8;border:6px solid {P['ha']};border-bottom:0}}
.h-kaared .h-k2{{aspect-ratio:1/1.35}}
@media (max-width:820px){{.h-kaarus-sisu{{grid-template-columns:minmax(0,1fr)}}.h-kaarus-sisu>div:first-child{{padding-bottom:0}}.h-kaared{{max-width:320px}}}}"""
    return h, c


def hero_terrazzo(a, d):
    P = d["p"]
    t1, t2, t3 = P["ha"], P["hf"], mix(P["ha"], P["hb"], .5)
    h = f"""<section class="h-terr" aria-labelledby="pk">
  <div class="wrap"><div class="h-terr-kaart">{_sisu(a, d)}</div></div>
</section>"""
    c = (f".h-terr{{padding:96px 0;background:radial-gradient(circle at 12% 20%,{t1} 0 18px,transparent 19px),radial-gradient(circle at 80% 14%,{t2} 0 10px,transparent 11px),"
         f"radial-gradient(ellipse at 88% 70%,{t1} 0 30px,transparent 31px),radial-gradient(circle at 30% 86%,{t3} 0 22px,transparent 23px),"
         f"radial-gradient(circle at 60% 40%,{t3} 0 8px,transparent 9px),radial-gradient(circle at 6% 64%,{t2} 0 12px,transparent 13px),{P['hb']}}}\n"
         f".h-terr-kaart{{background:{P['bg']};color:{P['fg']};padding:clamp(28px,5vw,64px);border-radius:min(var(--raadius),24px);max-width:820px;box-shadow:0 20px 60px rgba(0,0,0,.12)}}\n"
         ".h-terr h1{font-size:clamp(34px,5.6vw,80px);line-height:1;font-weight:var(--pea-kaal);letter-spacing:var(--pea-ls);margin:0 0 24px}\n"
         ".h-terr .lead{color:var(--muted)}\n.h-terr .nupp.teine{color:var(--fg)}")
    return h, c


def hero_neoon(a, d):
    P = d["p"]
    h = f"""<section class="h-neoon" aria-labelledby="pk">
  <div class="wrap"><div class="h-neoon-raam">{_sisu(a, d)}</div></div>
</section>"""
    c = baas("h-neoon", P, "88px 0 96px", h1_lisa=f"text-shadow:0 0 18px {P['ha']},0 0 42px {P['ha']}") + f""".h-neoon-raam{{border:2px solid {P['ha']};border-radius:28px;padding:clamp(28px,6vw,72px);box-shadow:0 0 24px {P['ha']},inset 0 0 24px {P['ha']}}}"""
    return h, c


def hero_pool(a, d):
    P = d["p"]
    h = f"""<section class="h-pool" aria-labelledby="pk">
  <div class="h-pool-tekst"><div class="h-pool-sisemus">{_sisu(a, d)}</div></div>{_koht("Salongi foto", "h-pool-foto")}
</section>"""
    c = baas("h-pool", P, "0", "clamp(34px,4.8vw,76px)") + f""".h-pool{{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr)}}
.h-pool-tekst{{padding:88px 48px 96px max(28px,calc((100vw - 1180px)/2 + 28px))}}
.h-pool-sisemus{{max-width:600px}}
.h-pool-foto{{border-radius:0;min-height:520px;border-left:10px solid {P['ha']}}}
@media (max-width:820px){{.h-pool{{grid-template-columns:minmax(0,1fr)}}.h-pool-tekst{{padding:64px 18px 72px}}.h-pool-foto{{min-height:220px;border-left:0;border-top:10px solid {P['ha']}}}}}"""
    return h, c


def hero_vaht(a, d):
    P = d["p"]
    mullid = "".join(f'<span class="m{i}"></span>' for i in range(7))
    asend = [(4, 70, 120), (14, 16, 60), (20, 58, 34), (3, 30, 22), (12, 80, 80), (19, 6, 44), (1, 46, 160)]
    mcss = "".join(f".h-vaht-mullid .m{i}{{right:{r}%;top:{t}%;width:{s}px;height:{s}px}}" for i, (r, t, s) in enumerate(asend))
    h = f"""<section class="h-vaht" aria-labelledby="pk">
  <div class="h-vaht-mullid" aria-hidden="true">{mullid}</div>
  <div class="wrap h-vaht-sisu">{_sisu(a, d)}</div>
</section>"""
    c = baas("h-vaht", P, "104px 0 112px") + f""".h-vaht-mullid span{{position:absolute;border-radius:50%;border:3px solid {P['ha']};background:radial-gradient(circle at 30% 30%,{mix(P['hf'], P['hb'], .35)},transparent 40%)}}
{mcss}
.h-vaht-sisu{{position:relative}}.h-vaht h1{{max-width:10em}}.h-vaht .lead{{max-width:28em}}
@media (max-width:760px){{.h-vaht-mullid{{opacity:.35}}}}"""
    return h, c


HEROD = dict(kamm=hero_kamm, kaarid=hero_kaarid, peegel=hero_peegel, lokid=hero_lokid, post=hero_post, toonid=hero_toonid,
             salgud=hero_salgud, kalender=hero_kalender, foon=hero_foon, ajakiri=hero_ajakiri, kaar=hero_kaar,
             terrazzo=hero_terrazzo, neoon=hero_neoon, pool=hero_pool, vaht=hero_vaht)


def lisa(nimi, hero, h1, P, pea, keha, teen, gal, kaik, pais, logo, theme=None):
    K[nimi] = dict(hero=HEROD[hero], h1=h1, p=P, pea=pea, keha=keha, theme=theme or P["hb"], teenused=teen, galerii=gal,
                   kaik=kaik, pais=pais, vars=P["vars"], css=pais_css(pais, P, logo))


def F(n):
    return f"'{n}'"


# nimi, avaplokk, pealkiri, palett, fondid, teenused/galerii/käik, päis, logo
JUUKSURID = [
    ("j-lofty", "lokid", "Hea juuksepäev algab siit.",
     pal("#FFFBF7", "#2A1E1A", "#9C4A2F", "#2A1E1A", "#F2B8A0", "#F6E7DC", "#2A1E1A", "#9C4A2F", "18px", pea=F("Fraunces"), keha=F("Manrope"), pea_kaal="400"),
     "Fraunces", "Manrope", "read", "polaroid", "ajajoon", "hele", 0),
    ("j-theodor", "post", "Meeste juuksur Raekoja platsil.",
     pal("#FFFFFF", "#151B26", "#B3261E", "#151B26", "#FF9C94", "#151B26", "#FFFFFF", "#D8342B", "4px", pea=F("Archivo"), keha=F("Inter"), pea_kaal="900", pea_ls="-0.03em"),
     "Archivo", "Inter", "numbrid", "ruudustik", "rida", "tume", 4),
    ("j-kiitna", "kalender", "Juuksur kesklinnas.",
     pal("#FFFFFF", "#1C2333", "#3949AB", "#1C2333", "#A5B4FF", "#E8EBF8", "#1C2333", "#3949AB", "12px", pea=F("Bricolage Grotesque"), keha=F("Inter"), pea_kaal="800", pea_ls="-0.035em"),
     "Bricolage Grotesque", "Inter", "kaardid", "mosaiik", "kaardid", "hele", 1),
    ("j-salonjoi", "vaht", "Salong Haljalas.",
     pal("#F7FBFA", "#0F2A2A", "#0F766E", "#0F2A2A", "#7FE0D2", "#0F2A2A", "#FFFFFF", "#5ED3C3", "999px", pea=F("Syne"), keha=F("Manrope"), pea_kaal="800", pea_ls="-0.03em"),
     "Syne", "Manrope", "veerud", "riba", "redel", "varv", 2),
    ("j-kristanoli", "kaar", "Juuksur Elva kandis.",
     pal("#FCF8F2", "#2E2620", "#8A5A2B", "#2E2620", "#E7C08D", "#EFE3D2", "#2E2620", "#8A5A2B", "6px", pea=F("DM Serif Display"), keha=F("Manrope"), pea_kaal="400", pea_ls="0"),
     "DM Serif Display", "Manrope", "plaadid", "polaroid", "ajajoon", "hele", 3),
    ("j-parnu-salong", "kamm", "Pärnu juuksur, aeg ühe klikiga.",
     pal("#FFFFFF", "#10243A", "#0E5A8A", "#10243A", "#8CCBF2", "#10243A", "#FFFFFF", "#F2C14E", "8px", pea=F("Space Grotesk"), keha=F("Inter"), pea_kaal="700", pea_ls="-0.035em"),
     "Space Grotesk", "Inter", "kaardid", "ruudustik", "rida", "varv", 5),
    ("j-rosita", "ajakiri", "Salong Rosita.",
     pal("#FFF8F8", "#3A1620", "#A3214A", "#3A1620", "#F7A8BE", "#FBE6EA", "#3A1620", "#A3214A", "2px", pea=F("Instrument Serif"), keha=F("Inter"), pea_kaal="400", pea_ls="-0.01em"),
     "Instrument Serif", "Inter", "read", "mosaiik", "kaardid", "hele", 6),
    ("j-kaar-salongid", "kaarid", "Käärid, kamm ja hea jutt.",
     pal("#FFFFFF", "#141414", "#1F1F1F", "#141414", "#F5D33C", "#F5D33C", "#141414", "#141414", "0px", pea=F("Unbounded"), keha=F("Inter"), pea_kaal="900", pea_ls="-0.04em"),
     "Unbounded", "Inter", "numbrid", "riba", "redel", "hele", 7),
    ("j-bp-ilusalong", "neoon", "Ilu ja juuksed ühest kohast.",
     pal("#FFFFFF", "#1A1426", "#7C3AED", "#1A1426", "#D0B4FF", "#140F1F", "#FFFFFF", "#C084FC", "16px", pea=F("Syne"), keha=F("Inter"), pea_kaal="800", pea_ls="-0.03em"),
     "Syne", "Inter", "kaardid", "polaroid", "ajajoon", "tume", 8),
    ("j-rilja", "toonid", "Juuksur Pärnumaa lõunas.",
     pal("#FBFAF5", "#24301F", "#4D6B2E", "#24301F", "#C9E39A", "#E9EEDC", "#24301F", "#4D6B2E", "10px", pea=F("Epilogue"), keha=F("Manrope"), pea_kaal="800", pea_ls="-0.03em"),
     "Epilogue", "Manrope", "veerud", "ruudustik", "rida", "hele", 9),
    ("j-aminates", "peegel", "Vaata peeglisse ja naerata.",
     pal("#FFFFFF", "#1E1B2E", "#B4235A", "#1E1B2E", "#FFA3C7", "#1E1B2E", "#FFFFFF", "#FF7AAE", "14px", pea=F("Fraunces"), keha=F("Inter"), pea_kaal="900"),
     "Fraunces", "Inter", "plaadid", "mosaiik", "redel", "tume", 0),
    ("j-lavendel", "pool", "Meeste juuksur Kaupmehe tänaval.",
     pal("#FBFAFD", "#221C30", "#5B3E96", "#221C30", "#CBB6F2", "#E9E3F4", "#221C30", "#5B3E96", "4px", pea=F("Familjen Grotesk"), keha=F("Inter"), pea_kaal="700", pea_ls="-0.03em"),
     "Familjen Grotesk", "Inter", "read", "riba", "kaardid", "hele", 1),
    ("j-nona", "salgud", "Juuksed, mis jäävad meelde.",
     pal("#FFFDF9", "#2B211B", "#B0602A", "#2B211B", "#F5B98A", "#2B211B", "#FFFFFF", "#F09A5B", "8px", pea=F("DM Serif Display"), keha=F("Inter"), pea_kaal="400", pea_ls="0"),
     "DM Serif Display", "Inter", "numbrid", "polaroid", "ajajoon", "tume", 2),
    ("j-glamrim", "foon", "Viimsi juuksur.",
     pal("#FFFFFF", "#2A1730", "#9D2C8F", "#2A1730", "#F3A6E8", "#FBEAF7", "#2A1730", "#9D2C8F", "24px", pea=F("Bricolage Grotesque"), keha=F("Manrope"), pea_kaal="800", pea_ls="-0.04em"),
     "Bricolage Grotesque", "Manrope", "kaardid", "ruudustik", "redel", "hele", 3),
    ("j-edem", "terrazzo", "Edem Ilustuudio.",
     pal("#FFFFFF", "#22302C", "#2F7A63", "#22302C", "#9EE0C8", "#DCEBE4", "#22302C", "#E3A587", "16px", pea=F("Epilogue"), keha=F("Inter"), pea_kaal="800", pea_ls="-0.035em"),
     "Epilogue", "Inter", "veerud", "mosaiik", "rida", "hele", 4),
    ("j-jbspot", "post", "Lõikus ilma ootamata.",
     pal("#F5F5F2", "#121212", "#1F4FD1", "#121212", "#9DB6FF", "#F5F5F2", "#121212", "#1F4FD1", "6px", pea=F("Space Grotesk"), keha=F("Space Grotesk"), pea_kaal="700", pea_ls="-0.04em"),
     "Space Grotesk", "Space Grotesk", "read", "riba", "redel", "hele", 5),
    ("j-poisipea", "toonid", "Poisipea või pikad lokid.",
     pal("#FFFFFF", "#1D2433", "#E0523A", "#1D2433", "#FFB4A6", "#FFE9E3", "#1D2433", "#C2412C", "999px", pea=F("Unbounded"), keha=F("Manrope"), pea_kaal="700", pea_ls="-0.03em"),
     "Unbounded", "Manrope", "kaardid", "polaroid", "kaardid", "hele", 6),
    ("j-lelii", "lokid", "Saaremaa ilusalong.",
     pal("#F8FBFD", "#11293B", "#1F6F96", "#11293B", "#9BD3F0", "#11293B", "#FFFFFF", "#7FC7EA", "10px", pea=F("Instrument Serif"), keha=F("Manrope"), pea_kaal="400", pea_ls="-0.01em"),
     "Instrument Serif", "Manrope", "plaadid", "ruudustik", "ajajoon", "varv", 7),
    ("j-patsike", "kamm", "Patsid, lõikus ja värv.",
     pal("#FFFCF5", "#2E2412", "#A15C00", "#2E2412", "#F6C76B", "#F8E7C4", "#2E2412", "#A15C00", "6px", pea=F("Archivo"), keha=F("Manrope"), pea_kaal="800", pea_ls="-0.03em"),
     "Archivo", "Manrope", "numbrid", "mosaiik", "rida", "hele", 8),
    ("j-mari-liisi", "peegel", "Ilutuba Kiilis.",
     pal("#FFFDFB", "#33232A", "#9A3B5C", "#33232A", "#F2AFC4", "#F6E6EA", "#33232A", "#9A3B5C", "20px", pea=F("Instrument Serif"), keha=F("Inter"), pea_kaal="400", pea_ls="-0.01em"),
     "Instrument Serif", "Inter", "veerud", "polaroid", "redel", "hele", 9),
    ("j-uncle-ve", "neoon", "Uncle Ve. Lõikus ja habe.",
     pal("#FFFFFF", "#0E1714", "#0F7B53", "#0E1714", "#6FF0BC", "#0B1210", "#FFFFFF", "#39E39F", "4px", pea=F("Unbounded"), keha=F("Inter"), pea_kaal="900", pea_ls="-0.035em"),
     "Unbounded", "Inter", "read", "riba", "kaardid", "tume", 0),
    ("j-auu-disain", "pool", "Disain sinu juustele.",
     pal("#FFFFFF", "#1A1A1A", "#C2410C", "#1A1A1A", "#FDBA8C", "#1A1A1A", "#FFFFFF", "#FB923C", "0px", pea=F("Syne"), keha=F("Inter"), pea_kaal="800", pea_ls="-0.04em"),
     "Syne", "Inter", "plaadid", "mosaiik", "ajajoon", "tume", 1),
    ("j-bellamark", "ajakiri", "Bellamark.",
     pal("#FBF9F4", "#1F1B16", "#7A5C1E", "#1F1B16", "#E9CF8E", "#1F1B16", "#FFFFFF", "#E3C06B", "2px", pea=F("DM Serif Display"), keha=F("Manrope"), pea_kaal="400", pea_ls="0"),
     "DM Serif Display", "Manrope", "numbrid", "ruudustik", "redel", "tume", 2),
    ("j-a-soleil", "vaht", "Päike ka pilvisel päeval.",
     pal("#FFFCF3", "#2B2210", "#B26B00", "#2B2210", "#FFD27A", "#FFF1CC", "#2B2210", "#B26B00", "999px", pea=F("Fraunces"), keha=F("Manrope"), pea_kaal="700"),
     "Fraunces", "Manrope", "kaardid", "riba", "rida", "hele", 3),
    ("j-kuldne-panter", "salgud", "Kuldne Panter.",
     pal("#FFFFFF", "#17130D", "#8F6A12", "#17130D", "#F1CB6A", "#17130D", "#FFFFFF", "#E8BE4F", "4px", pea=F("Archivo"), keha=F("Inter"), pea_kaal="900", pea_ls="-0.04em"),
     "Archivo", "Inter", "veerud", "polaroid", "kaardid", "tume", 4),
    ("j-ellu", "kaar", "Ellu juuksur.",
     pal("#F9FAFB", "#1F2A37", "#4F6D8A", "#1F2A37", "#B7D0E8", "#E4EBF2", "#1F2A37", "#4F6D8A", "28px", pea=F("Familjen Grotesk"), keha=F("Manrope"), pea_kaal="700", pea_ls="-0.03em"),
     "Familjen Grotesk", "Manrope", "read", "mosaiik", "ajajoon", "hele", 5),
    ("j-noorannika", "kaarid", "Värske soeng Laagris.",
     pal("#FFFFFF", "#1B2A22", "#1F7A4D", "#1B2A22", "#8EE6B5", "#1B2A22", "#FFFFFF", "#6BDDA0", "12px", pea=F("Bricolage Grotesque"), keha=F("Inter"), pea_kaal="800", pea_ls="-0.035em"),
     "Bricolage Grotesque", "Inter", "plaadid", "riba", "redel", "tume", 6),
    ("j-ilusalong-nr-1", "kalender", "Ilusalong Nr\u00a01.",
     pal("#FFFFFF", "#141B2D", "#C0264A", "#141B2D", "#FF9EB3", "#141B2D", "#FFFFFF", "#FF6F8E", "10px", pea=F("Unbounded"), keha=F("Inter"), pea_kaal="900", pea_ls="-0.04em"),
     "Unbounded", "Inter", "kaardid", "ruudustik", "rida", "tume", 7),
    ("j-ilumaja", "terrazzo", "Pärnu Ilumaja.",
     pal("#FFFFFF", "#2D1F26", "#8C3A5E", "#2D1F26", "#F0A7C6", "#F4DCE5", "#2D1F26", "#3F8C7A", "14px", pea=F("Fraunces"), keha=F("Inter"), pea_kaal="900"),
     "Fraunces", "Inter", "numbrid", "polaroid", "kaardid", "hele", 8),
    ("j-juukstop", "foon", "Juukstop. Lõikus ja värv.",
     pal("#F7F7F5", "#161616", "#D1462F", "#161616", "#FF9F8E", "#161616", "#FFFFFF", "#FF6B4F", "6px", pea=F("Space Grotesk"), keha=F("Manrope"), pea_kaal="700", pea_ls="-0.04em"),
     "Space Grotesk", "Manrope", "veerud", "mosaiik", "redel", "tume", 9),
]

for _n, _h, _t, _P, _pea, _keha, _te, _g, _k, _pais, _logo in JUUKSURID:
    lisa(_n, _h, _t, _P, _pea, _keha, _te, _g, _k, _pais, _logo)
