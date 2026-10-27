"""Torutööd, küte ja ventilatsioon: 15 avaploki ideed (torud, ventiilid, radiaatorid, õhk ja vesi),
igaüks kahes-kolmes eri paletis ja fondis."""
import math

from sisu import E
from kujundused import nupud, lead
from vahend import pal, baas, pais_css, mix

K = {}


def _sisu(a, d):
    return f'<h1 id="pk">{E(d["h1"])}</h1>{lead(a)}{nupud(a)}'


def _kaks(cls, a, d, joonis, pad="80px 0 88px", lisa="", suurus="clamp(34px,5.4vw,78px)"):
    """Tekst vasakul, joonis paremal (telefonis väike joonis teksti kohal)."""
    P = d["p"]
    h = f"""<section class="{cls}" aria-labelledby="pk">
  <div class="wrap {cls}-sisu"><div>{_sisu(a, d)}</div>{joonis}</div>
</section>"""
    c = baas(cls, P, pad, suurus) + f""".{cls}-sisu{{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:48px;align-items:center}}
.{cls}-sisu>svg,.{cls}-sisu>.joonis{{width:100%;max-width:380px;justify-self:end}}
@media (max-width:820px){{.{cls}-sisu{{grid-template-columns:minmax(0,1fr)}}.{cls}-sisu>svg,.{cls}-sisu>.joonis{{max-width:190px;justify-self:start;order:-1}}}}{lisa}"""
    return h, c


def _svg(vb, sisu):
    return f'<svg viewBox="{vb}" aria-hidden="true" focusable="false">{sisu}</svg>'


def hero_toru(a, d):
    """Paks toru põlvede ja muhvidega."""
    P = d["p"]
    t, m = P['ha'], mix(P['hf'], P['hb'], .35)
    s = _svg("0 0 360 320", f"""<path d="M10 70H170Q220 70 220 120V200Q220 250 270 250H350" stroke="{t}" stroke-width="40" fill="none"/>
<rect x="110" y="44" width="22" height="52" rx="4" fill="{m}"/><rect x="194" y="150" width="52" height="22" rx="4" fill="{m}"/>
<rect x="290" y="224" width="22" height="52" rx="4" fill="{m}"/><circle cx="60" cy="70" r="8" fill="{P['hb']}"/>""")
    return _kaks("h-xtoru", a, d, s)


def hero_ventiil(a, d):
    """Sulgeventiili ratas."""
    P = d["p"]
    kodarad = "".join(f'<line x1="150" y1="150" x2="{150 + 92 * math.cos(math.radians(k * 72 - 90)):.1f}" '
                      f'y2="{150 + 92 * math.sin(math.radians(k * 72 - 90)):.1f}" stroke="{P["ha"]}" stroke-width="14" stroke-linecap="round"/>'
                      for k in range(5))
    s = _svg("0 0 300 300", f"""<rect x="0" y="232" width="300" height="44" rx="8" fill="{mix(P['hf'], P['hb'], .3)}"/>
<rect x="132" y="150" width="36" height="90" fill="{mix(P['hf'], P['hb'], .3)}"/>
<circle cx="150" cy="150" r="100" fill="none" stroke="{P['ha']}" stroke-width="20"/>{kodarad}
<circle cx="150" cy="150" r="24" fill="{P['hf']}"/><circle cx="150" cy="150" r="9" fill="{P['hb']}"/>""")
    return _kaks("h-xventiil", a, d, s)


