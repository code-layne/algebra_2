---
name: lesson-planning
description: >-
  Author complete, build-ready lessons for the Algebra 2 LaTeX curriculum (a project with a
  shared/ style package — prefix algebra2 — and a Makefile hierarchy that compiles components
  with latexmk and merges them with pdfunite).
  Use this whenever the user wants to create, draft, or build a lesson, a lesson plan, a unit,
  or any lesson component — warm-up, guided notes (with the guided and individual practice), homework, cover sheet,
  unit test, or their answer keys. Lessons follow a traditional gradual-release model
  (warm-up → guided notes → individual practice → debrief → homework; no group activity). The course is defined by
  COURSE_PLAN.md at the project root: seven function-family units, each opening with a Lesson 0
  "Characteristics of ____ Functions," with a cumulative characteristics-of-functions spine.
  Decompose units into lessons from it.
  Trigger this even when the user just says "make lesson 1.3" or "I need a warm-up and key for
  tomorrow," and even if they don't say "skill" or "LaTeX".
  Also use it to RETROFIT an already-authored lesson to a named convention — boxguard, namestrip,
  vocabpar, the work rule, teachernotes — as in "apply boxguard namestrip retrofit to 1.1 and
  1.3." See the Retrofit section.
---

# Lesson Planning — Algebra 2

This skill authors lessons for the **Algebra 2** course and produces print-ready PDFs
through the project's own build system. **It builds around the project's conventions — it does
not invent its own.** The course is a **function-family** course for a secondary-school
audience: each unit is built around one function type, and **every unit opens with a Lesson 0,
"Characteristics of ____ Functions."** Author every component to build graph-reading fluency —
study how each new function type *behaves* before manipulating and solving it.

**Every lesson follows a traditional gradual-release model** — *I do, we do, you do alone.* A
warm-up activates prior knowledge; **Guided Notes** build and name the vocabulary with the class
on one worked context and end in a **Guided Practice** box (the "we do"); an **Individual
Practice** block on the notes' last page is the "you do" — three problems, worked silently and
alone; a **debrief** consolidates and surfaces errors; the **homework** page is started in class
and finished at home. The 60-minute period runs
**5 warm-up / 20 guided notes (incl. guided practice) / 15 individual practice / 10 debrief /
10 close & start the homework**. **There is no group activity** — the user cut it on 2026-08-31
("just cut the group activity … add an 'individual practice'") and confirmed the shape as
course-wide on 2026-09-01. `unit01/lesson01` and `unit01/lesson02` are the reference
implementations; 1.3–1.5 follow them.

> **This replaced the Math Medic "experience first, formalize later" (EFFL) model on 2026-08-31
> — user direction, "the students have revolted."** Anything still saying *Experience &
> Formalize*, *QuickNotes*, *Check Your Understanding*, or *the spoiler rule* is a lesson that
> has not been converted yet, not a pattern to copy. See the ⚠ Status block at the top of
> `COURSE_PLAN.md`.

**Four decisions the user confirmed, and that hold for every lesson (2026-08-31 → 2026-09-01):**

1. **No exit ticket.** The debrief closes the lesson; the formative check is the homework's
   last item (an SOL-style multiple-choice problem). Never scaffold `exit_ticket` in a new or
   converted lesson.
2. **No tiers.** The old Tier R / Approaching / Extension structure does **not** come back.
3. **No group activity.** The "you do" is an **Individual Practice** block *inside the Guided
   Notes* — a `scenariobox[Individual Practice --- On Your Own]{navy}` on the notes' own last
   page, three problems, silent. Never scaffold `activity` in a new or regenerated lesson.
4. **Timing is 5 / 20 / 15 / 10 / 10** — warm-up / guided notes incl. guided practice /
   individual practice / debrief / close & *start the homework in class*. The warm-up is set at
   **12pt**; everything else stays 10pt.

## The course at a glance

- **Structure** comes from **`COURSE_PLAN.md`** (project root) — the scope & sequence: the seven
  units, each unit's lesson list, and the cumulative **characteristics-of-functions spine**
  (§3), where each Lesson 0 introduces the new characteristics its function type is the first to
  require (asymptotes in Unit 4, origin symmetry in Unit 3, and so on). **This is the
  unit/lesson map.** See `references/course-workflow.md`.
- **Content** is **standards-based and original**: sourced from `COURSE_PLAN.md`, the standards
  the user supplies (usually Virginia SOL codes), and — as a topic/difficulty **model only** —
  the copyrighted All Things Algebra reference in `spec/`. **Never copy** the reference's
  problems or wording; everything authored is original.
