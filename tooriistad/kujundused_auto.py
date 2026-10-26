"""Autoteeninduste kujundused. Iga avaplokk on eri idee autode maailmast."""
from sisu import E, teenused
from kujundused import nupud, lead, v


def _teenused(a):
    return teenused(a.get("teenused_voti") or a["emtak"])


# ---------------- 500 € ----------------

def hero_tahhomeeter(a, d):
    kriipsud = "".join(
        f'<line x1="150" y1="22" x2="150" y2="{38 if i % 2 else 46}" stroke="{"#FF6B1A" if i > 14 else "#C9D1D9"}" stroke-width="{4 if i % 2 == 0 else 2}" transform="rotate({-120 + i * 12} 150 150)"/>'
        for i in range(21))
    h = f"""<section class="h-tahho" aria-labelledby="pk">
  <div class="wrap h-tahho-sisu">
    <div><h1 id="pk">{E(d["h1"])}</h1>{lead(a)}{nupud(a)}</div>
    <svg class="h-moodik" viewBox="0 0 300 260" aria-hidden="true" focusable="false">
      <path d="M40 210A125 125 0 1 1 260 210" fill="none" stroke="#252C34" stroke-width="18" stroke-linecap="round"/>
      <path d="M210 52A125 125 0 0 1 260 210" fill="none" stroke="#FF6B1A" stroke-width="18" stroke-linecap="round"/>
      {kriipsud}
      <line x1="150" y1="150" x2="150" y2="48" stroke="#FF6B1A" stroke-width="5" stroke-linecap="round" transform="rotate(38 150 150)"/>
      <circle cx="150" cy="150" r="14" fill="#FF6B1A"/><circle cx="150" cy="150" r="5" fill="#101418"/>
    </svg>
  </div>
</section>"""
    c = """.h-tahho{background:radial-gradient(ellipse at 75% 40%,#1C232B,#101418 60%);color:#fff;padding:72px 0 96px}
.h-tahho-sisu{display:grid;grid-template-columns:1.2fr 1fr;gap:48px;align-items:center}
.h-tahho h1{font-size:clamp(42px,6.4vw,92px);line-height:.95;font-weight:900;letter-spacing:-.035em;margin:0 0 24px}
.h-tahho .lead{color:#D5DCE3}
.h-tahho .nupp.teine{color:#fff}
@media (max-width:860px){.h-tahho-sisu{grid-template-columns:1fr}.h-moodik{max-width:300px}}"""
    return h, c


def hero_rehvijalg(a, d):
    h = f"""<section class="h-rehv" aria-labelledby="pk">
  <div class="h-muster-rehv" aria-hidden="true"></div>
  <div class="wrap h-rehv-sisu"><h1 id="pk">{E(d["h1"])}</h1><div class="h-rehv-all">{lead(a)}{nupud(a)}</div></div>
  <div class="h-muster-rehv" aria-hidden="true"></div>
</section>"""
    c = """.h-rehv{background:#F4F4F2}
.h-muster-rehv{height:64px;background:
 linear-gradient(135deg,transparent 0 30%,#F4F4F2 30% 40%,transparent 40%) 0 0/48px 64px,
 linear-gradient(225deg,transparent 0 30%,#F4F4F2 30% 40%,transparent 40%) 24px 0/48px 64px,#1E1E1E}
.h-rehv-sisu{padding-top:64px;padding-bottom:64px}
.h-rehv h1{font-size:clamp(38px,6.6vw,96px);line-height:1.02;font-weight:900;letter-spacing:-.03em;margin:0 0 36px;max-width:11em}
.h-rehv-all{display:grid;grid-template-columns:1fr auto;gap:32px;align-items:end}
.h-rehv .lead{margin:0}
.h-rehv .nupp.pea{background:#1E1E1E;color:#F2C230}
@media (max-width:760px){.h-rehv-all{grid-template-columns:1fr}}"""
    return h, c


def hero_numbrimark(a, d):
    tekst = a["lyhinimi"].upper()
    if len(tekst) > 9:
        tekst = tekst.split()[0][:9]
    h = f"""<section class="h-numbri" aria-labelledby="pk">
  <div class="wrap h-numbri-sisu">
    <div class="h-mark" aria-hidden="true"><span class="h-mark-eu">EST</span><span class="h-mark-tekst">{E(tekst)}</span></div>
    <h1 id="pk">{E(d["h1"])}</h1>
    {lead(a)}{nupud(a)}
  </div>
</section>"""
    c = """.h-numbri{background:linear-gradient(#E9EEF5,#F7F9FB);padding:72px 0 88px}
.h-numbri-sisu{display:flex;flex-direction:column;align-items:flex-start}
.h-mark{display:flex;align-items:stretch;background:#fff;border:5px solid #111;border-radius:10px;overflow:hidden;margin-bottom:36px;box-shadow:0 18px 40px -22px rgba(0,0,0,.45)}
.h-mark-eu{background:#0D3B8C;color:#fff;font-weight:700;font-size:clamp(14px,2vw,22px);display:flex;align-items:flex-end;padding:10px 10px 8px}
.h-mark-tekst{font-family:var(--pea),sans-serif;font-weight:700;font-size:clamp(40px,8vw,110px);letter-spacing:.06em;padding:4px 24px 0;color:#111;line-height:1.1}
.h-numbri h1{font-size:clamp(34px,4.6vw,60px);line-height:1.02;font-weight:700;letter-spacing:-.03em;margin:0 0 20px;max-width:16em}"""
    return h, c


def hero_mutrivoti(a, d):
    h = f"""<section class="h-voti" aria-labelledby="pk">
  <svg class="h-voti-svg" viewBox="0 0 400 400" aria-hidden="true" focusable="false">
    <path d="M300 40a70 70 0 0 0-92 86L60 274a34 34 0 1 0 48 48l148-148a70 70 0 0 0 86-92l-40 40-44-12-12-44z" fill="none" stroke="#C9A24A" stroke-width="6" stroke-linejoin="round"/>
  </svg>
  <div class="wrap h-voti-sisu"><h1 id="pk">{E(d["h1"])}</h1>{lead(a)}{nupud(a)}</div>
</section>"""
    c = """.h-voti{position:relative;background:#1F3D2B;color:#fff;overflow:hidden;padding:88px 0 104px}
.h-voti-svg{position:absolute;right:-40px;top:50%;width:520px;height:520px;margin-top:-260px;opacity:.85}
.h-voti-sisu{position:relative}
.h-voti h1{font-size:clamp(42px,6.4vw,92px);line-height:.96;font-weight:800;letter-spacing:-.03em;margin:0 0 24px;max-width:9.5em}
.h-voti .lead{color:#DDE7DF}
.h-voti .nupp.pea{background:#C9A24A;color:#1A2A1F}
.h-voti .nupp.teine{color:#fff}
@media (max-width:760px){.h-voti-svg{width:300px;height:300px;margin-top:-150px;right:-120px;opacity:.35}}"""
    return h, c