def hero_mano(a, d):
    """Manomeeter: skaala, nool ja punane tsoon."""
    P = d["p"]
    kriipsud = ""
    for k in range(11):
        n = math.radians(135 + k * 27)
        r1 = 96 if k % 5 else 86
        kriipsud += (f'<line x1="{150 + r1 * math.cos(n):.1f}" y1="{150 + r1 * math.sin(n):.1f}" x2="{150 + 108 * math.cos(n):.1f}" '
                     f'y2="{150 + 108 * math.sin(n):.1f}" stroke="{P["hb"]}" stroke-width="{5 if k % 5 == 0 else 3}"/>')
    n = math.radians(135 + 6.3 * 27)
    s = _svg("0 0 300 300", f"""<circle cx="150" cy="150" r="140" fill="{P['ha']}"/><circle cx="150" cy="150" r="122" fill="{P['hf']}"/>
<path d="M{150 + 104 * math.cos(math.radians(351)):.1f} {150 + 104 * math.sin(math.radians(351)):.1f}A104 104 0 0 1 {150 + 104 * math.cos(math.radians(405)):.1f} {150 + 104 * math.sin(math.radians(405)):.1f}" stroke="{P['ha']}" stroke-width="12" fill="none"/>
{kriipsud}<line x1="150" y1="150" x2="{150 + 90 * math.cos(n):.1f}" y2="{150 + 90 * math.sin(n):.1f}" stroke="{P['hb']}" stroke-width="7" stroke-linecap="round"/>
<circle cx="150" cy="150" r="13" fill="{P['hb']}"/>""")
    return _kaks("h-xmano", a, d, s)


def hero_radiaator(a, d):
    """Radiaatori ribid läbi kogu laiuse avaploki allservas."""
    P = d["p"]
    h = f"""<section class="h-xrad" aria-labelledby="pk">
  <div class="wrap">{_sisu(a, d)}</div>
  <div class="h-xrad-ribid" aria-hidden="true"></div>
</section>"""
    c = baas("h-xrad", P, "96px 0 0") + f""".h-xrad h1{{max-width:11em}}.h-xrad .lead{{max-width:30em}}
.h-xrad-ribid{{margin-top:72px;height:120px;border-top:14px solid {mix(P['hf'], P['hb'], .3)};
background:repeating-linear-gradient(90deg,{P['ha']} 0 30px,{P['hb']} 30px 40px)}}
@media (max-width:600px){{.h-xrad-ribid{{height:72px;margin-top:48px;background:repeating-linear-gradient(90deg,{P['ha']} 0 20px,{P['hb']} 20px 28px)}}}}"""
    return h, c


def hero_tilk(a, d):
    """Suur veetilk."""
    P = d["p"]
    s = _svg("0 0 260 320", f"""<path d="M130 10C130 10 30 140 30 210A100 100 0 0 0 230 210C230 140 130 10 130 10Z" fill="{P['ha']}"/>
<path d="M80 200A52 52 0 0 0 112 262" stroke="{mix('#FFFFFF', P['ha'], .7)}" stroke-width="12" fill="none" stroke-linecap="round"/>""")
    return _kaks("h-xtilk", a, d, s)


def hero_fan(a, d):
    """Ventilaator: neli laba rõngas."""
    P = d["p"]
    laba = f'<path d="M150 150C120 110 120 60 150 40C175 70 175 115 150 150Z" fill="{P["ha"]}"/>'
    labad = "".join(f'<g transform="rotate({k * 90} 150 150)">{laba}</g>' for k in range(4))
    s = _svg("0 0 300 300", f"""<circle cx="150" cy="150" r="138" fill="{mix(P['hf'], P['hb'], .14)}"/>
<circle cx="150" cy="150" r="138" fill="none" stroke="{P['hf']}" stroke-width="10"/>{labad}
<circle cx="150" cy="150" r="20" fill="{P['hf']}"/>""")
    return _kaks("h-xfan", a, d, s)


