# -*- coding: utf-8 -*-
"""Kentr – nagebouwde app-schermen (HTML) op basis van de SwiftUI-code in Kentr/Views.
Alle kentekens zijn fictief: ze bevatten klinkers in zijcodes waarin de RDW geen klinkers uitgeeft."""

ACCENT = "#0B2A6F"      # Theme.accent / AccentColor (licht)
YELLOW = "#F5C400"
EUBLUE = "#003399"
NAVY = "#0B1F4B"
NAVY_DEEP = "#071436"
INK = "#111111"

# ---------- iconen (benaderingen van de SF Symbols) ----------
def svg(body, size, color="currentColor", vb="0 0 24 24", extra=""):
    return (f'<svg width="{size}" height="{size}" viewBox="{vb}" fill="{color}" '
            f'style="display:block;flex:none;color:{color}" {extra}>{body}</svg>')

CAR_FRONT = ('<path d="M18.92 6.01C18.72 5.42 18.16 5 17.5 5h-11c-.66 0-1.21.42-1.42 1.01L3 12v8c0 .55.45 1 1 1h1c.55 0 1-.45 1-1v-1h12v1c0 '
             '.55.45 1 1 1h1c.55 0 1-.45 1-1v-8l-2.08-5.99zM6.5 16c-.83 0-1.5-.67-1.5-1.5S5.67 13 6.5 13s1.5.67 1.5 1.5S7.33 16 6.5 16zm11 '
             '0c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zM5 11l1.5-4.5h11L19 11H5z"/>')
CAR_SIDE = ('<path d="M2.5 15.5v-3.2c0-.5.3-.9.8-1.1l2.6-1 2.6-3.3c.4-.5 1-.8 1.6-.8h4.6c.6 0 1.1.2 1.5.6l3.3 3.2 1.9.4c.6.1 1.1.7 1.1 '
            '1.3v3.9h-2a2.6 2.6 0 0 0-5.2 0H9.7a2.6 2.6 0 0 0-5.2 0zM9 10.2h3.6V7.9h-1.9c-.3 0-.5.1-.7.3zm5 0h4.1l-2.1-2c-.2-.2-.4-.3-.7-.3H14z"/>'
            '<circle cx="7.1" cy="16.2" r="1.9"/><circle cx="17.1" cy="16.2" r="1.9"/>')
BOLT = '<path d="M13.2 1.8 6 13h5l-1.2 9.2L17.8 10.6h-5.2z"/>'