- **Out of scope** (no lessons): conic sections, sequences & series, probability & statistics,
  trigonometry, and linear systems / linear programming.
- **Style prefix is `algebra2`** — `shared/algebra2-{colors,article,boxes,key}.sty`, plus
  `shared/algebra2-beamer.sty` for the optional teacher `slides` deck. Course macros
  (`\CourseName`) are **inlined in each lesson plan**, not defined in `shared/`. The printed
  title is **just `Algebra 2`** — no teacher name, no school year, anywhere a title renders.

## What a lesson is

A lesson lives in `unitXX/lessonYY/` and consists of:

- **`main.tex`** — the teacher-facing **lesson plan** (the root document of the lesson dir).
- A set of **student components**, each its own subdirectory containing **either** a
  `main.tex` (authored, compiled to a PDF) **or** a `main.pdf` (a prefab PDF, used as-is):
  `cover`, `warmup`, `notes`, `homework`, and `slides`. **There is no `activity` directory.**
- An **answer key** for each keyed component, as a *separate* sibling directory:
  `warmup_key`, `notes_key`, `homework_key`. (`cover` and `slides` have no key.)
- **The debrief has no component.** It is a phase of the lesson plan — 10 minutes in which the
  class corrects its own Individual Practice in a second colour while the teacher works all
  three problems on the board.

The teaching components, and what each is for:

| Component | Phase | Budget | What it is |
| --- | --- | --- | --- |
| **`warmup`** | 5 min, **12pt** | **1p** | three spiral-review items; the last hands off into notes section 1 |
| **`notes`** | I do / we do 20 min, then you do alone 15 min | **4pp** | `objectivebox` → `vocabbox` → `hookbox` → **four numbered `notesbox` sections** → `practicebox` (the "we do") → **`scenariobox[Individual Practice --- On Your Own]{navy}`**, three problems, on its own clean page |
| **`homework`** | started in class, finished at home | **2pp** | a `Practice` `notesbox` of **~6 items spanning the whole standard** → `extensionbox` → closing `spiralbox` |

**Homework is an in-repo component and it IS scored.** Every lesson generates one, because
DeltaMath does not cover all of this course's content; where it does, the teacher **overrides per
lesson** and assigns a DeltaMath set instead, so each plan's *Reinforcement & Extension* box
carries a **DeltaMath override** sentence naming what to swap in. The cover's homework row takes a
`\blank{1.2cm}` — never `NA` — and reads *due next class*. See `references/components.md`.

*Legacy shapes.* Lesson 1.0 (converted 2026-08-31) still carries an `activity`/`activity_key`
pair and the interim 5/15/25/10/5 group-activity timing; lessons authored 2026-08-19 →
2026-08-31 in Units 2–7 carry an `experience`/`experience_key` pair (the EFFL centerpiece);
lessons authored before that carry `activity`, `exit_ticket`, and **tiered** activities. The
build accepts all of them. When touching a legacy lesson, **regenerate it in the current shape
rather than patching** — `git rm` the `activity{,_key}`, `experience{,_key}`, or
`exit_ticket{,_key}` dirs, and rebuild the plan and deck around the 5/20/15/10/10 table.
`unit01/lesson01` and `unit01/lesson02` are the reference implementations (1.3–1.5 follow them).

### The five work products

Every lesson builds **exactly five files** into `target/compiled/unitXX/`:

| File | What it is |
| --- | --- |
| `lessonYY_plan.pdf` | the lesson plan — the lesson-root `main.tex`, compiled |
| `lessonYY_slides.pdf` | the deck from `slides/main.tex`, **printed** — 3 slides per page with a ruled notes column beside each |
| `lessonYY_slides.pptx` | that same deck wrapped for PowerPoint, **full-page**, one page image per slide |
| `lessonYY_student.pdf` | cover + blank components, merged and paginated packet-wide |
| `lessonYY_key.pdf` | the same packet answered, **page for page** with the student one |

`shared/lesson.mk` discovers a component if it has a `main.tex` **or** a `main.pdf`, compiles the
`main.tex` ones with `latexmk -xelatex`, merges the packets with `pdfunite` in pedagogical order,
and renders the deck twice — 3-up for print via `shared/handout.tex`, full-page for PowerPoint via
`shared/pdf2pptx.py`. Both come from the one compiled deck, which stays the source of truth; never
edit a work product, edit `slides/main.tex` and rebuild. A prefab `main.pdf` is fed straight to `pdfunite`
from the source tree with no compile step (Step 4).

