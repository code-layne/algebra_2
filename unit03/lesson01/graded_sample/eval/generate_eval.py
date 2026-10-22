#!/usr/bin/env python3
"""Build the synthetic class set for graded_sample: the stand-in eval set.

For each of the 12 invented students in fake-roster.csv, this fills her
personalized quiz page with handwritten-looking answers, degrades the page like
a copier scan, and writes

  class-set-scan.pdf   all 12 pages, shuffled, 300 dpi grayscale (what ingest reads)
  expected-scores.csv  every student's correct score on every item, with the
                       response written and why it earns that score
  scan-pages.csv       ground truth for ingest: which student is on each scan
                       page, and the rotation/scale/shift applied to it

Responses are planned, not random guesses: about half the short-answer and
matching responses are correct; the rest come from the misconceptions Lesson 3.1
targets (dropping the sign change when subtracting, squaring a binomial as
a^2 + b^2, multiplying exponents instead of adding them) plus two other slips.
Exactly one item is left blank, exactly one answer is an equivalent form (1.5
for 3/2), and the rubric item gets written responses worth 0, 1, 2, 3 and 4
points (scored against ../../rubrics/alg2-u3-l1-gs-gs8.yaml, criterion by
criterion). Scoring is all-or-nothing on every non-rubric item: a set or an
expression earns its points only when complete and correct.

Everything is driven by one seed, so a rerun on the same build reproduces the
same files. Run it through make, which builds what it reads first:

    make -C unit03/lesson01 graded_sample_eval

or directly, after `make graded_sample` and `make roster-packets
COMP=graded_sample ROSTER=graded_sample/eval/fake-roster.csv`:

    python3 generate_eval.py [--seed N]

Needs Pillow and numpy, plus pdftoppm (poppler). The handwriting fonts are
Caveat and Indie Flower from Google Fonts (SIL Open Font License), in fonts/.
"""

import argparse
import csv
import json
import random
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = Path(__file__).resolve().parent
LESSON = HERE.parent.parent
ROOT = LESSON.parent.parent
BUILD = ROOT / "target" / "unit03" / "lesson01" / "grading" / "graded_sample"

DPI = 300
S = DPI / 72  # pixels per PDF point
FONTS = [HERE / "fonts" / "Caveat-Variable.ttf", HERE / "fonts" / "IndieFlower-Regular.ttf"]

# ── What students write ───────────────────────────────────────────────────────
# "^" starts a superscript (written smaller and raised), as students write it.
# Each wrong answer carries the error behind it; the three misconceptions the
# lesson targets are tagged "misconception:", other slips "error:".
SIGN = "misconception:subtraction-sign-change"
SQUARE = "misconception:binomial-square"
EXPONENT = "misconception:multiplied-exponents"

ITEMS = {
    "gs1": {"correct": ["A"], "wrong": [("B", SQUARE)]},
    "gs2": {"correct": ["C"], "wrong": [("D", EXPONENT)]},
    "gs3": {"correct": ["E"], "wrong": [("F", SIGN)]},
    "gs4": {"correct": ["G"], "wrong": [("B", "error:product-sign")]},
    "gs5": {"correct": ["3x^3 + 4x^2 - 5x - 4", "3x^3+4x^2-5x-4"],
            "wrong": [("3x^3 - 2x^2 - 3x + 8", SIGN),
                      ("3x^3 + 4x^2 - 3x + 8", SIGN)]},
    "gs6": {"correct": ["3/2"], "equivalent": "1.5",
            "wrong": [("14", "error:power-read-as-product"),
                      ("2", "error:squared-coefficient")]},
    "gs7": {"correct": ["5, 3", "3, 5"],
            "wrong": [("6, 2", EXPONENT), ("6, 3", EXPONENT)]},
}

# Work some students show beside item 5's box (outside it, so never graded).
WORK_GS5 = {
    True: ["5x^3-2x^3  x^2+3x^2", "-2x^3 +3x^2 -x -6"],
    False: ["5x^3-2x^3  x^2-3x^2", "-2x^3 -3x^2 +x +6"],
}

