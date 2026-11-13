# -*- coding: utf-8 -*-
"""Opmaak van de App Store-screenshots (kop + toestelrand) en de promobeelden in de Kentr-huisstijl."""
import base64, pathlib

YELLOW = "#F5C400"
EUBLUE = "#003399"

HEADLINES = [
    ("Al je auto's op één plek", "Van je eerste auto tot nu, met of zonder kenteken"),
    ("Elk kenteken opzoeken", "Techniek, APK en meer, rechtstreeks van de RDW"),
    ("Fiscale waarde en bijtelling", "Catalogusprijs, bruto BPM en een indicatie per maand"),
    ("Kenteken vergeten? Terugvinden!", "Zoek op merk, model, kleur en bouwjaar"),
    ("Ook zonder kenteken", "Merk, type en periode zijn genoeg; het kenteken zoek je later"),
    ("Je autohistorie in cijfers", "Merken, brandstof, bezitsduur en kilometers"),
    ("Veilig met Face ID en iCloud", "Geen account en geen eigen server"),
]

MARKETING = {
    "header_5244x2950.png": (2622, 1475, 2, "header"),
    "header_3840x1646.png": (1920, 823, 2, "header"),
    "search_5244x2950.png": (2622, 1475, 2, "search"),
    "search_3840x2560.png": (1920, 1280, 2, "search"),
    "search_1920x1280.png": (960, 640, 2, "search"),
}

def data_uri(path):
    return "data:image/png;base64," + base64.b64encode(pathlib.Path(path).read_bytes()).decode()

