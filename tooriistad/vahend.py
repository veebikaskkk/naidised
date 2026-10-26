"""Abivahendid uutele kujundustele: värvide segamine, kontrastiga palett, ühine avaploki baas ja logomärgid.

Palett kontrollib kontrasti juba loomisel (assert), et kontroll.py-s ei tuleks üllatusi.
"""
from kujundused import v


def _rgb(c):
    c = c.lstrip("#")
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))


def mix(a, b, t):
    """t osa värvi a, ülejäänu b."""
    A, B = _rgb(a), _rgb(b)
    return "#%02X%02X%02X" % tuple(round(x * t + y * (1 - t)) for x, y in zip(A, B))


def _lum(c):
    f = lambda x: x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4
    r, g, b = (x / 255 for x in _rgb(c))
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def kontrast(a, b):
    la, lb = sorted((_lum(a), _lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def kindel(fg, bg, vaja=4.7):
    """Nihutab fg-d mustema või valgema poole, kuni kontrast on piisav."""
    siht = "#000000" if _lum(bg) > 0.18 else "#FFFFFF"
    t = 1.0
    while kontrast(fg, bg) < vaja and t > 0:
        t -= 0.05
        fg = mix(fg, siht, t) if t > 0 else siht
    return fg


def parim(bg):
    return "#FFFFFF" if kontrast("#FFFFFF", bg) >= kontrast("#141414", bg) else "#141414"


def pal(bg, fg, acc, dark, dark_acc, hb, hf, ha, raadius="8px", surface=None, pea="'Inter'", keha="'Inter'",
        pea_kaal="800", pea_ls="-0.02em"):
    surface = surface or mix(acc, bg, 0.08)
    muted = kindel(mix(fg, bg, 0.74), surface)
    acc = kindel(acc, "#FFFFFF" if parim(acc) == "#FFFFFF" else "#141414", 4.6)
    acc_fg = parim(acc)
    dark_acc = kindel(dark_acc, dark, 4.8)
    hf = kindel(hf, hb, 7)
    hl = kindel(mix(hf, hb, 0.86), hb, 4.8)
    ha = kindel(ha, "#FFFFFF" if parim(ha) == "#FFFFFF" else "#141414", 4.6)
    haf = parim(ha)
    for x, y in ((fg, bg), (muted, bg), (muted, surface), (fg, surface), (acc_fg, acc), ("#FFFFFF", dark),
                 (dark_acc, dark), (hf, hb), (hl, hb), (haf, ha)):
        assert kontrast(x, y) >= 4.5, (x, y, kontrast(x, y))
    return dict(
        hb=hb, hf=hf, hl=hl, ha=ha, haf=haf, acc=acc, acc_fg=acc_fg, bg=bg, fg=fg, dark=dark,
        vars=v(pea=pea, keha=keha, pea_kaal=pea_kaal, pea_ls=pea_ls, bg=bg, fg=fg, muted=muted, surface=surface,
               line=mix(fg, bg, 0.16), accent=acc, accent_fg=acc_fg, dark=dark, dark_fg="#FFFFFF",
               dark_accent=dark_acc, fookus=acc, raadius=raadius, line_tugev=mix(fg, bg, 0.5)))


def baas(cls, P, pad="88px 0 96px", suurus="clamp(36px,6.2vw,90px)", h1_lisa=""):
    return (f".{cls}{{background:{P['hb']};color:{P['hf']};padding:{pad};position:relative;overflow:hidden}}\n"
            f".{cls} h1{{font-size:{suurus};line-height:1.0;font-weight:var(--pea-kaal);letter-spacing:var(--pea-ls);margin:0 0 24px;{h1_lisa}}}\n"
            f".{cls} .lead{{color:{P['hl']}}}\n"
            f".{cls} .nupp.pea{{background:{P['ha']};color:{P['haf']}}}\n"
            f".{cls} .nupp.teine{{color:{P['hf']}}}\n")


LOGOD = [
    "width:18px;height:18px;border-radius:50%;background:{a}",
    "width:16px;height:16px;background:{a};transform:rotate(45deg)",
    "width:20px;height:20px;border-radius:50%;border:4px solid {a}",
    "width:22px;height:11px;border-radius:22px 22px 0 0;background:{a}",
    "width:6px;height:22px;background:{a};box-shadow:10px 0 0 {a};margin-right:10px",
    "width:22px;height:20px;background:{a};clip-path:polygon(50% 0,100% 100%,0 100%)",
    "width:20px;height:20px;border-radius:50% 50% 50% 0;background:{a}",
    "width:8px;height:8px;border-radius:50%;background:{a};box-shadow:12px 0 0 {a},24px 0 0 {a};margin-right:24px",
    "width:20px;height:20px;border-radius:4px;border:3px solid {a};border-right-color:transparent",
    "width:22px;height:22px;background:conic-gradient({a} 0 25%,transparent 0 50%,{a} 0 75%,transparent 0)",
]


def pais_css(tyyp, P, logo_i):
    mark = LOGOD[logo_i % len(LOGOD)]
    if tyyp == "tume":
        return (f".pais-tume{{background:{P['dark']};color:#FFFFFF}}"
                f".pais-tume .logo-mark{{{mark.format(a=kindel(P['ha'], P['dark'], 3))}}}")
    if tyyp == "varv":
        return (f".pais-varv{{background:{P['hb']};color:{P['hf']}}}"
                f".pais-varv .logo-mark{{{mark.format(a=P['ha'] if kontrast(P['ha'], P['hb']) > 2 else P['hf'])}}}")
    return f".pais-hele .logo-mark{{{mark.format(a=P['acc'])}}}"
