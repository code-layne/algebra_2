# Algebra 2 — Course Scope & Sequence

**Course:** Algebra 2

> **Status (2026-08-22):** **The course title is now just `Algebra 2`.** The teacher name and the
> school year were stripped from every surface that renders a title — all 44 lesson plans, all 44
> packet covers, all 44 deck title slides, `shared/cover.py`'s binder-cover title block, the
> `lesson-planning` skeletons/scaffolder/docs, and these planning docs. `\SchoolYear` was deleted
> outright and `new_lesson.py --year` is gone. See §7 "Course title" for the per-surface spec.
>
> **Binder covers are gone (2026-08-22).** `shared/cover.py`, both `binder_cover/` directories,
> and all of `unit.mk`'s binder plumbing were deleted — unit covers are designed in Claude Design
> now and printed on their own. See §7 "Binder covers removed".
>
> **Status:** **The Algebra 1 review unit was dropped and the course renumbered (2026-08-20).**
> The old Unit 1 (Foundations: Algebra 1 Review) was deleted outright — directories, tests, and
> its §4 block — and every remaining unit moved down one: old Units 2–8 are now **Units 1–7**
> (Linear → Quadratic → Polynomial → Rational → Radical → Exponential → Logarithmic). All unit
> and lesson numbers in directories, `.tex` sources, and these planning docs were rewritten to
> the new scheme; in-course references to the old review unit now say "Algebra 1" instead.
> All numbers below are the **new** numbering.
> **Build evidence (2026-08-20):** full clean rebuild (`target/` **and** `.stamps/` removed —
> stale stamps otherwise satisfy make and skip compiles) of all 7 units: every lesson's five
> work products, unit tests for Units 1–6 with `sample_test`/`sample_test_key` re-dropped, all
> unit packets and the curriculum packets — exit 0. Compiled output spot-checked for the new
> unit numbers. Both binder covers regenerated (Unit 1 via auto-discovery — it has no
> `spec.py`; Unit 2 from its spec). Packet parity: all lesson packets page-for-page; unit
> packets match except **unit01 88/89 and unit05 162/163**, both caused by the pre-existing
> practice-test-vs-key idiom defect (§7 work-rule/tests block), not by the renumber.
> Caveat: `make -j` can race the student/key pagination passes of one lesson (shared
> `.paginate/` dir) — rerun the affected lesson serially if `pagination pass failed` appears.
> **Units 1–5 are content-complete** — every lesson (plan, cover, warm-up, notes, activity,
> exit ticket, homework, all keys, and a slide deck) plus the unit tests (practice + actual and
> both keys, with the practice pair published to `sample_test/` + `sample_test_key/`).
> **Unit 6 (Exponential Functions)** is locked at **6 lessons (6.0–6.5)** — shorter than
> Units 4–5 because exponentials have no A2.EO and no A2.EI standard; a regression capstone
> (6.5) covers A2.ST.2's exponential branch. **Lessons 6.0–6.3 are authored & building**;
> lessons 6.4–6.5 and the unit tests are still skeletons. **6.3 is the first no-SOL-standard
> lesson authored in the course**, and it set the pattern the Unit 7 twins (7.3, 7.4) must
> follow: the standards line reads ``none --- beyond-SOL / precalculus prep,'' and the exit
> ticket carries an **ordinary** multiple-choice item rather than the SOL-style item used in
> 6.0–6.2.
> **Unit 7 (Logarithmic Functions): Lesson 7.0 authored & building** — locked at **7 lessons
> (7.0–7.6)**. A standards audit found log properties and log equation-solving have **no 2023
> VA SOL home**; they are kept as full lessons anyway (7.3, 7.4), labelled **beyond-SOL /
> precalculus prep** and barred from SOL-style test items — matching how Unit 6 already treats
> 6.3. Three Unit 6 ↔ Unit 7 collisions were found and **resolved**: `A2.ST.2` is Unit 6's
> alone (6.5), since the standard never names logarithmic; $\ln$ lands in 7.5; and no-standard
> content is handled the same way in both units. Full rationale in the Unit 7 status block in
> §4. Lessons 7.1–7.6 and the Unit 7 tests are still skeletons.
> **Next actions, in priority order:
> (1) continue Unit 6 at Lesson 6.4** (compound interest, half-life, and $e$), which carries four
> promised-but-unsolved equations forward — $2^{x}=5$ and $1000(1.05)^{t}=2000$ from 6.3, plus 6.2's
> coffee $132(0.85)^{t}=32$ and soda $(0.9)^{t}=2.118$ — and which **7.4 and 7.5 both depend on**;
> **(2) continue Unit 7 at Lesson 7.1** (introduction to logarithms), which Lesson 7.0 sets up the same
> way. Note that
> 6.1–6.5 are a prerequisite chain for the *later* Unit 7 lessons — 7.4 pays off 6.4's cliffhanger
> and 7.5 needs the $e$ introduced there — so Unit 6 should not fall far behind Unit 7.
> Lesson lists below are proposals to react to and edit — pacing (days per lesson) is intentionally
> left open pending the school calendar. **Authoring note:** every unit from 4 on must apply the
> vocab-box paragraph-break fix (§7); retrofitting Units 1–3 is deferred to §8, after Unit 7 and finals.
>
> **Open item:** most authored slide decks have never been checked for overflow — a
> `grep -n "Overfull"` sweep over every `unit0{1..7}/lesson*/slides` log is the next action.
> The two decks checked during the old review unit's cleanup were both bad, so assume the rest
> are too; beamer spills silently and `make` still exits 0.
>
> **Course redesign started 2026-08-19 — "experience first, formalize later" (EFFL).** Direction
> from the user: the Algebra 1 review unit is dropped (done, see above), and every lesson moves
> to the Math Medic EFFL shape — **warm-up → experience (a
> group activity applying prior knowledge and stretching into the new material, then a QuickNotes
> box for the formal notes/examples, then an Application worked together, then a
> Check-Your-Understanding practice section)**. **No tiered instruction, no separate guided-notes
> or exit-ticket components — and, as of 2026-08-20, no homework component either.** Teacher circulates with questions/cues/prompts, not answers; the debrief attaches
> the vocabulary to what the groups found. **Lesson 1.0 is the pilot and is rebuilt in this shape
> (2026-08-19)** — see the Unit 1 block in §4 for the component map, build evidence, and what the
> build system needed. **The `lesson-planning` skill is updated to the EFFL schematic
> (2026-08-20, PR #94):** SKILL.md (component set, EFFL invariants — timebox, spoiler rule,
> `\answerspace`, 12pt-relative boxguards — and guardrails), references/components.md (the
> experience spec replaces guided-notes/activity/exit-ticket; EFFL plan/cover/warm-up/homework/
> slides specs), references/conventions.md (12pt experience preamble + macro; EFFL plan order),
> build.md, course-workflow.md, and new_lesson.py (defaults to
> cover,warmup,experience,homework,slides; dedicated experience skeletons; 60-min default; legacy
> components still scaffoldable by name; all skeletons rewritten around the EFFL flow).
> Smoke-tested: a fresh default scaffold builds all five work products, EXIT 0.
> **EFFL rollout progress: 1.0 (pilot) and 1.2 are regenerated; 1.1, 1.3–1.5 and Units 2–7 are
> still legacy-shape.** **The experience is now FOUR parts on a page budget — Activity ≤2pp ·
> QuickNotes ½pp · Application ½–1pp · Check Your Understanding 1–2pp, the CYU unscored (cover
> score column reads NA)** — user feedback 2026-08-20; the skill is updated and 1.2 is the
> reference implementation.
>
> **HOMEWORK IS DROPPED FROM THE COURSE — user feedback 2026-08-20, third iteration: "there is no
> more homework, there is only the unscored check your understanding."** The `homework` component
> and its key are gone; **Check Your Understanding is now a lesson's entire practice set**, still
> unscored (cover score column reads **NA**), still done in class, and students keep the packet.
> The EFFL component set is therefore `cover`, `warmup`(+key), `experience`(+key), `slides`, plan.
> CYU keeps its **1–2pp** budget but should now be authored toward the **full 2pp** and carry the
> lesson's whole standard spread, with the last item as the formative check; the lesson's forward
> preview (the old homework `spiralbox`) moves to the end of the experience. **Lesson 1.2 is
> regenerated against this (2026-08-20) and is the reference implementation.**
>
> **Skill + scaffolder updated (2026-08-20, same pass).** `homework` is out of the EFFL default
> component set everywhere: SKILL.md (component list, "there is no `homework` component", CYU now
> authored toward the full 2pp with ~6 items, legacy note tells you to fold homework into CYU when
> regenerating), references/components.md (TOC, packet order, plan section order — "Homework &
> Preview" → **"Close & Preview"**, two teacher notes not three, cover TOC three rows, the CYU spec
> rewritten around spanning the whole standard, and the old `## Homework` section replaced by
> `## Homework — removed` documenting the legacy state and the conversion recipe),
> references/conventions.md, references/build.md, references/course-workflow.md, and
> `new_lesson.py` (`DEFAULT_COMPONENTS = cover, warmup, experience, slides`; `homework` demoted to
> the legacy-but-scaffoldable list beside `notes`/`activity`/`exit_ticket`). Skeletons updated:
> `cover.tex` (homework row → the NA-scored CYU row), `lesson_plan.tex` (six-phase glance table
> with the **Application row that was missing**, a new Application box, the CYU box rewritten,
> Close & Preview, `[Homework]` teacher note deleted), `slides.tex` (final frame is "No homework").
> **Smoke-tested:** a fresh default scaffold creates no `homework` dir and builds all five work
> products, EXIT 0.
>
> **`shared/lesson.mk` is deliberately unchanged** — it still merges `homework`/`homework_key` when
> present, because 42 legacy lesson dirs still have them and their packets must keep building.
>
> **The remaining `homework` dirs are a byproduct, not a cleanup task — user direction 2026-08-20:
> *every* lesson gets regenerated, 1.0 and 1.1 included, so homework disappears lesson by lesson as
> the rollout reaches each one.** Do not open a separate sweep to delete them, and do not patch a
> legacy lesson's homework in place: when the rollout reaches a lesson, regenerate it whole in the
> EFFL shape and the homework dir goes with it. 42 dirs still carry one today (only 1.0 and 1.1 are
> authored; the rest are skeletons that will be written fresh anyway).
>
> **Final step, once the last lesson is regenerated:** drop `homework`/`homework_key` from
> `STUDENT_ORDER`/`KEYED_PAIRS` in `shared/lesson.mk` and from `KEYED` in `new_lesson.py`. They are
> retained *only* to keep not-yet-regenerated lessons building; when none remain, homework leaves
> the build system too and the word is gone from the project.
>
> **THE COMPONENT IS NOW CALLED "EXPERIENCE & FORMALIZE" — user direction, 2026-08-20.** The
> `experience` component is labelled **Experience & Formalize** everywhere a student or a teacher
> reads it: the cover's packet table, the component's `\pageheader`, the deck's activity frame, the
> lesson plan's activity box, and its teacher note (`\begin{teachernote}[Experience \& Formalize]`).
> In LaTeX it is written `Experience \& Formalize`. **The directory keeps the short name
> `experience/`** (with `experience_key/`), because it is a build identifier hard-coded in
> `shared/lesson.mk`'s `STUDENT_ORDER`/`KEYED_PAIRS`; renaming the directory would mean editing the
> build system, which the skill never does. **Directory `experience`, label *Experience &
> Formalize*.** The pedagogical model is still "experience first, formalize later" — the new label
> just says both halves out loud, since the component carries the formalizing too (QuickNotes and
> the Application), not only the experience.
>
> **Baked into the `lesson-planning` skill (2026-08-20):** `SKILL.md` (a dedicated *Naming rule*
> block plus every component reference), `references/components.md` (the `## Experience &
> Formalize` section, plan section order, cover TOC row, teacher-note titles),
> `references/conventions.md` (component preamble, plan order, teacher-note list),
> `references/build.md`, `references/course-workflow.md`, all five skeletons
> (`cover.tex`, `experience.tex`, `experience_key.tex`, `lesson_plan.tex`, `slides.tex`), and
> `scripts/new_lesson.py` (`DOC_TITLE`, comments). **Smoke-tested:** a fresh default scaffold
> carries the new label in all eight places and builds all five work products, EXIT 0.
>
> **EFFL rollout: Unit 1 Lessons 1.0, 1.1, and 1.2 are regenerated in the four-part
> Experience & Formalize shape (2026-08-20).** See the Unit 1 block in §4 for each lesson's
> content and build evidence. All three are homework-free; `unit01/lesson0{0,1}/homework{,_key}`
> were deleted with the regeneration, leaving **38** legacy homework dirs in Units 2--7.
>
> **Consistency pass on 1.0, 1.1, and 1.2 (2026-08-20/21).** 1.0's activity had lost Scenario 1's
> graph and items c--f and Scenario 2's whole box header, so the packet referred to a "Sunday
> evening" it never set up; both are restored and the activity is back to 2pp / 11 sub-questions
> (details in the §4 Unit 1 block). **1.1 and 1.2 were then checked for the same class of loss and
> are clean** — both keep two properly framed `scenariobox`es, every plan cue (1b/2b/2d/2e/2f in
> 1.1; 1a–1d/2a–2f in 1.2) resolves to a real packet item, and the arithmetic in every activity,
> application, and CYU item was re-derived and checks out. What they *did* carry was **teacher-plan
> drift of the same kind, none of it visible to students**, now fixed: 1.1's plan numbered the
> Drone Descent application as four items (the packet folds standard form into item 2, so the
> 60 m concept check is item **3**, not 4 — wrong in both the Application box and the teacher note)
> and miscounted its `work` blocks ("three", listing four; the lesson has **six**, since activity 2b
> and 2d carry them too); 1.2's teacher note called #4–6 the early-finisher bank while the CYU box,
> the Close box, and its own next sentence treat #6 as the formative check (now #4–5); and 1.0's
> plan pointed the CYU `work` block at 5c when it is **5b**. All three rebuild at exit 0 with
> **experience 5/5** and **packets 10pp/10pp**.
>
> **Lesson learned for the rollout: after a compression pass, re-read the plan against the packet
> item by item** — every `1c`/`2d`-style cue, every "item~N is the point of the box", and every
> `work`-block count. Compression is where these break.
>
> **Next: continue the rollout at Lesson 1.3, then 1.4 and 1.5 — regenerate, don't patch.** After
> Unit 1 is fully EFFL, resume Unit 6 at 6.4 and Unit 7 at 7.1.

---

## 1. Design principles

- **Function-type organization.** Each unit is built around one function family
  (linear → quadratic → polynomial → rational → radical → exponential →
  logarithmic).
- **Lesson 0 = "Characteristics of ____ Functions."** Every unit opens with a
  Lesson 0 that studies the *behavior* of the new function type before students
  learn to manipulate/solve it.
- **Cumulative characteristics spine.** Each Lesson 0 re-teaches the full
  "read-a-graph" toolkit built so far, then **adds the new characteristics that
  this function type is the first to require** (e.g., asymptotes debut in Unit 4,
  origin symmetry in Unit 3). See §3 for the full progression.
- **Consistent component set per lesson.** *Legacy shape (as originally authored):* warm-up,
  notes/slides, activity, exit ticket, homework, cover — each with an answer key.
  ***EFFL shape (from 2026-08-19, piloted in 1.0):*** cover, warm-up, **experience** (activity +
  QuickNotes + practice, one component), homework, slides — keys for warm-up, experience, and
  homework. No notes / activity / exit-ticket components and no tiers.

---

## 2. Units at a glance

| Unit | Title | Function family | Lessons (incl. L0) | Status |
|:---:|---|---|:---:|---|
| 1 | Linear Functions | Linear, absolute value, piecewise | 6 | **Complete** |
| 2 | Quadratic Functions | Quadratic (incl. complex numbers) | 8 | **Complete** |
| 3 | Polynomial Functions | Polynomial | 7 | **Complete** |
| 4 | Rational Functions | Rational | 8 | **Complete** |
| 5 | Radical Functions | Radical / power | 8 | **Complete** |
| 6 | Exponential Functions | Exponential | 6 | **In progress** (6.0–6.3 done) |
| 7 | Logarithmic Functions | Logarithmic | 7 | **In progress** (7.0 done) |

Every unit opens with **Lesson X.0: Characteristics of ____ Functions**.
**Out of scope for this course:** conic sections, sequences & series, probability
& statistics, trigonometry, and linear systems / linear programming.

---

## 3. The characteristics-of-functions spine (the heart of the course)

Each unit's Lesson 0 revisits everything to its left and introduces the row(s)
marked ●. Legend: **● introduced here** · **○ revisited / deepened** ·
**· applied but not new**.

| Characteristic | U1 Lin | U2 Quad | U3 Poly | U4 Rat'l | U5 Rad | U6 Exp | U7 Log |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Function definition & notation | ● | · | · | · | · | · | · |
| Domain & range (from a graph) | ● | ○ | ○ | ○ | ○ | ○ | ○ |
| x- and y-intercepts / zeros | ● | ○ | ○ | ○ | ○ | ○ | ○ |
| Slope / constant rate of change | ● | | | | | | |
| Increasing / decreasing intervals | ● | ○ | ○ | ○ | ○ | ○ | ○ |
| Positive / negative intervals | ● | ○ | ○ | ○ | ○ | ○ | ○ |
| Maximum / minimum (extrema) | | ● | ○ | · | · | · | · |
| Axis of symmetry / vertex | | ● | ○ | | | | |
| Even symmetry (about y-axis) | | ● | ○ | | | | |
| End behavior | | ● | ○ | ○ | ○ | ○ | ○ |
| Odd symmetry (about origin) | | | ● | | | | |
| Relative vs. absolute extrema | | | ● | · | · | · | · |
| Turning points | | | ● | · | | | |
| Zero multiplicity (graph behavior) | | | ● | · | | | |
| **Asymptotes (vertical)** | | | | ● | | | ○ |
| **Asymptotes (horizontal)** *(slant = enrichment only)* | | | | ● | | ○ | |
| Holes / removable discontinuity | | | | ● | | | |
| Domain restrictions | | | | ● | ○ | | ○ |
| Restricted domain from radicand | | | | | ● | | |
| Inverse relationship of families | | | | | ● | | ○ |
| Growth vs. decay / constant ratio | | | | | | ● | · |
| Inverse of exponential (dom/range swap) | | | | | | | ● |

> **Renumbering note (2026-08-20):** the dropped Algebra 1 review unit used to introduce
> *function definition & notation* and *domain & range*; those rows now debut in **U1 Lin**,
> so Lesson 1.0 must carry them as teaching focus (not just review) — verify 1.0's coverage
> when it is next revised.

> This table is the pacing/coherence backbone. When authoring each Lesson 0, the
> "new" rows (●) are the teaching focus; the "○/·" rows are quick review applied
> to the new graph.
>
> **Preview note:** the absolute-value and piecewise lessons in Unit 1 give
> students an early, informal look at **vertex, axis of symmetry, and min/max**
> (the V-shape) before Unit 2 formalizes them for parabolas. The ● stays in U2
> because that's where the Lesson-0 progression makes them a teaching focus.

---

## 4. Unit-by-unit lesson breakdown

