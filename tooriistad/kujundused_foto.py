"""Fotoga avaplokid: ehitus, kaevetööd, haljastus ja koristus.

Fotod on public/fotod kaustas (Unsplash, vt ALLIKAD.txt). Igal avaplokil on väike silt "Näidisfoto",
et klient teaks, et päris lehel on tema enda pilt.
"""
from sisu import E
from kujundused import nupud, lead
from vahend import pal, baas, pais_css, mix

K = {}

FOTOD = {
    "ehitus": ["ehitus-karkass", "ehitus-remont", "ehitus-katus", "ehitus-fassaad", "ehitus-tellingud", "ehitus-betoon",
               "ehitus-pahtel", "ehitus-katus2", "ehitus-seinad", "ehitus-tuba"],
    "kaeve": ["kaeve-kraav", "kaeve-kopp", "kaeve-kopp2", "kaeve-udu"],
    "haljastus": ["haljastus-muru", "haljastus-aed", "haljastus-hoov", "haljastus-rohi"],
    "koristus": ["koristus-pudel", "koristus-tolm", "koristus-pesu"],
    "juuksur": ["juuksur-foon", "juuksur-salong", "juuksur-pesu", "juuksur-toolid", "juuksur-lokid"],
    "juuksur-m": ["juuksur-habe2", "juuksur-habe", "juuksur-salong", "juuksur-toolid"],
    "elekter": ["elekter-pistik", "elekter-moot", "elekter-pirnid", "elekter-kinnas", "elekter-liin"],
    "toru": ["toru-valamu", "toru-katlaruum", "toru-vannituba", "toru-kraan", "toru-valamu2", "toru-soojuspump"],
    "toru-kliima": ["toru-soojuspump", "toru-katlaruum", "toru-valamu"],
    "toru-ahi": ["ahi-kamin", "ahi-tuli"],
    "viimistlus": ["viim-rull", "ehitus-pahtel", "ehitus-remont"],
    "auto": ["auto-padrun", "auto-alt", "auto-mutrivoti", "auto-pidur"],
    "auto-rehv": ["auto-rehvid", "auto-pidur", "auto-padrun"],
    "auto-detail": ["auto-pesu", "auto-armatuur", "auto-padrun"],
}


def _sisu(a, d):
    return f'<h1 id="pk">{E(d["h1"])}</h1>{lead(a)}{nupud(a)}'


def _img(nimi, cls="", lazy=False):
    return (f'<img class="{cls}" src="/fotod/{nimi}.jpg" srcset="/fotod/{nimi}-800.jpg 800w, /fotod/{nimi}.jpg 1387w" '
            f'sizes="(max-width: 800px) 100vw, 60vw" width="1387" height="774" alt=""'
            f'{" loading=\"lazy\"" if lazy else ""} decoding="async">')


# Fotod, millel on näha konkreetne salong või töökoda või töötaja nägu. Neile käib silt "Näidisfoto",
# et lehe saaja ei arvaks, et talle esitletakse kellegi teise salongi või töötajat tema omana.
SILDIGA = {"juuksur-salong", "juuksur-toolid", "juuksur-foon", "juuksur-habe", "juuksur-habe2", "auto-alt",
           "toru-valamu", "ehitus-katus2", "koristus-tolm", "elekter-liin"}


def _silt(cls, *fotod):
    return f'<span class="{cls}-silt">Näidisfoto</span>' if SILDIGA.intersection(fotod) else ""


def _silt_css(cls, P, kus="right:16px;bottom:16px", mob=""):
    css = f".{cls}-silt{{position:absolute;{kus};z-index:2;font-size:12px;font-weight:600;letter-spacing:.04em;padding:4px 8px;border-radius:4px;color:#FFFFFF;background:#1A1A1A}}"
    if mob:
        css += f"@media (max-width:820px){{.{cls}-silt{{{mob}}}}}"
    return css


def _aasta(a):
    return f'<p class="aasta-rida">Tegutseme aastast {E(a["aasta"])} · {E(a["piirkond"])}</p>' if a.get("aasta") else ""


def hero_taust(a, d):
    """Foto üle kogu avaploki, vasakult tihe värvikiht teksti all."""
    P, f, c = d["p"], d["foto"], "h-ftaust"
    h = f"""<section class="{c}" aria-labelledby="pk">{_img(f, c + "-img")}<div class="{c}-kiht" aria-hidden="true"></div>
  <div class="wrap {c}-sisu">{_sisu(a, d)}{_aasta(a)}</div>{_silt(c, f)}
</section>"""
    css = baas(c, P, "120px 0 128px", "clamp(36px,5.6vw,84px)") + f""".{c}-img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.{c}-kiht{{position:absolute;inset:0;background:linear-gradient(90deg,{P['hb']} 0%,{P['hb']}F2 38%,{P['hb']}99 62%,{P['hb']}26 100%)}}
.{c}-sisu{{position:relative;z-index:1}}.{c}-sisu>*{{max-width:min(620px,60%)}}.{c} .aasta-rida{{color:{P['hl']};font-size:14px;margin:28px 0 0}}
@media (max-width:760px){{.{c}{{padding:0 0 72px}}.{c}-img{{position:relative;display:block;height:240px}}.{c}-kiht{{display:none}}.{c}-sisu{{padding-top:40px}}.{c}-sisu>*{{max-width:none}}}}{_silt_css(c, P, mob="top:204px;bottom:auto")}"""
    return h, css


def hero_pool(a, d):
    """Kaks poolt: tekst värvilisel paneelil, foto kõrval kogu kõrguses."""
    P, f, c = d["p"], d["foto"], "h-fpool"
    h = f"""<section class="{c}" aria-labelledby="pk">
  <div class="{c}-tekst"><div class="{c}-sisu">{_sisu(a, d)}{_aasta(a)}</div></div>
  <div class="{c}-foto">{_img(f)}{_silt(c, f)}</div>
</section>"""
    css = baas(c, P, "0", "clamp(34px,4.6vw,72px)") + f""".{c}{{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);min-height:560px}}
.{c}-tekst{{display:flex;align-items:center;padding:88px max(24px,calc((100vw - 1180px)/2 + 24px)) 96px}}.{c}-tekst .{c}-sisu{{padding-right:40px}}
.{c}-foto{{position:relative;min-height:320px}}.{c}-foto img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.{c} .aasta-rida{{color:{P['hl']};font-size:14px;margin:28px 0 0}}
@media (max-width:860px){{.{c}{{grid-template-columns:minmax(0,1fr)}}.{c}-foto{{order:-1;min-height:0;aspect-ratio:16/10}}.{c}-tekst{{padding:48px 20px 64px}}.{c}-tekst .{c}-sisu{{padding-right:0}}}}{_silt_css(c, P)}"""
    return h, css


def hero_kaart(a, d):
    """Suur foto, tekst tahke kaardi sees foto peal."""
    P, f, c = d["p"], d["foto"], "h-fkaart"
    h = f"""<section class="{c}" aria-labelledby="pk">
  <div class="{c}-foto">{_img(f)}{_silt(c, f)}</div>
  <div class="wrap {c}-wrap"><div class="{c}-kaart">{_sisu(a, d)}</div></div>
</section>"""
    css = baas(c, P, "0 0 72px", "clamp(32px,4.4vw,64px)") + f""".{c}{{background:{P['bg']}}}
.{c}-foto{{position:relative;height:clamp(300px,52vw,560px)}}.{c}-foto img{{width:100%;height:100%;object-fit:cover;display:block}}
.{c}-wrap{{position:relative;margin-top:-180px}}.{c}-kaart{{background:{P['hb']};color:{P['hf']};padding:48px 52px;max-width:680px;border-radius:var(--raadius);box-shadow:0 24px 60px rgba(0,0,0,.18)}}
@media (max-width:760px){{.{c}-wrap{{margin-top:-48px}}.{c}-kaart{{padding:32px 24px}}}}{_silt_css(c, P, "right:16px;top:16px")}"""
    return h, css


def hero_riba(a, d):
    """Lai fotoriba üleval, all suur pealkiri ja faktirida."""
    P, f, c = d["p"], d["foto"], "h-friba"
    fakt = "".join(f"<li><b>{E(x)}</b><span>{E(y)}</span></li>" for x, y in (
        (a.get("aasta") or "", "asutatud"), (a["piirkond"], "tööpiirkond"), (str(a["tootajaid"]) if a.get("tootajaid") else "", "töötajat")) if x)
    h = f"""<section class="{c}" aria-labelledby="pk">
  <div class="{c}-foto">{_img(f)}{_silt(c, f)}</div>
  <div class="wrap {c}-sisu"><div>{_sisu(a, d)}</div><ul class="{c}-faktid">{fakt}</ul></div>
</section>"""
    css = baas(c, P, "0 0 96px", "clamp(34px,5vw,76px)") + f""".{c}-foto{{position:relative;height:clamp(220px,34vw,380px)}}.{c}-foto img{{width:100%;height:100%;object-fit:cover;display:block}}
.{c}-sisu{{display:grid;grid-template-columns:minmax(0,1.6fr) minmax(0,1fr);gap:48px;padding-top:64px;align-items:end}}
.{c}-faktid{{list-style:none;margin:0;padding:0;display:grid;gap:18px;border-left:3px solid {P['ha']};padding-left:24px}}
.{c}-faktid b{{display:block;font-family:var(--pea);font-size:28px;line-height:1.1}}.{c}-faktid span{{color:{P['hl']};font-size:14px}}
@media (max-width:820px){{.{c}-sisu{{grid-template-columns:minmax(0,1fr);gap:32px;padding-top:40px}}}}{_silt_css(c, P)}"""
    return h, css


def hero_raam(a, d):
    """Foto paksus raamis, kergelt kaldu, taga aktsendiplokk."""
    P, f, c = d["p"], d["foto"], "h-fraam"
    h = f"""<section class="{c}" aria-labelledby="pk">
  <div class="wrap {c}-sisu"><div>{_sisu(a, d)}{_aasta(a)}</div>
  <div class="{c}-foto"><div class="{c}-plokk" aria-hidden="true"></div>{_img(f)}{_silt(c, f)}</div></div>
</section>"""
    css = baas(c, P, "96px 0 104px", "clamp(34px,5vw,76px)") + f""".{c}-sisu{{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:64px;align-items:center}}
.{c}-foto{{position:relative;transform:rotate(-2deg)}}.{c}-foto img{{position:relative;display:block;width:100%;height:auto;aspect-ratio:4/3;object-fit:cover;border:10px solid {P['hf']}}}
.{c}-plokk{{position:absolute;inset:24px -24px -24px 24px;background:{P['ha']}}}.{c} .aasta-rida{{color:{P['hl']};font-size:14px;margin:28px 0 0}}
@media (max-width:820px){{.{c}-sisu{{grid-template-columns:minmax(0,1fr);gap:48px}}.{c}-foto{{order:-1;margin-right:24px}}}}{_silt_css(c, P, "right:22px;bottom:22px")}"""
    return h, css


def hero_kaar(a, d):
    """Foto kaare kujul paremal."""
    P, f, c = d["p"], d["foto"], "h-fkaar"
    h = f"""<section class="{c}" aria-labelledby="pk">
  <div class="wrap {c}-sisu"><div>{_sisu(a, d)}{_aasta(a)}</div><div class="{c}-foto">{_img(f)}{_silt(c, f)}</div></div>
</section>"""
    css = baas(c, P, "88px 0 0", "clamp(34px,5vw,76px)") + f""".{c}-sisu{{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,1fr);gap:56px;align-items:end}}
.{c}-sisu>div:first-child{{padding-bottom:96px}}.{c}-foto{{position:relative;border-radius:999px 999px 0 0;overflow:hidden;aspect-ratio:4/5;max-height:560px}}
.{c}-foto img{{width:100%;height:100%;object-fit:cover;display:block}}.{c} .aasta-rida{{color:{P['hl']};font-size:14px;margin:28px 0 0}}
@media (max-width:820px){{.{c}-sisu{{grid-template-columns:minmax(0,1fr);gap:24px}}.{c}-foto{{order:-1;aspect-ratio:4/3;max-width:420px}}.{c}-sisu>div:first-child{{padding-bottom:72px}}}}{_silt_css(c, P)}"""
    return h, css


def hero_duo(a, d):
    """Mustvalge foto värvitooniga, tekst keskel."""
    P, f, c = d["p"], d["foto"], "h-fduo"
    h = f"""<section class="{c}" aria-labelledby="pk">{_img(f, c + "-img")}<div class="{c}-kiht" aria-hidden="true"></div>
  <div class="wrap {c}-sisu">{_sisu(a, d)}</div>{_silt(c, f)}
</section>"""
    css = baas(c, P, "136px 0 144px", "clamp(38px,6vw,92px)") + f""".{c}-img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:grayscale(1) contrast(1.1)}}
.{c}-kiht{{position:absolute;inset:0;background:{P['hb']};opacity:{'.86' if P['hf'] == '#FFFFFF' else '.8'}}}.{c}-sisu{{position:relative;z-index:1;text-align:center}}
.{c} h1{{max-width:13em;margin-left:auto;margin-right:auto}}.{c} .lead{{margin-left:auto;margin-right:auto}}.{c} .nupud{{justify-content:center}}
@media (max-width:760px){{.{c}{{padding:0 0 72px}}.{c}-img{{position:relative;display:block;height:240px;filter:none}}.{c}-kiht{{display:none}}.{c}-sisu{{padding-top:40px}}}}{_silt_css(c, P, mob="top:204px;bottom:auto")}"""
    return h, css


def hero_kolm(a, d):
    """Kolm fotot mosaiigina paremal."""
    P, c = d["p"], "h-fkolm"
    fotod = d["fotod3"]
    h = f"""<section class="{c}" aria-labelledby="pk">
  <div class="wrap {c}-sisu"><div>{_sisu(a, d)}{_aasta(a)}</div>
  <div class="{c}-mos">{_img(fotod[0], c + "-a")}{_img(fotod[1], c + "-b")}{_img(fotod[2], c + "-c")}{_silt(c, *fotod)}</div></div>
</section>"""
    css = baas(c, P, "88px 0 96px", "clamp(34px,4.8vw,72px)") + f""".{c}-sisu{{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.05fr);gap:56px;align-items:center}}
.{c}-mos{{position:relative;display:grid;grid-template-columns:1.3fr 1fr;grid-template-rows:1fr 1fr;gap:10px;height:440px}}
.{c}-mos img{{width:100%;height:100%;object-fit:cover;display:block;border-radius:var(--raadius)}}.{c}-a{{grid-row:1/3}}
.{c} .aasta-rida{{color:{P['hl']};font-size:14px;margin:28px 0 0}}
@media (max-width:860px){{.{c}-sisu{{grid-template-columns:minmax(0,1fr);gap:40px}}.{c}-mos{{order:-1;height:260px}}}}{_silt_css(c, P, "left:12px;bottom:12px")}"""
    return h, css


def hero_aasta(a, d):
    """Suur aastaarv ja foto diagonaaliga."""
    P, f, c = d["p"], d["foto"], "h-faasta"
    aasta = E(a.get("aasta") or "")
    h = f"""<section class="{c}" aria-labelledby="pk">
  <div class="{c}-foto">{_img(f)}{_silt(c, f)}</div>
  <div class="wrap {c}-sisu"><p class="{c}-arv" aria-hidden="true">{aasta}</p>{_sisu(a, d)}</div>
</section>"""
    css = baas(c, P, "104px 0 112px", "clamp(34px,4.8vw,72px)") + f""".{c}-foto{{position:absolute;top:0;right:0;bottom:0;width:46%;clip-path:polygon(22% 0,100% 0,100% 100%,0 100%)}}
.{c}-foto img{{width:100%;height:100%;object-fit:cover;display:block}}.{c}-sisu{{position:relative}}.{c}-sisu>*{{max-width:min(600px,52%)}}
.{c}-arv{{font-family:var(--pea);font-weight:800;font-size:clamp(64px,10vw,150px);line-height:.9;margin:0 0 12px;color:{P['ha']};letter-spacing:-.04em}}
@media (max-width:820px){{.{c}-foto{{position:relative;width:auto;height:240px;clip-path:none;margin:-104px 0 40px}}.{c}-sisu>*{{max-width:none}}}}{_silt_css(c, P)}"""
    return h, css


def hero_diag(a, d):
    """Foto taustaks, värviline paneel diagonaaliga üle vasaku poole."""
    P, f, c = d["p"], d["foto"], "h-fdiag"
    h = f"""<section class="{c}" aria-labelledby="pk">{_img(f, c + "-img")}<div class="{c}-paneel" aria-hidden="true"></div>
  <div class="wrap {c}-sisu">{_sisu(a, d)}{_aasta(a)}</div>{_silt(c, f)}
</section>"""
    css = baas(c, P, "112px 0 120px", "clamp(34px,5vw,76px)") + f""".{c}-img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.{c}-paneel{{position:absolute;inset:0;background:{P['hb']};clip-path:polygon(0 0,62% 0,48% 100%,0 100%)}}
.{c}-sisu{{position:relative;z-index:1}}.{c}-sisu>*{{max-width:min(560px,46%)}}.{c} .aasta-rida{{color:{P['hl']};font-size:14px;margin:28px 0 0}}
@media (max-width:820px){{.{c}{{padding:0 0 72px}}.{c}-img{{position:relative;display:block;height:240px}}.{c}-paneel{{display:none}}.{c}-sisu{{padding-top:40px}}.{c}-sisu>*{{max-width:none}}}}{_silt_css(c, P, mob="top:204px;bottom:auto")}"""
    return h, css


def hero_print(a, d):
    """Kaks fotot nagu prinditud pildid laual."""
    P, c = d["p"], "h-fprint"
    f1, f2 = d["fotod3"][0], d["fotod3"][1]
    h = f"""<section class="{c}" aria-labelledby="pk">
  <div class="wrap {c}-sisu"><div>{_sisu(a, d)}{_aasta(a)}</div>
  <div class="{c}-pildid"><figure class="{c}-1">{_img(f1)}</figure><figure class="{c}-2">{_img(f2)}</figure>{_silt(c, f1, f2)}</div></div>
</section>"""
    css = baas(c, P, "96px 0 104px", "clamp(34px,4.8vw,72px)") + f""".{c}-sisu{{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:56px;align-items:center}}
.{c}-pildid{{position:relative;height:420px}}.{c} figure{{position:absolute;margin:0;background:#FFFFFF;padding:10px 10px 36px;box-shadow:0 18px 40px rgba(0,0,0,.25);width:68%}}
.{c} figure img{{display:block;width:100%;height:auto;aspect-ratio:4/3;object-fit:cover}}.{c}-1{{left:0;top:0;transform:rotate(-5deg)}}.{c}-2{{right:0;bottom:0;transform:rotate(4deg)}}
.{c} .aasta-rida{{color:{P['hl']};font-size:14px;margin:28px 0 0}}
@media (max-width:860px){{.{c}-sisu{{grid-template-columns:minmax(0,1fr);gap:40px}}.{c}-pildid{{order:-1;height:280px}}}}{_silt_css(c, P, "left:8px;bottom:8px")}"""
    return h, css


def hero_ring(a, d):
    """Ümmargune foto aktsendirõngaga."""
    P, f, c = d["p"], d["foto"], "h-fring"
    h = f"""<section class="{c}" aria-labelledby="pk">
  <div class="wrap {c}-sisu"><div>{_sisu(a, d)}{_aasta(a)}</div><div class="{c}-foto">{_img(f)}{_silt(c, f)}</div></div>
</section>"""
    css = baas(c, P, "88px 0 96px", "clamp(34px,5vw,76px)") + f""".{c}-sisu{{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,1fr);gap:56px;align-items:center}}
.{c}-foto{{position:relative;aspect-ratio:1;max-width:440px;justify-self:end;width:100%}}
.{c}-foto img{{width:100%;height:100%;object-fit:cover;border-radius:50%;display:block;box-shadow:0 0 0 12px {P['hb']},0 0 0 20px {P['ha']}}}
.{c} .aasta-rida{{color:{P['hl']};font-size:14px;margin:28px 0 0}}
@media (max-width:820px){{.{c}-sisu{{grid-template-columns:minmax(0,1fr);gap:40px}}.{c}-foto{{order:-1;max-width:240px;justify-self:start;margin-left:20px}}}}{_silt_css(c, P, "right:0;bottom:8%")}"""
    return h, css


HEROD = dict(taust=hero_taust, pool=hero_pool, kaart=hero_kaart, riba=hero_riba, raam=hero_raam, kaar=hero_kaar, duo=hero_duo,
             kolm=hero_kolm, aasta=hero_aasta, diag=hero_diag, print=hero_print, ring=hero_ring)

FONDID = [("Archivo", "Inter", "900", "-0.035em"), ("Fraunces", "Manrope", "900", "-0.02em"), ("Bricolage Grotesque", "Inter", "800", "-0.035em"),
          ("Epilogue", "Manrope", "800", "-0.03em"), ("Familjen Grotesk", "Inter", "700", "-0.03em"), ("DM Serif Display", "Manrope", "400", "0"),
          ("Space Grotesk", "Manrope", "700", "-0.035em"), ("Inter Display", "Inter", "800", "-0.03em"), ("Instrument Serif", "Inter", "400", "-0.01em"),
          ("Archivo", "Manrope", "800", "-0.03em")]
TEEN = ["kaardid", "read", "veerud", "numbrid", "plaadid"]
GAL = ["riba", "ruudustik", "polaroid", "mosaiik"]
KAIK = ["redel", "rida", "kaardid", "ajajoon"]

# Värvid kategooriate kaupa: (aktsent, avaploki aktsent tumedal, tekst/tume)
VARVID = {
    "ehitus": [("#B45309", "#FBBF24", "#1C1917"), ("#1D4ED8", "#FACC15", "#0F172A"), ("#9A3412", "#FDBA74", "#1F1A17"), ("#0F766E", "#FDE047", "#0F1F1C"),
               ("#B91C1C", "#FCA5A5", "#1B1B1F"), ("#4338CA", "#FCD34D", "#111827"), ("#A16207", "#FDE68A", "#1A1A1A"), ("#15803D", "#FACC15", "#14201A")],
    "kaeve": [("#B45309", "#FACC15", "#1A1712"), ("#A16207", "#FDE047", "#18181B"), ("#C2410C", "#FDBA74", "#1C1917"), ("#854D0E", "#FCD34D", "#1F1A14")],
    "haljastus": [("#15803D", "#BEF264", "#14201A"), ("#166534", "#FDE68A", "#13241B"), ("#4D7C0F", "#D9F99D", "#1A2312"), ("#0F766E", "#A7F3D0", "#0F1F1C")],
    "juuksur": [("#9D174D", "#F9A8D4", "#1F1420"), ("#7C3AED", "#C4B5FD", "#1E1B2E"), ("#B45309", "#FCD34D", "#1C1917"), ("#0F766E", "#99F6E4", "#0F1F1C")],
    "elekter": [("#1D4ED8", "#FACC15", "#0F172A"), ("#B45309", "#FDE047", "#1C1917"), ("#0F766E", "#FDE047", "#0F1F1C"), ("#4338CA", "#FCD34D", "#111827")],
    "toru": [("#0369A1", "#7DD3FC", "#0C1A2B"), ("#B91C1C", "#FCA5A5", "#1B1B1F"), ("#0E7490", "#A5F3FC", "#0B1F2A"), ("#C2410C", "#FDBA74", "#1C1917")],
    "viimistlus": [("#1D4ED8", "#FDE047", "#14213D"), ("#B4531F", "#FDBA74", "#2A1B12"), ("#0F766E", "#5EEAD4", "#0F1F1C"), ("#86198F", "#F0ABFC", "#2A1E2E")],
    "auto": [("#B91C1C", "#FCA5A5", "#18181B"), ("#1D4ED8", "#FACC15", "#0F172A"), ("#C2410C", "#FDBA74", "#1C1917"), ("#0F766E", "#5EEAD4", "#0F1F1C"),
             ("#4338CA", "#FCD34D", "#111827"), ("#A16207", "#FDE68A", "#1A1A1A")],
    "koristus": [("#0369A1", "#7DD3FC", "#0C1A2B"), ("#0E7490", "#A5F3FC", "#0B1F2A"), ("#7C3AED", "#C4B5FD", "#1E1B2E"), ("#BE185D", "#F9A8D4", "#1F1420")],
}


