---
name: lesson-planning
description: >-
  Author complete, build-ready lessons for the Algebra 2 LaTeX curriculum (a project with a
  shared/ style package — prefix algebra2 — and a Makefile hierarchy that compiles components
  with latexmk and merges them with pdfunite).
  Use this whenever the user wants to create, draft, or build a lesson, a lesson plan, a unit,
  or any lesson component — warm-up, guided notes, activity, exit ticket, homework, cover
  sheet, unit test, or their answer keys. The course is defined by COURSE_PLAN.md at the
  project root: eight function-family units, each opening with a Lesson 0 "Characteristics of
  ____ Functions," with a cumulative characteristics-of-functions spine. Decompose units into
  lessons from it. Trigger this even when the user just says "make lesson 2.3" or "I need a
  warm-up and key for tomorrow," and even if they don't say "skill" or "LaTeX."
---

# Lesson Planning — Algebra 2

This skill authors lessons for the **Algebra 2: Shepherd** course and produces print-ready PDFs
through the project's own build system. **It builds around the project's conventions — it does
not invent its own.** The course is a **function-family** course for a secondary-school
audience: after a foundations unit, each unit is built around one function type, and **every
unit opens with a Lesson 0, "Characteristics of ____ Functions."** Author every component to
build graph-reading fluency — study how each new function type *behaves* before manipulating and
solving it.

## The course at a glance

- **Structure** comes from **`COURSE_PLAN.md`** (project root) — the scope & sequence: the eight
  units, each unit's lesson list, and the cumulative **characteristics-of-functions spine**
  (§3), where each Lesson 0 introduces the new characteristics its function type is the first to
  require (asymptotes in Unit 5, origin symmetry in Unit 4, and so on). **This is the
  unit/lesson map.** See `references/course-workflow.md`.
- **Content** is **standards-based and original**: sourced from `COURSE_PLAN.md`, the standards
  the user supplies (usually Virginia SOL codes), and — as a topic/difficulty **model only** —
  the copyrighted All Things Algebra reference in `spec/`. **Never copy** the reference's
  problems or wording; everything authored is original.
- **Out of scope** (no lessons): conic sections, sequences & series, probability & statistics,
  trigonometry, and linear systems / linear programming.
- **Style prefix is `algebra2`** — `shared/algebra2-{colors,article,boxes,key}.sty`, plus
  `shared/algebra2-beamer.sty` for the optional teacher `slides` deck. Course macros
  (`\CourseName`, `\SchoolYear`) are **inlined in each lesson plan**, not defined in `shared/`.

## What a lesson is

A lesson lives in `unitXX/lessonYY/` and consists of:

- **`main.tex`** — the teacher-facing **lesson plan** (the root document of the lesson dir).
- A set of **student components**, each its own subdirectory containing **either** a
  `main.tex` (authored, compiled to a PDF) **or** a `main.pdf` (a prefab PDF, used as-is):
  `cover`, `warmup`, `notes`, `activity`, `exit_ticket`, `homework`, and optional `slides`.
- An **answer key** for each keyed component, as a *separate* sibling directory:
  `warmup_key`, `notes_key`, `activity_key`, `exit_ticket_key`, `homework_key`.
  (`cover` has no key.)

`shared/lesson.mk` discovers a component if it has a `main.tex` **or** a `main.pdf`, compiles
the `main.tex` ones with `latexmk -xelatex`, and merges all of them with `pdfunite` in
pedagogical order into `lessonYY_student.pdf` (cover + blank components), `lessonYY_key.pdf` (the
same packet with each blank swapped for its key, **paginated to match page for page**), and
`lessonYY_full.pdf` (cover + keyed versions, plus the lesson plan and slides). A prefab `main.pdf`
is fed straight to `pdfunite` from the source tree with no compile step (Step 4).

The characteristics lesson is **`lesson00`** (Lesson X.0); content lessons keep 1-based numbers.

## What a unit is

A unit (`unitXX/`) holds its lessons plus **unit-level summative assessments**, scaffolded
automatically when the unit is first created (Step 2):

- **`tests/`** — the blank tests, one subdir each: **`practice_test/`** (a study copy students
  keep) and **`actual_test/`** (the real test given in a testing setting). Its `Makefile`
  (`include ../../shared/tests.mk`) compiles both and its `drop` target publishes the *practice*
  test to `sample_test/main.pdf`.
- **`test_keys/`** — the matching answer keys: **`practice_test_key/`** and
  **`actual_test_key/`**; its `drop` publishes the *practice* key to `sample_test_key/main.pdf`.
- **`sample_test/`** and **`sample_test_key/`** — prefab drop-in dirs that receive those
  published PDFs. `shared/unit.mk` merges `sample_test` into **both** the unit student and full
  packets, and `sample_test_key` into the **full** packet only. The **actual** test and its key
  are never merged into any packet — they stay out of student hands.
- Optionally **`unit_cover/`** — a unit title page merged at the front of the unit packet.

## Workflow

