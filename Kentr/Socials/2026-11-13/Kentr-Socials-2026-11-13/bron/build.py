#!/usr/bin/env python3
"""Kentr – social banners (NL, lancering). Rendert HTML/CSS naar PNG met Playwright.

Gebruik: python3 build.py <uitvoermap>
Schermen zijn nagebouwd op basis van de SwiftUI-code (Kentr/Views); alle kentekens zijn fictief
(letters Q/E/A/U worden niet uitgegeven op Nederlandse platen).
"""
import base64, pathlib, sys
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else HERE.parent / "nl")
OUT.mkdir(parents=True, exist_ok=True)
ICON = "data:image/png;base64," + base64.b64encode((HERE / "icon.png").read_bytes()).decode()

ACCENT = "#0B2A6F"

# ---------- bouwstenen ----------
def plate(text, h=22):
    """KentekenPlateView: geel met blauwe EU-strook."""
    return f'''<span class="kp" style="height:{h}px;border-radius:{h*.14:.1f}px;border-width:{max(1,h*.045):.1f}px">
<span class="kp-eu" style="width:{h*.62:.1f}px"><i style="font-size:{h*.22:.1f}px">✷</i><b style="font-size:{h*.28:.1f}px">NL</b></span>
<span class="kp-t" style="font-size:{h*.58:.1f}px;padding:0 {h*.3:.1f}px">{text}</span></span>'''

def unknown(h=22):
    return f'<span class="unk" style="height:{h}px;font-size:{h*.36:.1f}px">⬚ Kenteken onbekend</span>'

CAR = '<svg viewBox="0 0 24 24" width="24" height="24"><path fill="#F5C400" d="M5 11l1.6-4.2A2 2 0 0 1 8.5 5.5h7a2 2 0 0 1 1.9 1.3L19 11h.5A1.5 1.5 0 0 1 21 12.5V16a1 1 0 0 1-1 1h-1a2 2 0 0 1-4 0H9a2 2 0 0 1-4 0H4a1 1 0 0 1-1-1v-3.5A1.5 1.5 0 0 1 4.5 11zm2.2 0h9.6l-1.2-3.2a.8.8 0 0 0-.7-.5H9.1a.8.8 0 0 0-.7.5z"/></svg>'
BOLT = '<svg viewBox="0 0 24 24" width="24" height="24"><path fill="#F5C400" d="M5 11l1.6-4.2A2 2 0 0 1 8.5 5.5h7a2 2 0 0 1 1.9 1.3L19 11h.5A1.5 1.5 0 0 1 21 12.5V16a1 1 0 0 1-1 1h-1a2 2 0 0 1-4 0H9a2 2 0 0 1-4 0H4a1 1 0 0 1-1-1v-3.5A1.5 1.5 0 0 1 4.5 11zm7.6-4.6L9.5 11h2l-.6 3.4 3.2-4.6h-2.1z"/></svg>'

def thumb(icon):
    return f'<span class="th">{icon}</span>'

def status_bar():
    return '''<div class="sb"><span>9:41</span><span class="sbr">
<svg width="18" height="11" viewBox="0 0 18 11"><rect x="0" y="7" width="3" height="4" rx="1"/><rect x="5" y="5" width="3" height="6" rx="1"/><rect x="10" y="2.5" width="3" height="8.5" rx="1"/><rect x="15" y="0" width="3" height="11" rx="1"/></svg>
<svg width="16" height="11" viewBox="0 0 16 11"><path d="M8 2.2c2.2 0 4.2.9 5.7 2.3l1.1-1.1A9.6 9.6 0 0 0 8 .6 9.6 9.6 0 0 0 1.2 3.4l1.1 1.1A8 8 0 0 1 8 2.2zm0 3.2c1.3 0 2.5.5 3.4 1.3l1.1-1.1A6.4 6.4 0 0 0 8 3.8a6.4 6.4 0 0 0-4.5 1.8l1.1 1.1c.9-.8 2.1-1.3 3.4-1.3zM8 8.6l1.9-1.9a2.7 2.7 0 0 0-3.8 0z"/></svg>
<svg width="26" height="12" viewBox="0 0 26 12"><rect x=".5" y=".5" width="22" height="11" rx="3" fill="none" stroke="#111" opacity=".4"/><rect x="2" y="2" width="19" height="8" rx="2"/><rect x="24" y="4" width="1.6" height="4" rx=".8" opacity=".4"/></svg></span></div>'''

