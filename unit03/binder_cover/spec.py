"""Unit 3 binder-cover content spec.

Consumed by shared/cover.py. Every element below is lifted from a Unit 3
lesson source — nothing here is content the unit does not teach. The lesson
each one comes from is noted so this stays checkable when the unit changes.

The unit's spine is one curve seen in every costume: $x^2-2x-3$, which is
$(x-1)^2-4$ in vertex form and $(x+1)(x-3)$ factored. It appears here as a
graph (3.0), a factoring solve (3.2), a completing-the-square solve (3.3),
and a linear--quadratic system (3.6). The one quadratic that will not yield a
real answer, $x^2+2x+5=0$, carries the complex thread (3.4 → 3.5).

Placement is hand-tuned: `at` is the element's top-left anchor, `tilt` rotates
it and `skew` leans it, both about its own centre. Elements with neither get
one assigned automatically. Drop the `at` keys and the auto-layout takes over.
"""

# ── Elements ─────────────────────────────────────────────────────────────────

ELEMENTS = [
    # 3.0/3.1 — the parent $y=x^2$ and the unit anchor $(x-1)^2-4$ beside it:
    # the whole transformation lesson in one panel.
    {"type": "graph", "at": (44, 50), "w": 252, "h": 180,
     "xr": (-4, 4), "yr": (-5, 6),
     "curves": [lambda x: x * x, lambda x: (x - 1) ** 2 - 4],
     "skew": (1, 0.05, -0.10, 0.99)},

    # 3.1 — vertex form, the form every characteristic is read straight off.
    {"type": "equation", "at": (338, 62), "size": 20, "tilt": -3,
     "expr": r"f(x) = a(x-h)^2 + k"},

    # 3.5 — the quadratic formula: the one method that solves every quadratic.
    {"type": "equation", "at": (330, 130), "size": 21, "tilt": 2,
     "expr": r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}"},

    # 3.6 — the unit anchor met by the line $y=x-3$: two points of intersection.
    {"type": "graph", "at": (566, 54), "w": 232, "h": 176,
     "xr": (-3, 5), "yr": (-5, 5),
     "curves": [lambda x: x * x - 2 * x - 3, lambda x: x - 3],
     "skew": (0.97, 0.16, -0.30, 0.94)},

    # 3.1 — the axis of symmetry from standard form.
    {"type": "equation", "at": (60, 268), "size": 19, "tilt": 2,
     "expr": r"x = -\frac{b}{2a}"},

    # 3.2 — the anchor solved by factoring, via the Zero Product Property.
    {"type": "slab", "at": (204, 250), "size": 16, "dx": 17, "dy": -12, "tilt": -2,
     "lines": [r"x^2 - 2x - 3 = 0",
               r"(x + 1)(x - 3) = 0",
               r"x = -1 \quad x = 3"]},

    # 3.3 — the same anchor by completing the square, landing on vertex form.
    {"type": "slab", "at": (48, 336), "size": 16, "dx": 18, "dy": -13, "tilt": 3,
     "lines": [r"x^2 - 2x = 3",
               r"(x - 1)^2 = 4",
               r"x = 1 \pm 2"]},

    # 3.3 — the Square Root Property, the first method past factoring.
    {"type": "equation", "at": (582, 268), "size": 19, "tilt": 2,
     "expr": r"x^2 = k \Rightarrow x = \pm\sqrt{k}"},

    # 3.1 — intercept form: the zeros readable on sight.
    {"type": "equation", "at": (568, 344), "size": 19, "tilt": -2,
     "expr": r"f(x) = a(x - p)(x - q)"},

    # 3.5 — the no-real-root case made visible: $y=x^2+4$ never meets the axis,
    # so it sits with the complex thread it forces.
    {"type": "graph", "at": (50, 736), "w": 200, "h": 180,
     "xr": (-3, 3), "yr": (-1, 13), "xtick": 1, "ytick": 4,
     "curves": [lambda x: x * x + 4],
     "skew": (0.98, -0.13, 0.26, 0.95)},

    # 3.4 — the imaginary unit, invented to break the negative-radicand wall.
    {"type": "equation", "at": (326, 744), "size": 21, "tilt": -3,
     "expr": r"i = \sqrt{-1} \quad i^2 = -1"},

    # 3.4/3.5 — the quadratic that has no real answer, finished over $a+bi$.
    {"type": "slab", "at": (612, 748), "size": 16, "dx": 17, "dy": -12, "tilt": -2,
     "lines": [r"x^2 + 2x + 5 = 0",
               r"(x + 1)^2 = -4",
               r"x = -1 \pm 2i"]},

    # 3.4 — the conjugate product, which is always real.
    {"type": "equation", "at": (312, 848), "size": 19, "tilt": 2,
     "expr": r"(a + bi)(a - bi) = a^2 + b^2"},

    # 3.5 — the discriminant, read before solving: two / one / no real roots.
    {"type": "slab", "at": (610, 906), "size": 16, "dx": 17, "dy": -12, "tilt": 2,
     "lines": [r"b^2 - 4ac > 0",
               r"b^2 - 4ac = 0",
               r"b^2 - 4ac < 0"]},

    # 3.0/3.7 — the projectile the unit opens and closes on: starts at 48 ft,
    # tops out at $(1,64)$, lands at $t=3$.
    {"type": "equation", "at": (58, 966), "size": 20, "tilt": -2,
     "expr": r"h(t) = -16t^2 + 32t + 48"},

    # 3.7 — the maximum-area pen against the barn wall; vertex $(10,200)$.
    {"type": "equation", "at": (376, 976), "size": 19, "tilt": 3,
     "expr": r"A(x) = x(40 - 2x)"},
]
