"""Elektrikute kujundused. 20 avaploki ideed elektri maailmast, igaüks kahes eri paletis ja fondis."""
from sisu import E
from kujundused import nupud, lead
from vahend import pal, baas, pais_css, mix

K = {}


def _sisu(a, d):
    return f'<h1 id="pk">{E(d["h1"])}</h1>{lead(a)}{nupud(a)}'


def _kaks(cls, a, d, svg, pad="80px 0 88px", lisa=""):
    """Kaheveeruline avaplokk: tekst vasakul, joonis paremal (telefonis üleval)."""
    P = d["p"]
    h = f"""<section class="{cls}" aria-labelledby="pk">
  <div class="wrap {cls}-sisu"><div>{_sisu(a, d)}</div>{svg}</div>
</section>"""
    c = baas(cls, P, pad) + f""".{cls}-sisu{{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:48px;align-items:center}}
.{cls}-sisu>svg,.{cls}-sisu>.joonis{{width:100%;max-width:400px;justify-self:end}}
@media (max-width:820px){{.{cls}-sisu{{grid-template-columns:minmax(0,1fr)}}.{cls}-sisu>svg,.{cls}-sisu>.joonis{{max-width:200px;justify-self:start;order:-1}}}}{lisa}"""
    return h, c


def hero_pistik(a, d):
    P = d["p"]
    svg = f"""<svg viewBox="0 0 300 300" aria-hidden="true" focusable="false"><rect x="10" y="10" width="280" height="280" rx="48" fill="{mix(P['hf'], P['hb'], .12)}"/>
<circle cx="150" cy="150" r="104" fill="{P['hf']}"/><circle cx="150" cy="150" r="84" fill="{mix(P['hf'], P['hb'], .85)}"/>
<circle cx="112" cy="150" r="14" fill="{P['hb']}"/><circle cx="188" cy="150" r="14" fill="{P['hb']}"/>
<rect x="138" y="58" width="24" height="16" rx="4" fill="{P['ha']}"/><rect x="138" y="226" width="24" height="16" rx="4" fill="{P['ha']}"/></svg>"""
    return _kaks("h-pist", a, d, svg)


def hero_valk(a, d):
    P = d["p"]
    h = f"""<section class="h-valk" aria-labelledby="pk">
  <div class="h-valk-kuju" aria-hidden="true"></div>
  <div class="wrap h-valk-sisu">{_sisu(a, d)}</div>
</section>"""
    c = baas("h-valk", P, "104px 0 112px") + f""".h-valk-kuju{{position:absolute;right:4%;top:-10%;width:min(420px,46vw);height:120%;background:{P['ha']};clip-path:polygon(58% 0,18% 54%,46% 54%,30% 100%,84% 38%,54% 38%,74% 0)}}
.h-valk-sisu{{position:relative}}.h-valk h1{{max-width:10em}}.h-valk .lead{{max-width:26em}}
@media (max-width:760px){{.h-valk-kuju{{opacity:.22;width:70vw}}}}"""
    return h, c


def hero_skeem(a, d):
    P = d["p"]
    s = P["ha"]
    svg = f"""<svg class="h-skeem-svg" viewBox="0 0 1200 500" preserveAspectRatio="xMaxYMid slice" aria-hidden="true" focusable="false" fill="none" stroke="{s}" stroke-width="3">
<path d="M640 60H820V160H980V60H1180M700 440V300H860V220H1040V340H1180M760 160V250H900M1040 60V160"/>
<g fill="{s}"><circle cx="820" cy="160" r="8"/><circle cx="980" cy="60" r="8"/><circle cx="860" cy="300" r="8"/><circle cx="1040" cy="220" r="8"/><circle cx="900" cy="250" r="8"/><circle cx="700" cy="300" r="8"/></g>
<path d="M900 120h40l10-16 20 32 20-32 20 32 10-16h40" stroke-width="4"/><rect x="1080" y="300" width="40" height="80" stroke-width="4"/></svg>"""
    h = f"""<section class="h-skeem" aria-labelledby="pk">{svg}
  <div class="wrap h-skeem-sisu">{_sisu(a, d)}</div>
</section>"""
    c = baas("h-skeem", P, "104px 0 112px") + """.h-skeem-svg{position:absolute;inset:0;width:100%;height:100%;opacity:.7}
.h-skeem-sisu{position:relative}.h-skeem h1{max-width:10em}.h-skeem .lead{max-width:26em}
@media (max-width:860px){.h-skeem-svg{opacity:.18}}"""
    return h, c


