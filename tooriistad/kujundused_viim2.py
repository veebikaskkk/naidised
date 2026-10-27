"""Viimistluse teine komplekt: 10 uut avaploki ideed, igaüks kahes eri paletis ja fondis."""
from sisu import E
from kujundused import nupud, lead
from vahend import pal, baas, pais_css, mix

K = {}


def _sisu(a, d):
    return f'<h1 id="pk">{E(d["h1"])}</h1>{lead(a)}{nupud(a)}'


def _kaks(cls, a, d, joonis, pad="80px 0 88px", lisa=""):
    P = d["p"]
    h = f"""<section class="{cls}" aria-labelledby="pk">
  <div class="wrap {cls}-sisu"><div>{_sisu(a, d)}</div>{joonis}</div>
</section>"""
    c = baas(cls, P, pad, "clamp(34px,5.6vw,80px)") + f""".{cls}-sisu{{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:48px;align-items:center}}
.{cls}-sisu>svg,.{cls}-sisu>.joonis{{width:100%;max-width:400px;justify-self:end}}
@media (max-width:820px){{.{cls}-sisu{{grid-template-columns:minmax(0,1fr)}}.{cls}-sisu>svg,.{cls}-sisu>.joonis{{max-width:220px;justify-self:start;order:-1}}}}{lisa}"""
    return h, c


def hero_tasapind(a, d):
    P = d["p"]
    svg = f"""<svg viewBox="0 0 400 120" aria-hidden="true" focusable="false"><rect x="4" y="30" width="392" height="60" rx="10" fill="{P['ha']}"/>
<rect x="150" y="42" width="100" height="36" rx="18" fill="{mix(P['hf'], P['hb'], .25)}"/><ellipse cx="200" cy="60" rx="20" ry="11" fill="{P['hf']}"/>
<line x1="176" y1="42" x2="176" y2="78" stroke="{P['hb']}" stroke-width="3"/><line x1="224" y1="42" x2="224" y2="78" stroke="{P['hb']}" stroke-width="3"/>
<circle cx="40" cy="60" r="10" fill="{P['hb']}"/><circle cx="360" cy="60" r="10" fill="{P['hb']}"/></svg>"""
    return _kaks("h-tase", a, d, svg)


def hero_rull(a, d):
    P = d["p"]
    h = f"""<section class="h-rull2" aria-labelledby="pk">
  <div class="h-rull2-triip" aria-hidden="true"></div>
  <svg class="h-rull2-svg" viewBox="0 0 220 300" aria-hidden="true" focusable="false"><rect x="10" y="10" width="200" height="70" rx="20" fill="{P['ha']}"/>
  <path d="M110 80v50" stroke="{P['hf']}" stroke-width="10" fill="none"/>
  <rect x="96" y="128" width="28" height="160" rx="12" fill="{P['hf']}"/></svg>
  <div class="wrap h-rull2-sisu">{_sisu(a, d)}</div>
</section>"""
    c = baas("h-rull2", P, "96px 0 104px", "clamp(34px,5.8vw,84px)") + f""".h-rull2-triip{{position:absolute;left:0;right:0;top:0;height:46%;background:linear-gradient(90deg,{P['ha']} 0 62%,transparent 62%);opacity:.18}}
.h-rull2-svg{{position:absolute;right:8%;top:40px;width:min(200px,22vw)}}
.h-rull2-sisu{{position:relative}}.h-rull2 h1{{max-width:11em}}.h-rull2 .lead{{max-width:28em}}
@media (max-width:760px){{.h-rull2-svg{{width:70px;top:24px;right:18px;opacity:.5}}}}"""
    return h, c


def hero_plaadid(a, d):
    P = d["p"]
    t = [P['ha'], P['hf'], mix(P['ha'], P['hb'], .5), mix(P['hf'], P['hb'], .25)]
    ruudud = "".join(f'<span class="r{(i * 7 + i // 4) % 4}"></span>' for i in range(16))
    rcss = "".join(f".h-plaat .r{i}{{background:{x}}}" for i, x in enumerate(t))
    joonis = f'<div class="joonis h-plaat" aria-hidden="true">{ruudud}</div>'
    return _kaks("h-pl2", a, d, joonis, lisa=f"""
.h-plaat{{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;padding:6px;background:{mix(P['hf'], P['hb'], .3)};border-radius:6px}}
.h-plaat span{{aspect-ratio:1;border-radius:2px}}{rcss}""")


