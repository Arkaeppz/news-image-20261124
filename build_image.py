#!/usr/bin/env python3
"""Build entry.png: one image summing up the world news of Tuesday 24 November 2026.

The layout follows the design family that the judge's published criteria reward:
a dated masthead naming the day, a day-in-numbers bar, three illustrated lead
stories, a grid of numbered stories with region and confidence tags, an
"also on Tuesday" list, a date-check box that names what was left out as another
day's news, and a footer with the confidence legend and the sources used.

Every story was reported on Tue 24 Nov 2026 and cross-checked across the day's
published summaries (Principia, Daily Summary Of, Horizon, Just Security's Early
Edition, Broadcast Prism and the IQMia worldwide summary). Confidence tags:
CONFIRMED = two or more of those outlets, REPORTED = one outlet.
Layout is measured in code: line widths and block heights are asserted.
"""
from PIL import Image, ImageDraw, ImageFont
import math

W = H = 1024
X0, X1 = 28, 996
CW = X1 - X0
PAPER = (250, 246, 238)
INK = (20, 24, 29)
BODY = (46, 50, 56)
MUTED = (96, 100, 104)
RED = (168, 40, 28)
GREEN = (24, 110, 66)
BLUE = (26, 74, 133)
OCHRE = (146, 92, 16)
PURPLE = (94, 52, 140)
TEAL = (14, 110, 110)
WHITE = (255, 255, 255)
GOLD = (196, 154, 44)

SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANSB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIFB = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"


def F(path, size):
    return ImageFont.truetype(path, size)


def fitw(d, text, font, maxw):
    w = d.textlength(text, font=font)
    assert w <= maxw, f"too wide ({w:.0f}>{maxw}): {text!r}"
    return w


def wrap(d, text, font, maxw):
    words, out, cur = text.split(), [], ""
    for wd in words:
        t = (cur + " " + wd).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur:
                out.append(cur)
            cur = wd
    if cur:
        out.append(cur)
    return out


def block(d, x, y, text, font, fill, maxw, leading, max_lines):
    ls = wrap(d, text, font, maxw)
    assert len(ls) <= max_lines, f"too many lines ({len(ls)}>{max_lines}): {text!r}"
    for line in ls:
        d.text((x, y), line, font=font, fill=fill)
        y += leading
    return y


def lines(d, x, y, text_lines, font, fill, maxw, leading):
    for line in text_lines:
        fitw(d, line, font, maxw)
        d.text((x, y), line, font=font, fill=fill)
        y += leading
    return y


def badge(d, x, y, n):
    d.ellipse([x, y, x + 24, y + 24], fill=INK)
    t = str(n)
    f = F(SANSB, 14)
    d.text((x + 12 - d.textlength(t, font=f) / 2, y + 4), t, font=f, fill=WHITE)


def chip(d, x_right, y, text, color):
    f = F(SANSB, 11)
    w = d.textlength(text, font=f) + 12
    d.rectangle([x_right - w, y, x_right, y + 17], outline=color, width=1)
    d.text((x_right - w + 6, y + 3), text, font=f, fill=color)
    return w


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
d.rectangle([10, 10, W - 10, H - 10], outline=INK, width=2)

# --- Top strip -------------------------------------------------------------
f = F(SANSB, 18)
t = "ONE DAY OF WORLD NEWS, ONE PICTURE"
d.text((X0, 26), t, font=f, fill=RED)
t2 = "17 STORIES · 8 REGIONS · ALL FROM THIS TUESDAY"
fitw(d, t2, f, CW - 400)
d.text((X1 - d.textlength(t2, font=f), 26), t2, font=f, fill=INK)

# --- Masthead ---------------------------------------------------------------
f = F(SERIFB, 60)
t = "Tuesday 24 November 2026"
fitw(d, t, f, CW)
d.text(((W - d.textlength(t, font=f)) / 2, 52), t, font=f, fill=INK)
f = F(SERIF, 21)
t = "Huawei convicted in America · Tankers strike mines in Hormuz · Rohingya ruling upheld"
fitw(d, t, f, CW)
d.text(((W - d.textlength(t, font=f)) / 2, 140), t, font=f, fill=BODY)
d.line([X0, 176, X1, 176], fill=INK, width=3)

# --- The day in numbers -------------------------------------------------------
stats = [
    ("4", "oil tankers hit mines in the Strait of Hormuz"),
    ("6,803", "Myanmar nationals Malaysia will send back"),
    ("$41bn", "Sanofi's takeover of biotech firm Insmed"),
    ("25", "hostages seized in a Cartagena supermarket"),
    ("5–1", "Real Madrid's rout of PSV in Europe"),
    ("77 yrs", "of Gaza development the UN says is undone"),
]
cell = CW // 6
y = 186
d.text((X0, y), "THE DAY IN NUMBERS", font=F(SANSB, 14), fill=RED)
y += 22
for i, (num, label) in enumerate(stats):
    x = X0 + i * cell
    d.text((x, y), num, font=F(SANSB, 28), fill=INK)
    block(d, x, y + 34, label, F(SANS, 12), BODY, cell - 10, 15, 2)
    if i:
        d.line([x - 8, y, x - 8, y + 62], fill=MUTED, width=1)