# Rubric responses, by score, each with its criterion breakdown
# (step, reason, corrected, answer — see the rubric YAML).
RUBRIC = {
    4: [("She went wrong when she took off the parentheses. Subtracting means every term "
         "of x^2 - 4x + 1 changes sign, not just the x^2. It should be "
         "3x^2 + 2x - 5 - x^2 + 4x - 1 = 2x^2 + 6x - 6", (1, 1, 1, 1)),
        ("Her first step is wrong: the minus goes to all three terms, so "
         "-(x^2 - 4x + 1) = -x^2 + 4x - 1. Then 3x^2 + 2x - 5 - x^2 + 4x - 1 = 2x^2 + 6x - 6",
         (1, 1, 1, 1))],
    3: [("The mistake is in the first step. She only subtracted the x^2 and forgot that the "
         "-4x and the +1 change signs too. Answer: 2x^2 + 6x - 6", (1, 1, 0, 1)),
        ("The first line is wrong. It should say 3x^2 + 2x - 5 - x^2 + 4x - 1, "
         "which makes 2x^2 + 6x - 6", (1, 0, 1, 1))],
    2: [("She forgot to distribute the negative to all the terms. "
         "3x^2 + 2x - 5 - x^2 + 4x - 1", (0, 1, 1, 0)),
        ("Her first line is wrong. The answer should be 2x^2 + 6x - 6", (1, 0, 0, 1)),
        ("You have to subtract every term, not just the first one, so the answer "
         "is 2x^2 + 6x - 6", (0, 1, 0, 1))],
    1: [("She messed up the signs. The answer is 2x^2 + 6x - 6", (0, 0, 0, 1)),
        ("Her first step is where it went wrong.", (1, 0, 0, 0))],
    0: [("Her answer is right because you combine like terms: 3x^2 - x^2 = 2x^2 "
         "and 2x - 4x = -2x", (0, 0, 0, 0)),
        ("She should have added them instead, 4x^2 - 2x - 4", (0, 0, 0, 0))],
}
RUBRIC_SCORES = [4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 2, 3]  # one per student, shuffled


