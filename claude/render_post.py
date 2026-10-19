#!/usr/bin/env python3
"""Render a 1080x1080 @malluradiographer post JPG (same layout as the canvas board).
usage: python3 render_post.py --title T --fact F --assets DIR --fonts DIR --out file.jpg [--date YYYY-MM-DD]
DIR assets holds 5be526d01cfbbeaf9b96bf3bec4502d8.png (yellow logo); fonts holds the two woff2 files.
Themes below are the ones confirmed so far; add the rest of the 12 monthly themes here."""
import argparse, base64, html, datetime, zoneinfo
THEMES = {10: dict(name="Classic neon navy", bg="#04070D", blue="#2F8CFF", green="#2BF5A0",
                   logo="5be526d01cfbbeaf9b96bf3bec4502d8", radius=0, backdrop="grid")}
def a(h, al):
    n = int(h[1:], 16); return f"rgba({n>>16&255}, {n>>8&255}, {n&255}, {al:.3f})"
def b64(p): return base64.b64encode(open(p, "rb").read()).decode()
ap = argparse.ArgumentParser()
for k in ("title", "fact", "assets", "fonts", "out"): ap.add_argument("--" + k, required=True)
ap.add_argument("--date"); ap.add_argument("--print-theme", action="store_true")
x = ap.parse_args()
d = datetime.date.fromisoformat(x.date) if x.date else datetime.datetime.now(zoneinfo.ZoneInfo("Europe/London")).date()
t = THEMES.get(d.month) or THEMES[10]
g, blue, green = .6, t["blue"], t["green"]
grid = a(blue, .16)
f1 = b64(f"{x.fonts}/space-grotesk-latin-700-normal.woff2"); f2 = b64(f"{x.fonts}/manrope-latin-500-normal.woff2")
logo = b64(f"{x.assets}/{t['logo']}.png")
page = f"""<!doctype html><meta charset=utf-8><style>
@font-face{{font-family:'Space Grotesk';font-weight:700;src:url(data:font/woff2;base64,{f1})}}
@font-face{{font-family:'Manrope';font-weight:500;src:url(data:font/woff2;base64,{f2})}}
body{{margin:0}}</style>
<div style="width:1080px;height:1080px;position:relative;overflow:hidden;background:{t['bg']};display:flex;align-items:center;justify-content:center;font-family:'Manrope';color:#F2F6FC">
<div style="position:absolute;left:-260px;top:-260px;width:820px;height:820px;border-radius:50%;background:radial-gradient(circle,{a(blue,.6*g)} 0%,{a(blue,0)} 68%)"></div>
<div style="position:absolute;right:-280px;bottom:-280px;width:860px;height:860px;border-radius:50%;background:radial-gradient(circle,{a(green,.45*g)} 0%,{a(green,0)} 68%)"></div>
<div style="position:absolute;inset:0;background-image:linear-gradient({grid} 1px,transparent 1px),linear-gradient(90deg,{grid} 1px,transparent 1px);background-size:54px 54px;-webkit-mask-image:radial-gradient(ellipse at center,#000 20%,transparent 78%)"></div>
<div style="position:absolute;inset:0;background:radial-gradient(ellipse at center,rgba(0,0,0,0) 45%,rgba(0,0,0,.55) 100%)"></div>
<div style="position:relative;width:860px;box-sizing:border-box;padding:84px 80px;display:flex;flex-direction:column;gap:36px;text-align:center;background:rgba(6,11,22,.65);border:1px solid {a(blue,.24)};border-radius:32px;box-shadow:0 30px 80px rgba(0,0,0,.55),0 0 90px {a(green,.12*g)}">
<h1 style="margin:0;font-family:'Space Grotesk';font-weight:700;font-size:62px;line-height:1.08;letter-spacing:-.015em;text-wrap:balance;color:#fff">{html.escape(x.title)}</h1>
<div style="width:72px;height:4px;border-radius:2px;background:{green};box-shadow:0 0 14px {a(green,.75)};margin:0 auto"></div>
<p style="margin:0;font-size:32px;line-height:1.45;font-weight:500;color:#C6D3E5">{html.escape(x.fact)}</p></div>
<img src="data:image/png;base64,{logo}" style="position:absolute;right:44px;bottom:36px;width:160px;border-radius:{t['radius']}px;filter:drop-shadow(0 6px 14px rgba(0,0,0,.55))"></div>"""
from playwright.sync_api import sync_playwright
from PIL import Image
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
    pg = b.new_page(viewport={"width": 1080, "height": 1080}); pg.set_content(page); pg.wait_for_timeout(800)
    pg.screenshot(path=x.out + ".png"); b.close()
Image.open(x.out + ".png").convert("RGB").save(x.out, quality=93)
print("theme:", t["name"], "->", x.out)