def hero_kellu(a, d):
    P = d["p"]
    h = f"""<section class="h-kellu" aria-labelledby="pk">
  <div class="wrap h-kellu-sisu"><div>{_sisu(a, d)}</div>
  <svg viewBox="0 0 300 260" aria-hidden="true" focusable="false"><path d="M20 200L150 120L280 200L150 240Z" fill="{P['ha']}"/>
  <path d="M150 120l0-60" stroke="{P['hf']}" stroke-width="10"/><rect x="128" y="20" width="44" height="60" rx="18" fill="{P['hf']}"/></svg></div>
</section>"""
    tex = mix(P['hf'], P['hb'], .07)
    c = baas("h-kellu", P, "88px 0 96px", "clamp(32px,5.2vw,76px)") + f""".h-kellu{{background-image:radial-gradient(ellipse at 20% 30%,{tex} 0 20%,transparent 40%),radial-gradient(ellipse at 70% 80%,{tex} 0 25%,transparent 45%),radial-gradient(ellipse at 90% 10%,{tex} 0 15%,transparent 35%)}}
.h-kellu-sisu{{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:48px;align-items:center}}
.h-kellu-sisu svg{{width:100%;max-width:360px;justify-self:end}}
@media (max-width:820px){{.h-kellu-sisu{{grid-template-columns:minmax(0,1fr)}}.h-kellu-sisu svg{{max-width:180px;justify-self:start;order:-1}}}}"""
    return h, c


def hero_tilgad(a, d):
    P = d["p"]
    tilk = "".join(f'<span class="t{i}"></span>' for i in range(9))
    pik = [60, 120, 40, 180, 90, 50, 140, 70, 110]
    tcss = "".join(f".h-tilgad .t{i}{{height:{p}px}}" for i, p in enumerate(pik))
    h = f"""<section class="h-tilgad" aria-labelledby="pk">
  <div class="h-tilgad-rida" aria-hidden="true">{tilk}</div>
  <div class="wrap h-tilgad-sisu">{_sisu(a, d)}</div>
</section>"""
    c = baas("h-tilgad", P, "0 0 96px", "clamp(34px,5.8vw,84px)") + f""".h-tilgad-rida{{display:flex;justify-content:space-around;align-items:flex-start;height:200px;border-top:28px solid {P['ha']}}}
.h-tilgad-rida span{{width:clamp(14px,2.4vw,30px);background:{P['ha']};border-radius:0 0 999px 999px}}{tcss}
.h-tilgad-sisu{{padding-top:24px}}.h-tilgad h1{{max-width:11em}}
@media (max-width:600px){{.h-tilgad-rida{{height:120px}}.h-tilgad-rida span:nth-child(n+7){{display:none}}}}"""
    return h, c


def hero_parkett(a, d):
    P = d["p"]
    p1, p2 = mix(P['ha'], P['hb'], .85), mix(P['ha'], P['hb'], .6)
    joonis = '<div class="joonis h-park" aria-hidden="true"></div>'
    return _kaks("h-par", a, d, joonis, lisa=f"""
.h-park{{aspect-ratio:1;border-radius:12px;background:
 linear-gradient(45deg,{p1} 25%,transparent 25%) 0 0/60px 60px,
 linear-gradient(-45deg,{p2} 25%,transparent 25%) 0 0/60px 60px,
 linear-gradient(45deg,transparent 75%,{p2} 75%) 0 0/60px 60px,
 linear-gradient(-45deg,transparent 75%,{p1} 75%) 0 0/60px 60px,{mix(P['ha'], P['hb'], .7)};box-shadow:inset 0 0 0 8px {P['hf']}}}""")


def hero_moodulint(a, d):
    P = d["p"]
    h = f"""<section class="h-lint" aria-labelledby="pk">
  <div class="wrap">{_sisu(a, d)}</div>
  <div class="h-lint-lint" aria-hidden="true"><span>10</span><span>20</span><span>30</span><span>40</span><span>50</span><span>60</span><span>70</span><span>80</span></div>
</section>"""
    c = baas("h-lint", P, "96px 0 0") + f""".h-lint h1{{max-width:11em}}
.h-lint-lint{{margin-top:72px;height:64px;display:flex;background:repeating-linear-gradient(90deg,{P['hf']} 0 2px,transparent 2px 12px) bottom/100% 18px no-repeat,{P['ha']};color:{P['haf']};font-weight:700;font-size:14px}}
.h-lint-lint span{{flex:1;padding:8px 0 0 6px;border-left:2px solid {P['hf']}}}"""
    return h, c


