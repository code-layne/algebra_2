# Build System

The project compiles with **XeLaTeX** (via `latexmk`), merges PDFs with **`pdfunite`** (poppler),
and wraps slide decks into `.pptx` with **`shared/pdf2pptx.py`**. The skill authors `.tex`; the
project's own Makefiles do the building. **Never edit `shared/` or the Makefiles to make a lesson
build — fix the lesson's `.tex` instead.**

## The five work products

Every lesson builds exactly five files into `target/compiled/unitXX/`:

| File | What it is | Built from |
| --- | --- | --- |
| `lessonYY_plan.pdf` | the teacher-facing lesson plan | the lesson-root `main.tex` |
| `lessonYY_slides.pdf` | the deck **printed**: 3 slides per page, notes column beside each | `slides/main.tex` |
| `lessonYY_slides.pptx` | the deck **projected**: full page, one page image per slide | `slides/main.tex` |
| `lessonYY_student.pdf` | cover + blank components, paginated packet-wide | the student components |
| `lessonYY_key.pdf` | that packet answered, page for page | the `_key` components |

There is **no `full` packet** — it was removed. The plan and the deck are their own deliverables
now, so nothing bundles them behind a cover with the answer keys.

**The two slide products are the same deck in its two forms** — the PDF is what you print, the
PPTX is what you project. Both are generated from the one Beamer deck compiled at
`target/unitXX/lessonYY/slides/main.pdf`, which is the source of truth. `shared/handout.tex`
re-frames its pages 3-up with a ruled note area beside each slide (`shared/pdf2pptx.py` gets the
raw full-page deck, since a PowerPoint of handout pages would be useless). Neither product is
ever edited by hand: change `slides/main.tex` and rebuild.

## The three-level Make hierarchy

Each level is a thin `Makefile` that includes a `shared/*.mk`. The scaffolder creates them as
needed (see "Scaffolding a lesson"), so you rarely write them by hand:

- **Root `Makefile`** (`include shared/root.mk`) — discovers `unit*/Makefile`, delegates, and
  merges unit PDFs into `target/compiled/curriculum_{student,key}.pdf`.
- **`unitXX/Makefile`** (`include ../shared/unit.mk`) — discovers `lesson*/Makefile`,
  delegates, and merges lesson PDFs into `target/compiled/unitXX_{student,key}.pdf`. It also
  merges the unit's `unit_cover`, `sample_test`, and `sample_test_key` (see "Unit assessments").
  **Only the two packets aggregate to unit level** — plans and decks stay per-lesson.
- **`lessonYY/Makefile`** (`include ../../shared/lesson.mk`) — the engine. It:
  - **Discovers a component if it has `main.tex` or `main.pdf`.** Authored components
    (`main.tex`) are compiled; prefab components (`main.pdf`) are used as-is from the source
    tree. A directory with neither is skipped.
  - Compiles each `<comp>/main.tex` with
    `latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error`,
    sending output to `target/UNIT/LESSON/<comp>/` and a stamp to `.stamps/`.
  - Copies the plan to its `_plan.pdf` name, renders the deck 3-up to `_slides.pdf` and
    full-page to `_slides.pptx`, and merges the two packets:
    - **student** = `cover warmup experience` + the legacy `notes activity exit_ticket homework`
      still merged for pre-EFFL lessons (blank versions
      present — EFFL lessons have `experience` and no `notes`/`activity`/`exit_ticket`; legacy
      lessons the reverse),
      in that pedagogical order → `lessonYY_student.pdf`.
    - **key** = the *same* packet with every blank component swapped for its `_key` (cover has no
      key and appears unchanged) → `lessonYY_key.pdf`. It carries no lesson plan and no slides —
      it is the student packet, answered, **page for page** (see "Packet pagination").

## Commands

```bash
make -C unitXX/lessonYY all       # all five work products
make -C unitXX/lessonYY plan      # lessonYY_plan.pdf
make -C unitXX/lessonYY slides    # lessonYY_slides.pdf  — 3-up printable
make -C unitXX/lessonYY pptx      # lessonYY_slides.pptx — full-page projectable
make -C unitXX/lessonYY student   # student packet for one lesson
make -C unitXX/lessonYY key       # answer-key packet, paginated to match the student packet
make -C unitXX/lessonYY clean     # remove this lesson's target/ and stamps

make -C unitXX student|key        # merge a whole unit
make student|key                  # merge the whole curriculum (from project root)
make clean | distclean            # clean everything (distclean also removes target/ and .stamps)
```

`plan`, `slides`, and `pptx` are incremental — they are real file targets and rebuild only when
their source changes. `student` and `key` always re-merge, because the pagination pass measures
both packets against each other every time.

Outputs land in `target/`: per-component PDFs under `target/UNIT/LESSON/<comp>/main.pdf`, the
five work products under `target/compiled/unitXX/`.