def ic(name, size, color="currentColor"):
    s = 'stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round"'
    if name == "car2":
        b = (f'<g transform="translate(5,-3) scale(.82)" opacity=".55">{CAR_FRONT}</g>'
             f'<g transform="translate(-1,4) scale(.85)">{CAR_FRONT}</g>')
    elif name == "car":
        b = CAR_FRONT
    elif name == "carside":
        b = CAR_SIDE
    elif name == "boltcar":
        b = f'<g transform="translate(0,3) scale(.9)">{CAR_SIDE}</g><g transform="translate(9,-1) scale(.45)">{BOLT}</g>'
    elif name == "search":
        b = f'<g {s} stroke-width="2.4"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5 21 21"/></g>'
    elif name == "qdash":
        b = (f'<rect x="2.5" y="2.5" width="19" height="19" rx="4.5" {s} stroke-width="1.9" stroke-dasharray="3.2 2.6"/>'
             '<path d="M9.3 9.6c0-1.6 1.2-2.7 2.8-2.7s2.8 1 2.8 2.5c0 1.2-.7 1.8-1.6 2.4-.8.5-1.1.9-1.1 1.7v.4" '
             f'{s} stroke-width="2"/><circle cx="12.2" cy="16.8" r="1.25"/>')
    elif name == "chart":
        b = (f'<path d="M3 3v18h18" {s} stroke-width="1.9"/>'
             '<rect x="6.5" y="12" width="3" height="6.5" rx=".8"/><rect x="11.5" y="7" width="3" height="11.5" rx=".8"/>'
             '<rect x="16.5" y="9.5" width="3" height="9" rx=".8"/>')
    elif name == "gear":
        b = ('<path d="M19.14 12.94c.04-.3.06-.61.06-.94 0-.32-.02-.64-.07-.94l2.03-1.58c.18-.14.23-.41.12-.61l-1.92-3.32c-.12-.22-.37-.29-.59-.22l-2.39.96c-.5-.38-1.03-.7-1.62-.94l-.36-2.54c-.04-.24-.24-.41-.48-.41h-3.84c-.24 0-.43.17-.47.41l-.36 2.54c-.59.24-1.13.57-1.62.94l-2.39-.96c-.22-.08-.47 0-.59.22L2.74 8.87c-.12.21-.08.47.12.61l2.03 1.58c-.05.3-.09.63-.09.94s.02.64.07.94l-2.03 1.58c-.18.14-.23.41-.12.61l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h3.84c.24 0 .44-.17.47-.41l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32c.12-.22.07-.47-.12-.61l-2.01-1.58zM12 15.6c-1.98 0-3.6-1.62-3.6-3.6s1.62-3.6 3.6-3.6 3.6 1.62 3.6 3.6-1.62 3.6-3.6 3.6z"/>')
    elif name == "chev":
        b = f'<path d="M9 5l7 7-7 7" {s} stroke-width="2.6"/>'
    elif name == "back":
        b = f'<path d="M15.5 3.5 7 12l8.5 8.5" {s} stroke-width="2.8"/>'
    elif name == "plus":
        b = f'<path d="M12 4v16M4 12h16" {s} stroke-width="2.4"/>'
    elif name == "plusfill":
        b = '<circle cx="12" cy="12" r="10"/><path d="M12 7v10M7 12h10" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>'
    elif name == "share":
        b = f'<g {s} stroke-width="1.9"><path d="M8 9H6.5A1.5 1.5 0 0 0 5 10.5v9A1.5 1.5 0 0 0 6.5 21h11a1.5 1.5 0 0 0 1.5-1.5v-9A1.5 1.5 0 0 0 17.5 9H16"/><path d="M12 14V2.5M8.3 6 12 2.3 15.7 6"/></g>'
    elif name == "ellipsis":
        b = f'<circle cx="12" cy="12" r="9.5" {s} stroke-width="1.9"/><circle cx="7.6" cy="12" r="1.35"/><circle cx="12" cy="12" r="1.35"/><circle cx="16.4" cy="12" r="1.35"/>'
    elif name == "info":
        b = f'<circle cx="12" cy="12" r="9.5" {s} stroke-width="1.9"/><path d="M12 11v6" {s} stroke-width="2.2"/><circle cx="12" cy="7.6" r="1.3"/>'
    elif name == "faceid":
        b = (f'<g {s} stroke-width="1.9"><path d="M3 8V5.5A2.5 2.5 0 0 1 5.5 3H8M16 3h2.5A2.5 2.5 0 0 1 21 5.5V8M21 16v2.5a2.5 2.5 0 0 1-2.5 2.5H16M8 21H5.5A2.5 2.5 0 0 1 3 18.5V16"/>'
             '<path d="M8.5 8.5v1.5M15.5 8.5v1.5M12 8.5v4.5h-1M9 15.5c1.8 1.6 4.2 1.6 6 0"/></g>')
    elif name == "photo":
        b = (f'<g {s} stroke-width="1.8"><rect x="5.5" y="3" width="16" height="13" rx="2.5"/><path d="M2.5 7v11.5A2.5 2.5 0 0 0 5 21h13"/>'
             '<path d="m8 14 3.5-4 2.5 3 2-2 3.5 3.5"/></g><circle cx="16.5" cy="7" r="1.5"/>')
    elif name == "icloud":
        b = f'<path d="M7 19h10.5a4.5 4.5 0 0 0 .6-8.96A6 6 0 0 0 6.6 9.1 5 5 0 0 0 7 19z" {s} stroke-width="1.9"/>'
    elif name == "hand":
        b = (f'<path d="M7.5 12.5V5.8a1.4 1.4 0 0 1 2.8 0V11m0-6.6V3.9a1.4 1.4 0 0 1 2.8 0V11m0-6.1a1.4 1.4 0 0 1 2.8 0V11.5m0-4.2a1.4 1.4 0 0 1 2.8 0v6.9'
             f'c0 4.2-2.8 7.3-6.6 7.3-2.6 0-4.1-1.2-5.6-3.4l-2.5-3.8a1.4 1.4 0 0 1 2.3-1.6l1.1 1.5" {s} stroke-width="1.7"/>')
    elif name == "question":
        b = (f'<circle cx="12" cy="12" r="9.5" {s} stroke-width="1.9"/><path d="M9.4 9.4c0-1.5 1.2-2.6 2.7-2.6s2.7 1 2.7 2.4c0 1.1-.7 1.7-1.5 2.2-.8.5-1.2.9-1.2 1.7v.5" '
             f'{s} stroke-width="2"/><circle cx="12.1" cy="16.8" r="1.2"/>')
    elif name == "sparkles":
        b = '<path d="M10 2.5 11.8 8.2 17.5 10 11.8 11.8 10 17.5 8.2 11.8 2.5 10 8.2 8.2z"/><path d="M18 13.5l.9 2.6 2.6.9-2.6.9-.9 2.6-.9-2.6-2.6-.9 2.6-.9z"/>'
    elif name == "wave":
        b = (f'<path d="M8 13V6.3a1.3 1.3 0 0 1 2.6 0V12m0-6.8V4.3a1.3 1.3 0 0 1 2.6 0V12m0-6.2a1.3 1.3 0 0 1 2.6 0V12.5m0-3.8a1.3 1.3 0 0 1 2.6 0v5.8'
             f'c0 4-2.6 6.9-6.2 6.9-2.4 0-3.9-1.1-5.3-3.2l-2.4-3.6a1.3 1.3 0 0 1 2.2-1.5l1.3 1.8M2.5 6.5c.5-1.6 1.5-2.8 3-3.5" {s} stroke-width="1.6"/>')
    elif name == "columns":
        b = (f'<g {s} stroke-width="1.8"><path d="M3 9.5 12 4l9 5.5zM4 21h16M5 18.5h14M6.5 11v7M10 11v7M14 11v7M17.5 11v7"/></g>')
    elif name == "refresh":
        b = f'<g {s} stroke-width="2"><path d="M20 12a8 8 0 1 1-2.6-5.9"/><path d="M20 4v4.5h-4.5"/></g>'
    elif name == "lock":
        b = '<rect x="5" y="10.5" width="14" height="11" rx="2.5"/><path d="M8 10.5V7.5a4 4 0 0 1 8 0v3" stroke="currentColor" stroke-width="2" fill="none"/>'
    else:
        raise ValueError(name)
    return svg(b, size, color)