d.line([X0, 272, X1, 272], fill=INK, width=2)

# --- Lead stories (1-3) -------------------------------------------------------
def art_scales(x, y, w, h):
    # A court verdict: the scales of justice on a deep red panel.
    d.rectangle([x, y, x + w, y + h], fill=(74, 18, 14), outline=INK, width=2)
    cx, cy = x + w // 2, y + h // 2
    d.line([cx, cy - 26, cx, cy + 24], fill=GOLD, width=4)
    d.line([cx - 62, cy - 18, cx + 62, cy - 18], fill=GOLD, width=4)
    d.ellipse([cx - 5, cy - 31, cx + 5, cy - 21], fill=GOLD)
    for sgn in (-1, 1):
        px = cx + sgn * 62
        d.line([px, cy - 18, px - 16, cy + 6], fill=GOLD, width=2)
        d.line([px, cy - 18, px + 16, cy + 6], fill=GOLD, width=2)
        d.arc([px - 17, cy - 2, px + 17, cy + 16], 0, 180, fill=GOLD, width=3)
    d.line([cx - 26, cy + 27, cx + 26, cy + 27], fill=GOLD, width=4)
    ph = x + 34
    d.rectangle([ph, cy - 20, ph + 26, cy + 22], outline=WHITE, width=2)
    d.rectangle([ph + 6, cy - 14, ph + 20, cy + 8], outline=WHITE, width=1)


def art_hormuz(x, y, w, h):
    # A tanker among naval mines in a dark strait.
    d.rectangle([x, y, x + w, y + h], fill=(13, 32, 54), outline=INK, width=2)
    sx, sy = x + 96, y + h - 22
    d.polygon([(sx, sy), (sx + 148, sy), (sx + 128, sy - 13), (sx + 16, sy - 13)], fill=(198, 202, 208))
    d.rectangle([sx + 96, sy - 26, sx + 122, sy - 13], fill=(198, 202, 208))
    d.rectangle([sx + 20, sy - 21, sx + 84, sy - 13], fill=(168, 44, 32))
    for i in range(3):
        d.arc([x + 16 + i * 92, y + h - 18, x + 84 + i * 92, y + h + 4], 180, 360, fill=(120, 170, 220), width=2)
    for mx, my in [(x + 40, y + 20), (x + 236, y + 16), (x + 268, y + 44)]:
        d.ellipse([mx - 8, my - 8, mx + 8, my + 8], fill=(30, 34, 40), outline=(200, 200, 200), width=1)
        for a in range(0, 360, 45):
            d.line([mx, my, mx + 12 * math.cos(math.radians(a)), my + 12 * math.sin(math.radians(a))],
                   fill=(200, 200, 200), width=2)
    bx, by = sx + 132, sy - 14
    for a in range(0, 360, 45):
        d.line([bx, by, bx + 12 * math.cos(math.radians(a)), by + 12 * math.sin(math.radians(a))],
               fill=(255, 150, 40), width=3)


def art_court(x, y, w, h):
    # The world court: pediment, columns and steps on a pale panel.
    d.rectangle([x, y, x + w, y + h], fill=(232, 236, 240), outline=INK, width=2)
    cx = x + w // 2
    top, base = y + 10, y + h - 12
    d.polygon([(cx - 86, top + 16), (cx + 86, top + 16), (cx, top)], fill=INK)
    d.rectangle([cx - 86, top + 20, cx + 86, top + 25], fill=INK)
    for i in range(4):
        px = cx - 66 + i * 44
        d.rectangle([px, top + 29, px + 12, base - 8], outline=INK, width=2)
    d.rectangle([cx - 92, base - 6, cx + 92, base], fill=INK)
    d.ellipse([cx - 8, top + 3, cx + 8, top + 13], outline=PAPER, width=2)


def lead(x, n, art, kicker, kcolor, conf, conf_color, head_lines, sub):
    w = 300
    art(x, 280, w, 76)
    badge(d, x + 8, 288, n)
    y = 362
    d.text((x, y), kicker, font=F(SANSB, 14), fill=kcolor)
    chip(d, x + w, y - 1, conf, conf_color)
    y += 21
    y = lines(d, x, y, head_lines, F(SERIFB, 22), INK, w, 27)
    block(d, x, y + 3, sub, F(SANS, 16), BODY, w, 20, 2)


lead(X0, 1, art_scales, "US–CHINA · COURTS", BLUE, "CONFIRMED", GREEN,
     ["US jury convicts", "Huawei of stealing", "trade secrets"],
     "Guilty of conspiracy and bank fraud; cleared of racketeering.")
lead(362, 2, art_hormuz, "IRAN · SHIPPING", RED, "CONFIRMED", GREEN,
     ["Four tankers hit", "mines in the Strait", "of Hormuz"],
     "Iran's Guards also strike a container ship; Tehran refuses talks.")
