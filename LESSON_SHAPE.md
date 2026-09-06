---
course: Algebra 2
prefix: algebra2
meeting_length: 60
reference_lesson: unit01/lesson01
components: [cover, warmup, notes, homework, slides]
keyed: [warmup, notes, homework]
one_page: [warmup]
doc_titles:
  warmup: Warm-Up
  notes: Guided Notes
  homework: Homework
  activity: Group Activity
  exit_ticket: Exit Ticket
note_labels:
  warmup: Warm-Up
  notes: Guided Notes
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

**Every lesson follows a traditional gradual-release model — I do, we do, you do alone.** A
warm-up activates prior knowledge; **Guided Notes** build and name the vocabulary with the class on
one worked context and end in a **Guided Practice** box (the "we do"); an **Individual Practice**
block on the notes' last page is the "you do" — three problems, worked silently and alone; a
**debrief** consolidates and surfaces errors; the **homework** page is started in class and
finished at home. This replaced the Math Medic "experience first, formalize later" (EFFL) model on
2026-08-31 (user direction — "the students have revolted"); the group activity was cut the same
day ("just cut the group activity … add an 'individual practice'") and the shape confirmed
course-wide on 2026-09-01.

| Phase | Minutes | Component |
| --- | --- | --- |
| Warm-up | 5 | `warmup` (**12pt**) |
| Guided notes, incl. Guided Practice (I do / we do) | 20 | `notes` |
| Individual practice, silent (you do alone) | 15 | `notes` — its last page |
| Debrief — the board, in a second colour | 10 | — (in the plan only) |
| Close & start the homework in class | 10 | `homework` |

**`warmup`** — 5 min, **one page at 12pt** (user direction, 2026-08-31 — larger type than the rest
of the packet, deliberately; still one page blank and keyed). Three quick spiral-review items
rehearsing exactly the prior skills the lesson leans on; the last item ends on the question notes
section 1 answers, deliberately left hanging. May be a prefab PDF.