def staroflife(size, color):
    arms = "".join(f'<rect x="10.4" y="2" width="3.2" height="20" rx="1.2" transform="rotate({a} 12 12)"/>' for a in (0, 60, 120))
    return svg(arms, size, color)

# ---------- componenten ----------
def fmt_plate(p):
    """Kenteken.format: groepen van letters/cijfers, 4 → 2+2."""
    p = "".join(ch for ch in p.upper() if ch.isalnum())
    groups, cur, cur_d = [], "", None
    for ch in p:
        d = ch.isdigit()
        if cur_d is not None and cur_d != d:
            groups.append(cur); cur = ""
        cur += ch; cur_d = d
    if cur: groups.append(cur)
    if len(groups) == 1:
        return f"{p[0:2]}-{p[2:4]}-{p[4:6]}"
    if len(groups) == 2:
        out = []
        for g in groups:
            out += [g[:2], g[2:]] if len(g) == 4 else [g]
        return "-".join(out)
    return "-".join(groups)

def plate(p, h):
    r = h * 0.14
    bw = max(1, h * 0.045)
    return f'''<div class="plate" style="height:{h}px;border-radius:{r}px;box-shadow:inset 0 0 0 {bw}px rgba(17,17,17,.85)">
      <div style="width:{h*0.62}px;background:{EUBLUE};display:flex;flex-direction:column;align-items:center;justify-content:center;gap:{h*0.04}px">
        {staroflife(h*0.22, YELLOW)}
        <div style="font:700 {h*0.28}px/1 Inter;color:#fff;letter-spacing:.02em">NL</div></div>
      <div style="background:{YELLOW};padding:0 {h*0.3}px;display:flex;align-items:center;font:700 {h*0.58}px/1 'DejaVu Sans Mono';color:{INK};letter-spacing:-.02em">{fmt_plate(p)}</div>
    </div>'''

def unknown_badge(h):
    return f'''<div class="unk" style="height:{h}px;border-radius:{h*0.14}px;padding:0 {h*0.3}px;font-size:{h*0.36}px">
      {ic("qdash", h*0.42)}<span>Kenteken onbekend</span></div>'''

def thumb(electric, size=56):
    return f'''<div class="thumb" style="width:{size}px;height:{size}px;border-radius:{size*0.22}px">
      {ic("boltcar" if electric else "carside", size*0.46, YELLOW)}</div>'''

