---
course: Algebra 2
prefix: algebra2
meeting_length: 60
reference_lesson: unit01/lesson04
components: [cover, warmup, notes, homework, slides]
keyed: [warmup, notes, homework]
one_page: [warmup]
doc_titles:
  warmup: Warm-Up
  notes: Guided Notes \& Practice
  homework: Homework
  activity: Group Activity
  exit_ticket: Exit Ticket
note_labels:
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

Two frontmatter notes. `activity` and `exit_ticket` appear in `doc_titles` **only so an older
lesson can be rebuilt by name** — neither is a default and neither belongs in a new or
regenerated lesson. `experience` is deliberately absent from `doc_titles` and has no skeleton, so
the scaffolder refuses it: it was the EFFL centrepiece and is never scaffolded again (its
`note_labels` entry exists only so `movenotes.py` can title a note lifted from a legacy key).

## 1. The lesson shape

**Algebra 2 is a function-family course** for a secondary-school audience: after a foundations
unit, each unit is built around one function type (linear → quadratic → polynomial → rational →
radical → exponential → logarithmic), and **every unit opens with a Lesson 0, "Characteristics of
____ Functions"** — `lesson00`, id `X.0`; content lessons keep 1-based numbers. Author every
component to build **graph-reading fluency**: study how each new function type *behaves* before
manipulating and solving it. The recurring move in every component is **read/interpret → justify**
("what does this feature mean here, and how do you know?").

