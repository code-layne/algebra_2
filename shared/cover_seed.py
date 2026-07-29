#!/usr/bin/env python3
"""Generate a light grayscale Algebra 2 Unit 1 binder cover sheet (SVG)."""
import math

W, H = 850, 1100

GRID   = "#c9c9c9"   # faint grid lines
EDGE   = "#9a9a9a"   # solid geometry edges
DASH   = "#b5b5b5"   # hidden / dashed edges
CURVE  = "#5f5f5f"   # function curves
AXIS   = "#7d7d7d"   # axes
TXT    = "#3a3a3a"   # main text
TXT2   = "#5e5e5e"   # secondary text

SERIF  = "TeX Gyre Termes, Times New Roman, serif"
MATH   = "LM Roman 10, Latin Modern Roman, TeX Gyre Termes, serif"
SCRIPT = "TeX Gyre Chorus, cursive"

out = []
def a(s): out.append(s)


# ---------- small helpers -------------------------------------------------

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def mathtext(x, y, parts, size=17, fill=TXT2, anchor="start", style="italic",
             family=MATH, extra=""):
    """parts: list of (text, kind) with kind in {'n','sup','sub'}."""
    tspans = []
    for t, kind in parts:
        if kind == "sup":
            tspans.append(f'<tspan font-size="{size*0.68:.1f}" dy="{-size*0.36:.1f}">{esc(t)}</tspan>'
                          f'<tspan font-size="{size}" dy="{size*0.36:.1f}"></tspan>')
        elif kind == "sub":
            tspans.append(f'<tspan font-size="{size*0.68:.1f}" dy="{size*0.24:.1f}">{esc(t)}</tspan>'
                          f'<tspan font-size="{size}" dy="{-size*0.24:.1f}"></tspan>')
        else:
            tspans.append(f'<tspan>{esc(t)}</tspan>')
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
            f'font-style="{style}" fill="{fill}" text-anchor="{anchor}" {extra}>'
            + "".join(tspans) + '</text>')


def gridlines(w, h, step=22):
    d = []
    x = 0.0
    while x <= w + 0.01:
        d.append(f"M{x:.1f} 0V{h:.1f}")
        x += step
    y = 0.0
    while y <= h + 0.01:
        d.append(f"M0 {y:.1f}H{w:.1f}")
        y += step
    return f'<path d="{"".join(d)}" fill="none" stroke="{GRID}" stroke-width="0.7"/>'


def polyline(pts, stroke=CURVE, width=1.7, dash=None, fill="none"):
    d = "M" + " L".join(f"{px:.2f} {py:.2f}" for px, py in pts)
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"{da} stroke-linejoin="round"/>'


def arrow(x1, y1, x2, y2, stroke=AXIS, width=1.1, head=6):
    ang = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - head * math.cos(ang - 0.42), y2 - head * math.sin(ang - 0.42))
    p2 = (x2 - head * math.cos(ang + 0.42), y2 - head * math.sin(ang + 0.42))
    return (f'<path d="M{x1:.1f} {y1:.1f}L{x2:.1f} {y2:.1f}" stroke="{stroke}" '
            f'stroke-width="{width}" fill="none"/>'
            f'<path d="M{x2:.1f} {y2:.1f}L{p1[0]:.1f} {p1[1]:.1f}L{p2[0]:.1f} {p2[1]:.1f}Z" fill="{stroke}"/>')


def slab(x, y, w, h, dx=16, dy=-11, label_lines=None, size=17):
    """A 3-D rectangular slab (front face + top + right side) holding text."""
    g = [f'<g>']
    # top face
    g.append(f'<path d="M{x} {y}L{x+dx} {y+dy}L{x+w+dx} {y+dy}L{x+w} {y}Z" '
             f'fill="#ffffff" stroke="{EDGE}" stroke-width="1"/>')
    # right face
    g.append(f'<path d="M{x+w} {y}L{x+w+dx} {y+dy}L{x+w+dx} {y+h+dy}L{x+w} {y+h}Z" '
             f'fill="#ffffff" stroke="{EDGE}" stroke-width="1"/>')
    # front face
    g.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#ffffff" '
             f'stroke="{EDGE}" stroke-width="1.2"/>')
    if label_lines:
        n = len(label_lines)
        lead = size * 1.55
        y0 = y + h / 2 - (n - 1) * lead / 2 + size * 0.35
        for i, parts in enumerate(label_lines):
            g.append(mathtext(x + w / 2, y0 + i * lead, parts, size=size,
                              fill=TXT2, anchor="middle"))
    g.append('</g>')
    return "".join(g)