def row(label, value=None, *, sub=None, bold=False, muted=False, chev=False, icon=None, tint=False, raw=None, cls=""):
    if raw is not None:
        return f'<div class="row {cls}">{raw}</div>'
    lab = label
    if icon:
        lab = f'<span class="lbl">{ic(icon, 22, ACCENT)}<span style="color:{ACCENT if tint else "#000"}">{label}</span></span>'
    val = ""
    if value is not None:
        style = "font-weight:600;color:#000" if bold else ("color:rgba(60,60,67,.6)")
        v = f'<span style="{style}">{value}</span>'
        if sub:
            v = f'<span style="display:flex;flex-direction:column;align-items:flex-end"><span style="{style}">{value}</span><span class="cap">{sub}</span></span>'
        val = v
    ch = f'<span style="color:#C4C4C7;margin-left:8px">{ic("chev", 14)}</span>' if chev else ""
    if "picker" in cls:
        ch = ('<svg width="9" height="14" viewBox="0 0 9 14" style="margin-left:6px"><path d="M1.5 5 4.5 2l3 3M1.5 9l3 3 3-3" '
              'stroke="rgba(60,60,67,.6)" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>')
    return f'<div class="row {cls}"><span class="rl">{lab}</span><span class="rv">{val}{ch}</span></div>'

def section(rows, header=None, footer=None, plain=False):
    h = f'<div class="sh">{header}</div>' if header else ""
    f = f'<div class="sf">{footer}</div>' if footer else ""
    body = "".join(rows)
    box = body if plain else f'<div class="card">{body}</div>'
    return f'<div class="sec">{h}{box}{f}</div>'

def toggle(on=True):
    return f'<span class="tg {"on" if on else ""}"><i></i></span>'

# ---------- schermen ----------
def scr_cars(ipad):
    cars_now = [("Volkswagen ID.3", "A427EU", "Sinds maart 2023", True)]
    cars_before = [
        ("Skoda Octavia", "EA412U", "juni 2016 – februari 2023", False),
        ("Opel Astra", "61UEAO", "2011 – 2016", False),
        ("Peugeot 206", "OEAI55", "2004 – 2011", False),
        ("Volkswagen Golf", "", "1999 – 2004", False),
    ]
    def car_row(t, p, per, el):
        pl = plate(p, 22) if p else unknown_badge(22)
        return row(None, raw=f'''<div class="carrow">{thumb(el)}<div class="cv">
            <div class="ct">{t}</div>{pl}<div class="cap">{per}</div></div>
            <span style="color:#C4C4C7;margin-left:auto">{ic("chev", 14)}</span></div>''')
    body = (f'<div class="search">{ic("search", 17, "rgba(60,60,67,.6)")}<span>Merk, model, kenteken of jaar</span></div>'
            + section([car_row(*c) for c in cars_now], "Nu in bezit")
            + section([car_row(*c) for c in cars_before], "Eerder"))
    return dict(title="Mijn auto's", large=True, tab=0, body=body,
                trailing=[ic("plus", 22, ACCENT)])

def lookup_top(p="EA412U"):
    field = row(None, raw=f'''<div style="display:flex;align-items:center;width:100%;gap:12px">
        <span style="font:700 22px/1 'DejaVu Sans Mono';color:#000;flex:1">{fmt_plate(p)}</span>
        <span class="pbtn">{ic("search", 17, "#fff")}</span></div>''')
    return section([field], "Kenteken",
                   "Zoek elk Nederlands kenteken op: techniek, catalogusprijs, BPM, bijtelling en APK.")

def vehicle_header(p, title, sub):
    pl = plate(p, 46) if p else unknown_badge(40)
    return f'''<div class="vh">{pl}<div class="vt">{title}</div><div class="vs">{sub}</div></div>'''

SKODA_VOERTUIG = [
    ("Merk", "Skoda"), ("Model", "Octavia"), ("Voertuigsoort", "Personenauto"), ("Carrosserie", "Stationwagen"),
    ("Kleur", "Grijs"), ("Bouwjaar", "2016"), ("Brandstof", "Benzine"), ("Vermogen", "85 kW (116 pk)"),
    ("Cilinderinhoud", "999 cc"), ("Massa rijklaar", "1.315 kg"), ("Zitplaatsen", "5"), ("Deuren", "4"),
    ("Verbruik (gecombineerd)", "4,8 l/100 km"),
]