def hero_pahtel(a, d):
    P = d["p"]
    h = f"""<section class="h-paht" aria-labelledby="pk">
  <div class="h-paht-sein" aria-hidden="true"><span></span></div>
  <div class="wrap h-paht-sisu">{_sisu(a, d)}</div>
</section>"""
    kare = mix(P['hf'], P['hb'], .12)
    c = baas("h-paht", P, "104px 0 112px") + f""".h-paht-sein{{position:absolute;top:0;bottom:0;right:0;width:40%;background:radial-gradient(circle,{kare} 0 1.5px,transparent 2px) 0 0/9px 9px,radial-gradient(circle,{kare} 0 1px,transparent 1.5px) 4px 5px/7px 7px}}
.h-paht-sein span{{position:absolute;top:0;bottom:0;left:0;width:55%;background:linear-gradient(90deg,{P['hb']},{mix(P['ha'], P['hb'], .25)})}}
.h-paht-sein::after{{content:"";position:absolute;left:55%;top:30%;width:14px;height:40%;background:{P['ha']};border-radius:4px;transform:translateX(-50%) rotate(8deg)}}
.h-paht-sisu{{position:relative}}.h-paht-sisu>*{{max-width:min(640px,58%)}}
@media (max-width:760px){{.h-paht-sein{{width:100%;height:16px;top:auto}}.h-paht-sein::after{{display:none}}.h-paht-sisu>*{{max-width:none}}}}"""
    return h, c


def hero_nurk(a, d):
    P = d["p"]
    svg = f"""<svg viewBox="0 0 320 300" aria-hidden="true" focusable="false"><path d="M160 20L300 90V250L160 290Z" fill="{mix(P['ha'], P['hb'], .55)}"/>
<path d="M160 20L20 90V250L160 290Z" fill="{P['ha']}"/><path d="M20 250L160 290L300 250L160 215Z" fill="{mix(P['hf'], P['hb'], .3)}"/>
<rect x="60" y="120" width="60" height="70" fill="{P['hb']}" opacity=".5" transform="skewY(17)"/></svg>"""
    return _kaks("h-nurk", a, d, svg)


def hero_purk(a, d):
    P = d["p"]
    svg = f"""<svg viewBox="0 0 300 300" aria-hidden="true" focusable="false"><circle cx="150" cy="150" r="140" fill="{P['hf']}"/>
<circle cx="150" cy="150" r="118" fill="{mix(P['hf'], P['hb'], .75)}"/><circle cx="150" cy="150" r="104" fill="{P['ha']}"/>
<path d="M90 120c30-20 90-20 120 0" stroke="{mix(P['ha'], '#FFFFFF', .7)}" stroke-width="8" fill="none" stroke-linecap="round"/></svg>"""
    return _kaks("h-purk", a, d, svg)


HEROD = dict(tasapind=hero_tasapind, rull=hero_rull, plaadid=hero_plaadid, kellu=hero_kellu, tilgad=hero_tilgad,
             parkett=hero_parkett, moodulint=hero_moodulint, pahtel=hero_pahtel, nurk=hero_nurk, purk=hero_purk)

FONDID = [("Archivo", "Inter", "900", "-0.035em"), ("Fraunces", "Manrope", "900", "-0.02em"), ("Space Grotesk", "Inter", "700", "-0.035em"),
          ("DM Serif Display", "Manrope", "400", "0"), ("Bricolage Grotesque", "Inter", "800", "-0.035em"), ("Epilogue", "Manrope", "800", "-0.03em"),
          ("Familjen Grotesk", "Inter", "700", "-0.03em"), ("Instrument Serif", "Inter", "400", "-0.01em"), ("Syne", "Manrope", "800", "-0.03em"),
          ("Inter Display", "Inter", "800", "-0.03em")]
TEEN = ["read", "kaardid", "veerud", "numbrid", "plaadid"]
GAL = ["mosaiik", "polaroid", "ruudustik", "riba"]
KAIK = ["ajajoon", "kaardid", "rida", "redel"]