TABS = [("Mijn auto's", "car"), ("Opzoeken", "search"), ("Terugvinden", "q"), ("Overzicht", "chart"), ("Instellingen", "gear")]
TAB_ICONS = {
    "car": '<path d="M4 12l1.8-4.6A2 2 0 0 1 7.7 6h8.6a2 2 0 0 1 1.9 1.4L20 12v5a1 1 0 0 1-1 1h-1.5a1 1 0 0 1-1-1v-1h-9v1a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1z"/>',
    "search": '<circle cx="10.5" cy="10.5" r="6" fill="none" stroke-width="2.2"/><path d="M15 15l5 5" stroke-width="2.4" stroke-linecap="round"/>',
    "q": '<rect x="4" y="4" width="16" height="16" rx="3" fill="none" stroke-width="2" stroke-dasharray="3 2.4"/><path d="M10 10a2 2 0 1 1 3 1.7c-.6.4-1 .8-1 1.5" fill="none" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="16" r="1.1"/>',
    "chart": '<rect x="4" y="12" width="3.5" height="8" rx="1"/><rect x="10.2" y="6" width="3.5" height="14" rx="1"/><rect x="16.5" y="9" width="3.5" height="11" rx="1"/>',
    "gear": '<circle cx="12" cy="12" r="7.5" fill="none" stroke-width="2.4" stroke-dasharray="3 2"/><circle cx="12" cy="12" r="3" fill="none" stroke-width="2.2"/>',
}

def tab_bar(active):
    items = ""
    for i, (label, key) in enumerate(TABS):
        col = ACCENT if i == active else "#8E8E93"
        items += f'<div class="tab" style="color:{col}"><svg width="26" height="26" viewBox="0 0 24 24" fill="{col}" stroke="{col}">{TAB_ICONS[key]}</svg><span>{label}</span></div>'
    return f'<div class="tabbar">{items}</div>'

def row(label, value, strong=False, muted=False):
    st = ' style="font-weight:600"' if strong else (' style="color:#8E8E93"' if muted else "")
    return f'<div class="cell lc"><span>{label}</span><span class="v"{st}>{value}</span></div>'

# ---------- schermen (390×844) ----------
def screen_cars():
    rows_now = f'''<div class="cell car">{thumb(BOLT)}<div class="cm"><b>Volkswagen ID.3</b>{plate("Q-417-AE")}<small>Sinds april 2026</small></div><span class="chev">›</span></div>'''
    rows_old = "".join(
        f'<div class="cell car">{thumb(CAR)}<div class="cm"><b>{t}</b>{p}<small>{d}</small></div><span class="chev">›</span></div>'
        for t, p, d in [
            ("Volkswagen Golf", plate("6-QAE-41"), "maart 2016 – april 2026"),
            ("Peugeot 206", plate("21-QE-AU"), "2009 – 2016"),
            ("Opel Kadett", unknown(), "2003 – 2009"),
        ])
    return f'''<div class="scr">{status_bar()}
<div class="nb"><span></span><span class="plus">+</span></div>
<div class="lt">Mijn auto's</div>
<div class="search">⌕&nbsp; Merk, model, kenteken of jaar</div>
<div class="sh">NU IN BEZIT</div><div class="grp">{rows_now}</div>
<div class="sh">EERDER</div><div class="grp">{rows_old}</div>
{tab_bar(0)}</div>'''