def scr_lookup(ipad):
    actions = section([row("Toevoegen aan mijn auto's", icon="plusfill", tint=True),
                       row("Deel", icon="share", tint=True)])
    body = (lookup_top() + vehicle_header("EA412U", "Skoda Octavia", "Bouwjaar 2016") + actions
            + section([row(a, b) for a, b in SKODA_VOERTUIG], "Voertuig"))
    return dict(title="Opzoeken", large=True, tab=1, body=body)

def scr_fiscal(ipad):
    fis = section([
        row("Catalogusprijs", "€ 28.490"), row("Bruto BPM", "€ 3.612"),
        row("Eerste toelating", "14 juni 2016"), row("Eerste toelating in NL", "14 juni 2016"),
        row("Laatste tenaamstelling", "2 maart 2023"), row("CO2-uitstoot", "106 g/km")],
        "Fiscaal", "De catalogusprijs is de fiscale waarde: de basis voor de bijtelling. Gegevens van de RDW, geen fiscaal advies.")
    bij = section([
        row("Percentage", "22%"), row("Per maand", "€ 522", bold=True), row("Per jaar", "€ 6.268"),
        row("Tarief vast t/m", "30 juni 2031"),
        row(None, raw='<span class="fn">Standaardtarief van 22% van de catalogusprijs.</span>')],
        "Bijtelling (indicatie)",
        "Als auto van de zaak met meer dan 500 km privé per jaar. Bruto bedrag dat bij je inkomen wordt opgeteld; wat je netto betaalt hangt af van je belastingschijf. Tarieven t/m 2027. Geen fiscaal advies.")
    st = section([
        row("APK geldig tot", "14 juni 2027"), row("Kilometerstand", "Logisch", sub="Laatst geregistreerd in 2026"),
        row("WAM-verzekerd", "Ja"), row("Open terugroepactie", "Nee")], "Status")
    tail = section([row(a, b) for a, b in SKODA_VOERTUIG[-2:]], None)
    body = f'<div style="margin-top:-30px">{tail}</div>' + fis + bij + st
    return dict(title="Opzoeken", large=False, tab=1, body=body)

def scr_find(ipad):
    auto = section([row("Merk (bv. Volkswagen)", raw='<span style="color:#000">VOLKSWAGEN</span>'),
                    row(None, raw='<span style="color:#000">Golf</span>'),
                    row("Kleur", "Rood", chev=False, cls="picker")], "Auto")
    bj = section([row("Van", "1994", cls="picker"), row("Tot en met", "1994", cls="picker")],
                 "Bouwjaar (eerste toelating)", "Hoe kleiner de periode, hoe korter de lijst.")
    btn = section([row(None, raw=f'<span style="display:flex;gap:8px;align-items:center;justify-content:center;width:100%;color:{ACCENT}">{ic("search", 19, ACCENT)}Zoek kentekens</span>')])
    results = [("AE41UO", "3 maart 1994"), ("EU17AI", "18 april 1994"), ("IO62EA", "9 mei 1994"),
               ("UA08OE", "27 juni 1994"), ("OI35UE", "12 augustus 1994"), ("EA90IU", "4 oktober 1994"),
               ("AU23IE", "21 november 1994")]
    rr = [row(None, raw=f'''<div style="display:flex;align-items:center;gap:12px;width:100%">{plate(p, 26)}
            <div style="display:flex;flex-direction:column;gap:2px"><span style="font:600 15px/1.2 Inter">Golf</span>
            <span class="cap">Rood · {d}</span></div><span style="color:#C4C4C7;margin-left:auto">{ic("chev", 14)}</span></div>''')
          for p, d in results]
    res = section(rr, "23 resultaten")
    body = f'<div style="margin-top:-6px"></div>' + auto + bj + btn + res
    return dict(title="Terugvinden", large=False, tab=2, body=body)

def scr_detail(ipad):
    mine = section([
        row("Periode", "1999 – 2004"), row("In bezit", "5 jaar"), row("Bouwjaar", "1994"),
        row("Kleur", "Rood"), row("Hoe gekregen", "Tweedehands gekocht")],
        "Mijn gegevens")
    notes = section([row(None, raw='<span style="color:#000">Mijn eerste auto, gekocht van oom Jan.</span>')], "Notities")
    find = section([row(None, raw=f'''<span class="lbl">{ic("search", 20, ACCENT)}<span>Kenteken terugvinden</span></span>
                    <span style="color:#C4C4C7;margin-left:auto">{ic("chev", 14)}</span>''')], None,
                   "Zoek in de RDW-gegevens op merk, model, kleur en bouwjaar en herken je oude kenteken.")
    body = vehicle_header("", "Volkswagen Golf", "1999 – 2004") + mine + notes + find
    return dict(title="Volkswagen Golf", large=False, tab=0, body=body, back="Mijn auto's",
                trailing=[ic("share", 22, ACCENT), ic("ellipsis", 22, ACCENT)])

