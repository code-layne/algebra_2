---
name: lesson-planning
description: >-
  Author complete, build-ready lessons for the Algebra 2 LaTeX curriculum (a project with a
  shared/ style package — prefix algebra2 — and a Makefile hierarchy that compiles components
  with latexmk and merges them with pdfunite).
  Use this whenever the user wants to create, draft, or build a lesson, a lesson plan, a unit,
  or any lesson component — warm-up, experience (activity + QuickNotes + practice), homework,
  cover sheet, unit test, or their answer keys. Lessons follow the Math Medic
  "experience first, formalize later" (EFFL) model. The course is defined by COURSE_PLAN.md at the
  project root: seven function-family units, each opening with a Lesson 0 "Characteristics of
  ____ Functions," with a cumulative characteristics-of-functions spine. Decompose units into
  lessons from it. Trigger this even when the user just says "make lesson 1.3" or "I need a
  warm-up and key for tomorrow," and even if they don't say "skill" or "LaTeX."
  Also use it to RETROFIT an already-authored lesson to a named convention — boxguard,
  namestrip, vocabpar, the work rule, teachernotes — as in "apply boxguard namestrip retrofit
  to 1.1 and 1.3." See the Retrofit section.
---

# Lesson Planning — Algebra 2

This skill authors lessons for the **Algebra 2: Shepherd** course and produces print-ready PDFs
through the project's own build system. **It builds around the project's conventions — it does
not invent its own.** The course is a **function-family** course for a secondary-school
audience: each unit is built around one function type, and **every unit opens with a Lesson 0,
"Characteristics of ____ Functions."** Author every component to build graph-reading fluency —
study how each new function type *behaves* before manipulating and solving it.

**Every lesson follows the Math Medic "experience first, formalize later" (EFFL) model**
(mathmedic.com/how-it-works): students work an activity in small groups using only prior
knowledge; the teacher circulates with *questions, cues, and prompts — not answers*; a debrief
attaches the formal vocabulary to what the groups already found (QuickNotes); then a practice
set applies it to new contexts. There is **no separate direct-instruction block, no guided-notes
component, no exit ticket, and no tiered instruction.** The 60-minute period runs
5 warm-up / 20 activity / 13 debrief / 7 application / 10 check-your-understanding / 5 close.

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
  (`\CourseName`, `\SchoolYear`) are **inlined in each lesson plan**, not defined in `shared/`.

## What a lesson is

A lesson lives in `unitXX/lessonYY/` and consists of:

- **`main.tex`** — the teacher-facing **lesson plan** (the root document of the lesson dir).
- A set of **student components**, each its own subdirectory containing **either** a
  `main.tex` (authored, compiled to a PDF) **or** a `main.pdf` (a prefab PDF, used as-is):
  `cover`, `warmup`, **`experience`**, `homework`, and `slides`.
- An **answer key** for each keyed component, as a *separate* sibling directory:
  `warmup_key`, `experience_key`, `homework_key`. (`cover` and `slides` have no key.)
- **`experience` is the heart of the lesson** — one document in **four** parts on a page budget:
  the group **Activity** (two scenarios worked from prior knowledge, **≤2pp**), a **QuickNotes**
  box the debrief fills (**½pp**), an **Application** worked together (**½–1pp**), and
  **Check Your Understanding** (**1–2pp**, practice — **not scored**). See
  `references/components.md`.
- *Legacy shape:* lessons authored before the 2026-08 EFFL redesign still carry `notes`,
  `activity`, and `exit_ticket` dirs; the build accepts both. When touching a legacy lesson,
  ask whether to regenerate it in the EFFL shape rather than patching the old components.

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
python3 ${CLAUDE_SKILL_DIR}/scripts/new_lesson.py --project . --unit 01 --lesson 03 \
  --title "Absolute Value Functions" --unit-title "Linear Functions" \
  --course "Algebra 2: Shepherd" \
  --components cover,warmup,experience,homework,slides