def hero_hooldusraamat(a, d):
    t = _teenused(a)
    read = "".join(f'<li><span>{E(n)}</span><span class="h-tempel" aria-hidden="true">tehtud</span></li>' for n, _, _ in t[:3])
    h = f"""<section class="h-raamat" aria-labelledby="pk">
  <div class="wrap h-raamat-sisu">
    <div><h1 id="pk">{E(d["h1"])}</h1>{lead(a)}{nupud(a)}</div>
    <div class="h-raamat-leht" aria-hidden="true"><p class="h-raamat-pk">Hooldusraamat</p><ul>{read}</ul></div>
  </div>
</section>"""
    c = """.h-raamat{background:#14294A;color:#fff;padding:72px 0 96px}
.h-raamat-sisu{display:grid;grid-template-columns:1.2fr 1fr;gap:56px;align-items:center}
.h-raamat h1{font-size:clamp(40px,5.6vw,78px);line-height:1;font-weight:400;margin:0 0 24px}
.h-raamat .lead{color:#DCE4F0}
.h-raamat .nupp.pea{background:#fff;color:#14294A}
.h-raamat .nupp.teine{color:#fff}
.h-raamat-leht{background:#FBF8F1;color:#14294A;padding:30px 30px 36px;border-radius:4px;transform:rotate(-2deg);box-shadow:0 30px 50px -24px rgba(0,0,0,.6);border-left:10px solid #B2332B}
.h-raamat-pk{font-family:var(--pea),serif;font-size:28px;margin:0 0 12px}
.h-raamat-leht ul{list-style:none;margin:0;padding:0}
.h-raamat-leht li{display:flex;justify-content:space-between;align-items:center;padding:14px 0;border-bottom:1px solid #D9D2C3;font-weight:600}
.h-tempel{color:#B2332B;border:2px solid #B2332B;border-radius:50%;padding:6px 8px;font-size:12px;text-transform:uppercase;letter-spacing:.06em;transform:rotate(-12deg)}
@media (max-width:860px){.h-raamat-sisu{grid-template-columns:1fr}.h-raamat-leht{transform:none}}"""
    return h, c


def hero_velg(a, d):
    kodarad = "".join(f'<path d="M150 150L140 46Q150 40 160 46Z" fill="url(#kroom)" transform="rotate({i * 72} 150 150)"/>' for i in range(5))
    h = f"""<section class="h-velg" aria-labelledby="pk">
  <div class="wrap h-velg-sisu">
    <svg class="h-ratas" viewBox="0 0 300 300" aria-hidden="true" focusable="false">
      <defs><linearGradient id="kroom" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F2F4F7"/><stop offset=".5" stop-color="#8B95A1"/><stop offset="1" stop-color="#E4E8ED"/></linearGradient></defs>
      <circle cx="150" cy="150" r="146" fill="#16191E"/><circle cx="150" cy="150" r="112" fill="none" stroke="url(#kroom)" stroke-width="10"/>
      {kodarad}<circle cx="150" cy="150" r="24" fill="url(#kroom)"/><circle cx="150" cy="150" r="8" fill="#E03A3A"/>
    </svg>
    <div><h1 id="pk">{E(d["h1"])}</h1>{lead(a)}{nupud(a)}</div>
  </div>
</section>"""
    c = """.h-velg{background:#0E1116;color:#fff;padding:72px 0 96px}
.h-velg-sisu{display:grid;grid-template-columns:1fr 1.2fr;gap:56px;align-items:center}
.h-ratas{animation:veere 18s linear infinite}
@keyframes veere{to{transform:rotate(360deg)}}
.h-velg h1{font-size:clamp(42px,6.4vw,92px);line-height:.95;font-weight:800;letter-spacing:-.035em;margin:0 0 24px}
.h-velg .lead{color:#D2D8DF}
.h-velg .nupp.teine{color:#fff}
@media (max-width:860px){.h-velg-sisu{grid-template-columns:1fr}.h-ratas{max-width:260px}}"""
    return h, c


def hero_garaaziuks(a, d):
    h = f"""<section class="h-uks" aria-labelledby="pk">
  <div class="h-lamellid" aria-hidden="true"></div>
  <div class="h-uks-ava">
    <div class="wrap"><h1 id="pk">{E(d["h1"])}</h1>{lead(a)}{nupud(a)}</div>
  </div>
</section>"""
    c = """.h-uks{background:#2A2D31}
.h-lamellid{height:170px;background:repeating-linear-gradient(#9AA0A6 0 30px,#7F858B 30px 32px,#A9AFB5 32px 34px);border-bottom:10px solid #3A3E43;box-shadow:0 12px 24px -6px rgba(0,0,0,.6) inset}
.h-uks-ava{background:radial-gradient(ellipse at 50% 0,#F29A3C 0,#C4621F 35%,#2A2D31 80%);color:#fff;padding:60px 0 96px}
.h-uks h1{font-size:clamp(42px,6.6vw,96px);line-height:.95;font-weight:800;letter-spacing:-.035em;margin:0 0 24px;max-width:10em}
.h-uks .lead{color:#FBE9DA}
.h-uks .nupp.pea{background:#fff;color:#2A2D31}
.h-uks .nupp.teine{color:#fff}
@media (max-width:600px){.h-lamellid{height:90px}}"""
    return h, c