def hero_lained(a, d):
    """Soojuslained, mis tõusevad paremal."""
    P = d["p"]
    lain = "".join(f'<path d="M{40 + k * 70} 300C{10 + k * 70} 250 {70 + k * 70} 200 {40 + k * 70} 150S{70 + k * 70} 50 {40 + k * 70} 10" '
                   f'stroke="{P["ha"] if k != 1 else mix(P["ha"], P["hb"], .55)}" stroke-width="22" fill="none" stroke-linecap="round"/>'
                   for k in range(3))
    h = f"""<section class="h-xlain" aria-labelledby="pk">
  <svg class="h-xlain-svg" viewBox="0 0 220 310" aria-hidden="true" focusable="false">{lain}</svg>
  <div class="wrap h-xlain-sisu">{_sisu(a, d)}</div>
</section>"""
    c = baas("h-xlain", P, "104px 0 112px", "clamp(34px,5.8vw,84px)") + f""".h-xlain-svg{{position:absolute;right:6%;top:50%;transform:translateY(-50%);width:min(240px,22vw)}}
.h-xlain-sisu{{position:relative}}.h-xlain-sisu>*{{max-width:min(680px,66%)}}
@media (max-width:760px){{.h-xlain-svg{{width:64px;top:28px;right:16px;transform:none;opacity:.6}}.h-xlain-sisu>*{{max-width:none}}.h-xlain h1{{padding-right:56px}}}}"""
    return h, c


def hero_vork(a, d):
    """Torustiku skeem: sirged torud ja liitmikud."""
    P = d["p"]
    t, s2 = P['ha'], mix(P['hf'], P['hb'], .45)
    s = _svg("0 0 320 300", f"""<path d="M20 60H300M20 150H220M100 60V280M220 150V280M300 60V200" stroke="{s2}" stroke-width="14" fill="none"/>
<path d="M20 240H300" stroke="{t}" stroke-width="14"/><path d="M160 60V240" stroke="{t}" stroke-width="14"/>
<g fill="{P['hf']}"><circle cx="100" cy="60" r="14"/><circle cx="160" cy="60" r="14"/><circle cx="220" cy="150" r="14"/>
<circle cx="160" cy="240" r="14"/><circle cx="100" cy="150" r="14"/><circle cx="300" cy="60" r="14"/></g>
<rect x="232" y="226" width="40" height="28" rx="6" fill="{t}"/>""")
    return _kaks("h-xvork", a, d, s)


def hero_pump(a, d):
    """Soojuspumba välisseade."""
    P = d["p"]
    rõngad = "".join(f'<circle cx="120" cy="120" r="{r}" fill="none" stroke="{mix(P["hf"], P["hb"], .35)}" stroke-width="5"/>'
                     for r in (78, 62, 46, 30))
    s = _svg("0 0 340 270", f"""<rect x="10" y="20" width="320" height="200" rx="18" fill="{P['hf']}"/>
<circle cx="120" cy="120" r="88" fill="{mix(P['hf'], P['hb'], .85)}"/>{rõngad}
<path d="M120 120L120 50M120 120L180 150M120 120L60 150" stroke="{P['ha']}" stroke-width="10" stroke-linecap="round"/>
<g fill="{mix(P['hf'], P['hb'], .55)}"><rect x="240" y="60" width="64" height="10" rx="5"/><rect x="240" y="84" width="64" height="10" rx="5"/><rect x="240" y="108" width="64" height="10" rx="5"/></g>
<circle cx="272" cy="176" r="12" fill="{P['ha']}"/><rect x="40" y="220" width="30" height="40" fill="{P['hf']}"/><rect x="270" y="220" width="30" height="40" fill="{P['hf']}"/>""")
    return _kaks("h-xpump", a, d, s)


def hero_kraan(a, d):
    """Kraan ja tilgad."""
    P = d["p"]
    s = _svg("0 0 300 320", f"""<rect x="20" y="40" width="44" height="120" rx="10" fill="{mix(P['hf'], P['hb'], .35)}"/>
<path d="M60 90H200Q240 90 240 130V160" stroke="{P['hf']}" stroke-width="40" fill="none"/>
<rect x="110" y="30" width="60" height="22" rx="11" fill="{P['ha']}"/><rect x="132" y="48" width="16" height="26" fill="{P['ha']}"/>
<path d="M240 200C240 200 222 226 222 240A18 18 0 0 0 258 240C258 226 240 200 240 200Z" fill="{P['ha']}"/>
<path d="M240 270C240 270 230 284 230 292A10 10 0 0 0 250 292C250 284 240 270 240 270Z" fill="{P['ha']}" opacity=".7"/>""")
    return _kaks("h-xkraan", a, d, s)