**There is no `full` packet.** It was removed — the plan and the deck are standalone deliverables
now, so never build, reference, or expect `lessonYY_full.pdf`. Because `slides` feeds two of the
five products, **every lesson owes a deck**; it is a default component, not an optional one.

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
  published PDFs. `shared/unit.mk` merges `sample_test` into the unit **student** packet and
  `sample_test_key` into the unit **key** packet. The **actual** test and its key are never
  merged into any packet — they stay out of student hands.
- Optionally **`unit_cover/`** — a unit title page merged at the front of the unit packet.

A unit aggregates **only the student and key packets** (`unitXX_{student,key}.pdf`); the plan,
the slide PDF, and the PPTX stay per-lesson.

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
   characteristics spine, per-unit lesson lists, and the running build **Status** — the ⚠ block
   at the top is the current pedagogy of record. It orients the whole session; you update its
   Status at the end (Step 6).
2. **Confirm the prefix.** `ls shared/*-colors.sty` → it is `algebra2`. All
   `\usepackage{algebra2-article}` etc. use it.
3. **Course macros are inlined in the lesson plan.** This course does **not** define
   `\CourseName` in `shared/`, so each lesson plan sets it itself (the scaffolder
   writes them — pass `--course` to set the name).
4. **Find the insertion point.** List `unit*/lesson*` to find the next unit/lesson number and
   whether the target lesson already exists.
5. **Open a model lesson.** `unit01/lesson01` and `unit01/lesson02` are the course-wide
   gradual-release reference implementations (1.3–1.5 follow them) — open one and mirror its
   preamble, box usage, and tone. The live project overrides the reference docs. (1.0 still has
   a group activity; Units 2–7 are on older shapes.)

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
python3 /Users/layneshepherd/Mathematics/algebra_2/.claude/worktrees/experience-formalize-lessons-3c941a/.claude/skills/lesson-planning/scripts/new_lesson.py --project . --unit 01 --lesson 03 \
  --title "Absolute Value Functions" --unit-title "Linear Functions" \
  --course "Algebra 2" \
  --components cover,warmup,notes,homework,slides