**Build with `make all`** when the lesson plan embeds a warm-up thumbnail: the thumbnail uses the
warm-up. Authored warm-ups are text-only in the plan (no thumbnail); prefab warm-ups embed
`warmup/main` (the PDF in the source tree), which resolves regardless of order.

## Slides → printed handout

`shared/handout.tex` turns the compiled deck into `lessonYY_slides.pdf`: three slides per letter
page, thumbnails down the left column, a labelled ruled note area beside each on the right. Every
slide is placed with `\includegraphics[page=n]`, so figures and math render exactly as they do on
the projector — the pass only re-frames.

- The Makefile passes the deck's page count in as `\DeckPages` (LaTeX cannot count the pages of
  an external PDF; `pdfinfo` already is a build dependency).
- The note column's height is measured from the slide beside it, so both columns end on the same
  line whatever the deck's aspect ratio.
- Tuning lives at the top of `handout.tex`: `\slidewidth` (4.35in), `\colgap`, `\NoteLines` (6).
  The note column resizes itself from `\slidewidth`.
- A deck whose slide count is not a multiple of three leaves the last page short; rows stay
  top-aligned rather than stretching to fill it.

## Slides → PPTX

`shared/pdf2pptx.py` wraps the **raw deck** (`target/unitXX/lessonYY/slides/main.pdf`, not the
3-up handout) into `lessonYY_slides.pptx`: `pdftoppm`
rasterizes each page at 300 dpi and the script writes the OOXML package with `zipfile`, one
full-bleed page image per slide. It is deliberately **dependency-free** — no LibreOffice, no
`python-pptx`; it uses only the poppler tools the build already needs.

- The canvas is scaled, aspect preserved, to PowerPoint's standard 7.5in height, so a 16:9 deck
  lands on exactly 13.333 × 7.5in ("Widescreen").
- **The slides are images, not editable text.** That is the point: TikZ figures and math render
  exactly as they do in the PDF. The `.tex` is the source of truth — edit it and rebuild.
  **Never edit the `.pptx`**; the next build overwrites it.
- Override the resolution with `make -C unitXX/lessonYY pptx PPTX_DPI=200` to trade sharpness for
  file size (a typical deck is ~1 MB at 300 dpi).

## Scaffolding a lesson

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/new_lesson.py --project . --unit 02 --lesson 03 \
  --title "..." --unit-title "..." \
  --components cover,warmup,experience,slides \
  [--prefab warmup,warmup_key] [--course "Algebra 2: Shepherd"] [--lesson-id 1.3]
