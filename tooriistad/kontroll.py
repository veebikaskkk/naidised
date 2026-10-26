"""Kontrollib kõiki public/*/index.html näidiseid master prompti nimekirja järgi.
Jooksuta: python3 tooriistad/kontroll.py   (väljub koodiga 1, kui midagi on valesti)"""
import hashlib, json, pathlib, re, subprocess, sys
from html.parser import HTMLParser

juur = pathlib.Path(__file__).resolve().parent.parent
pub = juur / "public"
vead = []

TUHJAD = {"meta", "link", "br", "img", "input", "hr", "source", "rect", "feDistantLight", "area", "base", "col", "wbr"}


class Parser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.pinu, self.h, self.idd, self.lingid, self.ressursid, self.vead = [], [], set(), [], [], []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "style" in a:
            self.vead.append(f"style= atribuut sildil <{tag}>")
        if tag == "style":
            self.vead.append("<style> plokk, CSP keelab")
        if tag == "script" and "src" not in a:
            self.vead.append("reasisene <script>, CSP keelab")
        if re.fullmatch(r"h[1-6]", tag):
            self.h.append(int(tag[1]))
        if "id" in a:
            self.idd.add(a["id"])
        if tag == "a" and a.get("href"):
            self.lingid.append(a["href"])
        if tag == "link" and a.get("href"):
            self.ressursid.append(a["href"])
        if tag.lower() not in {t.lower() for t in TUHJAD}:
            self.pinu.append(tag)

    def handle_startendtag(self, tag, attrs):
        a = dict(attrs)
        if "style" in a:
            self.vead.append(f"style= atribuut sildil <{tag}>")
        if "id" in a:
            self.idd.add(a["id"])

    def handle_endtag(self, tag):
        if tag.lower() in {t.lower() for t in TUHJAD}:
            return
        if not self.pinu or self.pinu[-1] != tag:
            self.vead.append(f"tasakaalust väljas </{tag}>, ootasin </{self.pinu[-1] if self.pinu else '-'}>")
        else:
            self.pinu.pop()


def luminants(hexv):
    hexv = hexv.lstrip("#")
    r, g, b = (int(hexv[i:i + 2], 16) / 255 for i in (0, 2, 4))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def kontrast(a, b):
    la, lb = sorted((luminants(a), luminants(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def tekst_ilma_siltideta(s):
    s = re.sub(r"<svg.*?</svg>", " ", s, flags=re.S)
    return re.sub(r"<[^>]+>", " ", s)


for leht in sorted(pub.glob("*/index.html")):
    nimi = leht.parent.name
    s = leht.read_text(encoding="utf-8")
    p = Parser()
    p.feed(s)
    v = [f"{nimi}: {x}" for x in p.vead]
    if p.pinu:
        v.append(f"{nimi}: sulgemata sildid {p.pinu}")
    if p.h.count(1) != 1:
        v.append(f"{nimi}: h1 arv on {p.h.count(1)}")
    for i in range(1, len(p.h)):
        if p.h[i] > p.h[i - 1] + 1:
            v.append(f"{nimi}: pealkirjatase hüppab h{p.h[i-1]} -> h{p.h[i]}")
    if "—" in s:
        v.append(f"{nimi}: pikk mõttekriips U+2014")
    tekst = tekst_ilma_siltideta(s)
    for m in re.finditer(r",\s+(ja|ning|või|ega)\s", tekst):
        v.append(f"{nimi}: koma rinnastava sidesõna ees: ...{tekst[max(0,m.start()-30):m.end()+10].strip()}...")
    if re.search(r"\[[A-ZÕÄÖÜ ]{2,}\]", s):
        v.append(f"{nimi}: kohatäide nagu [NIMI] jäi alles")
    for href in p.lingid:
        if href.startswith("#") and href[1:] not in p.idd:
            v.append(f"{nimi}: ankur {href} ei vii kuhugi")
    for href in p.ressursid:
        tee = (pub / href.lstrip("/")) if href.startswith("/") else (leht.parent / href)
        if not tee.exists():
            v.append(f"{nimi}: puudub fail {href}")
    css = (leht.parent / "stiil.css").read_text(encoding="utf-8")
    for url in re.findall(r'url\("(/[^"]+)"\)', css):
        if not (pub / url.lstrip("/")).exists():
            v.append(f"{nimi}: CSS viitab puuduvale failile {url}")
    v_ = dict(re.findall(r"--(tume|kesk|hele|toon|kiir):(#[0-9A-Fa-f]{6})", css))
    paarid = [("#FFFFFF", v_["tume"], "valge tumedal"), ("#FFFFFF", v_["kesk"], "valge keskmisel"),
              ("#1F2328", v_["hele"], "tekst helel"), ("#1F2328", v_["toon"], "tekst toonil"),
              ("#4A5157", v_["toon"], "väiketekst toonil"), ("#4A5157", "#FBFBFA", "väiketekst taustal"),
              ("#4A5157", "#FFFFFF", "väiketekst kaardil"), (v_["tume"], "#FBFBFA", "pealkiri taustal"),
              (v_["tume"], v_["toon"], "pealkiri toonil"), ("#1F2328", v_["kiir"], "tekst kiirel"),
              ("#363C41", "#FBFBFA", "sissejuhatus"), ("#FFFFFF", "#1F2328", "teip")]
    for a, b, kus in paarid:
        k = kontrast(a, b)
        if k < 4.5:
            v.append(f"{nimi}: kontrast {kus} {k:.2f} < 4.5")
    regkood = json.loads((juur / "andmed" / f"{nimi}.json").read_text(encoding="utf-8"))["registrikood"]
    if f"registrikood {regkood}" not in s:
        v.append(f"{nimi}: jaluses pole registrikoodi")
    vead += v
    print(("VIGA " if v else "ok   ") + nimi)

# Korratavus: genereeri uuesti, tulemus peab olema baidi pealt sama.
def rasi():
    h = hashlib.sha256()
    for f in sorted(pub.rglob("*")):
        if f.is_file():
            h.update(str(f.relative_to(pub)).encode()); h.update(f.read_bytes())
    return h.hexdigest()

enne = rasi()
subprocess.run([sys.executable, str(juur / "tooriistad" / "genereeri.py")], check=True, capture_output=True)
if rasi() != enne:
    vead.append("genereerimine ei ole korratav")

for x in vead:
    print(" -", x)
print("KÕIK KORRAS" if not vead else f"{len(vead)} viga")
sys.exit(1 if vead else 0)