def hero_armatuur(a, d):
    tuled = [("#F2A93B", '<path d="M8 20h6l2-4h8l2 4h4v8H8z M12 28v3M28 28v3" fill="none" stroke="currentColor" stroke-width="2"/>'),
             ("#E5484D", '<rect x="8" y="12" width="24" height="16" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M13 12V9M27 12V9M14 20h4M23 18v4M21 20h4" stroke="currentColor" stroke-width="2"/>'),
             ("#F2A93B", '<path d="M10 24c4-8 16-8 20 0M20 10v8" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="20" cy="26" r="2" fill="currentColor"/>'),
             ("#46B97A", '<path d="M8 22h24M14 16l-6 6 6 6M26 16l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2"/>')]
    ikoonid = "".join(f'<span class="h-tuli t{i}"><svg viewBox="0 0 40 40" aria-hidden="true" focusable="false">{p}</svg></span>' for i, (_, p) in enumerate(tuled))
    h = f"""<section class="h-armatuur" aria-labelledby="pk">
  <div class="wrap">
    <div class="h-tuled" aria-hidden="true">{ikoonid}</div>
    <h1 id="pk">{E(d["h1"])}</h1>
    {lead(a)}{nupud(a)}
  </div>
</section>"""
    c = ".h-armatuur{background:#0B0D10;color:#fff;padding:72px 0 96px}\n.h-tuled{display:flex;gap:18px;margin-bottom:40px}\n"
    c += ".h-tuli{width:64px;height:64px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:#161A1F}\n.h-tuli svg{width:40px;height:40px}\n"
    for i, (col, _) in enumerate(tuled):
        c += f".h-tuli.t{i}{{color:{col};box-shadow:0 0 24px -2px {col}}}\n"
    c += ".h-armatuur h1{font-size:clamp(40px,6vw,86px);line-height:.98;font-weight:700;letter-spacing:-.035em;margin:0 0 24px;max-width:12em}\n.h-armatuur .lead{color:#D0D6DC}\n.h-armatuur .nupp.teine{color:#fff}"
    return h, c


def hero_maantee(a, d):
    h = f"""<section class="h-tee" aria-labelledby="pk">
  <div class="wrap h-tee-sisu"><h1 id="pk">{E(d["h1"])}</h1>{lead(a)}{nupud(a)}</div>
  <div class="h-teekate" aria-hidden="true"><span></span></div>
</section>"""
    c = """.h-tee{background:linear-gradient(#DDEBF3,#F0F6F9 55%,#8DB36A 55%,#6E9A4F);padding-top:72px;overflow:hidden}
.h-tee h1{font-size:clamp(40px,6.2vw,90px);line-height:.98;font-weight:700;letter-spacing:-.03em;margin:0 0 22px;max-width:11em}
.h-tee-sisu{padding-bottom:80px}
.h-tee .lead{background:rgba(240,246,249,.9)}
.h-teekate{height:220px;position:relative;background:#4A4F55;clip-path:polygon(44% 0,56% 0,100% 100%,0 100%)}
.h-teekate span{position:absolute;left:50%;top:0;bottom:0;width:12px;margin-left:-6px;background:repeating-linear-gradient(#F2F2EE 0 24px,transparent 24px 48px);clip-path:polygon(40% 0,60% 0,100% 100%,0 100%)}"""
    return h, c


def hero_kerevarv(a, d):
    h = f"""<section class="h-metall" aria-labelledby="pk">
  <div class="wrap"><h1 id="pk">{E(d["h1"])}</h1><div class="h-metall-all">{lead(a)}{nupud(a)}</div></div>
</section>"""
    c = """.h-metall{color:#fff;padding:100px 0 96px;background:
 radial-gradient(circle at 20% 20%,rgba(255,255,255,.35),transparent 30%),
 radial-gradient(circle at 80% 70%,rgba(120,170,255,.35),transparent 40%),
 conic-gradient(from 210deg at 60% 40%,#0A1E4A,#1E4AA8,#0D2A66,#3A6FD8,#0A1E4A)}
.h-metall h1{font-size:clamp(44px,7.4vw,112px);line-height:.92;font-weight:900;letter-spacing:-.04em;margin:0 0 44px;max-width:10em}
.h-metall-all{display:grid;grid-template-columns:1fr auto;gap:32px;align-items:end;border-top:1px solid rgba(255,255,255,.4);padding-top:26px}
.h-metall .lead{margin:0;color:#E4ECFA}
.h-metall .nupp.pea{background:#fff;color:#0D2A66}
.h-metall .nupp.teine{color:#fff}
@media (max-width:760px){.h-metall-all{grid-template-columns:1fr}}"""
    return h, c


# ---------------- 250 € ----------------

def hero_tostuk(a, d):
    h = f"""<section class="h-tostuk" aria-labelledby="pk">
  <span class="h-post v" aria-hidden="true"></span><span class="h-post p" aria-hidden="true"></span>
  <div class="wrap h-tostuk-sisu"><h1 id="pk">{E(d["h1"])}</h1>{lead(a)}{nupud(a)}</div>
</section>"""
    c = """.h-tostuk{position:relative;background:#F3F3F0;padding:88px 0 96px;overflow:hidden}
.h-post{position:absolute;top:0;bottom:0;width:46px;background:repeating-linear-gradient(-45deg,#F2C200 0 18px,#1C1C1C 18px 36px)}
.h-post.v{left:0}.h-post.p{right:0}
.h-tostuk-sisu{position:relative;text-align:center;display:flex;flex-direction:column;align-items:center}
.h-tostuk h1{font-size:clamp(40px,6.4vw,92px);line-height:.96;font-weight:800;letter-spacing:-.035em;margin:0 0 22px;max-width:11em}
.h-tostuk .lead{margin-left:auto;margin-right:auto}
.h-tostuk .nupud{justify-content:center}
@media (max-width:600px){.h-post{width:18px}}"""
    return h, c


