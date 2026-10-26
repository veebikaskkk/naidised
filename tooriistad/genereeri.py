"""Genereerib kõik näidised andmed/*.json failidest kausta public/<slug>/.
Jooksuta: python3 tooriistad/genereeri.py   (HTML-i käsitsi ei muudeta)"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import kujundus

juur = pathlib.Path(__file__).resolve().parent.parent
(juur / "public" / "skript.js").write_text(kujundus.SKRIPT, encoding="utf-8")
for f in sorted((juur / "andmed").glob("*.json")):
    a = json.loads(f.read_text(encoding="utf-8"))
    out = juur / "public" / f.stem
    out.mkdir(parents=True, exist_ok=True)
    for nimi, sisu in kujundus.ehita(a).items():
        (out / nimi).write_text(sisu, encoding="utf-8")
    print("ok", f.stem, a["pakett"], a["kujundus"])
