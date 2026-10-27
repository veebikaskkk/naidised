"""Teeb eelvaatepildid (public/<slug>/eelvaade.jpg) ja meilid (meilid/<kuupäev>.csv + eelvaate HTML).

Kasutus: python3 tooriistad/meilid.py <kuupäev> [slug ...]
Eeldab, et kohalik server serveerib public/ kausta aadressil http://127.0.0.1:8770.
"""
import csv, html, json, pathlib, sys
from playwright.sync_api import sync_playwright
from PIL import Image

juur = pathlib.Path(__file__).resolve().parent.parent
VEEB = "https://naidis.veebikask.ee"
E = html.escape


def pildid(slugid):
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium-1243/chrome-linux64/chrome")
        for s in slugid:
            pg = b.new_page(viewport={"width": 1280, "height": 800}, device_scale_factor=1)
            pg.goto(f"http://127.0.0.1:8770/{s}/")
            pg.wait_for_timeout(700)
            # Teip ei kuulu pildile, see on lehel niikuinii.
            pg.evaluate("document.querySelector('.teip').remove()")
            tmp = juur / "meilid" / f"_{s}.png"
            pg.screenshot(path=str(tmp))
            pg.close()
            im = Image.open(tmp).convert("RGB").resize((1120, 700), Image.LANCZOS)
            im.save(juur / "public" / s / "eelvaade.jpg", quality=80, optimize=True, progressive=True)
            tmp.unlink()
        b.close()


def meil(a, s):
    lyhi = a["lyhinimi"]
    al, le = ("AS-il", "AS-ile") if a.get("vorm") == "AS" else ("OÜ-l", "OÜ-le")
    link = f"{VEEB}/{s}/"
    pilt = f"{VEEB}/{s}/eelvaade.jpg"
    if a["pakett"] == "500":
        hind = ("Hind on 500 € ühekordselt. Selle eest saate mitmelehelise kodulehe nagu näidisel: avaleht ning eraldi "
                "lehed teenuste, tehtud tööde ja hinnapäringu vormiga. Majutus ja haldus maksab 100 € aastas, nii et "
                "teie ei pea tehnilise poole pärast muretsema.")
    elif a["pakett"] == "400":
        hind = ("Hind on 400 € ühekordselt. Selle eest saate kodulehe koos broneerimiskalendriga: klient valib teenuse, "
                "päeva ja kellaaja ning broneering jõuab teie e-postile. Majutus ja haldus maksab 100 € aastas, nii et "
                "teie ei pea tehnilise poole pärast muretsema.")
    else:
        hind = ("Hind on 250 € ühekordselt. Majutus ja haldus maksab 75 € aastas, nii et teie ei pea tehnilise "
                "poole pärast muretsema.")
    pealkiri = f"Tegin {lyhi} {le} näidis-kodulehe"
    sissejuhatus = f"Märkasin, et {lyhi} {al} pole veel oma kodulehte ja tegin teile proovimiseks ühe valmis."
    keskel = ("Seal on teie teenused, broneerimiskalender ja kontaktid ning see töötab ka telefonis." if a["pakett"] == "400" else
              "Seal on teie teenused ja kontaktid ning see töötab ka telefonis.")
    keskel += " Kui see meeldib, paneme selle teie oma aadressile üles ja lisame pildid teie päris töödest."
    lopp = "Kui see teid ei huvita, vastake lihtsalt ei ja ma rohkem ei kirjuta."
    domeen = a.get("domeen") or ""
    aadress = f" Valmis lehel on teie oma aadress, näiteks {domeen}." if domeen else ""
    keha_html = (
        f'<p>Tere!</p><p>{E(sissejuhatus)}</p>'
        f'<p><a href="{link}"><img src="{pilt}" width="560" height="350" alt="{E(lyhi)} näidiskoduleht" '
        f'style="display:block;width:100%;max-width:560px;height:auto;border:1px solid #dddddd;border-radius:6px"></a></p>'
        f'<p style="font-size:13px;color:#555555;margin-top:-6px">Vaata lehte: <a href="{link}">{E(lyhi)} näidiskoduleht</a>.{E(aadress)}</p>'
        f'<p>{E(keskel)}</p><p>{E(hind)}</p><p>{E(lopp)}</p>')
    keha_tekst = f"Tere!\n\n{sissejuhatus}\n{link}\n{aadress.strip()}\n\n{keskel}\n\n{hind}\n\n{lopp}"
    return pealkiri, keha_html, keha_tekst, link, pilt


def main(kuupaev, slugid):
    (juur / "meilid").mkdir(exist_ok=True)
    if not slugid:
        slugid = [f.stem for f in sorted((juur / "andmed").glob("*.json"))]
    pildid(slugid)
    read, eelvaade = [], []
    for s in slugid:
        a = json.loads((juur / "andmed" / f"{s}.json").read_text(encoding="utf-8"))
        pk, kh, kt, link, pilt = meil(a, s)
        read.append([a["email"], a["nimi"], a["pakett"], pk, kh, kt, link, pilt, a.get("domeen", "")])
        eelvaade.append(f'<article><p class="m"><b>Kellele:</b> {E(a["email"])} &nbsp; <b>Pakett:</b> {a["pakett"]} €</p>'
                        f'<h2>{E(pk)}</h2>{kh}</article>')
    with open(juur / "meilid" / f"{kuupaev}.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["email", "firma", "pakett", "pealkiri", "keha_html", "keha_tekst", "link", "pilt", "domeen"])
        w.writerows(read)
    (juur / "meilid" / f"{kuupaev}-eelvaade.html").write_text(
        '<!doctype html><meta charset="utf-8"><title>Meilide eelvaade</title>'
        '<style>body{font-family:Arial,sans-serif;background:#eee;margin:0;padding:24px}article{background:#fff;max-width:640px;margin:0 auto 32px;padding:28px 32px;border-radius:8px}h2{font-size:18px}.m{font-size:13px;color:#666}</style>'
        + "".join(eelvaade), encoding="utf-8")
    print(len(read), "meili")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