BASE_CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{font-family:Inter,sans-serif;-webkit-font-smoothing:antialiased;overflow:hidden}
.bg{position:relative;overflow:hidden;background:linear-gradient(165deg,#13306F 0%,#0B1F4B 48%,#071436 100%)}
.ghost{position:absolute;border-radius:14px;background:rgba(245,196,0,.07);border:2px solid rgba(245,196,0,.10)}
.dev{position:absolute;background:#1B1C20;box-shadow:0 30px 80px rgba(0,0,0,.45),inset 0 0 0 1.5px #44464d}
.dev img{display:block}
.island{position:absolute;background:#000;border-radius:999px}
"""

def device(img_uri, w, h, s, ipad, left, top, rot=0, z=1):
    """Toestelrand met scherm. w,h = logische schermmaat, s = schaal."""
    sw, sh = w * s, h * s
    b = (16 if ipad else 10) * s / (0.78 if ipad else 0.74)
    r = (18 if ipad else 55) * s
    island = "" if ipad else (f'<div class="island" style="width:{124*s}px;height:{36*s}px;left:{b + (sw-124*s)/2}px;top:{b + 11*s}px"></div>')
    return (f'<div class="dev" style="left:{left}px;top:{top}px;width:{sw+2*b}px;height:{sh+2*b}px;padding:{b}px;'
            f'border-radius:{r+b}px;transform:rotate({rot}deg);z-index:{z}">'
            f'<img src="{img_uri}" style="width:{sw}px;height:{sh}px;border-radius:{r}px">{island}</div>')

def ghosts(cw, ch, k):
    out = []
    for x, y, w, rot in ((-.08, .06, .42, -9), (.74, .02, .38, 8), (.66, .86, .5, -6), (-.12, .78, .36, 7)):
        out.append(f'<div class="ghost" style="left:{x*cw}px;top:{y*ch}px;width:{w*cw}px;height:{w*cw*0.25}px;'
                   f'border-radius:{w*cw*0.03}px;transform:rotate({rot}deg)"></div>')
    return "".join(out[:k])

def screenshot_page(i, raw_path, w, h, ipad, cw, ch):
    title, sub = HEADLINES[i]
    s = 0.78 if ipad else 0.74
    b = (16 if ipad else 10) * s / s
    dev_w, dev_h = w * s + 2 * b, h * s + 2 * b
    left = (cw - dev_w) / 2
    top = ch - dev_h - (44 if ipad else 22)
    tsize, ssize = (56, 26) if ipad else (31, 15.5)
    ttop = 70 if ipad else 52
    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{BASE_CSS}
    .t{{position:absolute;left:{cw*0.07}px;right:{cw*0.07}px;top:{ttop}px;text-align:center;color:#fff}}
    .t h1{{font:800 {tsize}px/1.12 Inter;letter-spacing:-.015em}}
    .t p{{font:500 {ssize}px/1.35 Inter;color:rgba(255,255,255,.78);margin-top:{tsize*0.32}px}}
    .bar{{width:{tsize*1.4}px;height:{tsize*0.16}px;border-radius:9px;background:{YELLOW};margin:0 auto {tsize*0.38}px}}
    </style></head><body><div class="bg" style="width:{cw}px;height:{ch}px">
    {ghosts(cw, ch, 3)}
    <div class="t"><div class="bar"></div><h1>{title}</h1><p>{sub}</p></div>
    {device(data_uri(raw_path), w, h, s, ipad, left, top)}
    </div></body></html>"""
    return html

def mini_plate(text, h):
    return (f'<div style="display:inline-flex;height:{h}px;border-radius:{h*0.14}px;overflow:hidden;box-shadow:inset 0 0 0 {h*0.05}px #111,0 {h*0.2}px {h*0.5}px rgba(0,0,0,.35)">'
            f'<div style="width:{h*0.42}px;background:{EUBLUE};display:flex;align-items:flex-end;justify-content:center;padding-bottom:{h*0.1}px;'
            f'font:700 {h*0.22}px/1 Inter;color:#fff">NL</div>'
            f'<div style="background:{YELLOW};padding:0 {h*0.35}px;display:flex;align-items:center;font:900 {h*0.62}px/1 Inter;color:#111;letter-spacing:.01em">{text}</div></div>')

def marketing_page(kind, cw, ch, raw_dir, icon_path):
    raw = pathlib.Path(raw_dir) / "iphone-6.3"
    shots = [data_uri(raw / f) for f in ("02_opzoeken.png", "01_mijn-autos.png", "04_terugvinden.png")]
    W, H = 402, 874
    ratio = cw / ch
    # telefoons rechts
    if ratio > 2:        # 3840x1646
        s = ch * 0.80 / H
        cx, top = cw * 0.70, ch * 0.10
    elif ratio > 1.6:    # 5244x2950
        s = ch * 0.74 / H
        cx, top = cw * 0.69, ch * 0.13
    else:                # 3:2
        s = ch * 0.64 / H
        cx, top = cw * 0.665, ch * 0.17
    b = 10 * s / 0.74
    dw = W * s + 2 * b
    gap = dw * 0.78
    phones = (device(shots[0], W, H, s * 0.9, False, cx - dw / 2 - gap, top + ch * 0.06, -6, 1)
              + device(shots[2], W, H, s * 0.9, False, cx - dw / 2 + gap + dw * 0.1, top + ch * 0.06, 6, 1)
              + device(shots[1], W, H, s, False, cx - dw / 2, top, 0, 2))
    # tekst links
    tx = cw * 0.06
    tw = cx - dw / 2 - gap - tx - cw * 0.02
    base = min(ch * 0.075, tw * 0.13)
    icon = data_uri(icon_path)
    tagline = "Al je auto's. Altijd bij de hand." if kind == "header" else "Elk kenteken. Je hele autohistorie."
    sub = ("Houd elke auto bij die je hebt gehad. Zoek kentekens op bij de RDW, zie de fiscale waarde en bijtelling, en vind een vergeten kenteken terug."
           if kind == "header" else
           "Opzoeken bij de RDW, catalogusprijs en bijtelling, en een vergeten kenteken terugvinden.")
    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{BASE_CSS}
    .tx{{position:absolute;left:{tx}px;width:{tw}px;top:50%;transform:translateY(-50%);color:#fff}}
    .brand{{display:flex;align-items:center;gap:{base*0.45}px;margin-bottom:{base*0.55}px}}
    .brand img{{width:{base*1.7}px;height:{base*1.7}px;border-radius:{base*1.7*0.2237}px;box-shadow:0 {base*0.2}px {base*0.6}px rgba(0,0,0,.4)}}
    .brand span{{font:800 {base*1.25}px/1 Inter;letter-spacing:-.02em}}
    h1{{font:800 {base}px/1.1 Inter;color:{YELLOW};letter-spacing:-.015em}}
    p{{font:500 {base*0.42}px/1.45 Inter;color:rgba(255,255,255,.8);margin-top:{base*0.4}px}}
    .src{{margin-top:{base*0.6}px;display:flex;align-items:center;gap:{base*0.3}px;font:600 {base*0.34}px/1.25 Inter;color:rgba(255,255,255,.7)}}
    </style></head><body><div class="bg" style="width:{cw}px;height:{ch}px">
    {ghosts(cw, ch, 4)}
    <div class="tx"><div class="brand"><img src="{icon}"><span>Kentr</span></div>
      <h1>{tagline}</h1><p>{sub}</p>
      <div class="src"><span style="width:{base*0.22}px;height:{base*0.22}px;border-radius:50%;background:{YELLOW};flex:none"></span><span>Met openbare gegevens van RDW Open Data</span></div></div>
    {phones}
    </div></body></html>"""
    return html