def hero_kilp(a, d):
    P = d["p"]
    lyl = "".join(f'<span class="{"sees" if i not in (3, 9) else ""}"></span>' for i in range(12))
    svg = f'<div class="joonis h-kilp-kast" aria-hidden="true"><div class="h-kilp-rida">{lyl}</div></div>'
    return _kaks("h-kilp", a, d, svg, lisa=f"""
.h-kilp-kast{{background:{mix(P['hf'], P['hb'], .14)};border:3px solid {P['hf']};border-radius:14px;padding:22px}}
.h-kilp-rida{{display:grid;grid-template-columns:repeat(6,1fr);gap:8px 6px}}
.h-kilp-rida span{{height:72px;border-radius:4px;background:{P['hf']};position:relative}}
.h-kilp-rida span::after{{content:"";position:absolute;left:25%;right:25%;top:44%;height:26%;border-radius:2px;background:{P['hb']}}}
.h-kilp-rida span.sees::after{{top:22%;background:{P['ha']}}}""")


def hero_lamp(a, d):
    P = d["p"]
    svg = f"""<svg viewBox="0 0 300 380" aria-hidden="true" focusable="false"><defs><radialGradient id="kuma"><stop offset="0" stop-color="{P['ha']}" stop-opacity=".55"/><stop offset="1" stop-color="{P['ha']}" stop-opacity="0"/></radialGradient></defs>
<line x1="150" y1="0" x2="150" y2="150" stroke="{P['hf']}" stroke-width="4"/><circle cx="150" cy="270" r="110" fill="url(#kuma)"/>
<rect x="132" y="140" width="36" height="34" rx="4" fill="{P['hf']}"/><path d="M150 172c-46 0-64 38-58 74 6 30 32 42 34 64h48c2-22 28-34 34-64 6-36-12-74-58-74z" fill="{P['ha']}"/>
<path d="M136 254l14 18 14-18" fill="none" stroke="{P['hb']}" stroke-width="4"/></svg>"""
    return _kaks("h-lamp", a, d, svg, pad="64px 0 80px")


def hero_kaablid(a, d):
    P = d["p"]
    h = f"""<section class="h-kaab" aria-labelledby="pk">
  <svg class="h-kaab-svg" viewBox="0 0 1200 480" preserveAspectRatio="none" aria-hidden="true" focusable="false" fill="none" stroke-linecap="round">
    <path d="M-20 380C300 380 520 120 1220 160" stroke="#7A4A26" stroke-width="22"/>
    <path d="M-20 420C340 420 560 180 1220 220" stroke="#2F6FD6" stroke-width="22"/>
    <path d="M-20 460C380 460 600 240 1220 280" stroke="#3D9A3D" stroke-width="22"/><path d="M-20 460C380 460 600 240 1220 280" stroke="#F2D21B" stroke-width="22" stroke-dasharray="40 40"/>
  </svg>
  <div class="wrap h-kaab-sisu">{_sisu(a, d)}</div>
</section>"""
    c = baas("h-kaab", P, "88px 0 200px") + """.h-kaab-svg{position:absolute;left:0;right:0;bottom:0;width:100%;height:58%}
.h-kaab-sisu{position:relative}.h-kaab h1{max-width:12em}"""
    return h, c


def hero_siinus(a, d):
    P = d["p"]
    tee = "M0 60 " + " ".join(f"Q {75 + i * 150} {0 if i % 2 == 0 else 120}, {150 + i * 150} 60" for i in range(10))
    h = f"""<section class="h-siin" aria-labelledby="pk">
  <div class="wrap">{_sisu(a, d)}</div>
  <svg class="h-siin-svg" viewBox="0 0 1500 120" preserveAspectRatio="none" aria-hidden="true" focusable="false"><line x1="0" y1="60" x2="1500" y2="60" stroke="{mix(P['hf'], P['hb'], .3)}" stroke-width="2"/><path d="{tee}" fill="none" stroke="{P['ha']}" stroke-width="6"/></svg>
</section>"""
    c = baas("h-siin", P, "96px 0 0") + """.h-siin h1{max-width:12em}.h-siin-svg{display:block;width:100%;height:120px;margin-top:64px}"""
    return h, c


