---
course: Algebra 2
prefix: algebra2
meeting_length: 60
reference_lesson: unit01/lesson04
components: [cover, homework, slides]
keyed: [homework]
one_page: []
doc_titles:
  warmup: Warm-Up
  notes: Guided Notes \& Practice
  homework: Homework
  activity: Group Activity
  exit_ticket: Exit Ticket
note_labels:
  slides: Slides
  warmup: Warm-Up
  notes: Guided Notes \& Practice
  homework: Homework
  activity: Group Activity
  exit_ticket: Exit Ticket
  experience: Experience \& Formalize
skeletons: templates/lesson
unit_tests: true
structure_source: standards
spec_dir: spec
course_index: COURSE_PLAN.md
check_target: false
point_size: 12
---

# Lesson Shape — Algebra 2

This is the course profile the shared `lesson-planning` skill (`~/.claude/skills/lesson-planning/`)
reads before authoring anything. The skill carries the mechanism — build, LaTeX rules, workflow,
scripts; **this file carries the policy** — everything true of this course that is not
necessarily true of the others. Keep it current: when a convention changes, change it here first.
The frontmatter is machine-read by the scaffolder; the sections below are read by the skill at
Step 0. The skeletons, the per-component spec (`components.md`), and the content workflow
(`course-workflow.md`) live in `templates/lesson/`.

Two frontmatter notes. `warmup`, `notes`, `activity` and `exit_ticket` appear in `doc_titles`
**only so an older lesson can be rebuilt by name** — none is a default and none belongs in a new
or regenerated lesson (the slides-first shape of 2026-09-25 moved the warm-up and the notes onto
the deck). `experience` is deliberately absent from `doc_titles` and has no skeleton, so
the scaffolder refuses it: it was the EFFL centrepiece and is never scaffolded again (its
`note_labels` entry exists only so `movenotes.py` can title a note lifted from a legacy key).

## 1. The lesson shape

