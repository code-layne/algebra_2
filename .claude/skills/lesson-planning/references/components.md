# Components

The spec for authoring each file after scaffolding. The scaffolder (`scripts/new_lesson.py`)
gives you a correctly-preambled skeleton with TODO markers; this file says what fills them.
**Always also open a real built lesson (Unit 1) as the gold reference** — these specs summarize
the pattern, but the live project is authoritative. For macros and boxes see
`references/conventions.md`; for where content comes from, `references/course-workflow.md`.

Contents: [Lesson plan](#lesson-plan) · [Cover](#cover) · [Warm-up](#warm-up) ·
[Experience](#experience) · [Slides](#slides) ·
[Unit tests](#unit-tests-summative-assessments) ·
[Answer-key discipline](#answer-key-discipline)

**The lesson model is Math Medic EFFL** — experience first, formalize later. The student packet
is cover → warm-up → experience. There are **no** guided-notes, activity, or exit-ticket
components, **no tiers**, and — since 2026-08-20 — **no homework**: the experience's unscored
Check Your Understanding is a lesson's entire practice set, done in class, packet kept by the
student. (Lessons authored before those dates still carry the old components; new and regenerated
lessons must not.)

General rules:
- Student components preamble with `algebra2-article` + `algebra2-boxes`; keys with
  `algebra2-article` + `algebra2-key`.
- Keep the **key structurally identical** to its blank — it is the blank with answers filled in.
  **A component must come out the same number of pages on both sides.** Every worked solution goes
  in a `work` block authored identically in the two files (see "The work rule" in
  `references/conventions.md`); a prose answer that wraps to n lines gets `\writelines{n}` in the
  blank. Build both and compare page counts before you call a component done.
- Content is **standards-based and original**: source topic/sequencing from `COURSE_PLAN.md`
  and the standards the user supplies; never copy the `spec/` publisher reference (copyright).
- Every component runs the loop **read/interpret → justify** ("what does this feature mean
  here, and how do you know?"). Never ask students to *sketch/draw/construct* a graph from
  scratch — give a pre-drawn figure to read, a table to complete, or a computation task.
- **Spoiler rule:** the cover and the deck's learning-targets frame never pre-name the
  vocabulary the debrief will attach — plain language only. The plan (teacher-facing) keeps the
  formal objective.
- Use the project's boxes and fill-in macros rather than hand-rolling layout.

## Lesson plan

`main.tex` at the lesson root — teacher-facing, never handed to students. Canonical section
order (same skeleton for review and primary-content lessons):

1. **Title block** — `\CourseName: \SchoolYear` + `\UnitNumberName \LessonNumberName`.
2. **Primary Objective / Standards / Lesson model** — a `tcolorbox` (forestbg/forest): the
   objective in formal terms (the plan is teacher-facing — the spoiler rule does not apply
   here), the standards codes, and a one-paragraph statement of the EFFL model.
3. **Learning Targets & Key Understandings** — `skillbox{goldbox}`, two `tabularx` cells. Left:
   the "I can…" targets in student language. Right: the *why*, including the lesson's target
   misconception stated explicitly.
4. **Vocabulary, Concepts & Theorems** — `skillbox{sky}`, a `tabularx` term/definition table
   (use `\TallMath{...}` for tall formulas).
5. **Lesson at a Glance** — `fixedskillbox{forestbg}`: a Phase/Min/Students/Teacher table for
   the 60-minute period — Warm-Up 5 / Experience: Activity 20 / Debrief: Formalize 13 /
   Application 7 / Check Your Understanding 10 / Close 5.
6. **Warm-Up — Activate Prior Knowledge** — `fixedskillbox{forestbg}`: the 3 warm-up items and
   the *seed* each plants (which formal idea it sets up **without naming it**), plus what to
   debrief aloud.
7. **Experience — The Activity** — `skillbox{forestbg}`: the launch script (2 min), then
   `multicols{2}`: **What students do** (the arc of the two scenarios, naming the crux
   question) | **What the teacher does** (circulate; a bullet list of *questions, cues, and
   prompts — not answers* keyed to item numbers; which group work to pick for the board).
8. **Debrief — Formalize** — `skillbox{forestbg}`: the ordered "red ink" moves — each formal
   term written on top of a displayed student answer — plus the QuickNotes walkthrough and a
   "why this order" note. Any example the activity no longer carries (the special case) is
   posed cold by the teacher here.
9. **Application** — `skillbox{forestbg}`: the worked-together problem, the questions the teacher
   asks while the students hold the pen, and the concept the "what if we change a number?" part is
   really testing.
10. **Check Your Understanding — the lesson's practice, *not scored*** — `skillbox{redbox}`: the
   ~6 items itemized, pairing (pairs → solo), an explicit "**there is no homework**, so this is the
   whole practice set", an explicit "these carry no point value — do not collect for a grade (the
   cover's score column reads **NA**)", **which item is the formative check** with the sort
   categories, and — since 10 minutes rarely covers six items — **which items are the priority and
   which are the early-finisher bank**.
11. **Watch For** — `skillbox{redbox}`: misconceptions to catch while circulating, keyed to item
    numbers, plus cold-call prompts.
12. **Close & Preview** — `skillbox{goldbox}`: **nothing is assigned** — say so explicitly, name
    what changed today, and preview the next lesson. Never write a homework paragraph here.
13. **Teacher Notes** — one `teachernote` per component, in packet order:
    `\begin{teachernote}[Warm-Up]`, `[Experience]`. Pacing splits, must-land
    moments, the early-finisher move, how to sort the formative check. **This is the only place
    teacher prose goes** — never append one to a `_key`, which would make the key longer than
    its blank. See `references/conventions.md`.

Record the lesson's **standards** (the codes the user supplied) in the plan for the audit trail.

## Cover

`cover/main.tex` — student-facing front page of the packet. No key. Structure:
- Full-bleed forest banner (tikz) with `\LARGE` course name, unit, and `Lesson <id>  <title>`.
- `\namedateperiod` — **the only place in the lesson it appears.** See "Namestrip" below.
- `learningtargetbox` — an "I can…" list, **spoiler-free**: describe what students will be able
  to *do* in plain language, without pre-naming the vocabulary the debrief will attach
  ("read the story a straight-line graph tells — where it starts, where it hits zero, how fast
  it changes"), never the formal terms.
- `tocbox` — a `tabularx` with three rows (Warm-Up, Experience, **Check Your Understanding**) +
  a Total row. Score cells are `\blank{1.2cm}` **except Check Your Understanding, which prints
  `\textbf{NA}`** — it is practice and is not scored. **No homework row.** Keep descriptions
  spoiler-free too.
- `remindbox` (Keep in Mind) — describes the **EFFL process only** ("you and your group will
  work out … using what you already know — and only afterward will we name what you found")
  and **stops there**: no content preview, no vocabulary.

## Warm-up

`warmup/` (+ `warmup_key/`) — one page, ~3 quick items rehearsing **exactly the prior skills
the activity leans on**, each planting the *seed* of a formal idea **without naming it** (a
point on an axis seeds "intercept"; "for what input is $g(x)=0$?" seeds "zero"; a constant-step
table seeds "slope"). 10pt, no name row. The plan's Warm-Up box names each seed and what to
debrief aloud. May also be a **prefab PDF** (`warmup/main.pdf` + `warmup_key/main.pdf`) —
`lesson.mk` merges it directly. Key mirrors with `\ans`.

## Experience

`experience/` (+ `experience_key/`) — **the heart of the lesson**, one document, **four parts**,
in this order, on an explicit **page budget** (user, 2026-08-20 — the experience kept coming out too
long):

| Part | Budget | What it is |
| --- | --- | --- |
| 1. Activity | **≤ 2 pages** | group work from prior knowledge only |
| 2. QuickNotes | **½ page** | the debrief fills it |
| 3. Application | **½–1 page** | one problem worked *together*, right after the notes |
| 4. Check Your Understanding | **1–2 pages** | independent practice — **not scored** |

Hold the budget: it is the whole point of the four-part split. A part that runs over gets cut, not
carried. `\documentclass[12pt]{article}` (Math Medic sizing — the rest of the packet is
10pt), `\pageheader{Unit X, Lesson Y.Z}{Experience: <Activity Title>}`, no name row.

Preamble defines the open-answer-space macro, byte-identical in blank and key:

```latex
\newcommand{\answerspace}[2]{\par\nopagebreak\noindent\begin{minipage}[t][#1][t]{\linewidth}%
  \color{keyred}\bfseries #2\end{minipage}\par}
```

The blank passes `{}` as the second argument (reserves exactly `#1` of open space); the key
passes the answer — so the two files paginate identically by construction. Size `#1` for 2–4
handwritten lines (1.4–2.8cm). **No `\writelines` in the experience** — Math Medic answers go
in open space. Short inline `\blank{}`s remain for table cells and one-word/rule fills; keep
key `\ans{}` texts short enough not to wrap wider than the blank they replace, or the page
breaks drift.

1. **Activity** — a `headlinebox` framing one motivating context, then **two `scenariobox`es**
   (~10–13 lettered sub-questions total, ~2 pages) that students work **from prior knowledge
   only**: complete a table, write a rule, circle/label pre-drawn graphs, answer in the open
   space. Scenario 1 builds the whole toolkit on one example; scenario 2 varies it (the
   contrast case) and carries the lesson's **crux question** — the one that surfaces the target
   misconception — plus a closing story-vs-math question. **The timebox rule:** the activity
   must fit the 20-minute block; the special case and the compare-two-graphs question belong to
   the debrief, the Application, or Check Your Understanding, not here. Never name the formal vocabulary in the
   activity — students answer in their own words.
2. **QuickNotes** — one titled `tcolorbox` (sky/navy) the **debrief fills**: a small worked
   example figure beside fill-in bullets covering the lesson's formal terms. This is a summary
   of what the groups discovered, not a lecture; keep it to one box (~1 page). Blanks here are
   `\blank{}` fills (key: `\ans{}`).
3. **Application** — a `notesbox` (`Application: <Title>`) with **one problem worked together**,
   opening ``We will do this one together.'' This is the first place the just-named vocabulary is
   *used*, so it is the natural home for the lesson's **modeling standard** (write the model →
   solve it in a `work` block → interpret the answer → one "what if we change a number?" question
   that tests the concept rather than the procedure). Half a page to one page; the teacher holds
   the questions, the students hold the pen.
4. **Check Your Understanding** — a `notesbox` titled
   `Check Your Understanding \quad {\normalfont\itshape (practice --- not scored)}` with
   **~6 items in new contexts**, worked pairs → solo. **This is the lesson's entire practice set —
   there is no homework** — so it must span the lesson's whole standard, not just sample it: the
   core procedure, a *deliberate contrast pair* (same task, opposite condition — the pair that
   surfaces the target misconception), the special case the activity dropped plus its boundary
   ("for which $k$ does … fail?"), a **modeling item** in a fresh context with an
   interpret-the-answer follow-up, and an **SOL-style multiple-choice item as the formative check**
   (the plan says how to sort responses). Say "there is no homework" in the box's own intro line so
   students know the practice is here. Use `\answerspace` for explain items. Close the document
   with the `spiralbox` preview of the next lesson (it used to live at the end of the homework).

   **It carries no point value.** It is practice, so the cover's score column prints **`\textbf{NA}`**
   for it instead of a `\blank{}`, the plan tells the teacher to spot-check rather than collect for
   a grade, and the deck says "practice, not a quiz." Budget **1–2pp, and expect 2** now that it
   carries the whole load — but 2pp is a **ceiling**: a seventh item gets cut, never spilled onto a
   third page. Ten minutes will not cover six items for every student; the plan names which are the
   priority and which are the early-finisher bank.

Key mirrors exactly: same macro, answers in the second argument of each `\answerspace`,
`\ans{}` in the blanks, MC option tagged `\textcolor{keyred}{\textbf{$\leftarrow$ correct}}`.
`\boxguard` counts here are 12pt-relative: use ~14–16, not the 24–30 used in 10pt components.
Reference implementation: `unit01/lesson02/experience` (the four-part shape, with the six-item
CYU that replaced homework). `unit01/lesson00` is still the older three-part cut, still has a
`homework` dir, and is due to be re-cut to this budget.

## Homework — removed (2026-08-20)

**Do not create a `homework` component.** Homework was dropped from the course: Check Your
Understanding is the practice, it is unscored, it is done in class, and the student keeps the
packet. The scaffolder no longer includes `homework` in its defaults.

Lessons authored before 2026-08-20 still have `homework/` + `homework_key/`, and
`shared/lesson.mk` still merges them so those packets keep building. **Regenerating** such a
lesson means: delete both dirs, expand CYU to ~6 items absorbing what the homework carried, move
the closing `spiralbox` preview into the experience, drop the cover's homework row, retitle the
plan's "Homework & Preview" box to "Close & Preview", and delete the `[Homework]` teacher note.
`unit01/lesson02` is the worked example of exactly that conversion.

**Build gotcha when deleting a component:** a stale stamp under `.stamps/unitXX/lessonYY/` makes
`make` skip recompiling a *sibling* whose PDF was cleaned, and `pdfunite` then fails on a missing
file. Remove `.stamps/<unit>/<lesson>` alongside `target/<unit>/<lesson>`.

## Namestrip — where the name/date/period row goes

**The name row appears exactly once per lesson: on the cover.** Do not put `\namedateperiod`
(or `\namepartnerperiod`) in `warmup` or `experience` (or the legacy `homework`/`notes`/
`activity`/`exit_ticket`) — or in any `_key`. The components are stapled behind the cover, so a row on each one is redundant and
costs vertical space at the top of every page. Exempt: `cover/` (it's the one place it belongs)
and `unitXX/tests/` (taken in a testing setting, not behind a cover).

New lessons come out of the scaffolder already correct. To apply it to a lesson authored before
the convention:

```bash
python3 .claude/skills/lesson-planning/scripts/namestrip.py --project . --unit 02 --lesson 03
```

Add `--check` to report without changing anything (exits 1 if it finds any). The script skips
`cover/`, hits blanks and keys together, and is idempotent. Rebuild afterward and confirm the
warm-up and exit ticket are still one page each, blank and key.

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

**The deck follows the EFFL flow, ~10 frames:** title → learning targets (**spoiler-free**, plus
a "how today works" block) → warm-up → activity launch (the context, the scenarios, "your job")
→ 3–4 **debrief frames** that formalize in "red ink" (a `\redink{}` macro colors the formal
terms `redacc`, mirroring the second marker color on the board) → a QuickNotes summary frame →
practice. The debrief frames are the deck's payload — everything before them stays
vocabulary-free. Reference implementation: `unit01/lesson00/slides`.

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
- For multiple choice, keep all options and tag the correct one
  (`\textcolor{keyred}{\textbf{$\leftarrow$ correct}}`), then show the reasoning in a short
  `itemize`.
- `\ans` is text-mode: never put it inside `$...$` — wrap math fragments instead
  (`\ans{$\sqrt{n}$}`) — and never let it span a blank line.
- **No `teachernote` in a key.** Teacher-only guidance goes in the lesson plan, one note per
  component, titled `\begin{teachernote}[Experience]` and so on. A note in a key is the one block
  with no counterpart in the blank, and it is what makes a key run a page long.
- **Worked solutions are not `\ans{}` material.** An inline `$a=b \Rightarrow c=d \Rightarrow e=f$`
  crammed into one cell violates the work rule and gives the student no room; use a `work` block,
  identical in both files. See `references/conventions.md`.
- Because the key matches the blank line-for-line, the two paginate identically — verify it:
  ```bash
  for c in warmup experience; do
    echo -n "$c: "; pdfinfo target/UNIT/LESSON/$c/main.pdf | grep -c . >/dev/null
    printf '%s vs %s\n' "$(pdfinfo target/UNIT/LESSON/$c/main.pdf | awk '/^Pages/{print $2}')" \
                        "$(pdfinfo target/UNIT/LESSON/${c}_key/main.pdf | awk '/^Pages/{print $2}')"
  done
  ```