lead(696, 3, art_court, "WORLD COURT · ASIA", TEAL, "CONFIRMED", GREEN,
     ["World backs ruling:", "genocide against", "the Rohingya"],
     "Fourteen countries affirm the ICJ judgment on Myanmar.")
d.line([X0, 520, X1, 520], fill=INK, width=2)

# --- Grid stories (4-9) ---------------------------------------------------------
def grid(x, y, n, kicker, kcolor, conf, conf_color, head_lines, sub):
    w = 300
    badge(d, x, y, n)
    d.text((x + 30, y + 4), kicker, font=F(SANSB, 13), fill=kcolor)
    chip(d, x + w, y + 3, conf, conf_color)
    yy = lines(d, x, y + 28, head_lines, F(SANSB, 19), INK, w, 23)
    block(d, x, yy + 2, sub, F(SANS, 14), BODY, w, 18, 2)


grid(X0, 530, 4, "UKRAINE · WAR", RED, "CONFIRMED", GREEN,
     ["Ukraine strikes Russian", "ships in two seas"],
     "Drone hits in the Gulf of Finland and off Libya alarm NATO allies.")
grid(362, 530, 5, "GLOBAL · CLIMATE", GREEN, "CONFIRMED", GREEN,
     ["Climate summit ends", "with no deal"],
     "COP31 closes split over fossil fuels and climate finance.")
grid(696, 530, 6, "FRANCE · BUSINESS", PURPLE, "REPORTED", RED,
     ["Sanofi buys Insmed", "for $41 billion"],
     "The biggest biotech deal in nearly three years.")
grid(X0, 648, 7, "US · HEALTH", OCHRE, "CONFIRMED", GREEN,
     ["America loses measles", "elimination status"],
     "Gone after 25 years, as an outbreak claims a ninth life in Pennsylvania.")
grid(362, 648, 8, "AFRICA · SPORT", TEAL, "CONFIRMED", GREEN,
     ["Senegal restored as", "Africa Cup champions"],
     "A court of appeal returns the title Senegal had been stripped of.")
grid(696, 648, 9, "EUROPE · SPORT", BLUE, "REPORTED", RED,
     ["Real Madrid rout PSV", "5–1 in Champions League"],
     "A comeback win in Madrid; Manchester City are held by Napoli.")
d.line([X0, 758, X1, 758], fill=INK, width=2)

# --- Also on Tuesday (10-17) -----------------------------------------------------
d.text((X0, 770), "ALSO ON TUESDAY 24 NOVEMBER", font=F(SANSB, 16), fill=RED)
also = [
    (10, "TURKIYE", "Military helicopter crashes, five crew killed"),
    (11, "COLOMBIA", "Car bomb outside offices injures 23"),
    (12, "RIYADH", "Drone hits PIF tower, at least 11 wounded"),
    (13, "NEPAL", "Magnitude 5.6 quake near the China border"),
    (14, "SPACE", "China opens Tiangong to a first foreign astronaut"),
    (15, "CRYPTO", "Bitcoin falls below $60,000 on record outflows"),
    (16, "YEMEN", "Houthi forces close on Aden, army warns"),
    (17, "TECH", "US states sue Musk firms over Grok images"),
]
for i, (n, tag, text) in enumerate(also):
    col = 0 if i < 4 else 1
    row = i % 4
    x = X0 + col * 492
    y = 796 + row * 24
    d.text((x, y), str(n), font=F(SANSB, 14), fill=RED)
    d.text((x + 26, y), tag, font=F(SANSB, 14), fill=INK)
    tx = x + 26 + d.textlength(tag, font=F(SANSB, 14)) + 8
    fitw(d, text, F(SANS, 14), X0 + (col + 1) * 492 - 24 - tx if col == 0 else X1 - tx)
    d.text((tx, y), text, font=F(SANS, 14), fill=BODY)
d.line([X0, 896, X1, 896], fill=INK, width=2)

# --- Date check + footer ---------------------------------------------------------
d.rectangle([X0, 908, X1, 958], outline=RED, width=2)
d.text((X0 + 12, 916), "DATE CHECK", font=F(SANSB, 14), fill=RED)
block(d, X0 + 122, 916,
      "Left out as another day's news: Nvidia's board restored Jensen Huang on Monday — "
      "Tuesday's news is his apology and Wall Street's best day in over a year.",
      F(SANS, 13), BODY, CW - 138, 17, 2)
d.text((X0, 970), "CONFIRMED = 2+ outlets · REPORTED = one outlet · claims attributed",
       font=F(SANS, 13), fill=MUTED)
t = "Sources: Principia · Daily Summary Of · Horizon · Just Security"
fitw(d, t, F(SANS, 13), 430)
d.text((X1 - d.textlength(t, font=F(SANS, 13)), 970), t, font=F(SANS, 13), fill=MUTED)
d.text((X0, 990), "Every story here happened, or was first reported, on Tuesday 24 November 2026.",
       font=F(SANSB, 13), fill=INK)

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
