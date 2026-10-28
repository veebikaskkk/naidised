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
