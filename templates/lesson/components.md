# Components

The spec for authoring each file after scaffolding. The scaffolder (`~/.claude/skills/lesson-planning/scripts/new_lesson.py`)
gives you a correctly-preambled skeleton with TODO markers; this file says what fills them.
**Always also open the course's reference lesson, `unit01/lesson04`, as the gold
reference** — these specs summarize the pattern, but the live project is authoritative. For macros
and boxes see the shared skill's `references/conventions.md` (`~/.claude/skills/lesson-planning/`); for where content comes from,
`templates/lesson/course-workflow.md`.

Contents: [Lesson plan](#lesson-plan) · [Cover](#cover) · [Slides](#slides) ·
[Homework](#homework) · [Retired components](#retired-components) ·
[Unit tests](#unit-tests-summative-assessments) · [Answer-key discipline](#answer-key-discipline)

**The lesson model is slides first** (user direction, 2026-09-25). The deck *is* the lesson and
its printed handout (`lessonYY_slides.pdf`, three slides a page with a ruled notes column) is the
student's notes: a warm-up frame, then three or four cycles of **definition → worked example →
Now you try**, a wrap-up, and the homework started in class — **5 / 40 / 5 / 10** across the
60-minute period. The student packet is **cover → homework** (the homework only when it is
generated or a printed DeltaMath drop-in); the handout prints beside it. **Ask the user for each
lesson's homework source before scaffolding** — `LESSON_SHAPE.md` §2.

There is **no warm-up page, no Guided Notes, no group activity, no exit ticket, no tiers**, no
`experience` component, no `extensionbox`. Do not re-add any of them. Lessons still carrying them
are legacy — **regenerate rather than patch**, and ask first. See `LESSON_SHAPE.md` §7.

General rules:
- **Every student component is 12pt** (user direction, 2026-09-07 — cover and homework): `algebra2-article` + `algebra2-boxes`; keys with `algebra2-article` +
  `algebra2-key`. The lesson plan is 10pt and the deck 11pt.
- Keep the **key structurally identical** to its blank — it is the blank with answers filled in.
  **A component must come out the same number of pages on both sides.** Every worked solution goes
  in a `work` block authored identically in the two files (see "The work rule" in
  the shared skill's `references/conventions.md` (`~/.claude/skills/lesson-planning/`)); a `\writelines{n}` in the blank is answered with exactly `n`
  `\ansline{}`s in the key. Build both and compare page counts before you call a component done.
- Content is **standards-based and original**: source topic/sequencing from `COURSE_PLAN.md`
  and the standards the user supplies; never copy the `spec/` publisher reference (copyright).
- Every component runs the loop **read/interpret → justify** ("what does this feature mean
  here, and how do you know?"). Never ask students to *sketch/draw/construct* a graph from
  scratch — give a pre-drawn figure to read, a table to complete, or a computation task.
- **The vocabulary is named openly everywhere** — cover, deck, homework. Each term gets its own
  definition frame before any Now you try uses it.
- Use the project's boxes and fill-in macros rather than hand-rolling layout.

## Lesson plan

`main.tex` at the lesson root — teacher-facing, never handed to students. Canonical section
order (`LESSON_SHAPE.md` §5 wins over this summary):

1. **Title block** — `\CourseName` + `\UnitNumberName \LessonNumberName`. The course name is
   just `Algebra 2`: no teacher name, no school year.
2. **Primary Objective / Standards / Lesson model** — a `tcolorbox` (forestbg/forest): the
   objective in formal terms, the standards codes, the slides-first statement, and the lesson's
   **Homework source** (generated / DeltaMath online, *set name* / DeltaMath printed).
3. **Priority Ideas & Skills** — `skillbox{goldbox}`, two `tabularx` cells. Left: the skills, as
   things the student does. Right: the *why*, including the lesson's target misconception stated
   explicitly.
4. **Vocabulary, Concepts & Theorems** — `skillbox{sky}`, a term/definition table worded exactly
   as the deck's definition frames print them (`\TallMath{...}` for tall formulas).
5. **Lesson at a Glance** — `fixedskillbox{forestbg}`: Phase/Min/Students/Teacher — Warm-Up
   **5** / Lesson **40** / Wrap-up **5** / Homework **10**. Add the minutes up before you write
   them.
6. **Warm-Up (5 min, on the slides)** — the items, what each rehearses, and how the last one
   hands off into the first definition.
7. **The Lesson — definition, example, now you try (40 min)** — `skillbox{forestbg}` in
   `multicols{2}`, one paragraph per cycle in deck order: what to point at on the definition's
   display; the worked example and where students go wrong; the Now-you-try problem **with its
   answer**, and how long to let them work before the reveal. Name the crux cycle.
8. **Wrap-up (5 min)** — the definitions read back and the caution said aloud.
9. **Homework — scored, started in class, due the first class after two study halls** —
   `skillbox{goldbox}`: the source; the items and what each is for (or the DeltaMath set and what
   it covers); how to sort the formative check; a **Preview** of the next lesson.
10. **Watch For** — `skillbox{redbox}`: misconceptions to catch, keyed to Now-you-try and homework
    item numbers, plus cold-call prompts.
11. **Teacher Notes** — **two** `teachernote`s: `[Slides]`, `[Homework]`. Pacing that fills each
    phase's minutes, the must-land Now you try, what to cut if behind, how to sort the formative
    check. **This is the only place teacher prose goes** — never in a `_key`.

Record the lesson's **standards** (the codes the user supplied) in the plan for the audit trail.

## Cover

`cover/main.tex` — student-facing front page of the packet. No key. Structure:
- `\coverbanner{Unit N \quad Unit Title}{Lesson N.M \quad Lesson Title}` — it measures the title
  block and sizes the forest band to it.
- `\namedateperiod` — **the only place in the lesson it appears.** See "Namestrip" below.
- `learningtargetbox` — an "I can…" list **using the lesson's formal vocabulary in bold**.
- `tocbox` — a `tabularx` with **two scored rows** + a Total row: **1 Slide Notes** (the printed
  handout, worked in the notes column) and **2 Homework**, worded for the lesson's source —
  generated: what it covers; DeltaMath online: *DeltaMath: **set name** — online, not in this
  packet*; DeltaMath printed: *Homework (DeltaMath)* and what it covers. Every row ends in a
  `\blank{1.2cm}`, never `NA`; the homework row ends **"--- scored; due the first class after two
  study halls"**. Four columns (`c l X r`); **every row needs four cells** or the widths collapse.
- `remindbox` (Keep in Mind) — a **content** summary: the lesson's key definitions and the
  distinction it turns on, in three or four sentences — the same content as the deck's wrap-up.

## Retired components

**Warm-up page, Guided Notes & Practice, Individual Practice** — retired 2026-09-25 by the
slides-first shape (the warm-up and the notes moved onto the deck; Individual Practice was
already retired 2026-09-07). Their specs are in git history
(`git log -- templates/lesson/components.md`) for reading a legacy lesson; never author one. The
skeletons `warmup.tex`, `notes.tex`, `activity.tex` remain only so a legacy lesson can be rebuilt.

## Homework

`homework/` (+ `homework_key/`) — the lesson's individual practice, **scored**, started in class
in the last ten minutes, alone, and finished at home. **Its source is asked for every lesson**
(`LESSON_SHAPE.md` §2): **generated** — author it to this spec; **DeltaMath online** — no
`homework/` directory at all (`--components cover,slides`); **DeltaMath printed** — prefab
`homework/main.pdf` (+ `homework_key/main.pdf`) supplied by the user
(`--prefab homework,homework_key`). The rest of this section is the generated spec. Its contexts
differ from the deck's examples and Now you trys.

**2 pages, and 2pp is a ceiling** — a seventh item gets cut, never spilled onto a third page.
Structure:

- **An opening `remindbox`** — *"This is your graded homework. Your packet with completed homework
  is due the first class after two study halls. I will announce the due date in class and on
  TurtleNet."* plus the lesson's one-sentence rule, **identical in blank and key**.
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
- **A closing `spiralbox`** — two sentences previewing the next lesson.

Split the items `notesbox{Practice}` / `notesbox{Practice, continued}` with a `\newpage` between
them so **no item breaks across a page**. There is **no `extensionbox`** — it was retired with this
shape (the environment still exists in `algebra2-boxes.sty`; never author one).

In the key, the multiple-choice item keeps all four options with the **correct one wrapped in
`\ans{...}`**, and the answer lines below say which is right and why one distractor is wrong.

## Namestrip — where the name/date/period row goes

**The name row appears exactly once per lesson: on the cover.** Do not put `\namedateperiod`
(or `\namepartnerperiod`) in `homework` or any `_key`, or in a legacy
`warmup`/`notes`/`experience`/`exit_ticket`. The components are stapled behind the cover, so a row on each one is redundant and
costs vertical space at the top of every page. Exempt: `cover/` (it's the one place it belongs)
and `unitXX/tests/` (taken in a testing setting, not behind a cover).

New lessons come out of the scaffolder already correct. To apply it to a lesson authored before
the convention:

```bash
python3 ~/.claude/skills/lesson-planning/scripts/namestrip.py --project . --unit 02 --lesson 03
```

Add `--check` to report without changing anything (exits 1 if it finds any). The script skips
`cover/`, hits blanks and keys together, and is idempotent. Rebuild afterward and confirm every
component is still the same number of pages blank and keyed.

## Slides

`slides/` — **the lesson itself.** No key. Requires `shared/algebra2-beamer.sty`. Start from
`templates/lesson/slides.tex`.

**Every lesson owes a deck.** It feeds two of the five work products: `lessonYY_slides.pdf` (the
printed handout — the student's notes) and `lessonYY_slides.pptx` (projected). The `.tex` is the
only source of truth. The build compiles it **twice**: once as projected (every overlay step its
own page — the PPTX) and once in Beamer **handout mode** (overlays collapsed, `handout:0` content
dropped — the printed handout).

Preamble: `\documentclass[aspectratio=169,11pt]{beamer}` + `\usepackage{algebra2-beamer}`. The
title slide is hand-built (forest background canvas + minipage); content frames use
`\forestheader{Title}` and `\sectionlabel[color]{LABEL}`. `\CourseName` is **not** defined in
beamer — write the course name literally.

**Frame order:** title → **targets** (vocabulary in bold, "how today runs" 5/40/5/10) →
**warm-up** (2–3 items, answers in `\reveal`) → **three or four cycles**, each:

- **Definition** — `\forestheader{Definition: term}`; a `block` with the term in bold and the
  definition or general form as a complete sentence; a pre-drawn display where one helps. Nothing
  to fill in.
- **Example** — `\sectionlabel{Watch --- I do this one}`; one problem worked in full, each step
  with its reason (`\pause` between steps is fine).
- **Now you try** — `\sectionlabel[goldacc]{In the notes column --- then check}`; one or two
  problems of the example's shape on fresh numbers, problem in the top half of the frame, and
  `\reveal{\begin{block}{Check} answer + the deciding step \end{block}}`. The **last cycle's
  Now you try is the crux** (the case where the two answers disagree), flagged
  `\sectionlabel[redacc]{…}`.

→ **wrap-up** (definitions one line each + a *Watch out* block with the target misconception) →
**homework** (the block for the lesson's source, and a one-line preview).

**Answers only in `\reveal`.** Never hide an answer with `\pause` or `\only<2>` — handout mode
prints the last state. After building, prove the handout is answer-free:
`pdftotext target/unitXX/lessonYY/slides_handout/main.pdf - | grep -c Check` → 0.

## Unit tests (summative assessments)

Unit-level, not per-lesson — scaffolded once per unit under `unitXX/tests/` and
`unitXX/test_keys/` (see `LESSON_SHAPE.md` §6 and the shared skill's `references/build.md`). Author **two blank
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
actual versions parallel so the practice test is honest preparation, and make them the same number
of pages. Build/publish with `make -C unitXX/tests all` and `make -C unitXX/test_keys all`.

**`unit01/tests` and `unit01/test_keys` are the reference** (regenerated 2026-09-16): 12pt, **no
vocabulary part**, five skill parts (A–E) totalling 100 points, and a body that is
**byte-identical in blank and key** — the answers live only in a preamble-defined
`\slot{width}{answer}` (a fixed-width underline, filled in the key), in `\opt` / `\optok` (the key
marks the correct choice with a red arrow of zero width), and in `work` blocks, so the two files
cannot drift. The key carries **no `teachernote`**. Prefer that construction to hand-mirroring two
files.

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
  component, titled `\begin{teachernote}[Guided Notes \& Practice]` and so on. A note in a key is the one block
  with no counterpart in the blank, and it is what makes a key run a page long.
- **Worked solutions are not `\ans{}` material.** An inline `$a=b \Rightarrow c=d \Rightarrow e=f$`
  crammed into one cell violates the work rule and gives the student no room; use a `work` block,
  identical in both files. See the shared skill's `references/conventions.md` (`~/.claude/skills/lesson-planning/`).
- Because the key matches the blank line-for-line, the two paginate identically — verify it:
  ```bash
  for c in warmup notes homework; do
    echo -n "$c: "; pdfinfo target/UNIT/LESSON/$c/main.pdf | grep -c . >/dev/null
    printf '%s vs %s\n' "$(pdfinfo target/UNIT/LESSON/$c/main.pdf | awk '/^Pages/{print $2}')" \
                        "$(pdfinfo target/UNIT/LESSON/${c}_key/main.pdf | awk '/^Pages/{print $2}')"
  done
  ```