def hero_olitilk(a, d):
    h = f"""<section class="h-oli" aria-labelledby="pk">
  <div class="wrap h-oli-sisu">
    <svg class="h-tilk" viewBox="0 0 200 260" aria-hidden="true" focusable="false"><defs><linearGradient id="oli" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F7C76A"/><stop offset="1" stop-color="#B86E0E"/></linearGradient></defs>
      <path d="M100 10C100 10 20 120 20 170a80 80 0 0 0 160 0C180 120 100 10 100 10z" fill="url(#oli)"/><path d="M60 170a40 40 0 0 0 24 36" fill="none" stroke="#FFF3D6" stroke-width="8" stroke-linecap="round" opacity=".7"/></svg>
    <div><h1 id="pk">{E(d["h1"])}</h1>{lead(a)}{nupud(a)}</div>
  </div>
</section>"""
    c = """.h-oli{background:#17130E;color:#fff;padding:72px 0 96px}
.h-oli-sisu{display:grid;grid-template-columns:clamp(140px,20vw,240px) minmax(0,1fr);gap:64px;align-items:center}
.h-tilk{width:100%;height:auto}
.h-oli h1{font-size:clamp(30px,6.6vw,96px);line-height:.95;font-weight:800;letter-spacing:-.035em;margin:0 0 24px}
.h-oli .lead{color:#EADFCB}
.h-oli .nupp.pea{background:#E8A93A;color:#17130E}
.h-oli .nupp.teine{color:#fff}
@media (max-width:760px){.h-oli-sisu{grid-template-columns:minmax(0,1fr);gap:24px}.h-tilk{width:110px}}"""
    return h, c


def _hammasratas(cx, cy, r, n, klass):
    hambad = "".join(f'<rect x="{cx - 9}" y="{cy - r - 14}" width="18" height="22" rx="3" transform="rotate({i * 360 / n} {cx} {cy})"/>' for i in range(n))
    return f'<g class="{klass}" fill="none" stroke="#2B6CB0" stroke-width="4">{hambad}<circle cx="{cx}" cy="{cy}" r="{r}"/><circle cx="{cx}" cy="{cy}" r="{r * .35}"/></g>'


def hero_hammasrattad(a, d):
    h = f"""<section class="h-hamba" aria-labelledby="pk">
  <div class="wrap h-hamba-sisu">
    <div><h1 id="pk">{E(d["h1"])}</h1>{lead(a)}{nupud(a)}</div>
    <svg class="h-rattad" viewBox="0 0 360 320" aria-hidden="true" focusable="false">{_hammasratas(130, 150, 90, 12, "r1")}{_hammasratas(275, 230, 52, 8, "r2")}</svg>
  </div>
</section>"""
    c = """.h-hamba{background:#EEF3F8;padding:72px 0 96px}
.h-hamba-sisu{display:grid;grid-template-columns:1.2fr 1fr;gap:40px;align-items:center}
.h-hamba h1{font-size:clamp(40px,6vw,86px);line-height:.98;font-weight:700;letter-spacing:-.035em;margin:0 0 24px}
.h-rattad .r1{transform-origin:130px 150px;animation:poor 24s linear infinite}
.h-rattad .r2{transform-origin:275px 230px;animation:poor 14s linear infinite reverse}
@keyframes poor{to{transform:rotate(360deg)}}
@media (max-width:860px){.h-hamba-sisu{grid-template-columns:1fr}.h-rattad{max-width:280px}}"""
    return h, c


def hero_noolemark(a, d):
    h = f"""<section class="h-nool" aria-labelledby="pk">
  <div class="h-noolerida" aria-hidden="true"></div>
  <div class="wrap h-nool-sisu"><h1 id="pk">{E(d["h1"])}</h1>{lead(a)}{nupud(a)}</div>
</section>"""
    c = """.h-nool{background:#B4141B;color:#fff;padding-bottom:88px}
.h-noolerida{height:70px;background:linear-gradient(135deg,transparent 0 50%,#fff 50% 65%,transparent 65%) 0 0/70px 70px,linear-gradient(45deg,transparent 0 35%,#fff 35% 50%,transparent 50%) 0 0/70px 70px,#B4141B}
.h-nool-sisu{padding-top:64px}
.h-nool h1{font-size:clamp(30px,7.4vw,108px);line-height:1;font-weight:900;letter-spacing:-.03em;margin:0 0 24px;text-transform:uppercase;max-width:10em}
.h-nool .lead{color:#FBE3E4}
.h-nool .nupp.pea{background:#fff;color:#8E0F15}
.h-nool .nupp.teine{color:#fff}"""
    return h, c


def hero_teeviit(a, d):
    h = f"""<section class="h-viit" aria-labelledby="pk">
  <div class="wrap h-viit-sisu">
    <div class="h-mark-sinine" aria-hidden="true"><svg viewBox="0 0 100 100" focusable="false"><path d="M66 18a18 18 0 0 0-22 24L20 66a7 7 0 1 0 10 10l24-24a18 18 0 0 0 24-22l-9 9-9-3-3-9z" fill="#fff"/></svg></div>
    <div><h1 id="pk">{E(d["h1"])}</h1>{lead(a)}{nupud(a)}</div>
  </div>
</section>"""
    c = """.h-viit{background:#F5F7F9;padding:72px 0 96px}
.h-viit-sisu{display:grid;grid-template-columns:clamp(140px,18vw,240px) 1fr;gap:56px;align-items:center}
.h-mark-sinine{width:100%;aspect-ratio:1;background:#1A5BB8;border:8px solid #fff;outline:3px solid #1A5BB8;border-radius:16px;display:flex;align-items:center;justify-content:center}
.h-mark-sinine svg{width:62%}
.h-viit h1{font-size:clamp(40px,6vw,88px);line-height:.98;font-weight:800;letter-spacing:-.035em;margin:0 0 22px}
@media (max-width:760px){.h-viit-sisu{grid-template-columns:1fr;gap:28px}.h-mark-sinine{width:110px}}"""
    return h, c


def hero_sara(a, d):
    h = f"""<section class="h-sara" aria-labelledby="pk">
  <div class="wrap h-sara-sisu"><h1 id="pk">{E(d["h1"])}</h1>{lead(a)}{nupud(a)}</div>
</section>"""
    c = """.h-sara{color:#fff;padding:110px 0 110px;text-align:center;background:
 radial-gradient(circle at 18% 30%,rgba(255,255,255,.9) 0 1.5px,transparent 2.5px),
 radial-gradient(circle at 72% 22%,rgba(255,255,255,.8) 0 1px,transparent 2px),
 radial-gradient(circle at 84% 64%,rgba(255,255,255,.9) 0 2px,transparent 3px),
 radial-gradient(circle at 30% 76%,rgba(255,255,255,.7) 0 1px,transparent 2px),
 radial-gradient(ellipse at 50% -20%,#3A3F49,#0D0F13 65%)}
.h-sara-sisu{display:flex;flex-direction:column;align-items:center}
.h-sara h1{font-size:clamp(52px,9vw,136px);line-height:.92;font-weight:400;font-style:italic;letter-spacing:-.02em;margin:0 0 26px;background:linear-gradient(180deg,#fff 30%,#AEB6C2);-webkit-background-clip:text;background-clip:text;color:transparent}
.h-sara .lead{color:#D6DBE2;margin-left:auto;margin-right:auto}
.h-sara .nupud{justify-content:center}
.h-sara .nupp.pea{background:#fff;color:#0D0F13}
.h-sara .nupp.teine{color:#fff}"""
    return h, c


