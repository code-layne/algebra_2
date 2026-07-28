# Build System

The project compiles with **XeLaTeX** (via `latexmk`) and merges PDFs with **`pdfunite`**
(poppler). The skill authors `.tex`; the project's own Makefiles do the building. **Never edit
`shared/` or the Makefiles to make a lesson build — fix the lesson's `.tex` instead.**

## The three-level Make hierarchy

Each level below the root is a thin `Makefile` that includes a `shared/*.mk`. The scaffolder
creates them as needed (see "Scaffolding a lesson"), so you rarely write them by hand:

- **Root `Makefile`** — discovers `unit*/Makefile`, delegates, and merges unit PDFs into
  `target/compiled/curriculum_{student,full}.pdf`. (Already present in this repo.)
- **`unitXX/Makefile`** (`include ../shared/unit.mk`) — discovers `lesson*/Makefile`,
  delegates, and merges lesson PDFs into `target/compiled/unitXX_{student,full}.pdf`. It also
  merges the unit's `unit_cover`, `sample_test`, and `sample_test_key` (see "Unit assessments").
- **`lessonYY/Makefile`** (`include ../../shared/lesson.mk`) — the engine. It:
  - **Discovers a component if it has `main.tex` or `main.pdf`.** Authored components
    (`main.tex`) are compiled; prefab components (`main.pdf`) are used as-is from the source
    tree. A directory with neither is skipped.
  - Compiles each `<comp>/main.tex` with
    `latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error`,
    sending output to `target/UNIT/LESSON/<comp>/` and a stamp to `.stamps/`.
  - Builds two merged packets:
    - **student** = `cover warmup notes activity exit_ticket homework` (blank versions present),
      in that pedagogical order → `lessonYY_student.pdf`.
    - **full** = the lesson plan (`main.tex`) + `slides` + `cover` + the **`_key`** version of
      each keyed component (falling back to the blank if no key) → `lessonYY_full.pdf`. The
      `slides` component is built only when present and requires `shared/algebra2-beamer.sty`.

## Commands

```bash
make -C unitXX/lessonYY student   # student packet for one lesson
make -C unitXX/lessonYY full      # teacher/full packet (plan + slides + cover + keys)
make -C unitXX/lessonYY all       # both (runs student then full)
make -C unitXX/lessonYY clean     # remove this lesson's target/ and stamps

make -C unitXX student|full       # merge a whole unit
make student|full                 # merge the whole curriculum (from project root)
make clean | distclean            # clean everything (distclean also removes target/ and .stamps)
```

Outputs land in `target/`: per-component PDFs under `target/UNIT/LESSON/<comp>/main.pdf`,
merged packets under `target/compiled/`.

**Always build with `make all` (or `student` before `full`)** when the lesson plan embeds a
warm-up thumbnail: the thumbnail uses the warm-up, and `full` alone (from a clean tree) builds
only the `_key` versions. Authored warm-ups are text-only in the plan (no thumbnail); prefab
warm-ups embed `warmup/main` (the PDF in the source tree), which resolves regardless of order.

## Scaffolding a lesson

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/new_lesson.py --project . --unit 02 --lesson 03 \
  --title "..." --unit-title "..." \
  --components cover,warmup,notes,activity,exit_ticket,homework[,slides] \
  [--prefab warmup,warmup_key] [--course "Algebra 2: Shepherd"] [--lesson-id 2.3]
```

It detects the prefix (`algebra2`) from `shared/*-colors.sty`, and detects whether `\CourseName`
is defined in `shared/` — it is **not** in this course, so the generated lesson plan inlines the
course macros (pass `--course`/`--year` to set them; they default to "Algebra 2: Shepherd" /
2026–2027 if detected). It writes the lesson `Makefile`, the lesson plan, and each authored
component + key skeleton — **and creates the unit `Makefile` (and the root `Makefile` if it were
missing)** so unit/curriculum builds work, never clobbering existing ones. Pass `--prefab <dirs>`
to create empty drop-in directories instead (where you place each `main.pdf`). Add `slides` to
build a Beamer deck; the scaffolder requires `shared/algebra2-beamer.sty` and errors if it is
missing. Then author the skeletons (`references/components.md`).

## Prefab PDFs

To include a ready-made PDF as a component, drop it in as `<comp>/main.pdf` (and
`<comp>_key/main.pdf` for a prefab key). `lesson.mk` discovers it and feeds it straight to
`pdfunite` — no `main.tex`, no compile step. `make clean` removes only `target/` and stamps, so
your source PDFs are never deleted.

## Packet pagination and imposition (student packets)

Each component is its own document, so each numbers its pages from 1 and a naively merged packet
reads `1 / 1 / 1 2 3 4 5 / …`. After `pdfunite` builds the **student** packet, `shared/lesson.mk`
therefore runs one extra XeLaTeX pass over the merged PDF (`shared/paginate.tex`, invoked through
the `paginate` define) that:

- **numbers the packet end to end** — every page is re-placed at its original size and the
  packet-wide number is stamped in the article class's own footer position, masking the
  component-local one with a white band inside the bottom margin; and
- **starts every component on an odd page** — the recipe reads each component's page count with
  `pdfinfo`, builds a pdfpages page list with `{}` (empty page) after any odd-length component,
  and passes it in as `\PacketPages`. Inserted blanks are numbered like any other page.

This is automatic for every lesson — **no `.tex` change and no per-lesson sweep**. Notes:

- The last component is padded too, so every lesson packet has an **even** page count. Student
  packets are **duplex** documents — that is what the imposition is for.
- It assumes letter-size pages and the `algebra2-article` bottom margin. A prefab drop-in of a
  different page size would get its number misplaced; re-measure and adjust `\PgBaseline` if the
  shared geometry ever changes.
- **`full` packets are neither paginated nor imposed** — they mix letter pages with 16:9 Beamer
  slides, so one letter-paper stamping pass cannot number both. Teacher packets keep
  per-component numbering.
- **Unit packets are deliberately out of scope**: they inherit even lesson packets, but `unit.mk`
  neither numbers them nor pads `unit_cover` (1pp), so the first lesson opens on a verso. The
  lesson packet is the artifact students are handed.
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
`shared/unit.mk` then merges `sample_test` into the unit **student and full** packets and
`sample_test_key` into the **full** packet only. The **actual** test/key are never merged.

```bash
make -C unitXX/tests all         # compile practice + actual tests, publish sample_test/main.pdf
make -C unitXX/test_keys all     # compile both keys, publish sample_test_key/main.pdf
make -C unitXX full              # merges the published sample test + key into the unit packet
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