**Algebra 2 is a function-family course** for a secondary-school audience: after a foundations
unit, each unit is built around one function type (linear → quadratic → polynomial → rational →
radical → exponential → logarithmic), and **every unit opens with a Lesson 0, "Characteristics of
____ Functions"** — `lesson00`, id `X.0`; content lessons keep 1-based numbers. Author every
lesson to build **graph-reading fluency**: study how each new function type *behaves* before
manipulating and solving it. The recurring move is **read/interpret → justify** ("what does this
feature mean here, and how do you know?").

**Every lesson is taught from the slides (the *slides-first* shape — user direction,
2026-09-25: "the primary work to be done in the slides — definitions, examples with now you try,
and a homework assignment").** The deck *is* the lesson, and its printed handout
(`lessonYY_slides.pdf`, three slides a page with a ruled notes column) *is* the student's notes:
definitions printed in full, examples worked, and every **Now you try** left open with the notes
column as the work space. There is no guided-notes packet and no paper warm-up. The only
generated student paper besides the handout is the **cover** and, when the lesson's homework
is generated, the **homework**.

| Phase | Minutes | Where |
| --- | --- | --- |
| Warm-Up — 2–3 spiral-review items, answers revealed | 5 | deck |
| Lesson — 3–4 cycles of **definition → worked example → Now you try** | 40 | deck |
| Wrap-up — the definitions read back, the target misconception as a caution | 5 | deck |
| Start the homework, alone, teacher circulating | 10 | `homework` / DeltaMath |

**The phases total 60 minutes — `\MeetingLength`.** If a cycle does not fit, cut a cycle — do not
let the table lie, and do not edit `shared/` to make a lesson fit.

**`slides`** — the centrepiece, 11pt Beamer, `\forestheader` / `\sectionlabel`. Frame order:
title → **targets** (vocabulary in bold, plus a "how today runs" block, 5/40/5/10) → **warm-up**
(one frame; the last item leaves the question the first definition answers) → **one cycle per
idea, three or four cycles**:

1. **Definition** — the term in bold in a `block`, the definition or general form as a *complete
   printed sentence* (nothing to fill in — students annotate in the notes column), and a
   pre-drawn display (graph, table, the two things students conflate side by side) where one
   helps.
2. **Example** — the *I do*: one problem worked in full, every step with its reason. `\pause`
   between steps is fine; the handout collapses it and prints the whole worked example.
3. **Now you try** — the *you do*: one or two problems of the **same shape** as the example, on
   fresh numbers, worked alone in the notes column; the answer and the step that decides it sit
   in `\reveal{…}` (a `block` titled *Check*). **The last cycle's Now you try is the crux** —
   the case where the two answers disagree — flagged `\sectionlabel[redacc]{}`.

→ **wrap-up** (the definitions one line each, and a *Watch out* block with the target
misconception — the same content as the cover's *Keep in Mind*) → **homework** (the block for
this lesson's homework source — §2 — and a one-line preview). Typically 14–18 frames. Every
cycle uses **one context** where it can, so the lesson reads as one story; the Now you try is on
new numbers, never a repeat of the example.

**Answers are revealed, never printed.** `\reveal[n]{…}` (`algebra2-beamer.sty`, 2026-09-25) is
`\uncover<n-| handout:0>` — hidden on the projector until click *n* (default 2) and dropped from
the printed handout, because `shared/lesson.mk` frames the handout from a second compile of the
deck in Beamer's `handout` mode. The PPTX is framed from the projected compile, so each reveal is
its own slide (click to advance). Never put an answer outside `\reveal` on a Now-you-try or
warm-up frame; worked examples are the only frames that show their solutions in print. Size a
Now-you-try frame so the problem sits in the top half — the notes column beside it (six ruled
lines) is all the work space the student gets; a problem that needs more is two frames.

**`homework`** — see §2 for where it comes from. When it is **generated**: **12pt, 2 pages, and
2pp is a ceiling** — a seventh item gets cut, never spilled onto a third page. It opens with a
`remindbox` (*"This is your graded homework. Your packet with completed homework is due the first
class after two study halls. I will announce the due date in class and on TurtleNet."* plus the
lesson's one-sentence rule, identical in blank and key), then a `Practice` `notesbox` of **~6
items spanning the whole standard** (`\small`), in the canonical spread: the core procedure off a
*rule*; a deliberate *contrast pair* (the target misconception) closing with a "why?"; the same
procedure off a *table or graph* (so all three representations appear — and where the skill runs
backwards, "write its rule"); the *special case* and its boundary; a *model* in a fresh context
with a `work` block and an interpret-the-answer follow-up; and an **SOL-style multiple-choice item
as the formative check**. Split it `notesbox{Practice}` / `notesbox{Practice, continued}` with a
`\newpage` so no item breaks across a page, and close with a `spiralbox` previewing the next
lesson. **No `extensionbox`.** The homework's contexts differ from the deck's examples and Now
you trys — teach, then transfer.

**`cover`** — 12pt, `\coverbanner{Unit N \quad Title}{Lesson N.M \quad Title}`,
`\namedateperiod` (the only place it appears), a `learningtargetbox` of "I can…" targets **using
the formal vocabulary in bold**, a `tocbox` with **two scored rows** — *Slide Notes* (the printed
handout, worked in the notes column) and *Homework* (worded for the lesson's source, §2) — plus a
Total row, and a `remindbox` (*Keep in Mind*) that is a **content** summary — the lesson's
definitions and the distinction it turns on, never the process. `\small` inside the boxes.

**The printed products.** Per lesson the teacher prints **two** things for students: the slide
handout (`lessonYY_slides.pdf`) and the packet (`lessonYY_student.pdf` — cover, plus the homework
when it is generated or a printed DeltaMath drop-in). The build keeps the handout out of the
packet (the shared skill's rule); merging them is an open question for the user, not a default.

**What this course does not have — do not re-add any of it:**

- **No guided-notes component and no paper warm-up.** Never scaffold `notes/` or `warmup/` in a
  new lesson; the deck carries both. (`doc_titles` keeps their entries only so a legacy lesson
  still rebuilds by name.)
- **No group activity, no exit ticket.** The formative read is circulating during each Now you
  try, and again during the supervised homework start.
- **No debrief component, no hook frame with an unresolved vote, no Guided Practice frame.**
  Those belonged to the gradual-release shape (§7). The wrap-up is five minutes on the deck.
- **No `extensionbox`, no `objectivebox`, no `reflectionbox`, no tiers**, no `experience`
  component, no *QuickNotes*, no *Check Your Understanding*, no spoiler rule.
- **No `\answerspace`.** Open responses use `\writelines{n}` (see §4).

**Out of scope for the course** (no lessons): conic sections, sequences & series, probability &
statistics, trigonometry, and linear systems / linear programming.

**The pilot is `unit02/lesson02` (2026-09-25), awaiting user review.** Once approved it becomes the
reference — set `reference_lesson` to it in the frontmatter and name it here. Until then, mirror
`unit01/lesson04` for the preamble, the homework, the cover, and the plan's box vocabulary, and
`templates/lesson/slides.tex` for the deck. Every lesson authored before 2026-09-25 is in an older
shape (§7) and is regenerated lesson by lesson when touched — **no bulk sweep**.

## 2. Homework — ask for its source, every lesson

**Before scaffolding a lesson, ask the user how its homework is built** (user direction,
2026-09-25: "I want to be prompted each lesson for how the homework assignment should be
constructed"). Use `AskUserQuestion`, one question, never a default assumed from the last
lesson:

1. **Generated** — Claude authors `homework/` + `homework_key/` in the repo, to the §1 spec.
   Scaffold with the default components.
2. **DeltaMath** — then ask a second question: **online or printed?** and the **set name**.
   - **Online** — no homework in the packet. Scaffold with `--components cover,slides`. The
     cover's row 2 reads *DeltaMath: **set name** — online, not in this packet*; the deck's
     homework frame names the set; the plan's Homework box names it and what it covers.
   - **Printed** — the user exports the set as a PDF. Scaffold with
     `--prefab homework,homework_key` and ask the user to drop `homework/main.pdf` (and, if they
     have one, `homework_key/main.pdf` — without it the key packet repeats the blank). Build only
     once the PDF is there.

For a multi-lesson request, ask for every lesson's source in one `AskUserQuestion` call before
dispatching the subagents. Record the answer in the plan's *Lesson model* line and Homework box.

- **Both cover rows are scored** — a `\blank{1.2cm}`, never `NA`. For DeltaMath online the score
  comes from DeltaMath; the row still carries the blank for the teacher to transcribe.
- **The homework is started in class** in the last 10 minutes — launch item 1 aloud, then
  circulate — and finished at home, whatever its source.
- **Due date — course policy of record (user direction, 2026-09-03, recorded in the `COURSE_PLAN.md`
  Status block): homework is *always* due the first class after two study halls — never "due next
  class."** The wording, where it renders: the cover's homework row, the homework page's own
  remind box (*"Your packet with completed homework is due the first class after two study halls.
  I will announce the due date in class and on TurtleNet"*), the plan's Homework box and Homework
  teacher note, and the deck's homework frame — for DeltaMath too. The skeletons carry it.
- A generated homework's last item is the **formative check** (SOL-style multiple choice, four
  options; in the key the correct option is wrapped in `\ans{}` and the answer lines say which is
  right and why one distractor is wrong). The plan names the categories to sort responses into
  and how the next lesson opens for each. For DeltaMath, the plan names which problem in the set
  plays that role.

## 3. Where structure comes from

**Structure comes from `COURSE_PLAN.md`** at the project root — the scope & sequence: the seven
function-family units, each unit's lesson list (§4), and the cumulative
**characteristics-of-functions spine** (§3), where each Lesson 0 re-teaches the read-a-graph
toolkit built so far and introduces the characteristics its function type is the first to require
(vertex / axis of symmetry / end behaviour in Unit 2, origin symmetry / turning points /
multiplicity in Unit 3, asymptotes + holes + domain restrictions in Unit 4, and so on — never teach
a characteristic before its debut unit). **The ⚠ Status block at the top of `COURSE_PLAN.md` is
the current pedagogy of record** — read it at Step 0. `COURSE_BREAKDOWN.md` is the derived
unit-and-lesson table with standards clusters and authoring status.

**Content is standards-based and original.** There are no CED documents (`spec/` holds no
`ap-*` files). The standards are the ones **the user supplies** — usually 2023 Virginia SOL codes
(`A2.F.1`, `A2.EI.2`, …), possibly CCSS or a district sequence; take them as given, never invent
a code, and record them in the plan's Standards line for the audit trail. `spec/algebra2-vdoe-sol.pdf`
and `spec/algebra1-vdoe-sol.pdf` are the standards documents. Lessons 6.3, 7.3, and 7.4 have **no
SOL home** — they are kept as full lessons labelled *beyond-SOL / precalculus prep* and are barred
from SOL-style test items.

**Copyright.** `spec/Algebra-2-Curriculum/` is the All Things Algebra reference, © Gina Wilson,
licensed to this teacher for classroom use and not for redistribution. Use it as a **topic-sequencing
and difficulty model only** — never copy its problems, wording, or figures. Where a lesson uses a
tool (Desmos), show its output as a pre-made figure.

**Decomposing a unit:** one lesson per bullet in that unit's `COURSE_PLAN.md` list, in order, with
the characteristics lesson as Lesson 0. **Present the proposed lesson map and confirm it with the
user before authoring** — lessons occasionally merge or split. For a Lesson 0 the teaching focus is
the spine rows marked ● for that unit; ○ / · rows are quick review on the new graph. The full
procedure and the element-by-element mapping table (title, objective, priority skills, vocabulary,
hook, learning targets, standards line, practice contexts) are in
`templates/lesson/course-workflow.md`.

**The course index is `COURSE_PLAN.md`, and every run is bookended by it.** Read it at Step 0;
at the end of **every** execution, even a partial one, update the per-unit **Status** — which
lessons are scaffolded, which components are authored vs. still skeleton vs. built, any confirmed
lesson maps — plus the concrete next actions and open questions for the user. Keep it terse and
current: overwrite stale entries rather than appending a changelog. It lives in the repo, so it
travels with the branch and the Step 0 sync brings the latest state forward.

## 4. Style notes

- **Prefix `algebra2`** — `shared/algebra2-{colors,article,boxes,key,beamer}.sty`. `slides`
  needs `algebra2-beamer.sty` (present).
- **Course macros are inlined in each lesson plan, not defined in `shared/`:**
  `\newcommand{\CourseName}{Algebra 2}`, `\newcommand{\MeetingLength}{60 minutes}`,
  `\UnitNumberName`, `\LessonNumberName`. The scaffolder writes them from this profile's `course`
  and `meeting_length`; a hand-edited plan that drops them fails with `Undefined control sequence
  \CourseName`. **`\SchoolYear` no longer exists** — delete any reference, never re-add the macro.
  **The printed title is just `Algebra 2`** — no teacher name, no school year, anywhere a title
  renders (plan title block, cover banner, deck title slide, unit cover). Beamer has no
  `\CourseName`: the deck writes the course name literally.
- **Sizes.** **Every student component is `\documentclass[12pt]{article}`** + `algebra2-article` +
  `algebra2-boxes` (user direction 2026-09-07, matching the stats and SAAR courses), with
  `\small` inside the cover's and the notes' boxes and in the homework's practice boxes; the
  plan is 10pt and the deck 11pt. That is the frontmatter's `point_size: 12`. Budgets: cover 1p ·
  homework 2pp (ceiling); on legacy lessons, warm-up 1p · notes 4pp. 1.0, 1.1, 1.3, 1.5 are still
  10pt until regenerated.
- **The deck (`algebra2-beamer.sty`)** — `\forestheader{Title}`, `\sectionlabel[color]{LABEL}`,
  and **`\reveal[n]{answer}`** (added 2026-09-25): `\uncover<n-| handout:0>`, so an answer is
  hidden until click *n* on the projector and absent from the printed handout. It keeps the space
  reserved; wrap a whole `block` in it, not a fragment of a sentence. Plain `\pause` / `<+->` in
  a worked example is fine — handout mode collapses it and prints the finished example. **Never
  use `\only<2>` or `\pause` to hide an answer** — handout mode shows the last state, so the
  answer would print. Verify with `pdftotext` on `target/…/slides_handout/main.pdf` (§7).
- **`\boxguard`** (`-boxes`, `\Needspace`) defaults to 16 lines; at 10pt counts run **16–26**
  (`20–26` on a `notesbox`, `[12]` before the first `notesbox` after the vocab box, `[30]` when a box opens
  with an unbreakable `tabularx`/`\fbox`, `[14]` to keep a lead-in with its table). It is **inert
  inside a breakable `tcolorbox`**, and a "guard costs a page" verdict is only valid for the box
  heights it was measured against — re-measure after anything that changes heights (vocabpar in
  particular). Prefer it to `\newpage`; Lesson 1.0's Hook is the one deliberate hard break.
- **Palette — forest-green based.** Primary accent `forest` (#1E5631) with `forestlight`,
  `forestbg` (pale green background), `forestmid`; secondary `navy` (#1F3A5F) with `navylight`,
  `sky`, `skymid` (the vocabulary box and related callouts); `goldacc` / `goldbg` / `hookbg`;
  `redbg` / `redacc`; `greenbg` / `greenacc`; `charcoal`, `slate`, `linegray`, `keyred`
  (#CC0000). Lesson-plan background aliases: `goldbox`, `forestbox`, `greenbox`, `redbox`. Bare
  `gold` is undefined — use `goldacc`/`goldbg`. The AP Statistics recolouring does not apply
  here: `navy` really is navy, and `\navyheader` does not exist — the deck header is
  **`\forestheader{Title}`** with `\sectionlabel[color]{LABEL}`.
- **Environments (`-boxes`):** plan boxes `skillbox[Title]{bg}` (breakable) and
  **`fixedskillbox[Title]{bg}` (exists here; unbreakable — Lesson at a Glance and the Warm-Up
  box)**, `teachernote[Title]` (in `-boxes`, optional argument); student boxes `objectivebox`,
  `learningtargetbox`, `vocabbox`, `hookbox`, `notesbox{Title}`, `practicebox` (no argument, title
  fixed as "Guided Practice"), `spiralbox`, `scenariobox[Title]{color}`, `headlinebox{color}`,
  `blurbbox[Title]{color}`, `extensionbox`, `tocbox`, `remindbox`, and `reflectionbox` (legacy —
  never in a new lesson); plus `work` and `steptable`. **`tierbox` does not exist** and there is
  no tiered instruction. `\componenttable` / `\componenttablekey` were ported additively from the
  statistics course and have no use in this one.
- **Fill-in helpers (`-article`):** `\blank{W}`, `\writeline`, `\writelines{n}` (**occupies n+1
  line slots** — it ends in `\\`; raising one is not free: on 1.3 a `{2}`→`{3}` raise pushed the
  blank to 3pp against a 2pp key), `\termblanklong{Term}` (bold forest term on its own line + two
  write-lines — the vocab style in use), `\termblank{Term}` (a **fixed-height row**, `\termrowheight`
  1.30cm, ported 2026-09-03; its key counterpart `\termans{Term}{def}` in `-key` fills the same
  height — used by the 1.2 pilot only), `\pageheader{Unit X, Lesson Y.Z}{Doc Type}`,
  `\namedateperiod` (cover and unit tests only), `\namepartnerperiod` (unused), and
  `\coverbanner{unit}{lesson}` (measures the title block and sizes the band — the 1.2 pilot; the
  skeleton cover still draws the fixed 1.16in TikZ band).
- **There is no `\answerspace`.** The shared skill's page-parity mechanisms list it; here a prose
  answer is `\writelines{n}` in the blank answered by **exactly `n` `\ansline{}`s** in the key,
  each under ~95 characters so it does not wrap. **Reach for `work` before `\writelines`** — on 1.2
  every apparent `\ansline` drift was a solve, fixed by 16 `work` blocks and zero `\writelines`
  changes. Set `n` from the key's true wrapped length, rebuild, and re-measure the **blank**.
- **`work`** takes no argument; its body is an amsmath `aligned` — one statement per line, `&`
  immediately before the relation, flush left, never wrapped in `\[ \]`/`align`; `\workrowsep` adds
  leading to both sides together. Not inside table cells. **`steptable` / `\step{lhs}{=rhs}{prop}`
  / `\steprel`** is the *printed*-solution counterpart (only column 3 differs blank vs. key); it is
  a chain rule, not for a list of independent statements, and has **no in-tree example** since the
  review unit was deleted 2026-08-20 — follow the spec in the shared `references/conventions.md`.
- **Vocab rows in the current shape — `\vterm{Term}` ↔ `\vtermans{Term}{def}`,** a fixed-height
  (2.0cm) row carrying the term label and **open writing space — no inline blank and no rule
  line** (the SAAR user correction of 2026-09-06: the rule line crowded the row), defined in the
  notes' own preamble (copy the block from `unit01/lesson04/notes/main.tex`; the key's
  `\vtermans` fills exactly the same height, definitions two lines at most). `\termrowheight` /
  `\termrowinset` are taken by the package, hence the local `\vrowheight`. `\termblank` /
  `\termans` (rule line, 1.30cm) remain in `shared/` for 1.2; `\termblanklong` / `\vocabans`
  for the 2026-09-01 lessons.
- **Vocab keys — the vocabpar fix (2026-09-01 lessons only).** `\termblanklong` opens with `\noindent` (a no-op
  mid-paragraph) and `\ansline` ends with `\dotfill` without ending the paragraph, so every notes
  key that mirrors a `vocabbox` defines, in its own preamble,
  `\newcommand{\vocabans}[2]{\par\noindent\textbf{\textcolor{forest}{#1:}}\\[1pt]\ansline{#2}\par}`
  (the `\par` on **both** ends is required) and uses it in place of each `\termblanklong`; the
  blank puts `\par\vspace{2pt}` before the first term. Fix it per lesson, **not in `shared/`** — a
  package change would re-flow every verified unit. `unit01/lesson00/notes{,_key}` is the
  reference. (`\termans` is the `-key` macro for `\termblank` rows; never redefine it.)
- **Draw order in TikZ figures:** shading drawn *before* `\numline` (or the axis) is painted over
  and disappears — axis first, then shading, then endpoint dots (open:
  `\draw[color, thick, fill=white] (x,0) circle (3pt)`; closed: `\fill[color] (x,0) circle (3pt)`).
- **The plan** loads `graphicx` with `\graphicspath{{images/}}` (`-article` does not load
  `graphicx`), `tabularx`, `multicol`, and defines `\TallMath` per document:
  `\newcommand{\TallMath}[1]{$\displaystyle #1\rule[-1.4em]{0pt}{3.2em}$}`. **The cover** loads
  `ltablex` + `\keepXColumns`; its `tocbox` table is four columns (`c l X r`) and **every row needs
  four cells** or the widths collapse. A prefab warm-up's thumbnail is
  `\includegraphics[page=1]{warmup/main}`; an authored warm-up compiles to `target/` and has no
  source PDF, so its spiral-review box stays text-only.
- **Keys** load `algebra2-key` in place of `-boxes`; `\ans{}`, `\ansline{}`, the `work` blocks,
  and (where needed) a local `\vocabans`. Correct multiple-choice options may also be tagged
  `\textcolor{keyred}{\textbf{$\leftarrow$ correct}}`.

- **The Main Ideas / Notes table** (legacy gradual-release lessons only) — `guidednotes`, `\mainidea`, `\notesprompt`, `probgrid` /
  `probgrid*`, `\pcell`, `\writespace`, `\labelbox`, `\stepnum` — is defined in
  `algebra2-boxes.sty` (ported from AP Statistics 2026-09-12; the commentary there is the
  reference; labels and step discs are set in `forest`). Traps: **inside a table cell `\\` ends
  the row** and spills the rest into the label column — break lines with `\par`; **a row cannot
  break across pages** — give the figure its own sub-row (a bare `\\`, then `& ...`) and put each
  grid row in its own sub-row, reopening as `probgrid*` (no top rule); **`\pcell`'s height is the
  answer space only**, below the statement, and an answer longer than it overflows silently. The
  key differs from the blank only in `-key` for `-boxes`, the vocabulary rows, `\blank`→`\ans`,
  and the answer argument of each `\pcell`, `\writespace`, `\labelbox`.

## 5. Lesson-plan section order

Title block (`\CourseName` over `\UnitNumberName \LessonNumberName`) → **Primary Objective /
Standards (2023 VA SOL) / Lesson model** (a `tcolorbox`, `forestbg`/`forest`; the one-paragraph
slides-first statement, ending with the lesson's **Homework source**) → **Priority Ideas &
Skills** (`skillbox{goldbox}`, two `tabularx` cells: skills | the *why*, **with the target
misconception stated explicitly**) → **Vocabulary, Concepts & Theorems — one definition frame
each** (`skillbox{sky}`, worded exactly as the deck prints them) → **Lesson at a Glance**
(`fixedskillbox{forestbg}`, Phase / Min / Students / Teacher for **5 / 40 / 5 / 10**) →
**Warm-Up (5 min, on the slides)** (`skillbox{forestbg}`: the items, what each rehearses, the
handoff into the first definition) → **The Lesson — definition, example, now you try (40 min)**
(`skillbox{forestbg}`, `multicols{2}`, one paragraph per cycle in deck order: what to point at on
the definition's display, the example and where students go wrong, the Now-you-try **with its
answer**, how long to let them work before the reveal; the crux cycle named) → **Wrap-up (5
min)** → **Homework — scored, started in class, due the first class after two study halls**
(`skillbox{goldbox}`: the source, the items or the DeltaMath set, the formative check's sort, the
**Preview**) → **Watch For** (`skillbox{redbox}`, keyed to Now-you-try and homework item numbers,
plus cold-call prompts) → **Teacher Notes — two:** `[Slides]`, `[Homework]` (a DeltaMath lesson
keeps the Homework note: what the set covers and its formative item). **This is the only place
teacher prose goes.**

Plans from 2026-09-07 → 2026-09-24 use the gradual-release order (Warm-Up box, Guided Notes &
Practice, spoken Debrief, Close & Start Homework, three teacher notes, 5/35/10/10); plans from
2026-09-01 → 2026-09-06 the four-section order; earlier plans EFFL or Hook / Explicit Instruction
/ Tiers. All are legacy: regenerate, never patch.

## 6. Unit-level and course-level assessments

A unit holds **`tests/`** (`practice_test/` — the study copy students keep — and `actual_test/`;
`include ../../shared/tests.mk`; its `drop` target publishes the *practice* test to
`sample_test/main.pdf`), **`test_keys/`** (`practice_test_key/`, `actual_test_key/`;
`shared/test_keys.mk`; `drop` publishes the practice key to `sample_test_key/main.pdf`), the two
`sample_test*/` drop-in dirs (merged into the unit student / key packets by `shared/unit.mk`), and
**`unit_cover/`** — the LaTeX unit overview page that leads both unit packets. **The actual test and
its key are never merged into any packet** — they stay out of student hands. The scaffolder lays
all of this down the first time a unit is created (`--tests` re-runs it idempotently; `--no-tests`
skips it). Build: `make -C unitXX/tests all && make -C unitXX/test_keys all` **before** the unit
packet, so the prefab exists when `unit.mk` merges it.

Test structure: `\pageheader{Unit X: <Title>}{...}` + `\namedateperiod` (**tests are exempt from
namestrip** — taken in a testing setting, not stapled behind a cover); a local `\parthead{Part …}`
macro drawing a `headlinebox{forest}` divider; parts for vocabulary, multiple choice, short
answer / computation, extended response, with `\vspace` work room. The practice test opens with a
`remindbox` saying it mirrors the real test in format and ideas with different numbers; the actual
test has the same parts and difficulty, different numbers and contexts, and no such box. Keys mirror
their blanks (swap `-boxes` for `-key`), tag correct options, and put extended-response scoring in a
`teachernote`. Keep practice and actual parallel so the practice test is honest preparation; the
practice test and its key must be the same number of pages. **Unit 1's tests (regenerated
2026-09-16) are the reference:** 12pt, no vocabulary part, five skill parts (A–E, 100 pts), and a
body **byte-identical** in blank and key — answers live only in a preamble-defined
`\slot{width}{answer}` (a fixed-width underline, filled in the key), `\opt`/`\optok` (the key
marks the correct choice with a red arrow of zero width), and `work` blocks, so neither file can
drift. The key carries no `teachernote`. All four PDFs are 4pp.

**The unit study guide — `unitXX/study_guide/` (added 2026-09-14, user direction).** A
**reference sheet, not a problem set**: at 10pt, two pages, it carries for each lesson in the unit
a compact two-column table of vocabulary, forms, and the facts to know, closed by that lesson's
**target misconception stated as a caution** (`Watch out:`), and ends with a row of small
pre-drawn graphs the student must recognise on sight. It has **no problems and therefore no
key** — the practice test is the problem set. `shared/unit.mk` builds it exactly the way it
builds `unit_cover` (no `Makefile` of its own; `make -C unitXX study_guide`), and merges the same
PDF into **both** the student and the key packet, immediately before the sample test, so packet
alignment is unaffected. **No `\namedateperiod`** — it is neither a lesson cover nor a test.
Layout traps found authoring Unit 1's: a `tabularx` cannot be hidden inside a `\newenvironment`
(its body scanner needs a literal `\end{tabularx}`), and a column spec cannot be an ordinary
macro (use `\newcolumntype`). `unit01/study_guide` is the reference.

**Binder covers were removed (2026-08-22)** — `shared/cover.py`, every `binder_cover/` dir, and
the `unit.mk` hooks are gone; unit covers are designed outside the build and printed separately.
Never rebuild that feature; `unit_cover/` is unaffected and is not the same thing.

**Course level:** the **Mid-Year Exam sits in Week 16 (early January) and is cumulative over
Units 1–4** (resolved 2026-08-23, `COURSE_PLAN.md` §5–§6); a final exam follows Unit 7. Neither is
authored in the tree yet — `spec/` holds All Things Algebra models for both, usable as models, not
for redistribution. `COURSE_PLAN.md` §8 lists the cleanup deferred until Units 6–7 and the finals
are done (a home for `A2.EI.2c`; the vocabpar retrofit into Units 2–3).

## 7. Legacy shapes and regeneration

Recognize the shape by the component directories and the plan's section titles:

| Shape | Has | Lessons |
| --- | --- | --- |
| **current — slides-first** (2026-09-25) | no `warmup/`, no `notes/`; a deck with definition / example / Now-you-try cycles and `\reveal`; `homework{,_key}` generated, prefab, or absent (DeltaMath online); cover with **two** rows; plan 5/40/5/10 with two teacher notes | `unit02/lesson02` — the **pilot** (2026-09-25, homework = DeltaMath printed), pending user review; once approved it becomes `reference_lesson` |
| **gradual-release** (two-section, 12pt, 2026-09-07; `guidednotes` notes from 2026-09-12) | 12pt `warmup` + `notes` (vocab + hook, ONE `guidednotes` table + Guided Practice) + homework 2pp with the due-date `remindbox`; cover with three rows; 11-frame deck; plan 5/35/10/10, three teacher notes | `unit01/lesson04`, `unit02/lesson00`, `unit02/lesson01`; `unit01/lesson02` is its pilot (5/34/8/13) |
| **four-section interim** (2026-09-01) | 10pt `notes/` with an `objectivebox`, four numbered sections, and an *Individual Practice* `scenariobox`; 10pt homework with an `extensionbox`; plan 5/20/15/10/10 with four teacher notes | `unit01/lesson00`, `01`, `03`, `05` |
| **EFFL / group-activity** (2026-08-19 → 08-31) | `experience/` or `activity/` without `exit_ticket/` | none left |
| **pre-EFFL legacy** | `activity/` + `exit_ticket/` (+ keys), tiered activity, plan order Hook / Explicit Instruction / Tiers, 10pt warm-up; in Units 3–7 also teacher notes in the keys and `\namedateperiod` on every component (Unit 2 had both retrofitted 2026-07-30) | **36 lessons: `unit02/lesson02`–`lesson07`, and all of units 03–07** |

The build accepts all of them (`STUDENT_ORDER` still lists `warmup`, `notes`, `experience`,
`activity`, `exit_ticket`). When asked to touch an older lesson, **regenerate it whole in the
slides-first shape rather than patching** — ask first, and ask for its homework source (§2). The
content mapping, from any older shape:

| From | Becomes |
| --- | --- |
| the warm-up page | the warm-up frame (2–3 items, answers in `\reveal`) |
| the vocab box and each notes section / row / QuickNotes box | a **definition** frame per term, then that section's worked example as the **Example** frame |
| the notes' own problems, Guided Practice parts, Individual Practice, activity tiers, exit ticket | the **Now you try** problems — one cycle per idea, the crux last |
| hook, debrief, close | the targets frame, the wrap-up frame, and the homework frame |
| `homework` (+ its extension, cut) | the **generated** homework, the §1 spec — or dropped for DeltaMath |

Mechanically:

1. `git rm -r` every component dir but `cover` and `slides` — `warmup{,_key}`, `notes{,_key}`,
   `activity{,_key}`, `experience{,_key}`, `exit_ticket{,_key}` — and `homework{,_key}` too
   unless the source is *generated* (rewrite it) or *DeltaMath printed* (replace with the prefab).
2. Write the deck fresh from `templates/lesson/slides.tex`, cycles on one context, every
   Now-you-try answer in `\reveal`.
3. Rewrite the cover from `templates/lesson/cover.tex`: two rows, targets in the formal
   vocabulary, *Keep in Mind* matching the wrap-up frame.
4. Rebuild the plan from `templates/lesson/lesson_plan.tex` (5/40/5/10, §5 order, two teacher
   notes); apply the due-date wording of §2.
5. Namestrip (`namestrip.py`), then boxguard (§8).
6. Delete stale stamps — `rm -rf .stamps/unitXX/lessonYY target/unitXX/lessonYY` — or `make` skips
   a sibling whose PDF was cleaned and `pdfunite` fails on the missing file.

Finish with the evidence per lesson: `make -C unitXX/lessonYY all` exits 0; the homework is the
same page count as its key (2/2) when generated; **the handout deck has no answer in it** —
`pdftotext target/unitXX/lessonYY/slides_handout/main.pdf - | grep -c Check` is 0 (the *Check*
block title appears only inside `\reveal`); and the projected deck has more pages than the
handout deck by exactly the number of reveals. Then update `COURSE_PLAN.md`.

**Scoreboard (2026-09-25):** 44 lessons. **1 slides-first — the pilot `unit02/lesson02`**, awaiting user review. 4 gradual-release
(`unit01/lesson04`, `unit02/lesson00`, `unit02/lesson01`, pilot `unit01/lesson02`); 4
four-section interim (`unit01/lesson00`, `01`, `03`, `05`); 36 pre-EFFL legacy
(`unit02/lesson03`–`lesson07` and every lesson of Units 3–7; Units 3–7 still hold teacher notes
in 144 `_key` files and name rows on 300 non-cover components). Every lesson has a deck. Unit 6's
lesson 6.5 and Units 6–7's tests are skeletons; 7.1–7.6 are not scaffolded. Convert lesson by
lesson as they are taught, rebuilding the unit packet each time — never the whole course in one
pass.

## 8. Review order

When reviewing or converting a lesson: **shape → deck → teachernotes → namestrip → work rule →
boxguard** (plus **vocabpar** on a legacy lesson still carrying a `vocabbox`), then build and
prove page parity and the answer-free handout. Boxguard goes **last** because it repairs the
pagination the earlier conventions disturb. It is opt-in and nothing detects a missed one — `make`
exits 0 either way — so check the rendered pages (`pdftoppm -r 60 -png`). Per user decision there
is **no bulk sweep** for any of these: fix them lesson by lesson as review finds them.
Retrofittable names: **boxguard**, **namestrip**, **vocabpar**, **work rule**, **teachernotes**,
plus the shared skill's **deck** and **shape**.