```

That component list is the default, so `--components` can be omitted entirely. The script
auto-detects the prefix and writes each authored component's `main.tex` as a correctly-preambled
skeleton (and the matching `_key` skeleton for keyed components) — the warm-up at 12pt, the
notes with the Individual Practice block already in place. Because this course inlines
course macros, pass `--course "Algebra 2"` so the generated lesson plan defines
`\CourseName` correctly. There is no `--year`: the school year is never printed. Pass `--prefab warmup` to create that component as an empty drop-in
directory instead (Step 4). `slides` requires `shared/algebra2-beamer.sty`. Then fill in the
skeletons — **including the deck**, which is no longer optional.

`experience` is **not scaffoldable** — it was the EFFL centerpiece. `activity` and `exit_ticket`
still are, but only so an older lesson can be rebuilt unchanged; never add either to a new or
regenerated lesson.

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

- **Every student component is `\documentclass[10pt]{article}`** with
  `\usepackage{algebra2-article}` + `\usepackage{algebra2-boxes}` — **except the warm-up, which
  is `[12pt]`** (user direction, 2026-08-31) and must still fit one page blank and keyed. There
  is no `\answerspace` macro — open responses use `\writelines{n}`.
- **Guided Notes carry the vocabulary, and they come first.** The spoiler rule is dead: the
  cover, the deck, and the notes all name the formal terms, because the notes precede the
  practice. Build the definitions on the hook's own numbers, and **keep one worked context
  running through all four sections** — that is what makes the block read as one lesson rather
  than four procedures.
- **Section 3 of the notes is normally the target misconception.** Put the two things students
  conflate side by side in a two-column `tabularx`, then close with a gold caution `tcolorbox`
  giving a case where the two answers *disagree*.
- **Individual Practice is three problems, silent, on the notes' last page.** Put a
  `\boxguard[22]` before the `scenariobox[Individual Practice --- On Your Own]{navy}` so it
  lands on a clean page. The three problems are deliberately the three *shapes* (or directions)
  of the skill — e.g. equation / "and" / "or"; rule → features / graph → rule / the same-vertex
  pair — with the crux last, and every solve in a `work` block. The lesson plan carries an
  `[Individual Practice]` box (launch script; what students do | what the teacher does — cues,
  never answers; the early-finisher move) and the debrief works all three on the board.
- **Homework spans the whole standard, in ~6 items:** the core procedure off a *rule*; a
  deliberate *contrast pair*; the same procedure off a *table or graph* (so all three
  representations appear); the *special case* and its boundary; a *model* in a fresh context with
  an interpret-the-answer follow-up; and an **SOL-style multiple-choice item as the formative
  check** (the plan says how to sort responses). Then an `extensionbox` and the closing
  `spiralbox` preview. **2pp is a ceiling** — a seventh item gets cut, not spilled onto a third page.
- **Never ask students to "sketch/draw/construct" a graph from scratch** — give a pre-drawn
  figure to read, a table to complete, or a computation task.
- **Answer keys** are *separate files* that swap `-boxes` for `\usepackage{algebra2-key}` and
  wrap every answer in `\ans{...}` (inline) or `\ansline{...}` (fills a write-line). Mirror the
  blank document exactly, then fill the blanks. **A `\writelines{n}` in the blank is answered
  with exactly `n` `\ansline{}`s in the key** — keep each under ~95 characters so it does not
  wrap onto an extra line. In a `vocabbox`, the blank's `\termblanklong{Term}` becomes the key's
  `\vocabans{Term}{definition}` (the key defines that macro in its own preamble). There is **no**
  answer-key toggle — never try to build one.
- **Teacher notes go in the lesson plan, not in a key** — **four** `teachernote`s per lesson, in
  packet order: `[Warm-Up]`, `[Guided Notes]`, `[Individual Practice]`, `[Homework]`.
  A note in a key is the one block with no counterpart in the blank, so it makes the key run
  longer and costs the student packet a blank page.
- **The work rule: a component must be the same number of pages blank and keyed.** Put every
  worked solution in a `work` block — one statement per line, `&` before the relation so the whole
  block aligns on it — authored **byte-identically in the blank and the key**. The blank reserves
  the block's exact height and prints nothing; the key prints it. Never cram steps into one line
  as `$a=b \Rightarrow c=d$`. Full spec in `references/conventions.md`; `unit01/lesson00` is the
  reference implementation.
- Use the project's box vocabulary (`skillbox`, `objectivebox`, `learningtargetbox`, `vocabbox`,
  `hookbox`, `notesbox`, `practicebox`, `scenariobox`, `extensionbox`, `spiralbox`, `tocbox`,
  etc.) and fill-in helpers (`\blank`, `\writeline`, `\writelines`, `\termblanklong`,
  `\namedateperiod`) rather than reinventing layout. The full catalog is in
  `references/conventions.md`. At 10pt, `\boxguard` counts run **16–26**.
- **Match the course pedagogy.** Build graph-reading and interpretation fluency; keep answers
  traceable to the lesson's standards.
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
make -C unit01/lesson03 all       # all five work products — the usual command
make -C unit01/lesson03 plan      # the lesson plan            → lessonYY_plan.pdf
make -C unit01/lesson03 slides    # the Beamer deck            → lessonYY_slides.pdf
make -C unit01/lesson03 pptx      # the deck, PowerPoint-ready → lessonYY_slides.pptx
make -C unit01/lesson03 student   # cover + blank components   → lessonYY_student.pdf
make -C unit01/lesson03 key       # same packet, answered      → lessonYY_key.pdf
```

`make -C unitXX student|key` merges a unit; `make student|key` at the root merges the whole
curriculum. **`full` no longer exists at any level** — `make full` errors out. Output lands in
`target/`. The build needs XeLaTeX, `latexmk`, `pdfunite`, `pdftoppm`, and `python3`; if a compile
fails, surface the `.log` and fix the offending `.tex` rather than editing the build system.
Details and troubleshooting in `references/build.md`.

**Then verify parity before calling the lesson done** — every component's page count must equal
its `_key`'s, and the two packets must match:

```bash
for c in warmup notes homework; do printf '%s %s/%s\n' "$c" \
  "$(pdfinfo target/unit01/lesson03/$c/main.pdf | awk '/^Pages/{print $2}')" \
  "$(pdfinfo target/unit01/lesson03/${c}_key/main.pdf | awk '/^Pages/{print $2}')"; done
```

### Step 6 — Update the course plan (always do this last)