def hero_lyliti(a, d):
    P = d["p"]
    svg = f"""<svg viewBox="0 0 260 320" aria-hidden="true" focusable="false"><rect x="10" y="10" width="240" height="300" rx="28" fill="{P['hf']}"/>
<rect x="50" y="50" width="160" height="220" rx="16" fill="{mix(P['hf'], P['hb'], .82)}"/><path d="M50 160V66a16 16 0 0 1 16-16h128a16 16 0 0 1 16 16v94z" fill="{P['ha']}"/>
<rect x="110" y="96" width="40" height="8" rx="4" fill="{P['haf']}"/></svg>"""
    return _kaks("h-lyl", a, d, svg)


def hero_hoiatus(a, d):
    P = d["p"]
    h = f"""<section class="h-hoia" aria-labelledby="pk">
  <div class="h-hoia-riba" aria-hidden="true"></div>
  <div class="wrap h-hoia-sisu"><div>{_sisu(a, d)}</div>
  <svg viewBox="0 0 300 270" aria-hidden="true" focusable="false"><path d="M150 12L290 256H10Z" fill="{P['ha']}" stroke="{P['hf']}" stroke-width="12" stroke-linejoin="round"/><path d="M162 92l-40 78h32l-18 62 52-90h-34l20-50z" fill="{P['hf']}"/></svg></div>
  <div class="h-hoia-riba" aria-hidden="true"></div>
</section>"""
    c = baas("h-hoia", P, "0") + f""".h-hoia-riba{{height:28px;background:repeating-linear-gradient(-45deg,{P['ha']} 0 24px,{P['hf']} 24px 48px)}}
.h-hoia-sisu{{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:48px;align-items:center;padding-top:72px;padding-bottom:80px}}
.h-hoia-sisu svg{{width:100%;max-width:340px;justify-self:end}}
@media (max-width:820px){{.h-hoia-sisu{{grid-template-columns:minmax(0,1fr)}}.h-hoia-sisu svg{{max-width:160px;justify-self:start;order:-1}}}}"""
    return h, c


def hero_plaan(a, d):
    P = d["p"]
    jn = mix(P["hf"], P["hb"], .14)
    svg = f"""<svg viewBox="0 0 340 300" aria-hidden="true" focusable="false" fill="none" stroke="{P['hf']}" stroke-width="5">
<path d="M10 10H330V290H10ZM10 150H150M210 150H330M150 150V290M150 10V100"/><path d="M150 100a50 50 0 0 1 50 50" stroke-width="2" stroke-dasharray="6 6"/>
<g stroke="{P['ha']}" stroke-width="4"><circle cx="80" cy="80" r="16"/><path d="M69 69l22 22M91 69l-22 22"/><circle cx="260" cy="80" r="16"/><path d="M249 69l22 22M271 69l-22 22"/><circle cx="240" cy="220" r="16"/><path d="M229 209l22 22M251 209l-22 22"/></g>
<g fill="{P['ha']}" stroke="none"><rect x="10" y="210" width="14" height="20"/><rect x="316" y="180" width="14" height="20"/><rect x="100" y="276" width="20" height="14"/></g></svg>"""
    h, c = _kaks("h-plaan", a, d, svg)
    c += f"\n.h-plaan{{background-image:linear-gradient({jn} 1px,transparent 1px),linear-gradient(90deg,{jn} 1px,transparent 1px);background-size:32px 32px}}"
    return h, c


def hero_mootur(a, d):
    P = d["p"]
    svg = f"""<div class="joonis h-moot-seade" aria-hidden="true"><div class="h-moot-ekraan"><b>230</b><span>V AC</span></div>
<div class="h-moot-ketas"><span></span></div><div class="h-moot-pesad"><i></i><i></i><i></i></div></div>"""
    return _kaks("h-moot", a, d, svg, lisa=f"""
.h-moot-seade{{background:{P['ha']};border-radius:28px;padding:22px;max-width:300px !important;box-shadow:inset 0 0 0 6px {P['hf']}}}
.h-moot-ekraan{{background:#C9D8C2;color:#16210F;border-radius:10px;padding:18px 20px;display:flex;align-items:baseline;justify-content:flex-end;gap:8px;font-family:var(--pea),monospace}}
.h-moot-ekraan b{{font-size:64px;line-height:1;letter-spacing:.04em}}
.h-moot-ketas{{width:150px;height:150px;margin:22px auto;border-radius:50%;background:{P['hf']};position:relative}}
.h-moot-ketas span{{position:absolute;left:50%;top:12px;width:12px;height:60px;margin-left:-6px;border-radius:6px;background:{P['ha']};transform-origin:6px 63px;transform:rotate(40deg)}}
@media (max-width:820px){{.h-moot-seade{{max-width:220px !important}}.h-moot-ekraan b{{font-size:44px}}.h-moot-ketas{{width:100px;height:100px}}.h-moot-ketas span{{height:40px;transform-origin:6px 43px}}}}
.h-moot-pesad{{display:flex;justify-content:space-around}}.h-moot-pesad i{{width:30px;height:30px;border-radius:50%;background:{P['hf']};box-shadow:inset 0 0 0 8px {mix(P['hf'], P['ha'], .6)}}}""")


