"""Omast kaustast majutatud fondid (Google Fonts, latin + latin-ext)."""

FONDID = {
    "Inter": [("400", "normal", "inter-regular.woff"), ("600", "normal", "inter-semibold.woff")],
    "Inter Display": [("800", "normal", "interdisplay-extrabold.woff")],
    "Archivo": [("400", "normal", "archivo-regular.woff2"), ("600", "normal", "archivo-600.woff2"),
                ("800", "normal", "archivo-800.woff2"), ("900", "normal", "archivo-900.woff2")],
    "Bricolage Grotesque": [("400", "normal", "bricolage-grotesque-regular.woff2"),
                            ("700", "normal", "bricolage-grotesque-700.woff2"),
                            ("800", "normal", "bricolage-grotesque-800.woff2")],
    "DM Serif Display": [("400", "normal", "dm-serif-display-regular.woff2"),
                         ("400", "italic", "dm-serif-display-italic.woff2")],
    "Epilogue": [("400", "normal", "epilogue-regular.woff2"), ("600", "normal", "epilogue-600.woff2"),
                 ("800", "normal", "epilogue-800.woff2")],
    "Familjen Grotesk": [("400", "normal", "familjen-grotesk-regular.woff2"),
                         ("600", "normal", "familjen-grotesk-600.woff2"),
                         ("700", "normal", "familjen-grotesk-700.woff2")],
    "Fraunces": [("400", "normal", "fraunces-regular.woff2"), ("400", "italic", "fraunces-italic.woff2"),
                 ("700", "normal", "fraunces-700.woff2"), ("900", "normal", "fraunces-900.woff2")],
    "Instrument Serif": [("400", "normal", "instrument-serif-regular.woff2"),
                         ("400", "italic", "instrument-serif-italic.woff2")],
    "Manrope": [("400", "normal", "manrope-regular.woff2"), ("600", "normal", "manrope-600.woff2"),
                ("800", "normal", "manrope-800.woff2")],
    "Space Grotesk": [("400", "normal", "space-grotesk-regular.woff2"), ("500", "normal", "space-grotesk-500.woff2"),
                      ("700", "normal", "space-grotesk-700.woff2")],
    "Syne": [("400", "normal", "syne-regular.woff2"), ("700", "normal", "syne-700.woff2"),
             ("800", "normal", "syne-800.woff2")],
    "Unbounded": [("400", "normal", "unbounded-regular.woff2"), ("700", "normal", "unbounded-700.woff2"),
                  ("900", "normal", "unbounded-900.woff2")],
}


def font_face(*pered):
    out = []
    for p in dict.fromkeys(pered):
        for w, st, f in FONDID[p]:
            fmt = "woff2" if f.endswith("woff2") else "woff"
            out.append(f'@font-face{{font-family:"{p}";src:url("/fondid/{f}") format("{fmt}");'
                       f'font-weight:{w};font-style:{st};font-display:swap}}')
    return "\n".join(out)