def screen_lookup():
    return f'''<div class="scr">{status_bar()}
<div class="lt" style="margin-top:44px">Opzoeken</div>
<div class="sh">KENTEKEN</div>
<div class="grp"><div class="cell" style="justify-content:space-between"><span class="mono">Q-417-AE</span><span class="sbtn">⌕</span></div></div>
<div class="hdr">{plate("Q-417-AE", 46)}<div class="ht">Volkswagen ID.3</div><div class="hs">Bouwjaar 2026</div></div>
<div class="grp"><div class="cell act">⊕&nbsp; Toevoegen aan mijn auto's</div></div>
<div class="sh">FISCAAL</div>
<div class="grp">{row("Catalogusprijs", "€ 42.500")}{row("Bruto BPM", "€ 0")}{row("Eerste toelating", "14 april 2026")}{row("CO2-uitstoot", "0 g/km")}</div>
<div class="sh">BIJTELLING (INDICATIE)</div>
<div class="grp">{row("Percentage", "19,2%")}{row("Per maand", "€ 679", strong=True)}{row("Per jaar", "€ 8.150")}{row("Tarief vast t/m", "30 april 2031")}</div>
{tab_bar(1)}</div>'''

def screen_find():
    res = "".join(
        f'<div class="cell res">{plate(p, 26)}<div class="cm2"><b>Golf</b><small>Zwart · {d}</small></div><span class="chev">›</span></div>'
        for p, d in [("6-QAE-41", "3 maart 2009"), ("8-QEU-17", "12 maart 2009"), ("5-QUA-90", "27 mei 2009"), ("9-EQA-26", "8 oktober 2009")])
    return f'''<div class="scr">{status_bar()}
<div class="lt" style="margin-top:44px">Terugvinden</div>
<div class="grp"><div class="cell info"><span class="ii">i</span><span>De RDW publiceert geen eigenaren. Kentr toont auto's die passen bij je omschrijving, zodat je je eigen kenteken kunt herkennen.</span></div></div>
<div class="sh">AUTO</div>
<div class="grp">{row("Merk", "VOLKSWAGEN")}{row("Model", "Golf")}{row("Kleur", "Zwart")}</div>
<div class="sh">BOUWJAAR (EERSTE TOELATING)</div>
<div class="grp">{row("Van", "2009")}{row("Tot en met", "2009")}</div>
<div class="grp" style="margin-top:14px"><div class="cell act" style="justify-content:center">⌕&nbsp; Zoek kentekens</div></div>
<div class="sh">18 RESULTATEN</div>
<div class="grp">{res}</div>
{tab_bar(2)}</div>'''

SCREENS = {"cars": screen_cars, "lookup": screen_lookup, "find": screen_find}

def phone(screen, width, extra=""):
    s = width / 418  # 390 scherm + 2×14 rand
    return f'''<div class="ph" style="width:{width}px;height:{872*s:.0f}px;{extra}">
<div class="phi" style="transform:scale({s:.4f})"><div class="island"></div>{SCREENS[screen]()}</div></div>'''

def big_plates(w):
    """Gestapelde kentekenplaten zoals op de website/het icoon."""
    def p(txt, style):
        return f'<div class="bp" style="width:{w}px;height:{w*240/784:.0f}px;{style}"><div class="bp-eu"><i>✷</i>NL</div><div class="bp-t" style="font-size:{w*.16:.0f}px">{txt}</div></div>'
    return f'''<div class="bps" style="width:{w*1.1:.0f}px;height:{w*.62:.0f}px">
{p("", "transform:translate(-2%,0) rotate(-8deg);opacity:.45")}
{p("", f"transform:translate(0,{w*.08:.0f}px) rotate(-3.5deg);opacity:.75")}
{p("KENTR", f"transform:translate(0,{w*.2:.0f}px)")}</div>'''