def hero_led(a, d):
    P = d["p"]
    h = f"""<section class="h-led" aria-labelledby="pk">
  <div class="wrap h-led-sisu">{_sisu(a, d)}</div>
</section>"""
    c = baas("h-led", P, "112px 0 120px") + f""".h-led{{background-image:radial-gradient(circle,{P['ha']} 0 3px,transparent 4px),radial-gradient(circle,{mix(P['hf'], P['hb'], .14)} 0 3px,transparent 4px);background-size:96px 96px,24px 24px;background-position:12px 12px,0 0}}
.h-led-sisu{{position:relative}}.h-led h1{{max-width:11em;background:{P['hb']};display:inline;box-decoration-break:clone;-webkit-box-decoration-break:clone;padding:0 .12em}}
.h-led .lead{{background:{P['hb']};margin-top:28px;padding:6px 0}}"""
    return h, c


def hero_mast(a, d):
    P = d["p"]
    svg = f"""<svg viewBox="0 0 300 380" aria-hidden="true" focusable="false" fill="none" stroke="{P['hf']}" stroke-width="5" stroke-linejoin="round">
<path d="M150 10L96 370M150 10L204 370M118 220H182M128 150H172M106 300H194M118 220L194 300M182 220L106 300M128 150L182 220M172 150L118 220"/>
<path d="M40 80H260M60 130H240" /><path d="M150 10L40 80M150 10L260 80M128 150L60 130M172 150L240 130"/>
<g stroke="{P['ha']}" stroke-width="3"><path d="M40 86C10 140-10 160-40 170M260 86C290 140 310 160 340 170M60 136C40 180 20 200 -10 210M240 136C260 180 280 200 310 210"/></g></svg>"""
    return _kaks("h-mast", a, d, svg, pad="64px 0 72px")


def hero_pesad(a, d):
    P = d["p"]
    pesa = f'<svg viewBox="0 0 120 120" aria-hidden="true" focusable="false"><rect x="4" y="4" width="112" height="112" rx="22" fill="{P["hf"]}"/><circle cx="60" cy="60" r="38" fill="{mix(P["hf"], P["hb"], .85)}"/><circle cx="46" cy="60" r="6" fill="{P["hb"]}"/><circle cx="74" cy="60" r="6" fill="{P["hb"]}"/></svg>'
    h = f"""<section class="h-pesad" aria-labelledby="pk">
  <div class="wrap">{_sisu(a, d)}<div class="h-pesad-rida" aria-hidden="true">{pesa * 3}<span class="h-pesad-pistik"></span></div></div>
</section>"""
    c = baas("h-pesad", P, "88px 0 80px") + f""".h-pesad h1{{max-width:12em}}
.h-pesad-rida{{display:flex;gap:14px;margin-top:56px;align-items:center}}.h-pesad-rida svg{{width:clamp(64px,10vw,110px)}}
.h-pesad-pistik{{width:clamp(60px,14vw,180px);height:16px;border-radius:8px;background:{P['ha']}}}"""
    return h, c


