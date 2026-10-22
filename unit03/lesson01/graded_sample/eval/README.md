# graded_sample eval set (synthetic)

The stand-in eval set for the grading pipeline (build-order step 2 in
`math-shared/grading-system-design.md`), until a hand-graded real class set
replaces it. Everything here is invented. No real student's name or work is in it.

| File | What it is |
| --- | --- |
| `class-set-scan.pdf` | Twelve filled-in quizzes, one page each. Pages are shuffled, scanned as 300 dpi grayscale, and degraded like a copier: rotated up to ±1.2°, scaled 0.975–1.02, shifted, blurred, with noise and specks. This is what ingest reads. |
| `expected-scores.csv` | The correct score on every item for every student (96 rows). Each row has the response as written (`^` marks a superscript), why it earns that score, and, for the rubric item, the criterion breakdown. |
| `scan-pages.csv` | Ground truth for ingest. For each scan page: the student, and the rotation, scale and shift applied. |
| `fake-roster.csv` | The invented class in `roster-map.csv` format, written by `make_fake_roster.py`. `roster_import.py` refuses to write inside a git work tree. |
| `generate_eval.py` | Builds the three outputs above from the personalized quiz pages. |
| `fonts/` | Caveat and Indie Flower from Google Fonts (SIL Open Font License; the licenses are next to them). |

## The responses

The quiz is `../main.tex`: four matching items, three short answers (one each
for the expression, numeric and set checks), and one 4-point rubric item
(`../../rubrics/alg2-u3-l1-gs-gs8.yaml`).

- **Correct answers:** 42 of the 84 matching and short answers are correct. This
  is weighted by an invented ability per student, so papers range from strong to weak.
- **Equivalent form:** exactly one correct answer is written in a different
  form: `1.5` for `3/2` on item 6. It earns full credit.
- **Blank:** exactly one item is left blank.
- **Wrong answers:** each comes from one of Lesson 3.1's target misconceptions,
  or from one of three other slips:

  | Error | Category |
  | --- | --- |
  | Dropping the sign change when subtracting (item 3 `F`, item 5 `3x^3 - 2x^2 - 3x + 8`) | `misconception:subtraction-sign-change` |
  | Squaring a binomial as a^2 + b^2 (item 1 `B`) | `misconception:binomial-square` |
  | Multiplying exponents instead of adding them (item 2 `D`, item 7 `6, 2`, or `6, 3` when only the first term is multiplied) | `misconception:multiplied-exponents` |
  | Sign slip in (x-3)(x+3) (item 4 `B`) | `error:product-sign` |
  | Reading x^3 as 3x (item 6 `14`) | `error:power-read-as-product` |
  | Squaring the coefficient, (2x)^2 for 2x^2 (item 6 `2`) | `error:squared-coefficient` |

- **Rubric:** the rubric responses are worth 0, 1, 2, 3 and 4 points, at least two
  of each, scored criterion by criterion (step, reason, corrected, answer).
- **Scoring:** every non-rubric item is all-or-nothing. An expression or a set
  earns its points only when it is complete and correct.

About half of the students show scratch work beside item 5's box. It is
outside the box, so it is never graded, and ingest must not crop it.

## Regenerating

```sh
make -C unit03/lesson01 graded_sample_eval
```

This builds the quiz, its key and `manifest.json`, then one personalized copy
per invented student. It reruns `generate_eval.py`, which needs Pillow, numpy
and pdftoppm. One seed (`--seed`, default 20261021) drives everything, so the
same build gives byte-identical outputs.

Run `python3 make_fake_roster.py` only if the class should change. That also
changes every tracking id.
