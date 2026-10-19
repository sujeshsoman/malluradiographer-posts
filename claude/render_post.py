#!/usr/bin/env python3
"""Render the 1080x1080 @malluradiographer post JPG from claude/post-template.html (12 monthly themes).
usage: /usr/bin/python3 claude/render_post.py --title T --fact F --out file.jpg [--date YYYY-MM-DD] [--print-theme]
Month defaults to today's date in Europe/London. Needs playwright + pillow and chromium at /opt/pw-browsers/chromium."""
import argparse, datetime, os, zoneinfo
ap = argparse.ArgumentParser()
ap.add_argument("--title"); ap.add_argument("--fact"); ap.add_argument("--out"); ap.add_argument("--date")
ap.add_argument("--print-theme", action="store_true")
x = ap.parse_args()
d = datetime.date.fromisoformat(x.date) if x.date else datetime.datetime.now(zoneinfo.ZoneInfo("Europe/London")).date()
from playwright.sync_api import sync_playwright
tpl = "file://" + os.path.join(os.path.dirname(os.path.abspath(__file__)), "post-template.html")
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
    pg = b.new_page(viewport={"width": 1200, "height": 1200}); pg.goto(tpl)
    pg.select_option("#m", str(d.month))
    theme = pg.eval_on_selector("#m", "e=>e.options[e.selectedIndex].text")
    print("theme:", theme)
    if not x.print_theme:
        pg.evaluate("([t,f])=>{document.querySelector('#post [data-k=t]').textContent=t;document.querySelector('#post [data-k=f]').textContent=f}", [x.title, x.fact])
        pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(800)
        pg.locator("#post").screenshot(path=x.out + ".png"); b.close()
        from PIL import Image
        Image.open(x.out + ".png").convert("RGB").save(x.out, quality=93); os.remove(x.out + ".png"); print("saved", x.out)