def hero_plekk(a, d):
    h = f"""<section class="h-plekk" aria-labelledby="pk">
  <svg class="h-kere" viewBox="0 0 1200 400" preserveAspectRatio="none" aria-hidden="true" focusable="false">
    <defs><linearGradient id="kv" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#E9EDF2"/><stop offset=".5" stop-color="#C6CDD6"/><stop offset="1" stop-color="#9BA5B1"/></linearGradient></defs>
    <path d="M0 260C200 180 400 160 600 170S1000 230 1200 200V400H0z" fill="url(#kv)"/>
    <path d="M0 300C260 230 460 220 640 228S1000 270 1200 250" fill="none" stroke="#fff" stroke-width="3" opacity=".8"/>
    <path d="M560 172C620 150 700 150 760 176" fill="none" stroke="#7D8794" stroke-width="2"/>
  </svg>
  <div class="wrap h-plekk-sisu"><h1 id="pk">{E(d["h1"])}</h1>{lead(a)}{nupud(a)}</div>
</section>"""
    c = """.h-plekk{position:relative;background:#C2402E;color:#fff;padding:80px 0 240px;overflow:hidden}
.h-kere{position:absolute;left:0;right:0;bottom:0;width:100%;height:240px}
.h-plekk-sisu{position:relative}
.h-plekk h1{font-size:clamp(46px,8vw,120px);line-height:.92;font-weight:900;letter-spacing:-.02em;margin:0 0 24px}
.h-plekk .lead{color:#FCE3DE}
.h-plekk .nupp.pea{background:#fff;color:#8E2A1D}
.h-plekk .nupp.teine{color:#fff}
@media (max-width:600px){.h-kere{height:120px}.h-plekk{padding-bottom:140px}}"""
    return h, c


def hero_tellimus(a, d):
    h = f"""<section class="h-pilet" aria-labelledby="pk">
  <div class="wrap">
    <div class="h-pilet-kaart">
      <div class="h-pilet-vasak"><h1 id="pk">{E(d["h1"])}</h1>{lead(a)}{nupud(a)}</div>
      <div class="h-pilet-parem" aria-hidden="true"><span>Töökäsk</span><span class="nr">Nr 001</span></div>
    </div>
  </div>
</section>"""
    c = """.h-pilet{background:#2F4858;padding:80px 0}
.h-pilet-kaart{display:grid;grid-template-columns:1fr 160px;background:#FFFDF8;border-radius:14px;overflow:hidden;box-shadow:0 30px 60px -30px rgba(0,0,0,.6)}
.h-pilet-vasak{padding:48px 44px}
.h-pilet-parem{border-left:3px dashed #C9C2B3;background:#F3EEE2;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;font-weight:700;color:#2F4858;writing-mode:vertical-rl;letter-spacing:.1em}
.h-pilet-parem .nr{font-family:var(--pea),sans-serif;font-size:28px}
.h-pilet h1{font-size:clamp(38px,5.4vw,74px);line-height:1;font-weight:700;letter-spacing:-.03em;margin:0 0 22px;color:#2F4858}
@media (max-width:700px){.h-pilet-kaart{grid-template-columns:1fr}.h-pilet-parem{writing-mode:horizontal-tb;border-left:0;border-top:3px dashed #C9C2B3;padding:16px;flex-direction:row}.h-pilet-vasak{padding:32px 22px}}"""
    return h, c


def hero_voidutriibud(a, d):
    h = f"""<section class="h-triibud2" aria-labelledby="pk">
  <span class="h-v-triip a" aria-hidden="true"></span><span class="h-v-triip b" aria-hidden="true"></span>
  <div class="wrap h-triibud2-sisu"><h1 id="pk">{E(d["h1"])}</h1>{lead(a)}{nupud(a)}</div>
</section>"""
    c = """.h-triibud2{position:relative;background:#FFFFFF;padding:96px 0 104px;overflow:hidden}
.h-v-triip{position:absolute;top:-20%;bottom:-20%;width:70px;transform:skewX(-18deg)}
.h-v-triip.a{right:22%;background:#E1251B}.h-v-triip.b{right:calc(22% - 100px);background:#111}
.h-triibud2-sisu{position:relative}
.h-triibud2 h1{font-size:clamp(40px,6.4vw,92px);line-height:.95;font-weight:900;font-style:italic;letter-spacing:-.04em;margin:0 0 24px;max-width:9em}
.h-triibud2 .lead{background:rgba(255,255,255,.92);max-width:26em}
@media (max-width:760px){.h-v-triip{width:34px;opacity:.25}}"""
    return h, c


def hero_toosein(a, d):
    h = f"""<section class="h-sein" aria-labelledby="pk">
  <div class="wrap h-sein-sisu">
    <div><h1 id="pk">{E(d["h1"])}</h1>{lead(a)}{nupud(a)}</div>
    <svg class="h-tooriistad" viewBox="0 0 280 280" aria-hidden="true" focusable="false">
      <g fill="#2E3A2F"><rect x="30" y="30" width="16" height="120" rx="8"/><rect x="22" y="140" width="32" height="70" rx="6" fill="#D9762B"/>
      <path d="M100 30h30v40l-15 10-15-10z"/><rect x="108" y="78" width="14" height="140" rx="7"/>
      <path d="M190 40a28 28 0 1 0 40 0l-8 22h-24z" /><rect x="203" y="70" width="14" height="150" rx="7"/></g>
    </svg>
  </div>
</section>"""
    c = """.h-sein{padding:72px 0 96px;background:radial-gradient(#C9B48A 2px,transparent 2.5px) 0 0/22px 22px,#E7D8B8}
.h-sein-sisu{display:grid;grid-template-columns:1.3fr 1fr;gap:48px;align-items:center}
.h-sein h1{font-size:clamp(44px,7vw,104px);line-height:.94;font-weight:700;letter-spacing:-.04em;margin:0 0 24px;color:#2E3A2F}
.h-sein .lead{color:#3A3F33}
@media (max-width:760px){.h-sein-sisu{grid-template-columns:1fr}.h-tooriistad{max-width:200px}}"""
    return h, c