def hero_triibud(a, d):
    P = d["p"]
    h = f"""<section class="h-trii" aria-labelledby="pk">
  <div class="h-trii-ribad" aria-hidden="true"><span></span><span></span><span></span><span></span><span></span></div>
  <div class="wrap h-trii-sisu">{_sisu(a, d)}</div>
</section>"""
    c = baas("h-trii", P, "96px 0 104px") + """.h-trii-ribad{position:absolute;top:0;bottom:0;right:0;width:min(34%,380px);display:flex}
.h-trii-ribad span{flex:1}.h-trii-ribad span:nth-child(1){background:#7A4A26}.h-trii-ribad span:nth-child(2){background:#1A1A1A}
.h-trii-ribad span:nth-child(3){background:#8C8C8C}.h-trii-ribad span:nth-child(4){background:#2F6FD6}
.h-trii-ribad span:nth-child(5){background:repeating-linear-gradient(0deg,#3D9A3D 0 28px,#F2D21B 28px 56px)}
.h-trii-sisu{position:relative}.h-trii-sisu>*{max-width:min(640px,62%)}.h-trii h1{font-size:clamp(32px,5vw,72px)}
@media (max-width:760px){.h-trii-ribad{width:100%;height:14px;top:auto}.h-trii-sisu>*{max-width:none}}"""
    return h, c


def hero_ostsill(a, d):
    P = d["p"]
    svg = f"""<div class="joonis h-osts-ekraan" aria-hidden="true"><svg viewBox="0 0 300 200" focusable="false">
<path d="M0 50H300M0 100H300M0 150H300M60 0V200M120 0V200M180 0V200M240 0V200" stroke="{mix(P['ha'], '#0B140E', .25)}" stroke-width="1"/>
<path d="M0 140H40V60H100V140H160V60H220V140H280V60H300" fill="none" stroke="{P['ha']}" stroke-width="4"/></svg></div>"""
    return _kaks("h-osts", a, d, svg, lisa=f"""
.h-osts-ekraan{{background:#0B140E;border:10px solid {P['hf']};border-radius:18px;padding:14px;box-shadow:0 0 30px {mix(P['ha'], P['hb'], .3)}}}""")


def hero_lambirida(a, d):
    P = d["p"]
    lambid = "".join(f'<span class="l{i}"><i></i></span>' for i in range(5))
    h = f"""<section class="h-lrida" aria-labelledby="pk">
  <div class="h-lrida-lambid" aria-hidden="true">{lambid}</div>
  <div class="wrap h-lrida-sisu">{_sisu(a, d)}</div>
</section>"""
    pikkus = [60, 120, 40, 100, 70]
    lcss = "".join(f".h-lrida-lambid .l{i}{{height:{p}px}}" for i, p in enumerate(pikkus))
    c = baas("h-lrida", P, "0 0 96px") + f""".h-lrida-lambid{{display:flex;justify-content:space-around;max-width:900px;margin:0 auto 24px;align-items:flex-start;height:200px}}
.h-lrida-lambid span{{width:2px;background:{P['hf']};position:relative}}
.h-lrida-lambid i{{position:absolute;bottom:-40px;left:-30px;width:62px;height:40px;border-radius:62px 62px 0 0;background:{P['hf']}}}
.h-lrida-lambid .l1 i{{background:{P['ha']};box-shadow:0 30px 60px {P['ha']}}}{lcss}
.h-lrida-sisu{{text-align:center;display:flex;flex-direction:column;align-items:center;padding-top:40px}}.h-lrida h1{{max-width:12em}}
.h-lrida .lead{{margin-left:auto;margin-right:auto}}.h-lrida .nupud{{justify-content:center}}
@media (max-width:600px){{.h-lrida-lambid .l3,.h-lrida-lambid .l4{{display:none}}}}"""
    return h, c


def hero_sade(a, d):
    P = d["p"]
    kiired = "".join(f'<line x1="150" y1="150" x2="150" y2="{18 if i % 2 else 52}" transform="rotate({i * 22.5} 150 150)"/>' for i in range(16))
    svg = f"""<svg viewBox="0 0 300 300" aria-hidden="true" focusable="false"><g stroke="{P['ha']}" stroke-width="6" stroke-linecap="round">{kiired}</g>
<circle cx="150" cy="150" r="70" fill="{P['hb']}"/><circle cx="150" cy="150" r="54" fill="{P['ha']}"/><path d="M158 112l-28 44h22l-10 34 30-48h-22z" fill="{P['haf']}"/></svg>"""
    return _kaks("h-sade", a, d, svg)