def scr_stats(ipad):
    tiles = "".join(f'<div class="tile"><div class="tv">{v}</div><div class="cap">{l}</div></div>'
                    for v, l in (("5", "Auto's"), ("4", "Merken"), ("1", "Nu in bezit")))
    bezit = section([
        row("Totaal", "27 jaar en 4 maanden"), row("Gemiddeld per auto", "5 jaar en 5 maanden"),
        row("Langst gehouden", "Peugeot 206", sub="7 jaar"), row("Eerste auto", "Volkswagen Golf"),
        row("Zelf gereden", "106.500 km"), row("Zonder kenteken", "1")], "Bezit")
    merken = section([row(a, b) for a, b in (("Volkswagen", "2"), ("Opel", "1"), ("Peugeot", "1"), ("Skoda", "1"))], "Merken")
    brand = section([row(a, b) for a, b in (("Benzine", "4"), ("Elektriciteit", "1"))], "Brandstof")
    dec = section([row(a, b) for a, b in (("Jaren 1990", "1"), ("Jaren 2000", "1"), ("Jaren 2010", "2"), ("Jaren 2020", "1"))], "Per decennium")
    body = f'<div class="tiles">{tiles}</div>' + bezit + merken + brand + dec
    return dict(title="Overzicht", large=True, tab=3, body=body)

def scr_settings(ipad):
    def tl(icon, text):
        return row(None, raw=f'<span class="lbl">{ic(icon, 22, ACCENT)}<span>{text}</span></span><span style="margin-left:auto">{toggle(True)}</span>')
    sec1 = section([tl("faceid", "Vergrendel met Face ID")], "Beveiliging",
                   "Bij openen en na terugkeer naar de app wordt om Face ID gevraagd.")
    sec2 = section([tl("photo", "Zoek automatisch een voorbeeldfoto")], "Foto's",
                   "Na het invoeren van een kenteken zoekt Kentr een vrije foto van hetzelfde merk en model op Wikimedia Commons, met bronvermelding. Je kunt hem altijd vervangen door een eigen foto.")
    sec3 = section([row(None, raw=f'<span class="lbl">{ic("icloud", 22, ACCENT)}<span>Synchroniseert via iCloud</span></span>')], None,
                   "Je auto's staan in je eigen iCloud en zijn zo ook op je iPad beschikbaar. Kentr heeft geen eigen server.")
    sec4 = section([row("Weergave", "Automatisch", cls="picker")], "Weergave")
    links = section([row(t, icon=i, tint=True) for i, t in (
        ("hand", "Privacyverklaring"), ("question", "Support en contact"), ("sparkles", "Wat is nieuw"),
        ("wave", "Toon het welkomstscherm"), ("columns", "Bron: RDW Open Data"))])
    body = sec1 + sec2 + sec3 + sec4 + links
    return dict(title="Instellingen", large=True, tab=4, body=body)

SCREENS = [
    ("01_mijn-autos", scr_cars),
    ("02_opzoeken", scr_lookup),
    ("03_fiscaal-bijtelling", scr_fiscal),
    ("04_terugvinden", scr_find),
    ("05_zonder-kenteken", scr_detail),
    ("06_overzicht", scr_stats),
    ("07_faceid-icloud", scr_settings),
]

TABS = [("car2", "Mijn auto's"), ("search", "Opzoeken"), ("qdash", "Terugvinden"), ("chart", "Overzicht"), ("gear", "Instellingen")]

