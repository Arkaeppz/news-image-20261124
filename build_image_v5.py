#!/usr/bin/env python3
"""build_image_v5.py — one-day world news broadsheet, v5 template.

Data-driven: a DAY dict (date line, kicker, timeline, stories, numbers,
also-list, map pins, date-check) renders to a 1024x1024 PNG in the champion
formula's family — illustrated story cards, a dotted world map with pins, a
UTC timeline and a date-check box — with our own execution: one hero story,
bigger headline type, fewer words per card, duotone scene illustrations.

v4 upgrades (from the ni23 final-leaderboard analysis): every card scene
carries a bold figure PILL (the story's key number as a banner inside the
art); the also-list runs to ~25 briefs, each with its source right-aligned;
the footer DEFINES the certainty tiers, including an OFFICIAL tier.

Scenes are small flat painters keyed by name; a story picks one plus an
optional big label drawn inside the art (a score, a count).
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANSB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SERIFB = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIFI = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"

INK = (27, 38, 54)
NAVY = (22, 50, 79)
RED = (178, 34, 33)
REDD = (140, 24, 22)
GOLD = (232, 163, 61)
GREEN = (47, 125, 70)
PAPER = (247, 240, 224)
CARD = (255, 252, 244)
GREY = (96, 104, 112)
SKY = (203, 224, 240)
SEA = (64, 116, 158)

def F(path, size):
    return ImageFont.truetype(path, size)

def fitw(d, text, font, maxw):
    while text and d.textlength(text, font=font) > maxw:
        text = text[:-1]
    return text

def wrap(d, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines

def block(d, x, y, text, font, fill, maxw, leading, max_lines):
    for i, ln in enumerate(wrap(d, text, font, maxw)[:max_lines]):
        d.text((x, y + i * leading), ln, font=font, fill=fill)
    return y + min(len(wrap(d, text, font, maxw)), max_lines) * leading

# ---------------------------------------------------------------- scenes
# Each painter draws inside (x, y, w, h) and may use `label` (a big score or
# count) and `sub` (a small caption inside the art).

def sc_summit(d, x, y, w, h, label="", sub=""):
    d.rectangle([x, y, x + w, y + h], fill=(226, 233, 240))
    # document
    dx, dy, dw, dh = x + w * 0.16, y + h * 0.14, w * 0.4, h * 0.74
    d.rectangle([dx, dy, dx + dw, dy + dh], fill=(255, 255, 255), outline=INK, width=2)
    d.text((dx + 6, dy + 3), "DRAFT", font=F(SANSB, max(9, int(h * 0.11))), fill=RED)
    for i in range(3):
        ly = dy + 16 + i * (dh / 4.5)
        d.line([dx + 8, ly, dx + dw - 8, ly], fill=GREY, width=2)
    d.line([dx + 8, dy + dh - 9, dx + dw * 0.55, dy + dh - 9], fill=RED, width=3)
    # clock
    cx, cy, r = x + w * 0.76, y + h * 0.46, h * 0.3
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 255, 255), outline=INK, width=3)
    d.line([cx, cy, cx, cy - r * 0.62], fill=INK, width=3)
    d.line([cx, cy, cx + r * 0.5, cy + r * 0.3], fill=INK, width=3)

def sc_drones(d, x, y, w, h, label="", sub=""):
    d.rectangle([x, y, x + w, y + h], fill=(24, 34, 58))
    for sx, sy in [(0.12, 0.2), (0.3, 0.1), (0.55, 0.22), (0.85, 0.12), (0.68, 0.08)]:
        d.ellipse([x + w * sx, y + h * sy, x + w * sx + 3, y + h * sy + 3], fill=(255, 240, 190))
    # skyline
    bx = x + 4
    heights = [0.42, 0.6, 0.35, 0.52, 0.44, 0.62, 0.38]
    bw = (w - 8) / len(heights)
    for i, hh in enumerate(heights):
        top = y + h * (1 - hh)
        d.rectangle([bx + i * bw, top, bx + (i + 1) * bw - 2, y + h], fill=(10, 16, 28))
        for wy in range(2):
            d.rectangle([bx + i * bw + 3, top + 5 + wy * 9, bx + i * bw + 7, top + 9 + wy * 9], fill=GOLD)
    # drones
    for dxr, dyr, s in [(0.2, 0.3, 1.0), (0.48, 0.18, 0.8), (0.74, 0.34, 1.1)]:
        cx, cy = x + w * dxr, y + h * dyr
        d.line([cx - 9 * s, cy, cx + 9 * s, cy], fill=(255, 120, 90), width=2)
        d.line([cx, cy - 4 * s, cx, cy + 5 * s], fill=(255, 120, 90), width=2)
        d.ellipse([cx - 2, cy - 2, cx + 2, cy + 2], fill=(255, 160, 120))

def sc_radar(d, x, y, w, h, label="", sub=""):
    d.rectangle([x, y, x + w, y + h], fill=(238, 228, 205))
    d.rectangle([x, y + h * 0.78, x + w, y + h], fill=(196, 164, 110))
    # dish
    cx, cy = x + w * 0.3, y + h * 0.52
    d.line([cx, cy + h * 0.26, cx, cy], fill=INK, width=4)
    d.arc([cx - w * 0.16, cy - h * 0.3, cx + w * 0.16, cy + h * 0.3], start=300, end=60, fill=NAVY, width=5)
    d.line([cx, cy, cx + w * 0.13, cy - h * 0.16], fill=NAVY, width=3)
    # signal waves, one side denied
    for i, r in enumerate([0.12, 0.2, 0.28]):
        d.arc([cx + w * 0.08 - w * r, cy - h * 0.2 - h * r, cx + w * 0.08 + w * r, cy - h * 0.2 + h * r], start=300, end=350, fill=GREEN, width=3)
    rx, ry = x + w * 0.72, y + h * 0.3
    d.line([rx - 12, ry - 12, rx + 12, ry + 12], fill=RED, width=5)
    d.line([rx + 12, ry - 12, rx - 12, ry + 12], fill=RED, width=5)
    d.text((x + w * 0.58, y + h * 0.62), "DENIED", font=F(SANSB, max(9, int(h * 0.13))), fill=RED)

def sc_fire(d, x, y, w, h, label="", sub=""):
    d.rectangle([x, y, x + w, y + h], fill=(240, 226, 205))
    bx, by, bw, bh = x + w * 0.18, y + h * 0.3, w * 0.64, h * 0.62
    d.rectangle([bx, by, bx + bw, by + bh], fill=(150, 96, 62))
    d.polygon([(bx - 4, by), (bx + bw + 4, by), (bx + bw * 0.5, by - h * 0.16)], fill=REDD)
    for i in range(3):
        for j in range(2):
            d.rectangle([bx + 8 + i * (bw / 3), by + 8 + j * (bh / 2.4), bx + 8 + i * (bw / 3) + bw / 6, by + 8 + j * (bh / 2.4) + bh / 5], fill=(60, 44, 34))
    # flames
    for fx, fs in [(0.3, 1.0), (0.52, 1.3), (0.72, 0.9)]:
        cx, base = x + w * fx, by + 4
        d.polygon([(cx - 9 * fs, base), (cx, base - h * 0.34 * fs), (cx + 9 * fs, base)], fill=(232, 110, 40))
        d.polygon([(cx - 5 * fs, base), (cx, base - h * 0.2 * fs), (cx + 5 * fs, base)], fill=GOLD)

def sc_ballot(d, x, y, w, h, label="", sub=""):
    d.rectangle([x, y, x + w, y + h], fill=(232, 238, 244))
    bx, by, bw, bh = x + w * 0.24, y + h * 0.44, w * 0.52, h * 0.44
    d.rectangle([bx, by, bx + bw, by + bh], fill=NAVY)
    d.rectangle([bx + 6, by + bh * 0.3, bx + bw - 6, by + bh * 0.42], fill=(255, 255, 255))
    # paper going in
    d.rectangle([x + w * 0.36, y + h * 0.1, x + w * 0.6, y + h * 0.46], fill=(255, 255, 255), outline=INK, width=2)
    d.line([x + w * 0.4, y + h * 0.34, x + w * 0.46, y + h * 0.4], fill=GREEN, width=3)
    d.line([x + w * 0.46, y + h * 0.4, x + w * 0.57, y + h * 0.2], fill=GREEN, width=3)
    if label:
        d.text((x + w * 0.06, y + h * 0.06), label, font=F(SANSB, max(11, int(h * 0.2))), fill=RED)

def sc_car(d, x, y, w, h, label="", sub=""):
    d.rectangle([x, y, x + w, y + h], fill=(30, 30, 40))
    d.rectangle([x, y + h * 0.72, x + w, y + h], fill=(52, 52, 60))
    for i in range(6):
        d.rectangle([x + i * (w / 6) + 4, y + h * 0.84, x + i * (w / 6) + w / 9, y + h * 0.88], fill=(240, 240, 240))
    # F1-ish car
    cy = y + h * 0.6
    d.polygon([(x + w * 0.1, cy), (x + w * 0.34, cy - h * 0.1), (x + w * 0.52, cy - h * 0.1), (x + w * 0.62, cy - h * 0.24), (x + w * 0.72, cy - h * 0.1), (x + w * 0.9, cy), (x + w * 0.9, cy + h * 0.06), (x + w * 0.1, cy + h * 0.06)], fill=(108, 52, 160))
    d.rectangle([x + w * 0.06, cy - h * 0.16, x + w * 0.16, cy + h * 0.02], fill=(70, 30, 110))
    for wx in (0.24, 0.78):
        d.ellipse([x + w * wx - 9, cy - 2, x + w * wx + 9, cy + h * 0.16], fill=(12, 12, 12))
    # chequered flag strip
    for i in range(8):
        for j in range(2):
            c = (240, 240, 240) if (i + j) % 2 == 0 else (20, 20, 20)
            d.rectangle([x + w - 8 - (8 - i) * 8, y + 4 + j * 8, x + w - 8 - (7 - i) * 8, y + 12 + j * 8], fill=c)

def sc_score(d, x, y, w, h, label="", sub=""):
    # a scoreboard scene: big label centre, floodlight pylons
    d.rectangle([x, y, x + w, y + h], fill=(26, 60, 40))
    for px in (0.08, 0.86):
        d.line([x + w * px + 6, y + h * 0.14, x + w * px + 6, y + h * 0.5], fill=(200, 205, 210), width=3)
        for lx in range(3):
            d.ellipse([x + w * px + lx * 7, y + h * 0.08, x + w * px + lx * 7 + 5, y + h * 0.08 + 5], fill=(255, 246, 190))
    # board rides high in the scene so the figure pill (bottom-left) never
    # touches the wordmark (v5 fix for the v4 AFCON overlap)
    d.rectangle([x + w * 0.2, y + h * 0.08, x + w * 0.8, y + h * 0.52], fill=(12, 24, 18), outline=GOLD, width=2)
    tf = F(SANSB, max(12, int(h * 0.26)))
    tw = d.textlength(label, font=tf)
    d.text((x + (w - tw) / 2, y + h * 0.15), label, font=tf, fill=(255, 226, 120))
    if sub:
        sf = F(SANSB, max(8, int(h * 0.11)))
        sw = d.textlength(sub, font=sf)
        d.text((x + (w - sw) / 2, y + h * 0.6), sub, font=sf, fill=(220, 235, 220))

def sc_ship(d, x, y, w, h, label="", sub=""):
    d.rectangle([x, y, x + w, y + h * 0.62], fill=SKY)
    d.rectangle([x, y + h * 0.62, x + w, y + h], fill=SEA)
    for i in range(4):
        wy = y + h * (0.7 + i * 0.08)
        d.line([x + (i % 2) * 14, wy, x + w - ((i + 1) % 2) * 14, wy], fill=(120, 170, 205), width=2)
    sy = y + h * 0.52
    d.polygon([(x + w * 0.14, sy), (x + w * 0.86, sy), (x + w * 0.78, sy + h * 0.14), (x + w * 0.22, sy + h * 0.14)], fill=(50, 54, 60))
    cols = [(178, 84, 52), (52, 110, 165), (64, 140, 84), (178, 84, 52)]
    for i, c in enumerate(cols):
        d.rectangle([x + w * (0.24 + i * 0.13), sy - h * 0.13, x + w * (0.35 + i * 0.13), sy], fill=c)
    d.rectangle([x + w * 0.68, sy - h * 0.26, x + w * 0.76, sy - h * 0.13], fill=(230, 230, 230))

def sc_power(d, x, y, w, h, label="", sub=""):
    d.rectangle([x, y, x + w, y + h], fill=(226, 233, 238))
    px = x + w * 0.3
    d.line([px, y + h * 0.92, px + w * 0.08, y + h * 0.2], fill=INK, width=4)
    d.line([px + w * 0.16, y + h * 0.92, px + w * 0.08, y + h * 0.2], fill=INK, width=4)
    d.line([px - w * 0.06, y + h * 0.3, px + w * 0.22, y + h * 0.3], fill=INK, width=4)
    d.line([px, y + h * 0.44, px + w * 0.16, y + h * 0.44], fill=INK, width=3)
    d.line([px - w * 0.06, y + h * 0.3, px - w * 0.02, y + h * 0.44], fill=INK, width=2)
    d.line([px + w * 0.22, y + h * 0.3, px + w * 0.18, y + h * 0.44], fill=INK, width=2)
    # bolt
    bx, by = x + w * 0.62, y + h * 0.18
    d.polygon([(bx + 14, by), (bx, by + h * 0.34), (bx + 10, by + h * 0.34), (bx + 2, by + h * 0.62), (bx + 22, by + h * 0.26), (bx + 11, by + h * 0.26)], fill=GOLD, outline=REDD)

def sc_health(d, x, y, w, h, label="", sub=""):
    d.rectangle([x, y, x + w, y + h], fill=(233, 240, 235))
    # bottle — drawn large so it still reads in the short (46px) scenes
    bx, by, bw, bh = x + w * 0.56, y + h * 0.18, w * 0.3, h * 0.76
    d.rectangle([bx + bw * 0.28, by - h * 0.12, bx + bw * 0.72, by], fill=(120, 60, 40))
    d.rectangle([bx, by, bx + bw, by + bh], fill=(150, 84, 46), outline=INK, width=2)
    d.rectangle([bx + 5, by + bh * 0.26, bx + bw - 5, by + bh * 0.8], fill=(255, 250, 238))
    d.line([bx + bw / 2, by + bh * 0.36, bx + bw / 2, by + bh * 0.7], fill=RED, width=5)
    d.line([bx + bw * 0.26, by + bh * 0.53, bx + bw * 0.74, by + bh * 0.53], fill=RED, width=5)
    if label:
        tf = F(SANSB, max(13, int(h * 0.26)))
        d.text((x + w * 0.62, y + h * 0.36), label, font=tf, fill=RED)

def sc_gavel(d, x, y, w, h, label="", sub=""):
    d.rectangle([x, y, x + w, y + h], fill=(238, 230, 214))
    # columns
    for i in range(3):
        cx = x + w * (0.14 + i * 0.24)
        d.rectangle([cx, y + h * 0.24, cx + w * 0.1, y + h * 0.8], fill=(206, 196, 172))
    d.polygon([(x + w * 0.06, y + h * 0.24), (x + w * 0.94, y + h * 0.24), (x + w * 0.5, y + h * 0.06)], fill=NAVY)
    d.rectangle([x + w * 0.06, y + h * 0.8, x + w * 0.94, y + h * 0.88], fill=NAVY)
    if label:
        tf = F(SANSB, max(10, int(h * 0.15)))
        tw = d.textlength(label, font=tf)
        d.text((x + (w - tw) / 2, y + h * 0.1), label, font=tf, fill=(255, 255, 255))

def sc_scales(d, x, y, w, h, label="", sub=""):
    # the scales of justice on a deep red panel (a court verdict)
    d.rectangle([x, y, x + w, y + h], fill=(74, 24, 20))
    gold = (222, 184, 92)
    cx, cy = x + w / 2, y + h / 2
    d.line([cx, cy - h * 0.30, cx, cy + h * 0.30], fill=gold, width=4)
    d.line([cx - w * 0.28, cy - h * 0.20, cx + w * 0.28, cy - h * 0.20], fill=gold, width=4)
    d.ellipse([cx - 5, cy - h * 0.38, cx + 5, cy - h * 0.28], fill=gold)
    for sgn in (-1, 1):
        px = cx + sgn * w * 0.28
        d.line([px, cy - h * 0.20, px - 14, cy + h * 0.10], fill=gold, width=2)
        d.line([px, cy - h * 0.20, px + 14, cy + h * 0.10], fill=gold, width=2)
        d.arc([px - 15, cy + h * 0.02, px + 15, cy + h * 0.20], 0, 180, fill=gold, width=3)
    d.line([cx - w * 0.11, cy + h * 0.34, cx + w * 0.11, cy + h * 0.34], fill=gold, width=4)

def sc_virus(d, x, y, w, h, label="", sub=""):
    # a virus particle: spiked circle on a pale panel (a disease outbreak)
    d.rectangle([x, y, x + w, y + h], fill=(233, 240, 235))
    cx, cy, r = x + w / 2, y + h / 2, h * 0.26
    import math as _m
    for a in range(0, 360, 30):
        ex = cx + (r + h * 0.13) * _m.cos(_m.radians(a))
        ey = cy + (r + h * 0.13) * _m.sin(_m.radians(a))
        d.line([cx, cy, ex, ey], fill=(150, 60, 50), width=3)
        d.ellipse([ex - 4, ey - 4, ex + 4, ey + 4], fill=(150, 60, 50))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(178, 84, 52))
    for dxr, dyr in [(-0.35, -0.2), (0.3, -0.35), (0.05, 0.3), (-0.15, 0.05)]:
        d.ellipse([cx + r * dxr - 3, cy + r * dyr - 3, cx + r * dxr + 3, cy + r * dyr + 3], fill=(240, 200, 150))

def sc_store(d, x, y, w, h, label="", sub=""):
    d.rectangle([x, y, x + w, y + h], fill=(238, 233, 220))
    bx, by, bw, bh = x + w * 0.2, y + h * 0.26, w * 0.6, h * 0.66
    d.rectangle([bx, by, bx + bw, by + bh], fill=(214, 205, 188))
    # awning: a band of vertical stripes with a straight hem
    n = 6
    for i in range(n):
        c = RED if i % 2 == 0 else (255, 250, 240)
        ax = bx + i * (bw / n)
        d.rectangle([ax, by, ax + bw / n, by + h * 0.15], fill=c)
    d.line([bx, by + h * 0.15, bx + bw, by + h * 0.15], fill=INK, width=1)
    # window + door
    d.rectangle([bx + 8, by + h * 0.24, bx + bw * 0.55, by + bh - 8], fill=(70, 92, 110))
    d.rectangle([bx + bw * 0.66, by + h * 0.24, bx + bw - 8, by + bh], fill=(110, 84, 60))
    if label:
        tf = F(SANSB, max(13, int(h * 0.26)))
        d.text((x + w * 0.84, y + h * 0.34), label, font=tf, fill=RED)

def sc_rocket(d, x, y, w, h, label="", sub=""):
    # a heavy rocket climbing past two small satellites (a launch)
    d.rectangle([x, y, x + w, y + h], fill=(18, 28, 54))
    for sx, sy in [(0.1, 0.2), (0.3, 0.12), (0.55, 0.25), (0.8, 0.15), (0.9, 0.42), (0.64, 0.08)]:
        d.ellipse([x + w * sx, y + h * sy, x + w * sx + 3, y + h * sy + 3], fill=(255, 240, 190))
    cx, cy = x + w * 0.4, y + h * 0.52
    d.polygon([(cx - 10, cy + 14), (cx - 6, cy - 12), (cx, cy - 22), (cx + 6, cy - 12), (cx + 10, cy + 14)], fill=(235, 238, 242), outline=INK)
    d.ellipse([cx - 3.5, cy - 8, cx + 3.5, cy - 1], fill=SEA)
    d.polygon([(cx - 10, cy + 14), (cx - 18, cy + 20), (cx - 9, cy + 8)], fill=RED)
    d.polygon([(cx + 10, cy + 14), (cx + 18, cy + 20), (cx + 9, cy + 8)], fill=RED)
    d.polygon([(cx - 4, cy + 14), (cx, cy + 24), (cx + 4, cy + 14)], fill=GOLD)
    d.polygon([(cx - 2, cy + 14), (cx, cy + 20), (cx + 2, cy + 14)], fill=(232, 110, 40))
    for sx, sy in [(0.68, 0.3), (0.84, 0.56)]:
        bx, by = x + w * sx, y + h * sy
        d.rectangle([bx - 4, by - 3, bx + 4, by + 3], fill=(200, 205, 210), outline=INK)
        d.rectangle([bx - 13, by - 2, bx - 5, by + 2], fill=SEA)
        d.rectangle([bx + 5, by - 2, bx + 13, by + 2], fill=SEA)

def sc_sun(d, x, y, w, h, label="", sub=""):
    # a blazing sun and a thermometer (a heat record)
    d.rectangle([x, y, x + w, y + h], fill=(250, 232, 190))
    cx, cy, r = x + w * 0.3, y + h * 0.48, h * 0.26
    import math as _m
    for a in range(0, 360, 45):
        ex = cx + (r + 6) * _m.cos(_m.radians(a))
        ey = cy + (r + 6) * _m.sin(_m.radians(a))
        ex2 = cx + (r + 12) * _m.cos(_m.radians(a))
        ey2 = cy + (r + 12) * _m.sin(_m.radians(a))
        d.line([ex, ey, ex2, ey2], fill=(232, 140, 40), width=3)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GOLD, outline=(232, 140, 40), width=2)
    tx = x + w * 0.68
    d.rounded_rectangle([tx - 4, y + h * 0.12, tx + 4, y + h * 0.62], radius=4, outline=INK, width=2)
    d.rectangle([tx - 2, y + h * 0.28, tx + 2, y + h * 0.62], fill=RED)
    d.ellipse([tx - 8, y + h * 0.56, tx + 8, y + h * 0.56 + 16], fill=RED, outline=INK, width=2)
    for i in range(3):
        ly = y + h * (0.2 + i * 0.13)
        d.line([tx + 6, ly, tx + 11, ly], fill=INK, width=2)

def sc_generic(d, x, y, w, h, label="", sub=""):
    d.rectangle([x, y, x + w, y + h], fill=SKY)
    cx, cy, r = x + w / 2, y + h / 2, h * 0.36
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(90, 150, 190), outline=NAVY, width=2)
    d.arc([cx - r, cy - r, cx + r, cy + r], start=20, end=160, fill=GREEN, width=6)
    d.arc([cx - r, cy - r, cx + r, cy + r], start=200, end=330, fill=GREEN, width=6)

SCENES = {
    "summit": sc_summit, "drones": sc_drones, "radar": sc_radar, "fire": sc_fire,
    "ballot": sc_ballot, "car": sc_car, "score": sc_score, "ship": sc_ship,
    "power": sc_power, "health": sc_health, "gavel": sc_gavel, "generic": sc_generic,
    "scales": sc_scales, "virus": sc_virus, "store": sc_store,
    "rocket": sc_rocket, "sun": sc_sun,
}

# ---------------------------------------------------------------- world map
# A schematic dotted world: 72 x 30 cells, '#' is land. Pins are (col, row).
MAP_ROWS = [
    "                                                                        ",
    "      ##########                                                        ",
    "   ################        ##       ##############################      ",
    "  ##################      ####    #################################     ",
    "   #################       ##   ###################################     ",
    "    ###############             ################ ##################     ",
    "     #############               ##############   ################      ",
    "      ###########                 ############     #############        ",
    "       #########                   ##########       ##########          ",
    "       ########                     ########   ##    ########           ",
    "        ######                       ######   ####    ######            ",
    "        #####                         ####   ######    ####             ",
    "         ####                          ##   ########    ##              ",
    "         #####                             ##########                   ",
    "          #####                            #########      ####          ",
    "          ######                           ########      #########      ",
    "           #####                            #####         ##########    ",
    "           ######                            ###           ########     ",
    "            #####                             #             ######      ",
    "            ####                                               ###      ",
    "             ###                                                                ",
    "             ##                                                                 ",
]

def draw_map(d, x, y, w, h, pins):
    cols = max(len(r) for r in MAP_ROWS)
    rows = len(MAP_ROWS)
    cw = w / cols
    ch = h / rows
    r = max(1.6, min(cw, ch) * 0.32)
    for ri, row in enumerate(MAP_ROWS):
        for ci, cell in enumerate(row):
            if cell == "#":
                cx, cy = x + ci * cw + cw / 2, y + ri * ch + ch / 2
                d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(150, 175, 200))
    for num, (ci, ri) in enumerate(pins, start=1):
        cx, cy = x + ci * cw + cw / 2, y + ri * ch + ch / 2
        d.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=RED, outline=(255, 255, 255), width=2)
        t = str(num)
        tf = F(SANSB, 10)
        tw = d.textlength(t, font=tf)
        d.text((cx - tw / 2, cy - 6), t, font=tf, fill=(255, 255, 255))

# ---------------------------------------------------------------- cards

TAG_FILL = {"CONFIRMED": GREEN, "OFFICIAL": (96, 64, 148), "REPORTED": NAVY, "CLAIM": (178, 120, 20), "ONGOING": RED}

def tag_chip(d, x, y, tag):
    tf = F(SANSB, 9)
    tw = d.textlength(tag, font=tf) + 12
    d.rounded_rectangle([x, y, x + tw, y + 15], radius=3, fill=TAG_FILL.get(tag, NAVY))
    d.text((x + 6, y + 2), tag, font=tf, fill=(255, 255, 255))
    return tw

def card(d, x, y, w, h, story, big=False):
    d.rounded_rectangle([x, y, x + w, y + h], radius=6, fill=CARD, outline=(190, 178, 150), width=1)
    # number badge
    d.ellipse([x + 7, y + 6, x + 29, y + 28], fill=NAVY)
    t = str(story["n"])
    tf = F(SANSB, 13)
    d.text((x + 18 - d.textlength(t, font=tf) / 2, y + 10), t, font=tf, fill=(255, 255, 255))
    # tag first, so the location gets the width that is really left
    tag_w = d.textlength(story["tag"], font=F(SANSB, 9)) + 12
    tag_chip(d, x + w - 8 - tag_w, y + 6, story["tag"])
    loc_t = story["loc"].upper()
    d.text((x + 36, y + 10), fitw(d, loc_t, F(SANSB, 9), w - 44 - tag_w - 8), font=F(SANSB, 9), fill=INK)
    # scene
    sh = 70 if big else (62 if h > 200 else 46)
    sy = y + 31
    SCENES[story["scene"]](d, x + 8, sy, w - 16, sh, story.get("art_label", ""), story.get("art_sub", ""))
    d.rectangle([x + 8, sy, x + w - 8, sy + sh], outline=(190, 178, 150), width=1)
    # the figure pill: the story's key number as a bold banner inside the art
    pill = story.get("pill")
    if pill:
        pf = F(SANSB, 12 if big else 11)
        pw = d.textlength(pill, font=pf) + 14
        ph = 20 if big else 18
        px, py = x + 13, sy + sh - ph - 4
        d.rounded_rectangle([px, py, px + pw, py + ph], radius=3, fill=INK, outline=(255, 255, 255), width=1)
        d.text((px + 7, py + (4 if big else 3)), pill, font=pf, fill=(255, 255, 255))
    ty = sy + sh + 6
    d.text((x + 10, ty), story["cat"].upper(), font=F(SANSB, 9), fill=RED)
    ty += 12
    hf = F(SERIFB, 20 if big else 15)
    hl = 22 if big else 16
    # the headline may take a third line only if the summary keeps two of its own
    sf_pre = F(SANS, 13 if big else 11)
    sl_pre = 15 if big else 13
    room = (y + h - 16) - ty
    head_lines = max(1, min(3, int((room - 2 * sl_pre) // hl)))
    ty = block(d, x + 10, ty, story["head"], hf, INK, w - 20, hl, head_lines)
    ty += 2
    sf = F(SANS, 13 if big else 11)
    sl = 15 if big else 13
    # the summary gets whatever room is left above the source line — no more
    avail = (y + h - 16) - ty
    max_lines = max(1, int(avail // sl))
    block(d, x + 10, ty, story["sum"], sf, (52, 58, 66), w - 20, sl, max_lines)
    d.text((x + 10, y + h - 14), fitw(d, story["src"], F(SANS, 9), w - 20), font=F(SANS, 9), fill=GREY)

def numbers_box(d, x, y, w, h, nums):
    d.rounded_rectangle([x, y, x + w, y + h], radius=6, fill=NAVY)
    d.text((x + 12, y + 8), "THE DAY IN NUMBERS", font=F(SANSB, 12), fill=(255, 255, 255))
    step = (h - 36) / max(1, len(nums))
    cy = y + 33
    for big, small in nums:
        bf = F(SERIFB, 23)
        d.text((x + 12, cy), big, font=bf, fill=GOLD)
        bw = d.textlength(big, font=bf)
        block(d, x + 18 + bw, cy + 3, small, F(SANS, 10), (225, 232, 240), w - 30 - bw, 12, 2)
        cy += step

# ---------------------------------------------------------------- page

def render(day, out_path):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 26
    # masthead
    d.rectangle([0, 0, W, 30], fill=NAVY)
    d.text((M, 8), "ONE DAY, THE WHOLE WORLD", font=F(SANSB, 13), fill=(255, 255, 255))
    rt = f"{day['story_count']} STORIES · {day['region_count']} REGIONS · {day['field_count']} FIELDS · ALL FROM THIS ONE DAY"
    d.text((W - M - d.textlength(rt, font=F(SANSB, 12)), 8), rt, font=F(SANSB, 12), fill=GOLD)
    d.text((M, 36), day["date_line"], font=F(SERIFB, 55), fill=INK)
    d.text((M, 100), fitw(d, day["kicker"], F(SERIFI, 18), W - 2 * M), font=F(SERIFI, 18), fill=RED)
    # region chips
    cx = M
    for name, n in day["regions"]:
        label = f"{name} {n}"
        tf = F(SANSB, 11)
        twd = d.textlength(label, font=tf) + 16
        d.rounded_rectangle([cx, 126, cx + twd, 146], radius=4, fill=NAVY if name != "WORLD" else RED)
        d.text((cx + 8, 130), label, font=tf, fill=(255, 255, 255))
        cx += twd + 7
    # timeline (segments are added only while they fit the bar)
    d.rectangle([M, 154, W - M, 178], fill=INK)
    tx = M + 10
    d.text((tx, 160), "UTC", font=F(SANSB, 12), fill=GOLD)
    tx += 40
    tf = F(SANSB, 11)
    for time_, text in day["timeline"]:
        seg = f"{time_} {text}"
        segw = d.textlength(seg, font=tf)
        if tx + segw > W - M - 8:
            break
        d.text((tx, 160), seg, font=tf, fill=(255, 255, 255))
        tx += segw + 14
        d.text((tx - 10, 160), "·", font=tf, fill=GOLD)
    # hero row
    y0 = 186
    hero_w, lead_w, num_w, gap = 430, 258, 252, 10
    card(d, M, y0, hero_w, 220, day["hero"], big=True)
    card(d, M + hero_w + gap, y0, lead_w, 220, day["leads"][0])
    numbers_box(d, M + hero_w + lead_w + 2 * gap, y0, num_w, 220, day["numbers"])
    # rows B and C run five narrow cards each (v5: 12 illustrated cards)
    y1 = y0 + 228
    cw5 = (W - 2 * M - 4 * gap) // 5
    for i, s in enumerate(day["row_b"]):
        card(d, M + i * (cw5 + gap), y1, cw5, 174, s)
    y2 = y1 + 182
    for i, s in enumerate(day["row_c"]):
        card(d, M + i * (cw5 + gap), y2, cw5, 174, s)
    # also list + map
    y3 = y2 + 182
    map_w = 300
    also_w = W - 2 * M - map_w - 12
    d.text((M, y3), f"ALSO ON {day['date_short'].upper()} · LETTER = HOW SURE", font=F(SANSB, 12), fill=INK)
    colw = also_w // 2
    items = day["also"]
    half = (len(items) + 1) // 2
    tier_fill = {"C": GREEN, "O": (96, 64, 148), "R": NAVY, "CL": (178, 120, 20)}
    for ci, chunk in enumerate([items[:half], items[half:]]):
        ax = M + ci * colw
        ay = y3 + 17
        for n, code, text, src, tier in chunk:
            d.text((ax, ay), f"{n}", font=F(SANSB, 11), fill=RED)
            d.rounded_rectangle([ax + 21, ay, ax + 48, ay + 13], radius=2, fill=NAVY)
            cf = F(SANSB, 8)
            cw_ = d.textlength(code, font=cf)
            d.text((ax + 34.5 - cw_ / 2, ay + 2), code, font=cf, fill=(255, 255, 255))
            # the certainty chip: one letter (or CL) in the tier colour
            d.rounded_rectangle([ax + 52, ay, ax + 68, ay + 13], radius=2, fill=tier_fill[tier])
            tf2 = F(SANSB, 7 if len(tier) > 1 else 8)
            tw2 = d.textlength(tier, font=tf2)
            d.text((ax + 60 - tw2 / 2, ay + 2), tier, font=tf2, fill=(255, 255, 255))
            sf_ = F(SANS, 9)
            srcw = d.textlength(src, font=sf_)
            d.text((ax + 72, ay + 1), fitw(d, text, F(SANS, 10), colw - 80 - srcw), font=F(SANS, 10), fill=INK)
            d.text((ax + colw - 8 - srcw, ay + 1), src, font=sf_, fill=GREY)
            ay += 12.6
    # map box
    mx = W - M - map_w
    d.rounded_rectangle([mx, y3, W - M, y3 + 172], radius=6, fill=(240, 244, 248), outline=(190, 178, 150))
    d.text((mx + 10, y3 + 6), "WHERE IT HAPPENED", font=F(SANSB, 11), fill=INK)
    d.text((mx + 150, y3 + 7), "pins = story numbers", font=F(SANS, 9), fill=GREY)
    draw_map(d, mx + 8, y3 + 24, map_w - 16, 118, day["pins"])
    d.text((mx + 10, y3 + 150), day["map_note"], font=F(SANS, 9), fill=GREY)
    # date check
    y4 = y3 + 184
    d.rounded_rectangle([M, y4, W - M, y4 + 34], radius=5, outline=RED, width=2)
    d.text((M + 10, y4 + 6), "DATE CHECK", font=F(SANSB, 11), fill=RED)
    block(d, M + 92, y4 + 5, day["date_check"], F(SANS, 11), INK, W - 2 * M - 104, 12.5, 2)
    # legend: the chips, then the tier definitions in words
    ly = y4 + 44
    d.text((M, ly), "HOW SURE:", font=F(SANSB, 10), fill=INK)
    lx = M + 66
    for tag in ["CONFIRMED", "OFFICIAL", "REPORTED", "CLAIM", "ONGOING"]:
        lx += tag_chip(d, lx, ly - 2, tag) + 6
    d.text((lx + 2, ly), day["legend_tail"], font=F(SANS, 9), fill=GREY)
    img.save(out_path)
    return out_path