def hero_trummel(a, d):
    P = d["p"]
    svg = f"""<svg viewBox="0 0 320 320" aria-hidden="true" focusable="false"><circle cx="160" cy="160" r="150" fill="{P['hf']}"/>
<circle cx="160" cy="160" r="120" fill="none" stroke="{P['ha']}" stroke-width="14"/><circle cx="160" cy="160" r="100" fill="none" stroke="{P['ha']}" stroke-width="14"/>
<circle cx="160" cy="160" r="80" fill="none" stroke="{P['ha']}" stroke-width="14"/><circle cx="160" cy="160" r="48" fill="{P['hb']}"/><circle cx="160" cy="160" r="14" fill="{P['hf']}"/>
<path d="M280 160C300 230 320 260 380 280" stroke="{P['ha']}" stroke-width="14" fill="none"/></svg>"""
    return _kaks("h-trum", a, d, svg)


def hero_toide(a, d):
    P = d["p"]
    h = f"""<section class="h-toide" aria-labelledby="pk">
  <svg class="h-toide-svg" viewBox="0 0 200 200" aria-hidden="true" focusable="false" fill="none" stroke="{P['ha']}" stroke-width="16" stroke-linecap="round"><path d="M64 48a74 74 0 1 0 72 0"/><line x1="100" y1="16" x2="100" y2="96"/></svg>
  <div class="wrap h-toide-sisu">{_sisu(a, d)}</div>
</section>"""
    c = baas("h-toide", P, "104px 0 112px") + """.h-toide-svg{position:absolute;right:-6%;top:50%;width:min(560px,52vw);transform:translateY(-50%);opacity:.9}
.h-toide-sisu{position:relative}.h-toide h1{max-width:9em}.h-toide .lead{max-width:26em}
@media (max-width:760px){.h-toide-svg{opacity:.18;width:90vw}}"""
    return h, c


HEROD = dict(pistik=hero_pistik, valk=hero_valk, skeem=hero_skeem, kilp=hero_kilp, lamp=hero_lamp, kaablid=hero_kaablid,
             siinus=hero_siinus, lyliti=hero_lyliti, hoiatus=hero_hoiatus, plaan=hero_plaan, mootur=hero_mootur, led=hero_led,
             mast=hero_mast, pesad=hero_pesad, triibud=hero_triibud, ostsill=hero_ostsill, lambirida=hero_lambirida,
             sade=hero_sade, trummel=hero_trummel, toide=hero_toide)

FONDID = [("Archivo", "Inter", "900", "-0.035em"), ("Space Grotesk", "Inter", "700", "-0.035em"), ("Unbounded", "Manrope", "900", "-0.04em"),
          ("Bricolage Grotesque", "Manrope", "800", "-0.035em"), ("Epilogue", "Inter", "800", "-0.03em"), ("Syne", "Inter", "800", "-0.03em"),
          ("Familjen Grotesk", "Inter", "700", "-0.03em"), ("Inter Display", "Inter", "800", "-0.03em"), ("Space Grotesk", "Space Grotesk", "700", "-0.04em"),
          ("Archivo", "Manrope", "800", "-0.03em"), ("Fraunces", "Inter", "900", "-0.02em"), ("Bricolage Grotesque", "Inter", "700", "-0.04em")]
TEEN = ["kaardid", "read", "numbrid", "veerud", "plaadid"]
GAL = ["ruudustik", "mosaiik", "riba", "polaroid"]
KAIK = ["rida", "ajajoon", "redel", "kaardid"]