CSS = f"""
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{background:#F2F2F7;font-family:Inter,sans-serif;-webkit-font-smoothing:antialiased;font-feature-settings:'cv11','ss01'}}
.screen{{position:relative;overflow:hidden;background:#F2F2F7}}
.sb{{position:absolute;left:0;right:0;top:0;display:flex;align-items:center;justify-content:space-between;z-index:5;font:600 17px/1 Inter;color:#000}}
.nav{{position:absolute;left:0;right:0;z-index:4}}
.navbar{{height:44px;display:flex;align-items:center;justify-content:space-between;padding:0 16px}}
.navinline{{background:rgba(249,249,249,.97);backdrop-filter:blur(20px);border-bottom:.5px solid rgba(0,0,0,.18)}}
.navtitle{{font:600 17px/1 Inter;color:#000;position:absolute;left:0;right:0;text-align:center;pointer-events:none}}
.large{{font:700 34px/1.1 Inter;letter-spacing:-.01em;color:#000;padding:2px 16px 8px}}
.content{{position:absolute;left:0;right:0}}
.sec{{margin:0 0 35px}}
.sh{{font:400 13px/1.3 Inter;text-transform:uppercase;color:rgba(60,60,67,.6);padding:0 16px 7px 16px;letter-spacing:.01em}}
.sf{{font:400 13px/1.35 Inter;color:rgba(60,60,67,.6);padding:7px 16px 0}}
.card{{background:#fff;border-radius:10px;overflow:hidden}}
.row{{min-height:44px;display:flex;align-items:center;justify-content:space-between;padding:11px 16px;font:400 17px/1.25 Inter;color:#000;position:relative;gap:12px}}
.row+.row::before{{content:"";position:absolute;top:0;left:16px;right:0;border-top:.5px solid rgba(60,60,67,.29)}}
.rl{{flex:none}}
.rv{{display:flex;align-items:center;text-align:right}}
.lbl{{display:flex;align-items:center;gap:14px}}
.cap{{font:400 12px/1.3 Inter;color:rgba(60,60,67,.6)}}
.fn{{font:400 13px/1.35 Inter;color:rgba(60,60,67,.6)}}
.picker .rv span{{color:rgba(60,60,67,.6)}}
.plate{{display:inline-flex;overflow:hidden;flex:none;align-self:flex-start}}
.unk{{display:inline-flex;align-items:center;gap:6px;font-family:Inter;font-weight:600;color:rgba(60,60,67,.6);
  background:rgba(120,120,128,.12);border:1px dashed rgba(60,60,67,.4);align-self:flex-start}}
.thumb{{background:linear-gradient({NAVY},{NAVY_DEEP});display:flex;align-items:center;justify-content:center;flex:none}}
.carrow{{display:flex;align-items:center;gap:14px;width:100%;padding:4px 0}}
.cv{{display:flex;flex-direction:column;gap:6px}}
.ct{{font:600 17px/1.2 Inter}}
.search{{margin:2px 16px 18px;height:36px;border-radius:10px;background:rgba(118,118,128,.12);display:flex;align-items:center;gap:6px;padding:0 8px;
  font:400 17px/1 Inter;color:rgba(60,60,67,.6)}}
.pbtn{{width:46px;height:38px;border-radius:9px;background:{ACCENT};display:flex;align-items:center;justify-content:center}}
.vh{{display:flex;flex-direction:column;align-items:center;gap:10px;padding:8px 0 26px}}
.vh .plate,.vh .unk{{align-self:center}}
.vt{{font:700 22px/1.2 Inter;color:#000}}
.vs{{font:400 15px/1.2 Inter;color:rgba(60,60,67,.6)}}
.tiles{{display:flex;gap:12px;margin-bottom:35px}}
.tile{{flex:1;background:#fff;border-radius:16px;padding:14px 0;display:flex;flex-direction:column;align-items:center;gap:4px}}
.tv{{font:700 28px/1.1 Inter;color:{ACCENT}}}
.tile .cap{{font-size:12px}}
.tg{{width:51px;height:31px;border-radius:16px;background:#E9E9EA;position:relative;display:inline-block}}
.tg.on{{background:#34C759}}
.tg i{{position:absolute;top:2px;left:2px;width:27px;height:27px;border-radius:50%;background:#fff;box-shadow:0 3px 8px rgba(0,0,0,.15)}}
.tg.on i{{left:22px}}
.tabbar{{position:absolute;left:0;right:0;bottom:0;background:rgba(249,249,249,.97);backdrop-filter:blur(20px);border-top:.5px solid rgba(0,0,0,.2);display:flex;z-index:6}}
.tab{{flex:1;display:flex;flex-direction:column;align-items:center;gap:3px;padding-top:7px;font:500 10px/1 Inter;color:#8E8E93}}
.tab.sel{{color:{ACCENT}}}
.home{{position:absolute;bottom:8px;left:50%;transform:translateX(-50%);width:139px;height:5px;border-radius:3px;background:#000;z-index:7}}
.ipadtabs{{position:absolute;top:30px;left:50%;transform:translateX(-50%);display:flex;gap:2px;padding:5px;border-radius:24px;
  background:rgba(255,255,255,.9);box-shadow:0 2px 16px rgba(0,0,0,.08);z-index:6}}
.ipadtabs span{{white-space:nowrap;padding:9px 18px;border-radius:19px;font:500 15px/1 Inter;color:#000}}
.ipadtabs span.sel{{background:rgba(118,118,128,.12);color:{ACCENT};font-weight:600}}
"""