K = {}


def lisa(nimi, **kw):
    K[nimi] = kw


lisa("tahhomeeter", hero=hero_tahhomeeter, pea="Archivo", keha="Inter", theme="#101418", h1="Auto korda, tee jälle lahti.",
     teenused="numbrid", galerii="mosaiik", kaik="rida", pais="must",
     vars=v(pea="'Archivo'", keha="'Inter'", pea_kaal="900", pea_ls="-0.035em", bg="#F6F7F8", fg="#101418", muted="#4A535C", surface="#E8ECEF", line="#CDD4DA",
            accent="#C2410C", accent_fg="#FFFFFF", dark="#101418", dark_fg="#FFFFFF", dark_accent="#FF8A47", fookus="#C2410C", raadius="4px"),
     css=".pais-must{background:#101418;color:#fff}.pais-must .logo-mark{width:22px;height:22px;border-radius:50%;border:3px solid #FF6B1A;border-bottom-color:transparent}")
lisa("rehvijalg", hero=hero_rehvijalg, pea="Unbounded", keha="Manrope", theme="#1E1E1E", h1="Rehvid vahetatud, auto teele.",
     teenused="read", galerii="ruudustik", kaik="redel", pais="hele",
     vars=v(pea="'Unbounded'", keha="'Manrope'", pea_kaal="900", pea_ls="-0.03em", bg="#FFFFFF", fg="#1E1E1E", muted="#4D4D4D", surface="#F4F4F2", line="#DADAD5",
            accent="#1E1E1E", accent_fg="#F2C230", dark="#1E1E1E", dark_fg="#FFFFFF", dark_accent="#F2C230", fookus="#B38600", raadius="999px"),
     css=".pais-hele .logo-mark{width:22px;height:22px;border-radius:50%;background:repeating-conic-gradient(#1E1E1E 0 20deg,#F2C230 20deg 40deg)}")
lisa("numbrimark", hero=hero_numbrimark, pea="Space Grotesk", keha="Inter", theme="#0D3B8C", h1="Põlva autoremont Vahtra tänaval.",
     teenused="kaardid", galerii="polaroid", kaik="ajajoon", pais="hele",
     vars=v(pea="'Space Grotesk'", keha="'Inter'", pea_kaal="700", pea_ls="-0.03em", bg="#FFFFFF", fg="#111827", muted="#4B5563", surface="#EEF2F8", line="#D3DBE8",
            accent="#0D3B8C", accent_fg="#FFFFFF", dark="#0D3B8C", dark_fg="#FFFFFF", dark_accent="#FFD34D", fookus="#0D3B8C", raadius="8px"),
     css=".pais-hele .logo-mark{width:26px;height:16px;border:2px solid #111;border-left:8px solid #0D3B8C;border-radius:3px}")
lisa("mutrivoti", hero=hero_mutrivoti, pea="Epilogue", keha="Manrope", theme="#1F3D2B", h1="Võru autoremont aastast 1999.",
     teenused="veerud", galerii="mosaiik", kaik="kaardid", pais="tume",
     vars=v(pea="'Epilogue'", keha="'Manrope'", pea_ls="-0.03em", bg="#FAFAF6", fg="#1A2A1F", muted="#4B584F", surface="#ECF1EC", line="#D0DBD2",
            accent="#1F3D2B", accent_fg="#FFFFFF", dark="#1F3D2B", dark_fg="#FFFFFF", dark_accent="#E2C276", fookus="#1F3D2B", raadius="3px"),
     css=".pais-tume{background:#1F3D2B;color:#fff}.pais-tume .logo-mark{width:20px;height:20px;border:3px solid #C9A24A;border-radius:50%;border-right-color:transparent;transform:rotate(45deg)}")
lisa("hooldusraamat", hero=hero_hooldusraamat, pea="DM Serif Display", keha="Manrope", theme="#14294A", h1="Iga hooldus kirjas, iga auto korras.",
     teenused="read", galerii="polaroid", kaik="ajajoon", pais="tume",
     vars=v(pea="'DM Serif Display'", keha="'Manrope'", pea_kaal="400", pea_ls="0", bg="#FBF8F1", fg="#14294A", muted="#4D5870", surface="#F0EADD", line="#DCD3C2",
            accent="#B2332B", accent_fg="#FFFFFF", dark="#14294A", dark_fg="#FFFFFF", dark_accent="#F0B5AE", fookus="#B2332B", raadius="4px"),
     css=".pais-tume{background:#14294A;color:#fff}.pais-tume .logo-mark{width:18px;height:22px;border-radius:2px;background:#FBF8F1;border-left:5px solid #B2332B}")
lisa("velg", hero=hero_velg, pea="Syne", keha="Inter", theme="#0E1116", h1="Rehvid ja veljed Pärnus.",
     teenused="plaadid", galerii="riba", kaik="redel", pais="must",
     vars=v(pea="'Syne'", keha="'Inter'", pea_ls="-0.035em", bg="#FFFFFF", fg="#0E1116", muted="#4B525B", surface="#EEF0F3", line="#D3D8DE",
            accent="#C42B2B", accent_fg="#FFFFFF", dark="#0E1116", dark_fg="#FFFFFF", dark_accent="#FF7A7A", fookus="#C42B2B", raadius="999px"),
     css=".pais-must{background:#0E1116;color:#fff}.pais-must .logo-mark{width:22px;height:22px;border-radius:50%;background:radial-gradient(circle,#E03A3A 0 3px,#8B95A1 3px 6px,#16191E 6px 8px,#C9CFD6 8px)}")
