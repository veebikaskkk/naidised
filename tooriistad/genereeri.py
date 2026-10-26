"""Genereerib kõik näidised andmed/*.json failidest kausta public/<slug>/.
Jooksuta: python3 tooriistad/genereeri.py   (HTML-i käsitsi ei muudeta)"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import mall_viimistlus

MALLID = {"viimistlus": mall_viimistlus}
juur = pathlib.Path(__file__).resolve().parent.parent
for f in sorted((juur / "andmed").glob("*.json")):
    a = json.loads(f.read_text(encoding="utf-8"))
    index, css = MALLID[a["mall"]].ehita(a)
    out = juur / "public" / f.stem
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(index, encoding="utf-8")
    (out / "stiil.css").write_text(css, encoding="utf-8")
    print("ok", f.stem)
