# Components

The spec for authoring each file after scaffolding. The scaffolder (`~/.claude/skills/lesson-planning/scripts/new_lesson.py`)
gives you a correctly-preambled skeleton with TODO markers; this file says what fills them.
**Always also open the course's reference lesson, `unit01/lesson04`, as the gold
reference** — these specs summarize the pattern, but the live project is authoritative. For macros
and boxes see the shared skill's `references/conventions.md` (`~/.claude/skills/lesson-planning/`); for where content comes from,
`templates/lesson/course-workflow.md`.

Contents: [Lesson plan](#lesson-plan) · [Cover](#cover) · [Warm-up](#warm-up) ·
[Guided Notes](#guided-notes) · [Individual Practice](#individual-practice) · [Homework](#homework) ·
[Slides](#slides) · [Unit tests](#unit-tests-summative-assessments) ·
[Answer-key discipline](#answer-key-discipline)

**The lesson model is gradual release** — I do, we do, you do alone. The student packet is
**cover → warm-up → Guided Notes & Practice (ending in Guided Practice) → homework**, run as
**5 / 35 / 10 / 10** across the 60-minute period (warm-up / guided notes incl. Guided Practice /
debrief / close & start the homework in class). The **debrief is spoken and has no component**,
and **the homework IS the individual practice** — started in class in the last ten minutes,
alone, with the teacher circulating, and finished at home. There is no practice set at the end
of the notes.

There is **no group activity**, **no exit ticket**, **no tiers**, no `experience` component, no
`objectivebox` in the notes, no `extensionbox` on the homework, and no *Individual Practice*
page. Do not re-add any of them. Lessons still carrying them are legacy — **regenerate rather
than patch**, and ask first. See `LESSON_SHAPE.md` §7, *Legacy shapes and regeneration*, for the
shape-by-shape recognition table and the content mapping.

General rules:
- **Every student component is 12pt** (user direction, 2026-09-07 — cover, warm-up, notes and
  homework alike): `algebra2-article` + `algebra2-boxes`; keys with `algebra2-article` +
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
   the 60-minute period — Warm-Up **5** / Guided Notes & Practice **35** / Debrief **10** /
   Close & Start Homework **10**. Add the minutes up before you write them.
6. **Warm-Up — Activate Prior Knowledge (5 min)** — `fixedskillbox{forestbg}`, two minipages:
   *the three items and what each seeds* · *running it*. Say explicitly how the debriefed
   observation hands off into the first notes row, and end with the 12pt hand-off sentence.
7. **Guided Notes & Practice — I do, then we do (35 min)** — `skillbox{forestbg}` in
   `multicols{2}`: the hook and its unresolved vote; *I do* — one paragraph per section, with
   minutes, naming **by number** which problem of each grid the teacher works and where the
   `work` blocks are; *we do* — the Guided Practice part by part, "the pen must actually change
   hands", the circulating prompts, and which two papers to pick for the debrief.
8. **Debrief — whole class, spoken (10 min)** — `skillbox{forestbg}` in `multicols{2}`: exactly
   **four** things to land (the crux among them, pointed back at the notes row that settles it),
   the two things to demand aloud, and what to cut if short. **The debrief has no component** —
   it is a spoken phase.
9. **Homework — scored, started in class, due the first class after two study halls** —
   `skillbox{goldbox}`: the six items and what each is for, how to sort the formative check, the
   **DeltaMath override** sentence (is this content well covered there, and which set swaps in),
   and a **Preview** of the next lesson.
10. **Watch For (while circulating)** — `skillbox{redbox}`: misconceptions to catch, keyed to
    notes row / Guided Practice part / homework item numbers, plus cold-call prompts.
11. **Close & Start Homework (10 min)** — `skillbox{goldbox}`: the launch of item 1 aloud, the
    three piles of what the teacher sees while circulating, and the "what changed today"
    sentence.
12. **Teacher Notes** — **three** `teachernote`s, in packet order: `[Warm-Up]`,
    `[Guided Notes \& Practice]`, `[Homework]`. Pacing splits that actually fill each phase's
    minutes, must-land moments, common slips, the early-finisher move, and how to sort the
    formative check. **This is the only place teacher prose goes** — never append one to a `_key`,
    which would make the key longer than its blank. See the shared skill's `references/conventions.md` (`~/.claude/skills/lesson-planning/`).

There is **no Hook section** (the hook lives inside the Guided Notes box), **no Individual
Practice section**, and **no Reinforcement & Extension section** — the homework box absorbed it.
The full section order is `LESSON_SHAPE.md` §5, which wins over this summary.

Record the lesson's **standards** (the codes the user supplied) in the plan for the audit trail.

## Cover

`cover/main.tex` — student-facing front page of the packet. No key. Structure:
- `\coverbanner{Unit N \quad Unit Title}{Lesson N.M \quad Lesson Title}` — it measures the title
  block and sizes the forest band to it. (The skeleton still draws the old fixed TikZ band.)
- `\namedateperiod` — **the only place in the lesson it appears.** See "Namestrip" below.
- `learningtargetbox` — an "I can…" list **using the lesson's formal vocabulary in bold**. There
  is nothing to withhold: the notes name each term as they build it.
- `tocbox` — a `tabularx` with **three rows in packet order** (Warm-Up, Guided Notes \& Practice —
  "ending in *Guided Practice*", Homework) + a Total row. **Every row is scored** — a
  `\blank{1.2cm}`, homework included; nothing prints `NA` any more. The homework row's description
  ends **"--- scored; due the first class after two study halls"** (course policy of record,
  2026-09-03 — never "due next class"). The table is four columns (`c l X r`); **every row needs
  four cells** or the column widths collapse. There is no debrief row (it is a phase, not a
  component), no individual-practice row (the homework is the individual practice), and no
  activity row (there is no activity).
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

`notes/` (+ `notes_key/`) — **the direct-instruction centrepiece, 35 minutes**, in the **Main
Ideas / Notes** shape (modelled on the Algebra 2 guided-notes worksheets; density rules of
2026-09-12). `\pageheader{...}` (no name row — Namestrip), the `vocabbox`, the `hookbox` (it stays), then **one
`guidednotes` table** set in `\small`. Ported from AP Statistics 2026-09-12. **3–4 pages** at
12pt, **12–19 numbered problems**. The page belongs to the student's pen.

- `vocabbox` — one `\vterm{Term}` per key term (4–6): the fixed-height row pair `\vterm` /
  `\vtermans` defined in the notes preamble (copy from the reference lesson). The box says **"Fill in
  each term as we name it in the notes below"** — filled during instruction, never front-loaded.
  Then the `hookbox`, ending on a circle-one vote left unresolved.
- **No `objectivebox`** — the targets are on the cover. No `notesbox`, no `practicebox`.
- `guidednotes` — the two-column table, *Main Ideas / Questions* | *Notes*, **four to five
  rows**, each `\mainidea[small lead]{Label} & ... \\ \hline`. The label is one short word or
  two (uppercased by the macro; a single word over ten letters overflows). The Notes cell holds,
  in order:
  1. **One or two complete printed sentences** — the definition, read. Never a sentence with
     words punched out. A `\stepnum{n}` list for a procedure.
  2. **One large pre-drawn display** (TikZ, `scale` 0.8–1.0) the student reads — or annotates
     with `\labelbox{W}{}` ("This is a ___", an arrow's label). Where the idea deserves it, an
     *In your own words* line with a `\writespace{1.6cm}{}`.
  3. `\notesprompt{…}` and a **two-across `probgrid`** (`|Y|Y|`, never three across) of
     `\pcell{n}{statement}{H}{}` cells, **H = 1.8–2.6 cm** of answer space each, 2–4 problems
     per row.
- **Blanks:** a `\blank{}` only where a single word or number *is* the answer — a table to fill,
  a display to name. Budget a handful per lesson. Mid-sentence blanks are banned.
- **The I do / we do split is row by row**: the teacher reads the definition, marks up the
  display, and works the first problem of each grid; the class works the rest with the pen in
  their hand. **The trap and the crux are problems in a grid**, in the last instruction row.
  **The last row is Guided Practice**: `\mainidea[Guided practice]{Its Title}`, one new example
  in a second context, four problems worked *with* the class, prompt `We work these together.`
- **Packing** (a table row cannot break across pages): the figure gets its own sub-row (`\\`
  then `& …`), and **each grid row is its own sub-row** — close the `probgrid`, `\\ &`, reopen
  as `probgrid*` (no top rule). `\\` inside a cell ends the row: break lines with `\par`.
- **Every display is pre-drawn** and read; students construct only by filling a table.
- **The key mirrors the blank byte for byte** except `-key` for `-boxes`, the header's
  `--- Answer Key`, `\vterm`→`\vtermans`, `\blank`→`\ans`, and the answer argument of each
  `\pcell`, `\writespace`, `\labelbox`. Keep every answer shorter than its space. Prove the
  page counts match.

## Individual Practice

**Retired 2026-09-07** — the notes end at the Guided Practice row; the homework is the
individual practice. Never author the `scenariobox[Individual Practice ...]` page.

## Homework

`homework/` (+ `homework_key/`) — the **"you do alone"** block. **Every lesson generates one**
(user direction, 2026-08-31): DeltaMath does not cover all of this course's content, and where it
does the teacher **overrides** and assigns a DeltaMath set instead — so the plan's *Homework* box
always names what could be swapped in. **This page IS scored**: the cover's score cell is a
`\blank{1.2cm}`, never `NA`. It **is the lesson's individual practice** — started in class in the
last ten minutes, alone, and finished at home.

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
(or `\namepartnerperiod`) in `warmup`, `notes`, or `homework` — or in any `_key`,
or in a legacy `experience`/`exit_ticket`. The components are stapled behind the cover, so a row on each one is redundant and
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
vocabulary, plus a "how today runs" block with the **5 / 35 / 10 / 10** split) → warm-up (ending in
a "hold on to this" block) → hook (the vote, **left unresolved**) → **four notes frames**, two per
section (1a/1b, 2a/2b), matching the packet exactly (the crux frame is flagged
`\sectionlabel[redacc]{}` and carries a `\begin{block}` giving the case where the two answers
disagree) → **Guided Practice** (the lettered parts and "the questions I will ask") → **debrief**
(the same four numbered takeaways as the plan's debrief box, plus a "say it without the notes"
block) → **close & start the homework** (what changed today, a **Homework — scored, due the first
class after two study halls** block, and a one-line preview). Reference implementations:
`unit01/lesson02/slides` and `unit01/lesson04/slides`.

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