# ---------- background panels --------------------------------------------

def parabola_panel(w, h, coef=0.022, xlabels=True):
    """Grid panel with y-axis, x-axis, ticks and an upward parabola."""
    g = [gridlines(w, h)]
    cx, cy = w / 2, h * 0.78
    g.append(arrow(4, cy, w - 4, cy))                 # x axis
    g.append(arrow(cx, h - 4, cx, 4))                 # y axis
    for i in range(-3, 4):
        if i == 0:
            continue
        px = cx + i * 22
        if 0 < px < w:
            g.append(f'<path d="M{px:.1f} {cy-3.5}V{cy+3.5}" stroke="{AXIS}" stroke-width="1"/>')
            if xlabels:
                g.append(f'<text x="{px:.1f}" y="{cy+15}" font-family="{MATH}" font-size="10" '
                         f'fill="{AXIS}" text-anchor="middle">{i if i>0 else "−"+str(-i)}</text>')
    for j in range(1, 4):
        py = cy - j * 22
        if py > 4:
            g.append(f'<path d="M{cx-3.5} {py:.1f}H{cx+3.5}" stroke="{AXIS}" stroke-width="1"/>')
            g.append(f'<text x="{cx-7}" y="{py+3.5:.1f}" font-family="{MATH}" font-size="10" '
                     f'fill="{AXIS}" text-anchor="end">{j}</text>')
    pts = []
    x = -cx + 3
    while x <= w - cx - 3:
        yv = coef * x * x
        py = cy - yv
        if py > 3:
            pts.append((cx + x, py))
        x += 2
    g.append(polyline(pts, stroke=CURVE, width=2.0))
    g.append(f'<text x="{w-9}" y="{cy-6}" font-family="{MATH}" font-size="12" '
             f'font-style="italic" fill="{AXIS}" text-anchor="end">x</text>')
    g.append(f'<text x="{cx+8}" y="{14}" font-family="{MATH}" font-size="12" '
             f'font-style="italic" fill="{AXIS}">y</text>')
    return "".join(g)


def sine_panel(w, h):
    g = [gridlines(w, h)]
    cy = h / 2
    g.append(arrow(4, cy, w - 4, cy))
    cx = w * 0.22
    g.append(arrow(cx, h - 6, cx, 6))
    amp = h * 0.30
    period = (w - cx - 20) / 2.0          # two full waves across the panel
    pts = []
    x = 6
    while x <= w - 6:
        t = (x - cx) / period * 2 * math.pi
        pts.append((x, cy - amp * math.sin(t)))
        x += 2
    g.append(polyline(pts, stroke=CURVE, width=2.0))
    for k, lab in ((1, "π"), (2, "2π")):
        px = cx + k * period / 2
        if px < w - 6:
            g.append(f'<path d="M{px:.1f} {cy-3.5}V{cy+3.5}" stroke="{AXIS}" stroke-width="1"/>')
            g.append(f'<text x="{px:.1f}" y="{cy+16}" font-family="{MATH}" font-size="11" '
                     f'fill="{AXIS}" text-anchor="middle">{lab}</text>')
    px = cx - period / 2
    g.append(f'<text x="{px:.1f}" y="{cy+16}" font-family="{MATH}" font-size="11" '
             f'fill="{AXIS}" text-anchor="middle">−π</text>')
    g.append(f'<text x="{cx-6}" y="{cy-amp-4:.1f}" font-family="{MATH}" font-size="11" '
             f'font-style="italic" fill="{AXIS}" text-anchor="end">1</text>')
    g.append(f'<text x="{cx-6}" y="{cy+amp+10:.1f}" font-family="{MATH}" font-size="11" '
             f'fill="{AXIS}" text-anchor="end">−1</text>')
    g.append(f'<text x="{w-8}" y="{cy-7}" font-family="{MATH}" font-size="12" '
             f'font-style="italic" fill="{AXIS}" text-anchor="end">x</text>')
    g.append(f'<text x="{cx+7}" y="{16}" font-family="{MATH}" font-size="12" '
             f'font-style="italic" fill="{AXIS}">y</text>')
    return "".join(g)