**`notes` — *Guided Notes* — is the in-class centrepiece: 4 pages at 10pt.** `objectivebox` →
`vocabbox` (5–7 `\termblanklong` entries filled as each term is built) → `hookbox` (the 60-second
context whose numbers every worked example reuses) → **four numbered `notesbox` sections** on
**one worked context** — section 1 the defining idea and general form; section 2 the second
procedure (often a feature / how to find it / what it means `tabularx`); **section 3 normally the
target misconception**, the two things students conflate side by side in a two-column `tabularx`
closed by a gold caution `tcolorbox` (`colback=goldbg, colframe=goldacc`) giving a case where the
two answers *disagree*; section 4 the edge cases — → `practicebox` (the "we do": one new example,
all features at once, in a `work` block) → **Individual Practice**: `\boxguard[22]` then
`scenariobox[Individual Practice --- On Your Own]{navy}` on its own clean page, **three problems**
that are the three *shapes* (or directions) of the skill, **crux last** (usually ending in a "a
classmate says … what did they miss?" `\writelines{2}`), every solve in a `work` block, ~5 minutes
each. There is no separate component for it and no new environment in `shared/`.

**`homework`** — the "you do alone" that continues at home. **2 pages, and 2pp is a ceiling** — a
seventh item gets cut, never spilled onto a third page. A `Practice` `notesbox` of **~6 items
spanning the whole standard**, in the canonical spread: the core procedure off a *rule*; a
deliberate *contrast pair* (the target misconception) closing with a "why?"; the same procedure
off a *table or graph* (so all three representations appear); the *special case* and its
boundary; a *model* in a fresh context with a `work` block and an interpret-the-answer follow-up;
and an **SOL-style multiple-choice item as the formative check**. Then an `extensionbox` (the
procedure run backwards plus a "a classmate claims … explain why that cannot happen" item) and a
closing `spiralbox` previewing the next lesson.

**`cover`** — full-bleed forest banner (course name, unit, `Lesson <id>  <title>`),
`\namedateperiod` (the only place it appears), `learningtargetbox` of "I can…" targets **using the
formal vocabulary in bold** (there is nothing to withhold — the notes name every term before the
practice uses it), a `tocbox` with **three scored rows in packet order** (Warm-Up · Guided Notes
"ending in *Guided Practice* and *Individual Practice*" · Homework) plus a Total row, and a
`remindbox` (*Keep in Mind*) that is a **content** summary — the lesson's definitions and the
distinction it turns on, never the process.

**`slides`** — the Beamer deck, **11 frames** in the gradual-release flow: title → learning
targets (naming the vocabulary, plus a "how today runs" block with the 5/20/15/10/10 split) →
warm-up (ending in a "hold on to this" block) → hook → **four notes frames**, one per numbered
section, matching the packet exactly (the misconception frame gets a `block` with the case where
the two answers disagree; the last ends with the Guided Practice) → individual-practice launch
(the three problems, the one-sentence rule, "look up the page, not at your neighbour", the
early-finisher move) → debrief (the plan's four numbered takeaways) → close (what changed today, a
**Homework — start it now** block, a one-line preview). Reference decks: `unit01/lesson03/slides`
and `unit01/lesson04/slides`.

**What this course does not have — do not re-add any of it:**

- **No group activity.** Never scaffold, author, or restore `activity/`; the "you do" is the
  Individual Practice block inside the notes.
- **No exit ticket.** The debrief closes the lesson; the formative check is the homework's last
  item (the SOL-style multiple-choice problem) and the plan says how to sort responses.
- **No tiers.** The old Tier R / Approaching / Extension structure does not come back — one
  document, one version, for the whole class.
- **No `experience` component, no *QuickNotes*, no *Check Your Understanding*, no spoiler rule.**
  Anything still saying *Experience & Formalize* is a lesson not yet converted, not a pattern to
  copy.
- **No debrief component.** The debrief is a 10-minute phase of the plan in which the class
  corrects its own Individual Practice in a second colour while the teacher works all three
  problems on the board.
- **No `\answerspace`.** Open responses use `\writelines{n}` (see §4).

**Out of scope for the course** (no lessons): conic sections, sequences & series, probability &
statistics, trigonometry, and linear systems / linear programming.

**`unit01/lesson01` is the reference implementation** of this shape; 1.0 and 1.3–1.5 follow it.
Mirror its preamble, box usage, pacing, and tone; the live lesson overrides every document, this
one included. **`unit01/lesson02` is a pilot of a different shape** (2026-09-03 — the AP Statistics
1.4 spec: every student component 12pt, two-section notes ending at Guided Practice, the homework
*is* the individual practice, 5/34/8/13, three teacher notes) and is **pending the user's review of
the printed result**. Until the user adopts it course-wide, it is not the reference for anything;
see §7.

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
  its Homework teacher note, and the deck's close frame. Lesson 1.2 says so today; 1.0, 1.1, 1.3–1.5
  and the skeletons in `templates/lesson/` (`cover.tex`, `lesson_plan.tex`, `slides.tex`) still
  print "due next class" and pick up the wording when they are regenerated — **no bulk sweep**. When
  you author from a skeleton, replace the phrase.
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
- **Sizes.** Every student component is `\documentclass[10pt]{article}` + `algebra2-article` +
  `algebra2-boxes` **except the warm-up, which is `[12pt]`**; the plan is 10pt. (The shared skill's
  "every student component is 12pt" invariant does **not** hold here — the 1.2 pilot is all-12pt,
  but that is the pilot, not the course.) Budgets: warm-up 1p · notes 4pp · homework 2pp (ceiling).
- **`\boxguard`** (`-boxes`, `\Needspace`) defaults to 16 lines; at 10pt counts run **16–26**
  (`20–26` on a `notesbox`, `[22]` before the Individual Practice box, `[30]` when a box opens
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
- **Vocab keys — the vocabpar fix.** `\termblanklong` opens with `\noindent` (a no-op
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

## 5. Lesson-plan section order

Title block (`\CourseName` over `\UnitNumberName \LessonNumberName`) → **Primary Objective /
Standards (2023 VA SOL) / Lesson model** (a `tcolorbox`, `forestbg`/`forest`; the one-paragraph
gradual-release statement) → **Priority Ideas & Skills** (`skillbox{goldbox}`, two `tabularx`
cells: skills as things the student does | the *why*, **with the target misconception stated
explicitly**) → **Vocabulary, Concepts & Theorems** (`skillbox{sky}`, term/definition `tabularx`,
`\TallMath` for tall formulas — the terms the notes' `vocabbox` builds) → **Lesson at a Glance**
(`fixedskillbox{forestbg}`, Phase / Min / Students / Teacher for **5 / 20 / 15 / 10 / 10**) →
**Warm-Up — Activate Prior Knowledge & Spiral Review** (`fixedskillbox{forestbg}`: the ~3 items,
what each rehearses, what to debrief aloud, how it hands off into notes section 1, and the sentence
"this page is set at 12pt") → **Hook** (`skillbox{forestbg}`: the 60-second context, the questions
with answers in parentheses, the idea to land; its numbers are the notes' numbers) → **Guided Notes
— the Lesson (20 min)** (`skillbox{forestbg}` in `multicols{2}`: one bold paragraph per numbered
section saying what to build and where the `work` blocks are, ending with the Guided Practice
paragraph) → **Individual Practice — On Your Own (15 min, silent)** (`skillbox{redbox}`: the
1-minute launch script; *What students do* — the three problems, why they are the three shapes,
which is the crux | *What the teacher does* — questions, cues, prompts keyed to problem numbers,
**never answers**; the early-finisher move; note names for the debrief) → **Debrief (10 min — what
goes on the board, in a second colour)** (`skillbox{forestbg}`: **exactly four things to land** —
problem 1 worked, the must-land moment pointed back to the notes' caution box, problem 2, problem
3 / the crux and what a wrong answer reveals; which item to cut if short and which two to protect)
→ **Active Monitoring — Watch For** (`skillbox{redbox}`, keyed to notes / Individual Practice /
homework item numbers, plus cold-call prompts) → **Reinforcement & Extension** (`skillbox{goldbox}`:
the homework's ~6 items and extension itemized, the **DeltaMath override** sentence, the
**Preview** of the next lesson) → **Teacher Notes — four, in packet order:** `[Warm-Up]`,
`[Guided Notes]`, `[Individual Practice]`, `[Homework]` — pacing splits that actually fill each
phase's minutes, must-land moments, common slips, the early-finisher move, how to sort the
formative check. **This is the only place teacher prose goes.**

`[Individual Practice]` belongs to no component, so `movenotes.py` never produces it — author it by
hand when converting a lesson. Legacy plans carry `[Group Activity]`, `[Exit Ticket]`, or
`[Experience \& Formalize]`; all go when the lesson is regenerated. Plans from 2026-08-19 →
2026-08-31 use the EFFL order (Experience & Formalize / Debrief: Formalize / Application / Check Your
Understanding); earlier plans use Hook / Explicit Instruction / Tiers. Both are legacy: regenerate,
never patch.

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
practice test and its key should be the same number of pages (Unit 1's are 3pp vs. 4pp today — a
known, pre-existing mismatch).

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
| **current** (gradual release, 2026-09-01) | `notes/` + `homework/` only; 12pt warm-up; plan has an *Individual Practice* box and four teacher notes | `unit01/lesson00`, `01`, `03`, `04`, `05` — the target |
| **12pt pilot** (2026-09-03) | every student component 12pt; `\coverbanner`; `\termblank`/`\termans`; two-section notes ending at Guided Practice; plan 5/34/8/13 with three notes | `unit01/lesson02` — **pending user review; not the course shape** |
| **group-activity interim** (2026-08-31) | `activity/` without `exit_ticket/`; plan has a Group Activity box | none left (1.0 was converted 2026-09-01) |
| **EFFL** (2026-08-19 → 08-31) | `experience/` + `experience_key/`; *Experience & Formalize* / *QuickNotes* / *Check Your Understanding* / the spoiler rule | none left |
| **pre-EFFL legacy** | `activity/` + `exit_ticket/` (+ keys), tiered activity (Tier R / Approaching / Extension), plan order Hook / Explicit Instruction / Tiers, 10pt warm-up; in Units 3–7 also teacher notes in the keys and `\namedateperiod` on every component (Unit 2 had both retrofitted 2026-07-30) | **units 02–07, all 38 lessons** |

The build accepts all of them (`STUDENT_ORDER` still lists `experience`, `activity`,
`exit_ticket`). When asked to touch a legacy lesson, **regenerate it in the current shape rather
than patching** — ask first. The content mapping:

| From the group-activity shape | From EFFL | From the pre-EFFL legacy shape | Becomes |
| --- | --- | --- | --- |
| `notes` sections 1–4 | QuickNotes box | `notes` (drop the tiers language) | the four numbered sections of **Guided Notes** |
| the activity's crux items, chosen three | Activity + Application, condensed to three | Tier A/E items, three of them | **Individual Practice** — three problems inside the notes |
| `homework` | Check Your Understanding | `homework` + `exit_ticket` | the **Homework** page + `extensionbox` + `spiralbox` |

Mechanically:

1. `git rm -r` the `activity{,_key}`, `experience{,_key}`, or `exit_ticket{,_key}` dirs.
2. Write `notes` / `notes_key` and `homework` / `homework_key` fresh from the skeletons, on one
   worked context, with the Individual Practice block on the notes' last page and the SOL-style
   formative check last on the homework; fold the exit ticket's item into the homework.
3. Set the warm-up to 12pt (still one page, blank and key).
4. Rewrite the cover's packet table to the **three** scored rows and re-voice its learning targets
   with the formal vocabulary; the *Keep in Mind* box becomes a content summary.
5. Rebuild the plan around the 5/20/15/10/10 table in the §5 order, with **four** teacher notes
   (`movenotes.py` lifts the component-keyed ones out of the keys; write `[Individual Practice]`
   by hand); apply the due-date wording of §2.
6. Rewrite the deck to the 11-frame order of §1.
7. Namestrip the components (`namestrip.py`), then vocabpar, then boxguard (§8).
8. Delete stale stamps — `rm -rf .stamps/unitXX/lessonYY target/unitXX/lessonYY` — or `make` skips
   a sibling whose PDF was cleaned and `pdfunite` fails on the missing file.

Finish with the evidence per lesson: `make -C unitXX/lessonYY all` exits 0, warm-up 1/1, and every
component's page count equals its `_key`'s, compared on the compiled components, not the padded
packets. Then update `COURSE_PLAN.md`.

**Scoreboard (2026-09-06):** 44 lessons. **5 in the current shape** (`unit01/lesson00`, `01`,
`03`, `04`, `05`); **1 in the 12pt pilot** (`unit01/lesson02`); **38 pre-EFFL legacy** (every lesson
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