def lisa(nimi, kat, hero, h1, i):
    """Loob kujunduse: värvid, font ja fotod tulevad järjekorranumbrist, nii et naabrid ei sarnane."""
    akt, ha, tume = VARVID[kat.split("-")[0]][(i * 3) % len(VARVID[kat.split("-")[0]])]
    tyyp = ["tume", "hele", "varv", "tume", "hele"][i % 5]
    if tyyp == "hele":
        hb, hf, haa = mix(akt, "#FFFFFF", .08), tume, akt
    elif tyyp == "tume":
        hb, hf, haa = tume, "#FFFFFF", ha
    else:
        hb, hf, haa = mix(akt, "#000000", .55), "#FFFFFF", ha
    pea, keha, kaal, ls = FONDID[(i * 3 + 2) % len(FONDID)]
    raadius = ["6px", "2px", "12px", "8px", "0px", "16px"][(i * 5) % 6]
    P = pal("#FFFFFF", tume, akt, mix(tume, "#000000", .9), ha, hb, hf, haa, raadius, pea=f"'{pea}'", keha=f"'{keha}'", pea_kaal=kaal, pea_ls=ls)
    f = FOTOD[kat]
    K[nimi] = dict(hero=HEROD[hero], h1=h1, p=P, pea=pea, keha=keha, theme=P["hb"], teenused=TEEN[(i + 1) % 5], galerii=GAL[(i * 3 + 2) % 4],
                   kaik=KAIK[(i // 2 + 2) % 4], pais=["hele", "tume", "varv"][(i * 2) % 3], vars=P["vars"],
                   css=pais_css(["hele", "tume", "varv"][(i * 2) % 3], P, i + 1),
                   foto=f[i % len(f)], fotod3=[f[(i + k) % len(f)] for k in range(3)])



# (võti, kategooria, avaplokk, pealkiri, järjekorranumber)
FOTOLEHED = [
[
"f-azelta-projekt",
"ehitus",
"taust",
"Ehitus ja renoveerimine Tallinnas.",
0
],
[
"f-visare-ehitus",
"ehitus",
"kolm",
"Maja ehitus Järvamaal.",
1
],
[
"f-prisv-ehitus",
"ehitus",
"kaart",
"Ehitustööd Pärnus.",
2
],
[
"f-anle-ehitus",
"ehitus",
"diag",
"Uus maja või remont Tallinnas.",
3
],
[
"f-norges-hus-nova",
"ehitus",
"raam",
"Norges Hus Nova. Ehitus Harjumaal.",
4
],
[
"f-ganter-trade",
"ehitus",
"ring",
"Ehitame Võrus.",
5
],
[
"f-bariot-group",
"ehitus",
"duo",
"Katus, fassaad ja remont Tallinnas.",
6
],
[
"f-steba-building",
"ehitus",
"pool",
"Ehitus ja renoveerimine Rakveres.",
7
],
[
"f-maev-grupp",
"ehitus",
"aasta",
"Maja ehitus Tartus.",
8
],
[
"f-lestnev",
"ehitus",
"riba",
"Ehitustööd Harjumaal.",
9
],
[
"f-betonrak",
"ehitus",
"print",
"Uus maja või remont Tallinnas.",
10
],
[
"f-kk-grupp",
"ehitus",
"kaar",
"KK Grupp. Ehitus Rakveres.",
11
],
[
"f-ritori",
"ehitus",
"taust",
"Ehitame Tallinnas.",
12
],
[
"f-bergland-ehitus",
"ehitus",
"kolm",
"Katus, fassaad ja remont Tallinnas.",
13
],
[
"f-mpa-ehitus",
"ehitus",
"kaart",
"Ehitus ja renoveerimine Lääne-Virumaal.",
14
],
[
"f-timtar-grupp",
"ehitus",
"diag",
"Maja ehitus Lääne-Virumaal.",
15
],
[
"f-qvant-grupp",
"ehitus",
"raam",
"Ehitustööd Tartumaal.",
16
],
[
"f-teric-grupp",
"ehitus",
"ring",
"Uus maja või remont Ida-Virumaal.",
17
],
[
"f-hrhooned",
"ehitus",
"duo",
"HRHooned. Ehitus Hiiumaal.",
18
],
[
"f-bpanel",
"ehitus",
"pool",
"Ehitame Harjumaal.",
19
],
[
"f-marilander",
"ehitus",
"aasta",
"Katus, fassaad ja remont Võrumaal.",
20
],
[
"f-baum",
"ehitus",
"riba",
"Ehitus ja renoveerimine Pärnumaal.",
21
],
[
"f-masterbest-baltic",
"ehitus",
"print",
"Maja ehitus Tallinnas.",
22
],
[
"f-renkolm",
"ehitus",
"kaar",
"Ehitustööd Pärnumaal.",
23
],
[
"f-neval",
"ehitus",
"taust",
"Uus maja või remont Tallinnas.",
24
],
[
"f-kilaja",
"ehitus",
"kolm",
"Kilaja. Ehitus Põlvas.",
25
],
[
"f-mihest",
"ehitus",
"kaart",
"Ehitame Tartus.",
26
],
[
"f-praim-ehitus",
"ehitus",
"diag",
"Katus, fassaad ja remont Narvas.",
27
],
[
"f-innover-ehitus",
"ehitus",
"raam",
"Ehitus ja renoveerimine Tartumaal.",
28
],
[
"f-kenomer",
"ehitus",
"ring",
"Maja ehitus Harjumaal.",
29
],
[
"f-algera-infra",
"ehitus",
"duo",
"Ehitustööd Tallinnas.",
30
],
[
"f-k-k-disain",
"ehitus",
"pool",
"Uus maja või remont Võrumaal.",
31
],
[
"f-venles",
"ehitus",
"aasta",
"Venles. Ehitus Tallinnas.",
32
],
[
"f-kt-maja",
"ehitus",
"riba",
"Ehitame Pärnus.",
33
],
[
"f-baumix",
"ehitus",
"print",
"Katus, fassaad ja remont Tallinnas.",
34
],
[
"f-riivas",
"ehitus",
"kaar",
"Ehitus ja renoveerimine Narvas.",
35
],
[
"f-chihez",
"ehitus",
"taust",
"Maja ehitus Tartus.",
36
],
[
"f-aqr-trust",
"ehitus",
"kolm",
"Ehitustööd Jõgevamaal.",
37
],
[
"f-balthaus-ehitus",
"ehitus",
"kaart",
"Uus maja või remont Tallinnas.",
38
],
[
"f-danvik-ari",
"ehitus",
"diag",
"Danvik Äri. Ehitus Harjumaal.",
39
],
[
"f-oja-ehitus",
"ehitus",
"raam",
"Ehitame Valgamaal.",
40
],
[
"f-kauber-ehitus",
"ehitus",
"ring",
"Katus, fassaad ja remont Tartus.",
41
],
[
"f-mkm-teenused",
"ehitus",
"duo",
"Ehitus ja renoveerimine Tallinnas.",
42
],
[
"f-at-sim",
"ehitus",
"pool",
"Maja ehitus Saaremaal.",
43
],
[
"f-raudcom",
"ehitus",
"aasta",
"Ehitustööd Viljandimaal.",
44
],
[
"f-rr-ehitus",
"ehitus",
"riba",
"Uus maja või remont Pärnus.",
45
],
[
"f-conum",
"ehitus",
"print",
"Conum. Ehitus Harjumaal.",
46
],
[
"f-brovar-ehitus",
"ehitus",
"kaar",
"Ehitame Tartus.",
47
],
[
"f-ezze",
"ehitus",
"taust",
"Katus, fassaad ja remont Valgamaal.",
48
],
[
"f-mt-maja",
"ehitus",
"kolm",
"Ehitus ja renoveerimine Viljandimaal.",
49
],
[
"f-heliantex",
"ehitus",
"kaart",
"Maja ehitus Tallinnas.",
50
],
[
"f-sanna",
"ehitus",
"diag",
"Ehitustööd Tallinnas.",
51
],
[
"f-istrup",
"ehitus",
"raam",
"Uus maja või remont Rakveres.",
52
],
[
"f-th-building-service",
"ehitus",
"ring",
"TH Building service. Ehitus Tartumaal.",
53
],
[
"f-revalest-ehitus",
"ehitus",
"duo",
"Ehitame Harjumaal.",
54
],
[
"f-maveco-building",
"ehitus",
"pool",
"Katus, fassaad ja remont Pärnus.",
55
],
[
"f-nives-grupp",
"ehitus",
"aasta",
"Ehitus ja renoveerimine Tartumaal.",
56
],
[
"f-valdimberg",
"ehitus",
"riba",
"Maja ehitus Harjumaal.",
57
],
[
"f-karell-ehitus",
"ehitus",
"print",
"Ehitustööd Tallinnas.",
58
],
[
"f-dn-nord-betoon",
"ehitus",
"kaar",
"Uus maja või remont Valgas.",
59
],
[
"f-fenira-group",
"ehitus",
"taust",
"Fenira Group. Ehitus Pärnus.",
60
],
[
"f-samareks",
"ehitus",
"kolm",
"Ehitame Läänemaal.",
61
],
[
"f-likman-grupp",
"ehitus",
"kaart",
"Katus, fassaad ja remont Kohtla-Järvel.",
62
],
[
"f-dma-betoonitood",
"ehitus",
"diag",
"Ehitus ja renoveerimine Tallinnas.",
63
],
[
"f-pako-grupp",
"ehitus",
"raam",
"Maja ehitus Raplamaal.",
64
],
[
"f-betoonimeistri-grupp",
"ehitus",
"ring",
"Ehitustööd Tallinnas.",
65
],
[
"f-fast-group-baltic",
"ehitus",
"duo",
"Uus maja või remont Tartus.",
66
],
[
"f-saunatex",
"ehitus",
"pool",
"Saunatex. Ehitus Pärnus.",
67
],
[
"f-kemp-grupp",
"ehitus",
"aasta",
"Ehitame Harjumaal.",
68
],
[
"f-ecoclas",
"ehitus",
"riba",
"Katus, fassaad ja remont Võrus.",
69
],
[
"f-tarkleon",
"ehitus",
"print",
"Ehitus ja renoveerimine Sindis.",
70
],
[
"f-arteego-ehitus",
"ehitus",
"kaar",
"Maja ehitus Tallinnas.",
71
],
[
"f-terramont-ehitus",
"ehitus",
"taust",
"Ehitustööd Tallinnas.",
72
],
[
"f-everan-houses",
"ehitus",
"kolm",
"Uus maja või remont Läänemaal.",
73
],
[
"f-luts-teenus",
"ehitus",
"kaart",
"Luts Teenus. Ehitus Võrumaal.",
74
],
[
"f-fourwalls-ehitus",
"ehitus",
"diag",
"Ehitame Tallinnas.",
75
],
[
"f-stenco-grupp",
"ehitus",
"raam",
"Katus, fassaad ja remont Harjumaal.",
76
],
[
"f-kevadvihm",
"ehitus",
"ring",
"Ehitus ja renoveerimine Tallinnas.",
77
],
[
"f-piksmar",
"ehitus",
"duo",
"Maja ehitus Viljandimaal.",
78
],
[
"f-rekmar-ehitused",
"ehitus",
"pool",
"Ehitustööd Järvamaal.",
79
],
[
"f-elmon",
"ehitus",
"aasta",
"Uus maja või remont Tallinnas.",
80
],
[
"f-vekoolis",
"ehitus",
"riba",
"Vekoolis. Ehitus Kohtla-Järvel.",
81
],
[
"f-oleksen",
"ehitus",
"print",
"Ehitame Kohtla-Järvel.",
82
],
[
"f-lkp-grupp",
"ehitus",
"kaar",
"Katus, fassaad ja remont Võrus.",
83
],
[
"f-semehitus-company",
"ehitus",
"taust",
"Ehitus ja renoveerimine Tallinnas.",
84
],
[
"f-johanna-grupp",
"ehitus",
"kolm",
"Maja ehitus Rakveres.",
85
],
[
"f-mar-building",
"ehitus",
"kaart",
"Ehitustööd Tallinnas.",
86
],
[
"f-valge-torn",
"ehitus",
"diag",
"Uus maja või remont Tallinnas.",
87
],
[
"f-estorek",
"ehitus",
"raam",
"Estorek. Ehitus Lääne-Virumaal.",
88
],
[
"f-ecowash-building",
"ehitus",
"ring",
"Ehitame Tallinnas.",
89
],
[
"f-mk-neli",
"ehitus",
"duo",
"Katus, fassaad ja remont Tallinnas.",
90
],
[
"f-grendaria-bygg",
"ehitus",
"pool",
"Ehitus ja renoveerimine Tallinnas.",
91
],
[
"f-sultek",
"ehitus",
"aasta",
"Maja ehitus Pärnus.",
92
],
[
"f-vex-ehitus",
"ehitus",
"riba",
"Ehitustööd Narvas.",
93
],
[
"f-danata",
"ehitus",
"print",
"Uus maja või remont Jõgevamaal.",
94
],
[
"f-aestico-ehitus",
"ehitus",
"kaar",
"Aestico Ehitus. Ehitus Tallinnas.",
95
],
[
"f-rtkfassaad",
"ehitus",
"taust",
"Ehitame Tallinnas.",
96
],
[
"f-majakratt",
"ehitus",
"kolm",
"Katus, fassaad ja remont Võrumaal.",
97
],
[
"f-servo-grupp",
"ehitus",
"kaart",
"Ehitus ja renoveerimine Lääne-Virumaal.",
98
],
[
"f-pelna",
"ehitus",
"diag",
"Maja ehitus Tallinnas.",
99
],
[
"f-selgran-ehitus",
"ehitus",
"raam",
"Ehitustööd Võrus.",
100
],
[
"f-mk-maroon",
"ehitus",
"ring",
"Uus maja või remont Harjumaal.",
101
],
[
"f-sv-bau",
"ehitus",
"duo",
"SV Bau. Ehitus Tallinnas.",
102
],
[
"f-laskko-expert",
"ehitus",
"pool",
"Ehitame Maardus.",
103
],
[
"f-titol-forest",
"haljastus",
"aasta",
"Haljastus Ida-Virumaal.",
104
],
[
"f-salirland",
"haljastus",
"riba",
"Aiatööd Tallinnas.",
105
],
[
"f-gulib",
"haljastus",
"print",
"Korras aed Narva-Jõesuus.",
106
],
[
"f-segenso",
"haljastus",
"kaar",
"Segenso. Haljastus Tartumaal.",
107
],
[
"f-davkai-grupp",
"haljastus",
"taust",
"Muru ja hekid Kohtla-Järvel.",
108
],
[
"f-vilson-trade",
"haljastus",
"kolm",
"Haljastus Viljandimaal.",
109
],
[
"f-metsur-grupp",
"haljastus",
"kaart",
"Aiatööd Harjumaal.",
110
],
[
"f-amsten-grupp",
"haljastus",
"diag",
"Korras aed Narva-Jõesuus.",
111
],
[
"f-lounalaaned",
"haljastus",
"raam",
"Lõunalaaned. Haljastus Tartus.",
112
],
[
"f-kalrem",
"haljastus",
"ring",
"Muru ja hekid Tallinnas.",
113
],
[
"f-treulop",
"haljastus",
"duo",
"Haljastus Tallinnas.",
114
],
[
"f-tormolen",
"haljastus",
"pool",
"Aiatööd Tartus.",
115
],
[
"f-ida-eesti-teehoolduse",
"haljastus",
"aasta",
"Korras aed Ida-Virumaal.",
116
],
[
"f-lei",
"haljastus",
"riba",
"LEI. Haljastus Lääne-Virumaal.",
117
],
[
"f-voidust-grupp",
"haljastus",
"print",
"Muru ja hekid Viljandimaal.",
118
],
[
"f-kiki-maastikukujundus",
"haljastus",
"kaar",
"Haljastus Lääne-Virumaal.",
119
],
[
"f-puuhooldustood",
"haljastus",
"taust",
"Aiatööd Tallinnas.",
120
],
[
"f-valge-janes",
"haljastus",
"kolm",
"Korras aed Harjumaal.",
121
],
[
"f-artesti",
"haljastus",
"kaart",
"Artesti. Haljastus Narva-Jõesuus.",
122
],
[
"f-raicat",
"haljastus",
"diag",
"Muru ja hekid Viljandis.",
123
],
[
"f-muuri-talu",
"haljastus",
"raam",
"Haljastus Põlvamaal.",
124
],
[
"f-fiume-trade",
"haljastus",
"ring",
"Aiatööd Raplamaal.",
125
],
[
"f-jogedearu",
"haljastus",
"duo",
"Korras aed Lääne-Virumaal.",
126
],
[
"f-ahm",
"haljastus",
"pool",
"AHM. Haljastus Harjumaal.",
127
],
[
"f-workest-group",
"haljastus",
"aasta",
"Muru ja hekid Tartus.",
128
],
[
"f-arotaga",
"haljastus",
"riba",
"Haljastus Harjumaal.",
129
],
[
"f-moisalill",
"haljastus",
"print",
"Aiatööd Ida-Virumaal.",
130
],
[
"f-tafirent",
"haljastus",
"kaar",
"Korras aed Järvamaal.",
131
],
[
"f-dvsleon",
"haljastus",
"taust",
"Dvsleon. Haljastus Tallinnas.",
132
],
[
"f-renmar-puit",
"haljastus",
"kolm",
"Muru ja hekid Põlvamaal.",
133
],
[
"f-eksora-sv",
"kaeve",
"kaart",
"Kaevetööd Ida-Virumaal.",
134
],
[
"f-wakerman-grupp",
"kaeve",
"diag",
"Pinnasetööd Pärnus.",
135
],
[
"f-heimak",
"kaeve",
"raam",
"Heimak. Kaevetööd Raplamaal.",
136
],
[
"f-finkre-tehnika",
"kaeve",
"ring",
"Kaeve- ja pinnasetööd Viljandimaal.",
137
],
[
"f-koriku-puit",
"kaeve",
"duo",
"Süvendid ja trassid Hiiumaal.",
138
],
[
"f-sosun-e",
"kaeve",
"pool",
"Kaevetööd Tallinnas.",
139
],
[
"f-upa-building",
"kaeve",
"aasta",
"Pinnasetööd Harjumaal.",
140
],
[
"f-pkg-grupp",
"kaeve",
"riba",
"PKG Grupp. Kaevetööd Järvamaal.",
141
],
[
"f-gruntekspert",
"kaeve",
"print",
"Kaeve- ja pinnasetööd Harjumaal.",
142
],
[
"f-buldooser-ehitusmasinad",
"kaeve",
"kaar",
"Süvendid ja trassid Raplamaal.",
143
],
[
"f-tehmaster-group",
"kaeve",
"taust",
"Kaevetööd Tallinnas.",
144
],
[
"f-laxnel",
"kaeve",
"kolm",
"Pinnasetööd Raplamaal.",
145
],
[
"f-lpn-grupp",
"kaeve",
"kaart",
"LPN Grupp. Kaevetööd Pärnumaal.",
146
],
[
"f-hades-grupp",
"kaeve",
"diag",
"Kaeve- ja pinnasetööd Raplamaal.",
147
],
[
"f-reco-infra",
"kaeve",
"raam",
"Süvendid ja trassid Raplamaal.",
148
],
[
"f-tego-remont",
"kaeve",
"ring",
"Kaevetööd Narva-Jõesuus.",
149
],
[
"f-lex-gold-est",
"kaeve",
"duo",
"Pinnasetööd Ida-Virumaal.",
150
],
[
"f-kaleva-puidutoostus",
"kaeve",
"pool",
"Kaleva Puidutööstus. Kaevetööd Harjumaal.",
151
],
[
"f-janeri-puit",
"kaeve",
"aasta",
"Kaeve- ja pinnasetööd Tallinnas.",
152
],
[
"f-rar-teed",
"kaeve",
"riba",
"Süvendid ja trassid Pärnumaal.",
153
],
[
"f-vaiterel",
"kaeve",
"print",
"Kaevetööd Tartumaal.",
154
],
[
"f-miilante",
"kaeve",
"kaar",
"Pinnasetööd Lääne-Virumaal.",
155
],
[
"f-lone-v-v",
"kaeve",
"taust",
"LONE V.V.. Kaevetööd Tartus.",
156
],
[
"f-jonx",
"kaeve",
"kolm",
"Kaeve- ja pinnasetööd Võrumaal.",
157
],
[
"f-kivitammi-mk",
"kaeve",
"kaart",
"Süvendid ja trassid Harjumaal.",
158
],
[
"f-committed",
"kaeve",
"diag",
"Kaevetööd Järvamaal.",
159
],
[
"f-almon-grupp",
"kaeve",
"raam",
"Pinnasetööd Tallinnas.",
160
],
[
"f-ak-gramen",
"kaeve",
"ring",
"AK Gramen. Kaevetööd Harjumaal.",
161
],
[
"f-kangru-karjaar",
"kaeve",
"duo",
"Kaeve- ja pinnasetööd Tartus.",
162
],
[
"f-jl-kaevetood",
"kaeve",
"pool",
"Süvendid ja trassid Tallinnas.",
163
],
[
"f-mj-aiavalgustid",
"kaeve",
"aasta",
"Kaevetööd Harjumaal.",
164
],
[
"f-madis-jaetma",
"kaeve",
"riba",
"Pinnasetööd Harjumaal.",
165
],
[
"f-cp-teenused",
"kaeve",
"print",
"CP Teenused. Kaevetööd Valgamaal.",
166
],
[
"f-poide-tehnika",
"kaeve",
"kaar",
"Kaeve- ja pinnasetööd Saaremaal.",
167
],
[
"f-vasalemma-rallypark",
"kaeve",
"taust",
"Süvendid ja trassid Harjumaal.",
168
],
[
"f-kopaonud",
"kaeve",
"kolm",
"Kaevetööd Võrus.",
169
],
[
"f-allthings",
"kaeve",
"kaart",
"Pinnasetööd Pärnus.",
170
],
[
"f-golden-grupp",
"kaeve",
"diag",
"Golden Grupp. Kaevetööd Viljandimaal.",
171
],
[
"f-maustt",
"kaeve",
"raam",
"Kaeve- ja pinnasetööd Tartus.",
172
],
[
"f-trekas",
"kaeve",
"ring",
"Süvendid ja trassid Raplamaal.",
173
],
[
"f-durorent",
"ehitus",
"duo",
"Katus, fassaad ja remont Tartus.",
174
],
[
"f-domira-ehitus",
"ehitus",
"pool",
"Ehitus ja renoveerimine Tartumaal.",
175
],
[
"f-probfee-solutions",
"ehitus",
"aasta",
"Maja ehitus Lääne-Virumaal.",
176
],
[
"f-nordskat-grupp",
"ehitus",
"riba",
"Ehitustööd Tallinnas.",
177
],
[
"f-interno-ehitus",
"ehitus",
"print",
"Uus maja või remont Lääne-Virumaal.",
178
],
[
"f-d-r-byggmestari",
"ehitus",
"kaar",
"D.R. Byggmestari. Ehitus Pärnus.",
179
],
[
"f-imbrex-ehitus",
"ehitus",
"taust",
"Ehitame Tallinnas.",
180
],
[
"f-eleron-ehitus",
"ehitus",
"kolm",
"Katus, fassaad ja remont Järvamaal.",
181
],
[
"f-amalvi",
"ehitus",
"kaart",
"Ehitus ja renoveerimine Rakveres.",
182
],
[
"f-soliidne-kodu",
"ehitus",
"diag",
"Maja ehitus Tartus.",
183
],
[
"f-renotek-building",
"ehitus",
"raam",
"Ehitustööd Viljandimaal.",
184
],
[
"f-fayz-ehitus",
"ehitus",
"ring",
"Uus maja või remont Harjumaal.",
185
],
[
"f-elehitus",
"ehitus",
"duo",
"Elehitus. Ehitus Harjumaal.",
186
],
[
"f-seinest-grupp",
"ehitus",
"pool",
"Ehitame Harjumaal.",
187
],
[
"f-inkku",
"ehitus",
"aasta",
"Katus, fassaad ja remont Võrumaal.",
188
],
[
"f-haamer-ip",
"ehitus",
"riba",
"Ehitus ja renoveerimine Pärnus.",
189
],
[
"f-verol-grupp",
"ehitus",
"print",
"Maja ehitus Raplamaal.",
190
],
[
"f-tettu",
"ehitus",
"kaar",
"Ehitustööd Põlvas.",
191
],
[
"f-importehitus",
"ehitus",
"taust",
"Uus maja või remont Pärnus.",
192
],
[
"f-serden-ehitus",
"ehitus",
"kolm",
"Serden Ehitus. Ehitus Tallinnas.",
193
],
[
"f-rajave",
"ehitus",
"kaart",
"Ehitame Raplamaal.",
194
],
[
"f-tippkvaliteet-construction",
"ehitus",
"diag",
"Katus, fassaad ja remont Tartus.",
195
],
[
"f-alpri-ehitus",
"ehitus",
"raam",
"Ehitus ja renoveerimine Järvamaal.",
196
],
[
"f-atrox",
"ehitus",
"ring",
"Maja ehitus Tallinnas.",
197
],
[
"f-hpc-projektid",
"ehitus",
"duo",
"Ehitustööd Pärnus.",
198
],
[
"f-ehituse-ateljee",
"ehitus",
"pool",
"Uus maja või remont Tallinnas.",
199
],
[
"f-betrec",
"ehitus",
"aasta",
"BetRec. Ehitus Narvas.",
200
],
[
"f-balmer",
"ehitus",
"riba",
"Ehitame Põlvamaal.",
201
],
[
"f-s-t-i-grupp",
"ehitus",
"print",
"Katus, fassaad ja remont Jõgevamaal.",
202
],
[
"f-mereva",
"ehitus",
"kaar",
"Ehitus ja renoveerimine Saaremaal.",
203
],
[
"f-m-event",
"koristus",
"taust",
"Koristus Harjumaal.",
204
],
[
"f-cleaningaid-haldus",
"koristus",
"kolm",
"Puhas kodu ja kontor Tallinnas.",
205
],
[
"f-puhtad-lahendused",
"koristus",
"kaart",
"Koristusteenus Tartus.",
206
],
[
"f-sanctumere",
"koristus",
"diag",
"Sanctumere. Koristus Tallinnas.",
207
],
[
"f-anhel-puhastusteenused",
"koristus",
"raam",
"Kodu- ja kontorikoristus Tallinnas.",
208
],
[
"f-stsi-teeninduse",
"koristus",
"ring",
"Koristus Tallinnas.",
209
],
[
"f-edanella",
"koristus",
"duo",
"Puhas kodu ja kontor Maardus.",
210
],
[
"f-j-c-kapad",
"koristus",
"pool",
"Koristusteenus Põlvamaal.",
211
],
[
"f-vronas",
"koristus",
"aasta",
"Vronas. Koristus Tallinnas.",
212
],
[
"f-ari-puhastus",
"koristus",
"riba",
"Kodu- ja kontorikoristus Tallinnas.",
213
],
[
"f-getrix-vat",
"koristus",
"print",
"Koristus Tartus.",
214
],
[
"f-chene",
"koristus",
"kaar",
"Puhas kodu ja kontor Pärnumaal.",
215
],
[
"f-help-cleaning-team",
"koristus",
"taust",
"Koristusteenus Tallinnas.",
216
],
[
"f-jancom-puhastus",
"koristus",
"kolm",
"Jancom Puhastus. Koristus Tallinnas.",
217
],
[
"f-viru-partnerid",
"koristus",
"kaart",
"Kodu- ja kontorikoristus Rakveres.",
218
],
[
"f-bestclean-puhastusteenistus",
"koristus",
"diag",
"Koristus Harjumaal.",
219
],
[
"f-vts-pauls",
"koristus",
"raam",
"Puhas kodu ja kontor Harjumaal.",
220
],
[
"f-neleliis-haldusteenused",
"koristus",
"ring",
"Koristusteenus Tartumaal.",
221
],
[
"f-purehouse-service",
"koristus",
"duo",
"PureHouse Service. Koristus Tallinnas.",
222
],
[
"f-fem-puhastusteenus",
"koristus",
"pool",
"Kodu- ja kontorikoristus Tartus.",
223
],
[
"f-mrk-rakennus",
"ehitus",
"aasta",
"Maja ehitus Võrus.",
224
],
[
"f-esplest",
"ehitus",
"riba",
"Ehitustööd Lääne-Virumaal.",
225
],
[
"f-makero-install",
"ehitus",
"print",
"Uus maja või remont Harjumaal.",
226
],
[
"f-ekset-veod",
"ehitus",
"kaar",
"Ekset Veod. Ehitus Võrumaal.",
227
],
[
"f-landekspress",
"ehitus",
"taust",
"Ehitame Tallinnas.",
228
],
[
"f-ehitus-ja-paigaldus",
"ehitus",
"kolm",
"Katus, fassaad ja remont Võrumaal.",
229
],
[
"f-bluest-building",
"ehitus",
"kaart",
"Ehitus ja renoveerimine Haapsalus.",
230
],
[
"f-deu-nehitus",
"ehitus",
"diag",
"Maja ehitus Võrumaal.",
231
],
[
"f-lovikapa",
"ehitus",
"raam",
"Ehitustööd Pärnus.",
232
],
[
"f-e-elta-trans",
"ehitus",
"ring",
"Uus maja või remont Lääne-Virumaal.",
233
],
[
"f-dmv-ehitus",
"ehitus",
"duo",
"DMV Ehitus. Ehitus Tallinnas.",
234
],
[
"f-somar-ehitus",
"ehitus",
"pool",
"Ehitame Põlvamaal.",
235
],
[
"f-levetran",
"ehitus",
"aasta",
"Katus, fassaad ja remont Pärnus.",
236
],
[
"f-estraeg",
"ehitus",
"riba",
"Ehitus ja renoveerimine Tallinnas.",
237
],
[
"f-veirakon",
"ehitus",
"print",
"Maja ehitus Harjumaal.",
238
],
[
"f-diggerpower",
"ehitus",
"kaar",
"Ehitustööd Ida-Virumaal.",
239
],
[
"f-kiviidee",
"ehitus",
"taust",
"Uus maja või remont Tallinnas.",
240
],
[
"f-hjl-lahendused",
"ehitus",
"kolm",
"HJL Lahendused. Ehitus Tallinnas.",
241
],
[
"f-epicrates-grupp",
"ehitus",
"kaart",
"Ehitame Harjumaal.",
242
],
[
"f-vkmarik",
"ehitus",
"diag",
"Katus, fassaad ja remont Tallinnas.",
243
],
[
"f-vts-kuetsen",
"koristus",
"raam",
"Koristus Harjumaal.",
244
],
[
"f-kodu-puhastusteenus",
"koristus",
"ring",
"Puhas kodu ja kontor Harjumaal.",
245
],
[
"f-mirtko-haldus",
"koristus",
"duo",
"Koristusteenus Tallinnas.",
246
],
[
"f-koristame",
"koristus",
"pool",
"Koristame. Koristus Tallinnas.",
247
],
[
"f-intsverks",
"koristus",
"aasta",
"Kodu- ja kontorikoristus Lääne-Virumaal.",
248
],
[
"f-conerkar",
"koristus",
"riba",
"Koristus Tallinnas.",
249
],
[
"f-hansaprofid",
"koristus",
"print",
"Puhas kodu ja kontor Tallinnas.",
250
],
[
"f-tarkoris",
"koristus",
"kaar",
"Koristusteenus Tartus.",
251
],
[
"f-scanexport",
"koristus",
"taust",
"Scanexport. Koristus Tallinnas.",
252
],
[
"f-lenrid",
"koristus",
"kolm",
"Kodu- ja kontorikoristus Lääne-Virumaal.",
253
],
[
"f-kajavi-tood",
"koristus",
"kaart",
"Koristus Harjumaal.",
254
],
[
"f-mo-soe",
"koristus",
"diag",
"Puhas kodu ja kontor Saaremaal.",
255
],
[
"f-murcia-trade",
"koristus",
"raam",
"Koristusteenus Tallinnas.",
256
],
[
"f-repogil",
"koristus",
"ring",
"Repogil. Koristus Sindis.",
257
],
[
"f-kepsel",
"koristus",
"duo",
"Kodu- ja kontorikoristus Rakveres.",
258
],
[
"f-larysa-cleaning",
"koristus",
"pool",
"Koristus Tallinnas.",
259
],
[
"f-hoonetek",
"koristus",
"aasta",
"Puhas kodu ja kontor Tartus.",
260
],
[
"f-hadd",
"koristus",
"riba",
"Koristusteenus Tallinnas.",
261
],
[
"f-soom-puhtust",
"koristus",
"print",
"Sõõm Puhtust. Koristus Valgas.",
262
],
[
"f-ramilja",
"koristus",
"kaar",
"Kodu- ja kontorikoristus Tallinnas.",
263
],
[
"f-yld-ehitaja",
"ehitus",
"taust",
"Ehitus ja renoveerimine Harjumaal.",
264
],
[
"f-profimagi",
"ehitus",
"kolm",
"Maja ehitus Tartus.",
265
],
[
"f-vagral",
"ehitus",
"kaart",
"Ehitustööd Tallinnas.",
266
],
[
"f-keskest-ehitus",
"ehitus",
"diag",
"Uus maja või remont Jõgevamaal.",
267
],
[
"f-redon-grupp",
"ehitus",
"raam",
"Redon Grupp. Ehitus Lääne-Virumaal.",
268
],
[
"f-ralveko",
"ehitus",
"ring",
"Ehitame Põlvamaal.",
269
],
[
"f-eksmer-ehitus",
"ehitus",
"duo",
"Katus, fassaad ja remont Tartus.",
270
],
[
"f-transpoint-plus",
"ehitus",
"pool",
"Ehitus ja renoveerimine Pärnus.",
271
],
[
"f-ehtne-ehitus",
"ehitus",
"aasta",
"Maja ehitus Harjumaal.",
272
],
[
"f-elplen",
"ehitus",
"riba",
"Ehitustööd Maardus.",
273
],
[
"f-bt-ehitus",
"ehitus",
"print",
"Uus maja või remont Tartumaal.",
274
],
[
"f-spgv",
"ehitus",
"kaar",
"SPGV. Ehitus Lääne-Virumaal.",
275
],
[
"f-novok-ehitus",
"ehitus",
"taust",
"Ehitame Raplamaal.",
276
],
[
"f-rpl-service",
"ehitus",
"kolm",
"Katus, fassaad ja remont Viljandimaal.",
277
],
[
"f-th-ehitus",
"ehitus",
"kaart",
"Ehitus ja renoveerimine Harjumaal.",
278
]
]

for _r in FOTOLEHED:
    lisa(*_r)


# Varasemad lehed (saadetakse alates 29.10), nüüd fotoga avaplokiga. Pealkiri jäi sama.
UMBER = [
[
"p-a-soleil",
"juuksur",
"riba",
"Päike ka pilvisel päeval.",
300
],
[
"p-aminates",
"juuksur",
"print",
"Vaata peeglisse ja naerata.",
301
],
[
"p-auu-disain",
"juuksur",
"kaar",
"Disain sinu juustele.",
302
],
[
"p-bellamark",
"juuksur",
"taust",
"Bellamark.",
303
],
[
"p-bp-ilusalong",
"juuksur",
"kolm",
"Ilu ja juuksed ühest kohast.",
304
],
[
"p-edem-ilustuudio",
"juuksur",
"kaart",
"Edem Ilustuudio.",
305
],
[
"p-ellu",
"juuksur",
"diag",
"Ellu juuksur.",
306
],
[
"p-glamrim",
"juuksur",
"raam",
"Viimsi juuksur.",
307
],
[
"p-ilumaja",
"juuksur",
"ring",
"Pärnu Ilumaja.",
308
],
[
"p-ilusalong-lelii",
"juuksur",
"duo",
"Saaremaa ilusalong.",
309
],
[
"p-ilusalong-nr-1",
"juuksur",
"pool",
"Ilusalong Nr 1.",
310
],
[
"p-jbspot",
"juuksur",
"aasta",
"Lõikus ilma ootamata.",
311
],
[
"p-juukstop",
"juuksur",
"riba",
"Juukstop. Lõikus ja värv.",
312
],
[
"p-kaar-salongid",
"juuksur",
"print",
"Käärid, kamm ja hea jutt.",
313
],
[
"p-kiitna-tk",
"juuksur",
"kaar",
"Juuksur kesklinnas.",
314
],
[
"p-kristanoli",
"juuksur",
"taust",
"Juuksur Elva kandis.",
315
],
[
"p-kuldne-panter",
"juuksur",
"kolm",
"Kuldne Panter.",
316
],
[
"p-lavendel",
"juuksur-m",
"kaart",
"Meeste juuksur Kaupmehe tänaval.",
317
],
[
"p-lofty",
"juuksur",
"diag",
"Hea juuksepäev algab siit.",
318
],
[
"p-mari-liisi-ilutuba",
"juuksur",
"raam",
"Ilutuba Kiilis.",
319
],
[
"p-nona",
"juuksur",
"ring",
"Juuksed, mis jäävad meelde.",
320
],
[
"p-noorannika",
"juuksur",
"duo",
"Värske soeng Laagris.",
321
],
[
"p-parnu-salong",
"juuksur",
"pool",
"Pärnu juuksur, aeg ühe klikiga.",
322
],
[
"p-patsike",
"juuksur",
"aasta",
"Patsid, lõikus ja värv.",
323
],
[
"p-poisipea",
"juuksur",
"riba",
"Poisipea või pikad lokid.",
324
],
[
"p-rilja",
"juuksur",
"print",
"Juuksur Pärnumaa lõunas.",
325
],
[
"p-salong-rosita",
"juuksur",
"kaar",
"Salong Rosita.",
326
],
[
"p-salonjoi",
"juuksur",
"taust",
"Salong Haljalas.",
327
],
[
"p-theodor",
"juuksur-m",
"kolm",
"Meeste juuksur Raekoja platsil.",
328
],
[
"p-uncle-ve",
"juuksur",
"kaart",
"Uncle Ve. Lõikus ja habe.",
329
],
[
"p-4a-lux",
"elekter",
"diag",
"Valgus Tori vallas.",
330
],
[
"p-aavo-elekter",
"elekter",
"raam",
"Tartu elektrik.",
331
],
[
"p-albol-primer",
"elekter",
"ring",
"Elektritööd Otepää kandis.",
332
],
[
"p-calmar-electer",
"elekter",
"duo",
"Viljandi elektritööd.",
333
],
[
"p-el-teh-grupp",
"elekter",
"pool",
"Juhtmest kilbini.",
334
],
[
"p-electra-grupp",
"elekter",
"aasta",
"Tallinna elektritööd.",
335
],
[
"p-elektriparadiis",
"elekter",
"riba",
"Elektriparadiis Maardus.",
336
],
[
"p-elfi-elekter",
"elekter",
"print",
"Elektritööd Raplamaal.",
337
],
[
"p-eligero",
"elekter",
"kaar",
"Elektrik Ida-Virumaal.",
338
],
[
"p-elmiku",
"elekter",
"taust",
"Saaremaa elektritööd.",
339
],
[
"p-elortex",
"elekter",
"kolm",
"Pärnu elektrik.",
340
],
[
"p-elredi",
"elekter",
"kaart",
"Elektrik Tallinnas.",
341
],
[
"p-elren-elekter",
"elekter",
"diag",
"Saare elektrik.",
342
],
[
"p-estomeister",
"elekter",
"raam",
"Keila elektritööd.",
343
],
[
"p-ete-worx",
"elekter",
"ring",
"Elektritööd Jõhvi kandis.",
344
],
[
"p-eurest-group",
"elekter",
"duo",
"Elektritööd Keilas.",
345
],
[
"p-gentroon",
"elekter",
"pool",
"Elektritööd Pärnus ja Pärnumaal.",
346
],
[
"p-hooneabi",
"elekter",
"aasta",
"Elekter, mis lihtsalt töötab.",
347
],
[
"p-jannes",
"elekter",
"riba",
"Mulgimaa elektrik.",
348
],
[
"p-kaabeldusabi",
"elekter",
"print",
"Kaabeldus ja elekter Jõgevamaal.",
349
],
[
"p-kangro-nagla",
"elekter",
"kaar",
"Elektritööd Elva kandis.",
350
],
[
"p-khs",
"elekter",
"taust",
"Elektrik Jõgevamaal.",
351
],
[
"p-l-viru-elekter",
"elekter",
"kolm",
"Elektritööd Ida-Virumaal.",
352
],
[
"p-maasvool",
"elekter",
"kaart",
"Maasvool. Elekter Pärnus.",
353
],
[
"p-martipet",
"elekter",
"diag",
"Elektrik pealinnas.",
354
],
[
"p-msl-elektritood",
"elekter",
"raam",
"Võrumaa elektritööd.",
355
],
[
"p-otto-elekter",
"elekter",
"ring",
"Elektrik Jõgeva kandis.",
356
],
[
"p-peetri",
"elekter",
"duo",
"Elektrik Saaremaal.",
357
],
[
"p-pistrel",
"elekter",
"pool",
"Pistik, lüliti ja kilp.",
358
],
[
"p-reljans",
"elekter",
"aasta",
"Narva elektritööd.",
359
],
[
"p-sikuway",
"elekter",
"riba",
"Türi elektrik.",
360
],
[
"p-ss-elektritood",
"elekter",
"print",
"Elektritööd Pärnus ja ümbruses.",
361
],
[
"p-stablenord",
"elekter",
"kaar",
"Vool sees, mure läinud.",
362
],
[
"p-sven-elekter",
"elekter",
"taust",
"Elva kandi elektrik.",
363
],
[
"p-tagener",
"elekter",
"kolm",
"Elektritööd Tartus.",
364
],
[
"p-tavako-elekter",
"elekter",
"kaart",
"Pärnu elektritööd algusest lõpuni.",
365
],
[
"p-toostuselekter",
"elekter",
"diag",
"Elektritööd Viljandis.",
366
],
[
"p-valgis",
"elekter",
"raam",
"Valgus ja vool Narvas.",
367
],
[
"p-vitali-elekter",
"elekter",
"ring",
"Elekter korda Maardus.",
368
],
[
"p-winels",
"elekter",
"duo",
"Winels. Elektritööd Tallinnas.",
369
],
[
"p-allik-trans",
"toru",
"pool",
"Küte ja ventilatsioon Pärnus.",
370
],
[
"p-abc-kute",
"toru",
"aasta",
"Küte, jahutus ja ventilatsioon Tartus.",
371
],
[
"p-abix-teenindus",
"toru",
"riba",
"Keila kütte- ja ventilatsioonitööd.",
372
],
[
"p-fop-rem-grupp",
"toru",
"print",
"Küttetööd Ida-Virumaal.",
373
],
[
"p-berku-eritood",
"toru",
"kaar",
"Torutööd ja küte Hiiumaal.",
374
],
[
"p-lviworks",
"toru",
"taust",
"Vesi, küte ja ventilatsioon Tallinnas.",
375
],
[
"p-art-building",
"toru",
"kolm",
"Torutööd Tartus.",
376
],
[
"p-maxwelding-service",
"toru",
"kaart",
"Narva küttetööd.",
377
],
[
"p-sergo-torutood",
"toru",
"diag",
"Torutööd Pärnus.",
378
],
[
"p-kp-invest",
"toru",
"raam",
"Küttesüsteemid Tallinnas.",
379
],
[
"p-kp-kliima",
"toru-kliima",
"ring",
"Soojuspumbad Tartumaal.",
380
],
[
"p-entivent",
"toru",
"duo",
"Ventilatsioon Harjumaal.",
381
],
[
"p-veritang",
"toru",
"pool",
"Soe kodu Tallinnas.",
382
],
[
"p-teemantpoiss",
"toru",
"aasta",
"Teemantpoiss. Küte ja ventilatsioon.",
383
],
[
"p-estoman",
"toru",
"riba",
"Vesi ja kanalisatsioon Tallinnas.",
384
],
[
"p-aas-sanitaartehnika",
"toru",
"print",
"Sanitaartehnika Pärnus.",
385
],
[
"p-vexon-arendus",
"toru",
"kaar",
"Torutööd ja küte Tallinnas.",
386
],
[
"p-weldcom",
"toru",
"taust",
"Küttetorustikud Tallinnas.",
387
],
[
"p-deandra",
"toru",
"kolm",
"Torutööd pealinnas.",
388
],
[
"p-girlande",
"toru",
"kaart",
"Küte Harjumaal.",
389
],
[
"p-viktorija-maailm",
"toru",
"diag",
"Vesi ja kanalisatsioon Tartus.",
390
],
[
"p-jurgus-torutood",
"toru",
"raam",
"Jurgus. Torutööd Tartus.",
391
],
[
"p-ilstro-ehitus",
"toru",
"ring",
"Torutööd ja küte Kohtla-Järvel.",
392
],
[
"p-avass-grupp",
"toru",
"duo",
"Küttetööd Jõhvi kandis.",
393
],
[
"p-maritek",
"toru",
"pool",
"Torud ja küte Tartus.",
394
],
[
"p-kvv-torugrupp",
"toru",
"aasta",
"Vesi, kanalisatsioon ja küte.",
395
],
[
"p-vvs-paigaldus",
"toru",
"riba",
"Ventilatsioon Tallinnas.",
396
],
[
"p-kaltel",
"toru",
"print",
"Jõgeva torutööd ja küte.",
397
],
[
"p-acai-estonia",
"toru-ahi",
"kaar",
"Ahjud ja kaminad Viljandis.",
398
],
[
"p-torukunn",
"toru",
"taust",
"ToruKunn. Torutööd Tallinnas.",
399
],
[
"p-milann-santeh-grupp",
"toru",
"kolm",
"Santehnika Narvas.",
400
],
[
"p-kuul-ehitus",
"toru",
"kaart",
"Korras torud Tallinnas.",
401
],
[
"p-parnu-torutood",
"toru",
"diag",
"Torud ja küte Pärnumaal.",
402
],
[
"p-elrem",
"toru",
"raam",
"Torutööd Lääne-Virumaal.",
403
],
[
"p-inverter-heat",
"toru-kliima",
"ring",
"Soojuspumbad Järvamaal.",
404
],
[
"p-raksek",
"toru",
"duo",
"Küte ja ventilatsioon Saaremaal.",
405
],
[
"p-maida-sale",
"toru",
"pool",
"Torutööd ja küte Harjumaal.",
406
],
[
"p-cera-ehitus",
"toru",
"aasta",
"Torutööd Valgas.",
407
],
[
"p-seven-tehnika",
"toru",
"riba",
"Küte ja ventilatsioon Tallinnas.",
408
],
[
"p-kulmameister",
"toru-kliima",
"print",
"Soojuspumbad ja jahutus Narvas.",
409
],
[
"p-maximus-ehitus",
"toru",
"kaar",
"Vesi ja kanalisatsioon Tallinnas.",
410
],
[
"p-arek-grupp",
"toru",
"taust",
"Küttetööd Sauel.",
411
],
[
"p-kummionu",
"toru",
"kolm",
"Soe maja Võrus.",
412
],
[
"p-janest-grupp",
"toru",
"kaart",
"Küttesüsteemid Tartus.",
413
],
[
"p-sanekyte",
"toru",
"diag",
"Vesi ja küte Tartumaal.",
414
],
[
"p-valiskeere",
"toru",
"raam",
"Väliskeere. Küte Saaremaal.",
415
],
[
"p-baltkomfort",
"toru",
"ring",
"Santehnika Tallinnas.",
416
],
[
"p-riho-kinnisvarahooldus",
"toru",
"duo",
"Korras torud Viljandis.",
417
],
[
"p-e-r-kliima",
"toru-kliima",
"pool",
"Kliima ja küte Järvamaal.",
418
],
[
"p-kulmamasin",
"toru-kliima",
"aasta",
"Soojuspumbad ja jahutus Tartumaal.",
419
],
[
"p-sanjaan",
"toru",
"riba",
"Torud ja küte Jõgeval.",
420
],
[
"p-alvira-vsk",
"toru",
"print",
"Alvira VSK. Torutööd Ida-Virumaal.",
421
],
[
"p-hannobalt",
"toru",
"kaar",
"Torutööd Harjumaal.",
422
],
[
"p-valexehitus",
"toru",
"taust",
"Küte ja ventilatsioon Harjumaal.",
423
],
[
"p-ehitus-ja-soojus",
"toru",
"kolm",
"Küttetööd Pärnus.",
424
],
[
"p-k-kolded",
"toru-ahi",
"kaart",
"Ahjud ja kaminad Tartumaal.",
425
],
[
"p-vesi-ja-soojus",
"toru",
"diag",
"Soe maja Harjumaal.",
426
],
[
"p-napri-vent",
"toru",
"raam",
"Ventilatsioon Viljandimaal.",
427
],
[
"p-trubagood",
"toru",
"ring",
"Küttesüsteemid Tallinnas.",
428
],
[
"p-haldi-infra",
"toru",
"duo",
"Haldi Infra. Küte Lääne-Virumaal.",
429
],
[
"p-kagunurk",
"toru-ahi",
"pool",
"Ahjud ja pliidid Põlvas.",
430
],
[
"p-toruvennad",
"toru",
"aasta",
"Santehnika Pärnus.",
431
],
[
"p-goodreason",
"toru",
"riba",
"Küte ja ventilatsioon Tallinnas.",
432
],
[
"p-plumbweld",
"toru",
"print",
"Korras torud Tallinnas.",
433
],
[
"p-arvikom",
"toru",
"kaar",
"Arvikom. Torutööd Tallinnas.",
434
],
[
"p-rakimel",
"toru",
"taust",
"Küttetööd Tartus.",
435
],
[
"p-drandool",
"toru",
"kolm",
"Soe maja Pärnus.",
436
],
[
"p-shumas-ehitus",
"toru",
"kaart",
"Küttesüsteemid Narvas.",
437
],
[
"p-al-bi-sant",
"toru",
"diag",
"Torutööd Tartus.",
438
],
[
"p-ohu-ehitus",
"toru",
"raam",
"Värske õhk Tallinnas.",
439
],
[
"p-i-s-p-s",
"toru",
"ring",
"Vesi ja kanalisatsioon Tartus.",
440
],
[
"p-sanrec-eesti",
"toru",
"duo",
"Santehnika Harjumaal.",
441
],
[
"p-torupark",
"toru",
"pool",
"Korras torud Harjumaal.",
442
],
[
"p-spe-grupp",
"toru",
"aasta",
"Spe Grupp. Torud ja küte.",
443
],
[
"p-volffix",
"toru",
"riba",
"Volffix. Torutööd Tartus.",
444
],
[
"p-linmar-torutood",
"toru",
"print",
"Torutööd Harjumaal.",
445
],
[
"p-matex-service",
"toru",
"kaar",
"Vesi ja kanalisatsioon Põlvas.",
446
],
[
"p-raidora-grupp",
"toru",
"taust",
"Torutööd ja küte Tallinnas.",
447
],
[
"p-eestimeister",
"toru",
"kolm",
"Santehnika Tallinnas.",
448
],
[
"p-alfakliima",
"toru-kliima",
"kaart",
"Kliima ja küte Viljandis.",
449
],
[
"p-freeform",
"toru",
"diag",
"FreeForm. Küte Tallinnas.",
450
],
[
"p-ideaalkaminad",
"toru-ahi",
"raam",
"Ahjud ja kaminad Viljandis.",
451
],
[
"p-rjv-ehitus",
"toru",
"ring",
"Küte ja ventilatsioon Maardus.",
452
],
[
"p-j-t-terasmaa",
"toru",
"duo",
"Vesi ja küte Keilas.",
453
],
[
"p-lulekar-solutions",
"toru",
"pool",
"Korras torud Tartumaal.",
454
],
[
"p-mirtex-teenus",
"toru",
"aasta",
"Torud ja küte Harjumaal.",
455
],
[
"p-tornimees",
"toru",
"riba",
"Küttetööd Tallinnas.",
456
],
[
"p-elvetor",
"toru",
"print",
"Elvetor. Torutööd Viljandis.",
457
],
[
"p-dimlex-toru",
"toru",
"kaar",
"DimLex Toru. Torud ja küte.",
458
],
[
"p-tanpeeg",
"toru",
"taust",
"Soe maja Harjumaal.",
459
],
[
"p-arles",
"toru",
"kolm",
"Küttesüsteemid Tartus.",
460
],
[
"p-hansagas",
"toru",
"kaart",
"Hansagas. Küte Tallinnas.",
461
],
[
"p-termia",
"toru",
"diag",
"Küte ja ventilatsioon Tallinnas.",
462
],
[
"p-kaas-grupp",
"toru-ahi",
"raam",
"Ahjud ja pliidid Pärnumaal.",
463
],
[
"p-esajas-invest",
"toru",
"ring",
"Küttetööd Põlvamaal.",
464
],
[
"p-sanka",
"toru",
"duo",
"Torutööd Jõgevamaal.",
465
],
[
"p-fluk-tehnik",
"toru",
"pool",
"Vesi ja kanalisatsioon Kohtla-Järvel.",
466
],
[
"p-ra-luft",
"toru",
"aasta",
"Ventilatsioon Pärnumaal.",
467
],
[
"p-santeh-invest",
"toru",
"riba",
"Torutööd ja küte Tallinnas.",
468
],
[
"p-san-v",
"toru",
"print",
"Santehnika Pärnus.",
469
],
[
"p-sepa-ehitus",
"viimistlus",
"kaar",
"Sepa Ehitus Saku vallas.",
470
],
[
"p-privamal",
"viimistlus",
"taust",
"Plaatimine Kambja kandis.",
471
],
[
"p-porandast-laeni",
"viimistlus",
"kolm",
"Põrandast laeni, Pärnus.",
472
],
[
"p-joksi-mek",
"viimistlus",
"kaart",
"Remont Põlvamaal.",
473
],
[
"p-ksa-paigaldusgrupp",
"viimistlus",
"diag",
"Värvimine Tartu vallas.",
474
],
[
"p-sideline",
"viimistlus",
"raam",
"Viimistlus Võrumaal.",
475
],
[
"p-puidusober",
"viimistlus",
"ring",
"Põrandad ja viimistlus Kuusalus.",
476
],
[
"p-ille-siseviimistlus",
"viimistlus",
"duo",
"Ille Siseviimistlus.",
477
]
]

for _r in UMBER:
    lisa(*_r)


# Autoteenindused kolmandalt kontolt (alates 29.10).
AUTOLEHED = [
[
"f-autorem-dk",
"auto",
"taust",
"Autoremont Rakveres.",
600
],
[
"f-aldova",
"auto",
"kaar",
"Auto hooldus ja remont Võrumaal.",
601
],
[
"f-kttt",
"auto",
"print",
"Hooldus ja diagnostika Valgas.",
602
],
[
"f-remotors",
"auto",
"riba",
"Teie auto remont Raplamaal.",
603
],
[
"f-mertaks",
"auto",
"aasta",
"Autoteenindus Tallinnas.",
604
],
[
"f-tarmaks-autoservis",
"auto",
"pool",
"Autoremont Kohtla-Järvel.",
605
],
[
"f-alicron-grupp",
"auto",
"duo",
"Auto hooldus ja remont Kohtla-Järvel.",
606
],
[
"f-chippro",
"auto",
"ring",
"Hooldus ja diagnostika Viljandimaal.",
607
],
[
"f-raudvelg",
"auto-rehv",
"raam",
"Rehvivahetus Viljandimaal.",
609
],
[
"f-olympic-car-fest",
"auto",
"diag",
"Autoteenindus Harjumaal.",
609
],
[
"f-mt-autospa",
"auto-detail",
"kaart",
"Puhas auto Tartumaal.",
610
],
[
"f-karavani-service",
"auto-detail",
"kolm",
"Auto puhastus seest ja väljast.",
612
],
[
"f-kulasepp",
"auto",
"taust",
"Hooldus ja diagnostika Tartumaal.",
612
],
[
"f-repairit",
"auto",
"kaar",
"Teie auto remont Tallinnas.",
613
],
[
"f-anpo-teenused",
"auto",
"print",
"Autoteenindus Harjumaal.",
614
],
[
"f-serdna-servis",
"auto",
"riba",
"Autoremont Tartus.",
615
],
[
"f-onk-trans",
"auto",
"aasta",
"Auto hooldus ja remont Tallinnas.",
616
],
[
"f-tehrem",
"auto",
"pool",
"Hooldus ja diagnostika Saaremaal.",
617
],
[
"f-scalor",
"auto",
"duo",
"Teie auto remont Harjumaal.",
618
],
[
"f-vaivara-transservis",
"auto",
"ring",
"Autoteenindus Narva-Jõesuus.",
619
],
[
"f-sepresto",
"auto",
"raam",
"Autoremont Lääne-Virumaal.",
620
],
[
"f-laagna-auto",
"auto",
"diag",
"Auto hooldus ja remont Tallinnas.",
621
],
[
"f-sanderauto",
"auto",
"kaart",
"Hooldus ja diagnostika Jõgevamaal.",
622
],
[
"f-altek-pro",
"auto",
"kolm",
"Teie auto remont Ida-Virumaal.",
623
],
[
"f-viraks",
"auto",
"taust",
"Autoteenindus Tallinnas.",
624
],
[
"f-oktrans",
"auto",
"kaar",
"Autoremont Maardus.",
625
],
[
"f-amstell",
"auto",
"print",
"Auto hooldus ja remont Tallinnas.",
626
],
[
"f-kohalik-autohoole",
"auto",
"riba",
"Hooldus ja diagnostika Pärnumaal.",
627
],
[
"f-dafu-trans",
"auto",
"aasta",
"Teie auto remont Tallinnas.",
628
],
[
"f-rautor-grupp",
"auto",
"pool",
"Autoteenindus Tallinnas.",
629
],
[
"f-sandla-motoservice",
"auto",
"duo",
"Autoremont Saaremaal.",
630
],
[
"f-auto-korrashoid",
"auto",
"ring",
"Auto hooldus ja remont Viljandis.",
631
],
[
"f-garageplus",
"auto",
"raam",
"Hooldus ja diagnostika Harjumaal.",
632
],
[
"f-48cars",
"auto",
"diag",
"Teie auto remont Harjumaal.",
633
],
[
"f-krei-auto",
"auto",
"kaart",
"Autoteenindus Harjumaal.",
634
],
[
"f-viimserv",
"auto",
"kolm",
"Autoremont Tallinnas.",
635
],
[
"f-yescar",
"auto",
"taust",
"Auto hooldus ja remont Põlvamaal.",
636
],
[
"f-tku-teenused",
"auto",
"kaar",
"Hooldus ja diagnostika Saaremaal.",
637
],
[
"f-elten-motors",
"auto",
"print",
"Teie auto remont Tallinnas.",
638
],
[
"f-helcarteam",
"auto",
"riba",
"Autoteenindus Saaremaal.",
639
],
[
"f-tauriko",
"auto",
"aasta",
"Autoremont Raplamaal.",
640
],
[
"f-kraav-auto",
"auto",
"pool",
"Auto hooldus ja remont Hiiumaal.",
641
],
[
"f-lt-auto",
"auto",
"duo",
"Hooldus ja diagnostika Pärnus.",
642
],
[
"f-mechanic-car-service",
"auto",
"ring",
"Teie auto remont Tallinnas.",
643
],
[
"f-saare-diisel",
"auto",
"raam",
"Autoteenindus Saaremaal.",
644
],
[
"f-teorein",
"auto",
"diag",
"Autoremont Valgamaal.",
645
],
[
"f-vo-way",
"auto",
"kaart",
"Auto hooldus ja remont Ida-Virumaal.",
646
],
[
"f-klereke",
"auto",
"kolm",
"Hooldus ja diagnostika Tallinnas.",
647
],
[
"f-merksani",
"auto",
"taust",
"Teie auto remont Põlvas.",
648
],
[
"f-vahurel",
"auto",
"kaar",
"Autoteenindus Lääne-Virumaal.",
649
],
[
"f-dkmotors",
"auto",
"print",
"Autoremont Pärnumaal.",
650
],
[
"f-rehvi-maantee",
"auto-rehv",
"riba",
"Rehvid ja veljed Tallinnas.",
651
],
[
"f-revada-remont",
"auto",
"aasta",
"Hooldus ja diagnostika Tallinnas.",
652
],
[
"f-ra-detailing",
"auto-detail",
"pool",
"Auto detailing Raplas.",
654
],
[
"f-jp-garage",
"auto",
"duo",
"Autoteenindus Harjumaal.",
654
],
[
"f-lavenko",
"auto",
"ring",
"Autoremont Jõgevamaal.",
655
],
[
"f-tfs-ceramic",
"auto-detail",
"raam",
"Poleerimine ja keraamiline kaitse.",
657
]
]

for _r in AUTOLEHED:
    lisa(*_r)


# Elektrikud kolmandalt kontolt (4.–6.11).
ELEKTERLEHED = [
[
"f-ikiti-grupp",
"elekter",
"riba",
"Elektritööd Võrumaal.",
700
],
[
"f-utpro",
"elekter",
"print",
"Elektrik Tallinnas.",
701
],
[
"f-installor",
"elekter",
"kaar",
"Elektripaigaldus ja remont Keilas.",
702
],
[
"f-vigral",
"elekter",
"taust",
"Elektritööd kodus ja ettevõttes.",
703
],
[
"f-baltic-anur",
"elekter",
"kolm",
"Juhtmestik, kilbid ja valgustus Tallinnas.",
704
],
[
"f-sahkomees",
"elekter",
"kaart",
"Elektritööd Tartumaal.",
705
],
[
"f-nzelekter",
"elekter",
"diag",
"Elektrik Tallinnas.",
706
],
[
"f-dielekter",
"elekter",
"raam",
"Elektripaigaldus ja remont Tallinnas.",
707
],
[
"f-jarvelo",
"elekter",
"ring",
"Elektritööd kodus ja ettevõttes.",
708
],
[
"f-skat-elekter",
"elekter",
"duo",
"Juhtmestik, kilbid ja valgustus Tallinnas.",
709
],
[
"f-elwepro",
"elekter",
"pool",
"Elektritööd Pärnus.",
710
],
[
"f-voltexpert",
"elekter",
"aasta",
"Elektrik Tallinnas.",
711
],
[
"f-electrical-team",
"elekter",
"riba",
"Elektripaigaldus ja remont Kohtla-Järvel.",
712
],
[
"f-regina-elekter",
"elekter",
"print",
"Elektritööd kodus ja ettevõttes.",
713
],
[
"f-tarmik",
"elekter",
"kaar",
"Juhtmestik, kilbid ja valgustus Harjumaal.",
714
],
[
"f-electrico-solution",
"elekter",
"taust",
"Elektritööd Kohtla-Järvel.",
715
],
[
"f-brentel",
"elekter",
"kolm",
"Elektrik Pärnus.",
716
],
[
"f-aapol",
"elekter",
"kaart",
"Elektripaigaldus ja remont Pärnus.",
717
],
[
"f-arturi-elekter",
"elekter",
"diag",
"Elektritööd kodus ja ettevõttes.",
718
],
[
"f-elasi-elekter",
"elekter",
"raam",
"Juhtmestik, kilbid ja valgustus Tartumaal.",
719
],
[
"f-smartinstallation",
"elekter",
"ring",
"Elektritööd Tallinnas.",
720
],
[
"f-elekter4you",
"elekter",
"duo",
"Elektrik Tallinnas.",
721
],
[
"f-varistor",
"elekter",
"pool",
"Elektripaigaldus ja remont Pärnus.",
722
],
[
"f-asew",
"elekter",
"aasta",
"Elektritööd kodus ja ettevõttes.",
723
],
[
"f-rauteco",
"elekter",
"riba",
"Juhtmestik, kilbid ja valgustus Harjumaal.",
724
],
[
"f-kadrina-elektrik",
"elekter",
"print",
"Elektritööd Lääne-Virumaal.",
725
],
[
"f-elektritark",
"elekter",
"kaar",
"Elektrik Harjumaal.",
726
],
[
"f-stargo",
"elekter",
"taust",
"Elektripaigaldus ja remont Jõgeval.",
727
],
[
"f-elekto-hpn",
"elekter",
"kolm",
"Elektritööd kodus ja ettevõttes.",
728
],
[
"f-velsi-service",
"elekter",
"kaart",
"Juhtmestik, kilbid ja valgustus Ida-Virumaal.",
729
],
[
"f-vipersem",
"elekter",
"diag",
"Elektritööd Narvas.",
730
],
[
"f-v-j-elektritood",
"elekter",
"raam",
"Elektrik Pärnumaal.",
731
],
[
"f-tafles",
"elekter",
"ring",
"Elektripaigaldus ja remont Tallinnas.",
732
],
[
"f-traadiklubi",
"elekter",
"duo",
"Elektritööd kodus ja ettevõttes.",
733
],
[
"f-suda-elekter",
"elekter",
"pool",
"Juhtmestik, kilbid ja valgustus Tallinnas.",
734
],
[
"f-antti-mannik",
"elekter",
"aasta",
"Elektritööd Tartumaal.",
735
],
[
"f-elsa-ap",
"elekter",
"riba",
"Elektrik Pärnus.",
736
],
[
"f-haskeldaja",
"elekter",
"print",
"Elektripaigaldus ja remont Pärnumaal.",
737
],
[
"f-elektrivark",
"elekter",
"kaar",
"Elektritööd kodus ja ettevõttes.",
738
],
[
"f-hasti-elektri",
"elekter",
"taust",
"Juhtmestik, kilbid ja valgustus Tallinnas.",
739
],
[
"f-riigerm",
"elekter",
"kolm",
"Elektritööd Viljandimaal.",
740
],
[
"f-ricoran",
"elekter",
"kaart",
"Elektrik Lääne-Virumaal.",
741
],
[
"f-electa-solution",
"elekter",
"diag",
"Elektripaigaldus ja remont Raplamaal.",
742
],
[
"f-elerton",
"elekter",
"raam",
"Elektritööd kodus ja ettevõttes.",
743
],
[
"f-j-j-elekter",
"elekter",
"ring",
"Juhtmestik, kilbid ja valgustus Raplamaal.",
744
],
[
"f-terken",
"elekter",
"duo",
"Elektritööd Haapsalus.",
745
],
[
"f-priitel",
"elekter",
"pool",
"Elektrik Lääne-Virumaal.",
746
],
[
"f-elstorm",
"elekter",
"aasta",
"Elektripaigaldus ja remont Tallinnas.",
747
],
[
"f-istaco",
"elekter",
"riba",
"Elektritööd kodus ja ettevõttes.",
748
],
[
"f-garantpro",
"elekter",
"print",
"Juhtmestik, kilbid ja valgustus Tartumaal.",
749
],
[
"f-sulfuras",
"elekter",
"kaar",
"Elektritööd Harjumaal.",
750
],
[
"f-randes",
"elekter",
"taust",
"Elektrik Järvamaal.",
751
],
[
"f-euro-elektro-service",
"elekter",
"kolm",
"Elektripaigaldus ja remont Kohtla-Järvel.",
752
],
[
"f-elromelecter",
"elekter",
"kaart",
"Elektritööd kodus ja ettevõttes.",
753
],
[
"f-encast",
"elekter",
"diag",
"Juhtmestik, kilbid ja valgustus Saaremaal.",
754
],
[
"f-virteks-projekt",
"elekter",
"raam",
"Elektritööd Rakveres.",
755
],
[
"f-riest",
"elekter",
"ring",
"Elektrik Tartumaal.",
756
],
[
"f-sintra-group",
"elekter",
"duo",
"Elektripaigaldus ja remont Läänemaal.",
757
],
[
"f-corally",
"elekter",
"pool",
"Elektritööd kodus ja ettevõttes.",
758
],
[
"f-kindel-grupp",
"elekter",
"aasta",
"Juhtmestik, kilbid ja valgustus Tartumaal.",
759
]
]

for _r in ELEKTERLEHED:
    lisa(*_r)


# Autoteenindused neljandalt kontolt (veebikask.lehed, alates 30.10).
AUTOLEHED4 = [
[
"f-lesvenauto",
"auto",
"pool",
"Autoremont Tallinnas.",
800
],
[
"f-rm-auto",
"auto",
"duo",
"Auto hooldus ja remont Harjumaal.",
801
],
[
"f-plaviteks",
"auto",
"ring",
"Hooldus ja diagnostika Rakveres.",
802
],
[
"f-savana-auto",
"auto",
"raam",
"Teie auto remont Tallinnas.",
803
],
[
"f-nester-pluss",
"auto",
"diag",
"Autoteenindus Tartus.",
804
],
[
"f-a-trans-service",
"auto",
"kaart",
"Autoremont Harjumaal.",
805
],
[
"f-romuveski",
"auto",
"kolm",
"Auto hooldus ja remont Tartumaal.",
806
],
[
"f-o-h-servis",
"auto",
"taust",
"Hooldus ja diagnostika Tartumaal.",
807
],
[
"f-aleklena",
"auto",
"kaar",
"Teie auto remont Tallinnas.",
808
],
[
"f-volfor-at",
"auto",
"print",
"Autoteenindus Harjumaal.",
809
],
[
"f-myrtos",
"auto",
"riba",
"Autoremont Järvamaal.",
810
],
[
"f-carsave-tehnik",
"auto",
"aasta",
"Auto hooldus ja remont Tallinnas.",
811
],
[
"f-autoteenindus-r-z",
"auto",
"pool",
"Hooldus ja diagnostika Tallinnas.",
812
],
[
"f-tehnikateenindus",
"auto",
"duo",
"Teie auto remont Harjumaal.",
813
],
[
"f-kummix",
"auto-rehv",
"ring",
"Rehvivahetus Tartumaal.",
816
],
[
"f-spirit-autoteenindus",
"auto",
"raam",
"Autoremont Tartus.",
815
],
[
"f-o-a-s-service",
"auto",
"diag",
"Auto hooldus ja remont Maardus.",
816
],
[
"f-svp-grupp",
"auto",
"kaart",
"Hooldus ja diagnostika Pärnus.",
817
],
[
"f-a-osa",
"auto",
"kolm",
"Teie auto remont Tallinnas.",
818
],
[
"f-jarve-auto-viljandi",
"auto",
"taust",
"Autoteenindus Viljandis.",
819
],
[
"f-carland-grupp",
"auto",
"kaar",
"Autoremont Pärnumaal.",
820
],
[
"f-trostinauto",
"auto",
"print",
"Auto hooldus ja remont Tallinnas.",
821
],
[
"f-teriva",
"auto",
"riba",
"Hooldus ja diagnostika Saaremaal.",
822
],
[
"f-antraton-grupp",
"auto",
"aasta",
"Teie auto remont Järvamaal.",
823
],
[
"f-innmer",
"auto",
"pool",
"Autoteenindus Harjumaal.",
824
],
[
"f-aleks-cars-remont",
"auto",
"duo",
"Autoremont Tallinnas.",
825
],
[
"f-urmenn",
"auto",
"ring",
"Auto hooldus ja remont Pärnumaal.",
826
],
[
"f-autoremondi-tookoda",
"auto",
"raam",
"Hooldus ja diagnostika Ida-Virumaal.",
827
],
[
"f-veotehnika",
"auto",
"diag",
"Teie auto remont Tallinnas.",
828
],
[
"f-lepiku-auto",
"auto",
"kaart",
"Autoteenindus Lääne-Virumaal.",
829
],
[
"f-brimar-servis",
"auto",
"kolm",
"Autoremont Põlvamaal.",
830
],
[
"f-derek",
"auto",
"taust",
"Auto hooldus ja remont Tallinnas.",
831
],
[
"f-auto-elek-grupp",
"auto",
"kaar",
"Hooldus ja diagnostika Narvas.",
832
],
[
"f-liise-auto",
"auto",
"print",
"Teie auto remont Raplamaal.",
833
],
[
"f-paikeseauto",
"auto",
"riba",
"Autoteenindus Tallinnas.",
834
],
[
"f-tlauto",
"auto",
"aasta",
"Autoremont Pärnus.",
835
],
[
"f-urme-auto",
"auto",
"pool",
"Auto hooldus ja remont Jõgeval.",
836
],
[
"f-tocar-motors",
"auto",
"duo",
"Hooldus ja diagnostika Lääne-Virumaal.",
837
],
[
"f-elips-k",
"auto",
"ring",
"Teie auto remont Harjumaal.",
838
],
[
"f-kalmat",
"auto",
"raam",
"Autoteenindus Lääne-Virumaal.",
839
],
[
"f-avotex-service",
"auto",
"diag",
"Autoremont Järvamaal.",
840
],
[
"f-kardaani-expert",
"auto",
"kaart",
"Auto hooldus ja remont Kohtla-Järvel.",
841
],
[
"f-angry-orange-autod",
"auto",
"kolm",
"Hooldus ja diagnostika Pärnumaal.",
842
],
[
"f-rt-autoremont",
"auto",
"taust",
"Teie auto remont Tartus.",
843
],
[
"f-mkm-autod",
"auto",
"kaar",
"Autoteenindus Pärnumaal.",
844
],
[
"f-asoli-auto",
"auto",
"print",
"Autoremont Keilas.",
845
],
[
"f-novoral",
"auto",
"riba",
"Auto hooldus ja remont Harjumaal.",
846
],
[
"f-carmax-estonia",
"auto",
"aasta",
"Hooldus ja diagnostika Lääne-Virumaal.",
847
],
[
"f-byl-swed-service",
"auto",
"pool",
"Teie auto remont Tallinnas.",
848
],
[
"f-toru-autoremont",
"auto",
"duo",
"Autoteenindus Tartumaal.",
849
],
[
"f-hk-rehvikeskus",
"auto-rehv",
"ring",
"Rehvivahetus Tartus.",
852
],
[
"f-urkna",
"auto",
"raam",
"Auto hooldus ja remont Harjumaal.",
851
],
[
"f-kaasiku-auto",
"auto",
"diag",
"Hooldus ja diagnostika Jõgevamaal.",
852
],
[
"f-holmvik",
"auto",
"kaart",
"Teie auto remont Pärnumaal.",
853
],
[
"f-airol",
"auto",
"kolm",
"Autoteenindus Pärnus.",
854
],
[
"f-carton",
"auto",
"taust",
"Autoremont Rakveres.",
855
],
[
"f-villiservice",
"auto",
"kaar",
"Auto hooldus ja remont Tallinnas.",
856
],
[
"f-kalsim",
"auto",
"print",
"Hooldus ja diagnostika Tartumaal.",
857
],
[
"f-jr-auto",
"auto",
"riba",
"Teie auto remont Ida-Virumaal.",
858
],
[
"f-heifix",
"auto",
"aasta",
"Autoteenindus Valgas.",
859
],
[
"f-tabani-hg",
"auto",
"pool",
"Autoremont Tallinnas.",
860
],
[
"f-maveric-motors",
"auto",
"duo",
"Auto hooldus ja remont Lääne-Virumaal.",
861
],
[
"f-rif-auto",
"auto",
"ring",
"Hooldus ja diagnostika Jõgevamaal.",
862
],
[
"f-viksess",
"auto",
"raam",
"Teie auto remont Jõgevamaal.",
863
],
[
"f-ks-trak",
"auto",
"diag",
"Autoteenindus Võrumaal.",
864
],
[
"f-jo-racing-solutions",
"auto",
"kaart",
"Autoremont Saaremaal.",
865
],
[
"f-stevoauto",
"auto",
"kolm",
"Auto hooldus ja remont Ida-Virumaal.",
866
],
[
"f-maxiton-grupp",
"auto",
"taust",
"Hooldus ja diagnostika Harjumaal.",
867
],
[
"f-oskar-auto",
"auto",
"kaar",
"Teie auto remont Valgamaal.",
868
],
[
"f-kannu-ari",
"auto",
"print",
"Autoteenindus Pärnumaal.",
869
],
[
"f-oiluk-grupp",
"auto",
"riba",
"Autoremont Tallinnas.",
870
],
[
"f-octoport",
"auto",
"aasta",
"Auto hooldus ja remont Tallinnas.",
871
],
[
"f-nordic-classiccars",
"auto",
"pool",
"Hooldus ja diagnostika Tartumaal.",
872
],
[
"f-pritech",
"auto",
"duo",
"Teie auto remont Võrumaal.",
873
],
[
"f-veermikuproff",
"auto",
"ring",
"Autoteenindus Lääne-Virumaal.",
874
],
[
"f-gardi-elektroonika",
"auto",
"raam",
"Autoremont Rakveres.",
875
],
[
"f-klapivedru",
"auto",
"diag",
"Auto hooldus ja remont Tallinnas.",
876
],
[
"f-duubzu-motors",
"auto",
"kaart",
"Hooldus ja diagnostika Tallinnas.",
877
],
[
"f-tartrev",
"auto",
"kolm",
"Teie auto remont Tallinnas.",
878
],
[
"f-nnb-union",
"auto",
"taust",
"Autoteenindus Tallinnas.",
879
],
[
"f-peritex-auto",
"auto",
"kaar",
"Autoremont Lääne-Virumaal.",
880
],
[
"f-eriprojekt",
"auto",
"print",
"Auto hooldus ja remont Raplamaal.",
881
],
[
"f-a-t-autoremont",
"auto",
"riba",
"Hooldus ja diagnostika Lääne-Virumaal.",
882
],
[
"f-kiiskar",
"auto",
"aasta",
"Teie auto remont Saaremaal.",
883
],
[
"f-iper-autoremont",
"auto",
"pool",
"Autoteenindus Tallinnas.",
884
],
[
"f-aabestcar-autokeskus",
"auto",
"duo",
"Autoremont Harjumaal.",
885
],
[
"f-varviks",
"auto",
"ring",
"Kereremont ja värvimine Pärnus.",
886
],
[
"f-test-rem-diisel",
"auto",
"raam",
"Hooldus ja diagnostika Tallinnas.",
887
],
[
"f-raini-auto",
"auto",
"diag",
"Teie auto remont Pärnumaal.",
888
],
[
"f-vaabvarv",
"auto",
"kaart",
"Auto värvimine Tartumaal.",
889
],
[
"f-valserhooldus",
"auto",
"kolm",
"Autoremont Harjumaal.",
890
],
[
"f-sportan-auto",
"auto",
"taust",
"Auto hooldus ja remont Tallinnas.",
891
],
[
"f-rein-vello",
"auto",
"kaar",
"Hooldus ja diagnostika Tallinnas.",
892
],
[
"f-ahula-auto",
"auto",
"print",
"Teie auto remont Järvamaal.",
893
]
]

for _r in AUTOLEHED4:
    lisa(*_r)


# Nädala 9.–13.11 lehed (i 1000+)
NADALLEHED = [
[
"f-lapson-ehitus",
"viimistlus",
"raam",
"Siseviimistlus Harjumaal.",
1000
],
[
"f-divinest",
"viimistlus",
"ring",
"Värvimistööd Tallinnas.",
1001
],
[
"f-tm-porandad",
"viimistlus",
"duo",
"Plaatimine ja põrandad Tartumaal.",
1002
],
[
"f-4k-ehitus",
"viimistlus",
"pool",
"Plaatimine ja põrandad Järvamaal.",
1003
],
[
"f-pahtlily",
"viimistlus",
"aasta",
"Siseviimistlus Võrumaal.",
1004
],
[
"f-workbridge",
"viimistlus",
"riba",
"Remonditööd Tallinnas.",
1005
],
[
"f-revo-lux-living",
"viimistlus",
"print",
"Siseviimistlus Võrumaal.",
1006
],
[
"f-rutt",
"viimistlus",
"kaar",
"Krohvi- ja pahtlitööd Tartumaal.",
1007
],
[
"f-meh-service",
"viimistlus",
"taust",
"Siseviimistlus Harjumaal.",
1008
],
[
"f-ando-moobel",
"viimistlus",
"kolm",
"Remonditööd Tallinnas.",
1009
],
[
"f-viimasepeal-maalerdus",
"viimistlus",
"kaart",
"Krohvi- ja pahtlitööd Tartumaal.",
1010
],
[
"f-prixon",
"viimistlus",
"diag",
"Remonditööd Harjumaal.",
1011
],
[
"f-retromark",
"viimistlus",
"raam",
"Siseviimistlus Tartus.",
1012
],
[
"f-bourbon",
"viimistlus",
"ring",
"Remonditööd Tallinnas.",
1013
],
[
"f-bauvo-eesti",
"viimistlus",
"duo",
"Värvimistööd Tallinnas.",
1014
],
[
"f-valoflor",
"viimistlus",
"pool",
"Plaatimine ja põrandad Põlvamaal.",
1015
],
[
"f-domnitex",
"viimistlus",
"aasta",
"Siseviimistlus Narvas.",
1016
],
[
"f-mfk-ehitus",
"viimistlus",
"riba",
"Plaatimine ja põrandad Tartus.",
1017
],
[
"f-amsa",
"viimistlus",
"print",
"Siseviimistlus Harjumaal.",
1018
],
[
"f-margilan",
"viimistlus",
"kaar",
"Remonditööd Maardus.",
1019
],
[
"f-kalaia-enterprises",
"viimistlus",
"taust",
"Värvimistööd Tallinnas.",
1020
],
[
"f-moobelkoos",
"viimistlus",
"kolm",
"Remonditööd Järvamaal.",
1021
],
[
"f-build-cartel",
"viimistlus",
"kaart",
"Siseviimistlus Võrumaal.",
1022
],
[
"f-bluumforest-build",
"viimistlus",
"diag",
"Remonditööd Pärnumaal.",
1023
],
[
"f-janmasterfas",
"viimistlus",
"raam",
"Siseviimistlus Harjumaal.",
1024
],
[
"f-ah-building",
"viimistlus",
"ring",
"Remonditööd Valgas.",
1025
],
[
"f-suurmaa-grupp",
"viimistlus",
"duo",
"Siseviimistlus Lääne-Virumaal.",
1026
],
[
"f-sv-pro-ehitus",
"viimistlus",
"pool",
"Remonditööd Harjumaal.",
1027
],
[
"f-premium-kodu",
"viimistlus",
"aasta",
"Siseviimistlus Tallinnas.",
1028
],
[
"f-gardona",
"viimistlus",
"riba",
"Remonditööd Harjumaal.",
1029
],
[
"f-ramle-grupp",
"viimistlus",
"print",
"Siseviimistlus Pärnumaal.",
1030
],
[
"f-lentsius-design",
"viimistlus",
"kaar",
"Plaatimine ja põrandad Tartus.",
1031
],
[
"f-sikifest",
"viimistlus",
"taust",
"Siseviimistlus Jõgevamaal.",
1032
],
[
"f-stockton-ehitus",
"viimistlus",
"kolm",
"Remonditööd Saaremaal.",
1033
],
[
"f-silproff",
"viimistlus",
"kaart",
"Siseviimistlus Pärnus.",
1034
],
[
"f-karp-grupp",
"viimistlus",
"diag",
"Remonditööd Tallinnas.",
1035
],
[
"f-denisen-group",
"viimistlus",
"raam",
"Plaatimine ja põrandad Ida-Virumaal.",
1036
],
[
"f-kv-build",
"viimistlus",
"ring",
"Remonditööd Harjumaal.",
1037
],
[
"f-vennad-pressid",
"viimistlus",
"duo",
"Siseviimistlus Pärnus.",
1038
],
[
"f-greetel-eb",
"viimistlus",
"pool",
"Plaatimine ja põrandad Harjumaal.",
1039
],
[
"f-akj-ehitus",
"viimistlus",
"aasta",
"Värvimistööd Tallinnas.",
1040
],
[
"f-lucamoka",
"viimistlus",
"riba",
"Remonditööd Saaremaal.",
1041
],
[
"f-trl-2",
"viimistlus",
"print",
"Siseviimistlus Viljandimaal.",
1042
],
[
"f-vitroal",
"viimistlus",
"kaar",
"Remonditööd Tallinnas.",
1043
],
[
"f-umar-ruum",
"viimistlus",
"taust",
"Siseviimistlus Tallinnas.",
1044
],
[
"f-flex-interior",
"viimistlus",
"kolm",
"Remonditööd Tallinnas.",
1045
],
[
"f-marmar-design",
"viimistlus",
"kaart",
"Siseviimistlus Harjumaal.",
1046
],
[
"f-alsin",
"viimistlus",
"diag",
"Remonditööd Tallinnas.",
1047
],
[
"f-endo-viimistlus",
"viimistlus",
"raam",
"Krohvi- ja pahtlitööd Tallinnas.",
1048
],
[
"f-vertical-plus",
"viimistlus",
"ring",
"Värvimistööd Tallinnas.",
1049
],
[
"f-gabmar",
"viimistlus",
"duo",
"Siseviimistlus Tartus.",
1050
],
[
"f-inoutik",
"viimistlus",
"pool",
"Remonditööd Tallinnas.",
1051
],
[
"f-viskon-ehitus",
"viimistlus",
"aasta",
"Siseviimistlus Tartus.",
1052
],
[
"f-bajadera-renover",
"viimistlus",
"riba",
"Remonditööd Tallinnas.",
1053
],
[
"f-forexton-ehitus",
"viimistlus",
"print",
"Siseviimistlus Raplamaal.",
1054
],
[
"f-amm-moisaehitus",
"viimistlus",
"kaar",
"Remonditööd Lääne-Virumaal.",
1055
],
[
"f-ramel-property",
"viimistlus",
"taust",
"Siseviimistlus Tallinnas.",
1056
],
[
"f-wekkan",
"viimistlus",
"kolm",
"Remonditööd Pärnus.",
1057
],
[
"f-normicon-grupp",
"viimistlus",
"kaart",
"Siseviimistlus Kohtla-Järvel.",
1058
],
[
"f-margi-kaup",
"viimistlus",
"diag",
"Remonditööd Tartus.",
1059
],
[
"f-novacolor",
"viimistlus",
"raam",
"Siseviimistlus Tallinnas.",
1060
],
[
"f-porandapro",
"viimistlus",
"ring",
"Plaatimine ja põrandad Tartus.",
1061
],
[
"f-rekum",
"viimistlus",
"duo",
"Siseviimistlus Tartus.",
1062
],
[
"f-eebria-ehitus",
"viimistlus",
"pool",
"Remonditööd Tartumaal.",
1063
],
[
"f-plekkelement",
"viimistlus",
"aasta",
"Siseviimistlus Tartus.",
1064
],
[
"f-inmico",
"viimistlus",
"riba",
"Remonditööd Tallinnas.",
1065
],
[
"f-korden-grupp",
"viimistlus",
"print",
"Siseviimistlus Tallinnas.",
1066
],
[
"f-emerald-viimistlus",
"viimistlus",
"kaar",
"Remonditööd Tallinnas.",
1067
],
[
"f-tookontor",
"viimistlus",
"taust",
"Plaatimine ja põrandad Tartumaal.",
1068
],
[
"f-jd-projekt",
"viimistlus",
"kolm",
"Remonditööd Pärnus.",
1069
],
[
"f-ht-partnerid",
"viimistlus",
"kaart",
"Siseviimistlus Saaremaal.",
1070
],
[
"f-peipsi-ehitus",
"viimistlus",
"diag",
"Remonditööd Jõgevamaal.",
1071
],
[
"f-turges-grupp",
"viimistlus",
"raam",
"Plaatimine ja põrandad Tallinnas.",
1072
],
[
"f-dedmoros",
"viimistlus",
"ring",
"Plaatimine ja põrandad Tallinnas.",
1073
],
[
"f-mikote",
"viimistlus",
"duo",
"Siseviimistlus Pärnus.",
1074
],
[
"f-marendow",
"viimistlus",
"pool",
"Remonditööd Pärnus.",
1075
],
[
"f-altea-grupp",
"viimistlus",
"aasta",
"Siseviimistlus Harjumaal.",
1076
],
[
"f-kapral",
"viimistlus",
"riba",
"Remonditööd Haapsalus.",
1077
],
[
"f-bg-aatonen",
"viimistlus",
"print",
"Värvimistööd Tallinnas.",
1078
],
[
"f-pinzel",
"viimistlus",
"kaar",
"Värvimistööd Lääne-Virumaal.",
1079
],
[
"f-wolfer",
"auto",
"taust",
"Autoremont Tartus.",
1080
],
[
"f-carrem",
"auto",
"kolm",
"Auto hooldus ja remont Pärnus.",
1081
],
[
"f-kgn-oja-auto",
"auto",
"kaart",
"Hooldus ja diagnostika Haapsalus.",
1082
],
[
"f-ab-mehanic",
"auto",
"diag",
"Teie auto remont Tallinnas.",
1083
],
[
"f-dpl-service",
"auto",
"raam",
"Autoremont Tallinnas.",
1084
],
[
"f-veolab-repairs",
"auto",
"ring",
"Auto hooldus ja remont Tallinnas.",
1085
],
[
"f-caroffice",
"auto",
"duo",
"Hooldus ja diagnostika Tallinnas.",
1086
],
[
"f-evetom-group-ou",
"auto",
"pool",
"Teie auto remont Viljandimaal.",
1087
],
[
"f-autohooldusspets",
"auto",
"aasta",
"Autoremont Pärnus.",
1088
],
[
"f-ambiger",
"auto",
"riba",
"Auto hooldus ja remont Harjumaal.",
1089
],
[
"f-seersant-m-a",
"auto",
"print",
"Hooldus ja diagnostika Raplamaal.",
1090
],
[
"f-jaanuse-autoremont",
"auto",
"kaar",
"Teie auto remont Pärnus.",
1091
],
[
"f-caramelo",
"auto",
"taust",
"Autoremont Ida-Virumaal.",
1092
],
[
"f-stop-fix",
"auto",
"kolm",
"Auto hooldus ja remont Harjumaal.",
1093
],
[
"f-sektoil",
"auto",
"kaart",
"Hooldus ja diagnostika Tallinnas.",
1094
],
[
"f-aac-ferdinand",
"auto",
"diag",
"Teie auto remont Tallinnas.",
1095
],
[
"f-kiilaka-autod",
"auto",
"raam",
"Autoremont Tartumaal.",
1096
],
[
"f-maxcar-service",
"auto",
"duo",
"Hooldus ja diagnostika Tallinnas.",
1098
],
[
"f-tm-hooldusgrupp",
"auto",
"aasta",
"Autoremont Valgamaal.",
1100
],
[
"f-a-urva",
"auto",
"riba",
"Auto hooldus ja remont Harjumaal.",
1101
],
[
"f-naki-auto",
"auto",
"print",
"Hooldus ja diagnostika Tartumaal.",
1102
],
[
"f-kiire-tehnoabi",
"auto",
"kaar",
"Teie auto remont Pärnus.",
1103
],
[
"f-palmere-projekt",
"auto",
"taust",
"Autoremont Tartus.",
1104
],
[
"f-vvs-motors",
"auto",
"kaart",
"Hooldus ja diagnostika Tartumaal.",
1106
],
[
"f-wash-fly",
"auto-detail",
"diag",
"Auto puhastus Harjumaal.",
1107
],
[
"f-pt-auto",
"auto",
"raam",
"Autoremont Võrus.",
1108
],
[
"f-a-k-autoproff",
"auto",
"ring",
"Auto hooldus ja remont Tartumaal.",
1109
],
[
"f-woodrock",
"auto",
"duo",
"Hooldus ja diagnostika Tartus.",
1110
],
[
"f-vilikas",
"auto",
"pool",
"Teie auto remont Raplamaal.",
1111
],
[
"f-mrem",
"auto",
"aasta",
"Autoremont Lääne-Virumaal.",
1112
],
[
"f-js-auto",
"auto",
"riba",
"Auto hooldus ja remont Pärnus.",
1113
],
[
"f-tehnitek",
"auto",
"print",
"Hooldus ja diagnostika Võrumaal.",
1114
],
[
"f-infomar",
"auto",
"kaar",
"Teie auto remont Tallinnas.",
1115
],
[
"f-palmeren",
"auto",
"kolm",
"Auto hooldus ja remont Tallinnas.",
1117
],
[
"f-tb-garage",
"auto",
"kaart",
"Hooldus ja diagnostika Järvamaal.",
1118
],
[
"f-limmotors",
"auto",
"diag",
"Teie auto remont Pärnumaal.",
1119
],
[
"f-tuuniks",
"auto",
"raam",
"Autoremont Tartus.",
1120
],
[
"f-oilshop",
"auto",
"ring",
"Auto hooldus ja remont Harjumaal.",
1121
],
[
"f-quickquality",
"auto",
"duo",
"Hooldus ja diagnostika Maardus.",
1122
],
[
"f-anipar",
"auto",
"pool",
"Teie auto remont Põlvamaal.",
1123
],
[
"f-ankon-autoremont",
"auto",
"aasta",
"Autoremont Tallinnas.",
1124
],
[
"f-remhool",
"auto",
"riba",
"Auto hooldus ja remont Tartumaal.",
1125
],
[
"f-gekkon-service",
"auto",
"print",
"Hooldus ja diagnostika Tallinnas.",
1126
],
[
"f-edroc",
"auto",
"kaar",
"Teie auto remont Tartus.",
1127
],
[
"f-metcars",
"auto",
"kolm",
"Auto hooldus ja remont Tallinnas.",
1129
],
[
"f-judikon",
"auto",
"kaart",
"Hooldus ja diagnostika Narvas.",
1130
],
[
"f-rl-eriteenused",
"auto",
"diag",
"Teie auto remont Hiiumaal.",
1131
],
[
"f-ads-auto",
"auto",
"raam",
"Autoremont Harjumaal.",
1132
],
[
"f-aalux-rehvid-tallinn",
"auto-rehv",
"ring",
"Rehvitööd Viljandis.",
1133
],
[
"f-dentremoval",
"auto",
"pool",
"Teie auto remont Keilas.",
1135
],
[
"f-kliimamv",
"auto",
"aasta",
"Autoremont Valgamaal.",
1136
],
[
"f-motomeka-racing",
"auto",
"riba",
"Auto hooldus ja remont Pärnumaal.",
1137
],
[
"f-kenart",
"auto",
"print",
"Hooldus ja diagnostika Harjumaal.",
1138
],
[
"f-topservis-eesti",
"auto",
"kaar",
"Teie auto remont Maardus.",
1139
],
[
"f-altovega",
"auto",
"taust",
"Autoremont Harjumaal.",
1140
],
[
"f-alex-car",
"auto",
"kolm",
"Auto hooldus ja remont Tallinnas.",
1141
],
[
"f-maximar",
"auto",
"kaart",
"Hooldus ja diagnostika Valgas.",
1142
],
[
"f-sniros",
"auto",
"diag",
"Teie auto remont Ida-Virumaal.",
1143
],
[
"f-diserv",
"auto",
"raam",
"Autoremont Tallinnas.",
1144
],
[
"f-sipcam-grupp",
"auto",
"ring",
"Auto hooldus ja remont Tallinnas.",
1145
],
[
"f-pro-r-service",
"auto",
"duo",
"Hooldus ja diagnostika Tartumaal.",
1146
],
[
"f-jarem",
"auto",
"pool",
"Teie auto remont Kuressaares.",
1147
],
[
"f-ankrolo",
"auto",
"aasta",
"Autoremont Võrus.",
1148
],
[
"f-autotehnik-grupp",
"auto",
"riba",
"Auto hooldus ja remont Lääne-Virumaal.",
1149
],
[
"f-heiman-point",
"auto",
"print",
"Hooldus ja diagnostika Tartus.",
1150
],
[
"f-metwerk",
"auto",
"kaar",
"Teie auto remont Tallinnas.",
1151
],
[
"f-leritax",
"auto",
"taust",
"Autoremont Tallinnas.",
1152
],
[
"f-2a-motors",
"auto",
"kolm",
"Auto hooldus ja remont Viljandimaal.",
1153
],
[
"f-pavlocar",
"auto",
"kaart",
"Hooldus ja diagnostika Kohtla-Järvel.",
1154
],
[
"f-raimer",
"auto",
"diag",
"Teie auto remont Pärnus.",
1155
],
[
"f-d-p-c",
"toru",
"raam",
"Küte ja ventilatsioon Viljandimaal.",
1156
],
[
"f-j-toru",
"toru",
"ring",
"Santehnik Tallinnas.",
1157
],
[
"f-oo-projekt",
"toru-ahi",
"duo",
"Ahjud ja kaminad Saaremaal.",
1158
],
[
"f-tallenfix",
"toru",
"pool",
"Torutööd Hiiumaal.",
1159
],
[
"f-r-k-santehnika",
"toru",
"aasta",
"Torutööd Pärnus.",
1160
],
[
"f-wasser-graft",
"toru",
"riba",
"Küttetööd Ida-Virumaal.",
1161
],
[
"f-sonatec",
"toru",
"print",
"Küte ja ventilatsioon Tallinnas.",
1162
],
[
"f-tor-rem",
"toru",
"kaar",
"Santehnik Lääne-Virumaal.",
1163
],
[
"f-repairsystem",
"toru",
"taust",
"Ventilatsioon Tallinnas.",
1164
],
[
"f-apkures-sistemas",
"toru",
"kolm",
"Küttetööd Tallinnas.",
1165
],
[
"f-kuttekutt",
"toru",
"kaart",
"Küte ja ventilatsioon Sauel.",
1166
],
[
"f-aintor",
"toru",
"diag",
"Torutööd Pärnumaal.",
1167
],
[
"f-3d-vent",
"toru",
"raam",
"Ventilatsioon Tallinnas.",
1168
],
[
"f-pipe-welders",
"toru",
"ring",
"Torutööd Ida-Virumaal.",
1169
],
[
"f-pottseppa-teenused",
"toru-ahi",
"duo",
"Ahjud ja kaminad Tartus.",
1170
],
[
"f-nativo",
"toru",
"pool",
"Torutööd Tallinnas.",
1171
],
[
"f-svn-teh",
"toru",
"aasta",
"Torutööd Tallinnas.",
1172
],
[
"f-asmek",
"toru",
"riba",
"Küttetööd Tallinnas.",
1173
],
[
"f-reito",
"toru",
"print",
"Torutööd ja küte Viljandimaal.",
1174
],
[
"f-jknomar",
"toru",
"kaar",
"Küttetööd Harjumaal.",
1175
],
[
"f-gaasitoode-remondi",
"toru",
"taust",
"Küte ja ventilatsioon Tallinnas.",
1176
],
[
"f-profigrupp",
"toru",
"kolm",
"Torutööd Tallinnas.",
1177
],
[
"f-torusell1",
"toru",
"kaart",
"Torutööd Tallinnas.",
1178
],
[
"f-hiiter-r",
"toru-ahi",
"diag",
"Pottsepatööd Põlvas.",
1179
],
[
"f-soojemaks",
"toru",
"raam",
"Torutööd ja küte Tartumaal.",
1180
],
[
"f-nordicvent",
"toru",
"ring",
"Ventilatsioonitööd Tartus.",
1181
],
[
"f-mims",
"toru",
"duo",
"Torutööd Pärnus.",
1182
],
[
"f-a-kamin",
"toru-ahi",
"pool",
"Pottsepatööd Harjumaal.",
1183
],
[
"f-alfamarket",
"toru",
"aasta",
"Küte ja ventilatsioon Harjumaal.",
1184
],
[
"f-fomad-heat",
"toru-kliima",
"riba",
"Kliimaseadmed Narvas.",
1185
],
[
"f-bio-ehitus-grupp",
"toru",
"print",
"Torutööd ja küte Tallinnas.",
1186
],
[
"f-sanmaag",
"toru",
"kaar",
"Santehnik Valgamaal.",
1187
],
[
"f-kulmaservis",
"toru",
"taust",
"Küte ja ventilatsioon Tartus.",
1188
],
[
"f-tsitrale",
"toru",
"kolm",
"Küttetööd Tallinnas.",
1189
],
[
"f-nordtrend",
"toru",
"kaart",
"Torutööd ja küte Tallinnas.",
1190
],
[
"f-elbrus-teenindus",
"toru",
"diag",
"Santehnik Narvas.",
1191
],
[
"f-johel-grupp",
"toru",
"raam",
"Torutööd Valgas.",
1192
],
[
"f-puller-projekt",
"toru",
"ring",
"Küttetööd Harjumaal.",
1193
],
[
"f-re-valvesusteemid",
"toru",
"duo",
"Küte ja ventilatsioon Tartus.",
1194
],
[
"f-sollers-grupp",
"toru",
"pool",
"Santehnik Harjumaal.",
1195
],
[
"f-devas",
"toru",
"aasta",
"Küte ja ventilatsioon Harjumaal.",
1196
],
[
"f-baseterm",
"toru",
"riba",
"Santehnik Maardus.",
1197
],
[
"f-kunikramos",
"toru",
"print",
"Torutööd Tallinnas.",
1198
],
[
"f-air-glace",
"toru",
"kaar",
"Ventilatsioonitööd Tallinnas.",
1199
],
[
"f-luxtor",
"toru",
"taust",
"Torutööd Valgas.",
1200
],
[
"f-dicable",
"elekter",
"kolm",
"Elektrik Kohtla-Järvel.",
1201
],
[
"f-sveol",
"elekter",
"kaart",
"Elektripaigaldus Tallinnas.",
1202
],
[
"f-dksenergy",
"elekter",
"diag",
"Elektritööd Tallinnas.",
1203
],
[
"f-relagus",
"elekter",
"raam",
"Elektrik Harjumaal.",
1204
],
[
"f-autelsig",
"elekter",
"ring",
"Elektripaigaldus Viljandimaal.",
1205
],
[
"f-eldimar",
"elekter",
"duo",
"Elektritööd Narvas.",
1206
],
[
"f-systex",
"elekter",
"pool",
"Elektrik Tallinnas.",
1207
],
[
"f-ll-ks-grupp",
"elekter",
"aasta",
"Elektripaigaldus Jõgeval.",
1208
],
[
"f-evemar-plus",
"elekter",
"print",
"Elektrik Pärnus.",
1210
],
[
"f-elship",
"elekter",
"kaar",
"Elektripaigaldus Viljandis.",
1211
],
[
"f-gnova",
"elekter",
"kolm",
"Elektrik Maardus.",
1213
],
[
"f-signaal-r",
"elekter",
"kaart",
"Elektripaigaldus Põlvamaal.",
1214
],
[
"f-samara-group",
"elekter",
"diag",
"Elektritööd Tallinnas.",
1215
],
[
"f-vorguhaldus",
"elekter",
"raam",
"Elektrik Harjumaal.",
1216
],
[
"f-arolux",
"elekter",
"ring",
"Elektripaigaldus Tallinnas.",
1217
],
[
"f-heilhard-elekter",
"elekter",
"duo",
"Elektritööd Tartus.",
1218
],
[
"f-u-k-v-grupp",
"elekter",
"pool",
"Elektrik Lääne-Virumaal.",
1219
],
[
"f-railona-elekter",
"elekter",
"aasta",
"Elektripaigaldus Haapsalus.",
1220
],
[
"f-guardtech",
"elekter",
"riba",
"Elektritööd Rakveres.",
1221
],
[
"f-hericom-projekt",
"elekter",
"print",
"Elektrik Viljandimaal.",
1222
],
[
"f-raimaste-sarts",
"elekter",
"kaar",
"Elektripaigaldus Saaremaal.",
1223
],
[
"f-flerko",
"elekter",
"taust",
"Elektritööd Tallinnas.",
1224
],
[
"f-kaablijuku",
"elekter",
"kolm",
"Elektrik Ida-Virumaal.",
1225
],
[
"f-videocom",
"elekter",
"kaart",
"Elektripaigaldus Maardus.",
1226
],
[
"f-elravel",
"elekter",
"diag",
"Elektritööd Tartus.",
1227
],
[
"f-stelmars",
"elekter",
"raam",
"Elektrik Tallinnas.",
1228
],
[
"f-vidantel-group",
"elekter",
"ring",
"Elektripaigaldus Tallinnas.",
1229
],
[
"f-lemarx-group",
"elekter",
"duo",
"Elektritööd Tartus.",
1230
],
[
"f-adapter-grupp",
"elekter",
"pool",
"Elektrik Pärnus.",
1231
],
[
"f-sahko-are",
"elekter",
"aasta",
"Elektripaigaldus Tallinnas.",
1232
],
[
"f-vektrus",
"elekter",
"riba",
"Elektritööd Tallinnas.",
1233
],
[
"f-ideamill",
"elekter",
"print",
"Elektrik Tallinnas.",
1234
],
[
"f-aak-elekter",
"elekter",
"kaar",
"Elektripaigaldus Tallinnas.",
1235
],
[
"f-artalina-grupp",
"elekter",
"taust",
"Elektritööd Kohtla-Järvel.",
1236
],
[
"f-interpartner",
"elekter",
"kolm",
"Elektrik Pärnus.",
1237
],
[
"f-vooluvark",
"elekter",
"kaart",
"Elektripaigaldus Viljandis.",
1238
],
[
"f-vgoneup",
"elekter",
"diag",
"Elektritööd Pärnus.",
1239
],
[
"f-elgrand-elekter",
"elekter",
"raam",
"Elektrik Tallinnas.",
1240
],
[
"f-svelec",
"elekter",
"ring",
"Elektripaigaldus Tallinnas.",
1241
],
[
"f-haru-elekter",
"elekter",
"duo",
"Elektritööd Tallinnas.",
1242
],
[
"f-hektali",
"elekter",
"pool",
"Elektrik Lääne-Virumaal.",
1243
],
[
"f-spike-systems",
"elekter",
"aasta",
"Elektripaigaldus Harjumaal.",
1244
],
[
"f-avido",
"juuksur",
"riba",
"Juuksur Jõgevamaal.",
1245
],
[
"f-smb-firma",
"juuksur",
"print",
"Juuksurisalong Ida-Virumaal.",
1246
],
[
"f-vagantos",
"juuksur",
"kaar",
"Soengud ja värvid Jõgevamaal.",
1247
],
[
"f-rosamahe",
"juuksur",
"taust",
"Juuksur Tallinnas.",
1248
],
[
"f-navy-moon",
"juuksur",
"kolm",
"Juuksurisalong Tallinnas.",
1249
],
[
"f-sarah-iluustudio",
"juuksur",
"kaart",
"Soengud ja värvid Tallinnas.",
1250
],
[
"f-pinkpink",
"juuksur",
"diag",
"Juuksur Tallinnas.",
1251
],
[
"f-tukad-viltu",
"juuksur",
"raam",
"Juuksurisalong Tallinnas.",
1252
],
[
"f-scopo",
"juuksur",
"ring",
"Soengud ja värvid Tallinnas.",
1253
],
[
"f-meryl",
"juuksur",
"duo",
"Juuksur Tallinnas.",
1254
],
[
"f-cesario",
"juuksur",
"pool",
"Juuksurisalong Tallinnas.",
1255
],
[
"f-jolanta",
"juuksur",
"aasta",
"Soengud ja värvid Tallinnas.",
1256
],
[
"f-duvalje-style",
"juuksur",
"riba",
"Juuksur Tallinnas.",
1257
],
[
"f-d-soul",
"juuksur",
"print",
"Juuksurisalong Maardus.",
1258
],
[
"f-john-doe-barbershop",
"juuksur-m",
"kaar",
"Juukselõikus ja habe Tallinnas.",
1259
],
[
"f-margitabarber",
"juuksur-m",
"taust",
"Meeste juuksur Valgas.",
1260
],
[
"f-viola-prof",
"juuksur",
"kolm",
"Juuksurisalong Kohtla-Järvel.",
1261
],
[
"f-hn-beauty",
"juuksur",
"kaart",
"Soengud ja värvid Tallinnas.",
1262
],
[
"f-kingmoor",
"juuksur",
"diag",
"Juuksur Tallinnas.",
1263
],
[
"f-sirke",
"juuksur",
"raam",
"Juuksurisalong Lääne-Virumaal.",
1264
],
[
"f-sakura-ilusalon",
"juuksur",
"ring",
"Soengud ja värvid Kohtla-Järvel.",
1265
],
[
"f-jaama-juuksur",
"juuksur",
"duo",
"Juuksur Tartumaal.",
1266
],
[
"f-hasso-t",
"juuksur",
"pool",
"Juuksurisalong Tallinnas.",
1267
],
[
"f-kkrs",
"juuksur",
"aasta",
"Soengud ja värvid Tallinnas.",
1268
],
[
"f-snip-snip",
"juuksur",
"riba",
"Juuksur Tallinnas.",
1269
],
[
"f-natehair",
"juuksur",
"print",
"Juuksurisalong Kohtla-Järvel.",
1270
],
[
"f-juuksur-innake",
"juuksur",
"kaar",
"Soengud ja värvid Lääne-Virumaal.",
1271
],
[
"f-emfplace",
"juuksur",
"taust",
"Juuksur Tallinnas.",
1272
],
[
"f-kamoon",
"juuksur",
"kolm",
"Juuksurisalong Tartumaal.",
1273
],
[
"f-judream-ilusalong",
"juuksur",
"kaart",
"Soengud ja värvid Pärnus.",
1274
],
[
"f-r-hair-room",
"juuksur",
"diag",
"Juuksur Tallinnas.",
1275
],
[
"f-kamm-ja-foon",
"juuksur",
"raam",
"Juuksurisalong Maardus.",
1276
],
[
"f-beauty-cosmetics",
"juuksur",
"ring",
"Soengud ja värvid Võrus.",
1277
],
[
"f-regalgold-beauty",
"juuksur",
"duo",
"Juuksur Tallinnas.",
1278
],
[
"f-signe-juuksla",
"juuksur",
"pool",
"Juuksurisalong Tallinnas.",
1279
],
[
"f-kasnel",
"juuksur",
"aasta",
"Soengud ja värvid Harjumaal.",
1280
],
[
"f-tiisk-haldus",
"juuksur",
"riba",
"Juuksur Harjumaal.",
1281
],
[
"f-rebreymz",
"juuksur",
"print",
"Juuksurisalong Pärnus.",
1282
],
[
"f-beauty-alley",
"juuksur",
"kaar",
"Soengud ja värvid Tallinnas.",
1283
],
[
"f-salandra",
"juuksur",
"taust",
"Juuksur Tallinnas.",
1284
],
[
"f-ilusalong-lilia",
"juuksur",
"kolm",
"Juuksurisalong Tallinnas.",
1285
],
[
"f-gardiner-grupp",
"juuksur",
"kaart",
"Soengud ja värvid Tallinnas.",
1286
],
[
"f-triokump",
"juuksur",
"diag",
"Juuksur Raplamaal.",
1287
],
[
"f-temper-hair",
"juuksur",
"raam",
"Juuksurisalong Tallinnas.",
1288
],
[
"f-chrissu-haldus",
"koristus",
"duo",
"Koristus Raplamaal.",
1290
],
[
"f-aljastek",
"koristus",
"pool",
"Puhastusteenused Lääne-Virumaal.",
1291
],
[
"f-mi-mia-maid",
"koristus",
"aasta",
"Koristus Tartumaal.",
1292
],
[
"f-emd-ehitus",
"koristus",
"riba",
"Puhastusteenused Ida-Virumaal.",
1293
],
[
"f-mentorplus",
"koristus",
"print",
"Koristus Tallinnas.",
1294
],
[
"f-silvoran",
"koristus",
"kaar",
"Puhastusteenused Tallinnas.",
1295
],
[
"f-amr-clean",
"koristus",
"taust",
"Koristus Tallinnas.",
1296
],
[
"f-skills-factory",
"koristus",
"kolm",
"Puhastusteenused Narvas.",
1297
],
[
"f-ventiflow",
"koristus",
"kaart",
"Koristus Tallinnas.",
1298
],
[
"f-just-worker",
"koristus",
"diag",
"Puhastusteenused Tallinnas.",
1299
],
[
"f-briljantne-kasi",
"koristus",
"raam",
"Koristus Tallinnas.",
1300
],
[
"f-siniar-puhastus",
"koristus",
"ring",
"Puhastusteenused Harjumaal.",
1301
],
[
"f-shikan-taza",
"koristus",
"duo",
"Koristus Tallinnas.",
1302
],
[
"f-koristamine24",
"koristus",
"pool",
"Puhastusteenused Tallinnas.",
1303
],
[
"f-ronlin",
"koristus",
"aasta",
"Koristus Raplamaal.",
1304
],
[
"f-puhas-teenus",
"koristus",
"riba",
"Puhastusteenused Tallinnas.",
1305
],
[
"f-gt-solutions",
"koristus",
"print",
"Koristus Tallinnas.",
1306
],
[
"f-m-r-cleaning-team",
"koristus",
"kaar",
"Puhastusteenused Kuressaares.",
1307
],
[
"f-elegantico",
"koristus",
"taust",
"Koristus Tartumaal.",
1308
],
[
"f-5-nordik",
"koristus",
"kolm",
"Puhastusteenused Tallinnas.",
1309
],
[
"f-andraun-teenused",
"koristus",
"kaart",
"Koristus Haapsalus.",
1310
],
[
"f-simple-clean",
"koristus",
"diag",
"Puhastusteenused Tallinnas.",
1311
],
[
"f-vihmavarju",
"koristus",
"raam",
"Koristus Rakveres.",
1312
],
[
"f-catalia-cleaning",
"koristus",
"ring",
"Puhastusteenused Tallinnas.",
1313
],
[
"f-korstnatood",
"koristus",
"duo",
"Koristus Tartus.",
1314
],
[
"f-tuffel",
"koristus",
"pool",
"Puhastusteenused Sauel.",
1315
],
[
"f-sofie-haldus",
"koristus",
"riba",
"Puhastusteenused Raplamaal.",
1317
],
[
"f-caliber-partner",
"koristus",
"print",
"Koristus Harjumaal.",
1318
],
[
"f-ikpuhastus",
"koristus",
"kaar",
"Puhastusteenused Tallinnas.",
1319
],
[
"f-riverside-grupp",
"koristus",
"taust",
"Koristus Maardus.",
1320
],
[
"f-maria-fatima-cleaning-services",
"koristus",
"kolm",
"Puhastusteenused Tallinnas.",
1321
],
[
"f-red-heather",
"koristus",
"kaart",
"Koristus Tallinnas.",
1322
],
[
"f-excavart",
"kaeve",
"diag",
"Pinnasetööd Harjumaal.",
1323
],
[
"f-aarna-ettevotmised",
"kaeve",
"raam",
"Kaevetööd Põlvamaal.",
1324
],
[
"f-aasakas",
"kaeve",
"ring",
"Pinnasetööd Pärnus.",
1325
],
[
"f-taixon",
"kaeve",
"duo",
"Kaevetööd Võrumaal.",
1326
],
[
"f-kaeve3d",
"kaeve",
"pool",
"Pinnasetööd Tartumaal.",
1327
],
[
"f-forest-haldus",
"kaeve",
"aasta",
"Kaevetööd Võrumaal.",
1328
],
[
"f-rrk-kase",
"kaeve",
"riba",
"Pinnasetööd Jõgevamaal.",
1329
],
[
"f-bialex-ehitus",
"kaeve",
"print",
"Kaevetööd Tallinnas.",
1330
],
[
"f-demlak",
"kaeve",
"kaar",
"Pinnasetööd Jõgeval.",
1331
],
[
"f-kaever",
"kaeve",
"taust",
"Kaevetööd Tartumaal.",
1332
],
[
"f-marruskop",
"kaeve",
"kolm",
"Pinnasetööd Harjumaal.",
1333
],
[
"f-janrimar",
"kaeve",
"kaart",
"Kaevetööd Lääne-Virumaal.",
1334
],
[
"f-hipodroomi-tehnika",
"kaeve",
"diag",
"Pinnasetööd Tartus.",
1335
],
[
"f-kapp-ja-pojad",
"kaeve",
"raam",
"Kaevetööd Tartumaal.",
1336
],
[
"f-rvs-grupp",
"kaeve",
"ring",
"Pinnasetööd Ida-Virumaal.",
1337
],
[
"f-tariko",
"kaeve",
"duo",
"Kaevetööd Pärnumaal.",
1338
],
[
"f-reimus",
"kaeve",
"pool",
"Pinnasetööd Võrumaal.",
1339
],
[
"f-ristallika",
"kaeve",
"aasta",
"Kaevetööd Harjumaal.",
1340
],
[
"f-summergold",
"haljastus",
"riba",
"Aiatööd Harjumaal.",
1341
],
[
"f-kivila-aiad",
"haljastus",
"print",
"Haljastus ja aiatööd Raplamaal.",
1342
],
[
"f-puuspetsialist",
"haljastus",
"kaar",
"Aiatööd Kuressaares.",
1343
],
[
"f-setwell",
"haljastus",
"taust",
"Haljastus ja aiatööd Läänemaal.",
1344
],
[
"f-muraste-hooldus",
"haljastus",
"kolm",
"Aiatööd Harjumaal.",
1345
],
[
"f-tomzter",
"haljastus",
"kaart",
"Haljastus ja aiatööd Tallinnas.",
1346
],
[
"f-baustein",
"haljastus",
"diag",
"Aiatööd Lääne-Virumaal.",
1347
],
[
"f-vassjok",
"haljastus",
"raam",
"Haljastus ja aiatööd Võrumaal.",
1348
],
[
"f-green-express",
"haljastus",
"ring",
"Aiatööd Sauel.",
1349
],
[
"f-kaldes",
"haljastus",
"duo",
"Haljastus ja aiatööd Jõgeval.",
1350
],
[
"f-kp-teehooldus",
"haljastus",
"pool",
"Aiatööd Tartumaal.",
1351
],
[
"f-raixla",
"viimistlus",
"aasta",
"Siseviimistlus Järvamaal.",
1352
],
[
"f-kadrioru-ehitus",
"viimistlus",
"riba",
"Remonditööd Tallinnas.",
1353
],
[
"f-kestev-porand",
"viimistlus",
"print",
"Plaatimine ja põrandad Tartumaal.",
1354
],
[
"f-rand-partnerid",
"viimistlus",
"kaar",
"Värvimistööd Pärnus.",
1355
],
[
"f-renovest",
"viimistlus",
"taust",
"Siseviimistlus Pärnus.",
1356
],
[
"f-katoparquet",
"viimistlus",
"kolm",
"Plaatimine ja põrandad Tallinnas.",
1357
],
[
"f-kuldmar-grupp",
"viimistlus",
"kaart",
"Siseviimistlus Lääne-Virumaal.",
1358
],
[
"f-svaor",
"viimistlus",
"diag",
"Remonditööd Pärnus.",
1359
],
[
"f-mvv-plast",
"viimistlus",
"raam",
"Siseviimistlus Tallinnas.",
1360
],
[
"f-maaks",
"viimistlus",
"ring",
"Remonditööd Pärnumaal.",
1361
],
[
"f-trigmus",
"viimistlus",
"duo",
"Siseviimistlus Tartus.",
1362
],
[
"f-timkin",
"viimistlus",
"pool",
"Remonditööd Tallinnas.",
1363
],
[
"f-ledarel",
"viimistlus",
"aasta",
"Siseviimistlus Tallinnas.",
1364
],
[
"f-a-n-k-grupp",
"auto",
"riba",
"Auto hooldus ja remont Tartumaal.",
1365
],
[
"f-elt24",
"auto",
"print",
"Hooldus ja diagnostika Narvas.",
1366
],
[
"f-tige-mutter",
"auto",
"kaar",
"Teie auto remont Tartus.",
1367
],
[
"f-someru-rehvikoda",
"auto-rehv",
"taust",
"Rehvivahetus Lääne-Virumaal.",
1368
],
[
"f-estakada-auto",
"auto",
"kolm",
"Auto hooldus ja remont Narvas.",
1369
],
[
"f-sihvercar",
"auto",
"kaart",
"Hooldus ja diagnostika Viljandimaal.",
1370
],
[
"f-b-motors-group",
"auto",
"diag",
"Teie auto remont Tallinnas.",
1371
],
[
"f-scapino",
"auto",
"raam",
"Autoremont Jõgevamaal.",
1372
],
[
"f-trailer-control",
"auto",
"ring",
"Auto hooldus ja remont Tallinnas.",
1373
],
[
"f-mustrem",
"auto",
"duo",
"Hooldus ja diagnostika Jõgevamaal.",
1374
],
[
"f-huntal-auto",
"auto",
"pool",
"Teie auto remont Pärnumaal.",
1375
],
[
"f-purgatory",
"auto",
"aasta",
"Autoremont Harjumaal.",
1376
],
[
"f-aumarks-service",
"auto",
"riba",
"Auto hooldus ja remont Tallinnas.",
1377
],
[
"f-kabros",
"auto",
"print",
"Hooldus ja diagnostika Raplamaal.",
1378
],
[
"f-dl-racing",
"auto",
"kaar",
"Teie auto remont Kuressaares.",
1379
],
[
"f-reilent-keretood",
"auto",
"taust",
"Kereremont ja värvimine Ida-Virumaal.",
1380
],
[
"f-sanistor",
"toru",
"kaart",
"Torutööd Pärnumaal.",
1382
],
[
"f-semiserv",
"toru",
"diag",
"Santehnik Tallinnas.",
1383
],
[
"f-vesaro",
"toru",
"raam",
"Küte ja ventilatsioon Pärnumaal.",
1384
],
[
"f-katlaexpert",
"toru",
"ring",
"Torutööd Tallinnas.",
1385
],
[
"f-ventark",
"toru",
"duo",
"Ventilatsioon Tallinnas.",
1386
],
[
"f-veldpip",
"toru",
"pool",
"Santehnik Raplamaal.",
1387
],
[
"f-sannik-grupp",
"toru",
"aasta",
"Küte ja ventilatsioon Tallinnas.",
1388
],
[
"f-neltom",
"toru",
"riba",
"Santehnik Tartus.",
1389
],
[
"f-vaikoddala",
"toru-ahi",
"print",
"Ahjud ja kaminad Rakveres.",
1390
],
[
"f-enhotec",
"toru",
"kaar",
"Küttetööd Tallinnas.",
1391
],
[
"f-everk-ehitus",
"toru",
"taust",
"Torutööd Tallinnas.",
1392
],
[
"f-enodis",
"toru",
"kolm",
"Torutööd Tartumaal.",
1393
],
[
"f-ake-ko",
"toru",
"kaart",
"Torutööd Pärnumaal.",
1394
],
[
"f-ventpipe",
"toru",
"diag",
"Ventilatsioonitööd Viljandis.",
1395
],
[
"f-optimus-group",
"toru",
"raam",
"Torutööd Ida-Virumaal.",
1396
],
[
"f-tig-keevitus",
"toru",
"duo",
"Torutööd Tallinnas.",
1398
],
[
"f-artex-torutood",
"toru",
"pool",
"Santehnik Tartus.",
1399
],
[
"f-veering",
"toru",
"aasta",
"Torutööd Narvas.",
1400
],
[
"f-arcticmetal",
"toru",
"riba",
"Torutööd Harjumaal.",
1401
],
[
"f-gopipe",
"toru",
"print",
"Torutööd Põlvamaal.",
1402
],
[
"f-mariden-install",
"toru",
"kaar",
"Santehnik Tallinnas.",
1403
],
[
"f-jammi",
"elekter",
"taust",
"Elektritööd Võrumaal.",
1404
],
[
"f-gelora",
"elekter",
"kolm",
"Elektrik Tallinnas.",
1405
],
[
"f-elektro-mir",
"elekter",
"kaart",
"Elektripaigaldus Tallinnas.",
1406
],
[
"f-dm-system",
"elekter",
"diag",
"Elektritööd Tallinnas.",
1407
],
[
"f-kingu-elekter",
"elekter",
"raam",
"Elektrik Viljandimaal.",
1408
],
[
"f-ler-elekter",
"elekter",
"ring",
"Elektripaigaldus Tallinnas.",
1409
],
[
"f-is-projekt",
"elekter",
"duo",
"Elektritööd Viljandis.",
1410
],
[
"f-helek",
"elekter",
"pool",
"Elektrik Hiiumaal.",
1411
],
[
"f-elerium",
"elekter",
"aasta",
"Elektripaigaldus Harjumaal.",
1412
],
[
"f-dp-tech-partner",
"elekter",
"print",
"Elektrik Tallinnas.",
1414
],
[
"f-e-e-toode",
"elekter",
"kaar",
"Elektripaigaldus Keilas.",
1415
],
[
"f-aufstern",
"elekter",
"taust",
"Elektritööd Tallinnas.",
1416
],
[
"f-sansound-valve",
"elekter",
"kolm",
"Elektrik Tartumaal.",
1417
],
[
"f-trebor-susteemid",
"elekter",
"kaart",
"Elektripaigaldus Tallinnas.",
1418
],
[
"f-andelekt",
"elekter",
"raam",
"Elektrik Viljandimaal.",
1420
],
[
"f-adelanta-grupp",
"elekter",
"ring",
"Elektripaigaldus Harjumaal.",
1421
],
[
"f-pinder",
"elekter",
"duo",
"Elektritööd Põlvamaal.",
1422
],
[
"f-danzer",
"elekter",
"pool",
"Elektrik Harjumaal.",
1423
],
[
"f-iks-puhastus",
"koristus",
"aasta",
"Koristus Tallinnas.",
1424
],
[
"f-powerup",
"koristus",
"riba",
"Puhastusteenused Sauel.",
1425
],
[
"f-saleprime",
"koristus",
"print",
"Koristus Tallinnas.",
1426
],
[
"f-sofren-koristus",
"koristus",
"kaar",
"Puhastusteenused Harjumaal.",
1427
],
[
"f-amanda-kv",
"koristus",
"taust",
"Koristus Tallinnas.",
1428
],
[
"f-puhastamine24-7",
"koristus",
"kolm",
"Puhastusteenused Tallinnas.",
1429
],
[
"f-blomstre",
"koristus",
"kaart",
"Koristus Tallinnas.",
1430
],
[
"f-kaunid-hetked",
"koristus",
"diag",
"Puhastusteenused Harjumaal.",
1431
],
[
"f-evidora",
"koristus",
"ring",
"Puhastusteenused Tallinnas.",
1433
],
[
"f-cleanoks",
"koristus",
"duo",
"Koristus Tallinnas.",
1434
],
[
"f-laceriik",
"koristus",
"pool",
"Puhastusteenused Tallinnas.",
1435
],
[
"f-dratsena",
"haljastus",
"riba",
"Aiatööd Ida-Virumaal.",
1437
],
[
"f-vikingworks",
"haljastus",
"print",
"Haljastus ja aiatööd Raplamaal.",
1438
],
[
"f-floratum",
"haljastus",
"kaar",
"Aiatööd Tallinnas.",
1439
],
[
"f-kurikivi",
"haljastus",
"kolm",
"Aiatööd Harjumaal.",
1441
],
[
"f-rxl",
"viimistlus",
"kaart",
"Siseviimistlus Tartumaal.",
1442
],
[
"f-marenello",
"viimistlus",
"diag",
"Remonditööd Tallinnas.",
1443
],
[
"f-greal-group",
"viimistlus",
"raam",
"Plaatimine ja põrandad Tallinnas.",
1444
],
[
"f-msfassaad",
"viimistlus",
"ring",
"Krohvi- ja pahtlitööd Tartumaal.",
1445
],
[
"f-komex-grupp",
"viimistlus",
"duo",
"Siseviimistlus Järvamaal.",
1446
],
[
"f-rainest",
"viimistlus",
"pool",
"Värvimistööd Jõgevamaal.",
1447
],
[
"f-glb-ehitus",
"viimistlus",
"aasta",
"Siseviimistlus Tallinnas.",
1448
],
[
"f-alicante",
"viimistlus",
"riba",
"Remonditööd Tartus.",
1449
],
[
"f-jaani-terp",
"viimistlus",
"print",
"Siseviimistlus Järvamaal.",
1450
],
[
"f-temano",
"viimistlus",
"kaar",
"Remonditööd Tallinnas.",
1451
],
[
"f-raveri-grupp",
"viimistlus",
"taust",
"Siseviimistlus Järvamaal.",
1452
],
[
"f-aarne-teenus",
"viimistlus",
"kolm",
"Remonditööd Jõgevamaal.",
1453
],
[
"f-tiit-grupp",
"viimistlus",
"kaart",
"Siseviimistlus Tallinnas.",
1454
],
[
"f-ando-meema",
"viimistlus",
"diag",
"Plaatimine ja põrandad Valgamaal.",
1455
],
[
"f-pisihele",
"juuksur",
"raam",
"Juuksurisalong Tallinnas.",
1456
],
[
"f-good-look",
"juuksur",
"ring",
"Soengud ja värvid Tallinnas.",
1457
],
[
"f-arete-pro",
"juuksur",
"duo",
"Juuksur Rakveres.",
1458
],
[
"f-aleros",
"juuksur",
"pool",
"Juuksurisalong Tallinnas.",
1459
],
[
"f-shekina",
"juuksur",
"aasta",
"Soengud ja värvid Harjumaal.",
1460
],
[
"f-golden-comb",
"juuksur",
"riba",
"Juuksur Tallinnas.",
1461
],
[
"f-la-hair",
"juuksur",
"print",
"Juuksurisalong Tartus.",
1462
],
[
"f-noashark",
"juuksur",
"kaar",
"Soengud ja värvid Tallinnas.",
1463
],
[
"f-ketucat",
"juuksur",
"taust",
"Juuksur Tallinnas.",
1464
],
[
"f-kristina-iluteenused",
"juuksur",
"kolm",
"Juuksurisalong Tallinnas.",
1465
],
[
"f-arismabeauty",
"juuksur",
"kaart",
"Soengud ja värvid Tallinnas.",
1466
],
[
"f-kaarmeister",
"juuksur",
"diag",
"Juuksur Tallinnas.",
1467
],
[
"f-marano-jv",
"juuksur",
"raam",
"Juuksurisalong Pärnus.",
1468
],
[
"f-nely",
"juuksur",
"ring",
"Soengud ja värvid Tallinnas.",
1469
],
[
"f-vitar",
"juuksur",
"duo",
"Juuksur Kohtla-Järvel.",
1470
],
[
"f-vm-salong",
"juuksur",
"pool",
"Juuksurisalong Tartus.",
1471
],
[
"f-sola4beauty",
"juuksur",
"aasta",
"Soengud ja värvid Tallinnas.",
1472
],
[
"f-gessuhair",
"juuksur",
"riba",
"Juuksur Võrumaal.",
1473
],
[
"f-teenindusmaja",
"juuksur",
"print",
"Juuksurisalong Läänemaal.",
1474
],
[
"f-katri-beauty",
"juuksur",
"kaar",
"Soengud ja värvid Harjumaal.",
1475
],
[
"f-chop-n-dye-stuudio",
"juuksur",
"kolm",
"Juuksurisalong Tallinnas.",
1477
],
[
"f-voiter-hair",
"juuksur",
"kaart",
"Soengud ja värvid Tartus.",
1478
],
[
"f-slione",
"juuksur",
"diag",
"Juuksur Tallinnas.",
1479
],
[
"f-holmekogrupp",
"juuksur",
"raam",
"Juuksurisalong Tallinnas.",
1480
],
[
"f-ivika-salong",
"juuksur",
"ring",
"Soengud ja värvid Valgas.",
1481
],
[
"f-tins-system",
"juuksur",
"duo",
"Juuksur Tallinnas.",
1482
],
[
"f-future-netcom",
"auto",
"pool",
"Teie auto remont Tallinnas.",
1483
],
[
"f-anet-eesti",
"auto",
"aasta",
"Autoremont Tallinnas.",
1484
],
[
"f-boswel",
"auto",
"riba",
"Auto hooldus ja remont Tallinnas.",
1485
],
[
"f-mausir",
"auto",
"print",
"Hooldus ja diagnostika Harjumaal.",
1486
],
[
"f-extrafix",
"auto",
"kaar",
"Teie auto remont Keilas.",
1487
],
[
"f-antima-autoteenindus",
"auto",
"taust",
"Autoremont Jõgeval.",
1488
],
[
"f-tapa-np",
"auto",
"kolm",
"Auto hooldus ja remont Lääne-Virumaal.",
1489
],
[
"f-orissaare-autoteenindus",
"auto",
"kaart",
"Hooldus ja diagnostika Saaremaal.",
1490
],
[
"f-parnu-autopesulad",
"auto-detail",
"diag",
"Auto puhastus Pärnus.",
1491
],
[
"f-egnet",
"auto",
"raam",
"Autoremont Tallinnas.",
1492
],
[
"f-damarine",
"viimistlus",
"ring",
"Plaatimine ja põrandad Tallinnas.",
1493
],
[
"f-plastteed",
"viimistlus",
"duo",
"Siseviimistlus Tallinnas.",
1494
],
[
"f-bravoland",
"viimistlus",
"pool",
"Remonditööd Võrumaal.",
1495
],
[
"f-andri-ehitus",
"viimistlus",
"aasta",
"Siseviimistlus Jõgeval.",
1496
],
[
"f-manweld",
"viimistlus",
"riba",
"Remonditööd Tallinnas.",
1497
],
[
"f-aafloors",
"viimistlus",
"print",
"Plaatimine ja põrandad Järvamaal.",
1498
],
[
"f-333nn",
"viimistlus",
"kaar",
"Värvimistööd Harjumaal.",
1499
],
[
"f-martens-solo",
"viimistlus",
"taust",
"Siseviimistlus Tallinnas.",
1500
],
[
"f-medellin-eesti",
"viimistlus",
"kolm",
"Remonditööd Tartumaal.",
1501
],
[
"f-visarem",
"viimistlus",
"kaart",
"Plaatimine ja põrandad Pärnus.",
1502
],
[
"f-herkize",
"viimistlus",
"diag",
"Remonditööd Harjumaal.",
1503
],
[
"f-ringo-ehitus",
"viimistlus",
"raam",
"Siseviimistlus Harjumaal.",
1504
],
[
"f-samiron-ehitus",
"viimistlus",
"duo",
"Siseviimistlus Tallinnas.",
1506
],
[
"f-colotrin",
"viimistlus",
"pool",
"Värvimistööd Saaremaal.",
1507
],
[
"f-mf-flar",
"viimistlus",
"aasta",
"Siseviimistlus Tallinnas.",
1508
],
[
"f-furn-paigaldus",
"viimistlus",
"riba",
"Remonditööd Tallinnas.",
1509
],
[
"f-kodukindlus",
"viimistlus",
"print",
"Siseviimistlus Tallinnas.",
1510
],
[
"f-kvazar-ehitus",
"viimistlus",
"kaar",
"Remonditööd Jõgevamaal.",
1511
],
[
"f-thedesigner",
"viimistlus",
"taust",
"Siseviimistlus Tallinnas.",
1512
],
[
"f-ein-ko",
"viimistlus",
"kolm",
"Remonditööd Tallinnas.",
1513
],
[
"f-kindelmeister",
"viimistlus",
"kaart",
"Siseviimistlus Harjumaal.",
1514
],
[
"f-stage-point",
"viimistlus",
"diag",
"Remonditööd Pärnumaal.",
1515
],
[
"f-fortego",
"viimistlus",
"raam",
"Plaatimine ja põrandad Tallinnas.",
1516
],
[
"f-kapri-teenus",
"viimistlus",
"ring",
"Remonditööd Tallinnas.",
1517
],
[
"f-edelon-grupp",
"viimistlus",
"duo",
"Siseviimistlus Tallinnas.",
1518
],
[
"f-vormatex",
"viimistlus",
"pool",
"Remonditööd Võrumaal.",
1519
],
[
"f-seker-ehitus",
"viimistlus",
"aasta",
"Siseviimistlus Saaremaal.",
1520
],
[
"f-jerms",
"viimistlus",
"riba",
"Plaatimine ja põrandad Harjumaal.",
1521
],
[
"f-aprov-group",
"viimistlus",
"print",
"Siseviimistlus Haapsalus.",
1522
],
[
"f-kesklinna-projekt",
"viimistlus",
"kaar",
"Remonditööd Tallinnas.",
1523
],
[
"f-vd-rug",
"viimistlus",
"taust",
"Siseviimistlus Tallinnas.",
1524
],
[
"f-3-tooni",
"viimistlus",
"kolm",
"Remonditööd Tallinnas.",
1525
],
[
"f-golcom",
"viimistlus",
"kaart",
"Siseviimistlus Tallinnas.",
1526
],
[
"f-optimal-ehitus",
"viimistlus",
"diag",
"Remonditööd Tallinnas.",
1527
],
[
"f-kvantiteet",
"viimistlus",
"raam",
"Siseviimistlus Võrus.",
1528
],
[
"f-cityrem",
"viimistlus",
"ring",
"Remonditööd Tallinnas.",
1529
],
[
"f-komindex",
"viimistlus",
"duo",
"Siseviimistlus Tartumaal.",
1530
],
[
"f-omw-products",
"viimistlus",
"pool",
"Plaatimine ja põrandad Tallinnas.",
1531
],
[
"f-puitlahendused",
"viimistlus",
"aasta",
"Siseviimistlus Pärnus.",
1532
],
[
"f-fastexp",
"viimistlus",
"riba",
"Remonditööd Harjumaal.",
1533
],
[
"f-arbelton",
"viimistlus",
"print",
"Siseviimistlus Narvas.",
1534
],
[
"f-samabygg",
"viimistlus",
"kaar",
"Remonditööd Tallinnas.",
1535
],
[
"f-e-ruudus",
"viimistlus",
"kolm",
"Remonditööd Tallinnas.",
1537
],
[
"f-magean",
"viimistlus",
"kaart",
"Siseviimistlus Tallinnas.",
1538
],
[
"f-vinemar",
"viimistlus",
"diag",
"Krohvi- ja pahtlitööd Tartus.",
1539
],
[
"f-noge",
"viimistlus",
"raam",
"Siseviimistlus Raplamaal.",
1540
],
[
"f-varex",
"viimistlus",
"ring",
"Remonditööd Tallinnas.",
1541
],
[
"f-ovedec",
"viimistlus",
"duo",
"Siseviimistlus Pärnus.",
1542
],
[
"f-fastfix-ehitus",
"viimistlus",
"pool",
"Remonditööd Tartumaal.",
1543
],
[
"f-irroniset-ehitus",
"viimistlus",
"aasta",
"Siseviimistlus Tallinnas.",
1544
],
[
"f-haapsalu-alumiinium",
"viimistlus",
"riba",
"Remonditööd Haapsalus.",
1545
],
[
"f-harcon",
"viimistlus",
"print",
"Siseviimistlus Tallinnas.",
1546
],
[
"f-karral",
"viimistlus",
"kaar",
"Remonditööd Kuressaares.",
1547
],
[
"f-and-express",
"viimistlus",
"taust",
"Siseviimistlus Harjumaal.",
1548
],
[
"f-ruum3-kliimalahendused",
"viimistlus",
"kolm",
"Remonditööd Harjumaal.",
1549
],
[
"f-piretbygg",
"viimistlus",
"kaart",
"Plaatimine ja põrandad Viljandimaal.",
1550
],
[
"f-vector-ehitus",
"viimistlus",
"diag",
"Remonditööd Harjumaal.",
1551
],
[
"f-dalemo",
"viimistlus",
"raam",
"Siseviimistlus Tallinnas.",
1552
],
[
"f-sofi-service",
"viimistlus",
"ring",
"Värvimistööd Tallinnas.",
1553
],
[
"f-vasad",
"viimistlus",
"duo",
"Siseviimistlus Tallinnas.",
1554
],
[
"f-plaadistaja",
"viimistlus",
"pool",
"Plaatimine ja põrandad Rakveres.",
1555
],
[
"f-tembol",
"viimistlus",
"aasta",
"Siseviimistlus Tallinnas.",
1556
],
[
"f-janbra",
"viimistlus",
"riba",
"Remonditööd Harjumaal.",
1557
],
[
"f-linder-grupp",
"viimistlus",
"print",
"Siseviimistlus Tartus.",
1558
],
[
"f-tabi-remont",
"viimistlus",
"kaar",
"Remonditööd Haapsalus.",
1559
],
[
"f-damian",
"viimistlus",
"taust",
"Plaatimine ja põrandad Tallinnas.",
1560
],
[
"f-sihor-sr",
"viimistlus",
"kolm",
"Remonditööd Jõgevamaal.",
1561
],
[
"f-autel-susteemid",
"toru",
"diag",
"Küttetööd Põlvamaal.",
1563
],
[
"f-paikese-peegel",
"toru",
"raam",
"Küte ja ventilatsioon Tartumaal.",
1564
],
[
"f-na-rivor",
"toru",
"ring",
"Küttetööd Viljandimaal.",
1565
],
[
"f-faunagrupp",
"toru",
"duo",
"Küte ja ventilatsioon Järvamaal.",
1566
],
[
"f-marine-automation",
"toru",
"pool",
"Küttetööd Harjumaal.",
1567
],
[
"f-barneton",
"toru-ahi",
"aasta",
"Ahjud ja kaminad Harjumaal.",
1568
],
[
"f-bevisual",
"toru",
"riba",
"Küttetööd Tallinnas.",
1569
],
[
"f-renvector",
"toru",
"print",
"Torutööd Maardus.",
1570
],
[
"f-triston-insulate",
"toru",
"kaar",
"Küttetööd Põlvas.",
1571
],
[
"f-vr-style",
"toru",
"taust",
"Torutööd Tartus.",
1572
],
[
"f-spiraltube",
"toru",
"kolm",
"Torutööd Saaremaal.",
1573
],
[
"f-toomel",
"toru-ahi",
"kaart",
"Ahjud ja kaminad Tartumaal.",
1574
],
[
"f-tovuart",
"toru",
"diag",
"Küttetööd Tartus.",
1575
],
[
"f-alegmo-ehitus",
"toru",
"raam",
"Torutööd Tallinnas.",
1576
],
[
"f-pinnok",
"toru",
"ring",
"Torutööd Harjumaal.",
1577
],
[
"f-lauraliisa",
"toru",
"duo",
"Küte ja ventilatsioon Tallinnas.",
1578
],
[
"f-soetuba",
"toru-ahi",
"pool",
"Pottsepatööd Jõgevamaal.",
1579
],
[
"f-atorud",
"toru",
"aasta",
"Torutööd Lääne-Virumaal.",
1580
],
[
"f-kontemporan",
"toru",
"riba",
"Santehnik Narva-Jõesuus.",
1581
],
[
"f-kirsiotsa",
"toru-ahi",
"print",
"Ahjud ja kaminad Saaremaal.",
1582
],
[
"f-standhaus-ehitus",
"toru",
"kaar",
"Torutööd Tartus.",
1583
],
[
"f-baumeister",
"toru",
"taust",
"Torutööd Tartumaal.",
1584
],
[
"f-avinda",
"toru",
"kolm",
"Torutööd Tartus.",
1585
],
[
"f-piperix",
"toru",
"kaart",
"Torutööd ja küte Tartus.",
1586
],
[
"f-meniveks-grupp",
"toru",
"diag",
"Santehnik Tallinnas.",
1587
],
[
"f-wentaksystem",
"toru",
"raam",
"Küte ja ventilatsioon Pärnumaal.",
1588
],
[
"f-goldmaks",
"toru",
"ring",
"Küttetööd Harjumaal.",
1589
],
[
"f-amti",
"toru",
"duo",
"Torutööd Jõgevamaal.",
1590
],
[
"f-heikes",
"toru",
"pool",
"Santehnik Viljandimaal.",
1591
],
[
"f-virumaa-veepumbakeskus",
"toru",
"aasta",
"Torutööd Lääne-Virumaal.",
1592
],
[
"f-san-ins",
"toru",
"riba",
"Torutööd Maardus.",
1593
],
[
"f-bgb-grupp",
"toru",
"print",
"Torutööd Kohtla-Järvel.",
1594
],
[
"f-tornel",
"toru",
"kaar",
"Torutööd Tartus.",
1595
],
[
"f-lemps-ou",
"toru",
"taust",
"Küte ja ventilatsioon Harjumaal.",
1596
],
[
"f-vee-ala",
"toru",
"kolm",
"Santehnik Tallinnas.",
1597
],
[
"f-refservice",
"toru",
"kaart",
"Küte ja ventilatsioon Tallinnas.",
1598
],
[
"f-malm-ko",
"toru",
"diag",
"Santehnik Rakveres.",
1599
],
[
"f-deftman",
"toru",
"raam",
"Küte ja ventilatsioon Viljandis.",
1600
],
[
"f-az-group",
"toru",
"ring",
"Küttetööd Maardus.",
1601
],
[
"f-toru-vara",
"toru",
"duo",
"Torutööd Lääne-Virumaal.",
1602
],
[
"f-roho-torutood",
"toru",
"pool",
"Santehnik Tallinnas.",
1603
],
[
"f-ou-holzraum",
"toru",
"aasta",
"Torutööd Rakveres.",
1604
],
[
"f-powerside",
"auto",
"riba",
"Auto hooldus ja remont Lääne-Virumaal.",
1605
],
[
"f-poleerija",
"auto-detail",
"print",
"Autopesu ja puhastus Tartus.",
1606
],
[
"f-cadam-restoration",
"auto",
"kaar",
"Teie auto remont Järvamaal.",
1607
],
[
"f-jasty",
"auto",
"taust",
"Autoremont Kärdlas.",
1608
],
[
"f-elite-garage",
"auto",
"kolm",
"Auto hooldus ja remont Harjumaal.",
1609
],
[
"f-tmlv",
"auto",
"kaart",
"Hooldus ja diagnostika Harjumaal.",
1610
],
[
"f-5m-studio",
"auto",
"diag",
"Teie auto remont Tallinnas.",
1611
],
[
"f-lavi-autoteenindus",
"auto",
"raam",
"Autoremont Pärnumaal.",
1612
],
[
"f-mutrike",
"auto",
"ring",
"Auto hooldus ja remont Põlvamaal.",
1613
],
[
"f-innovalis",
"auto",
"duo",
"Hooldus ja diagnostika Tartumaal.",
1614
],
[
"f-starboy",
"auto",
"pool",
"Teie auto remont Tallinnas.",
1615
],
[
"f-martinus",
"auto",
"aasta",
"Autoremont Tallinnas.",
1616
],
[
"f-rpw-paintworks",
"auto",
"riba",
"Keretööd Tartumaal.",
1617
],
[
"f-autmet",
"auto",
"print",
"Hooldus ja diagnostika Tallinnas.",
1618
],
[
"f-tfs-service",
"auto",
"kaar",
"Teie auto remont Tallinnas.",
1619
],
[
"f-slaviir",
"auto",
"taust",
"Autoremont Tallinnas.",
1620
],
[
"f-patsner",
"auto",
"kolm",
"Auto hooldus ja remont Pärnumaal.",
1621
],
[
"f-antikorcar-grupp",
"auto",
"kaart",
"Hooldus ja diagnostika Tallinnas.",
1622
],
[
"f-tesarem",
"auto",
"diag",
"Teie auto remont Tallinnas.",
1623
],
[
"f-alivin",
"auto",
"raam",
"Autoremont Tartus.",
1624
],
[
"f-kaspari-keretood",
"auto",
"ring",
"Keretööd Tartumaal.",
1625
],
[
"f-kbl-teenused",
"auto",
"duo",
"Hooldus ja diagnostika Võrumaal.",
1626
],
[
"f-auto-td",
"auto",
"pool",
"Teie auto remont Tallinnas.",
1627
],
[
"f-tunk-zahur",
"auto",
"aasta",
"Autoremont Tartus.",
1628
],
[
"f-waldees",
"auto",
"riba",
"Auto hooldus ja remont Raplamaal.",
1629
],
[
"f-randol",
"auto",
"print",
"Hooldus ja diagnostika Pärnumaal.",
1630
],
[
"f-sarrus-sisustus",
"auto",
"kaar",
"Teie auto remont Pärnus.",
1631
],
[
"f-jetker",
"auto",
"taust",
"Autoremont Tartus.",
1632
],
[
"f-servis-s-j-m",
"auto",
"kolm",
"Auto hooldus ja remont Narvas.",
1633
],
[
"f-myrax-group",
"auto",
"diag",
"Teie auto remont Tallinnas.",
1635
],
[
"f-3remi3",
"auto",
"raam",
"Autoremont Hiiumaal.",
1636
],
[
"f-simplefix",
"auto",
"ring",
"Auto hooldus ja remont Tartus.",
1637
],
[
"f-san-carlos",
"auto",
"duo",
"Hooldus ja diagnostika Tallinnas.",
1638
],
[
"f-kaspo-service",
"auto",
"pool",
"Teie auto remont Pärnumaal.",
1639
],
[
"f-kastani-teenindus",
"auto",
"aasta",
"Autoremont Kuressaares.",
1640
],
[
"f-craft-service",
"auto",
"riba",
"Auto hooldus ja remont Järvamaal.",
1641
],
[
"f-lehtvedru",
"auto",
"print",
"Hooldus ja diagnostika Tartus.",
1642
],
[
"f-loksa-autoremont",
"auto",
"kaar",
"Teie auto remont Harjumaal.",
1643
],
[
"f-kp-garage",
"auto",
"taust",
"Autoremont Harjumaal.",
1644
],
[
"f-sttd",
"auto",
"kolm",
"Auto hooldus ja remont Tallinnas.",
1645
],
[
"f-prosalon",
"juuksur",
"kaart",
"Soengud ja värvid Tallinnas.",
1646
],
[
"f-lastejuuksur-juuksik",
"juuksur",
"diag",
"Juuksur Tallinnas.",
1647
],
[
"f-lokkis",
"juuksur",
"raam",
"Juuksurisalong Tallinnas.",
1648
],
[
"f-elsandera",
"juuksur",
"ring",
"Soengud ja värvid Tallinnas.",
1649
],
[
"f-r-salong",
"juuksur",
"duo",
"Juuksur Viljandis.",
1650
],
[
"f-magical-hair",
"juuksur",
"pool",
"Juuksurisalong Tallinnas.",
1651
],
[
"f-sivju",
"juuksur",
"aasta",
"Soengud ja värvid Harjumaal.",
1652
],
[
"f-julikru",
"juuksur",
"riba",
"Juuksur Kohtla-Järvel.",
1653
],
[
"f-anli-design",
"juuksur",
"print",
"Juuksurisalong Tallinnas.",
1654
],
[
"f-dii-beauty",
"juuksur",
"kaar",
"Soengud ja värvid Tartus.",
1655
],
[
"f-amelia-beauty",
"juuksur",
"taust",
"Juuksur Harjumaal.",
1656
],
[
"f-tallinna-perejuuksur-idee",
"juuksur",
"kolm",
"Juuksurisalong Tallinnas.",
1657
],
[
"f-dkstyles",
"juuksur",
"kaart",
"Soengud ja värvid Tallinnas.",
1658
],
[
"f-rkj",
"juuksur",
"diag",
"Juuksur Keilas.",
1659
],
[
"f-hamburgnee",
"juuksur",
"raam",
"Juuksurisalong Haapsalus.",
1660
],
[
"f-ju-hair-stuudio",
"juuksur",
"ring",
"Soengud ja värvid Tallinnas.",
1661
],
[
"f-illyhair",
"juuksur",
"duo",
"Juuksur Saaremaal.",
1662
],
[
"f-dem-brain",
"juuksur",
"pool",
"Juuksurisalong Tallinnas.",
1663
],
[
"f-e-dynasty",
"juuksur",
"aasta",
"Soengud ja värvid Tallinnas.",
1664
],
[
"f-arte-plus",
"juuksur",
"riba",
"Juuksur Tallinnas.",
1665
],
[
"f-ilusalong-sipelga",
"juuksur",
"print",
"Juuksurisalong Tallinnas.",
1666
],
[
"f-laureb-ilustuudio",
"juuksur",
"kaar",
"Soengud ja värvid Tartumaal.",
1667
],
[
"f-barberia",
"juuksur-m",
"taust",
"Meeste juuksur Tartumaal.",
1668
],
[
"f-antales",
"juuksur",
"kolm",
"Juuksurisalong Tallinnas.",
1669
],
[
"f-4hair",
"juuksur",
"kaart",
"Soengud ja värvid Tallinnas.",
1670
],
[
"f-telliks",
"juuksur",
"diag",
"Juuksur Tallinnas.",
1671
],
[
"f-starhair",
"juuksur",
"raam",
"Juuksurisalong Võrus.",
1672
],
[
"f-o-art-studio",
"juuksur",
"ring",
"Soengud ja värvid Tallinnas.",
1673
],
[
"f-fresheads",
"juuksur",
"duo",
"Juuksur Tallinnas.",
1674
],
[
"f-colorblind",
"juuksur",
"pool",
"Juuksurisalong Tallinnas.",
1675
],
[
"f-mariacut",
"juuksur",
"aasta",
"Soengud ja värvid Tallinnas.",
1676
],
[
"f-okos-parlour",
"juuksur",
"riba",
"Juuksur Tallinnas.",
1677
],
[
"f-serpentiin",
"juuksur",
"print",
"Juuksurisalong Tallinnas.",
1678
],
[
"f-keratinka",
"juuksur",
"kaar",
"Soengud ja värvid Harjumaal.",
1679
],
[
"f-insler",
"juuksur",
"taust",
"Juuksur Tallinnas.",
1680
],
[
"f-istoman",
"juuksur",
"kolm",
"Juuksurisalong Kohtla-Järvel.",
1681
],
[
"f-rannapiiga-ilusalong",
"juuksur",
"kaart",
"Soengud ja värvid Harjumaal.",
1682
],
[
"f-frizer",
"juuksur",
"diag",
"Juuksur Tallinnas.",
1683
],
[
"f-stiililaegas",
"juuksur",
"raam",
"Juuksurisalong Võrus.",
1684
],
[
"f-reemet-piiroja-studio",
"juuksur",
"ring",
"Soengud ja värvid Tallinnas.",
1685
],
[
"f-sirkal",
"juuksur",
"duo",
"Juuksur Harjumaal.",
1686
],
[
"f-cuticle",
"juuksur",
"pool",
"Juuksurisalong Pärnus.",
1687
],
[
"f-dragonfruit",
"juuksur",
"aasta",
"Soengud ja värvid Tallinnas.",
1688
],
[
"f-anneli-hobekaarid",
"juuksur",
"riba",
"Juuksur Tartus.",
1689
],
[
"f-lensija",
"koristus",
"print",
"Koristus Tallinnas.",
1690
],
[
"f-pesa-puhtaks-kodukoristus",
"koristus",
"kaar",
"Puhastusteenused Raplamaal.",
1691
],
[
"f-natalee",
"koristus",
"taust",
"Koristus Harjumaal.",
1692
],
[
"f-ventilationpro",
"koristus",
"kolm",
"Puhastusteenused Tallinnas.",
1693
],
[
"f-puhas-tuus",
"koristus",
"kaart",
"Koristus Tallinnas.",
1694
],
[
"f-meskus",
"kaeve",
"ring",
"Pinnasetööd Kuressaares.",
1697
],
[
"f-averton-teenused",
"kaeve",
"duo",
"Kaevetööd Raplamaal.",
1698
],
[
"f-vaikeekskavaator",
"kaeve",
"pool",
"Pinnasetööd Valgamaal.",
1699
],
[
"f-intersky",
"kaeve",
"aasta",
"Kaevetööd Tallinnas.",
1700
],
[
"f-vv-betoonporandad",
"kaeve",
"riba",
"Pinnasetööd Pärnumaal.",
1701
],
[
"f-parnu-kaevetehnik",
"kaeve",
"print",
"Kaevetööd Sindis.",
1702
],
[
"f-sencillez",
"kaeve",
"kaar",
"Pinnasetööd Tallinnas.",
1703
],
[
"f-bonnets",
"kaeve",
"taust",
"Kaevetööd Haapsalus.",
1704
],
[
"f-kiniska",
"kaeve",
"kolm",
"Pinnasetööd Raplamaal.",
1705
],
[
"f-braden-grupp",
"haljastus",
"kaart",
"Haljastus ja aiatööd Pärnus.",
1706
],
[
"f-alekstyle",
"haljastus",
"diag",
"Aiatööd Narva-Jõesuus.",
1707
],
[
"f-life-stone",
"haljastus",
"raam",
"Haljastus ja aiatööd Ida-Virumaal.",
1708
],
[
"f-klautek",
"haljastus",
"ring",
"Aiatööd Saaremaal.",
1709
],
[
"f-mel-ms",
"haljastus",
"duo",
"Haljastus ja aiatööd Tartumaal.",
1710
],
[
"f-astrantia",
"haljastus",
"pool",
"Aiatööd Võrumaal.",
1711
],
[
"f-inna-koristus",
"haljastus",
"aasta",
"Haljastus ja aiatööd Tallinnas.",
1712
],
[
"f-ip-koristus",
"haljastus",
"riba",
"Aiatööd Tallinnas.",
1713
],
[
"f-ecoquest-eesti",
"elekter",
"print",
"Elektrik Harjumaal.",
1714
],
[
"f-lepiku-elektritood",
"elekter",
"kaar",
"Elektripaigaldus Rakveres.",
1715
],
[
"f-elhe",
"elekter",
"taust",
"Elektritööd Võrumaal.",
1716
],
[
"f-digilux-elekter",
"elekter",
"kolm",
"Elektrik Tallinnas.",
1717
],
[
"f-tsaister-center",
"elekter",
"kaart",
"Elektripaigaldus Tallinnas.",
1718
],
[
"f-elcomsys",
"elekter",
"diag",
"Elektritööd Tallinnas.",
1719
],
[
"f-boa-signaal",
"elekter",
"raam",
"Elektrik Tartus.",
1720
],
[
"f-sanest-rent",
"elekter",
"ring",
"Elektripaigaldus Pärnus.",
1721
],
[
"f-foxmast",
"elekter",
"duo",
"Elektritööd Ida-Virumaal.",
1722
],
[
"f-elektrist",
"elekter",
"pool",
"Elektrik Tartumaal.",
1723
],
[
"f-vvd-industrial",
"elekter",
"aasta",
"Elektripaigaldus Tallinnas.",
1724
],
[
"f-voogman",
"elekter",
"riba",
"Elektritööd Võrumaal.",
1725
],
[
"f-vaan-elekter",
"elekter",
"print",
"Elektrik Valgamaal.",
1726
],
[
"f-camos-service",
"elekter",
"kaar",
"Elektripaigaldus Tallinnas.",
1727
],
[
"f-elmastro",
"elekter",
"taust",
"Elektritööd Harjumaal.",
1728
],
[
"f-goldland-ehitus",
"elekter",
"kolm",
"Elektrik Lääne-Virumaal.",
1729
],
[
"f-elektrilahendus",
"elekter",
"kaart",
"Elektripaigaldus Maardus.",
1730
],
[
"f-ledecom",
"ehitus",
"diag",
"Ehitame ja renoveerime Viljandimaal.",
1731
],
[
"f-oukhill",
"ehitus",
"raam",
"Ehitus ja renoveerimine Hiiumaal.",
1732
],
[
"f-dissident-ehitus",
"ehitus",
"ring",
"Maja ehitus Tallinnas.",
1733
],
[
"f-agar-poiss",
"ehitus",
"duo",
"Ehitustööd Raplamaal.",
1734
],
[
"f-akvamer",
"ehitus",
"pool",
"Ehitame ja renoveerime Viljandis.",
1735
],
[
"f-merbekon",
"ehitus",
"aasta",
"Ehitus ja renoveerimine Tallinnas.",
1736
],
[
"f-replei",
"ehitus",
"riba",
"Maja ehitus Lääne-Virumaal.",
1737
],
[
"f-kimoehitus",
"ehitus",
"print",
"Ehitustööd Tartus.",
1738
],
[
"f-raimet-services",
"ehitus",
"kaar",
"Ehitame ja renoveerime Viljandis.",
1739
],
[
"f-pujar",
"ehitus",
"taust",
"Ehitus ja renoveerimine Haapsalus.",
1740
],
[
"f-renkvist",
"ehitus",
"kolm",
"Maja ehitus Harjumaal.",
1741
],
[
"f-taviteone",
"ehitus",
"kaart",
"Ehitustööd Tartus.",
1742
],
[
"f-seriakolmetall",
"ehitus",
"diag",
"Ehitame ja renoveerime Tallinnas.",
1743
],
[
"f-kasaf-ehitus",
"ehitus",
"raam",
"Ehitus ja renoveerimine Kohtla-Järvel.",
1744
],
[
"f-anvekom",
"ehitus",
"ring",
"Maja ehitus Harjumaal.",
1745
],
[
"f-ecomerc-ehitus",
"ehitus",
"duo",
"Ehitustööd Harjumaal.",
1746
],
[
"f-jutavi",
"ehitus",
"pool",
"Ehitame ja renoveerime Pärnumaal.",
1747
],
[
"f-tartex",
"ehitus",
"aasta",
"Ehitus ja renoveerimine Jõgevamaal.",
1748
],
[
"f-brigadir",
"ehitus",
"riba",
"Maja ehitus Tartus.",
1749
],
[
"f-inks-viimistlus",
"ehitus",
"print",
"Ehitustööd Pärnumaal.",
1750
],
[
"f-ekollon-group-company",
"ehitus",
"kaar",
"Ehitame ja renoveerime Harjumaal.",
1751
],
[
"f-vare-ehitus",
"ehitus",
"taust",
"Ehitus ja renoveerimine Lääne-Virumaal.",
1752
],
[
"f-cold-constructions",
"ehitus",
"kolm",
"Maja ehitus Lääne-Virumaal.",
1753
],
[
"f-laas-service",
"ehitus",
"kaart",
"Ehitustööd Läänemaal.",
1754
],
[
"f-omasadu",
"ehitus",
"diag",
"Ehitame ja renoveerime Harjumaal.",
1755
],
[
"f-ratmont",
"ehitus",
"raam",
"Ehitus ja renoveerimine Pärnus.",
1756
],
[
"f-kivicom-ehitus",
"ehitus",
"ring",
"Maja ehitus Järvamaal.",
1757
],
[
"f-svartiro",
"ehitus",
"duo",
"Ehitustööd Valgas.",
1758
],
[
"f-roostalu",
"ehitus",
"pool",
"Ehitame ja renoveerime Pärnus.",
1759
],
[
"f-jarika",
"ehitus",
"aasta",
"Ehitus ja renoveerimine Tartus.",
1760
],
[
"f-madest",
"ehitus",
"riba",
"Maja ehitus Ida-Virumaal.",
1761
],
[
"f-mareo",
"ehitus",
"print",
"Ehitustööd Pärnumaal.",
1762
],
[
"f-judzin-grupp",
"ehitus",
"kaar",
"Ehitame ja renoveerime Narvas.",
1763
],
[
"f-multi-haldus",
"ehitus",
"taust",
"Ehitus ja renoveerimine Tallinnas.",
1764
],
[
"f-ramise-ehitus",
"ehitus",
"kolm",
"Maja ehitus Pärnumaal.",
1765
],
[
"f-construur",
"ehitus",
"kaart",
"Ehitustööd Harjumaal.",
1766
],
[
"f-albert-ehitus",
"ehitus",
"diag",
"Ehitame ja renoveerime Tallinnas.",
1767
],
[
"f-vlb-haldus",
"ehitus",
"raam",
"Ehitus ja renoveerimine Harjumaal.",
1768
],
[
"f-mop-keskus",
"ehitus",
"ring",
"Maja ehitus Narvas.",
1769
],
[
"f-peruskivi",
"ehitus",
"duo",
"Ehitustööd Tartus.",
1770
],
[
"f-pintex-building",
"ehitus",
"pool",
"Ehitame ja renoveerime Tallinnas.",
1771
],
[
"f-vikstre",
"ehitus",
"aasta",
"Ehitus ja renoveerimine Hiiumaal.",
1772
],
[
"f-delfino",
"ehitus",
"riba",
"Maja ehitus Lääne-Virumaal.",
1773
],
[
"f-traiel",
"ehitus",
"print",
"Ehitustööd Võrumaal.",
1774
],
[
"f-mevorah",
"ehitus",
"kaar",
"Ehitame ja renoveerime Ida-Virumaal.",
1775
],
[
"f-raumar",
"ehitus",
"taust",
"Ehitus ja renoveerimine Tartumaal.",
1776
],
[
"f-noobel-grupp",
"ehitus",
"kolm",
"Maja ehitus Rakveres.",
1777
],
[
"f-milt-ehitus",
"ehitus",
"kaart",
"Ehitustööd Rakveres.",
1778
],
[
"f-aita-ehitus",
"ehitus",
"diag",
"Ehitame ja renoveerime Võrumaal.",
1779
],
[
"f-groger",
"ehitus",
"ring",
"Maja ehitus Lääne-Virumaal.",
1781
],
[
"f-topler",
"ehitus",
"duo",
"Ehitustööd Harjumaal.",
1782
],
[
"f-lexvel",
"ehitus",
"pool",
"Ehitame ja renoveerime Tartumaal.",
1783
],
[
"f-taevapiir",
"ehitus",
"aasta",
"Ehitus ja renoveerimine Pärnus.",
1784
],
[
"f-lennu-ehitus",
"ehitus",
"riba",
"Maja ehitus Tartus.",
1785
],
[
"f-wepro-works",
"ehitus",
"print",
"Ehitustööd Tartumaal.",
1786
],
[
"f-mextar",
"ehitus",
"kaar",
"Ehitame ja renoveerime Tallinnas.",
1787
],
[
"f-ks-group",
"ehitus",
"taust",
"Ehitus ja renoveerimine Võrus.",
1788
],
[
"f-ref-ehitustood",
"ehitus",
"kolm",
"Maja ehitus Tallinnas.",
1789
],
[
"f-comters-grupp",
"ehitus",
"kaart",
"Ehitustööd Kohtla-Järvel.",
1790
],
[
"f-place4you",
"ehitus",
"diag",
"Ehitame ja renoveerime Tallinnas.",
1791
],
[
"f-lekser",
"ehitus",
"raam",
"Ehitus ja renoveerimine Tartus.",
1792
],
[
"f-domum-ehitus",
"ehitus",
"ring",
"Maja ehitus Järvamaal.",
1793
],
[
"f-teramo",
"ehitus",
"duo",
"Ehitustööd Tartumaal.",
1794
],
[
"f-tularik",
"ehitus",
"pool",
"Ehitame ja renoveerime Harjumaal.",
1795
],
[
"f-eksmeks",
"ehitus",
"aasta",
"Ehitus ja renoveerimine Lääne-Virumaal.",
1796
],
[
"f-melli-ehitus",
"ehitus",
"riba",
"Maja ehitus Saaremaal.",
1797
],
[
"f-rare-building",
"ehitus",
"print",
"Ehitustööd Tartus.",
1798
],
[
"f-liamluc",
"ehitus",
"kaar",
"Ehitame ja renoveerime Järvamaal.",
1799
],
[
"f-starwilde",
"ehitus",
"taust",
"Ehitus ja renoveerimine Tartumaal.",
1800
],
[
"f-stonera",
"ehitus",
"kolm",
"Maja ehitus Lääne-Virumaal.",
1801
],
[
"f-eternora",
"ehitus",
"kaart",
"Ehitustööd Pärnumaal.",
1802
],
[
"f-montech",
"ehitus",
"diag",
"Ehitame ja renoveerime Raplamaal.",
1803
],
[
"f-ja-ge-pro",
"ehitus",
"raam",
"Ehitus ja renoveerimine Raplamaal.",
1804
],
[
"f-park-koger",
"ehitus",
"ring",
"Maja ehitus Tallinnas.",
1805
],
[
"f-mupi",
"ehitus",
"duo",
"Ehitustööd Võrus.",
1806
],
[
"f-talis-nurk-ehitus",
"ehitus",
"pool",
"Ehitame ja renoveerime Tartumaal.",
1807
],
[
"f-nees",
"ehitus",
"aasta",
"Ehitus ja renoveerimine Harjumaal.",
1808
],
[
"f-inro-teenused",
"ehitus",
"riba",
"Maja ehitus Viljandimaal.",
1809
],
[
"f-k-k-constructions",
"ehitus",
"print",
"Ehitustööd Pärnus.",
1810
],
[
"f-alekto-projekt",
"ehitus",
"kaar",
"Ehitame ja renoveerime Tallinnas.",
1811
],
[
"f-simworks",
"ehitus",
"taust",
"Ehitus ja renoveerimine Tallinnas.",
1812
],
[
"f-bgb-construction",
"ehitus",
"kolm",
"Maja ehitus Lääne-Virumaal.",
1813
],
[
"f-viktoras-bygg",
"ehitus",
"kaart",
"Ehitustööd Tallinnas.",
1814
],
[
"f-sekme",
"ehitus",
"diag",
"Ehitame ja renoveerime Valgas.",
1815
],
[
"f-moltonesto",
"ehitus",
"raam",
"Ehitus ja renoveerimine Pärnus.",
1816
],
[
"f-refnar",
"ehitus",
"ring",
"Maja ehitus Tartus.",
1817
],
[
"f-ko-ehitus",
"ehitus",
"duo",
"Ehitustööd Võrumaal.",
1818
],
[
"f-bret-grupp",
"ehitus",
"pool",
"Ehitame ja renoveerime Valgamaal.",
1819
],
[
"f-artemis-grupp",
"ehitus",
"aasta",
"Ehitus ja renoveerimine Raplamaal.",
1820
],
[
"f-life-by-you",
"ehitus",
"riba",
"Maja ehitus Tartumaal.",
1821
],
[
"f-orub-orub",
"ehitus",
"print",
"Ehitustööd Tallinnas.",
1822
],
[
"f-nampes",
"ehitus",
"kaar",
"Ehitame ja renoveerime Raplamaal.",
1823
],
[
"f-kuldrak",
"ehitus",
"taust",
"Ehitus ja renoveerimine Tartumaal.",
1824
],
[
"f-deveron",
"ehitus",
"kolm",
"Maja ehitus Saaremaal.",
1825
],
[
"f-sooja-group",
"ehitus",
"kaart",
"Ehitustööd Kuressaares.",
1826
],
[
"f-lin-ehitus",
"ehitus",
"diag",
"Ehitame ja renoveerime Tallinnas.",
1827
],
[
"f-adesse-ehitus",
"ehitus",
"raam",
"Ehitus ja renoveerimine Jõgeval.",
1828
],
[
"f-proffestest",
"ehitus",
"ring",
"Maja ehitus Tallinnas.",
1829
],
[
"f-makkri",
"ehitus",
"duo",
"Ehitustööd Lääne-Virumaal.",
1830
],
[
"f-kirelo",
"ehitus",
"pool",
"Ehitame ja renoveerime Jõgevamaal.",
1831
],
[
"f-universbuild",
"ehitus",
"aasta",
"Ehitus ja renoveerimine Jõgeval.",
1832
],
[
"f-k-k-remontti",
"ehitus",
"riba",
"Maja ehitus Harjumaal.",
1833
],
[
"f-ensam-sk",
"ehitus",
"print",
"Ehitustööd Harjumaal.",
1834
],
[
"f-u-t-grupp",
"ehitus",
"kaar",
"Ehitame ja renoveerime Harjumaal.",
1835
],
[
"f-hiie-ehitus",
"ehitus",
"taust",
"Ehitus ja renoveerimine Harjumaal.",
1836
],
[
"f-v-v-est-ehitus",
"ehitus",
"kolm",
"Maja ehitus Viljandimaal.",
1837
],
[
"f-vajangu-ee",
"ehitus",
"kaart",
"Ehitustööd Lääne-Virumaal.",
1838
],
[
"f-ruuderi-ehitus",
"ehitus",
"diag",
"Ehitame ja renoveerime Võrumaal.",
1839
],
[
"f-tr-installation",
"ehitus",
"raam",
"Ehitus ja renoveerimine Tallinnas.",
1840
],
[
"f-masterbalt",
"ehitus",
"ring",
"Maja ehitus Tallinnas.",
1841
],
[
"f-autounion",
"ehitus",
"duo",
"Ehitustööd Tartus.",
1842
],
[
"f-wisemen-grupp",
"ehitus",
"pool",
"Ehitame ja renoveerime Tallinnas.",
1843
],
[
"f-vebeks-projekt",
"ehitus",
"aasta",
"Ehitus ja renoveerimine Harjumaal.",
1844
],
[
"f-alvsby",
"ehitus",
"riba",
"Maja ehitus Lääne-Virumaal.",
1845
],
[
"f-rastuk-grupp",
"ehitus",
"print",
"Ehitustööd Tartumaal.",
1846
],
[
"f-willu",
"ehitus",
"kaar",
"Ehitame ja renoveerime Hiiumaal.",
1847
],
[
"f-majamees-ehitus",
"ehitus",
"taust",
"Ehitus ja renoveerimine Pärnus.",
1848
],
[
"f-omg777",
"ehitus",
"kolm",
"Maja ehitus Raplamaal.",
1849
],
[
"f-valaste-grupp",
"ehitus",
"kaart",
"Ehitustööd Ida-Virumaal.",
1850
],
[
"f-raud-ja-betoon",
"ehitus",
"diag",
"Ehitame ja renoveerime Tartumaal.",
1851
],
[
"f-gelo-rent",
"ehitus",
"raam",
"Ehitus ja renoveerimine Pärnumaal.",
1852
],
[
"f-ptln-ehitus",
"ehitus",
"ring",
"Maja ehitus Tallinnas.",
1853
],
[
"f-ceko-ehitus",
"ehitus",
"duo",
"Ehitustööd Lääne-Virumaal.",
1854
],
[
"f-epto-ehitus",
"ehitus",
"pool",
"Ehitame ja renoveerime Võrumaal.",
1855
],
[
"f-puramiid-ehitus",
"ehitus",
"aasta",
"Ehitus ja renoveerimine Harjumaal.",
1856
],
[
"f-kimiken",
"ehitus",
"riba",
"Maja ehitus Tartumaal.",
1857
],
[
"f-westest-north",
"ehitus",
"print",
"Ehitustööd Pärnumaal.",
1858
],
[
"f-rimantase-ehitus",
"ehitus",
"kaar",
"Ehitame ja renoveerime Tallinnas.",
1859
],
[
"f-toomemagi",
"ehitus",
"taust",
"Ehitus ja renoveerimine Võrus.",
1860
],
[
"f-rehe-grupp",
"ehitus",
"kolm",
"Maja ehitus Saaremaal.",
1861
],
[
"f-ehituskang",
"ehitus",
"kaart",
"Ehitustööd Lääne-Virumaal.",
1862
],
[
"f-reiveltol",
"ehitus",
"diag",
"Ehitame ja renoveerime Pärnus.",
1863
],
[
"f-circinus-viimistlus",
"ehitus",
"raam",
"Ehitus ja renoveerimine Tartus.",
1864
],
[
"f-b-vod-engineering",
"ehitus",
"ring",
"Maja ehitus Tallinnas.",
1865
],
[
"f-tiiliker",
"ehitus",
"duo",
"Ehitustööd Tallinnas.",
1866
],
[
"f-romken-ehitus",
"ehitus",
"pool",
"Ehitame ja renoveerime Harjumaal.",
1867
],
[
"f-vanopal",
"ehitus",
"aasta",
"Ehitus ja renoveerimine Ida-Virumaal.",
1868
],
[
"f-nugrem",
"ehitus",
"riba",
"Maja ehitus Tallinnas.",
1869
],
[
"f-bac-systems",
"ehitus",
"print",
"Ehitustööd Tallinnas.",
1870
],
[
"f-mrmb-veritas",
"ehitus",
"kaar",
"Ehitame ja renoveerime Raplamaal.",
1871
],
[
"f-brn-group",
"ehitus",
"taust",
"Ehitus ja renoveerimine Võrumaal.",
1872
],
[
"f-katkoro",
"ehitus",
"kolm",
"Maja ehitus Harjumaal.",
1873
],
[
"f-woodworm",
"ehitus",
"kaart",
"Ehitustööd Jõgevamaal.",
1874
],
[
"f-terraway",
"ehitus",
"diag",
"Ehitame ja renoveerime Tallinnas.",
1875
],
[
"f-saaremaaler",
"ehitus",
"raam",
"Ehitus ja renoveerimine Saaremaal.",
1876
],
[
"f-kmr-ehitus",
"ehitus",
"ring",
"Maja ehitus Harjumaal.",
1877
],
[
"f-vintrans-group",
"ehitus",
"duo",
"Ehitustööd Tallinnas.",
1878
],
[
"f-balt-zt-company",
"ehitus",
"pool",
"Ehitame ja renoveerime Raplamaal.",
1879
],
[
"f-soosilla-ehitus",
"ehitus",
"aasta",
"Ehitus ja renoveerimine Viljandis.",
1880
],
[
"f-avikas",
"ehitus",
"riba",
"Maja ehitus Läänemaal.",
1881
],
[
"f-hiiu-suitsusaun",
"ehitus",
"print",
"Ehitustööd Hiiumaal.",
1882
],
[
"f-komarov-ehitus",
"ehitus",
"kaar",
"Ehitame ja renoveerime Tallinnas.",
1883
],
[
"f-apsalon",
"ehitus",
"taust",
"Ehitus ja renoveerimine Harjumaal.",
1884
],
[
"f-lalande",
"ehitus",
"kolm",
"Maja ehitus Raplamaal.",
1885
],
[
"f-raimen-ehitus",
"ehitus",
"kaart",
"Ehitustööd Viljandimaal.",
1886
],
[
"f-astoriina-ehitus",
"ehitus",
"diag",
"Ehitame ja renoveerime Põlvamaal.",
1887
],
[
"f-pearlbox",
"ehitus",
"raam",
"Ehitus ja renoveerimine Tallinnas.",
1888
],
[
"f-fooniks-grupp",
"ehitus",
"ring",
"Maja ehitus Saaremaal.",
1889
],
[
"f-hiietark",
"ehitus",
"duo",
"Ehitustööd Pärnus.",
1890
],
[
"f-mankoff",
"ehitus",
"pool",
"Ehitame ja renoveerime Tallinnas.",
1891
],
[
"f-jk-timber",
"ehitus",
"aasta",
"Ehitus ja renoveerimine Tallinnas.",
1892
],
[
"f-roje-grupp",
"ehitus",
"riba",
"Maja ehitus Tallinnas.",
1893
],
[
"f-printsiip-ehitus",
"ehitus",
"print",
"Ehitustööd Harjumaal.",
1894
],
[
"f-temec-ehitus",
"ehitus",
"kaar",
"Ehitame ja renoveerime Valgamaal.",
1895
],
[
"f-priidu-ehitus",
"ehitus",
"taust",
"Ehitus ja renoveerimine Tartumaal.",
1896
],
[
"f-varado-ehitus",
"ehitus",
"kolm",
"Maja ehitus Viljandimaal.",
1897
],
[
"f-teenuse-express",
"ehitus",
"kaart",
"Ehitustööd Tallinnas.",
1898
],
[
"f-tgz-projekt",
"ehitus",
"diag",
"Ehitame ja renoveerime Järvamaal.",
1899
],
[
"f-blackplanet",
"ehitus",
"raam",
"Ehitus ja renoveerimine Sauel.",
1900
],
[
"f-hindre-ehitus",
"ehitus",
"ring",
"Maja ehitus Hiiumaal.",
1901
],
[
"f-jaxson",
"ehitus",
"duo",
"Ehitustööd Võrumaal.",
1902
],
[
"f-jandec",
"ehitus",
"pool",
"Ehitame ja renoveerime Harjumaal.",
1903
],
[
"f-marivar",
"ehitus",
"aasta",
"Ehitus ja renoveerimine Tallinnas.",
1904
],
[
"f-temitex-ehitus",
"ehitus",
"riba",
"Maja ehitus Tartumaal.",
1905
],
[
"f-remppa",
"ehitus",
"print",
"Ehitustööd Tartumaal.",
1906
],
[
"f-altivi-project",
"ehitus",
"kaar",
"Ehitame ja renoveerime Saaremaal.",
1907
],
[
"f-laemees",
"ehitus",
"taust",
"Ehitus ja renoveerimine Tartumaal.",
1908
],
[
"f-euro-ehitusgrupp",
"ehitus",
"kolm",
"Maja ehitus Tallinnas.",
1909
],
[
"f-nesto-ehitus",
"ehitus",
"kaart",
"Ehitustööd Harjumaal.",
1910
],
[
"f-tsirkel-sistems",
"ehitus",
"diag",
"Ehitame ja renoveerime Võrumaal.",
1911
],
[
"f-vilomark",
"ehitus",
"raam",
"Ehitus ja renoveerimine Pärnus.",
1912
],
[
"f-albeco",
"ehitus",
"ring",
"Maja ehitus Rakveres.",
1913
],
[
"f-prime-im",
"ehitus",
"duo",
"Ehitustööd Lääne-Virumaal.",
1914
],
[
"f-ls-trust",
"ehitus",
"pool",
"Ehitame ja renoveerime Harjumaal.",
1915
],
[
"f-saareko-majad",
"ehitus",
"aasta",
"Ehitus ja renoveerimine Harjumaal.",
1916
],
[
"f-stonebystone",
"ehitus",
"riba",
"Maja ehitus Tallinnas.",
1917
],
[
"f-jproof",
"ehitus",
"print",
"Ehitustööd Põlvamaal.",
1918
],
[
"f-ratec",
"ehitus",
"kaar",
"Ehitame ja renoveerime Võrus.",
1919
],
[
"f-pai-kasi",
"ehitus",
"taust",
"Ehitus ja renoveerimine Tartus.",
1920
],
[
"f-skillman",
"ehitus",
"kolm",
"Maja ehitus Võrumaal.",
1921
],
[
"f-prantssai",
"ehitus",
"kaart",
"Ehitustööd Lääne-Virumaal.",
1922
],
[
"f-grp-ehitus-group",
"ehitus",
"diag",
"Ehitame ja renoveerime Narvas.",
1923
],
[
"f-starfire",
"ehitus",
"raam",
"Ehitus ja renoveerimine Tallinnas.",
1924
],
[
"f-twintbuilders",
"ehitus",
"ring",
"Maja ehitus Tartus.",
1925
],
[
"f-srg-grupp",
"ehitus",
"duo",
"Ehitustööd Rakveres.",
1926
],
[
"f-m-j-marconi",
"ehitus",
"pool",
"Ehitame ja renoveerime Pärnus.",
1927
],
[
"f-trendex-ehitus",
"ehitus",
"aasta",
"Ehitus ja renoveerimine Harjumaal.",
1928
],
[
"f-top-tugi",
"ehitus",
"riba",
"Maja ehitus Pärnus.",
1929
],
[
"f-mace-pj",
"ehitus",
"print",
"Ehitustööd Tartumaal.",
1930
],
[
"f-primorty",
"ehitus",
"kaar",
"Ehitame ja renoveerime Pärnus.",
1931
],
[
"f-egram-ehitus",
"ehitus",
"taust",
"Ehitus ja renoveerimine Tallinnas.",
1932
],
[
"f-loorand-ehitus",
"ehitus",
"kolm",
"Maja ehitus Lääne-Virumaal.",
1933
],
[
"f-belasco-ex",
"ehitus",
"kaart",
"Ehitustööd Tallinnas.",
1934
]
]

for _r in NADALLEHED:
    lisa(*_r)