def axes3d(size=210):
    """Isometric 3-D coordinate frame with a parabola sitting in the yz-plane."""
    o = (size * 0.42, size * 0.62)
    g = []
    # faint plane behind the frame
    p = [(o[0] - 10, o[1] - 90), (o[0] + 120, o[1] - 118),
         (o[0] + 120, o[1] + 22), (o[0] - 10, o[1] + 50)]
    g.append(f'<path d="M{p[0][0]:.0f} {p[0][1]:.0f}L{p[1][0]:.0f} {p[1][1]:.0f}'
             f'L{p[2][0]:.0f} {p[2][1]:.0f}L{p[3][0]:.0f} {p[3][1]:.0f}Z" fill="#ffffff" '
             f'stroke="{GRID}" stroke-width="0.9"/>')
    for i in range(1, 5):                      # ruling lines on that plane
        t = i / 5
        x1 = p[0][0] + (p[1][0] - p[0][0]) * t
        y1 = p[0][1] + (p[1][1] - p[0][1]) * t
        x2 = p[3][0] + (p[2][0] - p[3][0]) * t
        y2 = p[3][1] + (p[2][1] - p[3][1]) * t
        g.append(f'<path d="M{x1:.0f} {y1:.0f}L{x2:.0f} {y2:.0f}" stroke="{GRID}" stroke-width="0.6"/>')
    for i in range(1, 4):
        t = i / 4
        x1 = p[0][0] + (p[3][0] - p[0][0]) * t
        y1 = p[0][1] + (p[3][1] - p[0][1]) * t
        x2 = p[1][0] + (p[2][0] - p[1][0]) * t
        y2 = p[1][1] + (p[2][1] - p[1][1]) * t
        g.append(f'<path d="M{x1:.0f} {y1:.0f}L{x2:.0f} {y2:.0f}" stroke="{GRID}" stroke-width="0.6"/>')
    # three axes
    g.append(arrow(o[0], o[1], o[0], o[1] - 118))            # z up
    g.append(arrow(o[0], o[1], o[0] + 128, o[1] - 28))       # y right/back
    g.append(arrow(o[0], o[1], o[0] - 46, o[1] + 60))        # x forward/left
    g.append(f'<text x="{o[0]-4}" y="{o[1]-124}" font-family="{MATH}" font-size="13" '
             f'font-style="italic" fill="{AXIS}" text-anchor="end">z</text>')
    g.append(f'<text x="{o[0]+134}" y="{o[1]-26}" font-family="{MATH}" font-size="13" '
             f'font-style="italic" fill="{AXIS}">y</text>')
    g.append(f'<text x="{o[0]-54}" y="{o[1]+68}" font-family="{MATH}" font-size="13" '
             f'font-style="italic" fill="{AXIS}">x</text>')
    # parabola drawn in the tilted plane
    pts = []
    for k in range(-52, 53, 2):
        u = k                                   # along y
        v = 0.020 * k * k                       # height along z
        px = o[0] + u * 1.02 + 34
        py = o[1] - v - u * 0.22 - 34
        pts.append((px, py))
    g.append(polyline(pts, stroke=CURVE, width=2.0))
    return "".join(g)


