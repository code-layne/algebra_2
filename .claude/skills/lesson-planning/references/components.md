# Components

The spec for authoring each file after scaffolding. The scaffolder (`scripts/new_lesson.py`)
gives you a correctly-preambled skeleton with TODO markers; this file says what fills them.
**Always also open a real built lesson (`unit01/lesson00` or `unit01/lesson01`) as the gold
reference** — these specs summarize the pattern, but the live project is authoritative. For macros
and boxes see `references/conventions.md`; for where content comes from,
`references/course-workflow.md`.

Contents: [Lesson plan](#lesson-plan) · [Cover](#cover) · [Warm-up](#warm-up) ·
[Guided Notes](#guided-notes) · [Group Activity](#group-activity) · [Homework](#homework) ·
[Slides](#slides) · [Unit tests](#unit-tests-summative-assessments) ·
[Answer-key discipline](#answer-key-discipline)

**The lesson model is gradual release** — I do, we do, you do together, you do alone. The student
packet is **cover → warm-up → guided notes → group activity → homework**, run as
**5 / 15 / 25 / 10 / 5** across the 60-minute period. The **debrief is the 10-minute phase between
the activity and the close; it has no component** — the class corrects its own activity pages
while the teacher puts the crux items on the board.

There is **no exit ticket**, there are **no tiers**, and there is no `experience` component.
(Lessons authored 2026-08-19 → 2026-08-31 have an `experience` pair — the EFFL centerpiece — and
lessons before that have `exit_ticket` and tiered activities. Both are legacy; regenerate rather
than patch. See SKILL.md "Converting a lesson that is on an older shape.")

General rules:
- **Every student component is 10pt**: `algebra2-article` + `algebra2-boxes`; keys with
  `algebra2-article` + `algebra2-key`.
- Keep the **key structurally identical** to its blank — it is the blank with answers filled in.
  **A component must come out the same number of pages on both sides.** Every worked solution goes
  in a `work` block authored identically in the two files (see "The work rule" in
  `references/conventions.md`); a `\writelines{n}` in the blank is answered with exactly `n`
  `\ansline{}`s in the key. Build both and compare page counts before you call a component done.
- Content is **standards-based and original**: source topic/sequencing from `COURSE_PLAN.md`
  and the standards the user supplies; never copy the `spec/` publisher reference (copyright).
- Every component runs the loop **read/interpret → justify** ("what does this feature mean
  here, and how do you know?"). Never ask students to *sketch/draw/construct* a graph from
  scratch — give a pre-drawn figure to read, a table to complete, or a computation task.
- **The vocabulary is named openly everywhere** — cover, notes, activity, homework, deck. The old
  EFFL spoiler rule is dead, because the notes now come *before* the activity.
- Use the project's boxes and fill-in macros rather than hand-rolling layout.

## Lesson plan

`main.tex` at the lesson root — teacher-facing, never handed to students. Canonical section
order:

1. **Title block** — `\CourseName` + `\UnitNumberName \LessonNumberName`. The course name is
   just `Algebra 2`: no teacher name, no school year.
2. **Primary Objective / Standards / Lesson model** — a `tcolorbox` (forestbg/forest): the
   objective in formal terms, the standards codes, and a one-paragraph statement of the
   gradual-release model.
3. **Priority Ideas & Skills** — `skillbox{goldbox}`, two `tabularx` cells. Left: the skills, as
   things the student does. Right: the *why*, including the lesson's target misconception stated
   explicitly.
4. **Vocabulary, Concepts & Theorems** — `skillbox{sky}`, a `tabularx` term/definition table
   (use `\TallMath{...}` for tall formulas). These are the terms the notes' `vocabbox` builds.
5. **Lesson at a Glance** — `fixedskillbox{forestbg}`: a Phase/Min/Students/Teacher table for
   the 60-minute period — Warm-Up 5 / Guided Notes 15 / Group Activity 25 / Debrief 10 /
   Close & Homework 5.
6. **Warm-Up — Activate Prior Knowledge & Spiral Review** — `fixedskillbox{forestbg}`: the ~3
   items, which prior skill each rehearses, and what to debrief aloud. Say explicitly how the
   debriefed observation hands off into notes section 1.
7. **Hook** — `skillbox{forestbg}`: the 60-second context, the questions to ask with their
   answers in parentheses, and the idea to land in one sentence. **The hook's numbers should be
   the ones every worked example in the notes reuses.**
8. **Guided Notes — the Lesson (15 min)** — `skillbox{forestbg}` in `multicols{2}`: one bold
   paragraph per numbered notes section saying what to build and where the `work` blocks are,
   ending with the guided-practice release ("do item 1 together, then circulate").
9. **Group Work (25 min, groups of 3–4)** — `skillbox{redbox}`: **"One common task, no tiers"**,
   the 2-minute launch script, then `multicols{2}`: **What students do** (the arc of parts 1–4,
   naming where the crux question sits) | **What the teacher does** (circulate; a bullet list of
   *questions, cues, and prompts — not answers* keyed to item numbers; which group work to pick
   for the board).
10. **Debrief (10 min — what goes on the board, in a second color)** — `skillbox{forestbg}`: a
    numbered list of **exactly four things to land**, each on displayed student work — the fully
    labelled part-1 answer, the crux, the part-3 comparison and the conclusion it licenses, and
    the part-4 concept check with what a wrong answer reveals. End by naming which item to cut if
    time is short and which two to protect.
11. **Active Monitoring — Watch For** — `skillbox{redbox}`: misconceptions to catch while
    circulating, keyed to activity and homework item numbers, plus cold-call prompts.
12. **Reinforcement & Extension** — `skillbox{goldbox}`: itemize the homework's ~6 problems and
    its extension; a **DeltaMath override** sentence saying whether this content is well covered
    there and what set to swap in if so; and a **Preview** of the next lesson.
13. **Teacher Notes** — **four** `teachernote`s, in packet order: `[Warm-Up]`, `[Guided Notes]`,
    `[Group Activity]`, `[Homework]`. Pacing splits that actually fill each phase's minutes,
    must-land moments, common slips, the early-finisher move, and how to sort the formative
    check. **This is the only place teacher prose goes** — never append one to a `_key`, which
    would make the key longer than its blank. See `references/conventions.md`.

Record the lesson's **standards** (the codes the user supplied) in the plan for the audit trail.

## Cover

`cover/main.tex` — student-facing front page of the packet. No key. Structure:
- Full-bleed forest banner (tikz) with `\LARGE` course name, unit, and `Lesson <id>  <title>`.
- `\namedateperiod` — **the only place in the lesson it appears.** See "Namestrip" below.
- `learningtargetbox` — an "I can…" list **using the lesson's formal vocabulary in bold**. There
  is nothing to withhold: the notes name the terms before the activity uses them.
- `tocbox` — a `tabularx` with **four rows in packet order** (Warm-Up, Guided Notes, Group
  Activity, Homework) + a Total row. **Every row is scored** — a `\blank{1.2cm}`, homework
  included; nothing prints `NA` any more. The homework row's description ends
  *"--- \emph{due next class}"*. The table is four columns (`c l X r`); **every row needs four
  cells** or the column widths collapse. There is no debrief row (it is a phase, not a component).
- `remindbox` (Keep in Mind) — a **content** summary: the lesson's key definitions and the
  distinction it turns on, in three or four sentences, in a form the student can revise from.

## Warm-up

`warmup/` (+ `warmup_key/`) — one page, ~3 quick items of **spiral review**, rehearsing exactly
the prior skills the lesson leans on. 10pt, no name row. The plan's Warm-Up box names what each
item rehearses, what to debrief aloud, and how that hands off into notes section 1. May also be a
**prefab PDF** (`warmup/main.pdf` + `warmup_key/main.pdf`) — `lesson.mk` merges it directly. Key
mirrors with `\ans`.

## Guided Notes

`notes/` (+ `notes_key/`) — the **"I do / we do"** block, **15 minutes, 2–3 pages at 10pt**. This
is where the vocabulary is built and named, *before* the group activity uses it. Structure, in
order:

1. **`objectivebox`** — "By the end of this lesson, I will be able to…", 3–4 bullets in formal
   terms.
2. **`vocabbox`** — 5–7 `\termblanklong{Term}` entries the class fills in as each is built. The
   `\par\vspace{2pt}` before the first one is **required** (`\termblanklong`'s `\noindent` is a
   no-op mid-paragraph). The key defines a `\vocabans{Term}{definition}` macro in its preamble and
   uses it in place of each `\termblanklong`.
3. **`hookbox`** — the 60-second motivating context with 3–4 quick fill-in questions. **Its
   numbers are the ones the worked examples below reuse.**
4. **Four numbered `notesbox` sections** — the lesson broken into four ideas, each with fill-in
   blanks and, where there is algebra, a `work` block. Keep **one worked context running through
   all four**; that is what makes the block read as one lesson rather than four procedures.
   - Section 1 establishes the defining idea and the general form.
   - Section 2 is usually the second procedure (a fill-in `tabularx` of feature / how to find it /
     what it means works well).
   - **Section 3 normally carries the target misconception**: put the two things students conflate
     side by side in a two-column `tabularx`, then close with a gold caution `tcolorbox`
     (`colback=goldbg, colframe=goldacc`) giving a case where the two answers *disagree*.
   - Section 4 is the edge cases — the special case, the value where the rule fails, and the
     story-vs-math distinction.
5. **`practicebox`** — the **"we do"**: one new example, all features at once, with a `work`
   block. Do item 1 together, then release the rest and circulate.

`\boxguard` on each `notesbox`: 20–26 at 10pt.

## Group Activity

`activity/` (+ `activity_key/`) — the **"you do together"** block, **25 minutes, groups of 3–4,
2–3 pages at 10pt**. **Untiered:** every group works the same task. ~15–18 lettered sub-questions
fills the block. Structure:

- **`headlinebox`** — the motivating context in two sentences, the vocabulary from the notes the
  groups are expected to use, and the standing rule: *for every answer, be ready to show me where
  you see it.*
- **Four `scenariobox` parts:**
  1. **The straightforward case** — the whole toolkit run once, on a pre-drawn figure.
  2. **The contrast case** — the same moves with one condition varied. One item here is the
     **crux**: the one that surfaces the lesson's target misconception.
  3. **Side by side** — what the two cases share and what differs, ending in a "write a sentence
     explaining why" item. This is what the debrief generalizes from.
  4. **Model It** — *always*. A fresh real context carrying the lesson's **modelling standard**:
     interpret the parameters → solve it in a `work` block → interpret the answer → one "what if
     we change a number?" item that tests the concept rather than the procedure.

Open responses use `\writelines{2}` (two lines is the norm); short fills use `\blank{}`. Every
graph is **pre-drawn** — students label, circle, and read, never sketch from scratch. Alternate
`{forest}` and `{navy}` scenariobox colors so the parts are visually distinct.

## Homework

`homework/` (+ `homework_key/`) — the **"you do alone"** block. **Every lesson generates one**
(user direction, 2026-08-31): DeltaMath does not cover all of this course's content, and where it
does the teacher **overrides** and assigns a DeltaMath set instead — so the plan's *Reinforcement
& Extension* box always names what could be swapped in. **This page IS scored**: the cover's score
cell is a `\blank{1.2cm}`, never `NA`.

**2 pages, and 2pp is a ceiling** — a seventh item gets cut, never spilled onto a third page.
Structure:

- **A `Practice` `notesbox`** with **~6 items spanning the lesson's whole standard**, not sampling
  it. The canonical spread:
  1. the **core procedure** read off a *rule*;
  2. a deliberate **contrast pair** (same task, opposite condition) — the target misconception —
     closing with a "why?" item;
  3. the same procedure read off a **table or a graph**, so all three representations appear;
  4. the **special case** and its boundary ("for which $k$ does this fail?");
  5. a **model** in a fresh context, with a `work` block and an interpret-the-answer follow-up;
  6. an **SOL-style multiple-choice item** — the **formative check**. The plan says how to sort
     responses into named categories to decide how the next lesson opens.
- **An `extensionbox`** — a construction that runs the lesson's procedure backwards, plus a
  reasoning item ("a classmate claims … explain why that cannot happen").
- **A closing `spiralbox`** — two sentences previewing the next lesson.

In the key, the multiple-choice item keeps all four options with the **correct one wrapped in
`\ans{...}`**, and the answer lines below say which is right and why one distractor is wrong.

## Namestrip — where the name/date/period row goes

**The name row appears exactly once per lesson: on the cover.** Do not put `\namedateperiod`
(or `\namepartnerperiod`) in `warmup`, `notes`, `activity`, or `homework` — or in any `_key`,
or in a legacy `experience`/`exit_ticket`. The components are stapled behind the cover, so a row on each one is redundant and
costs vertical space at the top of every page. Exempt: `cover/` (it's the one place it belongs)
and `unitXX/tests/` (taken in a testing setting, not behind a cover).

New lessons come out of the scaffolder already correct. To apply it to a lesson authored before
the convention:

```bash
python3 .claude/skills/lesson-planning/scripts/namestrip.py --project . --unit 02 --lesson 03
```

Add `--check` to report without changing anything (exits 1 if it finds any). The script skips
`cover/`, hits blanks and keys together, and is idempotent. Rebuild afterward and confirm every
component is still the same number of pages blank and keyed.

## Slides

`slides/` — the teacher Beamer deck. No key. Requires `shared/algebra2-beamer.sty`.

**Every lesson owes a deck.** It is not optional: it feeds two of the five work products —
`lessonYY_slides.pdf` and `lessonYY_slides.pptx` (the same deck rasterized one page per slide by
`shared/pdf2pptx.py`). Because the PPTX slides are page images, the `.tex` is the only source of
truth; nothing is editable downstream.
Preamble: `\documentclass[aspectratio=169,11pt]{beamer}` + `\usepackage{algebra2-beamer}`.
The title slide is hand-built (forest background canvas + minipage); content slides use
`\forestheader{Title}` and `\sectionlabel[color]{LABEL}`. Note `\CourseName` is **not** defined
in beamer — write the course name literally.

**The deck follows the gradual-release flow, ~11 frames:** title → learning targets (naming the
vocabulary, plus a "how today runs" block with the 5/15/25/10/5 split) → warm-up → hook → **four
notes frames**, one per numbered notes section, matching the packet exactly (section 3 gets a
`\begin{block}` with the case where the two answers disagree) → group-activity launch (the four
parts, plus the figure if there is one, ending on *"for every answer, be ready to show me where
you see it"*) → **debrief** (the same four numbered takeaways as the plan's debrief box) → close
(what changed today, a **Homework** block naming what the packet page covers and that it is due
next class, and a one-line preview). Reference implementation: `unit01/lesson00/slides`.

## Unit tests (summative assessments)

Unit-level, not per-lesson — scaffolded once per unit under `unitXX/tests/` and
`unitXX/test_keys/` (see SKILL "What a unit is" and `references/build.md`). Author **two blank
tests and their two keys**, all with `\pageheader{Unit X: <Title>}{...}` + `\namedateperiod`
(tests are **exempt from Namestrip** — they are taken in a testing setting, not stapled behind a
lesson cover, so they keep their name row):

- **`tests/practice_test/main.tex`** — the study copy students keep. Opens with a `remindbox`
  telling students it mirrors the real test in format and ideas but uses different numbers.
  Organize into `\parthead{Part …}` sections (vocabulary, multiple choice, short
  answer/computation, extended response) with `\vspace` work room. This test is **published as
  the unit's `sample_test`** and lands in the student packet.
- **`tests/actual_test/main.tex`** — the real test given at test time. Same format, parts, and
  difficulty as the practice test, **different numbers/contexts**; no "this is practice" box.
  It is **never** merged into a packet — it is distributed separately.
- **`test_keys/practice_test_key/main.tex`**, **`test_keys/actual_test_key/main.tex`** — the
  keys, each mirroring its blank test exactly (preamble swaps `-boxes` for `-key`), answers in
  `\ans{...}`, correct MC options tagged, extended-response scoring in a `teachernote`. The
  practice key is published as `sample_test_key` (unit key packet only).

Content is summative — draw across the whole unit's lessons and standards. Keep the practice and
actual versions parallel so the practice test is honest preparation. Build/publish with
`make -C unitXX/tests all` and `make -C unitXX/test_keys all`.

## Answer-key discipline

There is no key toggle — every key is a separate file under `<comp>_key/` (this applies to the
test keys too):
- Copy the blank component **verbatim**, then swap `\usepackage{algebra2-boxes}` for
  `\usepackage{algebra2-key}`.
- Replace each blank/write-line with `\ans{answer}` (inline) or `\ansline{answer}` (fills a
  write-line). Title becomes "<DocTitle> — Answer Key".
- For multiple choice, keep all four options and wrap the **correct one** in `\ans{...}`, then
  use the answer lines below the item to say which is right and why one distractor is wrong.
- `\ans` is text-mode: never put it inside `$...$` — wrap math fragments instead
  (`\ans{$\sqrt{n}$}`) — and never let it span a blank line.
- **No `teachernote` in a key.** Teacher-only guidance goes in the lesson plan, one note per
  component, titled `\begin{teachernote}[Guided Notes]` and so on. A note in a key is the one block
  with no counterpart in the blank, and it is what makes a key run a page long.
- **Worked solutions are not `\ans{}` material.** An inline `$a=b \Rightarrow c=d \Rightarrow e=f$`
  crammed into one cell violates the work rule and gives the student no room; use a `work` block,
  identical in both files. See `references/conventions.md`.
- Because the key matches the blank line-for-line, the two paginate identically — verify it:
  ```bash
  for c in warmup notes activity homework; do
    echo -n "$c: "; pdfinfo target/UNIT/LESSON/$c/main.pdf | grep -c . >/dev/null
    printf '%s vs %s\n' "$(pdfinfo target/UNIT/LESSON/$c/main.pdf | awk '/^Pages/{print $2}')" \
                        "$(pdfinfo target/UNIT/LESSON/${c}_key/main.pdf | awk '/^Pages/{print $2}')"
  done
  ```
