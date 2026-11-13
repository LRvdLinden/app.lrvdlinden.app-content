# -*- coding: utf-8 -*-
"""Rendert de nagebouwde Kentr-schermen (stap 1) en de App Store-screenshots en promobeelden (stap 2)."""
import sys, os, base64, pathlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from playwright.sync_api import sync_playwright
import screens as S
import compose as C

OUT = pathlib.Path(sys.argv[1])          # .../AppStore
RAW = pathlib.Path(sys.argv[2])          # map voor ruwe schermen
ICON = sys.argv[3]

DEVICES = {
    # naam: (logisch b, h, schaal, ipad, uitvoer b, h)
    "iphone-6.3": (402, 874, 3, False, 1206, 2622),
    "iphone-6.1": (393, 852, 3, False, 1179, 2556),
    "ipad-13":    (1032, 1376, 2, True, 2064, 2752),
    "ipad-12.9":  (1024, 1366, 2, True, 2048, 2732),
}

def shot(pg, html, w, h, dsf, path):
    pg.set_viewport_size({"width": w, "height": h})
    pg.set_content(html, wait_until="load")
    pg.evaluate("document.fonts.ready")
    pg.screenshot(path=str(path), clip={"x": 0, "y": 0, "width": w, "height": h})

with sync_playwright() as p:
    br = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--force-color-profile=srgb"])
    ctxs = {}
    for dsf in (1, 2, 3):
        ctxs[dsf] = br.new_context(device_scale_factor=dsf)
    pages = {k: v.new_page() for k, v in ctxs.items()}
    only = os.environ.get("ONLY")
    # stap 1: ruwe schermen
    for dev, (w, h, dsf, ipad, ow, oh) in DEVICES.items():
        (RAW / dev).mkdir(parents=True, exist_ok=True)
        for name, fn in S.SCREENS:
            if only and only not in name: continue
            shot(pages[dsf], S.page(fn(ipad), w, h, ipad), w, h, dsf, RAW / dev / f"{name}.png")
    if os.environ.get("RAWONLY"): sys.exit(0)
    # stap 2: screenshots met kop en toestelrand
    for dev, (w, h, dsf, ipad, ow, oh) in DEVICES.items():
        d = OUT / "screenshots" / "nl-NL" / dev
        d.mkdir(parents=True, exist_ok=True)
        for i, (name, fn) in enumerate(S.SCREENS):
            if only and only not in name: continue
            raw = RAW / dev / f"{name}.png"
            html = C.screenshot_page(i, raw, w, h, ipad, ow // dsf, oh // dsf)
            shot(pages[dsf], html, ow // dsf, oh // dsf, dsf, d / f"{name}_{ow}x{oh}.png")
    # stap 3: promobeelden
    m = OUT / "marketing" / "nl-NL"
    m.mkdir(parents=True, exist_ok=True)
    for fname, (cw, ch, dsf, kind) in C.MARKETING.items():
        html = C.marketing_page(kind, cw, ch, RAW, ICON)
        shot(pages[dsf], html, cw, ch, dsf, m / fname)
    br.close()
