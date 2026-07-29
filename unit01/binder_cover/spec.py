"""Unit 1 binder-cover content spec.

Consumed by shared/cover.py. Every element below is lifted from a Unit 1
lesson source — nothing here is content the unit does not teach. The lesson
each one comes from is noted so this stays checkable when the unit changes.

Placement is hand-tuned: `at` is the element's top-left anchor, `tilt` rotates
it and `skew` leans it, both about its own centre. Elements with neither get
one assigned automatically. Drop the `at` keys and the auto-layout takes over.
"""

# ── Elements ─────────────────────────────────────────────────────────────────

ELEMENTS = [
    # 1.0 — the real-number set nesting from the notes: R > Q > Z > W > N,
    # with the irrationals that live in R but outside Q.
    {"type": "sets", "at": (46, 52), "w": 250, "h": 176,
     "outside": [r"\pi", r"\sqrt{5}", r"\sqrt[3]{2}", "e"],
     "skew": (1, 0.05, -0.10, 0.99)},

    # 1.2 — the quadratic formula, boxed in the notes as Method 3.
    {"type": "equation", "at": (348, 74), "size": 21, "tilt": -4,
     "expr": r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}"},

    # 1.2/1.3 — y = x^2 - 2x - 3, the curve the unit returns to three times.
    {"type": "graph", "at": (556, 52), "w": 238, "h": 178,
     "xr": (-3, 5), "yr": (-5, 5), "curves": [lambda x: x * x - 2 * x - 3],
     "skew": (0.97, 0.16, -0.30, 0.94)},

    # 1.1 — the product law of exponents, derived by counting factors.
    {"type": "equation", "at": (58, 262), "size": 19, "tilt": 2,
     "expr": r"a^m\cdot a^n = a^{m+n}"},

    # 1.1 — difference of squares, recognized on sight.
    {"type": "equation", "at": (300, 236), "size": 19, "tilt": 3,
     "expr": r"a^2 - b^2 = (a - b)(a + b)"},

    # 1.2 — the worked quadratic-formula solve of x^2 - 4x - 7 = 0.
    {"type": "slab", "at": (48, 306), "size": 17, "dx": 18, "dy": -13, "tilt": -2,
     "lines": [r"\frac{4 \pm \sqrt{44}}{2}",
               r"\frac{4 \pm 2\sqrt{11}}{2}",
               r"2 \pm \sqrt{11}"]},

    # 1.3 — f(x) = 2x - 6, the line every characteristic is read off.
    {"type": "graph", "at": (556, 268), "w": 238, "h": 176,
     "xr": (-3, 5), "yr": (-7, 5), "curves": [lambda x: 2 * x - 6],
     "skew": (0.99, 0.09, 0.20, 0.97)},

    # 1.3 — h(x) = 2^x, the exponential on its own tall window.
    {"type": "graph", "at": (52, 742), "w": 232, "h": 180,
     "xr": (-3, 4), "yr": (-2, 17), "ytick": 4,
     "curves": [lambda x: 2 ** x],
     "skew": (0.98, -0.13, 0.26, 0.95)},

    # 1.3 — slope as a rate of change.
    {"type": "equation", "at": (322, 748), "size": 19, "tilt": 2,
     "expr": r"m = \frac{y_2 - y_1}{x_2 - x_1}"},

    # 1.2 — the worked factoring solve of x^2 + x = 12.
    {"type": "slab", "at": (534, 736), "size": 16, "dx": 17, "dy": -12, "tilt": 2,
     "lines": [r"x^2 + x = 12",
               r"x^2 + x - 12 = 0",
               r"(x + 4)(x - 3) = 0",
               r"x = -4 \quad x = 3"]},

    # 1.2 — the solution set of -5x + 3 \ge 23, graphed on a number line.
    {"type": "numberline", "at": (318, 856), "w": 226, "lo": -6, "hi": 4,
     "expr": r"x \le -4", "size": 18,
     "shade": [(None, -4)], "marks": [(-4, "closed")], "tilt": 1},

    # 1.1 — simplest radical form, pulling out the largest perfect square.
    # (x chosen so it clears the number line on page 2's mirrored composition)
    {"type": "equation", "at": (612, 906), "size": 19, "tilt": -3,
     "expr": r"\sqrt{72} = 6\sqrt{2}"},

    # 1.0 — the distributive property, the engine of every product in the unit.
    {"type": "slab", "at": (64, 968), "size": 18, "dx": 17, "dy": -12, "tilt": -2,
     "lines": [r"a(b + c) = ab + ac"]},

    # 1.3 — the bacteria colony, P(t) = 50\cdot 2^t.
    {"type": "equation", "at": (352, 1012), "size": 19, "tilt": 2,
     "expr": r"P(t) = 50\cdot 2^t"},
]