# (võti, avaplokk, pealkiri, (bg, fg, aktsent, avaploki taust, avaploki tekst, avaploki aktsent), raadius, päis)
VIIMISTLUS2 = [
    ("v-bengo", "tasapind", "Viimistlus, mis jääb loodi.", ("#FFFFFF", "#14213D", "#1D4ED8", "#EEF2FB", "#14213D", "#F59E0B"), "8px", "hele"),
    ("v-pent", "plaadid", "Plaat ja põrand paika.", ("#FAFAF8", "#1C1C1A", "#0F766E", "#1C1C1A", "#FFFFFF", "#5EEAD4"), "4px", "tume"),
    ("v-remont", "rull", "Remont Tartu kandis.", ("#FFFFFF", "#2A1B12", "#B4531F", "#FDF1E7", "#2A1B12", "#D9692E"), "999px", "hele"),
    ("v-wellington", "kellu", "Pärnu krohvi- ja viimistlustööd.", ("#FBFAF7", "#1F2A24", "#3F6B4F", "#1F2A24", "#FFFFFF", "#C8B27A"), "6px", "varv"),
    ("v-ennu", "tilgad", "Saku kandi viimistlejad.", ("#FFFFFF", "#111827", "#B91C1C", "#FFF7F5", "#111827", "#DC2626"), "10px", "hele"),
    ("v-triebkraft", "parkett", "Tallinna remont ja viimistlus.", ("#FFFFFF", "#1B1917", "#92400E", "#1B1917", "#FFFFFF", "#D6A46A"), "4px", "tume"),
    ("v-orasgrupp", "moodulint", "Plaatimine ja põrandad Tallinnas.", ("#FFFFFF", "#0F172A", "#0369A1", "#F0F7FC", "#0F172A", "#F2C94C"), "6px", "hele"),
    ("v-granjano", "pahtel", "Sile sein Elva kandis.", ("#FCFBF8", "#24211C", "#7C5E2A", "#24211C", "#FFFFFF", "#E5C07B"), "12px", "varv"),
    ("v-gerax", "nurk", "Krohv ja pahtel Tartus.", ("#FFFFFF", "#1E2235", "#4338CA", "#EEEFFB", "#1E2235", "#6366F1"), "8px", "hele"),
    ("v-meliko", "purk", "Jõhvi krohvitööd.", ("#F8FAFC", "#0E1A2B", "#0F5BD8", "#0E1A2B", "#FFFFFF", "#60A5FA"), "16px", "tume"),
    ("v-profid-mehed", "purk", "Profid Mehed Rakveres.", ("#FFFFFF", "#1A1A1A", "#C2410C", "#FFF4EC", "#1A1A1A", "#EA580C"), "999px", "hele"),
    ("v-jes-teenus", "nurk", "Remont Rakveres.", ("#FFFFFF", "#132A20", "#166534", "#132A20", "#FFFFFF", "#86EFAC"), "6px", "tume"),
    ("v-sepa", "pahtel", "Sepa Ehitus Saku vallas.", ("#FFFFFF", "#1C1917", "#A16207", "#FEFCE8", "#1C1917", "#CA8A04"), "4px", "hele"),
    ("v-privamal", "moodulint", "Plaatimine Kambja kandis.", ("#FBFBF9", "#172033", "#1E40AF", "#172033", "#FFFFFF", "#FCD34D"), "8px", "varv"),
    ("v-porandast-laeni", "parkett", "Põrandast laeni, Pärnus.", ("#FFFFFF", "#2B1D14", "#9A3412", "#FBF3EC", "#2B1D14", "#B45309"), "10px", "hele"),
    ("v-joksi", "tilgad", "Remont Põlvamaal.", ("#FFFFFF", "#101828", "#7C3AED", "#101828", "#FFFFFF", "#C4B5FD"), "8px", "tume"),
    ("v-ksa", "kellu", "Värvimine Tartu vallas.", ("#FFFFFF", "#0C2A2A", "#0F766E", "#E6F4F1", "#0C2A2A", "#0F766E"), "14px", "hele"),
    ("v-sideline", "rull", "Viimistlus Võrumaal.", ("#FFFFFF", "#18181B", "#BE123C", "#18181B", "#FFFFFF", "#FB7185"), "6px", "tume"),
    ("v-puidusober", "plaadid", "Põrandad ja viimistlus Kuusalus.", ("#FFFDF7", "#1F2A1F", "#4D7C0F", "#EEF5E4", "#1F2A1F", "#65A30D"), "4px", "hele"),
    ("v-ille", "tasapind", "Ille Siseviimistlus.", ("#FFFFFF", "#2A1E2E", "#86198F", "#2A1E2E", "#FFFFFF", "#F0ABFC"), "16px", "varv"),
]

for i, (nimi, hero, h1, (bg, fg, acc, hb, hf, ha), raadius, pais) in enumerate(VIIMISTLUS2):
    pea, keha, kaal, ls = FONDID[(i * 3) % len(FONDID)]
    P = pal(bg, fg, acc, mix(fg, "#000000", .9), ha, hb, hf, ha, raadius, pea=f"'{pea}'", keha=f"'{keha}'", pea_kaal=kaal, pea_ls=ls)
    K[nimi] = dict(hero=HEROD[hero], h1=h1, p=P, pea=pea, keha=keha, theme=P["hb"], teenused=TEEN[i % 5], galerii=GAL[(i * 3) % 4],
                   kaik=KAIK[(i // 2) % 4], pais=pais, vars=P["vars"], css=pais_css(pais, P, i + 3))