def status_bar(ipad, w):
    batt = ('<svg width="27" height="13" viewBox="0 0 27 13"><rect x=".5" y=".5" width="23" height="12" rx="3.5" fill="none" stroke="#000" opacity=".4"/>'
            '<rect x="2" y="2" width="20" height="9" rx="2" fill="#000"/><rect x="24.5" y="4.3" width="1.6" height="4.4" rx=".8" fill="#000" opacity=".45"/></svg>')
    wifi = ('<svg width="17" height="12" viewBox="0 0 17 12"><path d="M8.5 2.3c2.3 0 4.4.9 6 2.4l1.2-1.2A10.2 10.2 0 0 0 8.5.6 10.2 10.2 0 0 0 1.3 3.5l1.2 1.2a8.5 8.5 0 0 1 6-2.4z'
            'M8.5 5.6c1.4 0 2.7.5 3.7 1.4l1.2-1.2a7 7 0 0 0-9.8 0L4.8 7a5.4 5.4 0 0 1 3.7-1.4zM8.5 8.8c.6 0 1.1.2 1.5.6L8.5 11 7 9.4c.4-.4.9-.6 1.5-.6z" fill="#000"/></svg>')
    cell = ('<svg width="18" height="12" viewBox="0 0 18 12">' + "".join(
        f'<rect x="{i*5}" y="{9-i*3}" width="3" height="{3+i*3}" rx="1" fill="#000"/>' for i in range(4)) + '</svg>')
    if ipad:
        return (f'<div class="sb" style="height:24px;padding:0 22px;font-size:15px"><span>9:41&nbsp;&nbsp;do 13 nov.</span>'
                f'<span style="display:flex;gap:7px;align-items:center">{wifi}<span style="font-size:14px">100%</span>{batt}</span></div>')
    return (f'<div class="sb" style="height:54px;padding:6px 36px 0 50px"><span>9:41</span>'
            f'<span style="display:flex;gap:7px;align-items:center">{cell}{wifi}{batt}</span></div>')

def render_screen(spec, w, h, ipad):
    sb_h = 24 if ipad else 54
    pad = 40 if ipad else 16
    top = sb_h
    nav_html = ""
    if ipad:
        top += 64
    trailing = "".join(f'<span style="margin-left:18px">{t}</span>' for t in spec.get("trailing", []))
    back = spec.get("back")
    lead = (f'<span style="display:flex;align-items:center;gap:4px;color:{ACCENT};font:400 17px/1 Inter;margin-left:-8px">'
            f'{ic("back", 22, ACCENT)}{back}</span>') if back else "<span></span>"
    if spec["large"]:
        nav_html = (f'<div class="nav" style="top:{top}px;padding:0 {pad-16}px"><div class="navbar">{lead}<span style="display:flex">{trailing}</span></div>'
                    f'<div class="large">{spec["title"]}</div></div>')
        content_top = top + 44 + 52
    else:
        nav_html = (f'<div class="nav navinline" style="top:0;padding:{top}px {pad-16}px 0"><div class="navbar" style="position:relative">{lead}'
                    f'<span class="navtitle">{spec["title"]}</span><span style="display:flex">{trailing}</span></div></div>')
        content_top = top + 44 + 20
    if ipad:
        tabs = "".join(f'<span class="{"sel" if i == spec["tab"] else ""}">{t}</span>' for i, (_, t) in enumerate(TABS))
        tabbar = f'<div class="ipadtabs">{tabs}</div><div class="home" style="width:315px"></div>'
        bottom = 0
    else:
        tabs = "".join(f'<div class="tab {"sel" if i == spec["tab"] else ""}">{ic(icn, 26)}<span>{t}</span></div>' for i, (icn, t) in enumerate(TABS))
        tabbar = f'<div class="tabbar" style="height:83px">{tabs}</div><div class="home"></div>'
    side = pad
    return f'''<div class="screen" style="width:{w}px;height:{h}px">
      {status_bar(ipad, w)}
      {nav_html}
      <div class="content" style="top:{content_top}px;padding:0 {side}px">{spec["body"]}</div>
      {tabbar}
    </div>'''

def page(spec, w, h, ipad):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{render_screen(spec, w, h, ipad)}</body></html>'