```

That component list is the default, so `--components` can be omitted entirely. The script
auto-detects the prefix and writes each authored component's `main.tex` as a correctly-preambled
skeleton (and the matching `_key` skeleton for keyed components). Because this course inlines
course macros, pass `--course` (and `--year` if it differs) so the generated lesson plan defines
`\CourseName` correctly. Pass `--prefab warmup` to create that component as an empty drop-in
directory instead (Step 4). `slides` requires `shared/algebra2-beamer.sty`. Then fill in the
skeletons — **including the deck**, which is no longer optional.

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

- **Student components** preamble with `\usepackage{algebra2-article}` +
  `\usepackage{algebra2-boxes}`. The **experience** uses `\documentclass[12pt]{article}` (Math
  Medic sizing); warm-up, homework, and cover stay `[10pt]`.
- **EFFL scope (the timebox rule).** The activity must fit the 20-minute block: **two
  scenarios, ~10–13 sub-questions, ~2 pages at 12pt**, worked from prior knowledge with every
  graph pre-drawn. Extra examples (the special case, the compare-two-graphs) belong to the
  debrief, the Application, or the homework — not the activity. Homework is 5–10 problems.
- **The experience page budget (non-negotiable).** Activity **≤2pp** · QuickNotes **½pp** ·
  Application **½–1pp** · Check Your Understanding **1–2pp**. A part that runs over gets cut, not
  carried. Prefer a *full* single CYU page over a second page that is 10% used.
- **Check Your Understanding is not scored.** It is practice: the cover's score column prints
  **`\textbf{NA}`** for it rather than a `\blank{}`, the plan tells the teacher to spot-check the
  formative item instead of collecting for a grade, and the deck says "practice, not a quiz."
- **The spoiler rule.** Nothing the student sees *before* the activity — the cover and the
  deck's learning-targets frame — may pre-name the vocabulary the debrief will attach. Write
  targets in plain language ("where it starts, where it hits zero, how fast it changes"), and
  keep the cover's Keep-in-Mind box to describing the EFFL process itself. The teacher-facing
  plan keeps the formal objective.
- **Open answer space, not write-lines, in the experience.** The component preamble defines
  `\answerspace{H}{answer}` (a fixed-height minipage, `\nopagebreak`-glued to its prompt):
  the blank passes an empty second argument, the key passes the red answer, so the two files
  paginate identically by construction. Size H for 2–4 handwritten lines (1.4–2.8cm). Short
  inline `\blank{}`s are still fine for table cells and one-word fills; keep key `\ans{}`
  texts short enough not to wrap wider than the blank they replace.
- **Answer keys** are *separate files* that swap `-boxes` for `\usepackage{algebra2-key}` and
  wrap every answer in `\ans{...}` (inline) or `\ansline{...}` (fills a write-line). Mirror the
  blank document exactly, then fill the blanks. There is **no** answer-key toggle — never try to
  build one.
- **Teacher notes go in the lesson plan, not in a key** — one `teachernote` per component, in
  packet order, titled for it: `\begin{teachernote}[Experience]` → "Teacher Note: Experience".
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
  The full catalog is in `references/conventions.md`. **`\boxguard` counts are baseline-relative:
  values tuned at 10pt are ~40% oversized at 12pt** — in the experience use ~14–16, not 24–30.
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

### Step 6 — Update the course plan (always do this last)

**Before you finish, record progress in `COURSE_PLAN.md`.** Update the per-unit **Status** (which
lessons are scaffolded, which components are authored vs. still skeleton vs. built, any confirmed
lesson maps) and note the concrete next actions and any open questions for the user. Do this at
the end of **every** execution, even a partial one; keep it terse and current (overwrite stale
entries rather than appending a changelog). Since it lives in the repo, it travels with the
branch, so the Step 0 sync always brings the latest state forward.

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
| **vocabpar** | `\par` around `\termblanklong`/`\ansline` in a `vocabbox` | Hand fix per lesson; `unit04/lesson00` is the reference |
| **work rule** | A component is the same length blank and keyed | `work` blocks authored identically in both files; `steptable`/`\step` for printed solutions; `\writelines{n}` to match a wrapped `\ansline`. References: `unit01/lesson02` (work); steptable has no in-tree example since the review-unit deletion (2026-08-20) — follow the spec in `references/conventions.md` |
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
- Mirror a built Unit 1 lesson for tone and preamble; the live project overrides these docs.
- Keep blank and key documents in lockstep — the key is the blank with answers filled in, and it
  must come out the **same number of pages**. Worked solutions live in shared `work` blocks (the
  work rule); a key that runs long costs the student packet blank padding.
- Function-family pedagogy: study a function type's behavior (Lesson 0) before manipulating it;
  build graph-reading fluency; no "sketch from scratch" questions.
- EFFL discipline: the activity fits 20 minutes (two scenarios, ~10–13 sub-questions, ~2pp at
  12pt); vocabulary arrives in the debrief, never before it (spoiler rule); no tiers, no
  guided-notes or exit-ticket components in new lessons.
- Don't modify `shared/` or the Makefiles to make a lesson build; fix the lesson's `.tex`.