APPLE = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M16.37 12.6c-.02-2.2 1.8-3.26 1.88-3.31-1.03-1.5-2.62-1.7-3.18-1.73-1.35-.14-2.64.8-3.33.8-.69 0-1.74-.78-2.87-.76-1.47.02-2.83.86-3.59 2.180-1.53 2.66-.39 6.59 1.1 8.750.73 1.05 1.59 2.23 2.73 2.19 1.1-.04 1.51-.71 2.84-.71 1.32 0 1.7.71 2.86.69 1.18-.02 1.93-1.07 2.65-2.13.83-1.22 1.18-2.4 1.2-2.46-.03-.01-2.3-.88-2.32-3.5zM14.2 6.130c.6-.73 1-1.74.9-2.75-.86.04-1.9.58-2.52 1.3-.55.64-1.04 1.67-.91 2.66.96.07 1.94-.49 2.53-1.210z"/></svg>'

def badge(fs):
    return f'<span class="badge" style="font-size:{fs}px">{APPLE}Binnenkort in de App Store</span>'

def brand(size, fs):
    return f'<div class="brand"><img src="{ICON}" style="width:{size}px;height:{size}px;border-radius:{size*.225:.0f}px"><span style="font-size:{fs}px">Kentr</span></div>'

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Inter,-apple-system,sans-serif;-webkit-font-smoothing:antialiased;color:#fff}
.c{position:relative;overflow:hidden;background:linear-gradient(180deg,#102C68 0%,#071436 100%)}
.glow{position:absolute;border-radius:50%;background:radial-gradient(circle,rgba(245,196,0,.09),rgba(245,196,0,0) 65%)}
h1{font-weight:800;letter-spacing:-.025em;line-height:1.05}
h1 em{font-style:normal;color:#F5C400}
.sub{color:rgba(255,255,255,.84);line-height:1.35;font-weight:500}
.url{color:rgba(255,255,255,.72);font-weight:600}
.brand{display:flex;align-items:center;gap:.5em}
.brand img{box-shadow:0 6px 18px rgba(0,0,0,.35)}
.brand span{font-weight:800;letter-spacing:-.02em}
.badge{display:inline-flex;align-items:center;gap:.55em;background:#000;color:#fff;border:2px solid rgba(255,255,255,.4);border-radius:.7em;padding:.55em 1em;font-weight:600;white-space:nowrap}
.badge svg{width:1.25em;height:1.25em}
.chips{display:flex;flex-wrap:wrap;gap:10px}
.chip{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.22);border-radius:999px;padding:.4em .9em;font-weight:600;color:#fff}
.chip b{color:#F5C400}
/* grote platen */
.bps{position:relative}
.bp{position:absolute;left:0;top:0;display:flex;border:5px solid #111;border-radius:16px;overflow:hidden;box-shadow:0 18px 40px rgba(0,0,0,.4)}
.bp-eu{width:18%;background:#003399;display:flex;flex-direction:column;align-items:center;justify-content:center;font-weight:700;font-size:22px;gap:2px}
.bp-eu i{font-style:normal;color:#F5C400;font-size:22px}
.bp-t{flex:1;background:#F5C400;color:#111;display:flex;align-items:center;justify-content:center;font-weight:900;letter-spacing:.02em}
/* telefoon */
.ph{position:absolute;filter:drop-shadow(0 30px 50px rgba(0,0,0,.5))}
.phi{position:absolute;left:0;top:0;width:418px;height:872px;transform-origin:0 0;background:#0d0d0f;border-radius:66px;padding:14px;box-shadow:inset 0 0 0 2px #3a3d46}
.island{position:absolute;left:50%;top:25px;width:122px;height:36px;margin-left:-61px;background:#000;border-radius:20px;z-index:5}
.scr{position:relative;width:390px;height:844px;border-radius:52px;overflow:hidden;background:#F2F2F7;color:#000;font-family:Inter,-apple-system,sans-serif;font-size:17px}
.sb{display:flex;justify-content:space-between;align-items:center;height:54px;padding:6px 34px 0 46px;font-weight:600;font-size:16px}
.sbr{display:flex;gap:6px;align-items:center}.sbr svg{fill:#111}
.nb{height:44px;display:flex;justify-content:space-between;align-items:center;padding:0 20px}
.plus{color:#0B2A6F;font-size:30px;font-weight:400}
.lt{font-size:34px;font-weight:800;letter-spacing:-.02em;padding:0 20px 8px}
.search{margin:4px 16px 6px;background:rgba(118,118,128,.12);border-radius:10px;height:36px;display:flex;align-items:center;padding:0 10px;color:#8E8E93;font-size:16px}
.sh{font-size:13px;color:#6D6D72;padding:16px 36px 6px;letter-spacing:.01em}
.grp{margin:0 16px;background:#fff;border-radius:10px;overflow:hidden}
.cell{display:flex;align-items:center;padding:11px 16px;min-height:44px;position:relative}
.cell+.cell::before{content:"";position:absolute;top:0;left:16px;right:0;height:.5px;background:#C6C6C8}
.cell.car+.cell.car::before{left:86px}
.lc{justify-content:space-between}.lc .v{color:#3C3C43;color:rgba(60,60,67,.85)}
.car{gap:14px;padding:8px 16px}
.th{width:56px;height:56px;border-radius:12px;background:linear-gradient(180deg,#0B1F4B,#071436);display:grid;place-items:center;flex:none}
.th svg{width:26px;height:26px}
.cm{display:flex;flex-direction:column;gap:5px;align-items:flex-start;flex:1;min-width:0}
.cm b{font-size:17px;font-weight:600}
.cm small,.cm2 small{font-size:12px;color:#8E8E93}
.chev{color:#C4C4C7;font-size:24px;font-weight:300}
.res{gap:12px;padding:9px 16px}
.cm2{display:flex;flex-direction:column;gap:1px;flex:1}.cm2 b{font-size:15px;font-weight:600}
.kp{display:inline-flex;overflow:hidden;border:solid rgba(17,17,17,.85);flex:none}
.kp-eu{background:#003399;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:0}
.kp-eu i{font-style:normal;color:#F5C400;line-height:1}.kp-eu b{color:#fff;line-height:1;font-weight:800}
.kp-t{background:#F5C400;color:#111;font-family:'DejaVu Sans Mono',monospace;font-weight:700;display:flex;align-items:center;white-space:nowrap;letter-spacing:-.02em}
.unk{display:inline-flex;align-items:center;padding:0 7px;color:#8E8E93;font-weight:600;border:1px dashed rgba(142,142,147,.6);border-radius:3px;background:rgba(142,142,147,.12)}
.mono{font-family:'DejaVu Sans Mono',monospace;font-weight:700;font-size:23px}
.sbtn{width:32px;height:32px;border-radius:8px;background:#0B2A6F;color:#fff;display:grid;place-items:center;font-size:20px}
.hdr{display:flex;flex-direction:column;align-items:center;gap:8px;padding:18px 0 14px}
.ht{font-size:22px;font-weight:700}.hs{font-size:15px;color:#6D6D72}
.act{color:#0B2A6F;font-weight:500}
.info{gap:12px;font-size:13px;line-height:1.35;color:#3C3C43;align-items:flex-start}
.ii{flex:none;width:18px;height:18px;border-radius:50%;border:1.6px solid #0B2A6F;color:#0B2A6F;font-size:11px;font-weight:800;display:grid;place-items:center;margin-top:1px}
.tabbar{position:absolute;left:0;right:0;bottom:0;height:84px;background:rgba(249,249,249,.94);border-top:.5px solid #C6C6C8;display:flex;justify-content:space-around;padding-top:7px}
.tab{display:flex;flex-direction:column;align-items:center;gap:2px;font-size:10px;font-weight:500;width:72px}
"""

def page(w, h, body):
    return f'<!doctype html><html lang="nl"><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="c" style="width:{w}px;height:{h}px">{body}</div></body></html>'

BANNERS = {}

# 1) Instagram/Facebook 1:1 – algemene lancering, schermen Mijn auto's + Opzoeken
BANNERS["instagram-post-1080x1080"] = (1080, 1080, f'''
<div class="glow" style="width:900px;height:900px;right:-300px;top:200px"></div>
<div style="position:absolute;left:72px;top:72px;width:600px">
 {brand(84, 46)}
 <h1 style="font-size:68px;margin-top:44px">Al je auto's.<br><em>Altijd bij de hand.</em></h1>
 <p class="sub" style="font-size:29px;margin-top:26px;width:540px">Elke auto die je ooit had, met kenteken of alleen merk en type. Met gegevens van de RDW.</p>
</div>
<div style="position:absolute;left:72px;bottom:72px">{badge(28)}<div class="url" style="font-size:26px;margin-top:20px">kent.lrvdlinden.app</div></div>
{phone("lookup", 320, "right:215px;top:640px;transform:rotate(-4deg)")}
{phone("cars", 360, "right:36px;top:330px")}
''')

# 2) Instagram/Facebook 4:5 – Kenteken terugvinden
BANNERS["instagram-post-1080x1350"] = (1080, 1350, f'''
<div class="glow" style="width:1000px;height:1000px;left:-420px;top:520px"></div>
<div style="position:absolute;left:72px;top:80px;right:72px">
 {brand(80, 44)}
 <h1 style="font-size:84px;margin-top:48px">Weet je je oude<br><em>kenteken nog?</em></h1>
 <p class="sub" style="font-size:32px;margin-top:26px;max-width:880px">Zoek op merk, model, kleur en bouwjaar en herken je auto in de RDW-gegevens.</p>
</div>
<div style="position:absolute;left:72px;top:720px">{big_plates(400)}</div>
<div style="position:absolute;left:72px;bottom:80px">{badge(28)}<div class="url" style="font-size:26px;margin-top:20px">kent.lrvdlinden.app</div></div>
{phone("find", 400, "right:60px;top:540px")}
''')

# 3) Story / Reels 1080×1920 – veilige zone 250 px boven en onder
BANNERS["story-1080x1920"] = (1080, 1920, f'''
<div class="glow" style="width:1200px;height:1200px;left:-60px;top:820px"></div>
<div style="position:absolute;left:80px;right:80px;top:270px;text-align:center;display:flex;flex-direction:column;align-items:center">
 <img src="{ICON}" style="width:150px;height:150px;border-radius:34px;box-shadow:0 10px 30px rgba(0,0,0,.4)">
 <h1 style="font-size:88px;margin-top:40px">Al je auto's<br><em>op één plek.</em></h1>
 <p class="sub" style="font-size:36px;margin-top:26px">Kenteken, catalogusprijs, BPM en bijtelling – met gegevens van de RDW.</p>
</div>
{phone("lookup", 400, "left:110px;top:900px;transform:rotate(-5deg)")}
{phone("cars", 430, "right:100px;top:840px")}
<div style="position:absolute;left:0;right:0;bottom:270px;display:flex;flex-direction:column;align-items:center;gap:18px;z-index:3">
 {badge(34)}<div class="url" style="font-size:30px">kent.lrvdlinden.app</div></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:780px;background:linear-gradient(180deg,rgba(7,20,54,0),rgba(7,20,54,.85) 35%,#071436 50%);z-index:2"></div>
''')

# 4) LinkedIn 1200×627 – fiscaal
BANNERS["linkedin-post-1200x627"] = (1200, 627, f'''
<div class="glow" style="width:800px;height:800px;right:-260px;top:-120px"></div>
<div style="position:absolute;left:72px;top:64px;width:640px">
 {brand(60, 34)}
 <h1 style="font-size:56px;margin-top:34px">Fiscale gegevens<br><em>uit een kenteken.</em></h1>
 <p class="sub" style="font-size:23px;margin-top:20px">Catalogusprijs, bruto BPM, eerste toelating en een indicatie van de bijtelling. Rechtstreeks van de RDW.</p>
 <div style="margin-top:30px;display:flex;align-items:center;gap:22px">{badge(20)}<span class="url" style="font-size:20px">kent.lrvdlinden.app</span></div>
</div>
{phone("lookup", 300, "right:90px;top:52px")}
''')

# 5) X / Bluesky / Threads 1600×900 – opzoeken + terugvinden
BANNERS["x-bluesky-threads-1600x900"] = (1600, 900, f'''
<div class="glow" style="width:1100px;height:1100px;right:-300px;top:-100px"></div>
<div style="position:absolute;left:96px;top:96px;width:700px">
 {brand(80, 44)}
 <h1 style="font-size:78px;margin-top:48px">Elk kenteken,<br><em>direct opgezocht.</em></h1>
 <p class="sub" style="font-size:31px;margin-top:28px">Techniek, APK, kilometerstandoordeel, catalogusprijs en bijtelling. En je vergeten kenteken terugvinden.</p>
</div>
<div style="position:absolute;left:96px;bottom:90px">{badge(28)}<div class="url" style="font-size:28px;margin-top:20px">kent.lrvdlinden.app</div></div>
{phone("find", 380, "right:400px;top:150px;transform:rotate(-4deg)")}
{phone("lookup", 400, "right:80px;top:96px")}
''')

# 6) Facebook-cover 1640×624 – inhoud binnen het midden
BANNERS["facebook-cover-1640x624"] = (1640, 624, f'''
<div class="glow" style="width:900px;height:900px;left:700px;top:-200px"></div>
<div style="position:absolute;left:260px;top:140px;width:640px">
 {brand(76, 42)}
 <h1 style="font-size:64px;margin-top:30px">Al je auto's.<br><em>Altijd bij de hand.</em></h1>
 <div style="margin-top:30px;display:flex;align-items:center;gap:24px">{badge(24)}<span class="url" style="font-size:24px">kent.lrvdlinden.app</span></div>
</div>
<div style="position:absolute;left:960px;top:150px">{big_plates(420)}</div>
''')

# 7) LinkedIn-cover 1584×396 – profielfoto valt linksonder, inhoud rechts
BANNERS["linkedin-cover-1584x396"] = (1584, 396, f'''
<div class="glow" style="width:700px;height:700px;left:500px;top:-200px"></div>
<div style="position:absolute;left:450px;top:62px;width:760px">
 {brand(64, 36)}
 <h1 style="font-size:46px;margin-top:22px">Al je auto's op <em>één plek.</em></h1>
 <div class="chips" style="margin-top:22px;font-size:17px;flex-wrap:nowrap"><span class="chip">Kenteken opzoeken</span><span class="chip">Kenteken terugvinden</span><span class="chip">Catalogusprijs &amp; BPM</span><span class="chip">Bijtelling</span></div>
</div>
<div style="position:absolute;right:80px;top:70px;text-align:right">{big_plates(280)}</div>
<div class="url" style="position:absolute;right:80px;bottom:44px;font-size:22px">kent.lrvdlinden.app</div>
''')

if __name__ == "__main__":
    only = sys.argv[2:]
    with sync_playwright() as p:
        b = p.chromium.launch()
        for name, (w, h, body) in BANNERS.items():
            if only and name not in only:
                continue
            pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=1)
            html = page(w, h, body)
            (HERE / "html").mkdir(exist_ok=True)
            (HERE / "html" / f"{name}.html").write_text(html, encoding="utf-8")
            pg.set_content(html)
            pg.wait_for_timeout(300)
            pg.screenshot(path=str(OUT / f"{name}.png"), clip={"x": 0, "y": 0, "width": w, "height": h})
            pg.close()
            print("ok", name)
        b.close()