**Every lesson follows a traditional gradual-release model — I do → we do → you do — on the
stats/SAAR two-section shape (piloted on 1.2 on 2026-09-03; adopted as the course shape when the
user applied it to 1.4 on 2026-09-07: "larger font for the cover, guided notes, and homework;
notes page 1 is vocab and hook, no primary-objective box; no extension boxes on the homework; no
individual practice section in the notes — the homework is the individual practice").** A warm-up
activates prior knowledge; **Guided Notes & Practice** name the vocabulary as each term is built,
deliver the instruction in **exactly two long sections** on one worked context, and end in a
**Guided Practice** box worked together with students holding the pen; a whole-class **debrief is
spoken**; and **the period ends with students starting the homework in class, alone** — the
homework *is* the individual practice. There is no practice set at the end of the notes.

| Phase | Minutes | Component |
| --- | --- | --- |
| Warm-Up | 5 | `warmup` |
| Guided Notes & Practice — I do / we do row by row (~20) + Guided Practice together (~15) | 35 | `notes` |
| Debrief — whole class, spoken | 10 | — (in the plan and the deck only) |
| Close & start the homework, alone, teacher circulating | 10 | `homework` |

**The phases total 60 minutes — `\MeetingLength`.** 5 / 35 / 10 / 10 is the SAAR allocation for
the same 60-minute period (user decision there, 2026-09-06); the 1.2 pilot's 5 / 34 / 8 / 13 is
superseded. Author the table exactly so; if a phase does not fit, cut content — do not let the
table lie, and do not edit `shared/`.

**`warmup`** — 5 min, **one page at 12pt**, blank and key. Three quick spiral-review items
rehearsing exactly the prior skills the lesson leans on; the last item ends on the question notes
section 1 answers, deliberately left hanging. May be a prefab PDF.

**`notes` — *Guided Notes \& Practice* — is the in-class centrepiece (2026-09-12 shape, ported
from AP Statistics).** `\pageheader{…}` → `vocabbox` (5–6 fixed-height `\vterm` rows, filled *as each term is
named*) → `hookbox` (the 60-second context whose numbers every row reuses, ending on a circle-one vote **left unresolved**) → **one two-column *Main Ideas / Questions* | *Notes* table**
(`guidednotes` in `algebra2-boxes.sty`), 3–4 pages at 12pt. **There is no `objectivebox`** — the
cover carries the targets. Each **row** is one idea on the one worked context: a short label on
the left (`\mainidea[lead]{Label}`); on the right one or two **complete printed sentences** (the
definition or the general form, read — never a sentence with words punched out), **one large
pre-drawn display** (a graph, a table, the two things students conflate side by side) the
student reads or annotates with `\labelbox`, then a bold prompt and a **two-across grid of a few
numbered problems** (`probgrid` + `\pcell`, **2–3 cm of work room each**, algebra in `work`
blocks); a procedure uses `\stepnum{n}`, the sentence to land an *In your own words*
`\writespace`. Three or four instruction rows — the last carries the **target misconception as
problems**, the case where the two answers *disagree* — then the **Guided Practice row** (`\mainidea[Guided practice]{Title}`, one new example, all features at once, worked *with* the class, four problems). **The notes end there.** **Density rules:** a `\blank{}` only where a single word or number *is* the answer (a table to fill, a display to name), never mid-sentence, a handful per lesson; 12–19 problems, two across, never three; every row a picture; the plan names, by problem number, which problems the teacher works, which is the trap, which is the crux. The hook plants the crux, the first rows earn it, the last instruction row settles it, and the Guided Practice tests it again on new ground.
Lessons authored before 2026-09-12 use the boxed notes (`notesbox` sections + `practicebox`);
convert them by the recipe in `templates/lesson/components.md` when you touch them.

**`homework`** — **12pt, 2 pages, and 2pp is a ceiling** — a seventh item gets cut, never
spilled onto a third page. It **is the individual practice**: opens with a `remindbox` (*"This is
your graded homework. Your packet with completed homework is due the first class after two study
halls. I will announce the due date in class and on TurtleNet."* plus the lesson's one-sentence
rule, identical in blank and key), then a `Practice` `notesbox` of **~6 items spanning the whole
standard** (`\small`), in the canonical spread: the core procedure off a *rule*; a deliberate
*contrast pair* (the target misconception) closing with a "why?"; the same procedure off a *table
or graph* (so all three representations appear — and where the skill runs backwards, "write its
rule"); the *special case* and its boundary; a *model* in a fresh context with a `work` block and
an interpret-the-answer follow-up; and an **SOL-style multiple-choice item as the formative
check**. Split it `notesbox{Practice}` / `notesbox{Practice, continued}` with a `\newpage` so no
item breaks across a page, and close with a `spiralbox` previewing the next lesson. **No
`extensionbox`** (retired with this shape; the environment still exists in `algebra2-boxes.sty` —
never author one).

**`cover`** — 12pt, `\coverbanner{Unit N \quad Title}{Lesson N.M \quad Title}` (measures the
title block and sizes the forest band to it), `\namedateperiod` (the only place it appears), a
`learningtargetbox` of "I can…" targets **using the formal vocabulary in bold**, a `tocbox` with
**three scored rows in packet order** (Warm-Up · Guided Notes & Practice · Homework) plus a Total
row, and a `remindbox` (*Keep in Mind*) that is a **content** summary — the lesson's definitions
and the distinction it turns on, never the process. `\small` inside the boxes.

**`slides`** — the Beamer deck, **11 frames**: title → learning targets (naming the vocabulary,
plus a "how today runs" block with the 5/35/10/10 split) → warm-up (ending in a "hold on to this"
block) → hook (the vote, **left unresolved**) → **four notes frames**, two per section (1a/1b,
2a/2b — the crux frame flagged `\sectionlabel[redacc]{}` with a `block` giving the case where the
two answers disagree) → Guided Practice (the lettered parts and "the questions I will ask") →
debrief (the plan's four numbered takeaways plus a "say it without the notes" block) → close &
start the homework (what changed today, a **Homework — scored, due the first class after two study
halls** block, a one-line preview). Reference decks: `unit01/lesson02/slides` and
`unit01/lesson04/slides`.

**What this course does not have — do not re-add any of it:**

- **No group activity.** Never scaffold, author, or restore `activity/`.
- **No exit ticket.** The formative read comes twice — circulating during Guided Practice, and
  again during the supervised homework start — and the plan says what to do with each of three
  piles of what the teacher sees.
- **No independent practice set in the notes, no *Individual Practice* `scenariobox`, no
  `objectivebox` in the notes, no `extensionbox` anywhere, no `reflectionbox`.** The debrief is
  spoken; the individual practice is the homework. (The 2026-09-01 shape had a 15-minute
  Individual Practice block on the notes' last page and four short sections; this shape retired
  it on 2026-09-07.)
- **No tiers.** One document, one version, for the whole class.
- **No `experience` component, no *QuickNotes*, no *Check Your Understanding*, no spoiler rule.**
- **No debrief component.** The debrief is a 10-minute spoken phase of the plan.
- **No `\answerspace`.** Open responses use `\writelines{n}` (see §4).

**Out of scope for the course** (no lessons): conic sections, sequences & series, probability &
statistics, trigonometry, and linear systems / linear programming.

**`unit01/lesson04` is the reference implementation** of this shape (regenerated 2026-09-07);
`unit01/lesson02` is the pilot it grew from (still 5/34/8/13, `\termblank` rows, and an
`objectivebox` — bring it in line when it is next touched). Mirror 1.4's preamble, box usage,
pacing, and tone; the live lesson overrides every document, this one included. **1.0, 1.1, 1.3,
and 1.5 are on the 2026-09-01 four-section shape** (10pt, Individual Practice block, extension
box) and are regenerated lesson by lesson — see §7.

## 2. Grading and homework policy

- **Every row of the cover's packet table is scored** — Warm-Up, Guided Notes, Homework each take a
  `\blank{1.2cm}`; **nothing prints `NA`**. There is no debrief row (a phase, not a component) and
  no activity row.
- **Homework is an in-repo component and it IS scored.** Every lesson generates one, because
  DeltaMath does not cover all of this course's content. Where it does, the teacher **overrides per
  lesson** and assigns a DeltaMath set instead, so each plan's *Reinforcement & Extension* box
  carries a **DeltaMath override** sentence saying whether the content is well covered there and
  what set to swap in. Paper is the default; never assume the override.
- **The homework is started in class** in the last 10 minutes — launch item 1 aloud, then
  circulate — and finished at home.
- **Due date — course policy of record (user direction, 2026-09-03, recorded in the `COURSE_PLAN.md`
  Status block): homework is *always* due the first class after two study halls — never "due next
  class."** The wording, where it renders: the cover's homework row, the homework page's own
  remind box (*"Your packet with completed homework is due the first class after two study halls.
  I will announce the due date in class and on TurtleNet"*), the plan's Homework / Close boxes and
  its Homework teacher note, and the deck's close frame. Lessons 1.2, 1.3 and 1.4 say so today
  (1.3 and 1.4 regenerated 2026-09-07); 1.0, 1.1, 1.5 and the skeletons in `templates/lesson/`
  (`cover.tex`, `lesson_plan.tex`, `slides.tex`) still print "due next class" and pick up the
  wording when they are regenerated — **no bulk sweep**. When you author from a skeleton, replace
  the phrase.
- The homework's last item is the **formative check** (SOL-style multiple choice, four options; in
  the key the correct option is wrapped in `\ans{}` and the answer lines say which is right and why
  one distractor is wrong). The plan names the categories to sort responses into and how the next
  lesson opens for each.

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
  plan is 10pt and the deck 11pt. That is the frontmatter's `point_size: 12`. Budgets: warm-up 1p ·
  notes 4pp (the fixed page plan of §1) · homework 2pp (ceiling). 1.0, 1.1, 1.3, 1.5 are still
  10pt until regenerated.
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

- **The Main Ideas / Notes table** — `guidednotes`, `\mainidea`, `\notesprompt`, `probgrid` /
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
gradual-release statement: two sections, Guided Practice with the pen in students' hands, spoken
debrief, the homework is the individual practice) → **Priority Ideas & Skills** (`skillbox{goldbox}`,
two `tabularx` cells: skills | the *why*, **with the target misconception stated explicitly**) →
**Vocabulary, Concepts & Theorems — taught directly in the guided notes** (`skillbox{sky}`,
term/definition `tabularx`) → **Lesson at a Glance** (`fixedskillbox{forestbg}`, Phase / Min /
Students / Teacher for **5 / 35 / 10 / 10**) → **Warm-Up — Activate Prior Knowledge (5 min)**
(`fixedskillbox{forestbg}`, two minipages: *the three items and what each seeds* · *running it*,
ending with the 12pt sentence) → **Guided Notes & Practice — I do, then we do (35 min)**
(`skillbox{forestbg}`, `multicols{2}`: the hook and the vote, *I do* one paragraph per section
with minutes and where the `work` blocks are, *we do* the Guided Practice part by part, "the pen
must actually change hands", the circulating prompts, which two papers to pick for the debrief)
→ **Debrief — whole class, spoken (10 min)** (`skillbox{forestbg}`, `multicols{2}`: exactly four
things to land, the two things to demand aloud, what to cut if short) → **Homework — scored,
started in class, due the first class after two study halls** (`skillbox{goldbox}`: the six items,
the formative check's sort, the **DeltaMath override** sentence, the **Preview**) → **Watch For
(while circulating)** (`skillbox{redbox}`, keyed to notes / GP part / homework item numbers, plus
cold-call prompts) → **Close & Start Homework (10 min)** (`skillbox{goldbox}`: the launch, the
three piles, the "what changed today" sentence) → **Teacher Notes — three, in packet order:**
`[Warm-Up]`, `[Guided Notes \& Practice]`, `[Homework]`. **This is the only place teacher prose
goes.**

Legacy plans carry `[Individual Practice]`, `[Group Activity]`, `[Exit Ticket]`, or
`[Experience \& Formalize]`; all go when the lesson is regenerated. Plans from 2026-09-01 →
2026-09-06 use the four-section order (Individual Practice box, Debrief with four takeaways,
Reinforcement & Extension); earlier plans use EFFL or Hook / Explicit Instruction / Tiers. All are
legacy: regenerate, never patch.

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
| **current** (two-section, 12pt, 2026-09-07) | every student component 12pt; `\coverbanner`; notes = vocab + hook / section 1 / section 2 / Guided Practice, one page each, no `objectivebox`; homework 2pp with a due-date `remindbox` and no `extensionbox`; plan 5/35/10/10 with three teacher notes | `unit01/lesson04` — the target; `unit01/lesson02` is the near-identical pilot (5/34/8/13, `\termblank`, `objectivebox`) |
| **four-section interim** (2026-09-01) | 10pt `notes/` with an `objectivebox`, four numbered sections, and an *Individual Practice* `scenariobox`; 10pt homework with an `extensionbox`; plan 5/20/15/10/10 with four teacher notes | `unit01/lesson00`, `01`, `03`, `05` |
| **group-activity interim** (2026-08-31) | `activity/` without `exit_ticket/`; plan has a Group Activity box | none left (1.0 was converted 2026-09-01) |
| **EFFL** (2026-08-19 → 08-31) | `experience/` + `experience_key/`; *Experience & Formalize* / *QuickNotes* / *Check Your Understanding* / the spoiler rule | none left |
| **pre-EFFL legacy** | `activity/` + `exit_ticket/` (+ keys), tiered activity (Tier R / Approaching / Extension), plan order Hook / Explicit Instruction / Tiers, 10pt warm-up; in Units 3–7 also teacher notes in the keys and `\namedateperiod` on every component (Unit 2 had both retrofitted 2026-07-30) | **units 02–07, all 38 lessons** |

The build accepts all of them (`STUDENT_ORDER` still lists `experience`, `activity`,
`exit_ticket`). When asked to touch a legacy lesson, **regenerate it in the current shape rather
than patching** — ask first. The content mapping:

| From the group-activity shape | From EFFL | From the pre-EFFL legacy shape | Becomes |
| --- | --- | --- | --- |
| `notes` sections 1–4, folded two into one | QuickNotes box | `notes` (drop the tiers language) | the **two** long sections of **Guided Notes & Practice**, each in two moves |
| the activity's / Individual Practice's crux items | Activity + Application | Tier A/E items | the **Guided Practice** part that tests the misconception on new ground, and the homework |
| `homework` (+ its extension, cut) | Check Your Understanding | `homework` + `exit_ticket` | the **Homework** page — the individual practice — + `spiralbox`, no extension |

Mechanically:

1. `git rm -r` the `activity{,_key}`, `experience{,_key}`, or `exit_ticket{,_key}` dirs.
2. Write `notes` / `notes_key` and `homework` / `homework_key` fresh, mirroring `unit01/lesson04`,
   on one worked context, on the four-page plan of §1 (no `objectivebox`, two sections, Guided
   Practice alone on page 4) and the two-page homework with the due-date `remindbox` and no
   `extensionbox`; fold any exit-ticket / Individual Practice crux into the Guided Practice or the
   homework.
3. Every student component at 12pt (the warm-up still one page, blank and key).
4. Rewrite the cover at 12pt with `\coverbanner`, the **three** scored rows, learning targets in
   the formal vocabulary, and a *Keep in Mind* content summary.
5. Rebuild the plan around the 5/35/10/10 table in the §5 order, with **three** teacher notes
   (`movenotes.py` lifts component-keyed ones out of legacy keys); apply the due-date wording of §2.
6. Rewrite the deck to the 11-frame order of §1.
7. Namestrip the components (`namestrip.py`), then vocabpar, then boxguard (§8).
8. Delete stale stamps — `rm -rf .stamps/unitXX/lessonYY target/unitXX/lessonYY` — or `make` skips
   a sibling whose PDF was cleaned and `pdfunite` fails on the missing file.

Finish with the evidence per lesson: `make -C unitXX/lessonYY all` exits 0, warm-up 1/1, and every
component's page count equals its `_key`'s, compared on the compiled components, not the padded
packets. Then update `COURSE_PLAN.md`.

**Scoreboard (2026-09-07):** 44 lessons. **1 in the current shape** (`unit01/lesson04`) plus
**the pilot** (`unit01/lesson02`); **4 in the four-section interim** (`unit01/lesson00`, `01`,
`03`, `05`); **38 pre-EFFL legacy** (every lesson
of Units 2–7), none with a 12pt warm-up. Of those, **Unit 2's 8 lessons** were already
teachernote-migrated, namestripped, and boxguarded in the 2026-07-30 sweep (they keep their
`activity` / `exit_ticket` pairs and tiered plans); **Units 3–7's 30 lessons** are untouched —
144 `_key` files still hold teacher notes and 300 non-cover components still carry a name row.
Every lesson has a deck. Unit 6's lesson 6.5 and Units 6–7's tests are skeletons; 7.1–7.6 are not
scaffolded. Per `COURSE_PLAN.md` §8, Units 2–3 still carry the vocabpar defect. Convert lesson by
lesson or unit by unit as you review, rebuilding the unit packet each time — never the whole
course in one pass.

## 8. Review order

When reviewing or converting a lesson: **shape → deck → teachernotes → namestrip → vocabpar →
work rule → boxguard**, then build and prove page parity. Vocabpar changes box heights, so it goes
before boxguard; boxguard goes **last** because it repairs the pagination the earlier conventions
disturb (a guard can be needed on only one side — on 1.4 namestrip let the key's Guided Practice
box squeeze onto a page the blank still pushed). Boxguard is opt-in and nothing detects a missed
one — `make` exits 0 either way — so check the rendered pages (`pdftoppm -r 60 -png`). Per user
decision there is **no bulk sweep** for any of these: fix them lesson by lesson as review finds
them. Retrofittable names: **boxguard**, **namestrip**, **vocabpar**, **work rule**,
**teachernotes**, plus the shared skill's **deck** and **shape**.