Follow these steps in order. Read the referenced files as you reach each step rather than all
upfront.

### Step 0 — Sync with upstream, then detect project context (always do this first)

**Sync the worktree first — before reading or writing anything.** This skill runs in a git
worktree; start *every* invocation by pulling the latest upstream changes so you author against
the current shared styles, plan, and lesson map. Do this automatically:

```bash
git fetch origin
DEFAULT=$(git symbolic-ref --quiet --short refs/remotes/origin/HEAD 2>/dev/null | sed 's@^origin/@@')
git merge --no-edit "origin/${DEFAULT:-main}"
```

If the working tree is dirty or the merge reports conflicts, **stop and surface it to the
user** — never force, reset, or discard changes to make the sync succeed. Once the sync is
clean, detect project context:

1. **Read the course plan.** Open `COURSE_PLAN.md` (project root) for the scope & sequence, the
   characteristics spine, per-unit lesson lists, and the running build **Status**. It orients
   the whole session; you update its Status at the end (Step 6).
2. **Confirm the prefix.** `ls shared/*-colors.sty` → it is `algebra2`. All
   `\usepackage{algebra2-article}` etc. use it.
3. **Course macros are inlined in the lesson plan.** This course does **not** define
   `\CourseName`/`\SchoolYear` in `shared/`, so each lesson plan sets them itself (the scaffolder
   writes them — pass `--course` to set the name).
4. **Find the insertion point.** List `unit*/lesson*` to find the next unit/lesson number and
   whether the target lesson already exists.
5. **Open a model lesson.** Unit 1 is built — open one of its lessons and mirror its preamble,
   box usage, and tone. The live project overrides the reference docs.

### Step 1 — Map the unit into lessons, then gather the lesson's content

The content path is always `references/course-workflow.md`:

- **Decompose the unit into lessons** from `COURSE_PLAN.md`: one lesson per bullet in that
  unit's list, in order, with the characteristics lesson as **Lesson 0**. Present the proposed
  lesson map for the unit and **confirm it with the user before authoring** — lessons
  occasionally merge or split.
- **Gather the lesson's content**: the topic from `COURSE_PLAN.md`, the standards the user
  supplies for it, and (for a Lesson 0) the characteristics the §3 spine marks ● for this unit.
  Use `spec/` only as a difficulty/sequencing model — author everything original (copyright).

### Step 2 — Scaffold the lesson directory

Run the scaffold script. It creates the lesson directory, the one-line lesson `Makefile`, the
component subdirectories you request, **and (if missing) the unit `Makefile`** so the unit build
works:

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/new_lesson.py --project . --unit 02 --lesson 03 \
  --title "Absolute Value Functions" --unit-title "Linear Functions" \
  --course "Algebra 2: Shepherd" \
  --components cover,warmup,notes,activity,exit_ticket,homework