lisa("garaaziuks", hero=hero_garaaziuks, pea="Bricolage Grotesque", keha="Inter", theme="#2A2D31", h1="Jõgeva töökoda, uks on lahti.",
     teenused="kaardid", galerii="ruudustik", kaik="rida", pais="betoon",
     vars=v(pea="'Bricolage Grotesque'", keha="'Inter'", pea_ls="-0.035em", bg="#F7F6F4", fg="#1F2124", muted="#4C4F54", surface="#E9E7E3", line="#D2CFC9",
            accent="#B5531A", accent_fg="#FFFFFF", dark="#2A2D31", dark_fg="#FFFFFF", dark_accent="#F29A3C", fookus="#B5531A", raadius="6px"),
     css=".pais-betoon{background:#9AA0A6;color:#1F2124}.pais-betoon .logo-mark{width:24px;height:20px;background:repeating-linear-gradient(#2A2D31 0 3px,#C9CDD1 3px 5px)}")
lisa("armatuur", hero=hero_armatuur, pea="Space Grotesk", keha="Space Grotesk", theme="#0B0D10", h1="Tuli põleb armatuuril? Vaatame üle.",
     teenused="numbrid", galerii="mosaiik", kaik="kaardid", pais="must",
     vars=v(pea="'Space Grotesk'", keha="'Space Grotesk'", pea_kaal="700", pea_ls="-0.03em", bg="#FAFAFA", fg="#0B0D10", muted="#4A4F57", surface="#EDEFF2", line="#D3D7DD",
            accent="#B45309", accent_fg="#FFFFFF", dark="#0B0D10", dark_fg="#FFFFFF", dark_accent="#F2A93B", fookus="#B45309", raadius="10px"),
     css=".pais-must{background:#0B0D10;color:#fff}.pais-must .logo-mark{width:14px;height:14px;border-radius:50%;background:#F2A93B;box-shadow:0 0 10px #F2A93B,20px 0 0 #E5484D,40px 0 0 #46B97A;margin-right:44px}")
lisa("maantee", hero=hero_maantee, pea="Familjen Grotesk", keha="Familjen Grotesk", theme="#4A4F55", h1="Raplamaa autodele, maanteelt otse töökotta.",
     teenused="veerud", galerii="riba", kaik="ajajoon", pais="taevas",
     vars=v(pea="'Familjen Grotesk'", keha="'Familjen Grotesk'", pea_kaal="700", pea_ls="-0.03em", bg="#FFFFFF", fg="#1C2620", muted="#4A564E", surface="#EEF4EA", line="#D3DFCB",
            accent="#3F6B2A", accent_fg="#FFFFFF", dark="#2D3330", dark_fg="#FFFFFF", dark_accent="#B6D88F", fookus="#3F6B2A", raadius="6px"),
     css=".pais-taevas{background:#DDEBF3}.pais-taevas .logo-mark{width:24px;height:18px;background:#4A4F55;clip-path:polygon(40% 0,60% 0,100% 100%,0 100%)}")
lisa("kerevarv", hero=hero_kerevarv, pea="Archivo", keha="Manrope", theme="#0D2A66", h1="Tallinna autoremont aastast 1997.",
     teenused="plaadid", galerii="polaroid", kaik="rida", pais="metall",
     vars=v(pea="'Archivo'", keha="'Manrope'", pea_kaal="900", pea_ls="-0.04em", bg="#F7F9FD", fg="#0A1E4A", muted="#46536E", surface="#E6EDFA", line="#C9D6EE",
            accent="#1E4AA8", accent_fg="#FFFFFF", dark="#0A1E4A", dark_fg="#FFFFFF", dark_accent="#9CC0FF", fookus="#1E4AA8", raadius="4px"),
     css=".pais-metall{background:#0A1E4A;color:#fff}.pais-metall .logo-mark{width:22px;height:22px;border-radius:50%;background:conic-gradient(#0A1E4A,#3A6FD8,#0D2A66,#9CC0FF,#0A1E4A)}")

lisa("tostuk", hero=hero_tostuk, pea="Bricolage Grotesque", keha="Manrope", theme="#F2C200", h1="Tartu autoremont Jaama tänaval.",
     teenused="kaardid", galerii="ruudustik", kaik="rida", pais="hele",
     vars=v(pea="'Bricolage Grotesque'", keha="'Manrope'", pea_ls="-0.035em", bg="#FFFFFF", fg="#1C1C1C", muted="#4D4D4A", surface="#F7F3DE", line="#E3DCB4",
            accent="#1C1C1C", accent_fg="#F2C200", dark="#1C1C1C", dark_fg="#FFFFFF", dark_accent="#F2C200", fookus="#B38F00", raadius="6px"),
     css=".pais-hele .logo-mark{width:10px;height:24px;background:repeating-linear-gradient(-45deg,#F2C200 0 4px,#1C1C1C 4px 8px);box-shadow:16px 0 0 #1C1C1C;margin-right:16px}")
lisa("olitilk", hero=hero_olitilk, pea="Syne", keha="Inter", theme="#17130E", h1="Õlivahetusest remondini.",
     teenused="read", galerii="mosaiik", kaik="kaardid", pais="must",
     vars=v(pea="'Syne'", keha="'Inter'", pea_ls="-0.035em", bg="#FDFAF4", fg="#17130E", muted="#57503F", surface="#F5ECD9", line="#E3D5B5",
            accent="#8A5208", accent_fg="#FFFFFF", dark="#17130E", dark_fg="#FFFFFF", dark_accent="#E8A93A", fookus="#8A5208", raadius="999px"),
     css=".pais-must{background:#17130E;color:#fff}.pais-must .logo-mark{width:16px;height:22px;background:#E8A93A;border-radius:50% 50% 50% 50%/60% 60% 40% 40%;clip-path:polygon(50% 0,100% 60%,90% 90%,50% 100%,10% 90%,0 60%)}")
lisa("hammasrattad", hero=hero_hammasrattad, pea="Space Grotesk", keha="Manrope", theme="#2B6CB0", h1="Nõmme autoremont aastast 1998.",
     teenused="numbrid", galerii="polaroid", kaik="ajajoon", pais="hele",
     vars=v(pea="'Space Grotesk'", keha="'Manrope'", pea_kaal="700", pea_ls="-0.035em", bg="#FFFFFF", fg="#10233D", muted="#475569", surface="#EEF3F8", line="#D2DDEA",
            accent="#2B6CB0", accent_fg="#FFFFFF", dark="#10233D", dark_fg="#FFFFFF", dark_accent="#90C2F5", fookus="#2B6CB0", raadius="8px"),
     css=".pais-hele .logo-mark{width:22px;height:22px;border-radius:50%;border:5px dotted #2B6CB0}")