def cone(w=100, h=150):
    apex = (w / 2, 0)
    cxb, cyb = w / 2, h - 22
    rx, ry = w / 2 - 4, 13
    g = []
    g.append(f'<path d="M{apex[0]} {apex[1]}L{cxb-rx} {cyb}" stroke="{EDGE}" stroke-width="1.3" fill="none"/>')
    g.append(f'<path d="M{apex[0]} {apex[1]}L{cxb+rx} {cyb}" stroke="{EDGE}" stroke-width="1.3" fill="none"/>')
    g.append(f'<path d="M{cxb-rx} {cyb}A{rx} {ry} 0 0 0 {cxb+rx} {cyb}" stroke="{EDGE}" '
             f'stroke-width="1.3" fill="none"/>')
    g.append(f'<path d="M{cxb-rx} {cyb}A{rx} {ry} 0 0 1 {cxb+rx} {cyb}" stroke="{DASH}" '
             f'stroke-width="1" stroke-dasharray="4 3" fill="none"/>')
    g.append(f'<path d="M{apex[0]} {apex[1]}V{cyb}" stroke="{DASH}" stroke-width="1" '
             f'stroke-dasharray="4 3" fill="none"/>')
    g.append(f'<path d="M{cxb} {cyb}L{cxb+rx} {cyb}" stroke="{DASH}" stroke-width="1" '
             f'stroke-dasharray="4 3" fill="none"/>')
    g.append(f'<circle cx="{cxb}" cy="{cyb}" r="1.7" fill="{EDGE}"/>')
    g.append(f'<text x="{cxb-8}" y="{cyb-h*0.4:.0f}" font-family="{MATH}" font-size="14" '
             f'font-style="italic" fill="{AXIS}" text-anchor="end">h</text>')
    g.append(f'<text x="{cxb+rx/2:.0f}" y="{cyb+16}" font-family="{MATH}" font-size="14" '
             f'font-style="italic" fill="{AXIS}" text-anchor="middle">r</text>')
    return "".join(g)


def cube(s=104, dx=34, dy=-26):
    g = []
    g.append(f'<rect x="0" y="{-dy}" width="{s}" height="{s}" fill="#ffffff" stroke="{EDGE}" stroke-width="1.3"/>')
    g.append(f'<path d="M0 {-dy}L{dx} {-dy+dy}L{s+dx} {-dy+dy}L{s} {-dy}Z" fill="#ffffff" stroke="{EDGE}" stroke-width="1.3"/>')
    g.append(f'<path d="M{s} {-dy}L{s+dx} {0}L{s+dx} {s}L{s} {s-dy}Z" fill="#ffffff" stroke="{EDGE}" stroke-width="1.3"/>')
    # hidden edges
    g.append(f'<path d="M{dx} {0}V{s}L{s+dx} {s}" stroke="{DASH}" stroke-width="0.9" '
             f'stroke-dasharray="4 3" fill="none"/>')
    g.append(f'<path d="M{dx} {0}L0 {-dy}" stroke="{DASH}" stroke-width="0.9" '
             f'stroke-dasharray="4 3" fill="none"/>')
    g.append(f'<text x="{-8}" y="{-dy+s/2:.0f}" font-family="{MATH}" font-size="14" '
             f'font-style="italic" fill="{AXIS}" text-anchor="end">a</text>')
    g.append(f'<text x="{s+dx/2+6:.0f}" y="{s-dy/2:.0f}" font-family="{MATH}" font-size="14" '
             f'font-style="italic" fill="{AXIS}">a</text>')
    return "".join(g)


def unit_circle(r=44):
    g = []
    g.append(arrow(-r - 22, 0, r + 22, 0))
    g.append(arrow(0, r + 22, 0, -r - 22))
    g.append(f'<circle cx="0" cy="0" r="{r}" fill="none" stroke="{CURVE}" stroke-width="1.7"/>')
    g.append(f'<text x="{r+26}" y="{-6}" font-family="{MATH}" font-size="12" '
             f'font-style="italic" fill="{AXIS}">x</text>')
    g.append(f'<text x="{7}" y="{-r-24}" font-family="{MATH}" font-size="12" '
             f'font-style="italic" fill="{AXIS}">y</text>')
    return "".join(g)