def hero_pk(a, d):
    """Põrandakütte toru looklemas ruudu sees."""
    P = d["p"]
    tee = "M40 40H260" + "".join(f"V{60 + k * 40}H{40 if k % 2 == 0 else 260}" for k in range(6)) + "V280"
    s = _svg("0 0 300 300", f"""<rect x="10" y="10" width="280" height="280" rx="14" fill="{mix(P['hf'], P['hb'], .1)}"/>
<path d="{tee}" stroke="{P['ha']}" stroke-width="12" fill="none" stroke-linejoin="round"/>
<circle cx="40" cy="40" r="12" fill="{P['hf']}"/><circle cx="40" cy="280" r="12" fill="{P['hf']}"/>""")
    return _kaks("h-xpk", a, d, s)


def hero_koll(a, d):
    """Kollektor: rida ventiile soe ja külm."""
    P = d["p"]
    kylm = mix(P['hf'], P['hb'], .45)
    vent = "".join(f'<rect x="{38 + k * 56}" y="120" width="20" height="110" fill="{mix(P["hf"], P["hb"], .3)}"/>'
                   f'<rect x="{28 + k * 56}" y="96" width="40" height="30" rx="8" fill="{P["ha"] if k % 2 == 0 else kylm}"/>'
                   for k in range(5))
    s = _svg("0 0 320 260", f"""<rect x="10" y="40" width="300" height="40" rx="20" fill="{P['ha']}"/>
<rect x="10" y="226" width="300" height="24" rx="12" fill="{kylm}"/>{vent}""")
    return _kaks("h-xkoll", a, d, s)


def hero_ring(a, d):
    """Ringlus: soe ja jahtunud vesi kahe noolena."""
    P = d["p"]
    kylm = mix(P['hf'], P['hb'], .5)
    s = _svg("0 0 300 300", f"""<path d="M60 150A90 90 0 0 1 228 105" stroke="{P['ha']}" stroke-width="28" fill="none"/>
<path d="M200 70L262 92L228 150Z" fill="{P['ha']}"/>
<path d="M240 150A90 90 0 0 1 72 195" stroke="{kylm}" stroke-width="28" fill="none"/>
<path d="M100 230L38 208L72 150Z" fill="{kylm}"/>""")
    return _kaks("h-xring", a, d, s)


def hero_kanal(a, d):
    """Ventilatsioonikanal restiga üle kogu laiuse."""
    P = d["p"]
    h = f"""<section class="h-xkanal" aria-labelledby="pk">
  <div class="h-xkanal-kanal" aria-hidden="true"><span></span></div>
  <div class="wrap h-xkanal-sisu">{_sisu(a, d)}</div>
</section>"""
    c = baas("h-xkanal", P, "0 0 104px", "clamp(34px,5.8vw,84px)") + f""".h-xkanal-kanal{{height:110px;background:{mix(P['hf'], P['hb'], .22)};position:relative;margin-bottom:64px}}
.h-xkanal-kanal span{{position:absolute;right:10%;top:15px;bottom:15px;width:min(320px,40%);border-radius:6px;
background:repeating-linear-gradient(0deg,{P['ha']} 0 8px,{mix(P['hf'], P['hb'], .22)} 8px 16px);box-shadow:0 0 0 8px {P['ha']}}}
.h-xkanal h1{{max-width:11em}}
@media (max-width:600px){{.h-xkanal-kanal{{height:64px;margin-bottom:40px}}.h-xkanal-kanal span{{top:10px;bottom:10px;width:50%}}}}"""
    return h, c