# (võti, avaplokk, pealkiri, (bg, fg, aktsent, avaploki taust, avaploki tekst, avaploki aktsent), raadius, päis)
ELEKTRIKUD = [
    ("e-vitali", "pistik", "Elekter korda Maardus.", ("#FFFFFF", "#111827", "#1D4ED8", "#0F1B3D", "#FFFFFF", "#FACC15"), "10px", "tume"),
    ("e-calmar", "valk", "Viljandi elektritööd.", ("#FFFFFF", "#0F172A", "#0E7490", "#F2F5F7", "#0F172A", "#F59E0B"), "4px", "hele"),
    ("e-elfi", "skeem", "Elektritööd Raplamaal.", ("#FAFAF7", "#13241B", "#166534", "#0F2418", "#FFFFFF", "#4ADE80"), "6px", "tume"),
    ("e-khs", "kilp", "Elektrik Jõgevamaal.", ("#FFFFFF", "#1C1917", "#C2410C", "#FFF4E8", "#1C1917", "#EA580C"), "8px", "hele"),
    ("e-tavako", "lamp", "Pärnu elektritööd algusest lõpuni.", ("#FFFFFF", "#18181B", "#A16207", "#18181B", "#FFFFFF", "#FACC15"), "999px", "tume"),
    ("e-gentroon", "kaablid", "Elektritööd Pärnus ja Pärnumaal.", ("#FFFFFF", "#0B1F33", "#0369A1", "#E8F1F8", "#0B1F33", "#0369A1"), "6px", "hele"),
    ("e-elmiku", "siinus", "Saaremaa elektritööd.", ("#F8FAFC", "#0C1A2B", "#1E40AF", "#0C1A2B", "#FFFFFF", "#38BDF8"), "8px", "varv"),
    ("e-hooneabi", "lyliti", "Elekter, mis lihtsalt töötab.", ("#FFFFFF", "#1F2937", "#B91C1C", "#F3F4F6", "#1F2937", "#DC2626"), "14px", "hele"),
    ("e-el-teh", "hoiatus", "Juhtmest kilbini.", ("#FFFFFF", "#111111", "#111111", "#111111", "#FFFFFF", "#FACC15"), "0px", "tume"),
    ("e-l-viru", "plaan", "Elektritööd Ida-Virumaal.", ("#F7FAFF", "#0A2540", "#1D4ED8", "#0A3A7A", "#FFFFFF", "#FDE047"), "4px", "varv"),
    ("e-reljans", "mootur", "Narva elektritööd.", ("#FFFFFF", "#1A1A1A", "#B45309", "#FBF6EE", "#1A1A1A", "#F59E0B"), "10px", "hele"),
    ("e-kangro-nagla", "led", "Elektritööd Elva kandis.", ("#FFFFFF", "#0F1A14", "#047857", "#0F1A14", "#FFFFFF", "#34D399"), "6px", "tume"),
    ("e-jannes", "mast", "Mulgimaa elektrik.", ("#FBFBF8", "#1E2420", "#4D7C0F", "#E9F0DF", "#1E2420", "#65A30D"), "4px", "hele"),
    ("e-electra", "pesad", "Tallinna elektritööd.", ("#FFFFFF", "#0D0D12", "#6D28D9", "#0D0D12", "#FFFFFF", "#A78BFA"), "12px", "tume"),
    ("e-peetri", "triibud", "Elektrik Saaremaal.", ("#FFFFFF", "#1B1B1B", "#1D4ED8", "#FFFFFF", "#1B1B1B", "#1D4ED8"), "2px", "hele"),
    ("e-albol", "ostsill", "Elektritööd Otepää kandis.", ("#F9FAF7", "#16201A", "#15803D", "#16201A", "#FFFFFF", "#86EFAC"), "8px", "varv"),
    ("e-sikuway", "lambirida", "Türi elektrik.", ("#FFFFFF", "#1F1A14", "#B45309", "#1F1A14", "#FFFFFF", "#FBBF24"), "999px", "tume"),
    ("e-valgis", "sade", "Valgus ja vool Narvas.", ("#FFFFFF", "#0B1A2E", "#0F5BD8", "#EAF2FF", "#0B1A2E", "#0F5BD8"), "10px", "hele"),
    ("e-eurest", "trummel", "Elektritööd Keilas.", ("#FFFFFF", "#202020", "#C2410C", "#202020", "#FFFFFF", "#FB923C"), "6px", "tume"),
    ("e-stablenord", "toide", "Vool sees, mure läinud.", ("#F8FAFC", "#0B1324", "#2563EB", "#0B1324", "#FFFFFF", "#60A5FA"), "16px", "varv"),
    ("e-elredi", "kilp", "Elektrik Tallinnas.", ("#FFFFFF", "#0F172A", "#0F766E", "#0F172A", "#FFFFFF", "#2DD4BF"), "4px", "tume"),
    ("e-kaabeldusabi", "kaablid", "Kaabeldus ja elekter Jõgevamaal.", ("#FFFFFF", "#1C1917", "#9A3412", "#1C1917", "#FFFFFF", "#FDBA74"), "8px", "tume"),
    ("e-aavo", "pistik", "Tartu elektrik.", ("#FFFFFF", "#1E1B4B", "#4338CA", "#EEF0FF", "#1E1B4B", "#4338CA"), "16px", "hele"),
    ("e-winels", "toide", "Winels. Elektritööd Tallinnas.", ("#FFFFFF", "#111827", "#DC2626", "#FFF1F1", "#111827", "#DC2626"), "6px", "hele"),
    ("e-elren", "mast", "Saare elektrik.", ("#F8FAFC", "#0B2533", "#0E7490", "#0B2533", "#FFFFFF", "#67E8F9"), "4px", "varv"),
    ("e-elortex", "led", "Pärnu elektrik.", ("#FFFFFF", "#18181B", "#CA8A04", "#FFFBEA", "#18181B", "#CA8A04"), "12px", "hele"),
    ("e-estomeister", "valk", "Keila elektritööd.", ("#FFFFFF", "#0C0A09", "#0C0A09", "#0C0A09", "#FFFFFF", "#FDE047"), "0px", "tume"),
    ("e-otto", "lamp", "Elektrik Jõgeva kandis.", ("#FFFDF7", "#1F1A10", "#92400E", "#FEF3C7", "#1F1A10", "#D97706"), "999px", "hele"),
    ("e-pistrel", "pesad", "Pistik, lüliti ja kilp.", ("#FFFFFF", "#102A43", "#0B69A3", "#E3F0FA", "#102A43", "#0B69A3"), "18px", "hele"),
    ("e-tagener", "skeem", "Elektritööd Tartus.", ("#FFFFFF", "#111111", "#4F46E5", "#FFFFFF", "#111111", "#4F46E5"), "8px", "hele"),
    ("e-maasvool", "siinus", "Maasvool. Elekter Pärnus.", ("#FAFAF9", "#1C1917", "#15803D", "#ECFDF3", "#1C1917", "#15803D"), "6px", "hele"),
    ("e-4a-lux", "lambirida", "Valgus Tori vallas.", ("#FFFFFF", "#111827", "#7C3AED", "#111827", "#FFFFFF", "#FDE68A"), "999px", "tume"),
    ("e-elektriparadiis", "sade", "Elektriparadiis Maardus.", ("#FFFFFF", "#1A0F2E", "#9333EA", "#1A0F2E", "#FFFFFF", "#F0ABFC"), "14px", "tume"),
    ("e-ss-elektritood", "hoiatus", "Elektritööd Pärnus ja ümbruses.", ("#FFFFFF", "#1B1B1B", "#1B1B1B", "#FFF8DB", "#1B1B1B", "#F5C400"), "2px", "hele"),
    ("e-toostuselekter", "trummel", "Elektritööd Viljandis.", ("#FFFFFF", "#0F172A", "#1D4ED8", "#DBEAFE", "#0F172A", "#1D4ED8"), "8px", "hele"),
    ("e-sven", "lyliti", "Elva kandi elektrik.", ("#FFFFFF", "#132A13", "#2F6B2F", "#132A13", "#FFFFFF", "#A3E635"), "10px", "tume"),
    ("e-eligero", "plaan", "Elektrik Ida-Virumaal.", ("#FFFFFF", "#111827", "#0369A1", "#FFFFFF", "#111827", "#0369A1"), "4px", "hele"),
    ("e-msl", "triibud", "Võrumaa elektritööd.", ("#FFFFFF", "#0F0F0F", "#B91C1C", "#0F0F0F", "#FFFFFF", "#F87171"), "4px", "tume"),
    ("e-ete-worx", "ostsill", "Elektritööd Jõhvi kandis.", ("#FFFFFF", "#0B1410", "#0F766E", "#ECFDF5", "#0B1410", "#0F766E"), "12px", "hele"),
    ("e-martipet", "mootur", "Elektrik pealinnas.", ("#FFFFFF", "#1E1E1E", "#C2410C", "#1E1E1E", "#FFFFFF", "#FDBA74"), "8px", "tume"),
]

for i, (nimi, hero, h1, (bg, fg, acc, hb, hf, ha), raadius, pais) in enumerate(ELEKTRIKUD):
    pea, keha, kaal, ls = FONDID[(i * 5) % len(FONDID)]
    P = pal(bg, fg, acc, mix(fg, "#000000", .9), ha, hb, hf, ha, raadius, pea=f"'{pea}'", keha=f"'{keha}'", pea_kaal=kaal, pea_ls=ls)
    K[nimi] = dict(hero=HEROD[hero], h1=h1, p=P, pea=pea, keha=keha, theme=P["hb"], teenused=TEEN[i % 5], galerii=GAL[(i * 3) % 4],
                   kaik=KAIK[(i // 2) % 4], pais=pais, vars=P["vars"], css=pais_css(pais, P, i))