def number_line(w=248, lo=-1, hi=7, open_at=2, closed_at=3):
    g = []
    n = hi - lo
    step = w / n
    g.append(arrow(-14, 0, w + 14, 0, stroke=AXIS, width=1.2))
    for i in range(n + 1):
        x = i * step
        g.append(f'<path d="M{x:.1f} -4V4" stroke="{AXIS}" stroke-width="1"/>')
        lab = lo + i
        s = f"−{-lab}" if lab < 0 else str(lab)
        g.append(f'<text x="{x:.1f}" y="16" font-family="{MATH}" font-size="11" '
                 f'fill="{AXIS}" text-anchor="middle">{s}</text>')
    xa = (open_at - lo) * step
    xb = (closed_at - lo) * step
    # shaded solution rays
    g.append(f'<path d="M{-10} 0H{xa:.1f}" stroke="{CURVE}" stroke-width="3.2"/>')
    g.append(f'<path d="M{xb:.1f} 0H{w+10}" stroke="{CURVE}" stroke-width="3.2"/>')
    g.append(f'<circle cx="{xa:.1f}" cy="0" r="4.6" fill="#ffffff" stroke="{CURVE}" stroke-width="1.8"/>')
    g.append(f'<circle cx="{xb:.1f}" cy="0" r="4.6" fill="#ffffff" stroke="{CURVE}" stroke-width="1.8"/>')
    return "".join(g)


def sqrt_expr(x, y, inner_parts, size=19, fill=TXT2):
    """Radical sign + overbar + inner expression, returns (svg, total_width)."""
    inner_w = 0.0
    for t, k in inner_parts:
        inner_w += len(t) * size * (0.36 if k == "sup" else 0.52)
    rw = size * 0.55
    g = []
    top = y - size * 0.98
    g.append(f'<path d="M{x:.1f} {y-size*0.42:.1f}L{x+rw*0.30:.1f} {y-size*0.18:.1f}'
             f'L{x+rw*0.62:.1f} {y+size*0.12:.1f}L{x+rw:.1f} {top:.1f}'
             f'H{x+rw+inner_w+6:.1f}" fill="none" stroke="{fill}" '
             f'stroke-width="1.3" stroke-linejoin="miter" stroke-linecap="round"/>')
    g.append(mathtext(x + rw + 3, y, inner_parts, size=size, fill=fill))
    return "".join(g), rw + inner_w + 8


# ---------- assemble the page --------------------------------------------