**Before you finish, record progress in `COURSE_PLAN.md`.** Update the per-unit **Status** (which
lessons are scaffolded, which components are authored vs. still skeleton vs. built, any confirmed
lesson maps) and note the concrete next actions and any open questions for the user. Do this at
the end of **every** execution, even a partial one; keep it terse and current (overwrite stale
entries rather than appending a changelog). Since it lives in the repo, it travels with the
branch, so the Step 0 sync always brings the latest state forward.

## Converting a lesson that is on an older shape

Lesson 1.0 (group-activity shape) and Units 2–7 (EFFL or pre-EFFL legacy) are not converted.
**Regenerate, don't patch.** The content mapping:

| From the 2026-08-31 group-activity shape | From EFFL | From the pre-EFFL legacy shape | Becomes |
| --- | --- | --- | --- |
| `notes` sections 1–4 | QuickNotes box | `notes` (drop the tiers language) | the four numbered sections of **Guided Notes** |
| the activity's crux items, chosen three | Activity + Application, condensed to three | Tier A/E items, three of them | **Individual Practice** — three problems inside the notes |
| `homework` | Check Your Understanding | `homework` + `exit_ticket` | the **Homework** page + `extensionbox` + `spiralbox` |

Mechanically: `git rm -r` the `activity{,_key}`, `experience{,_key}`, or `exit_ticket{,_key}`
dirs, write `notes`/`homework` (+ keys) fresh, set the warm-up to 12pt, rewrite the cover's TOC to
the **three** scored rows, rebuild the plan around the 5/20/15/10/10 table with four teacher
notes, and rewrite the deck to targets → warm-up → hook → notes 1–4 → individual-practice launch
→ debrief → close (11 frames).

**Build gotcha when deleting a component:** a stale stamp under `.stamps/unitXX/lessonYY/` makes
`make` skip recompiling a *sibling* whose PDF was cleaned, and `pdfunite` then fails on a missing
file. Remove `.stamps/<unit>/<lesson>` alongside `target/<unit>/<lesson>`.

## Retrofit — apply a named convention to a lesson already authored

Conventions land after lessons are written, so an existing lesson can be behind on one. The user
invokes this by name:

> `/lesson-planning apply boxguard namestrip retrofit to 1.1 and 1.3`

Apply **only the conventions named** (all of them if none are named), to the lessons named, then
build and report. Each has a fix and, where it is mechanical, a script:

| Name | The rule | How to apply |
| --- | --- | --- |
| **boxguard** | No box stranded as a ~1in sliver across a page break | `\boxguard` (or `\boxguard[n]`) on its own line before the `\begin{...}` — blank **and** key |
| **namestrip** | Name/date/period row on the cover only | `python3 .claude/skills/lesson-planning/scripts/namestrip.py --project . --unit NN --lesson MM` (`--check` to preview) |
| **vocabpar** | `\par` around `\termblanklong`/`\vocabans` in a `vocabbox` | Hand fix per lesson; `unit01/lesson00/notes{,_key}` is the reference |
| **work rule** | A component is the same length blank and keyed | `work` blocks authored identically in both files; `steptable`/`\step` for printed solutions; `\writelines{n}` matched by exactly `n` `\ansline`s. Reference: `unit01/lesson00`; steptable has no in-tree example since the review-unit deletion (2026-08-20) — follow the spec in `references/conventions.md` |
| **teachernotes** | Teacher prose in the lesson plan, one titled note per component | `python3 .claude/skills/lesson-planning/scripts/movenotes.py unitNN/lessonMM` (`--check` to preview) |

Full spec for each: `references/conventions.md` and `COURSE_PLAN.md` §7.

**Always finish a retrofit with the evidence**, per lesson: `make -C unitXX/lessonYY all` exits 0,
and every component's page count equals its `_key`'s. Report any component that still differs and
why. Then Step 6.

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
- Mirror `unit01/lesson00` or `unit01/lesson01` for tone and preamble; the live project overrides
  these docs.
- Keep blank and key documents in lockstep — the key is the blank with answers filled in, and it
  must come out the **same number of pages**. Worked solutions live in shared `work` blocks (the
  work rule); a key that runs long costs the student packet blank padding.
- Function-family pedagogy: study a function type's behavior (Lesson 0) before manipulating it;
  build graph-reading fluency; no "sketch from scratch" questions.
- Gradual-release discipline: vocabulary named in the notes, the "you do" done alone inside the
  notes, **no tiers, no exit ticket, no group activity, no `experience` component**, and a
  homework page for every lesson that is started in class.
- Don't modify `shared/` or the Makefiles to make a lesson build; fix the lesson's `.tex`.