lisa("noolemark", hero=hero_noolemark, pea="Unbounded", keha="Inter", theme="#B4141B", h1="Maardu autoteenindus.",
     teenused="plaadid", galerii="ruudustik", kaik="redel", pais="hele",
     vars=v(pea="'Unbounded'", keha="'Inter'", pea_kaal="900", pea_ls="-0.03em", bg="#FFFFFF", fg="#1A1A1A", muted="#4D4D4D", surface="#FBEBEC", line="#EFCFD1",
            accent="#B4141B", accent_fg="#FFFFFF", dark="#1A1A1A", dark_fg="#FFFFFF", dark_accent="#FF8A8F", fookus="#B4141B", raadius="2px"),
     css=".pais-hele .logo-mark{width:22px;height:22px;background:#B4141B;clip-path:polygon(0 0,60% 50%,0 100%,30% 100%,90% 50%,30% 0)}")
lisa("teeviit", hero=hero_teeviit, pea="Epilogue", keha="Inter", theme="#1A5BB8", h1="Väike-Maarja autoremont.",
     teenused="veerud", galerii="mosaiik", kaik="rida", pais="hele",
     vars=v(pea="'Epilogue'", keha="'Inter'", pea_ls="-0.035em", bg="#FFFFFF", fg="#122033", muted="#475467", surface="#EAF1FB", line="#CFDCEF",
            accent="#1A5BB8", accent_fg="#FFFFFF", dark="#122033", dark_fg="#FFFFFF", dark_accent="#9DC1F2", fookus="#1A5BB8", raadius="10px"),
     css=".pais-hele .logo-mark{width:22px;height:22px;border-radius:5px;background:#1A5BB8;box-shadow:inset 0 0 0 3px #fff,0 0 0 2px #1A5BB8}")
lisa("sara", hero=hero_sara, pea="Instrument Serif", keha="Manrope", theme="#0D0F13", h1="Auto nagu salongist.",
     teenused="read", galerii="riba", kaik="kaardid", pais="must",
     vars=v(pea="'Instrument Serif'", keha="'Manrope'", pea_kaal="400", pea_ls="-0.01em", bg="#FAFAFB", fg="#14161B", muted="#4E525C", surface="#EEEFF2", line="#D6D8DE",
            accent="#14161B", accent_fg="#FFFFFF", dark="#0D0F13", dark_fg="#FFFFFF", dark_accent="#D9DEE6", fookus="#14161B", raadius="999px"),
     css=".pais-must{background:#0D0F13;color:#fff}.pais-must .logo{font-style:italic}.pais-must .logo-mark{width:16px;height:16px;background:#fff;clip-path:polygon(50% 0,62% 38%,100% 50%,62% 62%,50% 100%,38% 62%,0 50%,38% 38%)}")
lisa("plekk", hero=hero_plekk, pea="Fraunces", keha="Inter", theme="#C2402E", h1="Mõlk sirgeks, värv peale.",
     teenused="plaadid", galerii="polaroid", kaik="rida", pais="hele",
     vars=v(pea="'Fraunces'", keha="'Inter'", pea_kaal="900", pea_ls="-0.02em", bg="#FFFFFF", fg="#2A1512", muted="#5B4A47", surface="#F9ECE9", line="#EDD3CE",
            accent="#A8361F", accent_fg="#FFFFFF", dark="#2A1512", dark_fg="#FFFFFF", dark_accent="#F2A08F", fookus="#A8361F", raadius="6px"),
     css=".pais-hele .logo-mark{width:26px;height:14px;border-radius:14px 14px 4px 4px;background:linear-gradient(#E9EDF2,#9BA5B1)}")
lisa("tellimus", hero=hero_tellimus, pea="Familjen Grotesk", keha="Inter", theme="#2F4858", h1="Autohooldus Tartu servas.",
     teenused="numbrid", galerii="ruudustik", kaik="ajajoon", pais="hele",
     vars=v(pea="'Familjen Grotesk'", keha="'Inter'", pea_kaal="700", pea_ls="-0.03em", bg="#FFFDF8", fg="#1E2E38", muted="#4C5961", surface="#F3EEE2", line="#DED6C4",
            accent="#2F4858", accent_fg="#FFFFFF", dark="#2F4858", dark_fg="#FFFFFF", dark_accent="#F2C57C", fookus="#2F4858", raadius="14px"),
     css=".pais-hele .logo-mark{width:24px;height:16px;border-radius:3px;background:#F3EEE2;border:2px solid #2F4858;border-right-style:dashed}")
lisa("voidutriibud", hero=hero_voidutriibud, pea="Unbounded", keha="Manrope", theme="#E1251B", h1="Remont, millega saab edasi sõita.",
     teenused="veerud", galerii="mosaiik", kaik="redel", pais="hele",
     vars=v(pea="'Unbounded'", keha="'Manrope'", pea_kaal="900", pea_ls="-0.04em", bg="#FFFFFF", fg="#111111", muted="#4D4D4D", surface="#F3F3F3", line="#DADADA",
            accent="#C81E16", accent_fg="#FFFFFF", dark="#111111", dark_fg="#FFFFFF", dark_accent="#FF6A62", fookus="#C81E16", raadius="0px"),
     css=".pais-hele .logo-mark{width:10px;height:22px;background:#E1251B;transform:skewX(-18deg);box-shadow:14px 0 0 #111;margin-right:14px}")
lisa("toosein", hero=hero_toosein, pea="Space Grotesk", keha="Familjen Grotesk", theme="#2E3A2F", h1="Valga autokoda.",
     teenused="kaardid", galerii="riba", kaik="kaardid", pais="hele",
     vars=v(pea="'Space Grotesk'", keha="'Familjen Grotesk'", pea_kaal="700", pea_ls="-0.04em", bg="#FFFDF8", fg="#1F271F", muted="#4E584D", surface="#F2EBDB", line="#DDD1B6",
            accent="#2E3A2F", accent_fg="#FFFFFF", dark="#2E3A2F", dark_fg="#FFFFFF", dark_accent="#F0A35E", fookus="#2E3A2F", raadius="4px"),
     css=".pais-hele .logo-mark{width:22px;height:22px;background:radial-gradient(#2E3A2F 2px,transparent 2.5px) 0 0/7px 7px,#E7D8B8;border-radius:3px}")