a(f'<svg xmlns="http://www.w3.org/2000/svg" width="8.5in" height="11in" viewBox="0 0 {W} {H}">')
a(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')
a(f'<rect x="18" y="18" width="{W-36}" height="{H-36}" fill="none" stroke="#d4d4d4" stroke-width="1.2"/>')
a('<g id="art">')

# --- top-left: 3-D axes with parabola, tipped back
a(f'<g transform="translate(52,58) matrix(1,0.05,-0.10,0.99,0,0)">{axes3d()}</g>')

# --- top-centre: quadratic formula (tilted slightly)
a('<g transform="translate(300,88) rotate(-4)">')
inner = [("b", "n"), ("2", "sup"), (" − 4ac", "n")]
sv, iw = sqrt_expr(58, 0, inner, size=20)
a(mathtext(0, 0, [("−b ± ", "n")], size=20, fill=TXT2))
a(sv)
bar_w = 58 + iw
a(f'<path d="M0 8H{bar_w:.0f}" stroke="{TXT2}" stroke-width="1.3"/>')
a(mathtext(bar_w / 2, 30, [("2a", "n")], size=20, fill=TXT2, anchor="middle"))
a(mathtext(-12, 8, [("x =", "n")], size=20, fill=TXT2, anchor="end"))
a('</g>')

# --- top-right: difference of squares
a(f'<g transform="translate(560,196) rotate(3)">'
  + mathtext(0, 0, [("a", "n"), ("2", "sup"), (" − b", "n"), ("2", "sup"),
                    (" = (a − b)(a + b)", "n")], size=19)
  + '</g>')

# --- right: parabola grid panel, tipped back to the right
a(f'<g transform="translate(548,232) matrix(0.97,0.16,-0.30,0.94,0,0)">'
  f'{parabola_panel(252, 196, coef=0.030)}</g>')

# --- f(x) = ax^2 + bx + c
a(f'<g transform="translate(210,272) rotate(-3)">'
  + mathtext(0, 0, [("f (x) = ax", "n"), ("2", "sup"), (" + bx + c", "n")], size=19)
  + '</g>')

# --- y = mx + b
a(f'<g transform="translate(64,404) rotate(2)">'
  + mathtext(0, 0, [("y = mx + b", "n")], size=19)
  + '</g>')

# --- left: cone
a(f'<g transform="translate(60,466) matrix(1,0.04,-0.07,1,0,0)">{cone(104,150)}</g>')

# --- left: slab with the solving steps
a(f'<g transform="translate(58,650) rotate(-2)">'
  + slab(0, 0, 208, 104, dx=18, dy=-13, label_lines=[
      [("2x + 3 = 7", "n")], [("2x = 4", "n")], [("x = 2", "n")]], size=17)
  + '</g>')

# --- right: cube
a(f'<g transform="translate(596,606) rotate(2)">{cube(102, 32, -25)}</g>')

# --- centre-low: unit circle
a(f'<g transform="translate(408,742) matrix(1,0.03,-0.05,1,0,0)">{unit_circle(44)}</g>')

# --- x^2 + y^2 = r^2
a(f'<g transform="translate(494,724) rotate(-2)">'
  + mathtext(0, 0, [("x", "n"), ("2", "sup"), (" + y", "n"), ("2", "sup"),
                    (" = r", "n"), ("2", "sup")], size=19)
  + '</g>')

# --- inequality + number line
a(f'<g transform="translate(58,840) rotate(1)">'
  + mathtext(0, 0, [("x", "n"), ("2", "sup"), (" − 5x + 6 > 0", "n")], size=19)
  + f'<g transform="translate(14,40)">{number_line(232)}</g></g>')

# --- distributive property slab
a(f'<g transform="translate(506,872) rotate(-2)">'
  + slab(0, 0, 232, 56, dx=17, dy=-12,
         label_lines=[[("a(b + c) = ab + ac", "n")]], size=18)
  + '</g>')

# --- bottom-left: sine panel, tipped forward
a(f'<g transform="translate(74,930) matrix(0.98,-0.13,0.26,0.95,0,0)">'
  f'{sine_panel(320, 150)}</g>')

# --- (x+2)^2 expansion
a(f'<g transform="translate(452,1002) rotate(2)">'
  + mathtext(0, 0, [("(x + 2)", "n"), ("2", "sup"), (" = x", "n"), ("2", "sup"),
                    (" + 4x + 4", "n")], size=19)
  + '</g>')

a('</g>')  # end art

# ---------- title block ---------------------------------------------------

def haloed(svg_text):
    """Draw the text twice: a white stroked copy underneath for legibility."""
    halo = svg_text.replace("<text ", '<text stroke="#ffffff" stroke-width="7" '
                                      'stroke-linejoin="round" ', 1)
    return halo + svg_text


a('<g id="title">')
title = (f'<text x="{W/2}" y="516" font-family="{SERIF}" font-size="94" fill="{TXT}" '
         f'text-anchor="middle" letter-spacing="1">Algebra 2</text>')
a(haloed(title))
a(f'<path d="M232 540H618" stroke="#ffffff" stroke-width="7"/>')
a(f'<path d="M232 540H618" stroke="{EDGE}" stroke-width="1.4"/>')
unit = (f'<text x="{W/2}" y="588" font-family="{SERIF}" font-size="42" fill="{TXT2}" '
        f'text-anchor="middle">Unit 1:  Foundations</text>')
a(haloed(unit))
a(f'<path d="M232 606H618" stroke="#ffffff" stroke-width="7"/>')
a(f'<path d="M232 606H618" stroke="{EDGE}" stroke-width="1.4"/>')
name = (f'<text x="{W/2}" y="672" font-family="{SCRIPT}" font-size="58" fill="{TXT}" '
        f'text-anchor="middle">Shepherd</text>')
a(haloed(name))
a(f'<path d="M318 692Q425 682 532 692" stroke="#ffffff" stroke-width="8" fill="none"/>')
a(f'<path d="M318 692Q425 682 532 692" stroke="{EDGE}" stroke-width="2" fill="none" stroke-linecap="round"/>')
a('</g>')

a('</svg>')

svg = "".join(out)
open("/home/claude/cover_front.svg", "w").write(svg)

# mirrored version
mirror = svg.replace(f'viewBox="0 0 {W} {H}">',
                     f'viewBox="0 0 {W} {H}"><g transform="translate({W},0) scale(-1,1)">')
mirror = mirror.replace("</svg>", "</g></svg>")
open("/home/claude/cover_back.svg", "w").write(mirror)
print("wrote both svgs", len(svg))