def hero_mullid(a, d):
    """Veemullid tõusevad paremas servas."""
    P = d["p"]
    mullid = [(72, 150, 84), (26, 40, 170), (48, 170, 240), (18, 60, 290), (60, 90, 370), (22, 200, 430)]
    m = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{P["ha"]}" stroke-width="{max(4, r // 8)}"/>' for r, x, y in mullid)
    h = f"""<section class="h-xmull" aria-labelledby="pk">
  <svg class="h-xmull-svg" viewBox="0 0 240 460" aria-hidden="true" focusable="false">{m}</svg>
  <div class="wrap h-xmull-sisu">{_sisu(a, d)}</div>
</section>"""
    c = baas("h-xmull", P, "104px 0 112px", "clamp(34px,5.8vw,84px)") + f""".h-xmull-svg{{position:absolute;right:5%;top:0;height:100%;width:auto;max-width:26vw}}
.h-xmull-sisu{{position:relative}}.h-xmull-sisu>*{{max-width:min(680px,66%)}}
@media (max-width:760px){{.h-xmull-svg{{height:150px;top:16px;right:8px;opacity:.5}}.h-xmull-sisu>*{{max-width:none}}.h-xmull h1{{padding-right:48px}}}}"""
    return h, c


def hero_katel(a, d):
    """Seinakatel torude ja näidikuga."""
    P = d["p"]
    m = mix(P['hf'], P['hb'], .35)
    s = _svg("0 0 280 320", f"""<rect x="50" y="10" width="180" height="230" rx="22" fill="{P['hf']}"/>
<rect x="80" y="44" width="120" height="56" rx="10" fill="{mix(P['hf'], P['hb'], .8)}"/>
<text x="140" y="84" text-anchor="middle" font-size="30" font-weight="700" fill="{P['ha']}" font-family="Inter,sans-serif">60°</text>
<circle cx="105" cy="150" r="16" fill="{P['ha']}"/><circle cx="175" cy="150" r="16" fill="{m}"/>
<rect x="80" y="196" width="120" height="10" rx="5" fill="{m}"/>
<path d="M90 240V310M140 240V310M190 240V310" stroke="{m}" stroke-width="14"/><path d="M90 240V310" stroke="{P['ha']}" stroke-width="14"/>""")
    return _kaks("h-xkatel", a, d, s)


def hero_dush(a, d):
    """Dušipea ja veejoad."""
    P = d["p"]
    joad = "".join(f'<line x1="{150 + dx}" y1="150" x2="{150 + dx * 1.8:.0f}" y2="290" stroke="{P["ha"]}" stroke-width="6" stroke-linecap="round" stroke-dasharray="14 12"/>'
                   for dx in (-48, -24, 0, 24, 48))
    s = _svg("0 0 300 300", f"""<path d="M40 20H150V60" stroke="{P['hf']}" stroke-width="16" fill="none" stroke-linejoin="round"/>
<path d="M80 130Q150 40 220 130Z" fill="{P['hf']}"/><rect x="76" y="128" width="148" height="14" rx="7" fill="{mix(P['hf'], P['hb'], .5)}"/>{joad}""")
    return _kaks("h-xdush", a, d, s)


def hero_termo(a, d):
    """Termomeeter suurena paremal, skaala kriipsudega."""
    P = d["p"]
    kriips = "".join(f'<rect x="150" y="{40 + k * 24}" width="{34 if k % 2 == 0 else 20}" height="6" rx="3" fill="{mix(P["hf"], P["hb"], .5)}"/>' for k in range(9))
    s = _svg("0 0 240 320", f"""<rect x="70" y="20" width="60" height="230" rx="30" fill="{mix(P['hf'], P['hb'], .15)}" stroke="{P['hf']}" stroke-width="8"/>
<circle cx="100" cy="262" r="46" fill="{P['ha']}" stroke="{P['hf']}" stroke-width="8"/><rect x="88" y="110" width="24" height="150" rx="12" fill="{P['ha']}"/>{kriips}""")
    return _kaks("h-xtermo", a, d, s)


def hero_ahi(a, d):
    """Kahhelahi koldeuksega ja leegiga."""
    P = d["p"]
    m = mix(P['hf'], P['hb'], .2)
    kahhel = "".join(f'<rect x="{40 + c * 56}" y="{30 + r * 46}" width="52" height="42" rx="4" fill="{m}"/>' for r in range(5) for c in range(4))
    s = _svg("0 0 300 300", f"""<rect x="34" y="24" width="232" height="246" rx="8" fill="{P['hf']}"/>{kahhel}
<rect x="104" y="170" width="92" height="80" rx="6" fill="{P['hb']}"/>
<path d="M150 180C130 205 128 225 150 244C172 225 170 205 150 180Z" fill="{P['ha']}"/>
<rect x="20" y="268" width="260" height="16" rx="4" fill="{P['hf']}"/>""")
    return _kaks("h-xahi", a, d, s)


def hero_helves(a, d):
    """Jahutus: lumehelves ja soojuslaine kõrvuti."""
    P = d["p"]
    haru = f'<g stroke="{P["ha"]}" stroke-width="12" stroke-linecap="round"><line x1="120" y1="150" x2="120" y2="50"/><line x1="120" y1="80" x2="98" y2="60"/><line x1="120" y1="80" x2="142" y2="60"/></g>'
    harud = "".join(f'<g transform="rotate({k * 60} 120 150)">{haru}</g>' for k in range(6))
    s = _svg("0 0 320 300", f"""<circle cx="120" cy="150" r="128" fill="{mix(P['hf'], P['hb'], .1)}"/>{harud}<circle cx="120" cy="150" r="14" fill="{P['hf']}"/>
<path d="M280 280C260 240 300 200 280 160S300 80 280 40" stroke="{mix(P['hf'], P['hb'], .55)}" stroke-width="14" fill="none" stroke-linecap="round"/>""")
    return _kaks("h-xhelves", a, d, s)


HEROD = dict(toru=hero_toru, ventiil=hero_ventiil, mano=hero_mano, radiaator=hero_radiaator, tilk=hero_tilk, fan=hero_fan,
             lained=hero_lained, vork=hero_vork, pump=hero_pump, kraan=hero_kraan, pk=hero_pk, koll=hero_koll, ring=hero_ring,
             kanal=hero_kanal, mullid=hero_mullid, katel=hero_katel, dush=hero_dush, termo=hero_termo,
             ahi=hero_ahi, helves=hero_helves)

FONDID = [("Archivo", "Inter", "900", "-0.035em"), ("Space Grotesk", "Inter", "700", "-0.035em"), ("Fraunces", "Manrope", "900", "-0.02em"),
          ("Bricolage Grotesque", "Inter", "800", "-0.035em"), ("Epilogue", "Manrope", "800", "-0.03em"), ("Familjen Grotesk", "Inter", "700", "-0.03em"),
          ("Archivo", "Manrope", "800", "-0.03em"), ("Space Grotesk", "Manrope", "700", "-0.03em"), ("DM Serif Display", "Manrope", "400", "0"),
          ("Inter Display", "Inter", "800", "-0.03em"), ("Instrument Serif", "Inter", "400", "-0.01em")]
TEEN = ["kaardid", "read", "veerud", "numbrid", "plaadid"]
GAL = ["riba", "ruudustik", "polaroid", "mosaiik"]
KAIK = ["redel", "rida", "kaardid", "ajajoon"]

# (võti, avaplokk, pealkiri, (bg, fg, aktsent, avaploki taust, avaploki tekst, avaploki aktsent), raadius, päis)
TORUFIRMAD = [
    ("t-allik-trans", "toru", "Küte ja ventilatsioon Pärnus.", ("#FFFFFF", "#0F1E2E", "#0B66A8", "#EAF3FA", "#0F1E2E", "#E25B26"), "8px", "hele"),
    ("t-abc-kute", "fan", "Küte, jahutus ja ventilatsioon Tartus.", ("#F8FAFC", "#0B1726", "#0E7490", "#0B1726", "#FFFFFF", "#38BDF8"), "12px", "tume"),
    ("t-abix", "mano", "Keila kütte- ja ventilatsioonitööd.", ("#FFFFFF", "#1A1A1A", "#B42318", "#FFF4EF", "#1A1A1A", "#D92D20"), "6px", "hele"),
    ("t-fop-rem", "radiaator", "Küttetööd Ida-Virumaal.", ("#FFFFFF", "#151A22", "#B54708", "#151A22", "#FFFFFF", "#F79009"), "4px", "tume"),
    ("t-berku", "vork", "Torutööd ja küte Hiiumaal.", ("#FBFBF8", "#13261F", "#13795B", "#E8F3EE", "#13261F", "#13795B"), "10px", "hele"),
    ("t-lviworks", "koll", "Vesi, küte ja ventilatsioon Tallinnas.", ("#FFFFFF", "#101828", "#1D4ED8", "#101828", "#FFFFFF", "#F97066"), "8px", "varv"),
    ("t-art-building", "kraan", "Torutööd Tartus.", ("#FFFFFF", "#0C2233", "#0369A1", "#E6F2FA", "#0C2233", "#0369A1"), "999px", "hele"),
    ("t-maxwelding", "ventiil", "Narva küttetööd.", ("#FFFFFF", "#1B1B1F", "#C2410C", "#1B1B1F", "#FFFFFF", "#FB923C"), "6px", "tume"),
    ("t-sergo", "tilk", "Torutööd Pärnus.", ("#F7FBFF", "#0A2540", "#0B5CAD", "#0A2540", "#FFFFFF", "#7CC4FA"), "14px", "varv"),
    ("t-kp-invest", "ring", "Küttesüsteemid Tallinnas.", ("#FFFFFF", "#1C1917", "#B91C1C", "#FBF1EE", "#1C1917", "#DC2626"), "8px", "hele"),
    ("t-kp-kliima", "pump", "Soojuspumbad Tartumaal.", ("#FFFFFF", "#0F1F1A", "#047857", "#0F1F1A", "#FFFFFF", "#6EE7B7"), "12px", "tume"),
    ("t-entivent", "kanal", "Ventilatsioon Harjumaal.", ("#FFFFFF", "#111827", "#4F46E5", "#EEF0FB", "#111827", "#4F46E5"), "6px", "hele"),
    ("t-veritang", "lained", "Soe kodu Tallinnas.", ("#FFFCF8", "#2A1608", "#B4400F", "#2A1608", "#FFFFFF", "#FDBA74"), "4px", "tume"),
    ("t-teemantpoiss", "pk", "Teemantpoiss. Küte ja ventilatsioon.", ("#FFFFFF", "#18181B", "#7C3AED", "#F4F0FF", "#18181B", "#7C3AED"), "16px", "hele"),
    ("t-estoman", "mullid", "Vesi ja kanalisatsioon Tallinnas.", ("#FFFFFF", "#082F49", "#0369A1", "#082F49", "#FFFFFF", "#7DD3FC"), "10px", "varv"),
    ("t-aas", "kraan", "Sanitaartehnika Pärnus.", ("#FFFFFF", "#0F172A", "#0F766E", "#0F172A", "#FFFFFF", "#5EEAD4"), "8px", "tume"),
    ("t-vexon", "toru", "Torutööd ja küte Tallinnas.", ("#FFFFFF", "#1F1F1F", "#A15C07", "#FFF8EB", "#1F1F1F", "#B45309"), "2px", "hele"),
    ("t-weldcom", "ventiil", "Küttetorustikud Tallinnas.", ("#F8FAFC", "#0F172A", "#2563EB", "#E2E8F0", "#0F172A", "#2563EB"), "4px", "hele"),
    ("t-deandra", "tilk", "Torutööd pealinnas.", ("#FFFFFF", "#111827", "#0E7490", "#ECFEFF", "#111827", "#0E7490"), "999px", "hele"),
    ("t-girlande", "mano", "Küte Harjumaal.", ("#FAFAF9", "#1C1917", "#A16207", "#1C1917", "#FFFFFF", "#FACC15"), "10px", "tume"),
    ("t-viktorija", "mullid", "Vesi ja kanalisatsioon Tartus.", ("#FFFFFF", "#1E1B4B", "#4338CA", "#EEF2FF", "#1E1B4B", "#4F46E5"), "14px", "hele"),
    ("t-jurgus", "vork", "Jurgus. Torutööd Tartus.", ("#FFFFFF", "#101010", "#C2410C", "#101010", "#FFFFFF", "#FDBA74"), "4px", "tume"),
    ("t-ilstro", "koll", "Torutööd ja küte Kohtla-Järvel.", ("#FFFFFF", "#0B2533", "#0E7490", "#E6F6F9", "#0B2533", "#C2410C"), "8px", "hele"),
    ("t-avass", "ring", "Küttetööd Jõhvi kandis.", ("#F9FAFB", "#111827", "#B91C1C", "#111827", "#FFFFFF", "#F87171"), "12px", "varv"),
    ("t-maritek", "radiaator", "Torud ja küte Tartus.", ("#FFFFFF", "#1B2430", "#475467", "#F2F4F7", "#1B2430", "#D92D20"), "6px", "hele"),
    ("t-kvv", "toru", "Vesi, kanalisatsioon ja küte.", ("#FFFFFF", "#0D1B2A", "#1565C0", "#0D1B2A", "#FFFFFF", "#64B5F6"), "8px", "tume"),
    ("t-vvs", "fan", "Ventilatsioon Tallinnas.", ("#FFFFFF", "#14213D", "#0F766E", "#E7F5F2", "#14213D", "#0F766E"), "10px", "hele"),
    ("t-kaltel", "pk", "Jõgeva torutööd ja küte.", ("#FFFDF9", "#231A12", "#B45309", "#231A12", "#FFFFFF", "#F59E0B"), "6px", "varv"),
    ("t-acai", "lained", "Ahjud ja kaminad Viljandis.", ("#FFFBF6", "#2B1A10", "#9A3412", "#FBEDE2", "#2B1A10", "#C2410C"), "4px", "hele"),
    ("t-torukunn", "kraan", "ToruKunn. Torutööd Tallinnas.", ("#FFFFFF", "#0A1F33", "#0B66A8", "#0A1F33", "#FFFFFF", "#FACC15"), "999px", "tume"),
    ("t-milann", "tilk", "Santehnika Narvas.", ("#FFFFFF", "#0C1A2B", "#1E40AF", "#EAF0FF", "#0C1A2B", "#1E40AF"), "12px", "hele"),
    ("t-kuul", "mullid", "Korras torud Tallinnas.", ("#FFFFFF", "#0F172A", "#0284C7", "#0F172A", "#FFFFFF", "#38BDF8"), "8px", "tume"),
    ("t-parnu-torutood", "ventiil", "Torud ja küte Pärnumaal.", ("#FFFFFF", "#132A20", "#166534", "#132A20", "#FFFFFF", "#86EFAC"), "6px", "varv"),
    ("t-elrem", "vork", "Torutööd Lääne-Virumaal.", ("#FFFFFF", "#1A1A2E", "#3730A3", "#EFF0FA", "#1A1A2E", "#E25B26"), "10px", "hele"),
    ("t-inverter-heat", "pump", "Soojuspumbad Järvamaal.", ("#FFFFFF", "#1C1917", "#C2410C", "#FFF4EC", "#1C1917", "#EA580C"), "14px", "hele"),
    ("t-raksek", "kanal", "Küte ja ventilatsioon Saaremaal.", ("#FFFFFF", "#0B1F2A", "#0E7490", "#0B1F2A", "#FFFFFF", "#67E8F9"), "4px", "tume"),
]

for i, (nimi, hero, h1, (bg, fg, acc, hb, hf, ha), raadius, pais) in enumerate(TORUFIRMAD):
    pea, keha, kaal, ls = FONDID[(i * 4) % len(FONDID)]
    P = pal(bg, fg, acc, mix(fg, "#000000", .9), ha, hb, hf, ha, raadius, pea=f"'{pea}'", keha=f"'{keha}'", pea_kaal=kaal, pea_ls=ls)
    K[nimi] = dict(hero=HEROD[hero], h1=h1, p=P, pea=pea, keha=keha, theme=P["hb"], teenused=TEEN[i % 5], galerii=GAL[(i * 3) % 4],
                   kaik=KAIK[(i // 2) % 4], pais=pais, vars=P["vars"], css=pais_css(pais, P, i + 5))