### Unit 1 — Linear Functions
> **Lessons 1.0, 1.1, and 1.2 regenerated in the four-part *Experience & Formalize* shape
> (2026-08-20).** Component set for all three: `cover`, `warmup`(+key), **`experience`**(+key),
> `slides`, plan. No `homework` anywhere in Unit 1's first three lessons.
>
> **Lesson 1.0 re-cut from three parts to four (2026-08-20).** The old three-part experience
> (Activity / QuickNotes / Practice) plus an 8-problem homework became: **Activity** (unchanged
> *Freezing Point* Saturday/Sunday pair, trimmed to 11 sub-questions — 1f folded into 1e, and the
> story-domain and math-domain questions merged into a single 2e — so it holds **2pp**),
> **QuickNotes** (compressed to ~½pp), a **new Application** (*The Car-Wash Card*,
> $B(w)=40-8w$: interpret slope and intercept, solve the zero in a `work` block, meaningful
> domain, then the concept check — at \$10 a wash the intercept does **not** move, only the
> steepness), and a **six-item unscored Check Your Understanding** absorbing the deleted homework:
> (1) features read off the *rule* $f(x)=2x+2$, (2) the contrast pair sharing a zero at $x=1$ with
> "why can the sign change only at the zero?", (3) a table whose $x$-step is 2, (4) the constant
> function with its boundary ($c(x)=b$ has a zero only when $b=0$, and then every input is one),
> (5) the pool model $W(t)=600+150t$ whose zero $t=-4$ is meaningless in the story, and (6) an
> SOL-style MC on $y=-3x+6$. CYU spans **rule / graph / table** across items 1--3. The homework's
> closing `spiralbox` moved to the end of the experience. Plan rebuilt with the six-phase glance
> table (5/20/13/7/10/5), separate Application and CYU boxes, **Close & Preview** in place of
> "Homework & Preview", and **two** teacher notes. Deck is 11 frames with a new Application frame,
> ending on "No homework". Standards unchanged: **A2.F.2a/c/f**.
>
> **Consistency fix — Lesson 1.0's activity had lost half of Scenario 1 and all of Scenario 2's
> frame (2026-08-20, found on review).** The 2026-08-20 re-cut compressed the *Freezing Point*
> activity into a single `scenariobox` titled *1. Saturday Morning*: Saturday kept only its table
> and its rule (its graph and items c--f were gone), and the **`2. Sunday Evening` box header and
> setup prose were dropped**, leaving Sunday's five questions orphaned inside Saturday's box. The
> handout therefore restarted its lettering at **a** mid-box, showed a *falling* line with no story
> attached to it, asked "what does each crossing tell you about **Sunday** evening?" and evaluated
> "5:00 **p.m.**" with no Sunday ever introduced, and gave $T(h)=6-2h$ inside a box whose own rule
> is $T(h)=2h-6$. The plan's circulate cues (1c/1d, 1e), its Part 1 description, and its debrief
> instruction to put "Saturday and Sunday side by side" all pointed at content the packet no longer
> contained. **Fixed:** Scenario 1 regains its pre-drawn rising graph and items **c--f** (the two
> axis crossings, the per-hour change located in the rule *and* on the graph, direction, and the
> above/below-freezing inequalities), compressed to hold one page; Scenario 2 regains its box and
> its "4:00 p.m., $6\,^\circ$C, falling $2\,^\circ$/hr" setup. Sunday's box and line are now
> **navy** and Saturday's **forest**, matching the deck's launch and debrief frames. Sub-question
> count is **11** (6 + 5) and the activity holds exactly **2pp**, as the timebox rule requires. Both
> `experience` and `experience_key` were edited identically, so they still paginate page-for-page.
> **Build evidence (after the fix):** `make -C unit01/lesson00 all` → EXIT 0; warm-up 1/1,
> experience **5/5**, cover 1, plan 6, slides 11 (handout 4pp + pptx); packets **10pp/10pp**.
>
> **Lesson 1.1 regenerated from the legacy shape (2026-08-20)** — the first full legacy→EFFL
> conversion in the course. `notes`, `activity`, `exit_ticket`, `homework` and their keys were
> deleted; every remaining file was rewritten. The experience, ***Two Receipts***, is 5pp:
> **Activity** (2pp, 10 sub-questions — *Summit Gym* shows a pre-drawn cost graph, so groups read
> the \$6 walk-in fee and \$3/climb straight off it and assemble $C(n)=3n+6$; *Basecamp Gym* gives
> only two receipts, 3 climbs \$24 and 7 climbs \$32, forcing the rate from a difference and the
> \$18 fee by working **backwards**, in a `work` block. **2d is the crux:** Priya writes
> $D-24=2(n-3)$ off the receipt she had — *is that the same rule?* Groups test $n=7$ and expand it
> to $D=2n+18$. 2e's cheaper-gym comparison has to switch somewhere ($n=12$); 2f asks for
> Basecamp's two numbers relative to Summit, no drawing), **QuickNotes** (~½pp: slope from any two
> points, the three forms and what each makes easy, the parent $y=x$ under stretch and shift,
> parallel/perpendicular, and the horizontal/vertical special cases), **Application**
> (*The Drone Descent* — $46$ m at $t=2$, $30$ m at $t=6$: rate in a `work` block, point-slope from
> $(2,46)$ expanded to $h=-4t+54$, the same line in standard form, then "start from 60 m instead —
> which number moves?"), and a **six-item unscored CYU** (slope from two points including the
> horizontal and vertical cases; one graphed line written both ways with a `work` block proving
> them equal; $y+2=-\tfrac34(x-4)$ through slope-intercept to standard; the parent
> $y=x \to y=-3x+2$ plus "which of $y=4$ and $x=4$ has no $y=mx+b$, and why"; a candle model,
> 17 cm at 1 h and 11 cm at 4 h; and an SOL-style MC on perpendicular slopes). Warm-up is 3 new
> items seeding exactly the activity's needs: counting steps between two marked points (with the
> deliberately ugly $y$-intercept $-\tfrac73$ that the picture will not give — the argument for
> point-slope), solving $2x+3y=12$ for $y$, and distributing $y-5=3(x-2)$. Plan is EFFL-shaped with
> the six-phase glance table, the target misconception named explicitly (*two equations that look
> different must be different lines*), and two teacher notes. Deck is 11 frames. Standards
> unchanged: **A.F.1a--e**.
> **Build evidence:** `make -C unit01/lesson01 all` → EXIT 0; warm-up 1/1, experience **5/5**,
> cover 1, plan 5, slides 11 (handout 4pp + pptx); packets **10pp/10pp**.
>
> **Lesson 1.2 relabelled only (2026-08-20).** It was regenerated into the four-part shape earlier
> the same day and is the reference implementation, so regenerating it meant applying the new
> *Experience & Formalize* label to its five files. `make -C unit01/lesson02 all` → EXIT 0;
> experience **5/5**, packets **10pp/10pp** — unchanged.
>
> **Conventions verified across 1.0--1.2 (2026-08-20):** namestrip (cover only), no `teachernote`
> in any key, **13 `work` blocks byte-identical blank↔key** (2 + 6 + 5, checked programmatically),
> zero Rule-1 `\ans`-inside-math violations (one was found in 1.1's key and fixed by closing the
> math first), zero overfull boxes in all three decks, and only the two pre-existing shared-style
> overfulls per lesson (the 6.0pt `\pageheader` and the 10.77pt `\namedateperiod`).
>
> **Unit-level build (2026-08-20):** `make -C unit01 student key` → EXIT 0; unit packets
> **76pp / 77pp** (down from 88/89 as 1.0 and 1.1 shed their legacy components). The 1-page
> difference is the **pre-existing** practice-test-vs-key idiom defect recorded in the §7
> work-rule/tests block — not introduced by this pass.
>
> **Page-budget lesson learned (2026-08-20).** Both regenerations first came out a page over, and
> micro-tightening (`itemsep`, `\answerspace` heights) recovered far less than expected. What
> actually worked: **a tall figure in a `minipage` beside too little text wastes its unmatched
> height** — pulling a second question into the left column, or the shared answer space up into it,
> reclaimed ~120pt in 1.0 alone. Second: **`\boxguard` is a page-break decision, not decoration** —
> a guard that is too high strands a whole box and leaves ~100pt dead at the foot of the previous
> page. Third: **the key is the binding constraint** — an `\ans{}` wider than the `\blank{}` it
> replaces wraps a line, so the key can run long on a page where the blank has room, and lowering a
> guard then splits the two files to different page counts. Check both sides after every guard
> change.
>
> *(Superseded)* The 1.0 entry below describes the pilot's original three-part cut and its
> homework; it is kept for the build-system history it records.
> **Lesson 1.0 rebuilt in the EFFL shape (2026-08-19) — the course pilot.** Components now:
> `cover`, `warmup`(+key), **`experience`**(+key), `homework`(+key), `slides`, plan; the old
> `notes`, `activity`, `exit_ticket` dirs (and keys) were deleted. The experience component,
> *Freezing Point*, is one 4-page document in three parts: **Activity** (four scenario boxes —
> Saturday warming $T(h)=2h-6$, Sunday cooling $T(h)=6-2h$ with the same zero $h=3$, a
> thermostat $T(h)=21$, and "the story vs.\ the math" for domain/range — all graphs pre-drawn,
> students label/circle and answer with prior knowledge only), **QuickNotes** (a sky/navy box the
> debrief fills: linear = constant rate, slope, intercepts, zero, positive/negative, increasing/
> decreasing, domain/range, on $f(x)=2x-4$), and **Practice: Check Your Understanding** (5 items:
> graphed line with slope $-\tfrac32$, a table, gift card $B(w)=40-8w$ with the one `work` block,
> a horizontal line, an SOL-style MC on "decreasing with zero at 2"). Warm-up is 3 items (points on a
> grid incl. points on an axis, evaluate $g(x)=3x-6$ incl. "for what $x$ is $g(x)=0$", continue a
> constant-step table and write its rule). Homework is 8 problems. Plan is EFFL-shaped: objective +
> standards + lesson model, learning targets/key understandings, vocabulary, a *Lesson at a Glance*
> timeline (5/20/12/13/5 min), warm-up, experience (what students do / what the teacher does, with
> the question-cue-prompt list per item), debrief (the six "red ink" moves, in order), practice,
> watch-for, homework, and three teacher notes (Warm-Up / Experience / Homework). Deck is 10 frames
> following the same flow (launch → warm-up → activity → four debrief frames → QuickNotes summary →
> practice/homework), zero overfull boxes.
> **Timebox trim (user feedback, 2026-08-19, third iteration) — "too much content for 60
> minutes."** The activity went from four parts to **two**: Saturday and Sunday only, with the
> meaningful-domain / story-vs-math questions folded into Sunday as 2e/2f, and Part 3 (the
> constant thermostat) and Part 4 deleted — the flat line is now the one example the teacher
> poses cold during the debrief (it stays in QuickNotes, practice, and homework), and the
> same-zero comparison lives in the debrief + the practice MC. Practice dropped the table item
> (homework #3 covers tables), leaving 4 items with the MC as the formative check. Experience is
> now **5pp/5pp** (~13 activity questions, Math Medic scale); \MeetingLength set to **60 min**
> (5 warm-up / 20 activity / 15 debrief / 15 practice / 5 close); plan, slides, and cover
> re-referenced. **EFFL scope rule for the skill:** an activity is 2 scenarios / ~10-13
> sub-questions / ~2pp at 12pt; extra examples belong to the debrief, practice, or homework.
> **Math Medic sizing (user feedback, 2026-08-19, second iteration):** the experience component
> was restyled to Math Medic's measured conventions — **12pt body** (was 10pt + `\small`) and
> **open answer space instead of write-lines**: a new `\answerspace{H}{answer}` macro (defined in
> the component preamble, identical in blank and key) reserves exactly H of open space via a
> fixed-height minipage — empty second arg in the blank, the red answer in the key — so pagination
> stays locked by construction; `\nopagebreak` keeps a prompt glued to its space. Experience is
> now 6pp/6pp (was 4/4 at 10pt); packet 12pp. Gotchas found: **boxguard counts tuned for 10pt are
> ~40% oversized at 12pt** (30 → 16, 26 → 14 here), and key `\ans{}` texts that run wider than the
> blank's `\blank{}` can wrap an extra line and shift a guard — keep interval-answer `\ans`es
> short. Warm-up, homework, and cover are still 10pt pending the user's verdict on the experience.
> **Spoiler rule (user feedback, 2026-08-19):** anything the student sees *before* the activity —
> the cover and the deck's learning-targets frame — must not pre-name the vocabulary the debrief
> will attach. Targets are written in plain language ("where it starts, where it hits zero, how
> fast it changes"), and the cover's Keep-in-Mind box stops after describing the EFFL process
> itself. Bake this into the skill update.
> **Build evidence:** `make -C unit01/lesson00 all` → EXIT 0; warm-up 1/1, experience 4/4,
> homework 2/2 (every key matches its blank), cover 1, plan 4, slides 10; packets 10pp/10pp.
> **Build system change (required):** `shared/lesson.mk` `STUDENT_ORDER`/`KEYED_PAIRS` now list
> `experience` (between `warmup` and `notes`), and `shared/cover.py` globs `experience/main.tex`
> for binder-cover art. Lessons without an `experience/` dir are unaffected. The scaffolder
> (`new_lesson.py`) does **not** know `experience` yet — that is part of the skill update.
> **Also note:** this was the first build on the user's Mac — TeX Live and poppler were installed
> via Homebrew (`brew install texlive poppler`, user-space, no sudo) on 2026-08-19.
>
> **Legacy status (scaffolded 2026-07-24; lessons 1.1–1.5 still in the old notes/activity/exit-ticket
> shape):** all 6 lesson dirs (`unit01/lesson00`–`lesson05`)
> created with skeleton `main.tex` for lesson plan + cover, warmup, notes, activity,
> exit_ticket, homework, slides, and each `*_key`. Unit assessments scaffolded:
> `tests/{practice_test,actual_test}`, `test_keys/`, `sample_test{,_key}/`.
> **Lesson 1.0 authored & builds (2026-07-24):** all components + keys + 7-slide deck done;
> reads a line's characteristics (domain/range, intercepts/zero, slope, increasing/decreasing,
> positive/negative intervals) off pre-drawn TikZ graphs. Standards: **2023 VA SOL A2.F.2a/c/f**
> (from `spec/algebra2-vdoe-sol.pdf`); slope is reactivated Algebra 1 prerequisite. Warm-up &
> exit ticket each fit one page (blank+key);
> notes 3pp, homework 2pp, activity 2pp (key 3pp, extra page is the teacher-only note).
> **Lesson 1.1 authored & builds (2026-07-24):** all components + keys + 7-slide deck done;
> covers slope as rate of change, the three forms (slope-intercept, point-slope, standard),
> writing equations from a graph / two points / slope+point, and graphing by transforming the
> parent $y=x$ ($kf(x)$ stretch/reflect, $f(x)+k$ shift — the lens A2.F.1 extends to every family).
> Standards: **2023 VA SOL A.F.1a–e** (Algebra 1 linear cluster, reactivated as Unit 1's
> foundation). Warm-up & exit ticket each fit one page (blank+key); notes 3pp, activity 2pp,
> homework 2pp; exit ticket includes an SOL-style MC item. `make -C unit01/lesson01 all` → EXIT 0
> (student 10pp, full 20pp).
> **Lesson 1.2 regenerated in the EFFL shape (2026-08-20) — the second lesson after the pilot, the
> lesson that set the *four-part* experience, and the first lesson with *no homework*.**
> Components: `cover`, `warmup`(+key), **`experience`**(+key), `slides`, plan; the old `notes`,
> `activity`, `exit_ticket` dirs (and keys) were deleted, and `homework`/`homework_key` were
> deleted on 2026-08-20 when homework was dropped course-wide.
>
> **EXPERIENCE SHAPE CHANGED — user feedback 2026-08-20, second iteration: "the experience section
> is still too long."** The experience is now **four** parts on an explicit page budget, not three:
> **Activity ≤ 2pp · QuickNotes ½pp · Application ½–1pp · Check Your Understanding 1–2pp.** The new
> **Application** part is a worked-together problem that sits between the notes and independent
> practice — the first place the just-named vocabulary is *used*. **Check Your Understanding is
> explicitly practice and carries no point value:** the cover's score column prints **NA** for it
> instead of a blank, the plan tells the teacher not to collect it for a grade, and the deck says
> "practice, not a quiz." This budget supersedes the earlier "activity + QuickNotes + practice"
> three-part spec and is baked into the skill (SKILL.md + references/components.md +
> references/conventions.md, 2026-08-20).
>
> **Content.** The experience, *In Range*, is 4pp: **Activity** (2pp — two scenario boxes on one
> pre-drawn trail: a parkway with mile markers 0–20 and a radio tower at mile 12 that a handheld
> radio reaches only from within 5 miles; Part 1 *Exactly Five Miles Out* gets markers 7 and 17 from
> the picture, names the distance $|x-12|$, builds $|x-12|=5$ and verifies both; Part 2 *In Range,
> Out of Range* shades can-reach ($7\le x\le17$, one piece) and cannot-reach ($x<7$ or $x>17$, two
> pieces), with **2d as the crux** — why one connected stretch vs. two — plus a single-value check
> and a story-vs-math trim at the ends of the parkway; **10 sub-questions**), **QuickNotes** (½pp:
> distance meaning, two-case rule with its $c=0$/$c<0$ branches, isolate-first, ``less th**AND**'' /
> ``great**OR**'', and the three notations, on the compact example $|x-3|$ with $c=2$),
> **Application** (½pp, *Roasting Tolerance* — 340 g bags rejected if more than 8 g off: write
> $|w-340|\le8$, solve to $332\le w\le348$ in a `work` block, read a 331 g bag off the *solved*
> range, then reason that tightening to 5 g gives a **narrower** interval around the same center),
> and **Check Your Understanding** (2pp, unscored, **six** items — the lesson's whole practice set
> now that homework is gone, absorbing what the old homework carried: (1) isolate-split-verify
> $3|x+1|-2=10$, (2) $|2x-1|\le5$ and (3) $|3x-6|\ge9$ as a deliberate *and*/*or* pair, each in all
> three notations, (4) the special cases the activity drops plus "for which $k$ does $|x-3|<k$ have
> no solution?" ($k\le0$ — the boundary is the trap), (5) a thermostat tolerance model $|T-68|\le2$
> with the "within includes the endpoints" follow-up, and (6) an SOL-style MC on $|x+2|>3$ as the
> formative check). Lesson 1.3's preview `spiralbox` moved from the deleted homework to the end of
> the experience. Warm-up is 3 items seeding the two-case rule, $|x-h|$, and one-vs-two shaded
> pieces — the last deliberately left hanging until Part 2c. Plan is EFFL-shaped with the
> **six-phase** glance table (5 warm-up / 20 activity / 13 debrief / 7 application / 10 CYU /
> 5 close, close assigns *nothing*), separate Application and Check-Your-Understanding boxes, a
> **Close & Preview** box in place of "Homework & Preview", and **two** teacher notes (Warm-Up,
> Experience). Deck is 11 frames ending on "No homework — this is the practice", zero overfull
> boxes. Standards unchanged: **2023 VA SOL A2.EI.1a–e**.
>
> **Build evidence (2026-08-20, homework-free rebuild):** `make -C unit01/lesson02 all` → EXIT 0;
> warm-up 1/1, experience **5/5**, cover 1, plan 5, slides 11 (handout 4pp + pptx); packets
> **10pp/10pp**. Conventions verified: namestrip (cover only), no `teachernote` in any key,
> **5 `work` blocks byte-identical blank↔key** (checked programmatically), zero Rule-1
> `\ans`-inside-math violations, only the two pre-existing `\pageheader`/`\namedateperiod`
> overfull hboxes. **Build gotcha:** deleting a component leaves a stale stamp in
> `.stamps/unitXX/lessonYY/` — `make` then skips recompiling a *sibling* component whose PDF was
> cleaned, and `pdfunite` fails on the missing file. Clear `.stamps/<unit>/<lesson>` alongside
> `target/<unit>/<lesson>` whenever a component directory is removed.
>
> **Three gotchas worth keeping.** (1) **Shading drawn *before* `\numline` is hidden under the
> axis** — draw the number line first, then the shading. (2) A CYU that spills ~10% onto a second
> page is worse than a tight one — compressing sub-items onto shared lines and trimming
> `\answerspace` heights pulled 4 exercises onto exactly 1pp (keep key answers short enough for the
> reduced heights). (3) Homework 7(a)/(b) needed `\writelines{3}` for key answers that wrap to four
> lines; parity was re-checked after the raise.
>
> *(Superseded legacy entry)* **Lesson 1.2 authored & builds (2026-07-24):** all components + keys + 7-slide deck done;
> absolute value as *distance from zero* driving equations $|ax+b|=c$ (two-case rule, isolate-first,
> no-solution/one-solution special cases) and inequalities ("less th**AND**" $<$ → one interval;
> "great**OR**" $>$ → two rays), with solution sets written three ways (set / interval / number
> line) and a tolerance-modeling strand. Standards: **2023 VA SOL A2.EI.1a–e** (from
> `spec/algebra2-vdoe-sol.pdf`). Warm-up & exit ticket each fit one page (blank+key); notes 3pp,
> activity 2pp, homework 2pp; exit ticket includes an SOL-style MC item.
> `make -C unit01/lesson02 all` → EXIT 0 (student 10pp, full 20pp).
> **Lesson 1.3 authored & builds (2026-07-24):** all components + keys + 7-slide deck done; the
> absolute value parent $y=|x|$ as a V (distance graph), transformations via vertex form
> $g(x)=a|x-h|+k$ (vertex $(h,k)$, axis $x=h$, opens up/down by sign of $a$, narrow/wide by $|a|$,
> min/max value $k$), and reading domain/range/intercepts/increasing-decreasing off pre-drawn V's;
> all graphs pre-drawn (no sketch-from-scratch) — students read graphs, match equation↔graph,
> complete tables, and build equations from graphs. Standards: **2023 VA SOL A2.F.1b/c** (the
> transformation lens applied to the absolute value parent as entry example) and **A2.F.2a/c/d/f**
> (characteristics; absolute value is a piecewise-defined function). Warm-up & exit ticket each fit
> one page (blank+key); notes 3pp, activity 2pp (key 3pp — extra page is the teacher note),
> homework 2pp; exit ticket includes an SOL-style MC item.
> `make -C unit01/lesson03 all` → EXIT 0 (student 10pp, full 21pp).
> **Lesson 1.4 authored & builds (2026-07-24):** all components + keys + 7-slide deck done;
> piecewise-defined functions as one function built from different rules on different pieces of the
> domain — evaluating by piece selection (watching the boundary's $<$ vs.\ $\le$), reading pre-drawn
> piecewise graphs with open/closed endpoints and spotting a discontinuity (jump), writing $|x|$ and
> $|x-h|$ as two-piece linear rules (bridge from 1.3), and the greatest-integer/step function
> $\lfloor x\rfloor$ (round down; staircase constant on each $[n,n+1)$). All graphs pre-drawn (no
> sketch-from-scratch); students evaluate, read, match, and model (streaming free-trial, overtime pay,
> parking step cost, data plan). Standards: **2023 VA SOL A2.F.2a/b/c/f** (characteristics of
> piecewise-defined functions, including graphs with discontinuities and constant intervals). Warm-up
> & exit ticket each fit one page (blank+key); notes 3pp, activity 2pp, homework 2pp; exit ticket
> includes an SOL-style MC item. `make -C unit01/lesson04 all` → EXIT 0 (student 10pp, full 20pp).
> **Lesson 1.5 authored & builds (2026-07-25):** all components + keys + 7-slide deck done; linear
> regression as fitting a *line to scattered data* — reading a scatterplot's association (direction /
> form / strength), interpreting the correlation coefficient $r\in[-1,1]$ (sign = direction, $|r|$ =
> strength; matching $r$ to plots), reading a line of best fit $\hat y=ax+b$ from technology and
> interpreting its slope (per-unit rate) and intercept (baseline) in context, predicting by
> substitution, distinguishing interpolation from extrapolation (with an "extrapolation breaks"
> moment), judging reasonableness, and correlation $\ne$ causation (lurking variables). All
> scatterplots/lines pre-drawn (no sketch-from-scratch); regression values are *given* since finding
> them is a technology task. Standards: **2023 VA SOL A2.ST.2c/d/e/f/g/h** (bivariate data,
> scatterplots, curve/line of best fit, correlation coefficient, predictions, reasonableness). Warm-up
> & exit ticket each fit one page (blank+key); notes 3pp, activity 2pp, homework 2pp; exit ticket
> includes an SOL-style MC item. `make -C unit01/lesson05 all` → EXIT 0 (student 10pp, full 20pp).
> **Unit 1 tests authored & build (2026-07-25):** `tests/practice_test` (3pp) + `tests/actual_test`
> (3pp) and their keys `test_keys/practice_test_key` (4pp) + `test_keys/actual_test_key` (4pp).
> Four parts each — A Vocabulary (matching, 8 pts), B Multiple Choice (6 items incl. SOL-style,
> 12 pts), C Short Answer & Computation (8 items, 40 pts), D Extended Response (2 justify items,
> 12 pts) — drawing across all six lessons: read line/V/piecewise graphs, write equations, solve
> $|ax+b|=c$ and $|ax+b|\lessgtr c$ (three-way solution sets), abs-value vertex form, piecewise
> evaluation + continuity, greatest-integer, and linear regression (slope/intercept interpretation,
> prediction, interpolation vs.\ extrapolation, correlation $\ne$ causation). Practice and actual are
> parallel with different numbers/contexts. `make -C unit01/tests all` and
> `make -C unit01/test_keys all` → EXIT 0; practice test + key published to `sample_test/` and
> `sample_test_key/`. **Unit 1 is content-complete; next is Unit 2 scaffolding.**
>
> **Unit 1 retrofitted to four conventions (2026-07-29)** — teachernotes → work rule → namestrip →
> boxguard, in that order, on all six lessons (1.0–1.5), one agent per lesson in parallel. Totals:
> **30 teacher notes** moved to the plans (zero left in any lesson key), **82 `work` blocks** added
> byte-identically across blanks and keys, **23 `\writelines{n}`** adjustments, **60 name rows**
> stripped (covers kept), **12 boxguard sites** (24 lines, blank + key each). `make -C unit01/lessonYY
> all` → **EXIT 0** for all six; **all 30 keyed components match their keys page for page**; every
> warm-up and exit ticket holds the 1-page constraint blank *and* keyed; all 30 work products
> present. Packets are **14pp student / 14pp key** for every lesson — 1.0 and 1.3 each shed 2pp
> (16 → 14) as their activity mismatches closed.
>
> Component shape is now uniform across the unit: warm-up 1/1, notes 3/3, activity 2/2, exit ticket
> 1/1, homework 2/2 — **except 1.5's notes at 4/4**, the one outlier (namestrip did not reclaim
> enough to drop it to 3). Each lesson plan grew 3pp → 4pp absorbing its five teacher notes.
>
> Ordering matters and was validated: teachernotes closed the mismatch outright on 1.0 and 1.3 but
> *opened* one on 1.2; namestrip opened one on 1.4; boxguard closed what the earlier passes
> disturbed. **Run them in this order.**
>
> **Open defect — 29 Rule-1 `\ans{}`-inside-`$…$` violations remain in Unit 1 keys**, concentrated in
> **1.1 (26: `notes_key` ×20, `homework_key` ×6)** and **1.3 (3: `notes_key`:51, `warmup_key`:33 and
> :53)**. Forms like `$y = \ans{$4x-3$}$` and `$t=\ans{$2$}$` do not error — LaTeX limps through
> because the inner `$` closes the outer math — but the answer is then set in **text mode inside a
> math expression**, and the construct is exactly what the global rule forbids. Fix by closing math
> first: `$y = $ \ans{$4x-3$}`. Detect them with a math-mode-aware scan, **not** a regex: a pattern
> like `\$[^$]*\\ans` reports every line that merely contains `$…$` somewhere plus an `\ans`
> elsewhere, which is ~154 false positives here and reads as "clean" when the pattern itself errors.
>
> Also fixed in passing: a Rule-1 `\ans{}`-inside-`$…$` violation in `unit01/lesson03/activity_key`,
> and two stray `main.pdf` files removed from `unit01/lesson05/notes{,_key}/` (inert — [shared/lesson.mk:46](shared/lesson.mk:46)
> `comp-pdf` prefers `main.tex` when both exist — but exactly the hazard the Unit 1 note warns of).
> **Still open on Unit 1: vocabpar** on 1.0, 1.1, 1.2, 1.4, 1.5 (1.3 done); and three content-level
> box stubs that a guard cannot fix because they sit inside breakable `tcolorbox`es (1.0 homework
> Practice, 1.2 activity Tier A 3 / homework Practice 5, 1.4 homework Practice) — those need a box
> split or two trimmed lines, not a guard.
>
> **`unit01/unit_cover/main.tex` authored (2026-07-31).** The unit title page — the LaTeX component
> `unit.mk` merges behind the generated `binder_cover/`, not to be confused with it. Modeled on
> `unit01/unit_cover/main.tex`: page-anchored TikZ banner (the fixed form — no negative `\vspace`),
> forest overview box, a six-row *Lessons in This Unit* table (1.0–1.5, each row's focus tagged with
> its standards), and a *Standards Addressed* box collapsing the unit to its five clusters — **A.F.1**
> (Algebra 1 linear, reactivated), **A2.EI.1**, **A2.F.1**, **A2.F.2**, **A2.ST.2**. `ltablex` is not
> loaded (the Unit 1 gotcha). Fits **exactly 1pp** at `\arraystretch` 1.5 / 1.25 with a 0.30\linewidth
> title column; zero overfull boxes. `make -C unit01 student` → EXIT 0, **90pp**, with the cover as
> **page 3** (the binder cover is 2pp). Units 2–7 still have no `unit_cover/`; this file is the
> template for them.

- **1.0** Characteristics of linear functions *(introduces: domain/range,
  intercepts, slope, increasing/decreasing, +/− intervals)*
- **1.1** Linear functions: slope & rate of change, forms of a line
  (slope-intercept, point-slope, standard), writing equations, and graphing
  with transformations
- **1.2** Absolute value equations & inequalities (solving algebraically)
- **1.3** Absolute value functions & transformations *(V-shape → previews vertex,
  axis of symmetry, min/max)*
- **1.4** Piecewise-defined functions — absolute value as the entry example, then
  the greatest-integer / step function and other classic piecewise functions
- **1.5** Linear regression (scatter plots, correlation, lines of best fit)

### Unit 2 — Quadratic Functions
> **Status (scaffolded 2026-07-25):** lesson map locked at **8 lessons (2.0–2.7)** — full
> breakdown (Systems 2.6 and Modeling 2.7 kept separate). All 8 lesson dirs
> `unit02/lesson00`–`lesson07` scaffolded with skeleton `main.tex` for lesson plan + cover,
> warmup, notes, activity, exit_ticket, homework, slides, and each `*_key`. Unit assessments
> scaffolded: `tests/{practice_test,actual_test}`, `test_keys/`, `sample_test{,_key}/`.
> **Lesson 2.0 authored & builds (2026-07-25):** all components + keys + 7-slide deck done; reads a
> parabola's characteristics off pre-drawn TikZ graphs — introduces the **vertex/turning point**
> (max vs. min and the max/min *value*), **axis of symmetry**, **even symmetry** (parent $y=x^2$),
> and **end behavior**, while revisiting domain/range, intercepts/zeros (up to two), increasing/
> decreasing, and positive/negative intervals; symmetry is the justification tool. Anchor graph
> $f(x)=x^2-2x-3=(x-1)^2-4$; projectile hook $h(t)=-16t^2+32t+48$ (vertex $(1,64)$, lands $t=3$).
> All parabolas pre-drawn via `plot` + `\clip` (no sketch-from-scratch); students read graphs/tables,
> use second differences to spot a quadratic, and interpret features in context. Standards: **2023 VA
> SOL A2.F.2a/c/d/f/g** (a,c,f revisited; d = absolute max/min and g = end behavior are new).
> Warm-up & exit ticket each fit one page (blank+key); notes 3pp, activity 4pp, homework 2pp; exit
> ticket includes an SOL-style MC item. `make -C unit02/lesson00 all` → EXIT 0 (student 12pp, full
> 22pp).
> **Lesson 2.1 authored & builds (2026-07-25):** all components + keys + 7-slide deck done; moves from
> *reading* a parabola (2.0) to *producing/graphing* one from its equation via the **three forms** ---
> vertex form $a(x-h)^2+k$ (vertex $(h,k)$, axis $x=h$, direction/width from $a$), standard form
> $ax^2+bx+c$ (axis $x=-b/2a$, vertex by substitution, $y$-int $(0,c)$), and intercept/factored form
> $a(x-p)(x-q)$ (zeros $p,q$, axis $x=(p+q)/2$) --- and reads each as **transformations** of the parent
> $y=x^2$ ($f(x)+k$, $f(x-h)$ with the right-shift sign flip, $a\,f(x)$ stretch/reflect). Unifying thread:
> the single curve $x^2-2x-3=(x-1)^2-4=(x+1)(x-3)$ (the 2.0 anchor) shown in all three costumes. All
> graphs pre-drawn via `plot`+`\clip` (no sketch-from-scratch); "graphing" is done by feature-extraction +
> equation↔graph matching + point tables. Standards: **2023 VA SOL A.F.2b/c/d** (Algebra 1 quadratic
> cluster reactivated as the graphing foundation), extended in Algebra 2 to the horizontal shift $f(x-h)$
> (the full **A2.F.1** transformation lens applied to the quadratic parent) with characteristics per
> **A2.F.2a/d**. Warm-up & exit ticket each fit one page (blank+key); notes 3pp, activity 2pp, homework
> 2pp; exit ticket includes an SOL-style MC item (horizontal-shift direction).
> `make -C unit02/lesson01 all` → EXIT 0 (student 10pp, full 20pp).
> **Lesson 2.2 authored & builds (2026-07-25):** all components + keys + 7-slide deck done; moves from
> *reading* a given factored form (2.1) to *producing* it and solving. Factoring the complete toolkit ---
> GCF first, $x^2+bx+c$ by the product/sum search, $ax^2+bx+c$ by grouping ($a\!\cdot\!c$ method),
> difference of squares $x^2-k^2$, and perfect-square trinomials (double root, graph tangent to axis) ---
> then the **Zero Product Property** ($AB=0\Rightarrow A=0$ or $B=0$; must set $=0$ first) to solve
> $ax^2+bx+c=0$, with the roots tied throughout to the parabola's $x$-intercepts/zeros. Unifying thread:
> the anchor $x^2-2x-3=(x+1)(x-3)$ from 2.0--2.1, now factored by hand. Two flagged traps: dividing by $x$
> (loses $x=0$) and the root$\leftrightarrow$factor sign flip. All graphs pre-drawn via `plot`+`\clip`;
> includes a patio-area model (reject the negative root). Restricted to real, factor-over-integers cases
> (square roots/completing the square → 2.3; complex roots → 2.4--2.5). Standards: **2023 VA SOL A2.EO.3b/d**
> (factor completely; difference-of-squares & perfect-square-trinomial identities) and
> **A2.EI.2a/b/d** (create, solve algebraically, and verify/interpret quadratic equations). Warm-up & exit
> ticket each fit one page (blank+key); notes 2pp, activity 2pp, homework 2pp; exit ticket includes an
> SOL-style MC item (root→factor sign flip). `make -C unit02/lesson02 all` → EXIT 0 (student 9pp, full
> 20pp).
> **Lesson 2.3 authored & builds (2026-07-25):** all components + keys + 7-slide deck done; solving
> quadratics that \emph{won't factor} via two methods --- the **Square Root Property** ($x^2=k\Rightarrow
> x=\pm\sqrt{k}$, $k\ge0$: isolate the square first, keep the $\pm$, simplest radical form, including
> $(x-h)^2=k$ binomial-square cases) and **completing the square** ($a=1$: move the constant, add
> $(b/2)^2$ to build a perfect square, then root), tied throughout to Lesson 2.1's **vertex form** (the
> same move rewrites $x^2-2x-3=(x-1)^2-4$, vertex $(1,-4)$ --- the unit anchor) and to a **choose-a-method**
> decision (factor / square roots / complete the square, dividing by $a$ first when $a\ne1$ in Tier E).
> Real solutions only; the negative-radicand wall ($x^2=-4$) is previewed and deferred to 2.4. All graphs
> pre-drawn via `plot`+`\clip`; includes a dropped-object model (square-root method) and a matted-photo area
> model. Standards: **2023 VA SOL A2.EI.2b** (solve algebraically --- square-root & completing-the-square
> methods, real solutions), **A2.EI.2a** (model), **A2.EI.2d** (verify/interpret roots as $x$-intercepts),
> building on **A2.EO.3d** (perfect-square-trinomial identity run forward) and **A2.F.2** vertex-form
> characteristics. Warm-up & exit ticket each fit one page (blank+key); notes 2pp, activity 2pp, homework
> 2pp; exit ticket includes an SOL-style MC item (which constant completes the square). `make -C
> unit02/lesson03 all` → EXIT 0 (student 9pp, full 19pp).
> **Lesson 2.4 authored & builds (2026-07-25):** all components + keys + 7-slide deck done; breaks the
> Lesson 2.3 ``no real solution'' wall by inventing the **imaginary unit** $i=\sqrt{-1}$ (working rule
> $i^2=-1$) --- rewriting negative radicals $\sqrt{-k}=i\sqrt{k}$ (pull $i$ out \emph{first}, then simplify;
> the $\sqrt{-a}\sqrt{-b}\ne\sqrt{ab}$ trap flagged), **standard form** $a+bi$ (real/imaginary parts,
> classify real / imaginary / pure imaginary, read points off the complex plane), and the three operations
> **add/subtract** (combine like terms) and **multiply** (FOIL then substitute $i^2=-1$), plus the
> **conjugate** product $(a+bi)(a-bi)=a^2+b^2$ (always real) and **powers of $i$** (cycle $i,-1,-i,1$; reduce
> exponent mod 4). Capstone reconnects to completing the square: $x^2+2x+5=0\Rightarrow(x+1)^2=-4\Rightarrow
> x=-1\pm2i$ (conjugate pair), previewing 2.5. Graphs pre-drawn via `plot`+`\clip` (no-real-roots parabola
> $y=x^2+4$) and Argand-plane point-reading; division-by-conjugate kept to a Tier E / homework extension as
> it sits beyond the add/subtract/multiply standard. Standards: **2023 VA SOL A2.EO.4a** (meaning of $i$),
> **A2.EO.4b** (equivalent negative-radical ↔ $a+bi$ forms), **A2.EO.4c** (add/subtract/multiply), building
> on **A2.EO.2** (radicals) and connecting forward to **A2.EI.2b** (2.5). Warm-up & exit ticket each fit one
> page (blank+key); notes 3pp, activity 2pp, homework 2pp; exit ticket includes an SOL-style MC item
> ($i^{38}$). `make -C unit02/lesson04 all` → EXIT 0 (student 10pp, full 20pp).
> **Lesson 2.5 authored & builds (2026-07-25):** all components + keys + 7-slide deck done; the \emph{one
> method that solves every quadratic}. Derives the **quadratic formula** $x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$ as
> completing the square (Lesson 2.3) done once on the general $ax^2+bx+c=0$, then a fixed protocol
> (standard form → read $a,b,c$ with signs → substitute/simplify) producing real \emph{and} complex ($a+bi$,
> Lesson 2.4) answers. Isolates the **discriminant** $b^2-4ac$ as a \emph{predictor} of the roots \emph{before}
> solving — three cases ($>0$ two real / $=0$ one repeated / $<0$ two complex-conjugate) each tied to a
> pre-drawn parabola's $x$-intercepts (2/1/0). Also: choose-a-method (factor/square-roots/formula), verify by
> substitution, and a projectile model (reject the impossible root). Unifying threads: the anchor
> $x^2-2x-3=0$ ($D=16$, roots $3,-1$ — matches 2.2 factoring) and the 2.4 leftover $x^2+2x+5=0$ ($D=-16$,
> roots $-1\pm2i$ — same conjugate pair the formula now reproduces). Tier E adds a discriminant \emph{parameter}
> problem (find $k$ for one/two/no real roots). All graphs pre-drawn via `plot`+`\clip` (no sketch-from-scratch).
> Standards: **2023 VA SOL A2.EI.2b** (solve over the complex numbers algebraically — the quadratic formula),
> **A2.EI.2a** (model), **A2.EI.2d** (verify/interpret), revisiting **A2.F.2d** (discriminant ↔ number/type of
> $x$-intercepts); builds on completing the square (2.3) and $i$ (2.4). Warm-up & exit ticket each fit one page
> (blank+key); notes 3pp, activity 2pp, homework 2pp; exit ticket includes an SOL-style MC item (root type from
> a given discriminant). `make -C unit02/lesson05 all` → EXIT 0 (student 10pp, full 20pp).
> **Lesson 2.6 authored & builds (2026-07-25):** all components + keys + 7-slide deck done; extends
> equation-solving from a \emph{single} quadratic (2.2--2.5) to a two-equation \textbf{system} with at least one
> quadratic. A \textbf{solution} is an ordered pair satisfying \emph{both} equations --- graphically a
> \textbf{point of intersection}; a \textbf{linear--quadratic} (line \& parabola) or
> \textbf{quadratic--quadratic} (two parabolas) system has \textbf{0, 1, or 2} solutions. Solve by
> \textbf{substitution} (set the two $y$-expressions equal) --- the key insight being that this \emph{collapses
> the system into one quadratic} already solvable by factoring (2.2) or the formula (2.5) --- then
> back-substitute to recover $y$; the collapsed equation's \textbf{discriminant} counts the intersection points
> (2/1/0), reusing Lesson 2.5's three cases (secant / tangent / miss). Includes the quad--quad ``identical-$x^2$
> terms cancel $\Rightarrow$ linear $\Rightarrow$ at most one solution'' trap, verification in \emph{both}
> equations, and a break-even model (revenue $=$ cost, two break-even points with a profit region between).
> Unifying thread: the unit anchor parabola $y=x^2-2x-3$ met by the line $y=x-3$ (solutions $(0,-3),(3,0)$; the
> collapsed $x^2-3x=0$) and by three horizontal lines $y=5/-4/-6$ ($D=36/0/-8\Rightarrow 2/1/0$ points). All
> graphs pre-drawn via `plot`+`\clip` (no sketch-from-scratch); students read intersections, solve by
> substitution/elimination, count solutions, and model. Standards: **2023 VA SOL A2.EI.3c** (solve
> linear--quadratic & quadratic--quadratic systems algebraically and graphically, incl.\ in context),
> **A2.EI.3b** (number of solutions), **A2.EI.3a** (create a system to model), **A2.EI.3d** (verify \&
> interpret). Warm-up & exit ticket each fit one page (blank+key); notes 3pp, activity 2pp, homework 2pp; exit
> ticket includes an SOL-style MC item (number of solutions from a collapsed quadratic).
> `make -C unit02/lesson06 all` → EXIT 0 (student 10pp, full 20pp).
> **Lesson 2.7 authored & builds (2026-07-25):** all components + keys + 7-slide deck done; the unit capstone, where
> students stop being handed a quadratic and \emph{build} one from a story, then read the answer off its features. A
> \textbf{feature-to-question map} organizes everything --- \textbf{$y$-intercept} $=$ starting value, a \textbf{zero}
> (positive root) $=$ ``when/where it reaches $0$,'' the \textbf{vertex} $=$ \textbf{max/min} (input $=$ when/where,
> output $=$ how much) --- across three model types: \textbf{projectile} $h(t)=-16t^2+v_0t+h_0$ (anchor
> $-16t^2+32t+48$: start $48$, max $(1,64)$, lands $t=3$), \textbf{maximum area} (pen against a barn wall, three sides,
> $A(x)=x(40-2x)$, vertex $(10,200)$, with the $40-2x$ trap and a feasible-domain beat), and \textbf{revenue
> optimization} (price\,$\times$\,changing demand, $R(x)=(8+x)(200-20x)$, best price at the vertex). The algebra is
> entirely reused (vertex by $x=-b/2a$ from 2.1; zeros by factoring/formula from 2.2/2.5); the new work is
> translating, choosing the feature, interpreting with units, and rejecting impossible values (negative time, a width
> outside the fence). Tier E ties back to systems (2.6) via a ``same-height'' object comparison. All graphs pre-drawn
> (scaled-axis projectile parabola + barn-wall pen schematic; no sketch-from-scratch). Standards: **2023 VA SOL
> A2.EI.2a** (create a quadratic model), **A2.EI.2d** (verify/interpret, incl.\ vertex as max/min), **A2.F.2d**
> (max/min from the vertex); builds on A2.F.2a/d (2.1) and A2.EI.2b (2.2, 2.5). Warm-up & exit ticket each fit one page
> (blank+key); notes 3pp, activity 2pp, homework 2pp; exit ticket includes an SOL-style MC item (which feature is the
> max height). `make -C unit02/lesson07 all` → EXIT 0 (student 9pp, full 20pp).
> **All eight Unit 2 lessons (2.0–2.7) are now authored & building.**
> **Unit 2 tests authored & build (2026-07-25):** `tests/practice_test` (3pp) + `tests/actual_test` (3pp) and their
> keys `test_keys/practice_test_key` (3pp) + `test_keys/actual_test_key` (3pp). Four parts each — A Vocabulary
> (8-term matching, 8 pts), B Multiple Choice (6 items incl. SOL-style discriminant item, 12 pts), C Short Answer &
> Computation (8 items, 40 pts), D Extended Response (2 justify items, 12 pts) — drawing across all eight lessons:
> read a pre-drawn parabola (vertex/axis/intercepts/zeros/range, 2.0–2.1), vertex from standard form via $-b/2a$
> (2.1), solve by factoring (2.2), square roots & completing the square (2.3), complex-number arithmetic in $a+bi$
> (2.4), quadratic formula + discriminant (2.5), linear–quadratic system (2.6), and a projectile feature-to-question
> model + discriminant-vs.-$x$-intercepts reasoning (2.7 / 2.5). Practice and actual are parallel forms (same
> structure, different numbers). `make -C unit02/tests all` and `make -C unit02/test_keys all` → EXIT 0; practice
> test/key published to `sample_test/` and `sample_test_key/` via the `drop` targets. **Unit 2 is complete (all
> lessons + assessments).**
> **All four conventions retrofitted to Unit 2 (2.0–2.7) + binder cover generated (2026-07-30).** Applied in the
> documented order — teachernotes → namestrip → vocabpar → work rule → boxguard (boxguard last, since it repairs the
> pagination the others disturb). Result: `make -C unit02/lessonNN all` exits 0 for all eight, **every one of the 40
> components matches its key page for page**, all 32 warm-up/exit-ticket documents are still 1pp, and
> `unit03_student.pdf` / `unit03_key.pdf` are **127pp each**.
> * **teachernotes** — 40 notes migrated (5 per lesson) out of the `_key` files into the lesson plans via
>   `movenotes.py`; no `teachernote` remains in any Unit 2 key. This alone closed the only pre-existing mismatch's
>   sibling cases and left just one (2.7 notes 3/2).
> * **namestrip** — 80 name-row lines removed (10 per lesson, blanks + keys); `--check` clean on all eight.
> * **vocabpar** — **not requested but required**: all eight `notes_key` files defined `\vocabans` without the
>   surrounding `\par`s, so every key's vocab box rendered as one run-on jumble with answers colliding into the next
>   term. Fixed to match the `unit04/lesson00` reference (`\par\noindent…\ansline{#2}\par`). This also closed the 2.7
>   notes mismatch outright (3/2 → 3/3) with **no packet growth**. Worth knowing: Unit 2's keys were shipping
>   unreadable vocab boxes. The blank-side half (`\par\vspace{2pt}` before the first `\termblanklong`, so the intro
>   sentence stops running into the first term) was applied too — free on seven of eight; **2.6 needed one more
>   mirrored trim** (practicebox and protocol `itemsep`) to stay 3/3. **Unit 2 is now fully vocabpar-clean, both
>   sides.** Units 1 and 3 still carry the defect.
> * **work rule** — Unit 2 had **zero** `work` blocks before this pass. **73 sites converted → 146 blocks**, verified
>   byte-identical blank↔key: 2.1 ×1, 2.2 ×11, 2.3 ×10, 2.4 ×17, 2.5 ×20, 2.6 ×9, 2.7 ×5. 2.0 got none — it is pure
>   graph-reading with no solve tasks, so the rule does not apply. Components absorbed the space: 2.2 activity 2→3,
>   2.3 homework 2→3, 2.5 activity 2→3 and homework 2→3. Two lessons needed the space bought back rather than the
>   conversion declined — 2.6 notes took mirrored `arraystretch` 1.4/1.3→1.15 trims (the blank's `termblanklong`
>   vocab box runs ~5 lines taller than the key's `vocabans`, and the new blocks consumed that slack), and 2.2's
>   activity justification slot went `\blank{5.5cm}`→`\writelines{2}` to match its wrapped `\ansline`.
> * **boxguard** — **12 guard sites, 24 lines** (each mirrored blank+key): 2.0 notes ×2, 2.1 notes ×2, 2.2 notes ×2 +
>   activity ×1 (`\tcbbreak`), 2.3 notes ×2, 2.4 notes ×1, 2.5 activity ×1 (`\tcbbreak`), 2.7 notes ×1. **Every guard
>   that landed was free** — no packet grew. 2.0/2.1/2.2/2.3/2.4/2.7 notes now have **zero broken boxes**. Confirms
>   the documented limit again: `\boxguard` is inert inside a breakable `tcolorbox`, so the two activity fixes used
>   `\tcbbreak` at a better split point instead. **One guard declined:** 2.6 notes box 1 leaves a ~3-line tail atop
>   p2, but guarding it pushes the whole ~4.5in box and costs a page (3/3 → 4/4); recovering ~3.5in is far beyond what
>   spacing trims give, so the stub stays — re-measure if that box's content changes.
> * **binder cover** — `unit02/binder_cover/spec.py` authored (16 hand-placed elements, every one traceable to a Unit
>   3 lesson) and `main.pdf` generated via `shared/cover.py`; `unit.mk` picks it up and it now leads both unit packets.
>   Composition follows Unit 1's: the unit anchor $x^2-2x-3$ in all three costumes (parent+vertex-form graph, factoring
>   and completing-the-square slabs, the linear–quadratic system), the quadratic formula and discriminant cases, the
>   complex thread ($i$, the conjugate product, $x^2+2x+5=0$, the no-real-roots parabola), and the 2.7 models.
> **Known defect, pre-existing and NOT from this pass — `unit02/lesson00/activity` p3 renders a broken TikZ graph:**
> the Tier E "Back to the ball" projectile plot ($h(t)=-16t^2+32t+48$) draws as a single enormous vertical spike
> filling the page, because its $y$-values reach 64 with no axis scaling. It is why that activity is 4pp with a nearly
> empty p4. Needs a content fix (scale the $y$-axis as 2.7's projectile figure does), not a guard.
> **Next action: begin Unit 3 (Polynomial Functions)** — or fix the 2.0 activity graph first if Unit 2 is going to print.
- **2.0** Characteristics of quadratic functions *(introduces: vertex/max-min,
  axis of symmetry, even symmetry, end behavior, turning point)*
- **2.1** Graphing quadratics (vertex, standard, intercept forms) & transformations
- **2.2** Solving by factoring (factoring quadratics)
- **2.3** Solving by square roots & completing the square
- **2.4** Complex numbers (operations, i)
- **2.5** The quadratic formula & the discriminant (incl. complex solutions)
- **2.6** Systems involving quadratics (linear–quadratic & quadratic–quadratic)
- **2.7** Modeling with quadratics (projectile/area/optimization)

### Unit 3 — Polynomial Functions
> **Status (map confirmed & scaffolded 2026-07-25):** lesson map locked at **7 lessons
> (3.0–3.6)** — the original 3.4 was split into a forward-solving lesson (3.4, RRT) and a
> counting/building lesson (3.5, FTA & complex zeros), pushing graphing+modeling to 3.6.
> All 7 lesson dirs `unit03/lesson00`–`lesson06` scaffolded with skeleton `main.tex` for
> lesson plan + cover, warmup, notes, activity, exit_ticket, homework, slides, and each
> `*_key`. Unit assessments scaffolded: `tests/{practice_test,actual_test}`, `test_keys/`,
> `sample_test{,_key}/`.
> Standards grounded against `spec/algebra2-vdoe-sol.pdf`: **A2.EO.3a/b/c/d** (operations,
> factoring, division, identities incl. sum/diff of cubes), **A2.EI.6a/b/c/d** (solve degree
> ≥3 over ℂ), **A2.F.2a/b/c/d/e/g** (characteristics/graphing; note polynomial is **not** in
> A2.F.1's family list, so transformations aren't a standard here — cube-root/radical graphing
> is Unit 5). Lesson 3.0 introduces the four new spine rows: ● odd/origin symmetry, ● relative
> vs. absolute extrema, ● turning points, ● zero multiplicity (end behavior deepened to the
> degree + leading-coefficient rule).
> **Lesson 3.0 authored & builds (2026-07-25):** all components + keys + 8-slide deck done; reads a
> polynomial's characteristics off pre-drawn TikZ graphs — introduces the **degree + leading-
> coefficient** end-behavior rule (even/odd degree ⇒ same/opposite arms; sign of $a$ ⇒ right arm),
> **turning points** (at most $n-1$), **relative (local) vs. absolute (global) extrema** (odd degree ⇒
> no absolute extrema), and **zero multiplicity** (odd crosses / even touches), plus **odd/origin
> symmetry** ($f(-x)=-f(x)$) alongside revisited even symmetry, domain/range, intercepts/zeros,
> increasing/decreasing. Anchor $g(x)=x^3-3x+2=(x-1)^2(x+2)$ (rel. max $(-1,4)$, rel. min/touch $(1,0)$,
> cross at $(-2,0)$); supporting graphs $x^3-4x$, $-x^4+4x^2$, $x^4-4x^2$, $x^2(x-3)$, $x^4-5x^2+4$,
> $(x+1)^2(x-2)$; Tier E open-box volume model $V(x)=x(10-2x)(8-2x)$ and a profit model $t(t-3)^2$. All
> graphs pre-drawn via `plot`+`\clip` (no sketch-from-scratch). Standards: **2023 VA SOL
> A2.F.2a/c/d** (revisited), **A2.F.2e** (relative extrema — new), **A2.F.2g** (end behavior — degree/
> lead rule), **A2.F.2b** (even/odd contrast). Warm-up & exit ticket each fit one page (blank+key);
> notes 4pp, activity 3pp, homework 2pp; exit ticket includes an SOL-style MC item (even-multiplicity
> touch + odd-degree end behavior). `make -C unit03/lesson00 all` → EXIT 0 (student 12pp, full 23pp).
> **Lesson 3.1 authored & builds (2026-07-25):** all components + keys + 8-slide deck done; turns 3.0's
> *factored* forms into *standard* forms. Covers standard form / degree / leading coefficient / term
> count (incl. two-variable term degree = sum of exponents), **adding & subtracting** as pure like-term
> collection with the year's biggest trap flagged (a leading minus is a factor of $-1$ — it flips
> **every** sign) plus the "degree can drop" case $(x^4+2x)-(x^4-5)=2x+5$, **multiplying** at all three
> sizes (monomial×poly, binomial×binomial, binomial×trinomial by box) in one *and two* variables, the
> **degree/leading-coefficient rule for products** (degrees add, leads multiply ⇒ end behavior known
> before expanding — the A2.F.2g link back to 3.0), and the **special products** $(a\pm b)^2$,
> $(a+b)(a-b)$ with the $(x+4)^2\ne x^2+16$ error killed numerically at $x=1$. Unifying thread: the unit
> anchor $(x-1)^2(x+2)$ is expanded to $x^3-3x+2$ (the $\pm 2x^2$ cells cancel — that is why there is no
> $x^2$ term), and homework expands 3.0's exit-ticket function $(x+1)^2(x-2)=x^3-3x-2$ and checks it
> against the graph students already read. Tier E expands 3.0's open-box model to
> $V(x)=4x^3-36x^2+80x$ (checked against that lesson's table, $V(1)=48$), builds a profit polynomial
> $P=R-C$, and justifies why a *product* never loses degree while a *sum* can. Standards: **2023 VA SOL
> A2.EO.3a** (sums, differences, products in one and two variables), **A2.EO.3d** in its *forward*
> direction (equality of forms; difference-of-squares & perfect-square-trinomial identities — factoring
> is 3.2), revisiting **A2.F.2g**. Warm-up & exit ticket each fit one page (blank+key); notes 3pp,
> activity 2pp (key 3pp — extra page is the teacher note), homework 2pp; exit ticket includes an
> SOL-style MC item ($(3x-4)^2$, distractors = the three classic errors).
> `make -C unit03/lesson01 all` → EXIT 0 (student 10pp, full 23pp).
> **Lesson 3.2 authored & builds (2026-07-25):** all components + keys + 10-slide deck done; runs 3.1
> *backward*. Organized around two habits and one standard: **GCF first, every time** (largest
> coefficient, *lowest* shared power; two-variable and negative-lead cases; the GCF *uncovers* hidden
> patterns — $2x^3-50x\Rightarrow 2x(x-5)(x+5)$), then a **count-the-terms decision tree** (2 terms →
> difference of squares or the new sum/difference of **cubes**; 3 → perfect-square trinomial, ordinary
> trinomial factoring, or **quadratic form**; 4 → **grouping**), all governed by the word
> **completely** — every factor prime over the integers. New identity: $a^3\pm b^3=(a\pm b)(a^2\mp
> ab+b^2)$ taught via **SOAP**, and *discovered* rather than announced (Warm-Up item 3 has students
> multiply $(x+2)(x^2-2x+4)=x^3+8$ before it is named — the A2.EO.3d verification direction). Flagged
> traps: a $2$ in the cube identity's middle term, SOAP sign flips, $a^2\mp ab+b^2$ is prime, mismatched
> binomials in grouping from not factoring a negative out of the second pair, and the
> squares/cubes asymmetry ($a^2+b^2$ prime but $a^3+b^3$ not). Unifying thread: the anchor
> $q(x)=x^4-5x^2+4$ — a **graph students already read in 3.0** — is factored in quadratic form to
> $(x-1)(x+1)(x-2)(x+2)$ and its four zeros matched to the intercepts (pre-drawn TikZ graph in the
> notes hook; no sketch-from-scratch). Closes on an honest **wall**: today's toolkit cannot crack the
> unit anchor $x^3-3x+2$ even though it factors — the motivation for 3.3/3.4. Tier E adds $x^6-64$
> factored *two ways* (squares-first vs. cubes-first ⇒ the rule "squares before cubes") and an
> expand-to-verify proof of the difference-of-cubes identity. Standards: **2023 VA SOL A2.EO.3b**
> (factor completely, one and two variables, ≤4 terms, over the integers) and **A2.EO.3d** (equality of
> forms; verify difference-of-squares, sum/difference-of-cubes, and perfect-square-trinomial
> identities), revisiting **A2.F.2c** (zeros from factored form) and **A2.EO.3a** (checking by
> multiplying). Warm-up & exit ticket each fit one page (blank+key); notes 3pp (key 4pp — extra page is
> the teacher note), activity 3pp, homework 2pp; exit ticket includes an SOL-style MC item ($8x^3-27$,
> distractors = the three cube-identity errors). `make -C unit03/lesson02 all` → EXIT 0 (student 12pp,
> full 26pp).
> **Lesson 3.3 authored & builds (2026-07-26):** all components + keys + 9-slide deck done; supplies the
> tool 3.2 lacked. Everything hangs on one statement, introduced from the Warm-Up's $247=5\cdot49+2$:
> $P=D\cdot Q+R$ with $\deg R<\deg D$, so **$R=0$ means the divisor is a factor**. Covers **monomial
> divisors** (split the fraction; one and two variables; the $\frac{5x^2y^2}{5x^2y^2}=1$-not-$0$ trap),
> **long division** with the two setup rules (standard form + a **placeholder 0** for every missing
> power) written with the subtraction shown as $-(\cdots)$, **synthetic division** for divisors $x-r$
> only (the sign flip $x+2\Rightarrow r=-2$ drilled as "rewrite it $x-(-2)$"), and both theorems
> *discovered rather than announced* — the **Remainder Theorem** lands when the remainder $-9$ from
> $(2x^3+3x^2-5)\div(x+2)$ turns out to equal $f(-2)$, proved in two lines by substituting $x=r$ into
> $f(x)=(x-r)q(x)+R$; the **Factor Theorem** arrives as a five-row equivalence table (factor $\iff$
> $f(r)=0$ $\iff$ remainder 0 $\iff$ zero $\iff$ $x$-intercept), already true in Warm-Up items 3–4.
> Unifying thread: the unit anchor $x^3-3x+2$ — unfactorable with 3.2's toolkit — is divided by $(x-1)$
> to give $x^2+x-2$ and hence $(x-1)^2(x+2)$, matched to the multiplicity-2 touch and the crossing
> students read off the 3.0 graph (**"the wall is down"**). Homework closes the unit's longest loop:
> $h(x)=x^3-3x-2$ (read on 3.0's exit ticket, expanded in 3.1, unfactorable in 3.2) is recovered as
> $(x+1)^2(x-2)$ by division; $(x^4-16)\div(x-2)$ returns $x^3+2x^2+4x+8=(x+2)(x^2+4)$, the same
> factorization 3.2 produced by a different road. Tier E carries the **factorable trinomial divisor**
> $x^2+x-6$ (the A2.EO.3c clause synthetic division cannot reach), a "find $k$ so $(x-3)$ is a factor"
> inversion, synthetic **substitution**, and a preview task where groups test the integer divisors of
> $6$ on $2x^3-3x^2-11x+6$, find $r=-2,3$, and discover the third zero $\frac12$ was never on the list —
> conjecturing the Rational Root Theorem a day early. Standards: **2023 VA SOL A2.EO.3c** (monomial,
> binomial, and factorable trinomial divisors), revisiting **A2.EO.3b** (factor the depressed
> polynomial completely) and **A2.EO.3a** (check by multiplying), touching **A2.F.2a/f** (zeros,
> $x$-intercepts, evaluating $f(r)$); direct prerequisite for **A2.EI.6c/d** in 3.4–3.5. Warm-up & exit
> ticket each fit one page (blank+key); notes 4pp (key 5pp), activity 3pp (key 4pp), homework 2pp; exit
> ticket includes an SOL-style MC item (which binomial divides $x^3-6x^2+11x-6$; distractors = the sign
> flip and two "grab the constant" errors). `make -C unit03/lesson03 all` → EXIT 0 (student 12pp,
> full 27pp).
> **Lesson 3.4 authored & builds (2026-07-26):** all components + keys + 9-slide deck done; supplies the
> candidate list 3.3 had to be handed. The whole lesson is one workflow — **list $\rightarrow$ test
> $\rightarrow$ divide $\rightarrow$ finish $\rightarrow$ verify** — hung on the **Rational Root
> Theorem**: for integer coefficients, a rational zero $\frac{p}{q}$ in lowest terms has $p \mid a_0$
> and $q \mid a_n$ (constant on *top*, leading coefficient on the *bottom*, every value with a $\pm$).
> The theorem is *earned rather than announced*: the Warm-Up finishes Lesson 3.3's Tier E preview task,
> dividing $h(x)=2x^3-3x^2-11x+6$ by $(x-3)$ to reach $(x-3)(2x-1)(x+2)$ and the zero $\tfrac12$ that
> the integer list missed, then asks where that denominator came from — and the notes answer it by
> multiplying the factors' leading coefficients ($1\cdot2\cdot1=2$) and constants ($(-3)(-1)(2)=6$),
> so a factor $(qx-p)$ has nowhere to hide. Flagged traps: the **flipped fraction** (leading
> coefficient on top), a **missing $\pm$**, unreduced duplicates ($\tfrac22$, $\tfrac63$), and the new
> hazard of this lesson — reading zeros off a **non-monic factor** ($2x-1 \Rightarrow x=\tfrac12$, not
> $2$ or $-\tfrac12$). Efficiency is taught explicitly (read the graph, shrink to the depressed
> polynomial, test cheaply with the Remainder Theorem), and both **limits** are made concrete:
> $x^3-x^2-2x+2=(x-1)(x^2-2)$ hands its other two zeros $\pm\sqrt2$ to the depressed polynomial, and
> $k(x)=x^3-3x-1$ has **no rational zeros at all** yet three real ones (established from a table of
> values with three sign changes — no sketch-from-scratch). Graph-reading carries real weight: two
> pre-drawn TikZ graphs (notes hook $h$, activity Tier A $2x^3+3x^2-11x-6$ with intercepts $-3$,
> $-\tfrac12$, $2$) let students *see* a fractional zero and pick it off the list instead of grinding
> twelve candidates. Tier E proves the monic case ($d=-r(r^2+br+c)$), runs the theorem backward to
> build $6x^3+x^2-4x+1$ from zeros $\tfrac12,\tfrac13,-1$ (the A2.EI.6a skill 3.5 opens with), and
> closes on $x^3-x^2+4x-4$ whose depressed $x^2+4$ has no real zeros — the door into 3.5. Homework
> closes another loop: $x^3+2x^2-5x-6$ (3.3's exit ticket, where the divisor was *given*) must now be
> cracked with no hints, plus an A2.EI.6d verification step. Standards: **2023 VA SOL A2.EI.6c**
> (solve degree $\ge 3$; over $\mathbb{R}$ today, $\mathbb{C}$ in 3.5) and **A2.EI.6d** (verify
> algebraically and graphically, explain the method), using **A2.EO.3c** and **A2.EO.3b** on every
> problem and touching **A2.F.2c**. Warm-up & exit ticket each fit one page (blank+key); notes 4pp
> (key 5pp), activity 3pp (key 4pp), homework 2pp (key 3pp); exit ticket includes an SOL-style MC item
> (which value is *not* a possible rational zero of $4x^3-x^2+6x-3$; answer $\tfrac23$, distractors all
> valid candidates). `make -C unit03/lesson04 all` → EXIT 0 (student 12pp, full 28pp).
> **Lesson 3.5 authored & builds (2026-07-26):** all components + keys + 9-slide deck done; the lesson
> that finishes every ``no solution'' sentence of the year. It hangs on one theorem and the corollary
> students actually use --- the **Fundamental Theorem of Algebra** (degree $n\ge1\Rightarrow$ at least
> one complex zero) and therefore **exactly $n$ complex zeros counted with multiplicity**, with
> $f(x)=a(x-r_1)\cdots(x-r_n)$. This is the first tool of the course that \emph{counts} solutions
> before finding any, so ``how do I know I am done?'' finally has an arithmetic answer. The **Complex
> Conjugate Root Theorem** (real coefficients $\Rightarrow$ $a+bi$ and $a-bi$ travel together) is
> \emph{earned rather than announced}: the Warm-Up has students multiply $(x-3i)(x+3i)=x^2+9$ and solve
> $x^2-2x+5=0$ into $1\pm2i$ before any pairing is named, and the notes then derive
> $\big(x-(a+bi)\big)\big(x-(a-bi)\big)=x^2-2ax+(a^2+b^2)$ as the reason the pair is \emph{required} ---
> a lone imaginary zero strands an $i$ in the coefficients. Two consequences carry more weight than the
> theorem itself: the number of imaginary zeros is always **even**, so an **odd-degree** real polynomial
> must have a real zero --- exactly what Lesson 3.0's opposite end-behavior arms forced graphically, and
> both arguments are put on the board. Graph-reading is the assessment core (**A2.EI.6b**): *imaginary
> zeros $=$ degree $-$ real zeros counted with multiplicity*, worked off pre-drawn TikZ graphs, with the
> recurring beat that an $x$-intercept \emph{is} a real zero and a graph can never show an imaginary
> one. Solving over $\mathbb{C}$ is Lesson 3.4's list$\to$test$\to$divide$\to$finish workflow with a
> single changed step --- a negative discriminant now yields a conjugate pair instead of ``no solution''
> ($x^3-5x^2+9x-5\Rightarrow 1,\,2\pm i$; $x^4-5x^2-36$ by quadratic form $\Rightarrow\pm3,\pm2i$) ---
> and **A2.EI.6a** drives the same road backward: zeros $\to$ factors $\to$ polynomial, supplying any
> missing conjugate. Unifying threads close three long loops: the Warm-Up finishes 3.4's Tier E
> cliffhanger $x^3-x^2+4x-4=(x-1)(x^2+4)\Rightarrow 1,\pm2i$ (whose pre-drawn graph crosses **once** ---
> the hook); the anchor $(x-1)^2(x+2)$ from 3.0 carries counting with multiplicity (a touch fills two
> slots); and homework finishes $x^3+2x^2+4x+8$, the quotient 3.3 produced from $x^4-16$, then revisits
> $x^2+4$ --- declared \emph{prime} in 3.2 --- to show that ``prime'' was always relative to a number
> system. Flagged traps: the unpaired imaginary zero (the signature error), hunting for imaginary zeros
> among the $x$-intercepts, counting distinct zeros instead of counting with multiplicity, the
> $(x-4i)(x+4i)=x^2+16$ sign slip, and ``no real solutions'' still written on a depressed quadratic.
> Tier E proves the conjugate-product lemma, derives the odd-degree result two ways, solves
> $x^4+13x^2+36=0$ (all four zeros imaginary, with a pre-drawn graph that never meets the axis), and
> closes on $f(x)=x-i$ --- a real counterexample-that-is-not, since the theorem says \emph{real}
> coefficients. The homework extension carries the real-vs-rational-coefficient distinction ($\sqrt5$
> forces no partner under merely real coefficients). All graphs pre-drawn via `plot`+`\clip` (no
> sketch-from-scratch). Standards: **2023 VA SOL A2.EI.6b** (number and type of solutions) and
> **A2.EI.6a** (factored form from zeros or $x$-intercepts), completing **A2.EI.6c** over $\mathbb{C}$
> and using **A2.EI.6d** (counting against the degree as the verification); builds on **A2.EO.4a/b/c**
> (2.4), **A2.EI.2b** and the discriminant (2.5), **A2.EO.3b/c** (3.2--3.3), and **A2.F.2c** (3.0).
> Warm-up & exit ticket each fit one page (blank+key); notes 4pp (key 6pp), activity 3pp (key 4pp),
> homework 2pp (key 3pp); exit ticket includes an SOL-style MC item (which list \emph{cannot} be the
> complete zeros of a real quartic --- the answer lists $3i$ twice with no $-3i$).
> `make -C unit03/lesson05 all` → EXIT 0 (student 12pp, full 30pp); `make -C unit03 all` → EXIT 0.
> **Lesson 3.6 authored & builds (2026-07-26):** all components + keys + 10-slide deck done; the unit
> capstone, where every tool built separately becomes **one procedure that runs both directions**. The
> spine is the **five-step graph plan**: degree \& leading coefficient $\Rightarrow$ the arms (3.0, with
> the 3.1 shortcut that degrees add and leads multiply, so nothing is expanded); factor completely
> $\Rightarrow$ the $x$-intercepts (3.2--3.4); **multiplicity** $\Rightarrow$ cross (odd) / touch (even)
> / **flatten-then-cross** ($\ge3$); $f(0)$ $\Rightarrow$ one exact point; and the one genuinely new
> move, a **sign chart** --- test a single $x$ in each interval between consecutive zeros, in
> \emph{factored} form, keeping only the sign --- which delivers the positive/negative intervals and, as
> a by-product, catches the even-multiplicity fingerprint automatically (the sign fails to flip at a
> double zero). The **turning-point limit** $n-1$ is taught in both directions ($k$ turns $\Rightarrow$
> degree $\ge k+1$), and the plan's honest limit is stated out loud: it fixes every zero and both arms
> exactly but never the \emph{coordinates} of a turning point. Reversed (**A2.EI.6a**), a graph yields a
> factored equation, with $a$ solved from the **$y$-intercept** --- the only labeled point that is not a
> zero, which is exactly why an $x$-intercept gives the useless $0=0$ --- and the answer is always a
> \emph{possible} equation of least degree, since a graph can hide imaginary zeros (3.5) and even
> factors. The characteristics read (**A2.F.2a/c/d/e**) is done on $p(x)=x^4-5x^2+4$ (3.2's quartic) and
> corrects a Unit 2 habit head-on: the relative max at $(0,4)$ is \emph{not} absolute, an odd degree has
> \emph{no} absolute extrema, and an even degree gets one or the other but never both. The modeling
> strand (**A2.F.2f**) builds $V(x)=x(10-2x)(8-2x)=4x^3-36x^2+80x$ from a $10\times8$ sheet (the 3.0/3.1
> open-box model, third appearance), finds the **feasible domain** $0<x<4$, and insists that $x=5$ --- a
> genuine zero of $V$ --- is nonsense; on that domain the relative max ($\approx52.5$ in$^3$ near
> $x=1.5$) \emph{is} the absolute max, which is why it answers the question. Hook: two cubics with
> \emph{identical} zeros and identical arms, $(x-1)^2(x+2)$ vs.\ $(x-1)(x+2)^2$, whose graphs look
> nothing alike --- multiplicity is the feature that separates look-alikes. Tier E closes the unit's
> longest loop by running the box backward: a $48$ in$^3$ order becomes $x^3-9x^2+20x-12=0$, solved by
> the Rational Root Theorem (3.4) to $x=1,2,6$, with $6$ rejected and the \emph{two} feasible cuts
> explained as straddling the maximum (both appear as $48$ in the notes table). All graphs pre-drawn via
> `plot`+`\clip` --- students predict, match, read, and build, never sketch. Standards: **2023 VA SOL
> A2.F.2a/b/c/d/e/f/g** with **A2.EI.6a**; builds on A2.EO.3b/c and A2.EI.6b/c. Warm-up \& exit ticket
> each fit one page (blank+key); notes 5pp (key 6pp), activity 3pp (key 4pp), homework 3pp (key 3pp);
> exit ticket includes an SOL-style MC item (touch at $x=2$ with both arms down; distractors each break
> exactly one of degree parity, lead sign, and multiplicity).
> `make -C unit03/lesson06 all` → EXIT 0 (student 14pp, full 30pp); `make -C unit03 all` → EXIT 0.
> **All seven Unit 3 lessons (3.0--3.6) are now authored & building.**
> **Unit 3 tests authored & building (2026-07-26):** `tests/{practice_test,actual_test}` and
> `test_keys/{practice_test_key,actual_test_key}`, all four 4pp, published to `sample_test/` and
> `sample_test_key/` by the `drop` targets. Both forms are **skill-for-skill parallel with different
> numbers** and follow the Unit 2 architecture: **Part A** vocabulary matching, 8 pts (degree, leading
> coefficient, end behavior, multiplicity, turning point, Factor Theorem, Rational Root Theorem, FTA
> --- same eight terms, shuffled between forms); **Part B** MC, 12 pts (end behavior from degree/lead;
> a special product with the $a^2\pm b^2$ and forgot-to-double distractors; sum/difference of cubes
> with the SOAP sign-flip distractor; Remainder Theorem with $f(-r)$ as the distractor; ``which value
> is *not* a possible rational zero'' with the flipped fraction as the answer; the missing conjugate);
> **Part C** computation, 40 pts in 8 items --- read a pre-drawn cubic graph with a cross and a
> multiplicity-2 touch (practice $-(x+1)(x-2)^2$, actual $(x-1)(x+2)^2$, both asking for the *absolute*
> extrema, answer **none**), subtract/multiply + degree \& lead of the product, factor completely
> (GCF, cubes, grouping), long division with a **placeholder** + a Remainder-Theorem factor check,
> synthetic division from a given zero, RRT list-then-solve with a **fractional** zero from a non-monic
> factor (practice $\tfrac12$, actual $\tfrac13$), solve over $\mathbb{C}$ by grouping (count first by
> FTA, then $x$-intercepts vs.\ imaginary pair), and build a least-degree real polynomial from a zero
> and an imaginary one; **Part D** extended response, 12 pts --- the five-step graph plan on a
> degree-4 factored form (degrees add / leads multiply, multiplicities, $y$-intercept, **sign chart**
> with no flip at the double zero, $n-1$ turning points) and the open-box model with feasible domain
> plus a genuine-but-meaningless zero to reject. Keys carry per-part `teachernote` scoring rubrics
> (Part D at 6 pts each). Total 72 pts. `make -C unit03/tests all` and
> `make -C unit03/test_keys all` → EXIT 0; `make -C unit03 student` → 87pp,
> `make -C unit03 full` → 195pp (practice test in both, practice key in the full packet only; the
> actual test and its key stay out of every packet). Note `make -C unit03 all` builds only the
> lessons --- the tests need their own two `make` calls.
> **Unit 3 is complete (all lessons + assessments).** Unit 4's map is confirmed and scaffolded; see
> its section below.
- **3.0** Characteristics of polynomial functions *(introduces: degree/leading
  coefficient → end behavior, odd/origin symmetry, relative vs. absolute extrema,
  turning points, zero multiplicity)* — A2.F.2a/b/c/d/e/g
- **3.1** Operations with polynomials (add, subtract, multiply) — A2.EO.3a
- **3.2** Advanced factoring (GCF, grouping, sum & difference of cubes,
  two-variable expressions) — A2.EO.3b/d
- **3.3** Dividing polynomials (long & synthetic); Remainder & Factor Theorems — A2.EO.3c
- **3.4** Zeros of polynomials: the Rational Root Theorem *(forward-solve — RRT lists
  candidates, synthetic division tests/depresses, factor completely, solve for real zeros)*
  — A2.EI.6c/d
- **3.5** Fundamental Theorem of Algebra & complex zeros *(count & build — number/type of
  solutions, complex-conjugate pairs, multiplicity, write a polynomial from its zeros)*
  — A2.EI.6a/b (+ c/d)
- **3.6** Graphing polynomial functions & modeling — A2.F.2a–e/g

### Unit 4 — Rational Functions
> **Status (map confirmed & scaffolded 2026-07-26):** lesson map locked at **8 lessons (4.0–4.7)**.
> Three changes from the original ~6-lesson draft, all driven by `spec/algebra2-vdoe-sol.pdf`:
> (1) **variation is required, not optional** — **A2.F.1d** (directly/inversely proportional from a
> table; write the equation and graph a direct or inverse variation in context) is a listed
> knowledge-and-skill with no other home in the course (Units 5–7 are radical/exp/log), and
> $y=k/x$ *is* the rational parent — so it becomes a real lesson, **4.7**, as the modeling capstone
> (matching the 2.7 / 3.6 pattern); (2) **the draft's single "Graphing" lesson was split** into
> **4.4** (parent $y=1/x$ + transformations) and **4.5** (analyze-and-graph from an equation),
> because unlike polynomials, **rational functions *are* in A2.F.1's family list**, so
> **A2.F.1a/b/c/e** (parent-graph distinction, write the equation from a graph, graph via
> $f(x)+k$, $f(kx)$, $f(x+k)$, $kf(x)$) is a separate obligation from **A2.F.2a/g/h** — same
> overload that forced the Unit 3 4.4/4.5 split; (3) **complex algebraic fractions (A2.EO.1c)**,
> unbulleted in the draft, attach to **4.3** since simplifying one *is* combine-then-divide.
> **Slant/oblique asymptotes are NOT in the 2023 SOL** — A2.F.2h covers vertical and horizontal
> only. Decision: teach slant as **Tier E enrichment in 4.5** (a callback to 3.3 polynomial
> division) and **never assess it**; the §3 spine row was amended accordingly.
> Scope guardrails from the standards: **A2.EO.1b** limits expressions to **monomial and binomial
> factors, linear and quadratic**; **A2.EI.4b** likewise limits rational equations to **factorable
> linear and quadratic** expressions. Keep 4.1–4.3 and 4.6 inside those bounds.
> All 8 lesson dirs `unit04/lesson00`–`lesson07` scaffolded with skeleton `main.tex` for lesson
> plan + cover, warmup, notes, activity, exit_ticket, homework, slides, and each `*_key`. Unit
> assessments scaffolded: `tests/{practice_test,actual_test}`, `test_keys/`, `sample_test{,_key}/`.
>
> **TODO when reviewing this unit — three slide decks may have colliding fractions (found
> 2026-07-28).** They use `\renewcommand{\arraystretch}{1.5}` on a `tabular` containing `\dfrac`
> with no explicit row skip. That is the exact pattern that broke slide 4 of Lesson 1.2, where
> each fraction's denominator overlapped the next row's numerator: `\arraystretch` scales a strut
> derived from `\baselineskip`, which a `\dfrac` overshoots. **Not yet rendered — these three are
> suspects, not confirmed breaks** (1.2 used a 1.6 stretch; 1.5 may or may not clear it).
>
> | Deck | Line | `\dfrac`s |
> | --- | --- | --- |
> | `unit04/lesson00/slides/main.tex` | 124 | 4 |
> | `unit04/lesson05/slides/main.tex` | 153 | 3 |
> | `unit04/lesson07/slides/main.tex` | 68 | 1 |
>
> Fix, if they do collide, is the one applied to 1.2: drop the `\arraystretch` line and space the
> rows explicitly with `\\[14pt]`, which sizes to the actual content instead of to the font.
> Check by rendering the affected page: `pdftoppm -png -r 110 -f N -l N <deck>.pdf /tmp/chk`.
> One more site outside this unit carries the same pattern — `unit01/lesson01/slides/main.tex:95`
> (stretch 1.35, 1 `\dfrac`); see the Unit 1 status.
> **Lesson 4.0 authored & builds (2026-07-26):** all components + keys + 10-slide deck done; the lesson
> where the course loses \emph{continuity}. Everything hangs on one sentence --- **the denominator runs
> the show** --- introduced from the Warm-Up, whose three items seed the three new ideas numerically
> before any of them is named: solving *denominator* $=0$ (the 3.2 factoring toolkit, reused as the
> domain-restriction engine); evaluating $\frac{1}{x-1}$ in **two** tables, one closing in on $x=1$
> ($-10,-100,100,10$ --- blows up *and* flips sign) and one running out to $x=1001$
> ($0.1,0.01,0.001$ --- settles down); and cancelling $\frac{x^2-4}{x-2}$ only to find the original
> gives $\tfrac00$ at $x=2$. Introduces **A2.F.2h** --- the *equations* of **vertical** and
> **horizontal** asymptotes --- plus **holes** and **domain restrictions**, organized around two
> contrasts that carry the whole lesson: a vertical asymptote is a restriction on *inputs* (untouchable,
> and the reason intervals must be written as **unions**) while a horizontal asymptote only describes
> *outputs* at the far ends (so a graph **may** cross it --- checked on $\frac{2x}{x^2+1}$ at $x=0$);
> and the **cancel test** decides whether a restriction is a wall or a single missing point. The
> horizontal asymptote is taught as the **degree comparison** ($n<m\Rightarrow y=0$; $n=m\Rightarrow$
> ratio of leading coefficients; $n>m\Rightarrow$ none), with the horizontal asymptote presented as
> *being* the end-behavior statement (**A2.F.2g**). Anchor $f(x)=\frac{x+2}{x-1}$ (VA $x=1$, HA $y=1$,
> zero $(-2,0)$, $y$-int $(0,-2)$, decreasing on *each* branch, range excludes $1$); hole examples
> $\frac{x^2-4}{x-2}=x+2$ ($x\neq2$, hole $(2,4)$) and the both-at-once
> $\frac{x-3}{x^2-9}=\frac{1}{x+3}$ ($x\neq3$: hole at $3$, wall at $-3$); supporting graphs
> $\frac{4}{x^2-4}$ (two walls, no $x$-intercept --- constant numerator), $\frac{2}{x+2}$,
> $\frac{x-2}{x+1}$, $\frac{x^2-1}{x-1}$ (a *line with a hole*), $\frac{x-4}{x-2}$,
> $\frac{x^2-x-6}{x-3}$. Closes on the **A2.F.2b** compare-and-contrast table (polynomial: continuous,
> domain all reals, no asymptotes, arms to $\pm\infty$ / rational: possibly discontinuous, restricted
> domain, asymptotes, arms flattening, intervals as unions) --- what makes this a Lesson 0 rather than a
> graphing lesson. Flagged traps: setting the *numerator* to zero for a VA; answering ``$1$'' instead of
> ``$x=1$''; announcing a VA at *every* excluded value without the cancel test; reading restrictions off
> the *simplified* form (the same error that becomes extraneous solutions in 4.6); one interval spanning
> a wall; and both overgeneralizations about asymptotes (that a HA can never be crossed, and that every
> rational function must have a VA). Modeling (**A2.F.2f**): activity Tier E interprets average cost
> $A(n)=\frac{6n+250}{n}$ (HA $y=6$ is the true per-shirt cost, never reached because
> $A(n)=6+\frac{250}{n}$; $n=0$ meaningless), and the homework extension reads a drug concentration
> $C(t)=\frac{5t}{t^2+1}$ --- HA $y=0$ as the drug clearing, peak $2.5$ mg/L at $t=1$, the graph
> *sitting on* its HA at $t=0$, and the deliberately unsettling case of a rational function with **no**
> vertical asymptote at all (domain $t\ge0$ comes from context, not algebra). All graphs pre-drawn via
> `plot`+`\clip` with branches truncated at the window edge and holes as open circles (no
> sketch-from-scratch). Standards: **2023 VA SOL A2.F.2h** (new), **A2.F.2a** (incl. graphs with
> discontinuities), **A2.F.2c**, **A2.F.2g**, **A2.F.2b**; builds on A2.EO.3b (3.2 factoring).
> **Slant asymptotes deliberately absent** (not in the 2023 SOL; Tier E of 4.5 only, never assessed).
> Warm-up & exit ticket each fit one page (blank+key); notes 5pp, activity 3pp, homework 3pp, cover 1pp
> --- every key paginates identically to its blank; exit ticket includes an SOL-style MC item
> ($h(x)=\frac{x-4}{x^2-16}$: hole at $x=4$, wall at $x=-4$; the three distractors ignore the
> cancelling, swap the two factors, and read restrictions off the simplified form).
> `make -C unit04/lesson00 all` → EXIT 0 (student 14pp, full 28pp).
> **Lesson 4.1 authored & builds (2026-07-26):** all components + keys + 9-slide deck done; the algebra
> that *produces* 4.0's holes. Everything hangs on one sentence --- **cancelling never restores an
> input** --- and it is earned rather than announced: the Warm-Up refutes ``$\frac{3+6}{3}=6$'' by
> computing the true value $3$ (so \emph{factors, not terms} is a fact students proved), and the Hook
> puts $A(x)=\frac{x^2-x-6}{x^2-9}$ beside its cancelled form $B(x)=\frac{x+2}{x+3}$ in a four-column
> table of values: they agree at $x=0,1,4$ ($\tfrac23,\tfrac34,\tfrac67$) and disagree at exactly one
> input, $x=3$, where $A$ gives $\tfrac00$ and $B$ gives $\tfrac56$. The lesson is a **four-step
> procedure** --- factor completely (the 3.2 toolkit) $\rightarrow$ **list the restrictions from the
> \emph{original} denominator** $\rightarrow$ divide out shared factors $\rightarrow$ write the simplest
> form \emph{with} its restrictions --- with step 2 deliberately placed before step 3 because after
> cancelling one restriction is invisible. Cancelling is justified, not assumed: $\frac{ac}{bc}
> =\frac ab\cdot\frac cc=\frac ab$ ($b,c\neq0$), which explains in one line both why $c$ must be a
> **factor** and why it must be nonzero. Covers **monomial factors**
> ($\frac{12x^3y}{18x^5y^2}=\frac{2}{3x^2y}$, $x,y\neq0$ --- the A2.EO.1b monomial clause), GCF cases
> ($\frac{3x^2-12}{x^2+x-6}$), and **opposite binomials** ($\frac{a-b}{b-a}=-1$; $\frac{x^2-16}{4-x}
> =-(x+4)$), contrasted with $x+3$ vs.\ $3+x$ (only \emph{subtraction} cares about order). Closes on
> **A2.EO.1d equivalence**: same value at every input \emph{both} accept --- so two equivalent forms can
> have different \emph{domains} --- checked two ways (factor, or test an input, with the asymmetry named:
> one match proves nothing, one mismatch disproves everything). Unifying thread: the anchor's pre-drawn
> graph shows $x=-3$ (factor stays) as a **vertical asymptote** and $x=3$ (factor cancels) as a **hole**
> at $\left(3,\tfrac56\right)$ whose height comes from the \emph{simplified} form --- 4.0's cancel test
> run from the algebra side. Flagged traps: cancelling **terms** ($\frac{x^2+9}{x+3}=x+3$, killed
> numerically at $x=1$, plus the Unit 3 fact that $x^2+9$ is prime); **restrictions read off the
> simplified denominator** (the signature error, and the direct ancestor of extraneous solutions in
> 4.6); a lost $-1$ from opposite binomials; a simplified form with no restriction list (half an
> answer); and a squared factor cancelled entirely (wall, not hole). Homework closes with
> $g(x)=\frac{x^2+2x-8}{x-2}$ --- a rational function whose graph is a **line** with a hole at $(2,6)$
> and no vertical asymptote --- and a design task previewing 4.5 (build an expression with a hole at
> $x=2$ and a wall at $x=-1$). All graphs pre-drawn via `plot`/line + `\clip` with holes as open circles
> (no sketch-from-scratch). Standards: **2023 VA SOL A2.EO.1b** (justify and determine equivalent
> rational expressions, monomial and binomial factors, linear and quadratic) and **A2.EO.1d**
> (equivalence of forms); builds on **A2.EO.3b** (3.2) and 4.0's restrictions/holes; prerequisite for
> A2.EO.1a (4.2--4.3), A2.F.2h from the equation (4.5), and A2.EI.4c (4.6). Warm-up & exit ticket each
> fit one page (blank+key); notes 4pp, activity 3pp, homework 2pp (key 3pp --- extra page is the teacher
> note), cover 1pp; exit ticket includes an SOL-style MC item ($\frac{4-x^2}{x^2-x-2}$; the three
> distractors drop the $-1$, read restrictions off the simplified denominator, and cancel the $x^2$
> terms). `make -C unit04/lesson01 all` → EXIT 0 (student 12pp, full 26pp).
> **Lesson 4.2 authored & builds (2026-07-26):** all components + keys + 10-slide deck done; the lesson
> where the restriction list stops being readable off the page. Multiplying is 4.1's four steps with one
> more denominator --- the only genuinely new mechanical idea is that cancelling runs **across the whole
> product** (any numerator factor against any denominator factor) --- so the weight of the lesson sits on
> **division**, and specifically on the **three sources of a restriction**: for $\frac AB\div\frac CD$,
> $B\neq0$ (the dividend must exist), $D\neq0$ (the divisor must exist --- **invisible after** the flip,
> since $D$ moves upstairs), and $C\neq0$ (**you cannot divide by zero**, and a fraction is zero exactly
> when its \emph{numerator} is --- **invisible before** the flip). The organizing sentence is
> **``flipping trades one blind spot for another''**: read the restrictions off the problem *as written*,
> then add the divisor's numerator. Source 3 is *earned rather than announced* --- Warm-Up item 1(c) asks
> which value $n$ may not have in $\frac49\div\frac n{15}$ (answer $0$) before any letters appear, and the
> Hook then puts $Q(x)=\frac{x+1}{x-5}\div\frac{x-2}{x+3}$ beside its flipped form
> $R(x)=\frac{(x+1)(x+3)}{(x-5)(x-2)}$ in a table at $x=0,1,2,-3$: they agree ($\tfrac3{10}$, $2$), are
> **both** undefined at $x=2$ *for different reasons* (denominator in $R$; zero divisor in $Q$), and part
> company at $x=-3$, where $Q$ has no value and $R$ gives $0$. Also taught: multiplying is never done by
> expanding (an expanded product **hides its own factors** --- the Unit 3 cost argument), and **flip
> before you cancel**, disproved numerically because top-with-top *does* happen to work for division while
> the other diagonal never does ($\frac43\div\frac54$: $\frac1{15}$ vs.\ $\frac{16}{15}$; with letters,
> $\frac x4\div\frac5x=\frac{x^2}{20}$, not $\frac1{20}$). Anchors: the product
> $\frac{x^2-9}{x^2+2x-8}\cdot\frac{x+4}{x^2+3x}=\frac{x-3}{x(x-2)}$ ($x\neq0,2,-3,-4$, two invisible) and
> the quotient $\frac{x^2-4}{x^2+7x+12}\div\frac{x^2+2x}{x+3}=\frac{x-2}{x(x+4)}$ ($x\neq0,-2,-3,-4$,
> one value from each of the three sources). Opposite binomials (4.1) carry forward inside products
> ($\frac{x^2-25}{x+2}\cdot\frac{2x+4}{5-x}=-2(x+5)$). Graph-reading closes the notes:
> $P(x)=\frac{x^2-1}{x}\cdot\frac{x}{x+1}$ is the **line $y=x-1$ with two holes**, at $(0,-1)$ and
> $(-1,-2)$ --- one per denominator --- pre-drawn with open circles (no sketch-from-scratch). Repeated
> beat: **a polynomial answer still carries restrictions** ($2x(x-6)$ with $x\neq0,-6$; a homework item
> whose written denominators are the constants $2$ and $5$, so *every* restriction comes from the divisor's
> numerator). Flagged traps: multiplying out first; missing the divisor's-numerator restriction (the
> signature error); cancelling across the $\div$; flipping the *first* fraction; restrictions read off the
> answer (4.1's error, now worse with two denominators); a lost $-1$. Tier E adds a **restriction
> detective** table (attribute each of $x\neq0,1,-2,-3$ to its source, one value having *two*), a
> build-it-backwards division, and a rectangle whose length is recovered by division, verified by
> multiplying back, with the source-3 restriction interpreted geometrically (zero width) and a feasible
> domain that is a **union**. Standards: **2023 VA SOL A2.EO.1a** (multiply, divide, simplify the result),
> applying **A2.EO.1b** and **A2.EO.1d**; builds on **A2.EO.3b** (3.2) and 4.1; prerequisite for
> **A2.EO.1a/c** (4.3 --- a complex fraction *is* a division) and **A2.EI.4c** (4.6). Warm-up & exit
> ticket each fit one page (blank+key); notes 4pp, activity 2pp (key 3pp --- extra page is the teacher
> note), homework 2pp (key 3pp), cover 1pp; exit ticket includes an SOL-style MC item on
> $\frac{x^2-25}{x^2+3x}\div\frac{x-5}{x+3}$ (distractors: restrictions off the answer / divisor's
> numerator forgotten / wrong fraction flipped). `make -C unit04/lesson02 all` → EXIT 0 (student 11pp,
> full 27pp).
> **Lesson 4.3 authored & builds (2026-07-26):** all components + keys + 11-slide deck done; the lesson
> where the denominators finally have to agree, and the standard's other half (**A2.EO.1c**) arrives.
> Three sentences carry it, one per leg: **the minus sign owns the whole numerator**, **build the LCD out
> of factors, not by multiplying denominators**, and **the main fraction bar is a division sign**. The
> subtraction rule is *earned rather than announced* --- Warm-Up 2(a) puts $9-(4-6)=11$ beside
> $9-4-6=-1$ before any letters appear, and the Hook then runs
> $D(x)=\frac{4x-1}{x+3}-\frac{2x-7}{x+3}$ against two students' answers in a table at $x=0,1,-3$:
> Dev's $\frac{2x-8}{x+3}$ (parentheses dropped) never matches, and Elin's plain $2$ matches the value
> but is still unfinished, because the last column exposes the missing $x\neq-3$ --- a horizontal line
> with a hole in it. Covers **like denominators** (add numerators, keep the denominator; the
> $\frac12+\frac12\ne\frac24$ disproof), the **parenthesis rule** on subtraction, and the **six-step LCD
> procedure** (factor $\rightarrow$ build the LCD as each *distinct* factor to its *highest* power
> $\rightarrow$ restrictions $\rightarrow$ **building factor** $\frac kk$ $\rightarrow$ combine
> $\rightarrow$ factor-and-divide-out), across monomial ($\frac{5}{6x^2}+\frac{7}{4x}$), binomial, and
> two-trinomial cases ($\frac{2}{x^2+5x+6}+\frac{3}{x^2-9}=\frac{5x}{(x+2)(x+3)(x-3)}$, where the shared
> $(x+3)$ enters the LCD *once*), plus **opposite binomials** in denominators
> ($\frac{4}{x-5}+\frac{2}{5-x}=\frac{2}{x-5}$ --- the LCD was never $(x-5)(5-x)$). The unifying idea is
> **``the LCD *is* the restriction list''**: it already contains every factor of every original
> denominator, so its factors hand over every excluded value for free --- with the standing warning that
> it must be built from the *original* denominators, never read off the answer (4.1's error at its third
> appearance). **Complex fractions** are taught in the standard's own words, as a *quotient of simple
> fractions*: Method 1 (combine top, combine bottom, keep--change--flip --- 4.2 reused outright) is the
> assessed method, Method 2 (multiply through by the LCD of the inner fractions) is the speed trick, and
> the conceptual beat is that **Method 2 erases the evidence for the inner-denominator restriction**
> since clearing them is exactly what it does. Restrictions come from two levels --- every inner
> denominator, and the *whole bottom*, which is Lesson 4.2's **source 3** in a new costume. Anchors: the
> subtraction $\frac{3}{x-3}-\frac{18}{x^2-9}=\frac{3}{x+3}$, $x\neq3,-3$, which lands on **exactly the
> Warm-Up's item-3 answer** from the opposite direction (the recognition is the hook of Section 3), and
> the complex fraction $\frac{1/x+1/2}{1/x-1/4}=\frac{2(x+2)}{4-x}$, $x\neq0,4$. Graph-reading closes the
> notes: that one subtraction produces **one hole and one wall** --- $y=\frac{3}{x+3}$ with a wall at
> $x=-3$ and a hole at $\left(3,\frac12\right)$ --- both from denominators that no longer appear
> (pre-drawn `plot`+`\clip` with the hole as an open circle; no sketch-from-scratch). Flagged traps: the
> **lost parenthesis** (the signature error, and worth extra time because the wrong answer often
> *simplifies more prettily* than the right one --- the homework error gallery is built on exactly that);
> **adding the denominators** ($\frac1x+\frac13=\frac{2}{x+3}$, killed at $x=1$); the LCD built as a
> *product* (not wrong, only expensive --- and it usually costs the cancellation); a doubled LCD from
> opposite binomials; restrictions read off the answer; and no restriction at all on a constant or
> polynomial answer. Modeling (**A2.F.2f**): Tier E's two paint crews (combined rate
> $\frac{2x+3}{x(x+3)}$, together-time $\frac{x(x+3)}{2x+3}$ --- a complex fraction, sanity-checked at
> $x=6$ giving $3.6$ h) and the homework's round trip ($30$ mi out at $x$, back at $x+5$;
> $T=\frac{30(2x+5)}{x(x+5)}$, average speed $\frac{2x(x+5)}{2x+5}=12$ mi/h at $x=10$ --- *not* the $12.5$
> everyone predicts, because the slower leg takes longer and counts for more). Homework problem 6 is the
> **A2.EO.1d** item, pairing a genuinely equivalent pair with one that only looks equivalent (the anchor
> versus $\frac{3}{x+3}$, which accepts $x=3$). Standards: **2023 VA SOL A2.EO.1a** (add and subtract) and
> **A2.EO.1c** (recognize and simplify a complex algebraic fraction), applying **A2.EO.1b** and
> **A2.EO.1d**; builds on **A2.EO.3b** (3.2) and 4.1--4.2; prerequisite for **A2.EI.4b/c** (4.6 --- solving
> begins by multiplying through by an LCD, and an extraneous solution is one of today's excluded values
> returning). Warm-up & exit ticket each fit one page (blank+key); notes 5pp, activity 3pp, homework 3pp,
> cover 1pp --- **every key paginates identically to its blank**; exit ticket includes an SOL-style MC item
> on $\frac{1/x-1/5}{x-5}$ (distractors: the lost $-1$ from opposite binomials / the main bar's restriction
> forgotten / never simplified, restrictions read off its own denominator).
> `make -C unit04/lesson03 all` → EXIT 0 (student 14pp, full 30pp); `make -C unit04 all` → EXIT 0.
> **Lesson 4.4 authored & builds (2026-07-26):** all components + keys + 11-slide deck done; the lesson
> where the unit's expressions go back on the grid. Everything hangs on one sentence --- **the asymptotes
> are the parent's axes, and they travel with the graph** --- and it is discovered numerically before it is
> named: the Hook puts two tables side by side, $y=\frac1x$ at $x=-2\ldots2$ and $y=\frac{1}{x-3}$ at
> $x=1\ldots5$, whose \emph{output} columns come out identical ($-\frac12,-1,\text{undef.},1,\frac12$), so
> the blow-up moved to $x=3$ while the settling-down value stayed at $y=0$. Introduces the **rational
> parent** $f(x)=\frac1x$ --- the two-branch **hyperbola**, VA $x=0$, HA $y=0$, origin symmetry (3.0),
> decreasing on *each* branch (4.0's union rule), and the fact no other parent in the course shares:
> **no intercepts at all** (a fraction is zero only when its numerator is; $x=0$ is not in the domain).
> Then **general form** $g(x)=\frac{a}{x-h}+k$ read in a fixed order --- $h\Rightarrow$ VA, $k\Rightarrow$ HA,
> $(h,k)$ the **center** where they cross (*not* a point of the graph), $a$ the stretch/reflection that moves
> **neither** asymptote. The four A2.F.1c transformations are all met, including the honest treatment of
> $f(kx)$: on this parent it collapses into $kf(x)$, since $\frac{1}{4x}=\frac{1/4}{x}$ --- which is why one
> letter $a$ suffices. Anchor $g(x)=\frac{2}{x-3}+1$ (VA $x=3$, HA $y=1$, center $(3,1)$, $y$-int $\frac13$,
> $x$-int $(1,0)$), plus the sharpened asymptote claim: a *transformed parent* **never** crosses its HA
> (that needs $\frac{2}{x-3}=0$) --- stronger than 4.0's "may cross," and worth contrasting with
> $\frac{2x}{x^2+1}$. **A2.F.1b** gets its own section (asymptotes $\rightarrow h,k$; one point $\rightarrow a$;
> **second point $\rightarrow$ check**) on $y=\frac{2}{x+1}-2$, and it is flagged as the likeliest SOL item on
> the standard. Closes on **A2.F.1a/e**: a compare-and-contrast table against $y=x^2$/$y=|x|$, then **the
> disguise** --- $\frac{x-1}{x-3}=\frac{(x-3)+2}{x-3}=1+\frac{2}{x-3}$, which *is* the anchor, and which lands
> on exactly the Warm-Up's item-3 pattern from the opposite direction; this is also *why* 4.0's degree rule
> holds for linear-over-linear, since the leftover constant **is** the ratio of the leading coefficients.
> Flagged traps: the **sign of $h$** (the signature error, costlier here because it puts the wall on the
> wrong side of the axis); the HA **read off the numerator** ($a$ and $k$ do different jobs); the two roles
> **crossed**; "the parent goes through $(0,0)$"; **range** given as "all reals" (the HA is a *range*
> exclusion); decreasing on $(-\infty,\infty)$; and $(h,k)$ plotted as a point of the graph. Modeling
> (**A2.F.2f**): activity Tier E dilutes brine, $C(x)=\frac{20}{5+x}$ (HA $y=0$ --- the salt never leaves;
> VA $x=-5$ is real algebra and meaningless chemistry; halving the concentration costs 5, then 10, then 20
> more liters --- diminishing returns), and the homework models free throws, $P(x)=\frac{12+x}{20+x}
> =1-\frac{8}{x+20}$ (HA $y=1$: $90\%$ costs 60 makes in a row, $95\%$ costs 140, $100\%$ takes forever).
> Homework problem 5 is the **A2.F.1e** table item --- constant *differences* ($y=3x$) against constant
> *products* ($xy=12$) --- which quietly seeds **4.7**'s inverse variation; do not name it there. All graphs
> pre-drawn via `plot`+`\clip` with branches truncated at the window edge (no sketch-from-scratch); the
> activity's three matching windows share $y\in[-5,5]$ so they sit on a common baseline. Standards:
> **2023 VA SOL A2.F.1a/b/c/e** (new), applying **A2.F.2h**, **A2.F.2a**, **A2.F.2c**, **A2.F.2g**, and
> **A2.F.2f**; builds on Units 1--2 transformations and 4.3's combining. Warm-up & exit ticket each fit one
> page (blank+key); notes 5pp, activity 3pp, homework 3pp, cover 1pp --- **every key paginates identically to
> its blank**; exit ticket includes an SOL-style MC item (VA $x=-4$, HA $y=3$; the three distractors flip the
> sign of $h$, swap the two jobs, and read the HA off the numerator).
> `make -C unit04/lesson04 all` → EXIT 0 (student 14pp, full 30pp); `make -C unit04 all` → EXIT 0.
> **Lesson 4.5 authored & builds (2026-07-27):** all components + keys + 13-slide deck done; the lesson
> where the asymptotes come off the face of the equation. Everything hangs on one sentence ---
> **factor it, and every feature is already in there; the sign chart is what turns the list into a
> picture** --- and the Hook is an \emph{argument for the tool} rather than a warm-up: three pre-drawn
> graphs that all have VA $x=-2$, VA $x=3$, an $x$-intercept $(1,0)$, and branches flattening toward
> $y=0$, exactly one of which is $\frac{x-1}{(x+2)(x-3)}$ (the distractors are the global sign flip and
> a squared $(x+2)$ that does not change sign at the wall). Guesses go on the board and stay there
> until the Section 4 sign chart reads \emph{below, above, below, above} and eliminates B and C by
> arithmetic. Organized as **the five-step build**, posted and held to all period: factor; restrictions
> off the **original** denominator + the cancel test (hole *with coordinates*, from the simplified
> expression / wall); degree comparison; intercepts **computed** ($x$-int from the *simplified*
> numerator, $y$-int $=f(0)$); sign chart whose **boundary points are the $x$-intercepts and the
> vertical asymptotes --- never the holes**, since the sign cannot change where the function is the
> same expression on both sides. Anchor A $f(x)=\frac{x-1}{x^2-x-6}$ (two walls, HA $y=0$, $(1,0)$,
> $(0,\frac16)$, four intervals) carries the lesson's sharpest new claim: it **crosses** its horizontal
> asymptote, at its own $x$-intercept --- which reconciles 4.0's "may cross" with 4.4's "never," both
> being the single fact that a fraction is zero only when its numerator is. Anchor B
> $g(x)=\frac{x^2-4}{x^2-x-6}$ adds the hole $(-2,\frac45)$, wall $x=3$, HA $y=1$, and the trap that
> $(-2,0)$ is **not** an $x$-intercept though the original numerator vanishes there; simplified it is
> $\frac{x-2}{x-3}=1+\frac{1}{x-3}$ --- yesterday's anchor family with one point punched out, so
> **4.5 did not replace 4.4, it surrounded it**. Flagged traps: restrictions read off the *simplified*
> form (the costliest, and tomorrow's extraneous solution); a wall announced at every excluded value
> without the cancel test; a cancelled zero called an intercept; the hole used as a boundary point;
> degrees compared factor-by-factor; refusing "no $x$-intercept" when the numerator is a nonzero
> constant; assuming signs alternate (homework 1(f), $\frac{x^2-9}{x^2-6x+9}$, breaks it --- two copies
> down, one up, so the restriction survives as a wall and there is *no* hole); one interval spanning a
> wall. Modeling (**A2.F.2f**) deliberately reverses 4.4's: activity Tier E is the **round trip**,
> $T(x)=\frac{30}{x}+\frac{30}{x+10}=\frac{60x+300}{x(x+10)}$ (4.3 run forwards), where the wall $x=0$
> and the floor $y=0$ both mean something and $x=-10$, $(-5,0)$ are negative speeds; the homework is
> **pollution cost**, $C(p)=\frac{25p}{100-p}$ ($25\to100\to225\to475\to2475$), where the *vertical*
> asymptote carries the meaning (no finite budget buys $100\%$ removal) and HA $y=-25$ means nothing.
> **Slant asymptotes appear once**, as activity Tier E Part 2 --- divide $\frac{x^2-4}{x+1}$ by 3.3
> long division to get $x-1-\frac{3}{x+1}$ against a pre-drawn dashed $y=x-1$ --- explicitly labelled
> enrichment and **never assessed**. All graphs pre-drawn via `plot`+`\clip` with holes as open circles
> (no sketch-from-scratch). Standards: **A2.F.2h**, **A2.F.2a**, **A2.F.2g** (new emphasis), applying
> **A2.F.1c**, **A2.F.2c**, **A2.F.2f**; builds on A2.EO.3b (3.2), A2.EO.1b/d (4.1), and the 3.6 sign
> chart. Warm-up & exit ticket each fit one page (blank+key); notes 5pp, activity 4pp, homework 3pp,
> cover 1pp --- **every key paginates identically to its blank**; exit ticket includes an SOL-style MC
> item (hole $x=1$, VA $x=-2$, HA $y=1$; the three distractors ignore the degree comparison, flip every
> sign, and cancel the wrong factor). `make -C unit04/lesson05 all` → EXIT 0 (student 15pp, full 33pp);
> `make -C unit04 all` → EXIT 0.
> **Lesson 4.6 authored & builds (2026-07-27):** all components + keys + 11-slide deck done; the unit's
> payoff loop, where the excluded values students have listed since 4.1 come back as answers to throw
> away. Everything hangs on one sentence --- **clearing the denominators solves a \emph{different}
> equation; the check is what brings you back** --- and the case for it is made before any procedure is
> taught. The Warm-Up seeds the justification with no algebra in it at all: start from the false
> statement $5=2$, multiply both sides by $3$ (still false, reversible by dividing), then by $\mathbf0$
> and get $0=0$ (true, and *not* reversible). The Hook then makes checking non-negotiable with two
> equations whose algebra is **literally identical** --- $\frac{x^2}{x-2}=\frac{4}{x-2}$ and
> $\frac{x^2}{x-3}=\frac{4}{x-3}$, both clearing to $x^2=4$ with candidates $\pm2$ --- but which have
> one solution and two; the row to dwell on is (I) at $x=2$, where both sides read $\frac40$ and the
> honest answer to ``true or false?'' is **neither**. Taught as **four steps in a fixed order**: factor
> every denominator and write the restriction list *at the top of the page*; multiply **every term** by
> the LCD (both *sides*, not just the fractions --- the term with no denominator is the one students
> drop); solve the linear or quadratic left behind; check each candidate against the list. Two framings
> carry the lesson: the LCD is an *expression*, so at each excluded value it **is** zero and the step is
> irreversible exactly there (**A2.EI.4d**); and therefore **an extraneous solution is never a random
> number --- it is always on the Step 1 list**, which turns Step 4 into comparing two short lists rather
> than re-substituting. A dedicated opening section separates **4.3 from 4.6** (*you may clear
> denominators only when there is an equals sign*) --- the predictable carry-over error after a
> combining lesson. Anchors: $\frac{6}{x}-\frac{2}{x-1}=1$ (candidates $2,3$, nothing thrown away) and
> $\frac{x}{x+1}+\frac{2}{x-1}=\frac{2}{x^2-1}$ ($-1$ extraneous, $0$ survives). **4.5 pays its debt in
> the graphical check (A2.EI.4b/c):** combining the second anchor onto one side gives
> $\frac{x(x+1)}{(x-1)(x+1)}=\frac{x}{x-1}$ --- one cancelling factor, one surviving --- so yesterday's
> cancel test sorts today's candidates, and the rule is boxed: **true solutions are $x$-intercepts;
> extraneous candidates are holes (or walls)**. Also covered: cross-multiplying presented as Step 2
> pre-cancelled and valid *only* for a proportion; and ``no solution'' as a complete answer, with its
> **two distinct causes** distinguished (every candidate extraneous, vs.\ the cleared equation itself
> never true --- homework 2(d) vs.\ 2(f) puts both on one page). The lesson's sharpest conceptual item is
> homework 4(d): $-1$ is excluded and was *never* a candidate, so **every extraneous solution is an
> excluded value, but not every excluded value is extraneous**. Modeling (**A2.EI.4a/c**): activity
> Tier E's work-rate problem ($\frac1x+\frac1{x+3}=\frac12$, candidates $3$ and $-2$, *neither
> extraneous* --- $-2$ is rejected by **context**) and the homework's river current
> ($\frac{6}{4-c}+\frac{6}{4+c}=4$, $c=\pm2$, with $c\neq4$ a 4.5 vertical asymptote meaning the paddler
> exactly matches the river). Activity Tier E part 3 answers the question sharp students ask --- clearing
> can *add* solutions but dividing by a variable expression *loses* them --- on
> $\frac{x^2}{x-1}=\frac{x}{x-1}$, where the careless division discards the only real solution ($0$) and
> keeps the extraneous one ($1$). Flagged traps: no restriction list on the page; restrictions off the
> *simplified* form; only the fractions multiplied by the LCD (homework 5's error analysis is built on
> it, and Tier A's error analysis has **no error in it at all** --- every line correct, Step 4 skipped);
> cross-multiplying a three-term equation; a negative or fractional answer rejected on reflex; and
> ``extraneous'' used as a synonym for ``rejected.'' Standards: **2023 VA SOL A2.EI.4b** (new),
> **A2.EI.4c**, **A2.EI.4d**, **A2.EI.4a**; applying A2.F.2h + the 4.5 cancel test and A2.EO.1a/b
> (4.1--4.3); builds on A2.EO.3b (3.2). Prerequisite for **5.4** (radical equations reuse the same
> extraneous logic). Warm-up & exit ticket each fit one page (blank+key); notes 4pp (key 5pp), activity
> 3pp (key 4pp), homework 3pp, cover 1pp --- the extra key page in notes/activity is the teacher note
> only, so every answer page paginates identically to its blank; exit ticket includes an SOL-style MC
> item on $\frac{x}{x+3}+\frac{3}{x-3}=\frac{18}{x^2-9}$, which clears to $x^2=9$ so *both* candidates
> are excluded (answer: no solution; the distractors keep one candidate or both --- a student choosing
> $\{3,-3\}$ did the algebra perfectly and skipped Step 4).
> `make -C unit04/lesson06 all` → EXIT 0 (student 13pp, full 31pp); `make -C unit04 all` → EXIT 0.
> **Lesson 4.7 authored & builds (2026-07-27):** all components + keys + 11-slide deck done; the unit's
> modeling capstone and its last lesson. Everything hangs on one instruction --- **run both rows of
> arithmetic, on every row of the table** --- seeded in the Warm-Up before either name is spoken: two
> tables where students fill a *quotient* row and a *product* row and discover that P's quotients settle
> ($5$) while Q's products do ($60$), with Q's quotient row deliberately ugly ($15$, $3.75$,
> $1.\overline{6}$, $0.6$). Constant quotient ⇒ **direct**, $y=kx$; constant product ⇒ **inverse**,
> $y=k/x$; neither ⇒ **neither**, which A2.F.1d names explicitly and students never volunteer. The Hook
> copies 4.6's design (identical surface features, different verdicts): Tables A ($y=6x$) and B
> ($y=3x+6$) both climb by a constant amount and are both lines, but doubling $x$ from $2$ to $4$ sends
> A's $y$ from $12$ to $24$ and B's only to $18$ --- and at $x=0$, B gives $6$. **A direct variation is
> a line through the origin; "climbs steadily" is not the test.** Anchors: gasoline $c=3.40g$ ($k$ =
> dollars *per gallon*, graph through $(0,0)$ because zero gallons costs zero dollars) and the
> $240$-mile trip $t=240/r$, where **$k$ is not a rate but the distance** ($rt=d$ in disguise) --- and
> where the unit closes its loop, because $t=240/r$ *is* the 4.4 parent stretched by $240$, so both
> asymptotes become sentences (VA $r=0$: "standing still, you never get there"; HA $t=0$: "no speed makes
> a trip take no time"). The "neither" section carries two traps in opposite directions: $y=5x+15$ (rises
> steadily, not direct --- a *fee before you buy anything*) and $y=10-x$ (falls steadily, products
> $9,16,21,24$, not inverse). Finding $k$ closes with the shortcut named as **yesterday's**: a direct
> variation is literally $y_1/x_1 = y_2/x_2$, a proportion, so cross-multiply (4.6); an inverse one is
> $x_1y_1=x_2y_2$. Joint/combined variation ($y=kxz$, $y=kx/z$) is present and **labeled enrichment,
> not assessed** --- A2.F.1d names direct and inverse only --- with students deriving $V=\pi r^2h$ from
> "$V$ varies jointly as $h$ and $r^2$." **4.6 pays its debt in the interpretation items:** every
> context rejection today (the road forbidding $r=-30$, a base of $-4$, $w=4.5$ workers, a seesaw rider
> weighing $-60$ lb) is a rejection the *algebra has no objection to*, and "extraneous" is explicitly
> not an acceptable word for it. Flagged traps: **$k$ computed from one row and never tested** (activity
> Tier A part 3 is an error analysis whose arithmetic is *flawless* --- $k=6/2=3$ from the first pair of
> $y=2x+2$); filling in only the row that matches the guess; "goes down, so inverse"; correct $k$ poured
> into the wrong *form* ($y=24x$ for an inverse, homework 5, where the sanity check "$x$ up ⇒ $y$ down"
> catches $288$ before any arithmetic); "neither" refused; $k$ reported as a bare number with no units;
> and a negative $k$ read as an error (homework 2(f)). Sharpest items: activity Tier E 3(a), where
> $y=6/x$ is shown to be a *direct* variation in $1/x$ --- which is exactly why $y=k/x$ is the parent
> $1/x$ scaled by $k$ and why $k$ cannot move the asymptotes; homework 4(d), *why can a direct variation
> never have an asymptote?* (it is a polynomial --- the 4.0 compare-and-contrast table, fair game on the
> test); and homework Extension part 3, proving no four-row table can be both direct and inverse
> ($kx=m/x$ forces $x^2=m/k$, at most two $x$-values), landing on a direct and an inverse through
> $(2,6)$ meeting again at $(-2,-6)$. Exit ticket item 2's table has products $12,18,18,12$ --- two
> match on purpose, so anyone who checks a pair and stops agrees with the wrong classmate. Warm-up &
> exit ticket each fit one page (blank+key); notes 5pp (key 5pp), activity 3pp (key 4pp), homework 3pp
> (key 4pp), cover 1pp, slides 11 frames --- the extra key pages are the teacher note.
> `make -C unit04/lesson07 all` → EXIT 0 (student 14pp, full 32pp).
> **Unit 4 tests authored & built (2026-07-27):** practice + actual and both keys, all 5pp, all four
> building clean (`make -C unit04/tests all` and `make -C unit04/test_keys all` → EXIT 0), and the
> practice pair published to `sample_test/` + `sample_test_key/`. One blueprint, two parallel forms
> (same parts, same item types, same difficulty, different numbers and contexts), 72 pts:
> **Part A vocabulary (8)** --- matching the eight terms the unit turns on (rational function, domain
> restriction, vertical/horizontal asymptote, hole, LCD, extraneous solution, constant of variation),
> with the two definitions written as the *cancel test's* two outcomes so the matching itself teaches
> the contrast; **Part B multiple choice (12)** --- domain from the *denominator*, simplify-with-
> restrictions, HA by degree comparison, an SOL-style hole-vs-wall item, transformed-parent asymptotes,
> and inverse variation, with every distractor a named error (numerator-zero, restrictions off the
> *simplified* denominator, inverted leading-coefficient ratio, skipped cancel test, direct-instead-of-
> inverse); **Part C computation (40)** --- one item per lesson: read a pre-drawn graph (practice
> $\frac{x+4}{x-2}$, decreasing branches; actual $\frac{x-3}{x+1}$, increasing branches --- both with
> unlabeled dashed asymptotes and lattice-point intercepts), simplify + restrictions incl. opposite
> binomials, multiply *and* divide (the three-sources-of-a-restriction item), add/subtract + a complex
> fraction, parent transformations both directions (describe from an equation, write an equation from
> given asymptotes), analyze-from-the-equation (hole coordinates from the *simplified* form), three
> rational equations (one clean, one whose only root is extraneous → **no solution**, one quadratic
> where a root must be thrown out), and a variation table classified by constant *products*;
> **Part D extended response (12)** --- a full analysis whose last part asks where $f$ and its
> simplified form agree and where they do not (the unit's central idea, graded as such), and an
> average-cost model ($A(n)=\frac{7n+180}{n}$ practice, $\frac{5n+240}{n}$ actual) rewritten as
> $c+\frac{\text{setup}}{n}$ so the HA is *interpreted*, not just stated, closing on "can the average
> cost ever equal the per-unit cost?" Keys carry per-part `teachernote` scoring rubrics and
> error-by-error item analysis. **Slant asymptotes deliberately absent** (4.5 Tier E only, never
> assessed), and every expression stays inside the A2.EO.1b / A2.EI.4b linear-and-quadratic bound.

- **4.0** Characteristics of rational functions *(introduces: vertical & horizontal
  asymptotes, holes/removable discontinuity, domain restrictions)* — A2.F.2a/b/c/g/**h**
- **4.1** Simplifying rational expressions & domain restrictions *(factor-and-cancel with the
  4.2 toolkit; restrictions read off the **original** denominator — the algebraic engine behind
  4.0's holes)* — A2.EO.1b/d
- **4.2** Multiplying & dividing rational expressions *(factor first; keep-change-flip;
  restrictions from every denominator including the divisor)* — A2.EO.1a
- **4.3** Adding & subtracting rational expressions + complex fractions *(LCD from factored
  denominators; a complex fraction as combine-then-divide)* — A2.EO.1a/**c**
- **4.4** The rational parent function & transformations *(the $y=1/x$ hyperbola; the four
  transformations move the asymptotes; write the equation from a graph)* — A2.F.1a/b/c/e
- **4.5** Graphing rational functions from the equation *(factor → holes vs. vertical asymptotes
  → horizontal asymptote by degree comparison → intercepts → sign chart reused from 3.6 → end
  behavior; slant asymptote as Tier E only)* — A2.F.2a/g/h + A2.F.1c
- **4.6** Solving rational equations & extraneous solutions *(LCD-multiply or cross-multiply;
  extraneous roots are exactly 4.1's excluded values — the unit's payoff loop)* — A2.EI.4a/b/c/d
- **4.7** Direct, inverse & joint variation *(modeling capstone: proportional vs. inversely
  proportional from a table, find $k$, write and interpret the equation; joint variation is not
  named in A2.F.1d — carry it as enrichment)* — A2.F.1d (+ A2.F.2f)

### Unit 5 — Radical Functions
> **Status (map confirmed & scaffolded 2026-07-27):** lesson map locked at **8 lessons (5.0–5.7)**,
> grounded against `spec/algebra2-vdoe-sol.pdf`. Two changes from the original ~5-lesson sketch:
> the single "simplifying & operations" lesson was **split into 5.2 (simplify + add/subtract) and
> 5.3 (multiply/divide + rationalizing)** — A2.EO.2a/b carries the same load the parallel rational-
> expression standard got across 4.1–4.3 — and the "inverse functions & composition" lesson was
> **split into 5.6 (composition) and 5.7 (inverses)**, since A2.F.2i, j, and k are three separate
> K&S and composition is the *prerequisite* that verifies an inverse. All 8 lesson dirs
> `unit05/lesson00`–`lesson07` scaffolded with skeleton `main.tex` for lesson plan + cover, warmup,
> notes, activity, exit_ticket, homework, slides, and each `*_key`. Unit assessments scaffolded:
> `tests/{practice_test,actual_test}`, `test_keys/`, `sample_test{,_key}/`. Skeletons compile
> (`make -C unit05/lesson01 all` → EXIT 0). **All 8 lessons are now authored and building
> (`make -C unit05 all` → EXIT 0, 2026-07-28); only `tests/` and `test_keys/` remain skeletons.**
> Unit shape deliberately mirrors Unit 4: characteristics → algebra engine → graphing → solving →
> capstone. Lesson 5.0 introduces the two new spine rows: ● restricted domain from the radicand,
> ● inverse relationship of families.
> **Standards coverage:** **A2.EO.2a/b/c** (simplify, operate on, and convert radical expressions ⇄
> rational exponents), **A2.EI.5a/b/c** (solve/verify/justify radical equations), **A2.F.1a/b/c/e**
> (square root *and* cube root parents + transformations), **A2.F.2a–g** (characteristics), and
> **A2.F.2i/j/k** (inverses and composition — Unit 5 is their only home in the course; Unit 7
> revisits the idea only as exponential ⇄ logarithmic).
> **Authoring note:** apply the §7 vocab-box paragraph-break fix in every notes/notes_key.
> **Lesson 5.0 authored & builds (2026-07-27):** all components + keys + 10-slide deck done; teaches
> the two radical parents **side by side** rather than treating $\sqrt[3]{x}$ as an afterthought, and
> hangs everything on one fact — **the index runs the show**. An *even* index refuses a negative
> radicand (nothing real squares to a negative), so the domain must be **solved for** by setting
> *radicand* $\ge 0$; an *odd* index refuses nothing (cubing keeps the sign), so the domain is all
> reals. That single split generates every difference between the families, and it is stated as a
> genuine escalation: a polynomial was defined *everywhere*, a rational function lost a few scattered
> inputs, and a square root loses an entire **half** of the number line at once — domain stops being
> something students *read* and becomes something they *compute*. Introduces the **endpoint** (solid
> dot, since $\sqrt{0}=0$ is real) and the fact that it is *always* an absolute extremum — a **minimum**
> if the arm climbs away from it, a **maximum** if it falls ($-\sqrt{x}+3$ in homework) — while a cube
> root, having no endpoint, has **no extrema at all**. The hardest new beat is **end behavior with only
> one end**: as $x\to-\infty$ a square root graph does *nothing*, it **stops**, and "the graph stops"
> is drilled as a complete answer rather than a missing one (the Active Monitoring list, Tier R item 6,
> and the exit ticket all police it). The second ● spine row, the **inverse relationship of families**,
> is *earned rather than announced*: Warm-Up item 3 has students fill tables for $y=x^2$ and
> $y=\sqrt{x}$ and notice the rows are swapped, and the notes then draw both reflections over $y=x$ —
> yielding the deeper reason for the domain rule (the domain of $\sqrt{x}$ *is* the range of $x^2$),
> the vertical-line-test argument for why $y=x^2$ needs a **restricted domain**, and the contrast that
> $y=x^3$ never repeats an output so all of it reflects. Anchor $f(x)=\sqrt{x+4}-1$ (endpoint
> $(-4,-1)$, zero $(-3,0)$, $y$-int $(0,1)$, abs min $-1$); guided practice on $p(x)=\sqrt{4-x}$, the
> sign-flip case that opens **left** (planted in Warm-Up item 2c and revisited in Tier E and homework,
> where $x\ge$ instead of $x\le$ is the predictable error). Tier A pairs $2-\sqrt{x}$ with
> $\sqrt[3]{x}-1$ so that *every* row of the feature table differs; Tier E derives $d=16t^2$ from a
> free-fall model $t(d)=\frac{\sqrt{d}}{4}$ and the homework extension derives $d=\frac{s^2}{24}$ from
> a skid-mark model $s(d)=\sqrt{24d}$ — both closing the inverse loop in context and rediscovering the
> restricted domain from "negative time/speed is meaningless." All graphs pre-drawn via `plot`+`\clip`
> (cube roots plotted as two branches, since pgfmath has no `cbrt`); no sketch-from-scratch. Standards:
> **2023 VA SOL A2.F.2a/b/c/d/f/g** and **A2.F.1a/e**, previewing **A2.F.2i/j** (inverses) without yet
> requiring the algebraic method. Warm-up & exit ticket each fit one page (blank+key); notes 5pp
> (key 5pp), activity 3pp (key 3pp), homework 2pp (key 3pp); exit ticket includes an SOL-style MC item
> (domain of $\sqrt{5-2x}$; distractors = the missing inequality flip, a sign slip, and treating an even
> index as unrestricted). `make -C unit05/lesson00 all` → EXIT 0 (student 13pp, full 28pp);
> `make -C unit05 all` → EXIT 0.
> **Lesson 5.1 authored & builds (2026-07-27):** all components + keys + 10-slide deck done; supplies
> the *algebra* underneath 5.0's geometry. One thesis, stated as a derivation rather than a
> definition: **a radical is an exponent in disguise**, and nobody chose it — if "power to a power"
> is to keep working, $\left(a^{1/n}\right)^n=a^{n/n}=a$, so $a^{1/n}$ has **no choice** but to be
> $\sqrt[n]{a}$. That move (extend a definition by insisting the old rules survive) is named aloud as
> reusable reasoning. From it: $a^{m/n}=\sqrt[n]{a^m}=\left(\sqrt[n]{a}\right)^m$, with the mantra
> **denominator = index, numerator = power** stated twice because *flipping the fraction*
> ($\sqrt[4]{x^3}\to x^{4/3}$) is the lesson's signature error and the exit-ticket MC distractor A.
> Three further beats: the **principal root** ($\sqrt{16}=4$, not $\pm4$ — write the $\pm$ yourself)
> with the four-row how-many-real-roots table; the $\sqrt[n]{a^n}$ **absolute-value** rule ($|a|$ even,
> $a$ odd) — the only place all week where variables are not assumed positive; and **root first, not
> power first**, taught by a two-column table that lets $\sqrt[4]{4096}$ actually appear in the hard
> column, so choosing the easy route is framed as the skill. Negative rational exponents get the
> repeated line "the minus sign *moves* the expression, it does not change its sign"
> ($16^{-1/2}=\frac14$). The payoff section closes the Hook — $\sqrt{x}\cdot\sqrt[3]{x}$, impossible
> as radicals (mismatched indices), one line as $x^{1/2+1/3}=x^{5/6}=\sqrt[6]{x^5}$ — which is the
> honest answer to "why does this notation exist." Section 6 keeps it a *function* lesson rather than
> a notation drill: 5.0's two parents are relabeled $y=x^{1/2}$ and $y=x^{1/3}$ (same pre-drawn
> graphs, new notation) and the domain rule is re-derived from the **denominator**, with the closing
> claim that "even index restricts the domain" and "even denominator restricts the domain" are one
> sentence in two notations — the homework's item 6 makes students say it. Tier E does the four
> mismatched-index problems no radical rule can touch (incl. nested $\sqrt{\sqrt[3]{x}}$, indices
> multiply) plus **Kepler's third law** $T(a)=a^{3/2}$ on a perfect-power table ($a=1,4,9,25$),
> Jupiter estimated at $5.2$ AU, and $a=T^{2/3}$ obtained by raising both sides to the **reciprocal**
> — the algebraic form of 5.0's reflection over $y=x$ and a genuine preview of 5.7. The homework
> extension is **Kleiber's law** $M(w)=70w^{3/4}$, deliberately the same shape: $16\times$ the mass
> buys only $8\times$ the calories, which is what an exponent below $1$ does to growth (the
> flattening read off the square root graph in 5.0), inverted to $w=\left(\frac{M}{70}\right)^{4/3}$.
> Standards: **2023 VA SOL A2.EO.2c** (governing — convert radical ⇄ rational exponent, assessed in
> every component) and **A2.EO.2a** (equivalent radical expressions, via the evaluations and
> property work — this lesson supplies the tool 5.2–5.3 lean on), revisiting **A2.F.2a**/**A2.F.1a**
> (domain and parent graphs) and reaching **A2.F.2f** (evaluate and interpret in context) through the
> two models, which also preview **A2.F.2i/j**. Warm-up & exit ticket each fit one page (blank+key);
> notes 4pp (key 4pp), activity 3pp (key 3pp), homework 3pp (key 3pp) — blank and key paginate
> identically throughout. Exit ticket includes an SOL-style MC item (which expression equals
> $\sqrt[4]{x^3}$; distractors = the flipped fraction, index×power, and reading a root as a negative
> exponent). `make -C unit05/lesson01 all` → EXIT 0 (student 13pp, full 27pp);
> `make -C unit05 all` → EXIT 0.
> **Lesson 5.2 authored & builds (2026-07-27):** all components + keys + 11-slide deck done. One
> sentence carries the lesson — **a radical splits over multiplication and never over addition** —
> and it is *established by the students* rather than announced: the Hook puts three statements on
> the board ($\sqrt8\cdot\sqrt2=4$, $\sqrt9+\sqrt{16}=\sqrt{25}$, $\sqrt8+\sqrt{18}=5\sqrt2$) and asks
> which is the lie. The one that *looks* absurd is true (to three decimals) and the reasonable-looking
> one is false, so the class discovers both halves of the day in three minutes. The properties are
> then **derived, not stated**: $\sqrt[n]{ab}=(ab)^{1/n}=a^{1/n}b^{1/n}$ is 5.1's power-of-a-product
> rule, with the even-index fine print ($a,b\ge0$) flagged as the place a student who cannot tell when
> a root exists will turn $\sqrt{-8}$ into $\sqrt{-4}\cdot\sqrt2$ — the exact pile 5.1's exit ticket
> told the teacher to sort for. Four further beats: **simplest form** as three conditions with
> condition 3 (no radical in a denominator) *explicitly deferred to 5.3* so students know something is
> being held back; **largest** perfect power, taught by working $\sqrt{72}$ both ways so that
> $2\sqrt{18}$ is framed as true-but-unfinished and the closing habit becomes "check the leftover";
> **the index sets the group size** (pairs escape a square root, triples a cube root — so $\sqrt[3]9$
> is *already* simplest even though 9 is a perfect square, the lesson's most-missed idea); and
> algebraic radicands via **divide the exponent by the index**, whose real content is the unifying
> claim that $\sqrt{x^7}=x^{7/2}=x^{3\frac12}=x^3\sqrt x$ — **simplifying a radical and rewriting an
> improper fraction as a mixed number are the same move** (pre-assembled in Warm-Up item 3, and the
> homework's closing item makes students say it). Adding is taught as literal like-term collection
> against Warm-Up item 2 ($3\sqrt5+7\sqrt5$ beside $3x+7x$), with the signature habit **simplify
> first, decide second** — "cannot combine" must be earned, never guessed. Tier E proves
> $\sqrt a+\sqrt b=\sqrt{a+b}$ forces $ab=0$ (square, cancel, the surviving $2\sqrt{ab}$ is exactly
> what the error deletes), generalizes the staircase $\sqrt2+\sqrt8+\cdots+\sqrt{2n^2}
> =\frac{n(n+1)}2\sqrt2$, and closes with a deliberate bridge to 5.4: $f(x)=\sqrt{8x}=2\sqrt{2x}$ is
> $g(x)=\sqrt{2x}$ **vertically stretched**, domain and endpoint unchanged. Homework extension is the
> **pendulum** $T(L)=2\pi\sqrt{L/32}$ — same shape as 5.1's Kepler and 5.0's free-fall models — with
> $L=2,8,18,32$ ft chosen so the fraction reduces to a perfect square and the periods come out exactly
> $\frac\pi2,\pi,\frac{3\pi}2,2\pi$; quadrupling the length only doubles the period (what a $\frac12$
> exponent does), a clockmaker's "just double the length" is refuted, and $\sqrt{L/32}=\sqrt{2L}/8$
> previews rationalizing before the word exists. Standards: **2023 VA SOL A2.EO.2a** (governing) and
> the *additive half* of **A2.EO.2b** — multiply/divide/rationalize are held for 5.3, which is why
> A2.EO.2b splits across the pair — revisiting **A2.EO.2c** as the source of both properties, and
> reaching **A2.F.2f** / previewing **A2.F.1b/c** through the pendulum and the vertical-stretch item.
> Warm-up & exit ticket each fit one page (blank+key); notes 4pp/4pp, activity 3pp/3pp, homework
> 2pp (key 3pp); exit ticket includes an SOL-style MC item ($\sqrt{50}+\sqrt{32}$; distractors =
> added radicands, simplified-then-added-radicands, and multiplied coefficients).
> `make -C unit05/lesson02 all` → EXIT 0 (student 12pp, full 28pp); `make -C unit05 all` → EXIT 0.
> **Lesson 5.3 authored & builds (2026-07-27):** all components + keys + 10-slide deck done. The
> lesson runs 5.2's product property **forwards**, and everything on the page is a consequence of a
> single line planted in Warm-Up item 2 --- $\sqrt a\cdot\sqrt a=a$, **a square root times itself
> erases the radical**. The Hook is the honest historical question rather than a puzzle: two
> students hand in $\frac{1}{\sqrt2}$ and $\frac{\sqrt2}{2}$, both are marked correct, both are
> $0.7071$, and the class is asked *why every textbook insists on the second* --- answered by
> ``it is 1850 and you must do this by hand: $1\div1.414214$ or $1.414214\div2$?'' That makes
> simplest-form condition 3 a fact about arithmetic instead of a decree, which matters because 5.2
> deliberately deferred it. Multiplication is taught with the emphasis on the **last** step, using
> products where neither factor simplifies alone but the product does ($\sqrt6\cdot\sqrt{10}
> =2\sqrt{15}$), so ``finish it'' is discovered rather than nagged; distributing and FOIL are
> explicitly Algebra 1 with the radical playing the variable, and $\left(\sqrt7+\sqrt2\right)^{2}
> =9+2\sqrt{14}$ is killed in advance by Warm-Up item 1(c)'s $(x+4)^{2}$. The intellectual center is
> **conjugates**, and they are *earned rather than announced*: Warm-Up 1(b) makes students say
> ``same terms, opposite middle sign'' about $(x+4)(x-4)$ before the word exists, the notes then
> work $\left(4+\sqrt3\right)\left(4-\sqrt3\right)$ term by term until $13$ appears and a student
> supplies the word *rational*, and $\left(4+\sqrt3\right)^{2}=19+8\sqrt3$ is placed immediately
> beside it --- same two numbers, radical survives. That contrast is the argument, and it is also
> the exit ticket's hardest distractor. A deliberate structural callback ties it to **Lesson 2.4**:
> $(a+bi)(a-bi)=a^{2}+b^{2}$ was the same move in a different number system, with the sign
> difference traced entirely to $i^{2}=-1$ versus $\left(\sqrt b\right)^{2}=+b$. Rationalizing is
> justified *before* it is performed ($\frac{\sqrt b}{\sqrt b}=1$, pre-assembled in Warm-Up item 3's
> $\frac34=\frac{15}{20}$), and the higher-index case $\frac{1}{\sqrt[3]2}$ needing $\sqrt[3]4$ is
> 5.2's ``the index sets the group size'' read forwards --- the same misconception that made
> students call $\sqrt[3]9$ unfinished. Tier E has three parts: rationalizing $\frac{1}{3-\sqrt5}$
> **three ways, two of which fail**, so the conjugate is ruled *in* rather than announced, plus the
> general proof and the 2.4 sign question; **rationalizing the numerator** ---
> $\frac{\sqrt{x+9}-3}{x}$ is $\frac00$ at $x=0$, becomes $\frac{1}{\sqrt{x+9}+3}$, and a table at
> $x=7,1,0.1,0.01$ closes on $\frac16$, a genuine calculus limit computed with today's tool; and
> higher-index rationalizing generalized, then re-derived with rational exponents. The homework
> extension is the **golden ratio** $\varphi=\frac{1+\sqrt5}{2}$, and unlike the unit's earlier
> models (free-fall, Kepler, Kleiber, the pendulum) rationalizing here is not tidying-up but the
> *only* way to see the result: the table's startling $1.6180/0.6180/2.6180$ is then proved by the
> conjugate ($\frac1\varphi=\varphi-1$, $\varphi^{2}=\varphi+1$), and a pre-drawn TikZ golden
> rectangle closes it --- remove the $1\times1$ square and the leftover has ratio
> $\frac{1}{\varphi-1}=\frac{2}{\sqrt5-1}=\varphi$, so the cut repeats forever. Homework item 2's
> follow-up is the sharpest diagnostic in the lesson: two of six products are conjugate pairs and
> *predictable in advance*, while a third, $\sqrt2\left(\sqrt8+\sqrt{18}\right)=10$, is rational
> only by luck of the numbers --- a student who cannot separate those has learned a pattern instead
> of a mechanism. Standards: **2023 VA SOL A2.EO.2b** (governing --- the *multiplicative* half,
> including rationalizing; 5.2 carried the additive half, which is why A2.EO.2b splits across the
> pair), **A2.EO.2a** used continuously since every answer returns to simplest form (condition 3
> now closed), and **A2.EO.2c** in the mismatched-index case $\sqrt2\cdot\sqrt[3]2=2^{5/6}$ and the
> two ``two roads'' items where rationalizing is shown to be $5^{-1/3}=\frac{5^{2/3}}{5}$;
> structurally revisits **A2.EO.4c** (2.4 complex conjugates). Warm-up & exit ticket each fit one
> page (blank+key); notes 4pp (key 5pp), activity 4pp (key 5pp), homework 3pp (key 4pp); exit ticket
> includes an SOL-style MC item ($\frac{4}{2-\sqrt3}$; distractors = the $a^{2}-b^{2}$ sign flip,
> multiplying by the same binomial, and cancelling the $4$ against the $2$).
> `make -C unit05/lesson03 all` → EXIT 0 (student 14pp, full 32pp); `make -C unit05 all` → EXIT 0.
> **Lesson 5.4 authored & builds (2026-07-27):** all components + keys + 11-slide deck done. The
> lesson has one sentence and one payoff. The sentence is **find one point and the whole graph
> follows** — written as $y=a\sqrt{x-h}+k$, a radical graph is the parent moved so its **anchor
> point** sits at $(h,k)$, and domain $[h,\infty)$ and range $[k,\infty)$ both *start there*. The
> Hook makes that a discovery rather than a rule: three pre-drawn graphs ($\sqrt x$, $\sqrt{x-3}$,
> $\sqrt x-3$) are matched to their equations, and then the real question — *in 5.0 you found the
> domain of $\sqrt{x-3}$ by solving $x-3\ge0$; look at the middle graph, where could you have just
> **read** it?* The answer is the sentence the whole unit has been waiting for: **sliding the graph
> right by 3 and refusing every input below 3 are the same event**, so from today the domain stops
> being something students compute and becomes something they look at. Warm-Up item 2 pre-assembles
> it by making them solve the inequality and write the endpoint in the same row. Three further
> beats: **$a$ never moves the anchor** (at the anchor the radical is $0$, and $a\cdot0=0$ whatever
> $a$ is), with the consequence students reliably miss — a *negative* $a$ turns the arm over, so the
> anchor becomes an absolute **maximum** and the range flips to $(-\infty,k]$; the **cube root**
> case, where $(h,k)$ is still the anchor but an **inflection point** rather than an endpoint,
> because an endpoint exists only where inputs are forbidden and an odd index forbids nothing; and
> the SOL's harder direction, **graph → equation** (**A2.F.1b**), taught with an explicit order —
> *the anchor is free, take it first* — since reaching for $a$ first leaves two unknowns in one
> equation. Section 5 carries the payoff, and it is the standard's own fourth transformation.
> **A2.F.1b/c name $f(kx)$**, and for a radical $f(kx)$ *collapses into* $kf(x)$: the product
> property (5.2) lets the constant walk out from under the radical, so $\sqrt{9x}$ and $3\sqrt x$
> are one graph with two names and **a radical has only one size dial**. That is voted on in Warm-Up
> item 3 (deliberately left unresolved on the board), proved in one line with rational exponents
> (5.1) in Tier E — $(kx)^{1/n}=k^{1/n}x^{1/n}$, stretch factor $\sqrt[n]{k}$ — and then immediately
> **fenced**: on $y=\sqrt x+1$, squeezing the input gives $3\sqrt x+1$ but stretching the output
> gives $3\sqrt x+3$, a constant gap of $2$ at every $x$, because the product property has nothing
> to say about a term sitting *outside* the radical. The same section carries the lesson's
> most-assessed procedural habit, **factor before you read $h$**: $\sqrt{4x-8}=2\sqrt{x-2}$ starts
> at $x=2$, not $8$ — which is the exit ticket's MC stem. Anchor $f(x)=\sqrt{x-3}+1$ grows into
> $2\sqrt{x-2}$ and $3\sqrt{x+2}-1$ across the notes; cube root anchor $g(x)=\sqrt[3]{x+1}-2$
> (inflection $(-1,-2)$, zero $(7,0)$, $y$-int $(0,-1)$). The **A2.F.1e** compare-and-contrast is
> Section 3's reflection pair: $-\sqrt[3]{x}$ and $\sqrt[3]{-x}$ are *one* curve (5.0's origin
> symmetry doing work) while $-\sqrt x$ and $\sqrt{-x}$ do not even share a domain — the homework's
> item 6 makes students explain both at once using *index* and *symmetry*. The homework extension is
> the **horizon model** $d(h)=\sqrt{1.5h}$ miles, table $h=6,24,54,96,150$ chosen so every distance
> is a whole number ($3,6,9,12,15$); unlike the unit's earlier models the payoff is a
> *transformation* — $\sqrt{1.5h}=\sqrt{1.5}\sqrt h\approx1.22\sqrt h$, so a real navigation formula
> is nothing but the parent with a single vertical stretch — closing on a sailor climbing a mast
> above a 20-ft deck, $D(h)=\sqrt{1.5(h+20)}$, whose anchor $(-20,0)$ **is not a place anyone can
> stand**: context domain $h\ge0$, usable graph begins at $D(0)=\sqrt{30}\approx5.5$ miles.
> Standards: **2023 VA SOL A2.F.1c** (governing — graph from the equation, all four named
> transformations) and **A2.F.1b** (write the equation from a graph), with **A2.F.2a** used
> continuously (domain/range/zeros/intercepts, now read off the anchor) and **A2.F.1e** in the
> reflection contrast; revisits **A2.F.1a** (5.0), **A2.EO.2a** (5.2's product property — the reason
> $f(kx)$ collapses), and **A2.EO.2c** (5.1's rational exponents, Tier E). All graphs pre-drawn via
> `plot`+`\clip`; no sketch-from-scratch. Warm-up & exit ticket each fit one page (blank+key);
> notes 5pp (key 6pp), activity 3pp (key 4pp), homework 3pp (key 4pp). Exit ticket includes an
> SOL-style MC item (anchor of $y=3\sqrt{2x-10}+1$; distractors = not factoring out the $2$,
> factoring but keeping the constant's sign, and reversing $k$ as though outside numbers flipped
> too). `make -C unit05/lesson04 all` → EXIT 0 (student 14pp, full 32pp); `make -C unit05 all` →
> EXIT 0.
> **Lesson 5.5 authored & builds (2026-07-27):** all components + keys + 10-slide deck done. The
> lesson rests on one claim, and it is a claim about *logic* rather than about radicals: **squaring
> hands you candidates, not solutions.** The Hook makes that unavoidable by putting a *flawless*
> solution to $\sqrt{x+7}=x-5$ on the board --- square, expand, collect, factor, $x=2$ or $x=9$ ---
> and telling students every line is correct, which it is. Then both answers are tested in the
> original: $x=9$ gives $4=4$, $x=2$ gives $3$ against $-3$. The question that opens the lesson is
> therefore *one answer is wrong and no step was wrong, so where did the wrong answer come from?*,
> which is a genuinely different demand from every prior unit --- correct procedure has always
> guaranteed a correct answer, and from today it does not. Warm-Up item 2 pre-assembles the whole
> mechanism in two yes/no questions (*if $x=-4$ then $x^{2}=16$? if $x^{2}=16$ then $x=4$?*), and
> item 3 factors $x^{2}-11x+18$ so that $2$ and $9$ are already familiar when the Hook produces
> them; item 1's $\left(\sqrt{x}+3\right)^{2}=x+6\sqrt x+9$ beside $\left(\sqrt{x-3}\right)^{2}=x-3$
> *is* the reason Step 1 of the method is **isolate**. Four further beats: the mechanism named
> exactly --- $a=b\Rightarrow a^{2}=b^{2}$ always, but $a^{2}=b^{2}$ leaves $a=b$ **or** $a=-b$, so
> **squaring destroys sign information** and can only *enlarge* a solution set; the **free
> shortcut**, an isolated even root equal to a negative number has no real solution and can be
> answered before any algebra (5.1's principal root), taught by then squaring $\sqrt{2x-1}+5=2$
> anyway so students see the phantom it would have produced; the **odd index closing the trapdoor**
> --- every real has exactly one real cube root, so $A^{3}=B^{3}$ forces $A=B$, cubing is
> *reversible*, and $\sqrt{x-4}=-2$ (no solution) sits beside $\sqrt[3]{x-4}=-2$ ($x=-4$, checks) as
> same numbers / opposite verdicts / **only the index differs**, the unit's thesis one more time;
> and the **graphical check** (A2.EI.5a), where the number of *intersections* is the number of real
> solutions, so 5.4's graphs return as the two sides of an equation. The single best figure in the
> lesson is the Hook's: $y=\sqrt{x+7}$ against $y=x-5$ crossing once at $(9,4)$, with $(2,3)$ and
> $(2,-3)$ marked in red and joined by a dashed segment --- two mirror-image points that squaring
> flattens onto the same number, which is the extraneous root made visible. The other unifying claim
> is the **4.6 callback**: multiplying by something that might be zero and squaring something that
> might be negative are the same structural event --- a non-reversible step produces candidates, and
> only the check promotes them. Activity Tier A carries the lesson's discovery item: three equations
> each lose exactly one candidate, and tabulating the *right-hand side* at each rejected value shows
> it is negative every time, yielding the predictive rule **a candidate is extraneous exactly when
> it makes the non-radical side negative** --- which students can apply *before* checking. Homework
> item 2(b), $\sqrt{4x+13}=x+4$, is the deliberate antidote to ``reject the negative one'': both
> candidates ($-1$ and $-3$) are negative and **both are genuine solutions**. Homework item 4(d) is
> the sharpest small item --- squaring $\sqrt{x+2}=-1$ returns part (b)'s answer, because squaring
> cannot tell the line $y=-1$ from $y=1$. Section 6 handles $x^{m/n}=k$ by the **reciprocal power**
> (5.1's Kepler move) with both traps flagged: an even *numerator* is a square in disguise (write the
> $\pm$ yourself --- $x^{2/3}=9$ has two solutions), an even *denominator* restricts the base.
> Tier E proves both rules, does two-radical equations (beyond A2.EI.5a's one-radical cap, flagged as
> extension; $\sqrt{x+5}-\sqrt x=1$ needs two squarings and gives $x=4$), and runs 5.2's pendulum
> $T(L)=2\pi\sqrt{L/32}$ *backwards* against that lesson's own table ($T=2\pi\Rightarrow L=32$,
> $T=\pi\Rightarrow L=8$), closing on a period of $-\pi$ that fails for two *separate* reasons,
> algebraic and contextual --- the 4.6 distinction, re-drawn. The homework extension is the
> **skid-mark model** $s(d)=\sqrt{24d}$ from 5.0's homework, run backwards ($30$ mph $\Rightarrow
> 37.5$ ft, $60$ mph $\Rightarrow 150$ ft --- doubling the speed *quadruples* the skid; the scene's
> $96$ ft gives exactly $48$ mph and contradicts the driver), and its payoff is the honest converse
> of the whole day: deriving $d=\frac{s^{2}}{24}$ requires squaring both sides, yet there is *no*
> extraneous risk, because both sides are non-negative in context and a phantom needs a sign
> disagreement to come through. Standards: **A2.EI.5a** (governing --- solve algebraically *and*
> graphically), **A2.EI.5b** (verify solutions; interpret in context --- the pendulum and skid-mark
> models), and **A2.EI.5c** (justify why a solution might be extraneous --- assessed directly in
> Exit Ticket 2(c), Tier A J1--J2, and homework 6); revisits **A2.EO.2c** (5.1, §6),
> **A2.F.1c**/**A2.F.2a** (5.4's graphs as the two sides of an equation), and **A2.EI.4c** (4.6).
> All graphs pre-drawn via `plot`+`\clip`; no sketch-from-scratch. Warm-up & exit ticket each fit one
> page (blank+key); notes 5pp/5pp, activity 4pp/4pp, homework 3pp/3pp --- blank and key paginate
> identically throughout. Exit ticket includes an SOL-style MC item (*which equation has no real
> solution?*), whose distractor **B**, $\sqrt[3]{x-1}=-5$, is the one that earns its keep: a student
> who learned ``roots can't be negative'' instead of ``*even* roots can't'' picks it, and that is a
> Unit 5 spine failure rather than a slip in today's procedure.
> `make -C unit05/lesson05 all` → EXIT 0 (student 15pp, full 29pp); `make -C unit05 all` → EXIT 0.
> **Lesson 5.6 authored & builds (2026-07-27):** all components + keys + 12-slide deck done. The
> lesson makes two claims and spends the period earning both. The first is **order is part of the
> answer**, and it is settled before any notation exists: the Hook puts a \$80 jacket in front of two
> cashiers who apply a $20\%$ discount and a \$10 coupon in opposite orders and reach \$54 and \$56.
> Neither made a mistake --- which is the whole point, and the missing \$2 turns out to be $20\%$ of
> the coupon, i.e.\ the discount eating the student's own savings. Warm-Up item 3 pre-assembles it in
> arithmetic ($10-4$ then double $=12$; double then $-4=16$), so ``order matters'' is said out loud by
> a student before the jacket appears; Warm-Up item 1(d) has students evaluate $g(-1)=2$ and feed the
> answer into $f$ --- **a composition computed before the symbol exists**, so nobody leaves thinking
> composition is a new operation; and item 2's $h(x+1)$ *is* the algebraic method of §4, which is why
> the parentheses are policed there. The notation is taught as a reading rule --- **the function next
> to the $x$ runs first, work inside out** --- with the day's signature error framed correctly as a
> *reading* error, not a mathematical one, and the enforcement mechanism is procedural: **write the
> middle number down**, since the wire between the two machines carries exactly one value and a
> student composing in their head is a student about to reverse the order. A2.F.2k's three
> representations are each given their own section (values \& a table in §2, two pre-drawn
> piecewise-linear graphs in §3, algebra in §4), with §2's table trio deliberately built so that one
> input, $x=0$, yields three different answers ($0$, $-2$, $2$) --- ``order matters'' made undeniable
> from values alone. §5 is where the unit pays: the anchor pair $f(x)=\sqrt{x}$, $g(x)=x-4$ gives
> $\sqrt{x-4}$ one way and $\sqrt{x}-4$ the other --- **two graphs students already read in 5.4**, with
> different endpoints *and* different domains --- and the section closes by revealing that **every
> transformation in 5.4 was a composition**, which is the long-deferred answer to *why inside changes
> act backwards*: the inner machine hands the root a number $4$ smaller, so $x$ must be $4$ bigger to
> compensate. §6 is the intellectual center and the bridge to 5.7. Domain is computed through **two
> gates** ($x$ in $g$'s domain, $g(x)$ in $f$'s), and then the surprise: with $f(x)=x^{2}$ and
> $g(x)=\sqrt{x}$, $\left(\sqrt{x}\,\right)^{2}$ simplifies all the way to $x$ and **still refuses
> $x=-9$**, because Gate 1 turned it away before stage 2 ever ran --- *simplifying erases the evidence
> of a gate, not the gate*. Beside it sits $\sqrt{x^{2}}=|x|$ (5.1's $\sqrt[n]{a^{n}}$ rule, the only
> place this week where variables are not assumed non-negative), which accepts everything but is not
> $x$. **Neither order is honestly ``$x$ for every real number,''** and that discomfort is left
> deliberately unresolved --- it is exactly why 5.7 must restrict the domain of $y=x^{2}$, the thread
> opened in 5.0. §7 adds decomposition (not in A2.F.2k; included because it makes 5.7 and next year's
> calculus easier), taught by ``what would your hands do first on a calculator?'' The inverse preview
> is *earned rather than announced*: Activity Tier A rows (d) $x+3$/$x-3$ and (e) $3x-1$/$\frac{x+1}{3}$
> come out to $x$ in **both** orders, and J1 asks students to invent a word for it --- the teacher note
> instructs collecting those wordings to open 5.7 beside the word *inverse*. Tier E generalizes the
> jacket ($0.8x-8$ vs.\ $0.8x-10$, a constant \$2 gap at every price), derives the full linear
> commuting condition ($f(g(x))=acx+ad+b$, $g(f(x))=acx+cb+d$, equal iff $ad+b=cb+d$, tested against
> both earlier pairs), decomposes $2\sqrt{x-5}+1$ into three machines and compares that list with 5.4's
> transformation list, and closes on the $\left(\sqrt{x}\,\right)^{2}$ vs.\ $\sqrt{x^{2}}$ table at
> $x=-4,-1,0,4,9$. Homework 5 carries **two different** misconceptions side by side --- Amara reads
> $\circ$ as multiplication, Ben reverses the order --- settled by evaluating all three expressions at
> $x=2$ ($25$/$20$/$7$); homework 3's follow-up kills the wrong generalization ``a square root means a
> restricted domain'' via row (e), $\sqrt{x^{2}+2}$, whose radicand can never go negative; and homework
> 2(g) is the unit's first *backwards* question (for what $x$ is $(p\circ q)(x)=0$?), the seed of 5.7's
> swap-and-solve. The homework extension composes 5.4's horizon model $d(h)=\sqrt{1.5h}$ with a mast
> climb $h(t)=6t+6$ to get $(d\circ h)(t)=3\sqrt{t+1}$ --- whole-number distances $3,6,9,12$ miles at
> $t=0,3,8,15$, a horizontal shift that *is* the sailor's 6-foot head start, a vertical stretch that is
> the $\sqrt{1.5\cdot6}=3$ hidden in the formula, the quadrupling (3 seconds buys the second 3 miles,
> 12 more buys the next 6), and a context-domain rejection of $t=-1$. Standards: **2023 VA SOL
> A2.F.2k** (governing --- composition algebraically *and* graphically), direct prerequisite for
> **A2.F.2i/j** (5.7); revisits **A2.F.1b/c** (5.4's transformations, now revealed as compositions),
> **A2.F.2a** (domain via two gates), **A2.EO.2a** (5.1's $\sqrt{x^{2}}=|x|$), and **A2.F.2f** (the
> mast-climb model). All graphs pre-drawn; no sketch-from-scratch. Warm-up & exit ticket each fit one
> page (blank+key); notes 5pp/5pp, activity 4pp/4pp, homework 3pp (key 4pp --- the extra page is the
> teacher note). Exit ticket includes an SOL-style MC item ($f(x)=x^{2}$, $g(x)=x-5$; answer
> $(x-5)^{2}$) whose three distractors are three *distinct* failures: $x^{2}-5$ is the order error,
> $x^{2}-25$ is the Unit 3 perfect-square error inside an otherwise correct composition, and
> $x^{3}-5x^{2}$ is reading $\circ$ as multiplication.
> `make -C unit05/lesson06 all` → EXIT 0 (student 15pp, full 32pp); `make -C unit05 all` → EXIT 0.
> **Lesson 5.7 authored & builds (2026-07-28) --- the unit capstone:** all components + keys +
> 13-slide deck done. The lesson answers the question Lesson 5.0 opened, and it does so with one
> sentence held back for six lessons: **$x^{2}$ has two arms and $x^{3}$ has one.** Everything else
> --- why $\sqrt{x}$ gets half the number line and $\sqrt[3]{x}$ gets all of it, why one has an
> endpoint and an absolute minimum and the other has neither --- is a consequence, and §5 says so
> explicitly with three pre-drawn graphs (full parabola failing a horizontal line at $y=4$, the
> restricted right arm passing, $y=x^{3}$ passing untouched). The **Hook is Celsius/Fahrenheit**, and
> it is built to produce the day's signature error rather than warn about it: Rosa writes
> $C(f)=\frac59f-32$ and Malik writes $\frac59(f-32)$, both are tested at $f=212$ where the room
> already knows the answer is $100$, and the question that carries the period is *Rosa reversed both
> operations correctly --- what did she not reverse?* Warm-Up item 3 pre-loads it in arithmetic
> ("double, then add $5$, and I get $17$" --- nobody halves first), so **reverse the operations
> \emph{and} the order; shoes before socks** is said by a student before the formula appears; Warm-Up
> item 1 is *solve for the other variable*, i.e.\ swap-and-solve's engine, already in students' hands;
> and Warm-Up item 2 is 5.6's own Tier A discovery ($2x+6$ against $\frac{x-6}{2}$, $x$ both ways)
> promoted to a warm-up, with the teacher note instructing that yesterday's student-invented wordings
> go on the board beside the word *inverse*. **Ordering is deliberate: the test (§2) precedes the
> construction (§3)**, so nobody builds a partner without owning a verdict procedure. §2 runs three
> cases --- a pass, a near-miss ($h(x)=\frac{x}{2}-6$ composes to $x-6$, off by a constant, which is
> why only composition catches it), and 5.6's cliffhanger, $\left(\sqrt{x}\,\right)^{2}=x$ against
> $\sqrt{x^{2}}=|x|$, which is the standing proof that **one order passing is not a verdict**. §3's
> swap-and-solve table ends on $\sqrt{x-2}\to x^{2}+2$ **for $x\ge0$**, and the restriction is treated
> as load-bearing throughout: it is the **range of $f$, written down** (§6), never guessed --- the
> reason Activity Tier A row (f), $\sqrt{x}-3$, needs $x\ge-3$ and is the assessed discriminator,
> since reflex says $x\ge0$. §1's red box owns the year's only treatment of **$f^{-1}$ as a label,
> not an exponent** ($f(x)=2x$: $\frac{x}{2}$ against $\frac{1}{2x}$, which at $x=4$ are $2$ and
> $\frac18$). §4 does A2.F.2j: the $\sqrt{x}$ table's rows literally trade places (the table students
> built in 5.0), the graphs are read with $y=x$ dashed, intercepts swap, and $f$ and $f^{-1}$ meet at
> $(4,4)$ **on the mirror line** --- the fact Tier E Part 1 then cashes in. Activity **Tier R** is
> arithmetic-first and withholds the word "inverse" until the last column; **Tier A** J3 is the
> deepest item (swap-and-solve happily produces a formula for $x^{2}-4$, which has no inverse
> function, so the horizontal line test is what licenses the word *the*); **Tier E** finishes the Hook
> and finds $-40^{\circ}$ by solving $F(c)=c$ --- explained with the mirror line, not algebra ---
> then does involutions ($6-x$, $\frac1x$, and the Unit 4 callback $\frac{2x+3}{x-2}$), proves
> $(f\circ g)^{-1}=g^{-1}\circ f^{-1}$ by testing both orders (socks and shoes, formalized: the Hook's
> error in general form), and restricts $y=x^{2}$ to $x\le0$ instead to get $-\sqrt{x}$, closing on
> $A=\pi r^{2}$, where the situation picks the branch for you. Homework carries the three named errors
> once each and catches each with a single number --- Priya takes a reciprocal ($f(3)=15$; her rule
> gives $\frac{1}{75}$), Devon reverses the operations but not the order ($f(4)=-8$; his gives $-23$),
> and item 2(c), $7-2x$, is the sleeper sign trap. The **extension is a pendulum**,
> $T(L)=2\pi\sqrt{L/32}$ inverted to $L(T)=\frac{8T^{2}}{\pi^{2}}$ --- the unit's only place where the
> *inverse* is what a real person needs, since a clockmaker asks how long to make it, not how fast it
> swings; a $2$-second swing gives $\approx3.24$ ft $\approx39$ inches, checkable against any real
> grandfather clock, quadrupling $L$ doubles $T$ ($\sqrt{4L}=2\sqrt{L}$, 5.0's flattening), and part
> (f) is the quiet one: every restricted domain this week had to be argued for, and here the context
> supplies it free. Standards: **2023 VA SOL A2.F.2i** (governing --- inverse of a linear, quadratic,
> or square root function algebraically *and* graphically, **plus the "justify and explain why two
> functions are inverses" clause**, which is the composition test and is assessed in every component)
> and **A2.F.2j** (reflection over $y=x$); rests on **A2.F.2k** (5.6, now a proof tool) and revisits
> **A2.F.2a**, **A2.EO.2a/c**, **A2.EI.5a**, **A2.F.2f**. All graphs pre-drawn; no sketch-from-scratch.
> Warm-up & exit ticket each fit one page (blank+key); notes 5pp/5pp, activity 4pp/4pp, homework 3pp
> (key 4pp --- the extra page is the teacher note); lesson plan 4pp. Exit ticket includes an
> SOL-style MC item ($f(x)=3x+12$; answer $\frac{x-12}{3}$) whose three distractors are the lesson's
> three named errors, one each: $\frac{x}{3}-12$ is Rosa's order error, $\frac{1}{3x+12}$ reads the
> $-1$ as an exponent, and $3x-12$ undoes nothing.
> `make -C unit05/lesson07 all` → EXIT 0 (student 15pp, full 33pp).
> **Unit 5 tests authored & published (2026-07-28) --- the unit is closed:** practice + actual and
> both keys, structured exactly like Unit 4's (Part A vocabulary matching 8 pts, Part B multiple
> choice 12 pts, Part C short answer 40 pts, Part D extended response 12 pts = 72 pts); blanks are
> 4pp, keys 5pp. The two forms are **item-for-item parallel with different numbers and contexts**, so
> the practice copy is a genuine study copy and not a preview. The blueprint is the one 5.7's
> homework spiral box already advertises to students --- convert, simplify, rationalize, read a
> graph, transform, solve with an extraneous check, compose with a domain, build *and justify* an
> inverse --- one Part C item each, in that order. Two constraints were treated as non-negotiable and
> are worth preserving in Units 6--7. First, **A2.F.2i is assessed as a justification, not a
> formula**: C8(b) and D1(e) both demand the composition test in *both* orders, and the scoring note
> says outright that one order is not a verdict; D1(f) then makes students explain why the
> unrestricted parabola is not the inverse (two arms / horizontal line test), which is 5.7's closing
> idea. D1(d) is scored so that guessing $x\ge0$ --- the reflex --- earns nothing: the restriction
> must be named as **the range of $f$**. Second, **A2.EI.5 carries a genuinely extraneous root**:
> C6(a) ($\sqrt{2x+3}=x$ practice, $\sqrt{3x+4}=x$ actual) produces two candidates of which exactly
> one survives, and the key attaches Tier A's predictive rule (the rejected candidate is the one
> making the non-radical side negative). C6 also runs the odd-index case (cubing is reversible, no
> extraneous risk), the free shortcut (an isolated even root equal to a negative --- answerable
> before any algebra), and $x^{m/n}=k$ with an even numerator, where the $\pm$ must be written in by
> hand. The graph item is pre-drawn (no sketch-from-scratch) and its part (f) polices 5.0's signature
> beat --- as $x\to-\infty$ **the graph stops** is the complete answer, and the teacher note forbids
> accepting a blank or ``$-\infty$''. The MC ``no real solution'' item deliberately keeps
> $\sqrt[3]{\ }=\text{negative}$ as a distractor, since choosing it is a Unit 5 *spine* failure
> (``roots can't be negative'' instead of ``*even* roots can't''), not a procedural slip. Both Part D
> modeling items are new contexts rather than reruns of the lessons' models (roller-coaster drop
> speed $v(h)=8\sqrt h$ on the practice, highway-ramp safe speed $s(r)=4\sqrt r$ on the actual), each
> chosen for whole-number outputs, each inverted, and each closing on part (e): *why was there never
> any extraneous danger here?* --- both sides non-negative, so squaring hid no sign. Standards
> covered: **A2.EO.2a/b/c**, **A2.EI.5a/b/c**, **A2.F.1b/c/e**, **A2.F.2a/f**, **A2.F.2i/j/k**.
> `make -C unit05/tests all` and `make -C unit05/test_keys all` → EXIT 0, and both `drop` targets ran
> (they are folded into `all`), so `unit05/sample_test/main.pdf` (4pp) and
> `unit05/sample_test_key/main.pdf` (5pp) hold the practice pair. `make -C unit05 student full` →
> EXIT 0: `target/compiled/unit06_student.pdf` is 115pp (practice test merged in) and
> `target/compiled/unit06_full.pdf` is 250pp (practice test + practice key merged in). Note that the
> unit-level `all` target builds only the lessons --- the merged unit packets come from
> `student`/`full`, and they land in `target/compiled/`, not `target/unit05/`.

- **5.0** Characteristics of radical functions *(introduces: restricted domain from the radicand,
  endpoint behavior, inverse relationship of families; both parents side by side — $y=\sqrt{x}$
  with domain $x\ge0$, an endpoint at the origin, an absolute min, one arm, vs. $y=\sqrt[3]{x}$
  with all reals, origin symmetry, and no extrema)* — A2.F.2a/b/c/d/e/f/g + A2.F.1a/e
- **5.1** $n$th roots & rational exponents *(index, even vs. odd index — why $\sqrt{-16}$ fails but
  $\sqrt[3]{-8}$ does not, principal root, $a^{m/n}=\sqrt[n]{a^m}$, exponent properties on rational
  exponents; the algebraic reason behind 5.0's domain split)* — A2.EO.2c
- **5.2** Simplifying radicals; adding & subtracting *(product/quotient properties, algebraic
  radicands, higher indices, then like-radical collection)* — A2.EO.2a/b
- **5.3** Multiplying & dividing radicals; rationalizing *(distribute/FOIL over radicals;
  **conjugates** for binomial denominators — callback to 2.4's complex conjugates)* — A2.EO.2b
- **5.4** Graphing radical functions & transformations *($y=a\sqrt{x-h}+k$ and
  $y=a\sqrt[3]{x-h}+k$; the endpoint is the transformation anchor; equation→graph and graph→equation
  both directions)* — A2.F.1b/c/e + A2.F.2a
- **5.5** Solving radical equations & extraneous solutions *(isolate → raise to the $n$th power →
  **always check**; extraneous roots explained as squaring destroying sign information — the
  structural echo of 4.6's excluded values; also $x^{m/n}=k$; verified graphically as an
  intersection)* — A2.EI.5a/b/c
- **5.6** Composition of functions *($(f\circ g)(x)$ numerically, graphically, and algebraically;
  order matters; domain of a composition)* — A2.F.2k
- **5.7** Inverse functions *(unit capstone: swap-and-solve, reflection over $y=x$, domain/range
  swap, why $y=x^2$ needs a restricted domain to have a square-root inverse — closes the loop opened
  in 5.0 — verified with 5.6's composition, $f(g(x))=g(f(x))=x$)* — A2.F.2i/j

### Unit 6 — Exponential Functions
> **Status (map confirmed & scaffolded 2026-07-27):** lesson map locked at **6 lessons (6.0–6.5)**,
> grounded against `spec/algebra2-vdoe-sol.pdf`. Two changes from the original ~5-lesson sketch:
> the order was set to characteristics → model form → graphing → solving → modeling → capstone
> (matching the Unit 4/6 shape), and a **new 6.5 (exponential regression & choosing a model)** was
> added because **A2.ST.2's exponential branch is otherwise unaddressed** — Lesson 1.5 covered that
> standard for lines only. All 6 lesson dirs `unit06/lesson00`–`lesson05` scaffolded with skeleton
> `main.tex` for lesson plan + cover, warmup, notes, activity, exit_ticket, homework, slides, and
> each `*_key`. Unit assessments scaffolded: `tests/{practice_test,actual_test}`, `test_keys/`,
> `sample_test{,_key}/`. **Authored to date: 6.0, 6.1, 6.2, 6.3, and 6.4 — all building.** Remaining:
> **6.5 (still skeleton)** and the four unit assessments, which should be written last so they can draw
> on the whole unit.
> **Standards coverage — note the shape:** there is **no `A2.EI` standard for exponential
> equations** (the EI strand runs absolute value → quadratic → quadratic systems → rational →
> radical → polynomial and stops), and **no `A2.EO` standard either**. Unit 6 therefore rests
> entirely on **A2.F.1a/b/c/e** (exponential parent + transformations + compare/contrast),
> **A2.F.2a–h** (characteristics; **h** names exponential explicitly for horizontal asymptotes),
> and **A2.ST.2d/e/g** (exponential curve of best fit). This is a genuinely lighter standards load
> than Units 4–5, which is why the unit is 6 lessons rather than 8.
> Lesson 6.0 introduces the one new spine row: ● growth vs. decay / constant ratio, and revisits
> ○ horizontal asymptote (● in U4) now as a **range boundary**.
> **Authoring note:** apply the §7 vocab-box paragraph-break fix in every notes/notes_key.
> **Lesson 6.0 authored & builds (2026-07-27):** all components + keys + 10-slide deck done. The
> lesson is organized around one sentence — **an asymptote is a boundary the range excludes, not a
> value the function reaches** — because the three errors students actually make (range written
> $[0,\infty)$, an invented absolute minimum of $0$, and a hunt for an $x$-intercept) are that single
> misconception in three costumes, and all three are the Unit 5 **endpoint** habit carried over
> unexamined. The growth parent $y=2^x$ and decay parent $y=\left(\frac12\right)^x$ are taught side
> by side (as U5 did for its two radical parents), and the escalation is named out loud: **U5 took
> away half the domain; U6 hands the domain back and takes half the range**. Also established: the
> family has **no zeros, ever** (a positive base to any real power is positive — earned numerically
> in Warm-Up item 1, where $2^{-8}=\frac1{256}$ is tiny but not negative and not zero), **no extrema
> and no turning points**, and end behavior with two different *kinds* of end — one arm to $\infty$,
> the other **flattening** onto the asymptote, the deliberate mirror of 5.0's "the graph stops"
> (with "$y\to-\infty$," the Unit 3 odd-degree reflex, flagged as the signature wrong answer). The
> **fingerprint test** (constant difference / constant second difference / **constant ratio**)
> reactivates 1.0 and 2.0 and returns as 6.5's opening move; growth vs. decay is read off $b$ **vs.
> $1$, never vs. $0$**, and never off $a$ (homework row $y=0.4(3)^x$ is the deliberate trap). Two
> Unit 4 contrasts are drawn: a rational graph may cross its HA in the middle, an exponential never
> crosses its own. Anchor $f(x)=4\left(\frac12\right)^x$; $b$ is also pulled off a *graph* by
> dividing consecutive outputs — the skill 6.1 and 6.5 both need. Tier E carries the only negative-$a$
> function of the day ($y=-2\cdot3^x$, range $(-\infty,0)$ — the sign of $a$ picks the *side* of the
> asymptote, with reflections deferred to 6.2) plus a medication model $A(t)=200(0.7)^t$; homework's
> extension is a depreciation model $V(t)=1200(0.75)^t$ whose "why $b=0.75$ and not $0.25$?" is the
> direct set-up for 6.1. All graphs pre-drawn via `plot`+`\clip` (no sketch-from-scratch); every
> exponential is plotted as $a\,e^{(\ln b)x}$ because pgfmath's `pow()` is unreliable for negative
> and fractional exponents. Standards: **2023 VA SOL A2.F.2a/c/d/f/g** and **A2.F.2h** (horizontal
> asymptotes — the standard names exponential explicitly), **A2.F.2b** (compare/contrast — the
> fingerprint table and the growth-vs-decay table), **A2.F.1a** (parent graphs) and **A2.F.1e**
> (graphs/tables/equations — Activity Tier A). Warm-up & exit ticket each fit one page (blank+key);
> notes 6pp (key 6pp), activity 3pp (key 4pp), homework 3pp (key 4pp), lesson plan 4pp; exit ticket
> includes an SOL-style MC item (range of $6\left(\frac13\right)^x$; distractors = closed bracket /
> forgot the floor / decay-means-negative). `make -C unit06/lesson00 all` → EXIT 0 (student 15pp,
> full 31pp).
>
> **Lesson 6.1 authored & builds (2026-07-28):** all components + keys + an 11-slide deck.
> `make -C unit06/lesson01 all` → EXIT 0 (student 13pp, full 29pp); warm-up and exit ticket each fit
> **exactly one page** blank *and* key, and notes/notes_key paginate identically at 4pp
> (activity 3pp / key 4pp, homework 3pp / key 3pp, lesson plan 4pp). The §7 vocab-box fix is applied.
> The lesson is organized around one sentence — **the base is the fraction you end up with, not the
> percent that changed** — because the three errors students actually make are all violations of it:
> $b=0.08$ for "up $8\%$" (percent-as-base), $b=1.15$ for "down $15\%$" (sign error), and
> $b=0.12$ for "loses $12\%$". The Warm-Up earns the rule numerically before it is stated — a \$50
> jacket worked *twice*, once by finding the change and once as a single multiplication, ending on
> "the new price is ___% of the old price," so students say **$108\%$** before they ever see $1+r$.
> Three build-sources are taught in the order table → story → two points, deliberately mirroring
> **A2.F.1e**: the *same* form gets written from three different representations. From a table both
> numbers are free ($a$ is the $x=0$ column, $b$ is 6.0's constant ratio); from a story the percent
> must be translated; from two points, **dividing the two equations cancels $a$** and the leftover
> exponent is the **gap** between the inputs (the part students drop), with the cube root pulled
> straight from Unit 5. The Hook is two towns with the same population — Riverton "+300 people a
> year" vs. Kellsboro "+4% a year" — which reactivates 6.0's add-vs-multiply fingerprint and asks
> "$4\%$ *of what?*"; the teacher then writes $8000(0.04)^t$ on the board on purpose and lets
> $P(1)=320$ kill it. **A2.F.2f is the assessed standard**: every model built is evaluated *and*
> read back as a sentence (town $P(10)\approx16{,}127$; car $V(5)\approx\$12{,}666$; books
> $V(3)\approx\$2940.10$; bacteria $C(6)\approx1882$; phone $V(4)\approx\$333.14$), and a bare
> number is explicitly not an answer. Error analysis is a first-class item type here, in three
> places (Activity Tier A's three-student deer herd, Homework 5's Jonah/Priya, ET distractors) and
> always phrased as *what situation would this model be right for?* — because the sign error and the
> percent-as-base error need different re-teaches. Activity Tier E Part 3 (a 240-gal tank losing
> 60 gal/day vs. 25%/day, identical on day 1) is the linear-vs-exponential contrast in context and
> revisits 6.0's asymptote: the linear model goes **negative** by day 14, the exponential one never
> reaches 0. The homework extension (Ashford $20{,}000$ at $-2\%$ vs. Brookvale $12{,}000$ at $+5\%$)
> locates the crossing between years 6 and 8 from a table and then **fails** to solve
> $20{,}000(0.98)^t=12{,}000(1.05)^t$ for lack of a common base — **6.4's wall, arriving early on
> purpose**; leave it standing and do not mention logarithms. All graphs pre-drawn via
> `plot`+`\clip` as $a\,e^{(\ln b)x}$ (no sketch-from-scratch). Standards: **A2.F.2f** (primary),
> **A2.F.1e** (three representations of one form), **A2.F.2b** (linear vs. exponential),
> **A2.F.2a/h** (range and asymptote used to validate a model), and it is the stated prerequisite
> for **A2.ST.2d/e** in 6.5 — the Activity's reverse-translation table is exactly the "technology
> hands you $a$ and $b$; say what they mean" skill.
>
> **Lesson 6.2 authored & builds (2026-07-28):** all components + keys + a 10-slide deck.
> `make -C unit06/lesson02 all` → EXIT 0 (student 13pp, full 29pp); warm-up and exit ticket each fit
> **exactly one page** blank *and* key; homework 3pp/3pp; notes 4pp (key 5pp) and activity 3pp (key
> 4pp), where the extra key page is **teacher note only** and pp. 1–4 / 1–3 align with the blank. The
> §7 vocab-box fix is applied. The lesson is organized around one sentence — **only $f(x)+k$ moves the
> asymptote, and everything that depends on the asymptote moves with it** — which is what finally
> gives the inside/outside distinction consequences: $h$ slides the graph past an asymptote that never
> budges, $a$ picks the *side* of it, and only $k$ relocates it to $y=k$, taking the range
> $(k,\infty)$ / $(-\infty,k)$ with it. The Hook deliberately mirrors 5.4's: three pre-drawn graphs of
> $2^{x}$, $2^{x}-3$, and $2^{\,x-3}$ with their asymptotes dashed — *two equations contain a $3$,
> both graphs moved, why is only one dashed line somewhere new?* — closing by pointing at graph II
> crossing the $x$-axis and asking students to reconcile it with Lesson 6.0. That is the unit's second
> **refinement, not contradiction** beat: 6.0's "no zeros, ever" was a claim about $y=ab^{x}$ (i.e.
> $k=0$), and the precise rule is that the graph has an $x$-intercept **exactly when $a$ and $k$ have
> opposite signs** — a criterion reused as the closing question of the Homework feature table, in
> Tier A's matching, and in Tier E Part 2. The signature error of the day is the **two minus signs**:
> $-b^{x}$ negates the *output* (flip over the $x$-axis, range to the other side of the asymptote,
> base unchanged so **still growth**) versus $b^{-x}$ negating the *input* (flip over the $y$-axis,
> range unchanged, and genuinely **decay**, since $b^{-x}=\left(\frac1b\right)^{x}$ — the Unit 5
> negative-exponent property, earned numerically in Warm-Up item 3 before it is ever stated).
> "$-2^{x}$ is decay" is refused throughout and tied back to 6.0's *read the family off $b$, never off
> $a$*; the Homework's $y=-4^{x}$ row and the slides' four-row family table are the deliberate traps.
> Graph → equation is taught as a strict **three-step order** — dashed line gives $k$, the
> $y$-intercept is $a+k$ (so subtract before claiming $a$), one more point gives $b$ — because
> skipping step 1 produces $a=5$ instead of $3$ every time; this is the reading 6.5 leans on, and
> Tier A repeats it with a *negative* $k$ so that $a$ comes out **larger** than the intercept. Tier E
> carries the one piece of genuinely new mathematics: $2^{\,x-3}=\frac18\cdot2^{x}$, so for this
> family a horizontal shift and a vertical compression are the **same transformation** (the
> exponential analogue of 5.4's input/output equivalence), with part (d) testing the same trick on
> $(x-3)^{2}$, where it fails. Two modeling contexts make $k$ physical: cooling coffee
> $T(t)=68+132(0.85)^{t}$ (Activity Tier E) and a soda warming, $T(t)=72-34(0.9)^{t}$ (Homework
> extension, where $a<0$ because the soda starts *below* the asymptote) — both with an
> algebraic-versus-contextual range beat, and both ending on an equation with **no common base**
> ($132(0.85)^{t}=32$ and $(0.9)^{t}=2.118$), left standing on purpose for 6.4 / Unit 7; logarithms
> are never named. The soda's $x$-intercept question is answerable *without* logs — a base under $1$
> exceeds $1$ only at a negative exponent — which is the reasoning 6.3 formalizes. All graphs
> pre-drawn via `plot`+`\clip` as $a\,e^{(\ln b)(x-h)}+k$ (no sketch-from-scratch). Standards:
> **A2.F.1b/c** (primary — transformations of the exponential parent and the effect of each
> parameter), **A2.F.1e** (equation ↔ graph ↔ table, run in both directions), **A2.F.2h** and
> **A2.F.2a** (horizontal asymptote and range — the measure applied to every item on every page).
> Exit ticket includes an SOL-style MC item (range of $3(2)^{x}-6$; distractors = bracket error /
> ignored the shift / sign of $k$ backwards).
>
> **Lesson 6.3 authored & builds (2026-07-28):** all components + keys + a 10-slide deck.
> `make -C unit06/lesson03 all` → EXIT 0 (student 13pp, full 27pp); warm-up and exit ticket each fit
> **exactly one page** blank *and* key, and notes (4pp), activity (3pp) and homework (3pp) each
> paginate identically to their keys. The §7 vocab-box fix is applied. **This is the course's first
> no-standard lesson, and it establishes the house pattern for 7.3 and 7.4:** the Primary Objective box
> states **``Standards (2023 VA SOL): none --- beyond-SOL / precalculus prep''** with the audit
> reasoning inline (no `A2.EI` strand for exponential equations, no `A2.EO` standard either), names the
> two standards merely *exercised* rather than claimed (**A2.EO.2c** supplies every Step-1 rewrite,
> **A2.F.2a** is what rules solutions out), and the exit ticket deliberately carries an **ordinary**
> multiple-choice item, with a note in the plan saying why it is not SOL-style.
> The lesson is organized around one sentence — **you may drop the base because an exponential never
> uses the same output twice** — which converts the one-to-one property from a rule into a consequence
> of Lesson 6.0's *no turning points*. The Hook is the whole lesson in one picture: $y=x^{2}$ and
> $y=2^{x}$ with the **same** gold line $y=4$ across both, two crossings against one, so that $x=\pm2$
> versus $x=2$ is explained by shape before any algebra — and the Unit 2 $\pm$ reflex is named and
> refused on the spot. Section 1 then pays off a debt from 6.1: students accepted $b>0$, $b\neq1$ as a
> rule about *models*, and $1^{5}=1^{9}$ shows those are exactly the conditions that make *solving*
> valid (Tier E Part 2 makes students build the counterexample themselves and discover $1^{x}=1$ has
> infinitely many solutions). Step 1 is openly Unit 5 work and is where every mechanical error lives;
> both are defused **numerically in the Warm-Up before being stated** — $2^{3}\cdot2^{4}=128=2^{7}$
> against $\left(2^{3}\right)^{4}=4096=2^{12}$ — and they recur as the two named students in the
> Activity (Devon adds instead of multiplying; Priya never rewrites the left side of $9^{x}=27$) and
> again with new numbers in the homework (Jamal, Elise). Non-integer answers are treated as a
> first-class teaching point rather than an accident: $\frac23$ is checked in full as
> $8^{2/3}=\left(\sqrt[3]8\right)^{2}=4$, and the homework asks students to *list* their three
> fractional answers and say why that is not a symptom of error. Section 4 makes every solution an
> intersection — $2^{x}=4$ at $x=2$ is precisely where $y=2^{x}-4$ crossed the $x$-axis in 6.2, the
> payoff 6.2's homework and roadmap both promised — and establishes the count: one solution when
> $c>0$, none when $c\le0$, never two. **The distinction the whole lesson builds toward is between two
> failures that look identical on paper:** $2^{x}=-3$ has *no solution* (a range fact, no algebra
> needed), while $2^{x}=5$ *has* one this method cannot reach. That pair is the Exit Ticket's item-4
> follow-up (``does $2^{x}=10$ still have a solution?'' — ``no'' is the wrong answer and the single most
> informative response on the page), Tier E Part 3(e) ($50\cdot2^{t}=1000$ against $50\cdot2^{t}=0$),
> and the homework Extension, where $4^{x}\cdot2^{\,x+1}=8^{\,x-1}$ reduces to $1=-3$ and is then
> re-read in **6.2's** language as two vertical stretches of $y=8^{x}$ ($2\cdot8^{x}$ and
> $\frac18\cdot8^{x}$) that cannot meet because $8^{x}$ is never $0$. Students leave with a written list
> of four unsolved-but-solvable equations — $2^{x}=5$, the coffee, the soda, and $1000(1.05)^{t}=2000$ —
> which is 6.4's opening move. Logarithms are never named. All graphs pre-drawn via `plot`+`\clip` (the
> parabola plotted directly, exponentials as $a\,e^{(\ln b)x}$); the Hook's lead-in and its two graphs
> are wrapped in a `minipage` so the page break cannot orphan the sentence from the picture.
>
> **Lesson 6.4 authored & builds (2026-07-28):** all components + keys + a 10-slide deck.
> `make -C unit06/lesson04 all` → EXIT 0 (student 13pp, full 28pp); warm-up and exit ticket each fit
> **exactly one page** blank *and* key, activity and homework paginate identically to their keys at 3pp,
> and notes are 4pp against a 5pp key whose extra page is **teacher note only** (pp. 1–4 align). The §7
> vocab-box fix is applied, and `\boxguard` is used before notes Sections 1–3 and `\boxguard[30]` before
> Section 4 (which opens with a tikzpicture). The lesson is organized around one sentence — **the base is
> what happens in one period, and the exponent counts the periods** — because compound interest,
> continuous growth, half-life, and doubling are that one sentence four times, and because the day's two
> signature errors are that sentence broken in half in opposite directions: $1000(1.08)^{20}$ keeps the
> annual rate with the quarterly count, $1000(1.02)^{5}$ splits the rate but counts years. They appear as
> **Renata and Miles** in Activity Tier A (with the closing question asking students to name the one
> sentence both broke) and again in different models as **Tobias** (annual base, monthly count) and
> **Marisol** ($t$ where $t/h$ belongs) in the homework, where the absurd sizes of the wrong answers
> (\$81,969.36 from \$5000; $0.00034$ mg from 90 mg) are taught as the reasonableness check. The Hook is
> four banks paying $6\%$ on \$1000 — \$1060.00 / \$1061.36 / \$1061.68 / \$1061.83 — printed rather than
> computed, because the surprise is the *differences* ($+\$1.36$, $+\$0.32$, $+\$0.15$): compounding 365
> times as often earns **\$1.83**. That shrinking is what makes $e$ necessary rather than decorative, and
> $e$ is **earned numerically** from $\left(1+\frac1m\right)^{m}$ ($2.71692$, $2.71815$, $2.71827$ — "the
> digits are freezing from the left") and named as *the number the chopping runs into*, never by a
> formula; $A=Pe^{rt}$ is then read as a **ceiling**, and the \$2500-at-$4\%$-for-6-years thread
> (\$3163.30 annually / \$3174.34 quarterly / \$3178.12 continuously) answers the Hook out loud —
> compounding schedules are not where returns come from. Half-life arrives as *the same sentence on a
> different clock*: the Warm-Up produces **1.5 halvings in 9 hours** before any formula, so $t/h$ is a
> unit conversion rather than a rule, and the 80 mg tracer table saves $t=9$ ($28.28$ mg) for last as the
> fractional-exponent beat — the direct descendant of 6.3's $x=\frac23$. **6.3's method is shown to
> survive selectively**, which is a genuinely new structural point: $80\left(\frac12\right)^{t/6}=10$ has
> a common base ($\frac18$) and $=25$ does not ($\frac5{16}$), so half-life questions often *are* 6.3
> problems while interest questions essentially never are (Activity Tier E Part 3 pairs 75 mg against
> 200 mg on one drug to isolate exactly this). The lesson ends on the promised **wall**:
> $1000(1.05)^{t}=2000\Rightarrow(1.05)^{t}=2$, bracketed on a pre-drawn graph between $t=14$
> (\$1979.93) and $t=15$ (\$2078.93) so the answer visibly **exists**, held against $2^{x}=-3$ which has
> none — the 6.3 distinction, one day later, in a context students care about. The running list is now
> five long ($2^{x}=5$, the coffee, the soda, the investment, and the homework's truck
> $(0.82)^{t}=0.5$); logarithms are never named. Two beyond-computation beats: Tier E's **Rule of 72**
> is taught as *calibration* (excellent at $8\%$, drifting at $5\%$ and $12\%$) with "why 72?" answered
> only as "that is a logarithm question, and it is Unit 7"; and the homework Extension's depreciating
> truck ends on the asymptote being **mathematically right and physically wrong**, deliberate set-up for
> 6.5's extrapolation discussion. Every graph is pre-drawn on a money-sized grid (anisotropic tikz unit
> vectors, `xstep`/`ystep` grids) with the curve plotted as $P\,e^{(\ln b)t}$. Standards:
> **A2.F.2f** (primary), **A2.F.2a** and **A2.F.2h** (range and horizontal asymptote of every decay
> model), **A2.F.1e** (verbal → equation → table/graph). Exit ticket includes an SOL-style MC item
> (\$1500 at $4.8\%$ quarterly for 7 yr; the three distractors are *neither converted*, Miles's error,
> and Renata's error, so the wrong answer names the re-teach).

- **6.0** Characteristics of exponential functions *(introduces: growth vs. decay and the constant
  multiplicative rate / **constant ratio**; revisits the horizontal asymptote as a **range
  boundary**. Growth $y=2^x$ and decay $y=(\frac12)^x$ taught side by side, as Unit 5 did for the
  two radical parents. The escalation reverses: U5 took away half the **domain**, exponential hands
  the domain back and takes half the **range**. First family in the course with **no zeros, ever**;
  no extrema, no turning points; end behavior with two different *kinds* of end — one arm to
  $\infty$, the other flattening onto the asymptote, the mirror of 5.0's "the graph stops". Family
  fingerprint from a table: constant difference (1.0) / constant second difference (2.0) /
  **constant ratio**)* — A2.F.2a/b/c/d/f/g/h + A2.F.1a/e
- **6.1** Exponential growth & decay — building $y=ab^x$ *($a$ = initial value, $b$ = growth factor;
  why $b>0$ and $b\ne1$; the percent↔factor translation ("up 8%" $\Rightarrow b=1.08$; "loses 15%"
  $\Rightarrow b=0.85$) with its two signature errors ($b=0.08$, and $b=1.15$ for a decrease);
  writing the equation from a table, from two points, from a story)* — A2.F.2f, feeding A2.ST.2d/e
  — **authored & building 2026-07-28**
- **6.2** Graphing exponential functions & transformations *($f(x)+k$ is the only transformation
  that **moves the asymptote** — and therefore the range; $kf(x)$ moves the $y$-intercept but not
  the HA; $f(x+k)$ and $f(kx)$; reflections carry real content — $f(-x)$ turns growth into decay
  because $2^{-x}=(\frac12)^x$, a 5.1 exponent identity rather than a new rule)* —
  A2.F.1b/c/e + A2.F.2a/h — **authored & building 2026-07-28**
- **6.3** Solving exponential equations with a common base *(one-to-one property: rewrite both sides
  over one base, equate exponents; runs on Unit 5's machinery — $8^x=4$, $3^x=\frac1{27}$,
  $\sqrt[3]{2}=2^{1/3}$; verified graphically as an intersection)* — **supporting skill, no SOL
  standard**; kept because Unit 7 needs it and it sets up 6.4's wall — **authored & building
  2026-07-28**
- **6.4** Modeling: compound interest, half-life, and $e$ *($A=P(1+\frac rn)^{nt}$ compounded
  annually → quarterly → daily, the limit that **produces $e$**, then $A=Pe^{rt}$; half-life
  $A_0(\frac12)^{t/h}$, doubling time, depreciation. Ends on a deliberate **wall**:
  $2000=1000(1.05)^t$ has no common base — readable off a graph, not yet solvable — which is Unit
  8's opening move, the same device used at 3.2→4.3)* — A2.F.2f/a/h — **authored & building
  2026-07-28**
- **6.5** Exponential regression & choosing a model *(unit capstone: linear vs. quadratic vs.
  exponential from real data — 6.0's fingerprint test applied to a scatterplot — model from
  technology, interpret $a$ and $b$ in context, predict, and an "extrapolation breaks" beat that
  bites far harder on an exponential than it did on 1.5's line)* — A2.ST.2d/e/g + A2.F.2b

### Unit 7 — Logarithmic Functions
> **Status (scaffolded 2026-07-27; Lesson 7.0 authored & building):** locked at
> **7 lessons (7.0–7.6)**. The unit was opened ahead of Units 5–6 at the user's request, so only
> `unit07/lesson00` has been scaffolded — `lesson01`–`lesson06` still need `new_lesson.py` runs, and
> the unit assessments laid down with the unit (`tests/{practice_test,actual_test}`, `test_keys/`,
> `sample_test{,_key}/`) are still skeletons. **Lesson 7.0 is fully authored**: lesson plan, cover,
> warm-up, guided notes, activity, exit ticket, homework, an 11-frame slide deck, and all five answer
> keys. `make -C unit07/lesson00 all` → EXIT 0 (`lesson00_student.pdf` 13 pp, `lesson00_full.pdf`
> 31 pp); the warm-up and exit ticket each fit **exactly one page** in blank *and* key, and
> notes/notes_key paginate identically at 5 pp. The §7 vocab-box paragraph-break fix is applied in
> `notes/` and `notes_key/`.
>
> **Unit 6 cross-references: checked 2026-07-27, consistent.** 7.0 was authored before Unit 6
> existed, so its warm-up and hook lean on the exponential parent. Lesson 6.0 has since landed and
> the two agree — same parent $y=2^{x}$ with the same lattice points $(0,1),(1,2),(2,4),(3,8)$, range
> $(0,\infty)$ *not* $[0,\infty)$, horizontal asymptote $y=0$, and the same
> `\draw[navy, dashed, semithick]` convention. 7.0 also already makes the
> **attained endpoint vs. never-reached asymptote** contrast against Unit 5, which is exactly the
> distinction 7.0 carries into the log domain ($>0$, not $\ge 0$). No edits were needed.
> **6.4 landed 2026-07-28, so 7.4 and 7.5 are unblocked.** 7.4's cliffhanger is now concrete and
> five equations long — 6.4's notes and homework leave students with a posted list ($2^{x}=5$,
> $132(0.85)^{t}=32$, $(0.9)^{t}=2.118$, $(1.05)^{t}=2$, $(0.82)^{t}=0.5$), every one of which has an
> answer and none of which has a common base; **7.4 should take that exact list down, in that order.**
> 7.5 can rely on $e$ being introduced numerically (the $\left(1+\frac1m\right)^{m}$ table, $e$ as *the
> number the chopping runs into*, $A=Pe^{rt}$ as a **ceiling**) but **not** on any limit notation or
> any use of $\ln$ — 6.4 never names logarithms. 7.4 also establishes the *base-is-one-period /
> exponent-counts-periods* sentence and the half-life form $A_{0}\left(\frac12\right)^{t/h}$, which is
> what 7.5 finally solves for $t$.
>
> The map moved twice in one day. It was first cut from a 6-lesson sketch to 5 after a standards
> audit of `spec/algebra2-vdoe-sol.pdf` found **logarithms in only two 2023 VA SOL standards** —
> `A2.F.1` (a/b/c/e) and `A2.F.2` (a–h, i/j) — with **no `A2.EO` standard for log properties and
> no `A2.EI` standard for logarithmic equations** (the same gap Unit 6 documents for exponentials).
> It then grew to 7 when the Unit 6 map landed and three collisions were resolved (below).
>
> **Collisions with Unit 6, resolved 2026-07-27.** Both unit maps were confirmed the same day in
> separate sessions; neither saw the other. Rulings:
> 1. **`A2.ST.2` belonged to Unit 6, not Unit 7.** The standard names the curve of best fit as
>    "linear, quadratic, exponential, or a combination" — **logarithmic is not in the list**, so
>    Unit 7 never had a real claim. **6.5 keeps the regression capstone outright**; the Unit 7
>    modeling lesson was rewritten as **7.5 (natural logs & log scales)** with an `A2.F.2f` anchor.
> 2. **Natural log now has a definite home: 7.5.** Unit 6's ruling assigned $\ln$ to "7.5", which
>    the interim 5-lesson map had deleted; the lesson is restored under that number. $e$ itself
>    stays in **6.4** as the limit of ever-more-frequent compounding, per the Unit 6 ruling.
> 3. **No-standard content is now handled symmetrically.** Unit 6 keeps **6.3** (common-base
>    solving) as a full lesson despite having no SOL standard; Unit 7's **7.4** (solving log &
>    exponential equations) is likewise **restored to a full lesson**, reversing the earlier Tier E
>    demotion. This keeps the promise **6.4** makes — it ends on $2000=1000(1.05)^t$, "no common
>    base … which is Unit 7's opening move" — for every student rather than only in enrichment.
>    **Consequence:** **7.3 (properties of logarithms) had to be promoted out of Tier E as well**,
>    since condensing is a prerequisite for solving $\log x + \log(x-3) = 1$. Both lessons are
>    labelled **beyond-SOL / precalculus prep** and must stay off the SOL-style test items.
>
> **Authoring constraint for 7.2:** `A2.F.1b` limits **graph → equation** for exponential and
> logarithmic functions to a **single transformation**. `A2.F.1c` (equation → graph) carries no such
> cap, so multi-step transformations are fair game in that direction only. *(Unit 6 recorded the
> identical constraint independently — it binds both units.)*
> **Authoring note:** apply the §7 vocab-box paragraph-break fix in every notes/notes_key.
>
> **Authoring note — the TikZ logarithm macro (established in 7.0).** pgfmath has no `log_b`, so
> every logarithmic curve is drawn by *parameterizing on $y$* rather than $x$, which also renders
> smoothly right up to the asymptote:
> ```latex
> % y = log_b(x-h) + k   <=>   x = b^(y-k) + h.   Args: {b}{h}{k}{ymin}{ymax}
> \newcommand{\logcurve}[5]{\draw[very thick, forest, domain=#4:#5, samples=120, smooth]
>   plot ({pow(#1,\x-(#3))+(#2)},{\x});}
> ```
> Reuse it verbatim in 7.1–7.6. Asymptotes follow the Unit 4 convention:
> `\draw[navy, dashed, semithick]`.

- **7.0** Characteristics of logarithmic functions ***(authored & building 2026-07-27)*** *(the unit's only ● spine row — **inverse of
  exponential, domain/range swap**. Built by reflecting Unit 6's $y=b^x$ over $y=x$: domain $x>0$
  and **why** (the exponential's range becomes the log's domain), range all reals, **vertical
  asymptote $x=0$** — the exponential's horizontal asymptote reflected, revisiting the Unit 4
  asymptote row in a new place — $x$-intercept $(1,0)$ and no $y$-intercept, increasing $b>1$ vs.
  decreasing $0<b<1$, end behavior that grows without bound but slowly, no extrema. Inherits 6.0's
  "no zeros, ever" contrast: the exponential has no $x$-intercept and the log has no $y$-intercept
  — the same fact reflected. $\log_b x$ arrives as the **name of that curve**, not yet as an
  operation — the 5.0-before-6.1 move that let students read $\sqrt{x}$ before meeting rational
  exponents)* — A2.F.2a/b/c/d/e/f/g/h + A2.F.1a/e + A2.F.2i/j
- **7.1** Introduction to logarithms *(log ⇄ exponential form as one statement read two ways — "a
  logarithm **is** an exponent"; evaluating by asking "$b$ to what power?"; common log; the four
  identities $\log_b 1=0$, $\log_b b=1$, $\log_b b^x=x$, $b^{\log_b x}=x$; and **change of base**
  for calculator work. Domain re-derived algebraically — the log of a negative or zero is
  undefined, which is 7.0's $x>0$ restriction arriving a second time by a different road)* —
  supports A2.F.2a/f; the notational foundation the rest of the unit requires
- **7.2** Graphing logarithmic functions & transformations *($y=a\log_b(x-h)+k$, with the
  **vertical asymptote as the transformation anchor** — the structural role the endpoint played in
  6.4 and the vertex in 2.1. Mirrors 6.2 exactly: there, $f(x)+k$ was the only transformation that
  moved the *horizontal* asymptote and therefore the range; here $f(x+k)$ is the only one that moves
  the *vertical* asymptote, and therefore the domain. Respect the single-transformation cap on
  graph → equation)* — A2.F.1a/b/c/e + A2.F.2a/h
- **7.3** Properties of logarithms *(product, quotient, and power; expanding & condensing. Derived
  rather than announced — each property is an exponent law in disguise ($b^m\cdot b^n=b^{m+n}$
  *is* the product rule), the same "insist the old rules survive" move named aloud in 5.1.
  Signature trap: $\log(x+y)\ne\log x+\log y$, killed numerically. Change of base returns as a
  consequence rather than a memorized formula)* — **beyond-SOL / precalculus prep, no standard**;
  kept because 7.4 cannot run without condensing *(same reasoning that kept 6.3)*
- **7.4** Solving logarithmic & exponential equations *(the lesson **6.4's cliffhanger promises**:
  $2000=1000(1.05)^t$ finally falls. One-to-one property; take a log of both sides; condense-then-
  convert for log equations; and **extraneous solutions** — a candidate making any argument $\le 0$
  is rejected, the *third* appearance of that structure after 4.6 (excluded values) and 5.5
  (squaring destroys sign), and the first time the rejection comes from a **domain restriction**
  rather than an algebraic artifact. Verified graphically as an intersection)* — **beyond-SOL /
  precalculus prep, no standard**; kept for the same reason 6.3 was
- **7.5** Natural logarithms & logarithmic scales *($\ln$ as $\log_e$, the inverse of the $e^x$
  introduced in 6.4 — so the 7.0 reflection argument runs once more on a specific base; solving
  continuous-growth models $A=Pe^{rt}$ for time with $\ln$, half-life and doubling time finished
  properly. Then **log scales as the answer to "why did anyone invent this"**: pH, Richter, and
  decibels compress multiplicative ranges into additive ones, so "two points on the Richter scale"
  means a factor of 100, not a difference of 2 — read off pre-drawn scale diagrams and tables)* —
  A2.F.2f *(A2.ST.2 deliberately **not** claimed here — it is 6.5's, see collision 1)*
- **7.6** Comparing function families *(**course capstone**: identify the family from a graph,
  table, or equation across all eight families met since Unit 1; compare domain/range, asymptotes,
  intercepts, symmetry, and end behavior side by side; and settle the "which eventually wins"
  question — linear vs. quadratic vs. exponential vs. logarithmic growth rates off pre-drawn graphs
  and tables, with the exponential-beats-polynomial and log-loses-to-everything results made
  concrete. Extends 6.0's constant-difference / second-difference / constant-ratio fingerprint test
  into a full identification toolkit. Claims the `A2.F.1e` / `A2.F.2b` compare-and-contrast clauses,
  which every unit since 1.0 has applied in passing but no lesson has ever made the teaching
  focus)* — A2.F.1e + A2.F.2b

---

## 5. Assessment structure

Per Unit 1's pattern:
- **Per lesson:** warm-up, exit ticket, homework (each with key).
- **Per unit:** unit cover + sample test + sample test key.
- **Course-level reference exists** in `spec/`: mid-year test and final exam
  (All Things Algebra originals) — usable as models, not for redistribution.

*(Open: mid-year checkpoint placement — natural break after Unit 3.)*

---

## 6. Decisions & remaining open questions

**Resolved:**
- **The Algebra 1 review unit is dropped (2026-08-20, EFFL redesign)** — it had been built as a
  4-lesson review citing **A.\*** codes from `spec/algebra1-vdoe-sol.pdf`, but the redesign
  removed it outright and renumbered old Units 2–8 to 1–7. Its earlier rulings (no ATA drop-ins,
  A.EI.2 and A.ST.1 omitted from the review) are moot with it; the standing consequences are that
  **no Algebra 1 standards are formally reviewed** (prior knowledge is exercised inside each
  unit's warm-ups instead) and regression is taught in place — Lesson 1.5 for linear and
  Lesson 6.5 for exponential.
- Absolute-value & piecewise functions → **Unit 1**.
- Complex numbers → **Unit 2** (with quadratics); quadratic systems → **Unit 2**.
- Advanced factoring (sum/difference of cubes, two-variable expressions) → **Unit 3**.
- Conic sections, sequences & series, probability & statistics, trigonometry →
  **out of scope** (no material taught).
- Systems of **linear** equations/inequalities & linear programming →
  **out of scope** (omitted). *(Systems of **quadratics** remain in Unit 2.)*
- **Direct/inverse variation → a required Unit 4 lesson (4.7)**, not optional — A2.F.1d has no
  other home in the course. *(Joint variation is not named in the standard; enrichment only.)*
- **Slant/oblique asymptotes → Tier E enrichment in 4.5, never assessed** — A2.F.2h covers
  vertical and horizontal asymptotes only.
- **Unit 4 lesson map → 8 lessons (4.0–4.7)**, splitting graphing into a transformations lesson
  (A2.F.1) and an analyze-and-graph lesson (A2.F.2).
- **Unit 5 lesson map → 8 lessons (5.0–5.7)**, splitting radical operations into 5.2/6.3 and
  composition (5.6) from inverses (5.7).
- **Radical equations capped at one radical** per A2.EI.5a — two-radical equations are Tier E
  enrichment only, never assessed *(same treatment slant asymptotes got in 4.5)*.
- **Cube root gets equal billing with square root** throughout Unit 5 — A2.F.1 and A2.F.2 both name
  the two families explicitly, so 5.0 and 5.4 teach them side by side rather than treating
  $\sqrt[3]{x}$ as an afterthought.
- **Inverse functions & composition → Unit 5 (5.6–5.7)**, not a standalone unit — A2.F.2i/j/k have
  no other home, and the square-root/quadratic pair is the natural motivating example.
- **Unit 6 lesson map → 6 lessons (6.0–6.5)**, not the original ~5 — a regression/model-choice
  capstone (6.5) was added to cover **A2.ST.2's exponential branch**, which Lesson 1.5 handled for
  lines only. The unit stays shorter than 5–6 because exponentials have **no A2.EO and no A2.EI
  standard** at all.
- **Common-base exponential solving (6.3) is kept despite having no SOL standard** — Unit 7's
  logarithmic solving depends on it, and it is what makes 6.4's "no common base exists" wall honest.
- **Exponential transformations given a *graph* are capped at a single transformation** per the
  explicit clause in A2.F.1b. Multi-transformation work is equation→graph and Tier E only *(same
  treatment slant asymptotes got in 4.5 and two-radical equations in 5.5)*.
- **$e$ does not get its own lesson** — it is introduced inside 6.4 as the limit of ever-more-
  frequent compounding, since the standards never name it separately. Natural log stays in 7.5.
- **A2.ST.1 (normal distribution, $z$-scores, Empirical Rule) → out of scope**, confirmed
  2026-07-27. Consistent with the probability & statistics exclusion above; A2.ST.2 remains in
  (Lesson 1.5 for lines, Lesson 6.5 for exponentials). Closed — do not re-raise.

- **Unit 7 lesson map → 7 lessons (7.0–7.6)** *(confirmed 2026-07-27)*. Full rationale in the
  Unit 7 status block in §4.
- **Properties of logarithms (7.3) and solving logarithmic/exponential equations (7.4) are kept as
  full lessons despite having no SOL standard** — the same ruling 6.3 got, applied symmetrically.
  The standards audit found logarithms only in `A2.F.1` and `A2.F.2`: there is **no `A2.EO`
  standard for log properties and no `A2.EI` standard for logarithmic equations**. Both are
  labelled **beyond-SOL / precalculus prep** and must stay **off the SOL-style test items**, but
  they are taught and assessed on the unit test. Keeping 7.4 is what makes 6.4's "no common base"
  cliffhanger honest for every student; keeping 7.3 is forced by 7.4, which cannot run without
  condensing. *(Supersedes the interim ruling that demoted both to Tier E.)*
- **`A2.ST.2` belongs to Unit 6 alone (6.5), not Unit 7** — the standard names the curve of best
  fit as "linear, quadratic, exponential, or a combination"; **logarithmic is not in the list**.
  Unit 7's modeling lesson (7.5) therefore claims `A2.F.2f` and covers $\ln$ and log scales
  instead of regression.
- **Natural log → Unit 7 (7.5)**, consistent with the 6.4 ruling above; $e$ itself stays in 6.4.
- **`A2.F.1e` / `A2.F.2b` (compare & contrast the families) → Unit 7 (7.6)** as an explicit lesson,
  the course capstone. Every unit applied these clauses in passing, but no lesson ever made them
  the teaching focus.

**Still open:**
- **Pacing:** days per lesson / target unit lengths, and how they fit the calendar. **Unit 7 at 7
  lessons is the longest of the back half** — if the calendar is tight, the compression candidate
  is merging 7.1 into 7.3 (intro + properties as one dense lesson), *not* cutting 7.6.
- **`A2.EI.2c` (quadratic inequalities in one variable) is uncovered** — cited by no lesson, and
  Unit 2 is marked complete. Unlike `A2.ST.1` and `A2.ST.3`, which are *knowingly* out of scope per
  the decisions above, this clause was never declared out. Needs a home. See §8.

---

## 7. Conventions

- **Directory:** `unitXX/lessonYY/` with the standard component subfolders
  (`warmup`, `notes`/`slides`, `activity`, `exit_ticket`, `homework`, `cover`,
  plus each `*_key`). Unit-level: `unit_cover`, `sample_test`, `sample_test_key`.
- **Lesson 0 numbering:** the characteristics lesson is `lesson00` in each unit
  (or `X.0` in titles) so content lessons keep 1-based numbers.
- **Build:** `make -C unitXX/lessonYY all` (five work products); `make -C unitXX student key`;
  root `make all` / `make student` / `make key`. **`full` no longer exists** — see
  "The five work products" below.
- **Component naming (2026-08-20):** the EFFL centrepiece is **labelled *Experience & Formalize***
  everywhere a student or teacher reads it — the cover's packet table, the component's
  `\pageheader`, the deck's activity frame, the lesson plan's activity box, and its teacher note.
  In LaTeX: `Experience \& Formalize`. **Its directory stays `experience/`** (with
  `experience_key/`) — that name is a build identifier in `shared/lesson.mk`'s
  `STUDENT_ORDER`/`KEYED_PAIRS`, so renaming the directory would mean editing the build system.
  **Directory `experience`, label *Experience & Formalize*.**
- **Authoring:** use the `lesson-planning` skill.
- **Retrofitting:** the conventions below land *after* lessons are written, so an existing lesson
  can be behind on one. Bring it forward by name — the skill has a Retrofit section listing every
  convention with its fix and script:
  `/lesson-planning apply boxguard namestrip retrofit to 1.1 and 1.3`
  (naming none applies all). Retrofittable names: **boxguard**, **namestrip**, **vocabpar**,
  **work rule**, **teachernotes**.

### Vocab-box paragraph breaks — required from Unit 4 onward

`\termblanklong` (blank) and the key-local `\vocabans` (key) both **open with `\noindent`, which is a
no-op in the middle of a paragraph**, and `\ansline` ends with `\dotfill` but never ends the
paragraph. Left alone, this produces two visible defects in the `vocabbox`:

1. **In the blank:** the intro sentence ("Fill in each term as we build it together.") and the *first*
   term label run together on one line.
2. **In the key:** every term label after the first is pulled onto the end of the *previous* answer's
   dotted line — badly garbled, worse than the blank.

**Do this in every notes/notes_key from Unit 4 on** (Lesson 4.0 is the reference implementation):

```latex
% notes/main.tex — force a paragraph break before the first term
Fill in each term as we build it together.
\par\vspace{2pt}
\termblanklong{First term}

% notes_key/main.tex — define \vocabans with \par on BOTH ends
\newcommand{\vocabans}[2]{%
  \par\noindent\textbf{\textcolor{forest}{#1:}}\\[1pt]\ansline{#2}\par}
```

Fixing it per-lesson (rather than patching `\termblanklong` in
`shared/algebra2-article.sty`) is deliberate: a shared-package change would re-flow the notes of every
already-verified unit at once. The shared fix is the right long-term answer, but it belongs with the
retrofit below, where the pagination of Units 1–3 can be re-verified in one pass.

**The defect is present throughout Unit 1, confirmed 2026-07-29.** The four-convention sweep of
Lessons 1.0–1.5 found the garbled `vocabbox` in the `notes_key` of every lesson inspected; on **1.2**
it reaches past the vocab box into `homework_key` items 7 and extension (b), so the collision is
not confined to `vocabbox` — anywhere an `\ansline` is followed by a `\noindent`-opening macro is
exposed. Each affected key already defines a local `\vocabans`, but without the `\par` on both ends.

**vocabpar changes box heights, so boxguard must be re-run after it.** On 1.3 the taller vocab
boxes flipped a guard verdict that the first pass had recorded as impossible — see the boxguard
section's "Re-run boxguard" note. Sequence vocabpar **before** boxguard.

**Lesson 1.3 fixed 2026-07-29** (the first Unit 1 lesson to get it), by hand, per the 4.0 pattern:
`\par\vspace{2pt}` before the first term in `notes/main.tex`, and `\par` on both ends of
`\vocabans` plus the same `\par\vspace{2pt}` in `notes_key/main.tex`. **It was free** — notes stayed
3/3 and the packet stayed 14pp, so the fear that this re-flows pagination did not materialize here.
Both sides verified by rendering page 1: the blank's intro sentence and first term are on separate
lines, and the key's five term labels each sit above their own dotted answer line.

That 1.3 came out free is evidence the Units 1–3 sweep may be cheaper than assumed, but it is one
data point on a 3pp notes file — **1.5's notes are 4pp and the rest of Unit 1 is unfixed.** Lessons
1.0, 1.1, 1.2, 1.4 and 1.5 still carry the defect.

### Boxguard — the page-break rule (named 2026-07-28)

**"Boxguard" names both the defect and the fix.** When a review turns up "lesson 1.3 has a
boxguard problem on page 4," it means a box broke across a page leaving roughly an inch — a
title plus a line or two — at the **top or bottom** of a page. **Push the whole box to the next
page.** Breaking a box is fine only when each side of the break gets a substantial chunk. The
white space you give up is cheaper than a stub that reads as a printing mistake.

`\boxguard` is defined in **`shared/algebra2-boxes.sty`** (and so reaches every key through
`algebra2-key.sty`) — no per-file preamble needed:

```latex
\boxguard                      % default: needs 16 lines of room, else break
\begin{notesbox}{2. ...}

\boxguard[30]                  % box OPENS with an unbreakable \fbox / tabularx
\begin{notesbox}{3. ...}

\boxguard[14]                  % inside a box: keep a lead-in with its table
\textbf{Now justify a solution, line by line.}
```

Prefer `\boxguard` to a hard `\newpage` — it self-adjusts when content above it changes.
Reserve `\newpage` for an explicit "this box must start a page" instruction (Lesson 1.0's Hook
is the one such case). Apply every guard to the blank **and** its `_key`, then rebuild and check
the pages with `pdftoppm -r 60 -png <pdf> /tmp/pg`; page counts should not move.

Unlike the vocab-box fix above, this one **is** a shared-package change — it is purely additive
(`\RequirePackage{needspace}` + one `\newcommand`), so no already-verified unit re-flows until
a lesson actually calls `\boxguard`. Per user decision there is **no bulk sweep**: fix boxguard
problems lesson-by-lesson as they are found in review.

**Applied so far:** Lesson 1.0 (reference), **Lessons 1.1 and 1.3 (2026-07-28)**, **all of Unit 1
— Lessons 1.0–1.5 (2026-07-29)**, **all of Unit 2 — Lessons 2.0–2.7 (2026-07-30, 12 sites / 24 lines,
every one free; one declined on 2.6 notes — see the Unit 2 status)**, 10 guard sites (each applied to a blank and its key, 20 lines),
plus **1.1 notes Section 2 (2026-07-29)** — the stub the earlier pass had declined; see limit 2.

**Boxguard is opt-in and nothing detects a missed one.** `\boxguard` only acts where an author
typed it: across the authored lessons today, **48 of 838** breakable boxes carry a guard. A box
that strands a stub is not a compile error and `make` still exits 0, so violations surface only
when someone looks at the PDF. That is why 1.1's Section 2 stub survived a retrofit that had
already touched the same file — it was seen, priced at a page, and declined (limit 2).

**What the Unit 1 sweep confirmed.** Every guard that landed was *free* — no packet grew. The
useful new observation is that a guard can be needed on **only one side**: on 1.3 the first two
guards fire in the key and are no-ops in the blank, and on 1.4 the
guard exists purely because namestrip had let the key's Guided Practice box squeeze onto a page the
blank still pushed, opening a 3/2 mismatch. **Boxguard is therefore the right last step** — it
repairs pagination the three earlier conventions disturb. Both documented limits held up
repeatedly: guards inside breakable `tcolorbox`es were correctly skipped as inert (1.0 homework,
1.2 activity/homework, 1.4 homework), and several guards were declined because firing them cost a
page and with it the blank/key match (1.1 activity Tier A — measured at 2 padding pages).

**Re-run boxguard after any change that alters box heights — vocabpar in particular (2026-07-29).**
1.3's notes were re-guarded after its vocabpar fix and the earlier conclusion **reversed**. The
first pass had found that guarding notes box 1 "clears that stub only by stranding box 3's tail,
and guarding box 3 in turn overflows to 4pp," so it left the stub. vocabpar changed the arithmetic:
`\termblanklong`/`\vocabans` now break properly, making **both** vocab boxes taller, and with the
new heights `\boxguard[18]` on box 1 **and** `\boxguard[20]` on box 3 both fit — 4 guard sites on
1.3, still **3/3, packet still 14pp**. The blank went from one stub to **zero broken boxes**, and
because the taller key vocab box now also pushes box 1 off page 1, **the key paginates identically
to the blank**: p1 objective/vocab/hook, p2 boxes 1–2, p3 boxes 3–4 + Guided Practice.

Two things to carry forward: a "guard costs a page" verdict is only valid for the box heights it
was measured against, so **re-measure rather than trusting a prior refusal**; and vocabpar and
boxguard interact, so **vocabpar belongs before boxguard** in the retrofit order, alongside
namestrip.

Unit 1 totals after the re-run: **12 guard sites, 24 lines** — 1.0 ×2, 1.1 ×2, 1.2 ×2, **1.3 ×4**,
1.4 ×1, 1.5 ×1.

**Two limits found on 1.1 / 1.3 (2026-07-28) — read these before guarding a lesson:**

1. **`\boxguard` is inert inside a breakable `tcolorbox`.** On 1.3's notes, Section 3 ends with a
   two-line tail stranded at the top of page 5. A guard placed *inside* the box (in vertical mode,
   before the closing paragraph) does nothing — tested at `[11]` and `[30]`, neither fired, because
   `\needspace` measures the outer page while tcolorbox splits its own assembled vbox afterwards.
   The box is also ~8in tall, so it cannot be pushed whole (that would leave ~7.5in blank on page 4).
   **1.3's Section 3 tail is therefore left as-is** — it needs a content fix (split the box in two,
   or trim two lines), not a guard. Ignore the "inside a box" example in the skill's convention
   table until that claim is re-verified. **Remedy found 2026-07-29 (1.2 activity, Tier R):** when
   the goal is simply *start this part on the next page*, use tcolorbox's own **`\tcbbreak`** on its
   own line at the split point. It is defined only inside a `breakable` box, splits the box's vbox
   where you ask rather than measuring the outer page, and so does exactly what `\needspace` cannot.
   It is an *unconditional* break, so mirror it in the blank and the key and re-check both page
   counts; it does not replace `\boxguard` for the conditional case.
2. **A guard that costs a page also costs the blank/key match — but the page can be bought back.**
   1.1's notes Section 2 opened with a title+one-line stub at the foot of page 2. Guarding it
   (`\boxguard[30]`, blank + key) pushes the blank to 5pp while the key stays at 4 — a mismatch plus
   2 pages of packet padding, and guard values are binary here (any value that fires causes the
   overflow). The 2026-07-28 pass therefore left the stub. **Resolved 2026-07-29 by paying for the
   guard instead of declining it:** the blank overflowed by only ~4 lines, so mirrored spacing trims
   in Sections 2–4 recovered them — `\arraystretch` 1.7→1.5 on the Section 3 divide and Section 4
   radicals tables, 1.6→1.5 on the Section 2 "Apply them", Section 3 factoring, and Section 4
   rational-exponent tables, `\\[10pt]`→`\\[8pt]`, and Guided Practice `itemsep` 4pt→3pt. Notes are
   **4/4** again and the packets stay **18pp**, with Section 2 now opening page 3 whole and Section 3
   breaking with a substantial chunk on each side. Generalize: before declining a guard, measure the
   overflow — a few lines of table stretch is usually cheaper than the stub.

   Where a guard is free it is applied: 1.1's Hook (blank) and Section 4 (key) are both guarded.

### Namestrip — the name/date/period rule (named 2026-07-28)

**"Namestrip" names both the defect and the fix.** When a review turns up "lesson 2.2 needs a
namestrip," it means the name/date/period row is repeating on components that sit *behind* the
cover sheet. **The row belongs on the cover and nowhere else in the lesson.** The student writes
their name once; every other component is stapled behind it, so a second row is redundant and
costs vertical space at the top of every page — space that matters most on the warm-up and exit
ticket, which are held to one page.

Strip `\namedateperiod` from `warmup`, `notes`, `exit_ticket`, `homework` and
`\namepartnerperiod` from `activity` — **and from all five `_key` files**, which stay in
lockstep. Two exemptions:

- **`cover/`** — the one place the row belongs. Never strip it.
- **`unitXX/tests/` and `test_keys/`** — the actual test is taken in a testing setting, not
  stapled behind a lesson cover, so the tests keep their name row.

Apply it with the skill script rather than by hand — it skips `cover/`, hits blanks and keys
together, and is idempotent:

```bash
python3 .claude/skills/lesson-planning/scripts/namestrip.py --project . --unit 02 --lesson 03
python3 .claude/skills/lesson-planning/scripts/namestrip.py --project . --unit 02 --lesson 03 --check
```

`--check` reports without writing and exits 1 if it finds anything, so it also works as a review
gate. Rebuild afterward and confirm the warm-up and exit ticket are **still 1 page** blank *and*
key.

**Going forward this is automatic:** `new_lesson.py` and the `worksheet.tex` /
`worksheet_key.tex` skeletons no longer emit a name row (they carry a `% NAMESTRIP:` comment
explaining why), so newly scaffolded lessons are born correct. Like boxguard, there is **no bulk
sweep** of already-authored lessons: Units 2–7 still carry the row on ~450 component files, and
stripping them all at once would re-flow the pagination of every verified lesson. **Namestrip
lesson-by-lesson as reported.** Lesson 1.0 is the reference implementation.

**Applied so far:** the (since-deleted) Algebra 1 review unit, then **all of Unit 1 — Lessons
1.0–1.5 (2026-07-29)**, 10 rows each (60 total), blanks and keys together, covers untouched.
Units 2–7 still carry the row.

**Namestrip is not always free — sequence it before boxguard.** On 1.4 it reclaimed enough vertical
space that the *key*'s Guided Practice box fit on a page the blank still pushed, opening a 3/2
mismatch that a `\boxguard` then closed. Run it before the guard pass, never after.

### Packet pagination — one document, numbered as one document (2026-07-28)

Every component compiles as its own document, so each one numbers its pages from 1. Merged, a
student packet used to read `1 / 1 / 1 2 3 4 5 / 1 2 3 / 1 / 1 2 3` — the student cannot say
"turn to page 9." **The student packet is one document: numbered end to end, and imposed so that
every component starts on a right-hand page.**

Unlike boxguard and namestrip, this is **not a per-lesson fix and needs no sweep.** It lives in
the build: after `pdfunite` merges the student packet, `shared/lesson.mk` runs a pagination pass
(`shared/paginate.tex`) that

1. re-places every page at its original size and stamps the packet-wide number in the article
   class's own footer position, and
2. **inserts a blank verso after any component with an odd page count**, so each component opens
   on an odd page — the student turns to a new component, not into the middle of one.

Every lesson gets both on its next `make … student`; no `.tex` file changes.

**Student packets are duplex documents** (user decision, 2026-07-28) — that is what the
imposition is for, and single-sided the inserted blanks would just be wasted sheets. Duplex
absorbs them almost for free: Lesson 1.0 went 14pp → 20pp, but only 7 sheets → 10. The last
component is padded too, so a lesson packet always has an **even** page count.

**Inserted blanks are numbered** (user decision, 2026-07-28) — the blank verso is a real page of
the packet, so it carries its folio like any other and a student flipping through sees an
unbroken run. Lesson 1.0's blanks read 2, 4, 10, 14, 16, 20.

Two deliberate limits:

- **Blank components keep printing their own number**; the pass covers it with a white band
  inside the 0.75in bottom margin (well clear of body content) and prints the packet number in
  its place. The masked digit survives in the invisible text layer — harmless in print, but it
  is why `pdftotext` shows two numbers per page. Suppressing it at the source would mean
  compiling every student component a second time.
- **`full` packets are not paginated or imposed.** They interleave letter-size documents with
  16:9 Beamer slides (`453.54 × 255.12pt`), and a single letter-paper stamping pass would
  misplace the number on the slide pages. Teacher packets keep per-component numbering.
- **Unit- and course-level packets are out of scope** (user decision, 2026-07-28: "just the
  lesson packets"). They inherit even, recto-correct lesson packets, but `unit.mk` neither
  numbers them nor pads its own bookends — `unit_cover` is 1pp, so in `unit01_student.pdf` the
  first lesson opens on a verso. **The lesson packet is the thing that gets handed to students;**
  if unit-level printing ever matters, run the same pass over the unit merge.

If the geometry in `shared/algebra2-article.sty` ever changes, re-measure the footer baseline and
update `\PgBaseline` in `shared/paginate.tex`:

```bash
pdftotext -f 3 -l 3 -bbox target/compiled/unit01/lesson00_student.pdf /tmp/p.html && tail -3 /tmp/p.html
```

### The `key` packet — the student packet, answered, page for page (2026-07-28)

> Superseded in part on 2026-07-28 by "The five work products" below: `full` is gone. Everything
> here about how `key` is built and paginated still holds.

What was missing was a packet to teach **from** — the thing the students are holding, with the
answers filled in. That is **`key`**:

```bash
make -C unitXX/lessonYY key    # → target/compiled/unitXX/lessonYY_key.pdf
make -C unitXX key             # → target/compiled/unitXX_key.pdf
make key                       # → target/compiled/curriculum_key.pdf
```

It is `student` with each blank component swapped for its `_key` — same cover, same components,
same order, no lesson plan, no slides.

**The two packets are paginated in lockstep** (user requirement: "if I say page 7, their page 7
needs to be my page 7"). The `paginate` define in `shared/lesson.mk` now takes the counterpart
packet's PDF list as a third argument and gives each component the *same slot* in both packets:

> slot = `max(blank pages, key pages)` rounded up to even; the shorter side is padded with blank
> versos to fill it.

Recto starts and end-to-end numbering fall out of the same rule, so nothing about the student
packet's existing behavior changed except that a long key can now cost it padding pages — **keep
keys tight.** Both targets compute the slots from the same two lists, so `make student` and
`make key` agree whether run together or separately; the price is that `make student` compiles
the `_key` components too.

Verified on Unit 1 Lesson 1.3, the case where the key runs long (notes 6→7pp, activity 3→4pp):
both packets are 22pp with components opening on 1, 3, 5, 13, 17, 19. Check any lesson with:

```bash
pdfinfo target/compiled/unit01/lesson03_student.pdf | grep Pages && pdfinfo target/compiled/unit01/lesson03_key.pdf | grep Pages
```

Unit-level `key` mirrors unit-level `student` piece for piece (unit cover, the equal-length lesson
packets, then `sample_test_key` in place of `sample_test`). Only that trailing pair can differ in
length, and it sits at the end.

### The work rule — a component is the same length blank and keyed (2026-07-28)

The blank-slot problem, attacked at the source instead of the packet. Padding has two causes:
**parity** (an odd-length component) and **blank/key mismatch** (the key needs room the blank did
not give). The mismatch was self-inflicted: blanks left a one-line `\blank{8.0cm}` where a
four-step solve belongs, and keys crammed the solve back in as
`\ans{$3x-6=x-6 \Rightarrow 2x=0 \Rightarrow x=0$}`. Neither side was honest about the space.

**The rule (user decision, 2026-07-28):** every worked solution lives in a `\begin{work}` block
that is **byte-identical in the blank and the key**. Under `algebra2-boxes` the blank builds the
box and ships a `\vphantom` of it — exact height, nothing on the page, nothing in the PDF text
layer. Under `algebra2-key` the same box prints in `keyred`. Same code path, same metrics, so the
two cannot drift.

Format, as specified: **one statement per line**; the `&` immediately before the relation so the
whole block aligns on it; when *simplifying*, row 1 is the original expression, the relation, and
the first simplification, and each later row starts at the `&=`; when *solving*, one row per step,
every row aligned on its relation (`=`, `<`, `>`, `\le`, `\ge`), reversals included.

```latex
\begin{work}
  x &= \frac{4\pm\sqrt{(-4)^2-4(1)(-7)}}{2(1)} \\
    &= \frac{4\pm\sqrt{16+28}}{2} \\
    &= \frac{4\pm\sqrt{44}}{2}    \\
    &= 2\pm\sqrt{11}
\end{work}
```

Scope: multi-step work only. A table cell holding one final answer is already the same size on
both sides — leave those as `\blank{}`/`\ans{}`. `work` does not go inside a table cell; if a table
asks for real work, pull those items out of the table (that is what the Lesson 1.2 Hook needed).
`\workrowsep` (default `0pt`, i.e. typeset spacing exactly as specified) adds leading between rows
and moves both sides together, so raising it for handwriting room cannot break the match.

**Pilot: Lesson 1.2**, converted end to end (Hook, quadratic-formula chain, guided practice,
Tier A Part 1, homework items 6 and 8, the whole exit ticket).

| component | before (blank/key) | after | pads before → after |
|---|---|---|---|
| notes | 5 / 5 | 6 / 6 | 1 → 0 |
| activity | 3 / 3 | 4 / 4 | 1 → 0 |
| homework | 3 / 3 | 4 / 4 | 1 → 0 |
| exit ticket | 1 / 1 | 1 / 2 | 1 → 1 |

The packet is **still 20pp** and its blank pages went **6 → 3**: the components absorbed exactly
the pages that used to be padding, and the room landed where students actually work. The three
that remain are the 1pp cover, the 1pp warm-up (both structural parity), and the exit ticket.

**`\ansline` prose drifts the same way**, without a shared body to measure. Homework item 8 came
out 3 / 4 until the blank's `\writelines{3}` was raised to `\writelines{5}` to match the key's
wrapped answer. Applied by hand; noted in `references/conventions.md`.

#### Extended to the unit tests — no current in-tree example (2026-07-31; reference deleted 2026-08-20)

The rule was written for lesson components, but unit tests have the same blank-against-key problem:
`sample_test` merges into the unit **student** packet and `sample_test_key` into the unit **key**
packet, so a key that runs long desyncs the two packets from that point on. The reference
implementation was the old Algebra 1 review unit's tests (21 `work` blocks per form,
byte-identical in blank and key, `\workrowsep` at `10pt`), which were deleted with that unit —
the spec below still stands, and the next unit tests authored or retrofitted should follow it.

Two test-specific wrinkles the lesson-component rule does not cover:

- **A test has no lesson plan**, so there is nowhere outside the key to put teacher prose. Resolved
  by which pair is packet-merged: the **practice** pair carries **no** `teachernote` at all, and
  the whole scoring guide goes in `actual_test_key` behind a `\newpage`. The actual test and its
  key are never merged into any packet, so those pages are free.
- **Part D needs sub-question structure** — one `\vspace{5.6cm}` under six lettered prompts cannot
  be matched to a key answer. Break it out per sub-question: `work` blocks for the computational
  parts, `\writelines{n}` against n `\ansline`s for the prose.

**Units 1–5 tests are still on the old `\vspace{}`-vs-`\ans{}` idiom** and have not been
retrofitted. Unit 1's is the one with a live defect: `practice_test` 3pp against
`practice_test_key` 4pp, which costs the Unit 1 student packet a blank page.

### Teacher notes move to the lesson plan (2026-07-28)

Once the work rule was in, `teachernote` was the last thing making a key longer than its blank —
the one block with no counterpart on the student side. Lesson 1.2's exit ticket was 1pp blank /
2pp keyed purely because of it, even after the note was cut roughly in half.

**Decision (user, 2026-07-28): teacher prose lives in the lesson plan, one note per component, in
packet order, titled for it.**

```latex
\begin{teachernote}[Warm-Up]  ... \end{teachernote}   % → "Teacher Note: Warm-Up"
% then [Guided Notes], [Group Activity], [Exit Ticket], [Homework]
```

The plan is teacher-facing already and sits outside the page-matched packet, so nothing is lost and
the keys shed their one asymmetry. `teachernote` therefore **moved from `algebra2-key` to
`algebra2-boxes`** (the lesson plan loads `-boxes`, not `-key`), and its title argument is
**optional** — a bare `\begin{teachernote}` still renders plain "Teacher Note", so the 46
un-migrated lessons keep compiling untouched. Verified against `unit01/lesson00/notes_key`.

Migrate a lesson with `scripts/movenotes.py` (see §7 conventions in the skill):

```bash
python3 .claude/skills/lesson-planning/scripts/movenotes.py unit01/lesson02
```

**Result on Lesson 1.2 — every component now matches its key exactly:**

| component | blank / key | pads |
|---|---|---|
| cover | 1 / 1 | 1 (parity) |
| warm-up | 1 / 1 | 1 (parity) |
| guided notes | 6 / 6 | 0 |
| group activity | 4 / 4 | 0 |
| exit ticket | 1 / 1 | 1 (parity) |
| homework | 4 / 4 | 0 |

20pp packet, **3 blank pages, zero of them caused by a key**. The three that remain are the three
1pp components, which are structural. The lesson plan grew to 6pp, which costs nothing — `full` is
not paginated and the plan never reaches students.

**Still to do:** the other 29 lessons (Units 3–7) keep their notes in the keys. `movenotes.py`
handles them one at a time; Lessons 1.2 and 1.0 are the reference implementations.

**All of Unit 1 migrated 2026-07-29** — 5 notes per lesson, 30 total; no `teachernote` remains in
any Unit 1 lesson key. Each plan grew 3pp → 4pp, which costs nothing. It was again the single
highest-yield step: it closed the blank/key mismatch outright on **1.0** (activity 3→2) and **1.3**
(activity 3→2), matching the 1.3 result. **But it cuts both ways** — on **1.2** it *opened* a
mismatch (`notes_key` 3→2), because that key had been running long purely on its teacher note; the
work-rule pass then put it back to 3/3. Expect either direction, and always re-measure after it.

**Lessons 1.1 and 1.3 migrated 2026-07-28** (5 notes each). On **1.3 this was the whole fix for the
notes**: 6/7 → **6/6**, and the packet dropped **22pp → 20pp** without touching a single item of
content. Worth knowing before reaching for the work rule — on a lesson whose only asymmetry is the
teacher note, `movenotes.py` alone closes it.

### `steptable` — the alignment rule for *printed* solutions (2026-07-28)

Lesson 1.0 was converted second and turned out to need the other half of the rule. It has **no
solve-from-scratch tasks**: every chain is printed and the student names the property beside each
line, so `work` (which hides its body in the blank) applies almost nowhere. What does apply is
"one statement per line, all lines aligned on the sign" — and the existing one-column tables did
not align, because `$3x-12=18$` above `$3x-12+12=18+12$` puts the two `=` in different places.

`steptable` splits the step into a right-aligned left side and a left-aligned relation + right
side, so every relation lands in one column:

```latex
\begin{steptable}
  \step{3(x-4)}{=18}{Given}
  \step{3x-12}{=18}{\blank{6.0cm}}
  \step{3x-12+12}{=18+12}{\blank{6.0cm}}
\end{steptable}
```

`\steprel` is the variant for the row where the *relation itself* is the blank — the flip
demonstration, where the symbol turning around is the whole point. Only column 3 differs between
blank and key, so nothing can drift.

Two implementation notes worth keeping: the environment captures its body with `+b` rather than
splitting `\begin{tabularx}`/`\end{tabularx}` across begin/end code (tabularx rescans its body to
solve the X column, and the split form fails with "Missing } inserted"); and it is a **chain**
rule — a table of independent statements to classify, like Lesson 1.0's exit ticket item 2 whose
rows carry two relations each, stays a plain table.

**Lesson 1.0 result:** 6 step tables converted (notes ×3, activity ×2, homework ×1), a `work`
block added to the one item where students actually solve (exit ticket MC, $-5x\ge20$), and its
five teacher notes moved to the plan. All five components match their keys — **but its packet is
still 20pp with 6 pads, unchanged.** Blank and key already matched here, and nothing grew enough
to flip a component from odd to even, so every pad is parity. That is the honest boundary of this
work: the rule fixes *mismatch* and improves how a solution reads; it does not touch parity, and
1.0 had no mismatch to fix. Lesson 1.2 gained because its new work blocks pushed three components
from odd to even.

Lesson 1.2 had no blank/key mismatch to begin with, so its gain came from the components growing
into their padding. The lessons where the rule directly removes a mismatch are the ones already
flagged — Unit 1 Lesson 1.3 (notes 6/7, activity 3/4), Unit 5 Lessons 5.3 and 5.4.

**Lesson 1.3 cleared 2026-07-28.** Both flagged mismatches are gone, but only one of them was the
work rule's doing: the notes (6/7) were fixed by **teachernotes** alone, and the activity (3/4) by
the **`\ansline` half** of the rule — seven prose answers whose blanks reserved one write-line for
answers that wrap to three, four, even five. Raising each `\writelines{n}` to the key's true
wrapped length took the blank to 4pp, matching the key. **Every component of 1.3 now matches**
(1/1, 6/6, 4/4, 1/1, 4/4), packet 20pp.

**Lesson 1.1 converted 2026-07-28**, blank and key byte-identical in both: the **exit ticket**'s
evaluate item (the key had crammed `2(-3)^2-5(-3)+|{-3}-8| = 2(9)+15+|{-11}| = 18+15+11` onto one
line, and blank/key were faking a match with mismatched `\vspace` values — 4pt/8pt against 2pt),
and the **notes** guided-practice evaluate item. Both now reserve three aligned rows where the
student actually works. Every component still matches (1/1, 4/4, 3/3, 1/1, 3/3), packet still 18pp,
and the exit ticket held its one-page constraint.

**Scope note:** 1.1's Tier A items and 1.3's "write the equation" tables were deliberately left
as `\blank{}`/`\ans{}` — they hold single final answers, and 1.3's are table cells, which the rule
excludes. 1.3's exit ticket item 2(d) is a genuine multi-step solve left alone on purpose: it is
already structured as equation-then-answer, it matches its key, and a `work` block risks the
one-page constraint.

**All of Unit 1 converted 2026-07-29 — 82 `work` blocks**, every one byte-identical between its
blank and its key (verified by diffing the extracted blocks). Per lesson: 1.0 ×1, 1.1 ×10, 1.2 ×16,
1.3 ×5, 1.4 ×2, 1.5 ×7. The spread is the point: **1.2 needed 16 and 1.0 needed 1**, because 1.0 is
a read-features-off-a-graph lesson (structurally like 1.0) where nearly every answer is a single
value, while 1.2 (absolute-value equations & inequalities) is almost entirely multi-step solving.
Do not expect a uniform yield per lesson — count the multi-step items first.

The two drift patterns the rule exists to catch both showed up repeatedly, and are worth naming so
they are recognized on sight:

1. **The blank reserved nothing.** 2.1's exit ticket item 2 had a bare `\vspace{1.4cm}` where the
   key carried a full multi-step chain; 1.2's exit ticket item 2 had the chain **printed in the key
   and entirely absent from the blank**. Students had no room for work the key showed.
2. **The key crammed the chain onto one line** — `\ans{$C(3)=\$30$; $C(8)=30+10(3)=\$60$}` (1.4),
   `\ans{$\dfrac{7-1}{3-1}=3$}` (1.1), `\ans{$d(0)=80(4)=320$ m; $d(7)=80(3)=240$ m.}` (1.3).

**`\writelines{n}` consumes n+1 line slots** — it ends in `\\`, so `\writelines{3}` occupies four.
Found on 1.3, where raising activity Tier E 3 from `{2}` to `{3}` overflowed the blank to 3pp; it
was returned to `{2}`. Measure the key's true wrapped length, then set `n` to that, and re-measure
the blank rather than assuming the raise is free. 23 `\writelines{n}` adjustments were made across
Unit 1 (1.0 ×5, 1.1 ×4, 1.3 ×4, 1.4 ×6, plus 1.2 ×0 and 1.5's set) — on **1.2 the count was zero**,
because both of its prose-drift spots turned out to be multi-step solves that a `work` block fixed
instead. Reach for `work` first; `\writelines` is only for genuine prose.

No `steptable` conversions were needed anywhere in Unit 1 — none of the six lessons has a "justify
each line" printed-solution chain. The environment's only user was the old Algebra 1 review unit
(deleted 2026-08-20), so it currently has **no in-tree example**; the spec above is the reference.

### The five work products — `full` removed, PPTX added (2026-07-28)

A lesson now builds **exactly five files** into `target/compiled/unitXX/`, and nothing else:

| File | What it is |
| --- | --- |
| `lessonYY_plan.pdf` | the lesson plan — the lesson-root `main.tex` |
| `lessonYY_slides.pdf` | the deck from `slides/main.tex`, **printed** — 3 slides/page, notes column |
| `lessonYY_slides.pptx` | that deck for PowerPoint, **full-page**, one page image per slide |
| `lessonYY_student.pdf` | cover + blank components, paginated packet-wide |
| `lessonYY_key.pdf` | that packet answered, page for page |

```bash
make -C unitXX/lessonYY all                 # all five
make -C unitXX/lessonYY plan|slides|pptx|student|key
```

**`full` is gone at every level** — lesson, unit, and root. `make full` now errors. The plan and
the deck were the only reason it existed; they are standalone deliverables now, so nothing bundles
a lesson plan behind a cover with the answer keys. `make clean` still sweeps stale `_full.pdf`
files out of `target/`.

**Units aggregate only the two packets** (`unitXX_{student,key}.pdf`, and the curriculum pair at
the root). The plan, the slide PDF, and the PPTX stay per-lesson — they are teacher artifacts, not
something to hand out as one bound document.

**Every lesson owes a deck.** `slides` feeds two of the five products, so it is a default
component in `new_lesson.py`, not an optional one. All 48 existing lessons already had one.

> **The slides PDF became a 3-up printable on 2026-07-29** (user request, with a mockup). The two
> slide products are now the deck's two forms — **the PDF is what you print, the PPTX is what you
> project** — both generated from the one compiled deck at
> `target/unitXX/lessonYY/slides/main.pdf`, which stays the source of truth. Nothing per-lesson
> changed: no `.tex` edits, no rescaffolding, all 50 existing decks work untouched.
>
> `shared/handout.tex` (new) does the re-framing: three slides per letter page, thumbnails down
> the left column at `\slidewidth` = 4.35in, and beside each a "Notes" label over 6 ruled lines.
> Slides are placed with `\includegraphics[page=n]`, so TikZ and math render exactly as projected.
> Two details worth keeping: the deck's page count is passed in as `\DeckPages` because LaTeX
> cannot count the pages of an external PDF (`pdfinfo` already is a build dependency), and the note
> column is a fixed-height `minipage` measured from the slide beside it with `s` inner alignment,
> so `\vfill` distributes the rules and both columns end on the same line at any aspect ratio.
> Tuning knobs are the three lengths at the top of the file. A deck whose slide count is not a
> multiple of 3 leaves the last page short, top-aligned rather than stretched.
>
> In `shared/lesson.mk` the `_slides.pdf` rule calls the new `handout` define instead of `cp`, and
> **the `_slides.pptx` rule was re-pointed at the raw deck** rather than at `_slides.pdf` — a
> PowerPoint of 3-up handout pages would be useless to project. Verified on Unit 1: decks of 7, 7,
> 8, and 9 slides → handouts of 3, 3, 3, 3 pages (9 gives exactly 3 with no trailing blank), PPTX
> still 13.333 × 7.5in, `make all` exit 0 on all four.
>
> **The handout caught one real overflow the 2026-07-28 sweep missed.**
> `unit01/lesson03/slides/main.tex` slide 4 ("Six questions, asked of one line") ran its last line
> — "the situation wins." — to `yMax` 256.94pt on a 255.12pt page: **1.8pt off the bottom, genuinely
> clipped**, and XeLaTeX reported no `Overfull \vbox` for it. Fixed in the right column with no loss
> of content: `\arraystretch` 1.25 → 1.12 across the six characteristic rows, the `\vspace{2pt}`
> after the tabular dropped, and the block's `\\[3pt]` → `\\[2pt]`. Now `yMax` 243.59 — an 11.5pt
> bottom margin, in family with slides 3, 6, and 7 (11–13pt). `make -C unit01/lesson03 all` exit 0,
> deck still 9 slides → handout 3 pages, student/key still 20/20.
>
> **Measure clipping this way, not by eye or by log** — beamer will happily ship an over-tall frame
> without warning:
> ```bash
> pdftotext -f <p> -l <p> -bbox <deck>.pdf /tmp/p.html
> grep -o 'yMax="[0-9.]*"' /tmp/p.html | sort -t'"' -k2 -g | tail -1   # vs page height 255.12pt
> ```
> Swept every built deck this way (the deleted review unit plus Units 1, 5, and 7): **no other
> frame clips.** The tightest survivors named at the time all belonged to the deleted review
> unit, so no near-the-edge frames are currently on record — re-measure when a deck changes. The
> `unit01/lesson01/slides/main.tex:95` site this plan flagged as unchecked is **fine**: that deck's
> worst margin is 12.72pt.

**The PPTX is a wrapper, not a port.** `shared/pdf2pptx.py` rasterizes each page with `pdftoppm`
at 300 dpi and writes the OOXML package by hand with `zipfile` — no LibreOffice, no `python-pptx`,
nothing beyond the poppler tools the build already needs. The canvas is scaled aspect-preserving to
PowerPoint's standard 7.5in height, so a 16:9 deck lands on exactly 13.333 × 7.5in ("Widescreen").
Slides are page images, so TikZ figures and math render exactly as in the PDF but **nothing is
editable in PowerPoint**. The `.tex` is the source of truth — edit it and rebuild; never edit the
`.pptx`. Trade sharpness for size with `make ... pptx PPTX_DPI=200`.

`plan`, `slides`, and `pptx` are real file targets and rebuild only when their source changes.
`student` and `key` stay phony — the pagination pass has to measure both packets each time.

The root `Makefile` is now a thin `include shared/root.mk`, matching the unit and lesson levels
(and matching what `new_lesson.py` already assumed when creating a missing root Makefile).

**Verified 2026-07-28:** `make all` from the root → EXIT 0 across all 8 units / 48 lessons; every
lesson emits all five products. Generated `.pptx` packages check out structurally — well-formed
XML throughout, no dangling relationships, every part content-typed, slide count matching the PDF.

### Course title — "Algebra 2", nothing else (2026-08-22)

Every place a course title renders, it reads **`Algebra 2`**. No teacher name, no school year.
The old `Algebra 2: Shepherd: 2026--2027` form is gone from the whole tree.

Where it lives, and what it is now:

| Surface | Source | Now |
| --- | --- | --- |
| Lesson plan title block | `unitXX/lessonYY/main.tex` | `{\Large\bfseries \CourseName \\` with `\newcommand{\CourseName}{Algebra 2}` |
| Packet cover banner | `.../cover/main.tex` | `{\color{white}\textbf{\LARGE Algebra 2}}` |
| Deck title slide | `.../slides/main.tex` | `Algebra 2~$\cdot$~Unit N: <Unit Title>` (literal — beamer has no `\CourseName`) |
| Unit cover sheet | `unitXX/unit_cover/main.tex` | already `Algebra 2` — unchanged |

**`\SchoolYear` no longer exists.** Its `\newcommand` was deleted from all 44 lesson plans, from
`assets/skeletons/lesson_plan.tex`, and from `old_templates/main.tex`; `new_lesson.py` no longer
emits it and its `--year` flag is gone. A plan that still references `\SchoolYear` will fail with
`Undefined control sequence` — delete the reference, do not re-add the macro.

The generated binder cover also carried the name in a script face. That whole feature was
removed the same day — see "Binder covers removed" below.

Scaffolding a new lesson: pass `--course "Algebra 2"`. There is no year to pass.
### Binder covers removed (2026-08-22)

The generated binder cover is **gone from the project**. Unit covers are designed in Claude
Design now and printed on their own, so the build no longer draws one or merges one.

Deleted: `shared/cover.py` (the SVG generator), `unit01/binder_cover/main.pdf`,
`unit02/binder_cover/{main.pdf,spec.py}`, and every binder hook in `shared/unit.mk` —
`HAS_BINDER_COVER`, `BINDER_COVER_SRC`/`_PDF`, `PYTHON`/`COVER_SCRIPT`, the `binder_cover`,
`_binder_cover`, and `clean_unit_cover` targets, and the `$(BINDER_COVER_PDF)` entry at the head
of both the `student` and `key` `pdfunite` lists.

Consequences:

- **`make -C unitXX clean_unit_cover` and `make -C unitXX binder_cover` no longer exist.** They
  error as unknown targets. Nothing replaces them.
- **The unit01 and unit02 packets are 2 pages shorter** — those were the only two units that had
  a binder cover, and it contributed the same sheet twice.
- **The project's optional dependencies are gone with it.** `cairosvg`, the native `cairo`
  library, and the five TeX OpenType fonts the generator needed at the OS level were required by
  nothing else; the README section documenting them is deleted. The build now needs only XeLaTeX,
  `latexmk`, poppler, and `python3`.
- **`unit_cover/` is unaffected** and is *not* the same thing: it is the LaTeX unit overview page
  (`unitXX/unit_cover/main.tex`), still compiled and still leading both unit packets.

Earlier §4 status entries that describe authoring a binder cover (Unit 1, Unit 2) are left as
written — they are dated records of what happened, superseded by this block.

If a designed cover should ever be bound *into* a unit packet rather than printed separately, the
cheap path is a prefab drop-in slot modeled on `sample_test/` — a directory whose `main.pdf` is
merged as-is, with no generator. That is deliberately **not** built; ask for it if it is wanted.
---

## 8. Deferred cleanup — do after Unit 7 and the finals are done

Non-blocking issues intentionally postponed so unit authoring keeps moving. **Do not start these until
Units 6–7 and the final exams are complete.**

- [ ] **Give `A2.EI.2c` (quadratic inequalities in one variable, over $\mathbb{R}$, solved
      algebraically) a home.** Cited by no lesson in the course; Unit 2 was marked complete without
      it. Options: a Unit 2 addendum lesson (2.8), a Tier E strand retrofitted into 2.2/2.5, or a
      finals-review lesson. Decide before the final exam is authored — unlike `A2.ST.1`/`A2.ST.3`,
      this clause was never declared out of scope.
- [ ] **Retrofit the vocab-box paragraph-break fix into Units 1, 2, and 3** (§7 above). Affects
      `unit0{1,2,3}/lesson*/notes/main.tex` and `notes_key/main.tex`. All three units currently show
      defect 1, and every Lesson 0 key that defines `\vocabans` (Units 1, 2, 3) shows defect 2.
      Preferred approach once nothing else is in flight: fix `\termblanklong` in
      `shared/algebra2-article.sty` to emit a leading `\par`, add the trailing `\par` to `\ansline` in
      `shared/algebra2-key.sty`, then drop the per-lesson workarounds. **Re-verify after:** every
      warm-up and exit ticket still fits exactly one page (blank *and* key), and each key still
      paginates identically to its blank —
      `pdfinfo target/unitXX/lessonYY/<comp>/main.pdf | grep Pages`.
