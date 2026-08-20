# Course Workflow — from `COURSE_PLAN.md` to lessons

The course structure comes from **`COURSE_PLAN.md`** at the project root — the scope &
sequence: the eight units, each unit's lesson list, and the cumulative
**characteristics-of-functions spine**. The mathematical **content** of a lesson is
**standards-based**, drawn from that plan plus any standards the user supplies and the
publisher reference in `spec/` (used as a topic/sequencing model, never copied verbatim —
see "Copyright" below). This file explains how to turn the plan into lessons and where each
lesson's parts come from.

## Course identity (read this first)

This is **Algebra 2: Shepherd**, a **function-family** course for a secondary-school
audience. After a foundations unit, each unit is built around one function type
(linear → quadratic → polynomial → rational → radical → exponential → logarithmic), and
**every unit opens with a Lesson 0, "Characteristics of ____ Functions."** Prize concrete
examples and graph-reading fluency; introduce each new function type by first studying how
it *behaves*, then how to manipulate and solve it.

**Out of scope for this course** (do not author lessons on these): conic sections, sequences
& series, probability & statistics, trigonometry, and linear systems / linear programming.

## The characteristics-of-functions spine (the backbone)

`COURSE_PLAN.md` §3 is the heart of the course. Each unit's **Lesson 0** re-teaches the full
"read-a-graph" toolkit built so far and **introduces the new characteristics that its function
type is the first to require**. When authoring any Lesson 0:

- Look up the unit's column in the §3 spine table. The rows marked **● introduced** are the
  teaching focus; the **○ revisited / · applied** rows are quick review applied to the new graph.
- New characteristics debut where the plan says they do — e.g. **vertex / axis of symmetry /
  end behavior** in Unit 3 (quadratics), **origin symmetry / turning points / multiplicity**
  in Unit 4 (polynomials), **asymptotes + holes + domain restrictions** in Unit 5 (rationals).
  Don't teach a characteristic before its debut unit.

## Where the content lives

- **`COURSE_PLAN.md`** (project root) — the scope & sequence, per-unit lesson lists, the
  characteristics spine (§3), and the running build **Status**. **This is the unit/lesson map.**
- **The standards the user supplies** — usually Virginia SOL codes (e.g. `AII.6`, `AII.7`) but
  possibly CCSS or a district scope-and-sequence. Take them as given; don't invent codes.
- **`spec/Algebra-2-Curriculum/`** — the All Things Algebra reference (unit PDFs, assessments,
  warm-ups). Use it as a **topic-sequencing and difficulty model only** — it is copyrighted
  (see below).

## Copyright — the `spec/` reference

The `spec/Algebra-2-Curriculum/` materials are **© Gina Wilson (All Things Algebra)**, licensed
to this teacher for classroom use and **not for redistribution**. Use them to calibrate topic
order, granularity, and difficulty — **never** copy their problems, wording, or figures into an
authored lesson. Everything you write must be original. Standard mathematical topics and a
scope-and-sequence are facts, not protected expression; the specific problems and phrasing are.

## Decomposing a unit into lessons

**Convention: one lesson per bullet in that unit's `COURSE_PLAN.md` list, in listed order**,
with the characteristics lesson as **Lesson 0** (`lesson00`). Lesson id is `<unit>.<n>` where
`n = 0` is Characteristics and content lessons count up from 1 (Lesson 2.0, 2.1, 2.2, …).
Always **present the proposed lesson map for the unit and confirm it with the user before
authoring** — lessons occasionally merge or split.

Worked example — **Unit 2 (Linear Functions)** from `COURSE_PLAN.md`:

| Lesson | Topic | Notes |
| --- | --- | --- |
| 2.0 | Characteristics of linear functions | domain/range, intercepts, slope, incr/decr, +/− intervals |
| 2.1 | Linear functions | slope, forms of a line, writing equations, graphing & transformations |
| 2.2 | Absolute value equations & inequalities | solving algebraically |
| 2.3 | Absolute value functions & transformations | previews vertex / axis of symmetry / min-max |
| 2.4 | Piecewise-defined functions | absolute value entry → greatest-integer / step functions |
| 2.5 | Linear regression | scatter plots, correlation, lines of best fit |

Do the same for the other units from `COURSE_PLAN.md`.

## Mapping content into a lesson

| Lesson element | Source |
| --- | --- |
| Lesson title (`\LessonNumberName`) | "Lesson X.Y: <Topic>" from `COURSE_PLAN.md` |
| **Primary Objective** (lesson plan) | one or two sentences: what students will be able to *do / interpret / justify* with this topic, in student terms |
| **Priority Ideas & Skills** (gold box) | the concrete skills implied by the topic + standards; for a Lesson 0, the characteristics the spine marks ● for this unit |
| **Vocabulary, Concepts & Theorems** | terms/notation the topic introduces (use `\TallMath{...}` for tall formulas) |
| **Hook** | a scenario or graph that motivates the topic |
| **Learning Targets** (cover, "I can…") | one target per priority skill (or per standard), reworded as "I can …" |
| **Standards line** (lesson plan) | the SOL/other codes the user supplied for this lesson; record them for the audit trail |
| Activity / practice / homework contexts | original scenarios and practice exercising each skill; the experience's two scenarios stretch prior knowledge into the new material, and practice + homework span the difficulty the standards imply (no tiers) |

Keep wording in the course's teaching voice. The recurring move: read/interpret a graph or
result, *then* justify — "what does this feature mean here, and how do you know?" Where a lesson
uses a tool (Desmos), show its output as a pre-made figure rather than asking students to
construct one — and never ask students to *sketch/draw/construct* a graph from scratch.

## Review lessons

A review lesson (e.g. Unit 1's foundations lessons) uses the same skeleton; its "standards" are
the prerequisite skills being re-activated, and it carries no new function-family framework.