def plan(students, manifest, rng):
    """Every student's response to every item, and its expected score."""
    points = {q["id"]: q["points"] for q in manifest["questions"]}
    types = {q["id"]: q["type"] for q in manifest["questions"]}
    slots = [(s, i) for s in students for i in ITEMS]

    # About half correct, weighted by an invented "ability" per student, so the
    # class has strong and weak papers rather than coin flips on every item.
    ability = dict(zip(students, rng.sample([0.2 + 0.06 * k for k in range(len(students))],
                                            len(students))))
    keyed = sorted(slots, key=lambda sl: rng.random() ** (1 / ability[sl[0]]), reverse=True)
    correct = set(keyed[:len(slots) // 2])

    # Exactly one equivalent form (1.5 for 3/2) and exactly one blank.
    equivalent = rng.choice([sl for sl in sorted(correct) if sl[1] == "gs6"])
    blank = rng.choice([sl for sl in sorted(set(slots) - correct) if sl[1] != "gs6"])

    rows = []
    rubric_scores = rng.sample(RUBRIC_SCORES, len(RUBRIC_SCORES))
    used = {k: 0 for k in RUBRIC}
    for n, s in enumerate(students):
        for i, bank in ITEMS.items():
            if (s, i) == blank:
                resp, cat, pts = "", "blank", 0
            elif (s, i) == equivalent:
                resp, cat, pts = bank["equivalent"], "equivalent-form", points[i]
            elif (s, i) in correct:
                resp, cat, pts = rng.choice(bank["correct"]), "correct", points[i]
            else:
                resp, cat = rng.choice(bank["wrong"])
                pts = 0
            rows.append({"tracking_id": s, "item": i, "type": types[i],
                         "max_points": points[i], "points": pts, "category": cat,
                         "response": resp, "criteria": ""})
        score = rubric_scores[n]
        text, crit = RUBRIC[score][used[score] % len(RUBRIC[score])]
        used[score] += 1
        assert sum(crit) == score
        rows.append({"tracking_id": s, "item": "gs8", "type": "rubric", "max_points": points["gs8"],
                     "points": score, "category": f"rubric-{score}", "response": text,
                     "criteria": ";".join(f"{c}={v}" for c, v in
                                          zip(("step", "reason", "corrected", "answer"), crit))})
    return rows


# ── Handwriting ───────────────────────────────────────────────────────────────

def tokens(text):
    """(char, superscript?) pairs: "x^23" -> x, 2*, 3*."""
    out, sup = [], False
    for ch in text:
        if ch == "^":
            sup = True
            continue
        if sup and not ch.isdigit():
            sup = False
        out.append((ch, sup))
    return out


class Hand:
    """One student's handwriting: a font, a weight, an ink tone, a slant habit."""

    def __init__(self, rng, font_path):
        self.rng = rng
        self.path = str(font_path)
        self.weight = rng.uniform(420, 640) if "Caveat" in self.path else None
        self.ink = rng.uniform(25, 85)  # pencil/pen darkness, 0 = black
        self.slant = rng.uniform(-3.0, 3.0)
        self._fonts = {}

    def font(self, size):
        size = max(8, int(round(size)))
        if size not in self._fonts:
            f = ImageFont.truetype(self.path, size)
            if self.weight is not None:
                try:
                    f.set_variation_by_axes([self.weight])
                except (OSError, AttributeError):
                    pass
            self._fonts[size] = f
        return self._fonts[size]

    def line(self, text, size):
        """An alpha mask of one written line, with per-character jitter in
        size and baseline."""
        rng = self.rng
        w = int(size * (len(text) + 2) * 0.9) + 40
        h = int(size * 2.4)
        mask = Image.new("L", (w, h), 0)
        d = ImageDraw.Draw(mask)
        x, base = size * 0.3, h * 0.68
        for ch, sup in tokens(text):
            s = size * rng.uniform(0.9, 1.1) * (0.6 if sup else 1)
            f = self.font(s)
            y = base + rng.uniform(-0.05, 0.05) * size - (0.45 * size if sup else 0)
            if ch != " ":
                d.text((x, y), ch, font=f, fill=255, anchor="ls")
            x += f.getlength(ch) * rng.uniform(0.96, 1.1) + (size * 0.05 if ch == " " else 0)
        bbox = mask.getbbox()
        return mask.crop(bbox) if bbox else mask.crop((0, 0, 1, 1))

    def block(self, text, size, width):
        """Several lines, word-wrapped to width pixels, slightly uneven."""
        words, lines, cur = text.split(), [], ""
        for wd in words:
            trial = f"{cur} {wd}".strip()
            if cur and self.font(size).getlength(trial.replace("^", "")) > width:
                lines.append(cur)
                cur = wd
            else:
                cur = trial
        lines.append(cur)
        masks = [self.line(l, size) for l in lines]
        step = int(size * 1.35)
        out = Image.new("L", (max(m.width for m in masks) + int(size), step * len(masks) + int(size)), 0)
        for k, m in enumerate(masks):
            dx = int(self.rng.uniform(0, size * 0.25))
            out.paste(m, (dx, k * step + int(step - m.height * 0.8)), m)
        return out.crop(out.getbbox())


def write_in(page, mask, box, hand, rng, margin=0.12, align="center"):
    """Composite a handwriting mask into a box (PDF points), rotated by the
    student's slant plus jitter, shrunk to fit inside the box."""
    x, y, w, h = box
    angle = hand.slant + rng.uniform(-2.5, 2.5)
    m = mask.rotate(angle, resample=Image.BICUBIC, expand=True)
    bw, bh = w * S * (1 - 2 * margin), h * S * (1 - 2 * margin)
    k = min(1.0, bw / m.width, bh / m.height)
    if k < 1:
        m = m.resize((max(1, int(m.width * k)), max(1, int(m.height * k))), Image.LANCZOS)
    left, top = x * S, (page.height / S - y - h) * S
    free_x, free_y = w * S - m.width, h * S - m.height
    fx = rng.uniform(0.3, 0.55) if align == "center" else rng.uniform(0.04, 0.1)
    px = int(left + free_x * fx)
    py = int(top + free_y * rng.uniform(0.3, 0.6))
    arr = np.asarray(page, dtype=np.float32)
    a = np.asarray(m, dtype=np.float32) / 255 * rng.uniform(0.82, 0.95)
    region = arr[py:py + m.height, px:px + m.width]
    a = a[:region.shape[0], :region.shape[1]]
    arr[py:py + a.shape[0], px:px + a.shape[1]] = region * (1 - a) + hand.ink * a
    return Image.fromarray(arr.clip(0, 255).astype(np.uint8))


def fill_page(page, rows, manifest, hand, rng):
    boxes = {q["id"]: q["box"] for q in manifest["questions"]}
    for r in rows:
        if not r["response"]:
            continue
        x, y, w, h = boxes[r["item"]]
        if r["type"] == "choice":
            mask = hand.line(r["response"], h * S * rng.uniform(0.62, 0.75))
            page = write_in(page, mask, boxes[r["item"]], hand, rng, margin=0.14)
        elif r["type"] == "short":
            mask = hand.line(r["response"], h * S * rng.uniform(0.5, 0.6))
            page = write_in(page, mask, boxes[r["item"]], hand, rng)
        else:
            size = 15 * S * rng.uniform(0.9, 1.05)
            mask = hand.block(r["response"], size, w * S * 0.9)
            while mask.height > h * S * 0.88 and size > 8 * S:
                size *= 0.92
                mask = hand.block(r["response"], size, w * S * 0.9)
            page = write_in(page, mask, boxes[r["item"]], hand, rng, margin=0.04, align="left")
    # Scratch work beside item 5's box, for about half the class.
    gs5 = next(r for r in rows if r["item"] == "gs5")
    if gs5["response"] and rng.random() < 0.5:
        x, y, w, h = boxes["gs5"]
        work = WORK_GS5[gs5["category"] == "correct"]
        mask = hand.block("   ".join(work), 11 * S, (x - 90) * S)
        page = write_in(page, mask, (78, y - 6, x - 98, h + 10), hand, rng, margin=0.02, align="left")
    return page


# ── The copier ────────────────────────────────────────────────────────────────

def scan(page, rng, nrng):
    """Grayscale copier scan: rotation, scaling, shift, toner and paper tone,
    blur, sensor noise, specks."""
    W, H = page.size
    angle = rng.uniform(-1.2, 1.2)
    scale = rng.uniform(0.975, 1.02)
    im = page.rotate(angle, resample=Image.BICUBIC, fillcolor=255)
    im = im.resize((round(W * scale), round(H * scale)), Image.BICUBIC)
    dx = (W - im.width) // 2 + rng.randint(-24, 24)
    dy = (H - im.height) // 2 + rng.randint(-24, 24)
    canvas = Image.new("L", (W, H), 255)
    canvas.paste(im, (dx, dy))
    canvas = canvas.filter(ImageFilter.GaussianBlur(rng.uniform(0.5, 0.9)))
    arr = np.asarray(canvas, dtype=np.float32)
    paper, toner = rng.uniform(232, 246), rng.uniform(18, 45)
    arr = toner + (paper - toner) * (arr / 255)
    arr += nrng.normal(0, rng.uniform(2.5, 4.5), arr.shape)
    for _ in range(rng.randint(150, 400)):  # dust and toner specks
        cx, cy, r = rng.randrange(W), rng.randrange(H), rng.choice((1, 1, 2, 3))
        arr[max(cy - r, 0):cy + r, max(cx - r, 0):cx + r] *= rng.uniform(0.3, 0.8)
    out = Image.fromarray(arr.clip(0, 255).astype(np.uint8))
    return out, {"rotation_deg": round(angle, 3), "scale": round(scale, 4), "dx_px": dx, "dy_px": dy}


def render(pdf):
    with tempfile.TemporaryDirectory() as t:
        subprocess.run(["pdftoppm", "-gray", "-r", str(DPI), "-f", "1", "-l", "1", "-singlefile",
                        str(pdf), f"{t}/p"], check=True)
        return Image.open(f"{t}/p.pgm").convert("L").copy()


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--seed", type=int, default=20261021)
    ap.add_argument("--build", type=Path, default=BUILD,
                    help="grading output for graded_sample (manifest.json, students/)")
    ap.add_argument("--out", type=Path, default=HERE)
    args = ap.parse_args()

    manifest = json.loads((args.build / "manifest.json").read_text())
    if manifest["pages"] != 1:
        sys.exit("generate_eval: graded_sample must be one page")
    with open(HERE / "fake-roster.csv", newline="", encoding="utf-8") as f:
        students = [r["tracking_id"] for r in csv.DictReader(f)]
    missing = [s for s in students if not (args.build / "students" / f"{s}.pdf").exists()]
    if missing:
        sys.exit(f"generate_eval: no personalized copy for {missing}; run "
                 "`make -C unit03/lesson01 graded_sample_eval`")

    rng = random.Random(args.seed)
    nrng = np.random.default_rng(args.seed)
    rows = plan(students, manifest, rng)

    pages, meta = [], []
    for k, s in enumerate(students):
        hand = Hand(rng, FONTS[k % 2])
        page = render(args.build / "students" / f"{s}.pdf")
        page = fill_page(page, [r for r in rows if r["tracking_id"] == s], manifest, hand, rng)
        scanned, m = scan(page, rng, nrng)
        pages.append(scanned)
        meta.append({"tracking_id": s, "page": 1, "font": FONTS[k % 2].stem, **m})

    order = list(range(len(pages)))
    rng.shuffle(order)
    out_pdf = args.out / "class-set-scan.pdf"
    first, *rest = [pages[i] for i in order]
    # Fixed dates keep a rerun byte-identical (Pillow otherwise stamps "now").
    stamp = time.strptime("2026-10-21", "%Y-%m-%d")
    first.save(out_pdf, "PDF", save_all=True, append_images=rest, resolution=DPI, quality=55,
               creationDate=stamp, modDate=stamp)

    with open(args.out / "scan-pages.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["scan_page", *meta[0]], lineterminator="\n")
        w.writeheader()
        for n, i in enumerate(order, 1):
            w.writerow({"scan_page": n, **meta[i]})
    with open(args.out / "expected-scores.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

    nonrubric = [r for r in rows if r["type"] != "rubric"]
    right = sum(r["category"] in ("correct", "equivalent-form") for r in nonrubric)
    cats = {}
    for r in rows:
        cats[r["category"]] = cats.get(r["category"], 0) + 1
    print(f"{len(students)} students, {len(rows)} responses -> {out_pdf.name}, expected-scores.csv, "
          f"scan-pages.csv")
    print(f"  non-rubric: {right}/{len(nonrubric)} correct (incl. equivalent form)")
    for c in sorted(cats):
        print(f"  {cats[c]:3d}  {c}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
