# Components

The spec for authoring each file after scaffolding. The scaffolder (`scripts/new_lesson.py`)
gives you a correctly-preambled skeleton with TODO markers; this file says what fills them.
**Always also open a real built lesson (`unit01/lesson00` or `unit01/lesson01`) as the gold
reference** — these specs summarize the pattern, but the live project is authoritative. For macros
and boxes see `references/conventions.md`; for where content comes from,
`references/course-workflow.md`.

Contents: [Lesson plan](#lesson-plan) · [Cover](#cover) · [Warm-up](#warm-up) ·
[Guided Notes](#guided-notes) · [Individual Practice](#individual-practice) · [Homework](#homework) ·
[Slides](#slides) · [Unit tests](#unit-tests-summative-assessments) ·
[Answer-key discipline](#answer-key-discipline)

**The lesson model is gradual release** — I do, we do, you do alone. The student packet is
**cover → warm-up → guided notes (ending in Guided Practice and Individual Practice) → homework**,
run as **5 / 20 / 15 / 10 / 10** across the 60-minute period (warm-up / guided notes incl. guided
practice / individual practice / debrief / close & start the homework in class). The **debrief is
the 10-minute phase between the individual practice and the close; it has no component** — the
class corrects its own practice in a second colour while the teacher works all three problems on
the board.

There is **no group activity** (cut course-wide, 2026-09-01), **no exit ticket**, **no tiers**,
and no `experience` component. (Lesson 1.0 still has an `activity` pair from the interim
2026-08-31 shape; Units 2–7 have `experience` pairs or `exit_ticket` + tiered activities. All
legacy; regenerate rather than patch. See SKILL.md "Converting a lesson that is on an older
shape.")

General rules:
- **Every student component is 10pt except the warm-up, which is 12pt** (and still one page):
  `algebra2-article` + `algebra2-boxes`; keys with `algebra2-article` + `algebra2-key`.
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
- **The vocabulary is named openly everywhere** — cover, notes, homework, deck. The old EFFL
  spoiler rule is dead, because the notes now come *before* the practice.
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
   the 60-minute period — Warm-Up 5 / Guided Notes 20 / Individual Practice 15 / Debrief 10 /
   Close & Homework 10.
6. **Warm-Up — Activate Prior Knowledge & Spiral Review** — `fixedskillbox{forestbg}`: the ~3
   items, which prior skill each rehearses, and what to debrief aloud. Say explicitly how the
   debriefed observation hands off into notes section 1.
7. **Hook** — `skillbox{forestbg}`: the 60-second context, the questions to ask with their
   answers in parentheses, and the idea to land in one sentence. **The hook's numbers should be
   the ones every worked example in the notes reuses.**
8. **Guided Notes — the Lesson (20 min)** — `skillbox{forestbg}` in `multicols{2}`: one bold
   paragraph per numbered notes section saying what to build and where the `work` blocks are,
   ending with the Guided Practice paragraph ("do this one *with* the class — it is the last
   thing they see before working alone").
9. **Individual Practice — On Your Own (15 min, silent)** — `skillbox{redbox}`: the 1-minute
   launch script, then `multicols{2}`: **What students do** (the three problems and why they are
   the three shapes of the skill; which is the crux) | **What the teacher does** (circulate,
   silent; a bullet list of *questions, cues, and prompts — not answers* keyed to problem
   numbers; the early-finisher move; note names for the debrief).
10. **Debrief (10 min — what goes on the board, in a second color)** — `skillbox{forestbg}`: a
    numbered list of **exactly four things to land** — problem 1 worked, the must-land moment
    (the target misconception, pointed back to the notes' caution box), problem 2, and problem 3
    / the crux with what a wrong answer reveals. End by naming which item to cut if time is short
    and which two to protect.
11. **Active Monitoring — Watch For** — `skillbox{redbox}`: misconceptions to catch while
    circulating, keyed to notes, Individual Practice, and homework item numbers, plus cold-call
    prompts.
12. **Reinforcement & Extension** — `skillbox{goldbox}`: itemize the homework's ~6 problems and
    its extension; a **DeltaMath override** sentence saying whether this content is well covered
    there and what set to swap in if so; and a **Preview** of the next lesson.
13. **Teacher Notes** — **four** `teachernote`s, in packet order: `[Warm-Up]`, `[Guided Notes]`,
    `[Individual Practice]`, `[Homework]`. Pacing splits that actually fill each phase's minutes,
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
- `tocbox` — a `tabularx` with **three rows in packet order** (Warm-Up, Guided Notes — "ending
  in *Guided Practice* and *Individual Practice*", Homework) + a Total row. **Every row is scored** — a `\blank{1.2cm}`, homework
  included; nothing prints `NA` any more. The homework row's description ends
  *"--- \emph{due next class}"*. The table is four columns (`c l X r`); **every row needs four
  cells** or the column widths collapse. There is no debrief row (it is a phase, not a
  component) and no activity row (there is no activity).
- `remindbox` (Keep in Mind) — a **content** summary: the lesson's key definitions and the
  distinction it turns on, in three or four sentences, in a form the student can revise from.

## Warm-up

`warmup/` (+ `warmup_key/`) — one page, ~3 quick items of **spiral review**, rehearsing exactly
the prior skills the lesson leans on. **12pt** (user direction, 2026-08-31 — larger type than
the rest of the packet, deliberately; it must still fit one page blank and keyed), no name row.
The last item ends on the question notes section 1 answers, deliberately left hanging. The plan's Warm-Up box names what each
item rehearses, what to debrief aloud, and how that hands off into notes section 1. May also be a
**prefab PDF** (`warmup/main.pdf` + `warmup_key/main.pdf`) — `lesson.mk` merges it directly. Key
mirrors with `\ans`.

## Guided Notes

`notes/` (+ `notes_key/`) — the **"I do / we do"** block (**20 minutes** including the Guided
Practice box) **plus the "you do alone"** (the Individual Practice block, **15 minutes**) —
**4 pages at 10pt**, with Individual Practice landing on its own clean page. This is where the
vocabulary is built and named, *before* the practice uses it. Structure, in order:

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
   block, worked *with* the class — the last thing students see before working alone.
6. **Individual Practice** — see the next section.

`\boxguard` on each `notesbox`: 20–26 at 10pt; `\boxguard[22]` before the Individual Practice box.

## Individual Practice

The **"you do alone"** block, **15 minutes, silent**, living on the **last page of the Guided
Notes** — not a component of its own. It is a `scenariobox[Individual Practice --- On Your
Own]{navy}` (no new environment in `shared/`), preceded by `\boxguard[22]` so it lands on a clean
working page. **Three problems**, deliberately the three *shapes* (or directions) of the skill —
for 1.2 an equation / an "and" / an "or"; for 1.3 rule → features / graph → rule / the same-vertex
pair; for 1.4 evaluate across a boundary / read a graph and write its rule / two pieces and the
staircase — with the **crux last**: the problem that isolates the lesson's target misconception,
usually ending in a "a classmate says … what did they miss?" `\writelines{2}`. Every solve goes in
a `work` block. Open the box with a one-sentence rule to apply; keep it to ~5 minutes a problem.

The lesson plan's *Individual Practice* box carries the launch script and the teacher's cues; the
debrief works all three problems on the board. There is **no group work** anywhere in the lesson.

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
(or `\namepartnerperiod`) in `warmup`, `notes`, or `homework` — or in any `_key`,
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

**The deck follows the gradual-release flow, 11 frames:** title → learning targets (naming the
vocabulary, plus a "how today runs" block with the 5/20/15/10/10 split) → warm-up (ending in a
"hold on to this" block) → hook → **four notes frames**, one per numbered notes section, matching
the packet exactly (the misconception section gets a `\begin{block}` with the case where the two
answers disagree; the last notes frame ends with the Guided Practice) → **individual-practice
launch** (the three problems, the one-sentence rule, "look up the page, not at your neighbour",
the early-finisher move) → **debrief** (the same four numbered takeaways as the plan's debrief
box) → close (what changed today, a **Homework — start it now** block naming what the packet page
covers and that the rest is due next class, and a one-line preview). Reference implementations:
`unit01/lesson02/slides` and `unit01/lesson03/slides`.

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
  for c in warmup notes homework; do
    echo -n "$c: "; pdfinfo target/UNIT/LESSON/$c/main.pdf | grep -c . >/dev/null
    printf '%s vs %s\n' "$(pdfinfo target/UNIT/LESSON/$c/main.pdf | awk '/^Pages/{print $2}')" \
                        "$(pdfinfo target/UNIT/LESSON/${c}_key/main.pdf | awk '/^Pages/{print $2}')"
  done
  ```