```

That component list is the default — `slides` included, since two of the five work products come
from the deck.

It detects the prefix (`algebra2`) from `shared/*-colors.sty`, and detects whether `\CourseName`
is defined in `shared/` — it is **not** in this course, so the generated lesson plan inlines the
course macros (pass `--course`/`--year` to set them; they default to "Algebra 2: Shepherd" /
2026–2027 if detected). It writes the lesson `Makefile`, the lesson plan, and each authored
component + key skeleton — **and creates the unit `Makefile` (and the root `Makefile` if it were
missing)** so unit/curriculum builds work, never clobbering existing ones. Pass `--prefab <dirs>`
to create empty drop-in directories instead (where you place each `main.pdf`). The `slides`
component requires `shared/algebra2-beamer.sty`; the scaffolder errors if it is missing. Then
author the skeletons (`references/components.md`).

## Prefab PDFs

To include a ready-made PDF as a component, drop it in as `<comp>/main.pdf` (and
`<comp>_key/main.pdf` for a prefab key). `lesson.mk` discovers it and feeds it straight to
`pdfunite` — no `main.tex`, no compile step. `make clean` removes only `target/` and stamps, so
your source PDFs are never deleted.

## Packet pagination and imposition (student + key packets)

Each component is its own document, so each numbers its pages from 1 and a naively merged packet
reads `1 / 1 / 1 2 3 4 5 / …`. After `pdfunite` builds the **student** or **key** packet,
`shared/lesson.mk` therefore runs one extra XeLaTeX pass over the merged PDF
(`shared/paginate.tex`, invoked through the `paginate` define) that:

- **numbers the packet end to end** — every page is re-placed at its original size and the
  packet-wide number is stamped in the article class's own footer position, masking the
  component-local one with a white band inside the bottom margin;
- **starts every component on an odd page** — the recipe reads each component's page count with
  `pdfinfo` and builds a pdfpages page list with `{}` (empty page) padding, passed in as
  `\PacketPages`. Inserted blanks are numbered like any other page; and
- **keeps the student and key packets page for page** — each component gets the same *slot* in
  both packets, `max(blank pages, key pages)` rounded up to even, and the shorter side is padded
  with blank versos to fill it. So the teacher's page 7 is the student's page 7. Both targets
  compute the slots from the same two PDF lists, so they agree whether built together or
  separately — which is why `make student` compiles the `_key` components too.

This is automatic for every lesson — **no `.tex` change and no per-lesson sweep**. Notes:

- The last component is padded too, so every lesson packet has an **even** page count. Student
  packets are **duplex** documents — that is what the imposition is for.
- A key component that runs longer than its blank (answers take room) costs the *student* packet
  padding pages. That is the price of matched pagination; keep keys tight where you can.
- It assumes letter-size pages and the `algebra2-article` bottom margin. A prefab drop-in of a
  different page size would get its number misplaced; re-measure and adjust `\PgBaseline` if the
  shared geometry ever changes.
- **The plan and the deck are never paginated or imposed** — they are standalone documents, and
  the deck is 16:9 rather than letter, so the letter-paper stamping pass does not apply to them.
- **Unit packets are deliberately out of scope**: they inherit even lesson packets, but `unit.mk`
  neither numbers them nor pads `unit_cover` (1pp), so the first lesson opens on a verso. The
  lesson packet is the artifact students are handed. The unit **key** packet still lines up with
  the unit **student** packet, since it is built from the same cover and the same (equal-length)
  lesson packets; only the trailing sample test / sample test key can differ in length.
- The pass writes to `target/UNIT/LESSON/.paginate/`; on failure the recipe prints
  `paginate.log`.

## Unit assessments (tests)

Each unit carries summative assessments alongside its lessons, scaffolded automatically when the
unit is first created (skip with `--no-tests`, force a re-scaffold with `--tests`):

- **`unitXX/tests/`** — `practice_test/main.tex` (student study copy) and `actual_test/main.tex`
  (real test), plus `Makefile` = `include ../../shared/tests.mk`.
- **`unitXX/test_keys/`** — `practice_test_key/main.tex` and `actual_test_key/main.tex`, plus
  `Makefile` = `include ../../shared/test_keys.mk`.
- **`unitXX/sample_test/`**, **`unitXX/sample_test_key/`** — drop-in dirs that receive published
  PDFs (initially empty, with a `.gitkeep`).

`shared/tests.mk`/`shared/test_keys.mk` compile every `*/main.tex` subdir, then a `drop` target
**publishes the practice test/key** to `sample_test/main.pdf` and `sample_test_key/main.pdf`.
`shared/unit.mk` then merges `sample_test` into the unit **student** packet and `sample_test_key`
into the unit **key** packet (falling back to the blank sample test if no key was published). The
**actual** test/key are never merged.

```bash
make -C unitXX/tests all         # compile practice + actual tests, publish sample_test/main.pdf
make -C unitXX/test_keys all     # compile both keys, publish sample_test_key/main.pdf
make -C unitXX student key       # merges the published sample test / key into the unit packets
make -C unitXX/tests clean       # remove target/UNIT/tests
```

Build order matters: run `make -C unitXX/tests all` (and `test_keys all`) **before** the unit
packet, so the `sample_test` prefab exists when `unit.mk` merges it. Output lands in
`target/UNIT/tests/<name>/main.pdf` and `target/UNIT/test_keys/<name>/main.pdf`.

## Troubleshooting

`-file-line-error` makes errors report as `file:line: message`. Read the component's log at
`target/UNIT/LESSON/<comp>/main.log`. Common issues:

- **`File 'warmup/main' not found`** in the lesson plan → the plan embeds a thumbnail but the
  warm-up isn't built/present. Build `student` first, or (authored warm-ups) keep the spiral
  review text-only, or (prefab) ensure the PDF is present as `warmup/main.pdf` so the thumbnail
  (`\includegraphics{warmup/main}`) resolves.
- **`Undefined control sequence \CourseName`** → the course macros aren't defined. In this
  course they are **inlined in the lesson plan** (not in `shared/`); the scaffolder writes them,
  but a hand-edited plan may have dropped them. Re-add `\CourseName`/`\SchoolYear` to the preamble.
- **`\includegraphics` fails for a screenshot** → put images in `images/` (the plan sets
  `\graphicspath{{images/}}`) and load `graphicx` (the plan does; `-article` does not).
- **Key won't compile / option clash** → a key loads `-key` only; do **not** also load
  `-boxes` (it's pulled in). Mirror the blank, swapping that one package line.
- **Garbled glyphs or font errors** → the build is XeLaTeX-only (it uses `unicode-math` /
  `fontspec`-style features); don't compile with `pdflatex`. `latexmk -xelatex` is set in
  `lesson.mk`.
- **`pdfunite: command not found`** → install poppler-utils.
- **A new component didn't appear in the packet** → its directory has neither `main.tex` nor
  `main.pdf`, or its name isn't in `STUDENT_ORDER`/`KEY_ORDER`. Use the standard component names.

If a fix seems to require changing `shared/` or a Makefile, stop and raise it — that's a
project-level refactor, not a per-lesson change.