```

The script auto-detects the prefix and writes each authored component's `main.tex` as a
correctly-preambled skeleton (and the matching `_key` skeleton for keyed components). Because
this course inlines course macros, pass `--course` (and `--year` if it differs) so the generated
lesson plan defines `\CourseName` correctly. Pass `--prefab warmup` to create that component as
an empty drop-in directory instead (Step 4). Add `slides` to scaffold a Beamer deck (requires
`shared/algebra2-beamer.sty`). Then fill in the skeletons.

**Unit assessments scaffold automatically.** When the run creates a *new* unit, the scaffolder
also lays down that unit's `tests/`, `test_keys/`, `sample_test/`, and `sample_test_key/` dirs
(practice + actual test skeletons and their keys, plus thin-include Makefiles) — see "What a
unit is." It never clobbers authored tests on later lessons. Use `--no-tests` to skip them, or
`--tests` to (re)scaffold them for a unit that already exists (idempotent).

### Step 3 — Author the lesson plan and components

**Before writing any component, do a full `Read` on each scaffolded `main.tex` skeleton you are
about to replace.** Use the `Read` tool on the actual file — a `cat`/`bash` dump does **not**
register the file with the editor and the first write will fail ("file has not been read yet").
Read every skeleton you intend to author (each component and its `_key`) up front, then write
them. This is mandatory.

Author each file following `references/components.md`, which gives the required section structure
and a worked skeleton for every component and its key. Hold to these invariants:

- **Student components** preamble with `\documentclass[10pt]{article}` +
  `\usepackage{algebra2-article}` + `\usepackage{algebra2-boxes}`.
- **Answer keys** are *separate files* that swap `-boxes` for `\usepackage{algebra2-key}` and
  wrap every answer in `\ans{...}` (inline) or `\ansline{...}` (fills a write-line). Mirror the
  blank document exactly, then fill the blanks. There is **no** answer-key toggle — never try to
  build one.
- **Teacher notes go in the lesson plan, not in a key** — one `teachernote` per component, in
  packet order, titled for it: `\begin{teachernote}[Exit Ticket]` → "Teacher Note: Exit Ticket".
  A note in a key is the one block with no counterpart in the blank, so it makes the key run
  longer and costs the student packet a blank page.
- **The work rule: a component must be the same number of pages blank and keyed.** Put every
  worked solution in a `work` block — one statement per line, `&` before the relation so the whole
  block aligns on it — authored **byte-identically in the blank and the key**. The blank reserves
  the block's exact height and prints nothing; the key prints it. Never cram steps into one line
  as `$a=b \Rightarrow c=d$`. Full spec in `references/conventions.md`; `unit01/lesson02` is the
  reference implementation.
- Use the project's box vocabulary (`skillbox`, `objectivebox`, `learningtargetbox`, `vocabbox`,
  `hookbox`, `notesbox`, `practicebox`, `scenariobox`, `tocbox`, etc.) and fill-in helpers
  (`\blank`, `\writeline`, `\termblanklong`, `\namedateperiod`) rather than reinventing layout.
  The full catalog is in `references/conventions.md`.
- **Match the course pedagogy.** Build graph-reading and interpretation fluency; keep answers
  traceable to the lesson's standards. Never ask students to "sketch/draw/construct" a graph from
  scratch — give a pre-drawn figure to read, a table to complete, or a computation task.
- If the warm-up is a **prefab** PDF (`warmup/main.pdf` in the source tree), the lesson plan may
  embed its thumbnail via `\includegraphics[page=1]{warmup/main}`. **Authored** warm-ups compile
  to `target/` and have no source PDF to embed, so keep the spiral review text-only; the
  scaffolder picks the right form automatically.

### Step 4 — Handle prefab components

When the user supplies a ready-made PDF for a component, just drop it in — no wrapper needed:

1. Place the PDF as `<comp>/main.pdf` (e.g. `warmup/main.pdf`).
2. If the key is also a prefab PDF, place it as `<comp>_key/main.pdf`.

`shared/lesson.mk` discovers the component by its `main.pdf` and feeds it straight to `pdfunite`,
skipping compilation. Use `--prefab <comp>` when scaffolding to create the empty drop-in
directory.

### Step 5 — Build

Build from the lesson directory (or the unit/root for wider packets):

```bash
make -C unit02/lesson03 student   # cover + blank student components → lessonYY_student.pdf
make -C unit02/lesson03 key       # same packet, answered, page-for-page → lessonYY_key.pdf
make -C unit02/lesson03 full      # lesson plan + slides + keyed versions → lessonYY_full.pdf
make -C unit02/lesson03 all       # all three
```

`make -C unitXX student|key|full` merges a unit; `make student|key|full` at the root merges the whole
curriculum. Output lands in `target/`. The build needs XeLaTeX, `latexmk`, and `pdfunite`; if a
compile fails, surface the `.log` and fix the offending `.tex` rather than editing the build
system. Details and troubleshooting in `references/build.md`.

### Step 6 — Update the course plan (always do this last)

**Before you finish, record progress in `COURSE_PLAN.md`.** Update the per-unit **Status** (which
lessons are scaffolded, which components are authored vs. still skeleton vs. built, any confirmed
lesson maps) and note the concrete next actions and any open questions for the user. Do this at
the end of **every** execution, even a partial one; keep it terse and current (overwrite stale
entries rather than appending a changelog). Since it lives in the repo, it travels with the
branch, so the Step 0 sync always brings the latest state forward.

## Reference files

- `references/conventions.md` — the style packages, every box environment, the fill-in and
  answer-key macros, color palette, and per-document-type preambles. Read before authoring.
- `references/components.md` — section-by-section spec and a skeleton for the lesson plan, each
  component + key, and the unit tests.
- `references/course-workflow.md` — decomposing `COURSE_PLAN.md` into lessons, the characteristics
  spine, standards mapping, and the copyright rule on the `spec/` reference.
- `references/build.md` — the Makefile hierarchy, scaffolding, prefab PDFs, unit tests, build
  commands, and troubleshooting.

## Guardrails

- **Bookend every run with the course plan:** read `COURSE_PLAN.md` at the start (Step 0) and
  update its Status + next-steps at the end (Step 6). Never skip the end-of-run update.
- **Full `Read` each skeleton before writing it** (Step 3). A `bash`/`cat` dump does not register
  the file with the editor, so the write fails; always use the `Read` tool first.
- Structure comes from `COURSE_PLAN.md`; content is standards-based and **original** — the `spec/`
  All Things Algebra materials are copyrighted, used only as a topic/difficulty model.
- Mirror a built Unit 1 lesson for tone and preamble; the live project overrides these docs.
- Keep blank and key documents in lockstep — the key is the blank with answers filled in, and it
  must come out the **same number of pages**. Worked solutions live in shared `work` blocks (the
  work rule); a key that runs long costs the student packet blank padding.
- Function-family pedagogy: study a function type's behavior (Lesson 0) before manipulating it;
  build graph-reading fluency; no "sketch from scratch" questions.
- Don't modify `shared/` or the Makefiles to make a lesson build; fix the lesson's `.tex`.
