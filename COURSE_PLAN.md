# Algebra 2 — Course Scope & Sequence

**Course:** Algebra 2: Shepherd · **School year:** 2026–2027

> **Status:** Unit 1 is built in source. **Units 2, 3, 4, and 5 are content-complete** — every lesson
> (plan, cover, warm-up, notes, activity, exit ticket, homework, all keys, and a slide deck) plus the
> unit tests (practice + actual and both keys, with the practice pair published to `sample_test/` +
> `sample_test_key/`). **Unit 5 (Rational Functions) closed out 2026-07-27**: all 8 lessons 5.0–5.7
> authored & building, and the **unit tests are now authored, built, and published**.
> **Unit 6 (Radical Functions): in progress** — lesson map confirmed & unit scaffolded 2026-07-27,
> locked at **8 lessons (6.0–6.7)**; all lesson dirs, component skeletons, and the unit `tests/` +
> `test_keys/` are laid down. **Lessons 6.0, 6.1, and 6.2 are authored & building (2026-07-27)**;
> lessons 6.3–6.7 and the unit tests are still skeletons.
> **Unit 7 (Exponential Functions): map confirmed & unit scaffolded 2026-07-27**, locked at
> **6 lessons (7.0–7.5)** — shorter than Units 5–6 because exponentials have no A2.EO and no A2.EI
> standard; a regression capstone (7.5) was added to cover A2.ST.2's exponential branch. All lesson
> dirs, component skeletons, and the unit `tests/` + `test_keys/` are laid down; **no Unit 7 content
> authored yet**.
> **Unit 8 (Logarithmic Functions): scaffolded 2026-07-27; Lesson 8.0 authored & building** —
> locked at **7 lessons (8.0–8.6)**. A standards audit found log properties and log equation-solving
> have **no 2023 VA SOL home**; they are kept as full lessons anyway (8.3, 8.4), labelled
> **beyond-SOL / precalculus prep** and barred from SOL-style test items — matching how Unit 7
> already treats 7.3. Three Unit 7 ↔ Unit 8 collisions were found and **resolved**: `A2.ST.2` is
> Unit 7's alone (7.5), since the standard never names logarithmic; $\ln$ lands in 8.5; and
> no-standard content is now handled the same way in both units. Full rationale in the Unit 8 status
> block in §4.
> **Next action: author Lesson 6.3 (multiplying & dividing radicals; rationalizing with
> conjugates)**, then proceed 6.4 → 6.7 in order, then the Unit 6 tests, then Unit 7 at Lesson 7.0.
> Unit 8 was opened out of order at the user's request; its remaining lessons (8.1–8.6) and unit
> tests are still skeletons.
> Lesson lists below are proposals to react to and edit — pacing (days per lesson) is intentionally
> left open pending the school calendar. **Authoring note:** every unit from 5 on must apply the
> vocab-box paragraph-break fix (§7); retrofitting Units 2–4 is deferred to §8, after Unit 8 and finals.

---

## 1. Design principles

- **Function-type organization.** After a foundations unit, each unit is built
  around one function family (linear → quadratic → polynomial → rational →
  radical → exponential → logarithmic).
- **Lesson 0 = "Characteristics of ____ Functions."** Every unit opens with a
  Lesson 0 that studies the *behavior* of the new function type before students
  learn to manipulate/solve it.
- **Cumulative characteristics spine.** Each Lesson 0 re-teaches the full
  "read-a-graph" toolkit built so far, then **adds the new characteristics that
  this function type is the first to require** (e.g., asymptotes debut in Unit 5,
  origin symmetry in Unit 4). See §3 for the full progression.
- **Consistent component set per lesson.** warm-up, notes/slides, activity,
  exit ticket, homework, cover — each with an answer key (matches Unit 1).

---

## 2. Units at a glance

| Unit | Title | Function family | Lessons (incl. L0) | Status |
|:---:|---|---|:---:|---|
| 1 | Foundations | (review) | 3 (no L0) | **Built** |
| 2 | Linear Functions | Linear, absolute value, piecewise | 6 | **Complete** |
| 3 | Quadratic Functions | Quadratic (incl. complex numbers) | 8 | **Complete** |
| 4 | Polynomial Functions | Polynomial | 7 | **Complete** |
| 5 | Rational Functions | Rational | 8 | **Complete** |
| 6 | Radical Functions | Radical / power | 8 | **In progress** (6.0–6.2 done) |
| 7 | Exponential Functions | Exponential | 6 | **Scaffolded** (map confirmed) |
| 8 | Logarithmic Functions | Logarithmic | 7 | **In progress** (8.0 done) |

Units 2–8 each open with **Lesson X.0: Characteristics of ____ Functions**.
**Out of scope for this course:** conic sections, sequences & series, probability
& statistics, trigonometry, and linear systems / linear programming.

---

## 3. The characteristics-of-functions spine (the heart of the course)

Each unit's Lesson 0 revisits everything to its left and introduces the row(s)
marked ●. Legend: **● introduced here** · **○ revisited / deepened** ·
**· applied but not new**.

| Characteristic | U1 | U2 Lin | U3 Quad | U4 Poly | U5 Rat'l | U6 Rad | U7 Exp | U8 Log |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Function definition & notation | ● | · | · | · | · | · | · | · |
| Domain & range (from a graph) | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| x- and y-intercepts / zeros | | ● | ○ | ○ | ○ | ○ | ○ | ○ |
| Slope / constant rate of change | | ● | | | | | | |
| Increasing / decreasing intervals | | ● | ○ | ○ | ○ | ○ | ○ | ○ |
| Positive / negative intervals | | ● | ○ | ○ | ○ | ○ | ○ | ○ |
| Maximum / minimum (extrema) | | | ● | ○ | · | · | · | · |
| Axis of symmetry / vertex | | | ● | ○ | | | | |
| Even symmetry (about y-axis) | | | ● | ○ | | | | |
| End behavior | | | ● | ○ | ○ | ○ | ○ | ○ |
| Odd symmetry (about origin) | | | | ● | | | | |
| Relative vs. absolute extrema | | | | ● | · | · | · | · |
| Turning points | | | | ● | · | | | |
| Zero multiplicity (graph behavior) | | | | ● | · | | | |
| **Asymptotes (vertical)** | | | | | ● | | | ○ |
| **Asymptotes (horizontal)** *(slant = enrichment only)* | | | | | ● | | ○ | |
| Holes / removable discontinuity | | | | | ● | | | |
| Domain restrictions | | | | | ● | ○ | | ○ |
| Restricted domain from radicand | | | | | | ● | | |
| Inverse relationship of families | | | | | | ● | | ○ |
| Growth vs. decay / constant ratio | | | | | | | ● | · |
| Inverse of exponential (dom/range swap) | | | | | | | | ● |

> This table is the pacing/coherence backbone. When authoring each Lesson 0, the
> "new" rows (●) are the teaching focus; the "○/·" rows are quick review applied
> to the new graph.
>
> **Preview note:** the absolute-value and piecewise lessons in Unit 2 give
> students an early, informal look at **vertex, axis of symmetry, and min/max**
> (the V-shape) before Unit 3 formalizes them for parabolas. The ● stays in U3
> because that's where the Lesson-0 progression makes them a teaching focus.

---

## 4. Unit-by-unit lesson breakdown

### Unit 1 — Foundations *(built)*
- **1.1** Evaluating & simplifying algebraic expressions
- **1.2** Equations & inequalities
- **1.3** Functions & statistics review
- Assessments: sample test + key (present in source)

### Unit 2 — Linear Functions
> **Status (scaffolded 2026-07-24):** all 6 lesson dirs (`unit02/lesson00`–`lesson05`)
> created with skeleton `main.tex` for lesson plan + cover, warmup, notes, activity,
> exit_ticket, homework, slides, and each `*_key`. Unit assessments scaffolded:
> `tests/{practice_test,actual_test}`, `test_keys/`, `sample_test{,_key}/`.
> **Lesson 2.0 authored & builds (2026-07-24):** all components + keys + 7-slide deck done;
> reads a line's characteristics (domain/range, intercepts/zero, slope, increasing/decreasing,
> positive/negative intervals) off pre-drawn TikZ graphs. Standards: **2023 VA SOL A2.F.2a/c/f**
> (from `spec/algebra2-vdoe-sol.pdf`); slope is reactivated Algebra 1 prerequisite. Warm-up &
> exit ticket each fit one page (blank+key);
> notes 3pp, homework 2pp, activity 2pp (key 3pp, extra page is the teacher-only note).
> **Lesson 2.1 authored & builds (2026-07-24):** all components + keys + 7-slide deck done;
> covers slope as rate of change, the three forms (slope-intercept, point-slope, standard),
> writing equations from a graph / two points / slope+point, and graphing by transforming the
> parent $y=x$ ($kf(x)$ stretch/reflect, $f(x)+k$ shift — the lens A2.F.1 extends to every family).
> Standards: **2023 VA SOL A.F.1a–e** (Algebra 1 linear cluster, reactivated as Unit 2's
> foundation). Warm-up & exit ticket each fit one page (blank+key); notes 3pp, activity 2pp,
> homework 2pp; exit ticket includes an SOL-style MC item. `make -C unit02/lesson01 all` → EXIT 0
> (student 10pp, full 20pp).
> **Lesson 2.2 authored & builds (2026-07-24):** all components + keys + 7-slide deck done;
> absolute value as *distance from zero* driving equations $|ax+b|=c$ (two-case rule, isolate-first,
> no-solution/one-solution special cases) and inequalities ("less th**AND**" $<$ → one interval;
> "great**OR**" $>$ → two rays), with solution sets written three ways (set / interval / number
> line) and a tolerance-modeling strand. Standards: **2023 VA SOL A2.EI.1a–e** (from
> `spec/algebra2-vdoe-sol.pdf`). Warm-up & exit ticket each fit one page (blank+key); notes 3pp,
> activity 2pp, homework 2pp; exit ticket includes an SOL-style MC item.
> `make -C unit02/lesson02 all` → EXIT 0 (student 10pp, full 20pp).
> **Lesson 2.3 authored & builds (2026-07-24):** all components + keys + 7-slide deck done; the
> absolute value parent $y=|x|$ as a V (distance graph), transformations via vertex form
> $g(x)=a|x-h|+k$ (vertex $(h,k)$, axis $x=h$, opens up/down by sign of $a$, narrow/wide by $|a|$,
> min/max value $k$), and reading domain/range/intercepts/increasing-decreasing off pre-drawn V's;
> all graphs pre-drawn (no sketch-from-scratch) — students read graphs, match equation↔graph,
> complete tables, and build equations from graphs. Standards: **2023 VA SOL A2.F.1b/c** (the
> transformation lens applied to the absolute value parent as entry example) and **A2.F.2a/c/d/f**
> (characteristics; absolute value is a piecewise-defined function). Warm-up & exit ticket each fit
> one page (blank+key); notes 3pp, activity 2pp (key 3pp — extra page is the teacher note),
> homework 2pp; exit ticket includes an SOL-style MC item.
> `make -C unit02/lesson03 all` → EXIT 0 (student 10pp, full 21pp).
> **Lesson 2.4 authored & builds (2026-07-24):** all components + keys + 7-slide deck done;
> piecewise-defined functions as one function built from different rules on different pieces of the
> domain — evaluating by piece selection (watching the boundary's $<$ vs.\ $\le$), reading pre-drawn
> piecewise graphs with open/closed endpoints and spotting a discontinuity (jump), writing $|x|$ and
> $|x-h|$ as two-piece linear rules (bridge from 2.3), and the greatest-integer/step function
> $\lfloor x\rfloor$ (round down; staircase constant on each $[n,n+1)$). All graphs pre-drawn (no
> sketch-from-scratch); students evaluate, read, match, and model (streaming free-trial, overtime pay,
> parking step cost, data plan). Standards: **2023 VA SOL A2.F.2a/b/c/f** (characteristics of
> piecewise-defined functions, including graphs with discontinuities and constant intervals). Warm-up
> & exit ticket each fit one page (blank+key); notes 3pp, activity 2pp, homework 2pp; exit ticket
> includes an SOL-style MC item. `make -C unit02/lesson04 all` → EXIT 0 (student 10pp, full 20pp).
> **Lesson 2.5 authored & builds (2026-07-25):** all components + keys + 7-slide deck done; linear
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
> includes an SOL-style MC item. `make -C unit02/lesson05 all` → EXIT 0 (student 10pp, full 20pp).
> **Unit 2 tests authored & build (2026-07-25):** `tests/practice_test` (3pp) + `tests/actual_test`
> (3pp) and their keys `test_keys/practice_test_key` (4pp) + `test_keys/actual_test_key` (4pp).
> Four parts each — A Vocabulary (matching, 8 pts), B Multiple Choice (6 items incl. SOL-style,
> 12 pts), C Short Answer & Computation (8 items, 40 pts), D Extended Response (2 justify items,
> 12 pts) — drawing across all six lessons: read line/V/piecewise graphs, write equations, solve
> $|ax+b|=c$ and $|ax+b|\lessgtr c$ (three-way solution sets), abs-value vertex form, piecewise
> evaluation + continuity, greatest-integer, and linear regression (slope/intercept interpretation,
> prediction, interpolation vs.\ extrapolation, correlation $\ne$ causation). Practice and actual are
> parallel with different numbers/contexts. `make -C unit02/tests all` and
> `make -C unit02/test_keys all` → EXIT 0; practice test + key published to `sample_test/` and
> `sample_test_key/`. **Unit 2 is content-complete; next is Unit 3 scaffolding.**

- **2.0** Characteristics of linear functions *(introduces: domain/range,
  intercepts, slope, increasing/decreasing, +/− intervals)*
- **2.1** Linear functions: slope & rate of change, forms of a line
  (slope-intercept, point-slope, standard), writing equations, and graphing
  with transformations
- **2.2** Absolute value equations & inequalities (solving algebraically)
- **2.3** Absolute value functions & transformations *(V-shape → previews vertex,
  axis of symmetry, min/max)*
- **2.4** Piecewise-defined functions — absolute value as the entry example, then
  the greatest-integer / step function and other classic piecewise functions
- **2.5** Linear regression (scatter plots, correlation, lines of best fit)

### Unit 3 — Quadratic Functions
> **Status (scaffolded 2026-07-25):** lesson map locked at **8 lessons (3.0–3.7)** — full
> breakdown (Systems 3.6 and Modeling 3.7 kept separate). All 8 lesson dirs
> `unit03/lesson00`–`lesson07` scaffolded with skeleton `main.tex` for lesson plan + cover,
> warmup, notes, activity, exit_ticket, homework, slides, and each `*_key`. Unit assessments
> scaffolded: `tests/{practice_test,actual_test}`, `test_keys/`, `sample_test{,_key}/`.
> **Lesson 3.0 authored & builds (2026-07-25):** all components + keys + 7-slide deck done; reads a
> parabola's characteristics off pre-drawn TikZ graphs — introduces the **vertex/turning point**
> (max vs. min and the max/min *value*), **axis of symmetry**, **even symmetry** (parent $y=x^2$),
> and **end behavior**, while revisiting domain/range, intercepts/zeros (up to two), increasing/
> decreasing, and positive/negative intervals; symmetry is the justification tool. Anchor graph
> $f(x)=x^2-2x-3=(x-1)^2-4$; projectile hook $h(t)=-16t^2+32t+48$ (vertex $(1,64)$, lands $t=3$).
> All parabolas pre-drawn via `plot` + `\clip` (no sketch-from-scratch); students read graphs/tables,
> use second differences to spot a quadratic, and interpret features in context. Standards: **2023 VA
> SOL A2.F.2a/c/d/f/g** (a,c,f revisited; d = absolute max/min and g = end behavior are new).
> Warm-up & exit ticket each fit one page (blank+key); notes 3pp, activity 4pp, homework 2pp; exit
> ticket includes an SOL-style MC item. `make -C unit03/lesson00 all` → EXIT 0 (student 12pp, full
> 22pp).
> **Lesson 3.1 authored & builds (2026-07-25):** all components + keys + 7-slide deck done; moves from
> *reading* a parabola (3.0) to *producing/graphing* one from its equation via the **three forms** ---
> vertex form $a(x-h)^2+k$ (vertex $(h,k)$, axis $x=h$, direction/width from $a$), standard form
> $ax^2+bx+c$ (axis $x=-b/2a$, vertex by substitution, $y$-int $(0,c)$), and intercept/factored form
> $a(x-p)(x-q)$ (zeros $p,q$, axis $x=(p+q)/2$) --- and reads each as **transformations** of the parent
> $y=x^2$ ($f(x)+k$, $f(x-h)$ with the right-shift sign flip, $a\,f(x)$ stretch/reflect). Unifying thread:
> the single curve $x^2-2x-3=(x-1)^2-4=(x+1)(x-3)$ (the 3.0 anchor) shown in all three costumes. All
> graphs pre-drawn via `plot`+`\clip` (no sketch-from-scratch); "graphing" is done by feature-extraction +
> equation↔graph matching + point tables. Standards: **2023 VA SOL A.F.2b/c/d** (Algebra 1 quadratic
> cluster reactivated as the graphing foundation), extended in Algebra 2 to the horizontal shift $f(x-h)$
> (the full **A2.F.1** transformation lens applied to the quadratic parent) with characteristics per
> **A2.F.2a/d**. Warm-up & exit ticket each fit one page (blank+key); notes 3pp, activity 2pp, homework
> 2pp; exit ticket includes an SOL-style MC item (horizontal-shift direction).
> `make -C unit03/lesson01 all` → EXIT 0 (student 10pp, full 20pp).
> **Lesson 3.2 authored & builds (2026-07-25):** all components + keys + 7-slide deck done; moves from
> *reading* a given factored form (3.1) to *producing* it and solving. Factoring the complete toolkit ---
> GCF first, $x^2+bx+c$ by the product/sum search, $ax^2+bx+c$ by grouping ($a\!\cdot\!c$ method),
> difference of squares $x^2-k^2$, and perfect-square trinomials (double root, graph tangent to axis) ---
> then the **Zero Product Property** ($AB=0\Rightarrow A=0$ or $B=0$; must set $=0$ first) to solve
> $ax^2+bx+c=0$, with the roots tied throughout to the parabola's $x$-intercepts/zeros. Unifying thread:
> the anchor $x^2-2x-3=(x+1)(x-3)$ from 3.0--3.1, now factored by hand. Two flagged traps: dividing by $x$
> (loses $x=0$) and the root$\leftrightarrow$factor sign flip. All graphs pre-drawn via `plot`+`\clip`;
> includes a patio-area model (reject the negative root). Restricted to real, factor-over-integers cases
> (square roots/completing the square → 3.3; complex roots → 3.4--3.5). Standards: **2023 VA SOL A2.EO.3b/d**
> (factor completely; difference-of-squares & perfect-square-trinomial identities) and
> **A2.EI.2a/b/d** (create, solve algebraically, and verify/interpret quadratic equations). Warm-up & exit
> ticket each fit one page (blank+key); notes 2pp, activity 2pp, homework 2pp; exit ticket includes an
> SOL-style MC item (root→factor sign flip). `make -C unit03/lesson02 all` → EXIT 0 (student 9pp, full
> 20pp).
> **Lesson 3.3 authored & builds (2026-07-25):** all components + keys + 7-slide deck done; solving
> quadratics that \emph{won't factor} via two methods --- the **Square Root Property** ($x^2=k\Rightarrow
> x=\pm\sqrt{k}$, $k\ge0$: isolate the square first, keep the $\pm$, simplest radical form, including
> $(x-h)^2=k$ binomial-square cases) and **completing the square** ($a=1$: move the constant, add
> $(b/2)^2$ to build a perfect square, then root), tied throughout to Lesson 3.1's **vertex form** (the
> same move rewrites $x^2-2x-3=(x-1)^2-4$, vertex $(1,-4)$ --- the unit anchor) and to a **choose-a-method**
> decision (factor / square roots / complete the square, dividing by $a$ first when $a\ne1$ in Tier E).
> Real solutions only; the negative-radicand wall ($x^2=-4$) is previewed and deferred to 3.4. All graphs
> pre-drawn via `plot`+`\clip`; includes a dropped-object model (square-root method) and a matted-photo area
> model. Standards: **2023 VA SOL A2.EI.2b** (solve algebraically --- square-root & completing-the-square
> methods, real solutions), **A2.EI.2a** (model), **A2.EI.2d** (verify/interpret roots as $x$-intercepts),
> building on **A2.EO.3d** (perfect-square-trinomial identity run forward) and **A2.F.2** vertex-form
> characteristics. Warm-up & exit ticket each fit one page (blank+key); notes 2pp, activity 2pp, homework
> 2pp; exit ticket includes an SOL-style MC item (which constant completes the square). `make -C
> unit03/lesson03 all` → EXIT 0 (student 9pp, full 19pp).
> **Lesson 3.4 authored & builds (2026-07-25):** all components + keys + 7-slide deck done; breaks the
> Lesson 3.3 ``no real solution'' wall by inventing the **imaginary unit** $i=\sqrt{-1}$ (working rule
> $i^2=-1$) --- rewriting negative radicals $\sqrt{-k}=i\sqrt{k}$ (pull $i$ out \emph{first}, then simplify;
> the $\sqrt{-a}\sqrt{-b}\ne\sqrt{ab}$ trap flagged), **standard form** $a+bi$ (real/imaginary parts,
> classify real / imaginary / pure imaginary, read points off the complex plane), and the three operations
> **add/subtract** (combine like terms) and **multiply** (FOIL then substitute $i^2=-1$), plus the
> **conjugate** product $(a+bi)(a-bi)=a^2+b^2$ (always real) and **powers of $i$** (cycle $i,-1,-i,1$; reduce
> exponent mod 4). Capstone reconnects to completing the square: $x^2+2x+5=0\Rightarrow(x+1)^2=-4\Rightarrow
> x=-1\pm2i$ (conjugate pair), previewing 3.5. Graphs pre-drawn via `plot`+`\clip` (no-real-roots parabola
> $y=x^2+4$) and Argand-plane point-reading; division-by-conjugate kept to a Tier E / homework extension as
> it sits beyond the add/subtract/multiply standard. Standards: **2023 VA SOL A2.EO.4a** (meaning of $i$),
> **A2.EO.4b** (equivalent negative-radical ↔ $a+bi$ forms), **A2.EO.4c** (add/subtract/multiply), building
> on **A2.EO.2** (radicals) and connecting forward to **A2.EI.2b** (3.5). Warm-up & exit ticket each fit one
> page (blank+key); notes 3pp, activity 2pp, homework 2pp; exit ticket includes an SOL-style MC item
> ($i^{38}$). `make -C unit03/lesson04 all` → EXIT 0 (student 10pp, full 20pp).
> **Lesson 3.5 authored & builds (2026-07-25):** all components + keys + 7-slide deck done; the \emph{one
> method that solves every quadratic}. Derives the **quadratic formula** $x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$ as
> completing the square (Lesson 3.3) done once on the general $ax^2+bx+c=0$, then a fixed protocol
> (standard form → read $a,b,c$ with signs → substitute/simplify) producing real \emph{and} complex ($a+bi$,
> Lesson 3.4) answers. Isolates the **discriminant** $b^2-4ac$ as a \emph{predictor} of the roots \emph{before}
> solving — three cases ($>0$ two real / $=0$ one repeated / $<0$ two complex-conjugate) each tied to a
> pre-drawn parabola's $x$-intercepts (2/1/0). Also: choose-a-method (factor/square-roots/formula), verify by
> substitution, and a projectile model (reject the impossible root). Unifying threads: the anchor
> $x^2-2x-3=0$ ($D=16$, roots $3,-1$ — matches 3.2 factoring) and the 3.4 leftover $x^2+2x+5=0$ ($D=-16$,
> roots $-1\pm2i$ — same conjugate pair the formula now reproduces). Tier E adds a discriminant \emph{parameter}
> problem (find $k$ for one/two/no real roots). All graphs pre-drawn via `plot`+`\clip` (no sketch-from-scratch).
> Standards: **2023 VA SOL A2.EI.2b** (solve over the complex numbers algebraically — the quadratic formula),
> **A2.EI.2a** (model), **A2.EI.2d** (verify/interpret), revisiting **A2.F.2d** (discriminant ↔ number/type of
> $x$-intercepts); builds on completing the square (3.3) and $i$ (3.4). Warm-up & exit ticket each fit one page
> (blank+key); notes 3pp, activity 2pp, homework 2pp; exit ticket includes an SOL-style MC item (root type from
> a given discriminant). `make -C unit03/lesson05 all` → EXIT 0 (student 10pp, full 20pp).
> **Lesson 3.6 authored & builds (2026-07-25):** all components + keys + 7-slide deck done; extends
> equation-solving from a \emph{single} quadratic (3.2--3.5) to a two-equation \textbf{system} with at least one
> quadratic. A \textbf{solution} is an ordered pair satisfying \emph{both} equations --- graphically a
> \textbf{point of intersection}; a \textbf{linear--quadratic} (line \& parabola) or
> \textbf{quadratic--quadratic} (two parabolas) system has \textbf{0, 1, or 2} solutions. Solve by
> \textbf{substitution} (set the two $y$-expressions equal) --- the key insight being that this \emph{collapses
> the system into one quadratic} already solvable by factoring (3.2) or the formula (3.5) --- then
> back-substitute to recover $y$; the collapsed equation's \textbf{discriminant} counts the intersection points
> (2/1/0), reusing Lesson 3.5's three cases (secant / tangent / miss). Includes the quad--quad ``identical-$x^2$
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
> `make -C unit03/lesson06 all` → EXIT 0 (student 10pp, full 20pp).
> **Lesson 3.7 authored & builds (2026-07-25):** all components + keys + 7-slide deck done; the unit capstone, where
> students stop being handed a quadratic and \emph{build} one from a story, then read the answer off its features. A
> \textbf{feature-to-question map} organizes everything --- \textbf{$y$-intercept} $=$ starting value, a \textbf{zero}
> (positive root) $=$ ``when/where it reaches $0$,'' the \textbf{vertex} $=$ \textbf{max/min} (input $=$ when/where,
> output $=$ how much) --- across three model types: \textbf{projectile} $h(t)=-16t^2+v_0t+h_0$ (anchor
> $-16t^2+32t+48$: start $48$, max $(1,64)$, lands $t=3$), \textbf{maximum area} (pen against a barn wall, three sides,
> $A(x)=x(40-2x)$, vertex $(10,200)$, with the $40-2x$ trap and a feasible-domain beat), and \textbf{revenue
> optimization} (price\,$\times$\,changing demand, $R(x)=(8+x)(200-20x)$, best price at the vertex). The algebra is
> entirely reused (vertex by $x=-b/2a$ from 3.1; zeros by factoring/formula from 3.2/3.5); the new work is
> translating, choosing the feature, interpreting with units, and rejecting impossible values (negative time, a width
> outside the fence). Tier E ties back to systems (3.6) via a ``same-height'' object comparison. All graphs pre-drawn
> (scaled-axis projectile parabola + barn-wall pen schematic; no sketch-from-scratch). Standards: **2023 VA SOL
> A2.EI.2a** (create a quadratic model), **A2.EI.2d** (verify/interpret, incl.\ vertex as max/min), **A2.F.2d**
> (max/min from the vertex); builds on A2.F.2a/d (3.1) and A2.EI.2b (3.2, 3.5). Warm-up & exit ticket each fit one page
> (blank+key); notes 3pp, activity 2pp, homework 2pp; exit ticket includes an SOL-style MC item (which feature is the
> max height). `make -C unit03/lesson07 all` → EXIT 0 (student 9pp, full 20pp).
> **All eight Unit 3 lessons (3.0–3.7) are now authored & building.**
> **Unit 3 tests authored & build (2026-07-25):** `tests/practice_test` (3pp) + `tests/actual_test` (3pp) and their
> keys `test_keys/practice_test_key` (3pp) + `test_keys/actual_test_key` (3pp). Four parts each — A Vocabulary
> (8-term matching, 8 pts), B Multiple Choice (6 items incl. SOL-style discriminant item, 12 pts), C Short Answer &
> Computation (8 items, 40 pts), D Extended Response (2 justify items, 12 pts) — drawing across all eight lessons:
> read a pre-drawn parabola (vertex/axis/intercepts/zeros/range, 3.0–3.1), vertex from standard form via $-b/2a$
> (3.1), solve by factoring (3.2), square roots & completing the square (3.3), complex-number arithmetic in $a+bi$
> (3.4), quadratic formula + discriminant (3.5), linear–quadratic system (3.6), and a projectile feature-to-question
> model + discriminant-vs.-$x$-intercepts reasoning (3.7 / 3.5). Practice and actual are parallel forms (same
> structure, different numbers). `make -C unit03/tests all` and `make -C unit03/test_keys all` → EXIT 0; practice
> test/key published to `sample_test/` and `sample_test_key/` via the `drop` targets. **Unit 3 is complete (all
> lessons + assessments). Next action: begin Unit 4 (Polynomial Functions).**
- **3.0** Characteristics of quadratic functions *(introduces: vertex/max-min,
  axis of symmetry, even symmetry, end behavior, turning point)*
- **3.1** Graphing quadratics (vertex, standard, intercept forms) & transformations
- **3.2** Solving by factoring (factoring quadratics)
- **3.3** Solving by square roots & completing the square
- **3.4** Complex numbers (operations, i)
- **3.5** The quadratic formula & the discriminant (incl. complex solutions)
- **3.6** Systems involving quadratics (linear–quadratic & quadratic–quadratic)
- **3.7** Modeling with quadratics (projectile/area/optimization)

### Unit 4 — Polynomial Functions
> **Status (map confirmed & scaffolded 2026-07-25):** lesson map locked at **7 lessons
> (4.0–4.6)** — the original 4.4 was split into a forward-solving lesson (4.4, RRT) and a
> counting/building lesson (4.5, FTA & complex zeros), pushing graphing+modeling to 4.6.
> All 7 lesson dirs `unit04/lesson00`–`lesson06` scaffolded with skeleton `main.tex` for
> lesson plan + cover, warmup, notes, activity, exit_ticket, homework, slides, and each
> `*_key`. Unit assessments scaffolded: `tests/{practice_test,actual_test}`, `test_keys/`,
> `sample_test{,_key}/`.
> Standards grounded against `spec/algebra2-vdoe-sol.pdf`: **A2.EO.3a/b/c/d** (operations,
> factoring, division, identities incl. sum/diff of cubes), **A2.EI.6a/b/c/d** (solve degree
> ≥3 over ℂ), **A2.F.2a/b/c/d/e/g** (characteristics/graphing; note polynomial is **not** in
> A2.F.1's family list, so transformations aren't a standard here — cube-root/radical graphing
> is Unit 6). Lesson 4.0 introduces the four new spine rows: ● odd/origin symmetry, ● relative
> vs. absolute extrema, ● turning points, ● zero multiplicity (end behavior deepened to the
> degree + leading-coefficient rule).
> **Lesson 4.0 authored & builds (2026-07-25):** all components + keys + 8-slide deck done; reads a
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
> touch + odd-degree end behavior). `make -C unit04/lesson00 all` → EXIT 0 (student 12pp, full 23pp).
> **Lesson 4.1 authored & builds (2026-07-25):** all components + keys + 8-slide deck done; turns 4.0's
> *factored* forms into *standard* forms. Covers standard form / degree / leading coefficient / term
> count (incl. two-variable term degree = sum of exponents), **adding & subtracting** as pure like-term
> collection with the year's biggest trap flagged (a leading minus is a factor of $-1$ — it flips
> **every** sign) plus the "degree can drop" case $(x^4+2x)-(x^4-5)=2x+5$, **multiplying** at all three
> sizes (monomial×poly, binomial×binomial, binomial×trinomial by box) in one *and two* variables, the
> **degree/leading-coefficient rule for products** (degrees add, leads multiply ⇒ end behavior known
> before expanding — the A2.F.2g link back to 4.0), and the **special products** $(a\pm b)^2$,
> $(a+b)(a-b)$ with the $(x+4)^2\ne x^2+16$ error killed numerically at $x=1$. Unifying thread: the unit
> anchor $(x-1)^2(x+2)$ is expanded to $x^3-3x+2$ (the $\pm 2x^2$ cells cancel — that is why there is no
> $x^2$ term), and homework expands 4.0's exit-ticket function $(x+1)^2(x-2)=x^3-3x-2$ and checks it
> against the graph students already read. Tier E expands 4.0's open-box model to
> $V(x)=4x^3-36x^2+80x$ (checked against that lesson's table, $V(1)=48$), builds a profit polynomial
> $P=R-C$, and justifies why a *product* never loses degree while a *sum* can. Standards: **2023 VA SOL
> A2.EO.3a** (sums, differences, products in one and two variables), **A2.EO.3d** in its *forward*
> direction (equality of forms; difference-of-squares & perfect-square-trinomial identities — factoring
> is 4.2), revisiting **A2.F.2g**. Warm-up & exit ticket each fit one page (blank+key); notes 3pp,
> activity 2pp (key 3pp — extra page is the teacher note), homework 2pp; exit ticket includes an
> SOL-style MC item ($(3x-4)^2$, distractors = the three classic errors).
> `make -C unit04/lesson01 all` → EXIT 0 (student 10pp, full 23pp).
> **Lesson 4.2 authored & builds (2026-07-25):** all components + keys + 10-slide deck done; runs 4.1
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
> $q(x)=x^4-5x^2+4$ — a **graph students already read in 4.0** — is factored in quadratic form to
> $(x-1)(x+1)(x-2)(x+2)$ and its four zeros matched to the intercepts (pre-drawn TikZ graph in the
> notes hook; no sketch-from-scratch). Closes on an honest **wall**: today's toolkit cannot crack the
> unit anchor $x^3-3x+2$ even though it factors — the motivation for 4.3/4.4. Tier E adds $x^6-64$
> factored *two ways* (squares-first vs. cubes-first ⇒ the rule "squares before cubes") and an
> expand-to-verify proof of the difference-of-cubes identity. Standards: **2023 VA SOL A2.EO.3b**
> (factor completely, one and two variables, ≤4 terms, over the integers) and **A2.EO.3d** (equality of
> forms; verify difference-of-squares, sum/difference-of-cubes, and perfect-square-trinomial
> identities), revisiting **A2.F.2c** (zeros from factored form) and **A2.EO.3a** (checking by
> multiplying). Warm-up & exit ticket each fit one page (blank+key); notes 3pp (key 4pp — extra page is
> the teacher note), activity 3pp, homework 2pp; exit ticket includes an SOL-style MC item ($8x^3-27$,
> distractors = the three cube-identity errors). `make -C unit04/lesson02 all` → EXIT 0 (student 12pp,
> full 26pp).
> **Lesson 4.3 authored & builds (2026-07-26):** all components + keys + 9-slide deck done; supplies the
> tool 4.2 lacked. Everything hangs on one statement, introduced from the Warm-Up's $247=5\cdot49+2$:
> $P=D\cdot Q+R$ with $\deg R<\deg D$, so **$R=0$ means the divisor is a factor**. Covers **monomial
> divisors** (split the fraction; one and two variables; the $\frac{5x^2y^2}{5x^2y^2}=1$-not-$0$ trap),
> **long division** with the two setup rules (standard form + a **placeholder 0** for every missing
> power) written with the subtraction shown as $-(\cdots)$, **synthetic division** for divisors $x-r$
> only (the sign flip $x+2\Rightarrow r=-2$ drilled as "rewrite it $x-(-2)$"), and both theorems
> *discovered rather than announced* — the **Remainder Theorem** lands when the remainder $-9$ from
> $(2x^3+3x^2-5)\div(x+2)$ turns out to equal $f(-2)$, proved in two lines by substituting $x=r$ into
> $f(x)=(x-r)q(x)+R$; the **Factor Theorem** arrives as a five-row equivalence table (factor $\iff$
> $f(r)=0$ $\iff$ remainder 0 $\iff$ zero $\iff$ $x$-intercept), already true in Warm-Up items 3–4.
> Unifying thread: the unit anchor $x^3-3x+2$ — unfactorable with 4.2's toolkit — is divided by $(x-1)$
> to give $x^2+x-2$ and hence $(x-1)^2(x+2)$, matched to the multiplicity-2 touch and the crossing
> students read off the 4.0 graph (**"the wall is down"**). Homework closes the unit's longest loop:
> $h(x)=x^3-3x-2$ (read on 4.0's exit ticket, expanded in 4.1, unfactorable in 4.2) is recovered as
> $(x+1)^2(x-2)$ by division; $(x^4-16)\div(x-2)$ returns $x^3+2x^2+4x+8=(x+2)(x^2+4)$, the same
> factorization 4.2 produced by a different road. Tier E carries the **factorable trinomial divisor**
> $x^2+x-6$ (the A2.EO.3c clause synthetic division cannot reach), a "find $k$ so $(x-3)$ is a factor"
> inversion, synthetic **substitution**, and a preview task where groups test the integer divisors of
> $6$ on $2x^3-3x^2-11x+6$, find $r=-2,3$, and discover the third zero $\frac12$ was never on the list —
> conjecturing the Rational Root Theorem a day early. Standards: **2023 VA SOL A2.EO.3c** (monomial,
> binomial, and factorable trinomial divisors), revisiting **A2.EO.3b** (factor the depressed
> polynomial completely) and **A2.EO.3a** (check by multiplying), touching **A2.F.2a/f** (zeros,
> $x$-intercepts, evaluating $f(r)$); direct prerequisite for **A2.EI.6c/d** in 4.4–4.5. Warm-up & exit
> ticket each fit one page (blank+key); notes 4pp (key 5pp), activity 3pp (key 4pp), homework 2pp; exit
> ticket includes an SOL-style MC item (which binomial divides $x^3-6x^2+11x-6$; distractors = the sign
> flip and two "grab the constant" errors). `make -C unit04/lesson03 all` → EXIT 0 (student 12pp,
> full 27pp).
> **Lesson 4.4 authored & builds (2026-07-26):** all components + keys + 9-slide deck done; supplies the
> candidate list 4.3 had to be handed. The whole lesson is one workflow — **list $\rightarrow$ test
> $\rightarrow$ divide $\rightarrow$ finish $\rightarrow$ verify** — hung on the **Rational Root
> Theorem**: for integer coefficients, a rational zero $\frac{p}{q}$ in lowest terms has $p \mid a_0$
> and $q \mid a_n$ (constant on *top*, leading coefficient on the *bottom*, every value with a $\pm$).
> The theorem is *earned rather than announced*: the Warm-Up finishes Lesson 4.3's Tier E preview task,
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
> build $6x^3+x^2-4x+1$ from zeros $\tfrac12,\tfrac13,-1$ (the A2.EI.6a skill 4.5 opens with), and
> closes on $x^3-x^2+4x-4$ whose depressed $x^2+4$ has no real zeros — the door into 4.5. Homework
> closes another loop: $x^3+2x^2-5x-6$ (4.3's exit ticket, where the divisor was *given*) must now be
> cracked with no hints, plus an A2.EI.6d verification step. Standards: **2023 VA SOL A2.EI.6c**
> (solve degree $\ge 3$; over $\mathbb{R}$ today, $\mathbb{C}$ in 4.5) and **A2.EI.6d** (verify
> algebraically and graphically, explain the method), using **A2.EO.3c** and **A2.EO.3b** on every
> problem and touching **A2.F.2c**. Warm-up & exit ticket each fit one page (blank+key); notes 4pp
> (key 5pp), activity 3pp (key 4pp), homework 2pp (key 3pp); exit ticket includes an SOL-style MC item
> (which value is *not* a possible rational zero of $4x^3-x^2+6x-3$; answer $\tfrac23$, distractors all
> valid candidates). `make -C unit04/lesson04 all` → EXIT 0 (student 12pp, full 28pp).
> **Lesson 4.5 authored & builds (2026-07-26):** all components + keys + 9-slide deck done; the lesson
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
> must have a real zero --- exactly what Lesson 4.0's opposite end-behavior arms forced graphically, and
> both arguments are put on the board. Graph-reading is the assessment core (**A2.EI.6b**): *imaginary
> zeros $=$ degree $-$ real zeros counted with multiplicity*, worked off pre-drawn TikZ graphs, with the
> recurring beat that an $x$-intercept \emph{is} a real zero and a graph can never show an imaginary
> one. Solving over $\mathbb{C}$ is Lesson 4.4's list$\to$test$\to$divide$\to$finish workflow with a
> single changed step --- a negative discriminant now yields a conjugate pair instead of ``no solution''
> ($x^3-5x^2+9x-5\Rightarrow 1,\,2\pm i$; $x^4-5x^2-36$ by quadratic form $\Rightarrow\pm3,\pm2i$) ---
> and **A2.EI.6a** drives the same road backward: zeros $\to$ factors $\to$ polynomial, supplying any
> missing conjugate. Unifying threads close three long loops: the Warm-Up finishes 4.4's Tier E
> cliffhanger $x^3-x^2+4x-4=(x-1)(x^2+4)\Rightarrow 1,\pm2i$ (whose pre-drawn graph crosses **once** ---
> the hook); the anchor $(x-1)^2(x+2)$ from 4.0 carries counting with multiplicity (a touch fills two
> slots); and homework finishes $x^3+2x^2+4x+8$, the quotient 4.3 produced from $x^4-16$, then revisits
> $x^2+4$ --- declared \emph{prime} in 4.2 --- to show that ``prime'' was always relative to a number
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
> (3.4), **A2.EI.2b** and the discriminant (3.5), **A2.EO.3b/c** (4.2--4.3), and **A2.F.2c** (4.0).
> Warm-up & exit ticket each fit one page (blank+key); notes 4pp (key 6pp), activity 3pp (key 4pp),
> homework 2pp (key 3pp); exit ticket includes an SOL-style MC item (which list \emph{cannot} be the
> complete zeros of a real quartic --- the answer lists $3i$ twice with no $-3i$).
> `make -C unit04/lesson05 all` → EXIT 0 (student 12pp, full 30pp); `make -C unit04 all` → EXIT 0.
> **Lesson 4.6 authored & builds (2026-07-26):** all components + keys + 10-slide deck done; the unit
> capstone, where every tool built separately becomes **one procedure that runs both directions**. The
> spine is the **five-step graph plan**: degree \& leading coefficient $\Rightarrow$ the arms (4.0, with
> the 4.1 shortcut that degrees add and leads multiply, so nothing is expanded); factor completely
> $\Rightarrow$ the $x$-intercepts (4.2--4.4); **multiplicity** $\Rightarrow$ cross (odd) / touch (even)
> / **flatten-then-cross** ($\ge3$); $f(0)$ $\Rightarrow$ one exact point; and the one genuinely new
> move, a **sign chart** --- test a single $x$ in each interval between consecutive zeros, in
> \emph{factored} form, keeping only the sign --- which delivers the positive/negative intervals and, as
> a by-product, catches the even-multiplicity fingerprint automatically (the sign fails to flip at a
> double zero). The **turning-point limit** $n-1$ is taught in both directions ($k$ turns $\Rightarrow$
> degree $\ge k+1$), and the plan's honest limit is stated out loud: it fixes every zero and both arms
> exactly but never the \emph{coordinates} of a turning point. Reversed (**A2.EI.6a**), a graph yields a
> factored equation, with $a$ solved from the **$y$-intercept** --- the only labeled point that is not a
> zero, which is exactly why an $x$-intercept gives the useless $0=0$ --- and the answer is always a
> \emph{possible} equation of least degree, since a graph can hide imaginary zeros (4.5) and even
> factors. The characteristics read (**A2.F.2a/c/d/e**) is done on $p(x)=x^4-5x^2+4$ (4.2's quartic) and
> corrects a Unit 3 habit head-on: the relative max at $(0,4)$ is \emph{not} absolute, an odd degree has
> \emph{no} absolute extrema, and an even degree gets one or the other but never both. The modeling
> strand (**A2.F.2f**) builds $V(x)=x(10-2x)(8-2x)=4x^3-36x^2+80x$ from a $10\times8$ sheet (the 4.0/4.1
> open-box model, third appearance), finds the **feasible domain** $0<x<4$, and insists that $x=5$ --- a
> genuine zero of $V$ --- is nonsense; on that domain the relative max ($\approx52.5$ in$^3$ near
> $x=1.5$) \emph{is} the absolute max, which is why it answers the question. Hook: two cubics with
> \emph{identical} zeros and identical arms, $(x-1)^2(x+2)$ vs.\ $(x-1)(x+2)^2$, whose graphs look
> nothing alike --- multiplicity is the feature that separates look-alikes. Tier E closes the unit's
> longest loop by running the box backward: a $48$ in$^3$ order becomes $x^3-9x^2+20x-12=0$, solved by
> the Rational Root Theorem (4.4) to $x=1,2,6$, with $6$ rejected and the \emph{two} feasible cuts
> explained as straddling the maximum (both appear as $48$ in the notes table). All graphs pre-drawn via
> `plot`+`\clip` --- students predict, match, read, and build, never sketch. Standards: **2023 VA SOL
> A2.F.2a/b/c/d/e/f/g** with **A2.EI.6a**; builds on A2.EO.3b/c and A2.EI.6b/c. Warm-up \& exit ticket
> each fit one page (blank+key); notes 5pp (key 6pp), activity 3pp (key 4pp), homework 3pp (key 3pp);
> exit ticket includes an SOL-style MC item (touch at $x=2$ with both arms down; distractors each break
> exactly one of degree parity, lead sign, and multiplicity).
> `make -C unit04/lesson06 all` → EXIT 0 (student 14pp, full 30pp); `make -C unit04 all` → EXIT 0.
> **All seven Unit 4 lessons (4.0--4.6) are now authored & building.**
> **Unit 4 tests authored & building (2026-07-26):** `tests/{practice_test,actual_test}` and
> `test_keys/{practice_test_key,actual_test_key}`, all four 4pp, published to `sample_test/` and
> `sample_test_key/` by the `drop` targets. Both forms are **skill-for-skill parallel with different
> numbers** and follow the Unit 3 architecture: **Part A** vocabulary matching, 8 pts (degree, leading
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
> (Part D at 6 pts each). Total 72 pts. `make -C unit04/tests all` and
> `make -C unit04/test_keys all` → EXIT 0; `make -C unit04 student` → 87pp,
> `make -C unit04 full` → 195pp (practice test in both, practice key in the full packet only; the
> actual test and its key stay out of every packet). Note `make -C unit04 all` builds only the
> lessons --- the tests need their own two `make` calls.
> **Unit 4 is complete (all lessons + assessments).** Unit 5's map is confirmed and scaffolded; see
> its section below.
- **4.0** Characteristics of polynomial functions *(introduces: degree/leading
  coefficient → end behavior, odd/origin symmetry, relative vs. absolute extrema,
  turning points, zero multiplicity)* — A2.F.2a/b/c/d/e/g
- **4.1** Operations with polynomials (add, subtract, multiply) — A2.EO.3a
- **4.2** Advanced factoring (GCF, grouping, sum & difference of cubes,
  two-variable expressions) — A2.EO.3b/d
- **4.3** Dividing polynomials (long & synthetic); Remainder & Factor Theorems — A2.EO.3c
- **4.4** Zeros of polynomials: the Rational Root Theorem *(forward-solve — RRT lists
  candidates, synthetic division tests/depresses, factor completely, solve for real zeros)*
  — A2.EI.6c/d
- **4.5** Fundamental Theorem of Algebra & complex zeros *(count & build — number/type of
  solutions, complex-conjugate pairs, multiplicity, write a polynomial from its zeros)*
  — A2.EI.6a/b (+ c/d)
- **4.6** Graphing polynomial functions & modeling — A2.F.2a–e/g

### Unit 5 — Rational Functions
> **Status (map confirmed & scaffolded 2026-07-26):** lesson map locked at **8 lessons (5.0–5.7)**.
> Three changes from the original ~6-lesson draft, all driven by `spec/algebra2-vdoe-sol.pdf`:
> (1) **variation is required, not optional** — **A2.F.1d** (directly/inversely proportional from a
> table; write the equation and graph a direct or inverse variation in context) is a listed
> knowledge-and-skill with no other home in the course (Units 6–8 are radical/exp/log), and
> $y=k/x$ *is* the rational parent — so it becomes a real lesson, **5.7**, as the modeling capstone
> (matching the 3.7 / 4.6 pattern); (2) **the draft's single "Graphing" lesson was split** into
> **5.4** (parent $y=1/x$ + transformations) and **5.5** (analyze-and-graph from an equation),
> because unlike polynomials, **rational functions *are* in A2.F.1's family list**, so
> **A2.F.1a/b/c/e** (parent-graph distinction, write the equation from a graph, graph via
> $f(x)+k$, $f(kx)$, $f(x+k)$, $kf(x)$) is a separate obligation from **A2.F.2a/g/h** — same
> overload that forced the Unit 4 4.4/4.5 split; (3) **complex algebraic fractions (A2.EO.1c)**,
> unbulleted in the draft, attach to **5.3** since simplifying one *is* combine-then-divide.
> **Slant/oblique asymptotes are NOT in the 2023 SOL** — A2.F.2h covers vertical and horizontal
> only. Decision: teach slant as **Tier E enrichment in 5.5** (a callback to 4.3 polynomial
> division) and **never assess it**; the §3 spine row was amended accordingly.
> Scope guardrails from the standards: **A2.EO.1b** limits expressions to **monomial and binomial
> factors, linear and quadratic**; **A2.EI.4b** likewise limits rational equations to **factorable
> linear and quadratic** expressions. Keep 5.1–5.3 and 5.6 inside those bounds.
> All 8 lesson dirs `unit05/lesson00`–`lesson07` scaffolded with skeleton `main.tex` for lesson
> plan + cover, warmup, notes, activity, exit_ticket, homework, slides, and each `*_key`. Unit
> assessments scaffolded: `tests/{practice_test,actual_test}`, `test_keys/`, `sample_test{,_key}/`.
> **Lesson 5.0 authored & builds (2026-07-26):** all components + keys + 10-slide deck done; the lesson
> where the course loses \emph{continuity}. Everything hangs on one sentence --- **the denominator runs
> the show** --- introduced from the Warm-Up, whose three items seed the three new ideas numerically
> before any of them is named: solving *denominator* $=0$ (the 4.2 factoring toolkit, reused as the
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
> the *simplified* form (the same error that becomes extraneous solutions in 5.6); one interval spanning
> a wall; and both overgeneralizations about asymptotes (that a HA can never be crossed, and that every
> rational function must have a VA). Modeling (**A2.F.2f**): activity Tier E interprets average cost
> $A(n)=\frac{6n+250}{n}$ (HA $y=6$ is the true per-shirt cost, never reached because
> $A(n)=6+\frac{250}{n}$; $n=0$ meaningless), and the homework extension reads a drug concentration
> $C(t)=\frac{5t}{t^2+1}$ --- HA $y=0$ as the drug clearing, peak $2.5$ mg/L at $t=1$, the graph
> *sitting on* its HA at $t=0$, and the deliberately unsettling case of a rational function with **no**
> vertical asymptote at all (domain $t\ge0$ comes from context, not algebra). All graphs pre-drawn via
> `plot`+`\clip` with branches truncated at the window edge and holes as open circles (no
> sketch-from-scratch). Standards: **2023 VA SOL A2.F.2h** (new), **A2.F.2a** (incl. graphs with
> discontinuities), **A2.F.2c**, **A2.F.2g**, **A2.F.2b**; builds on A2.EO.3b (4.2 factoring).
> **Slant asymptotes deliberately absent** (not in the 2023 SOL; Tier E of 5.5 only, never assessed).
> Warm-up & exit ticket each fit one page (blank+key); notes 5pp, activity 3pp, homework 3pp, cover 1pp
> --- every key paginates identically to its blank; exit ticket includes an SOL-style MC item
> ($h(x)=\frac{x-4}{x^2-16}$: hole at $x=4$, wall at $x=-4$; the three distractors ignore the
> cancelling, swap the two factors, and read restrictions off the simplified form).
> `make -C unit05/lesson00 all` → EXIT 0 (student 14pp, full 28pp).
> **Lesson 5.1 authored & builds (2026-07-26):** all components + keys + 9-slide deck done; the algebra
> that *produces* 5.0's holes. Everything hangs on one sentence --- **cancelling never restores an
> input** --- and it is earned rather than announced: the Warm-Up refutes ``$\frac{3+6}{3}=6$'' by
> computing the true value $3$ (so \emph{factors, not terms} is a fact students proved), and the Hook
> puts $A(x)=\frac{x^2-x-6}{x^2-9}$ beside its cancelled form $B(x)=\frac{x+2}{x+3}$ in a four-column
> table of values: they agree at $x=0,1,4$ ($\tfrac23,\tfrac34,\tfrac67$) and disagree at exactly one
> input, $x=3$, where $A$ gives $\tfrac00$ and $B$ gives $\tfrac56$. The lesson is a **four-step
> procedure** --- factor completely (the 4.2 toolkit) $\rightarrow$ **list the restrictions from the
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
> at $\left(3,\tfrac56\right)$ whose height comes from the \emph{simplified} form --- 5.0's cancel test
> run from the algebra side. Flagged traps: cancelling **terms** ($\frac{x^2+9}{x+3}=x+3$, killed
> numerically at $x=1$, plus the Unit 4 fact that $x^2+9$ is prime); **restrictions read off the
> simplified denominator** (the signature error, and the direct ancestor of extraneous solutions in
> 5.6); a lost $-1$ from opposite binomials; a simplified form with no restriction list (half an
> answer); and a squared factor cancelled entirely (wall, not hole). Homework closes with
> $g(x)=\frac{x^2+2x-8}{x-2}$ --- a rational function whose graph is a **line** with a hole at $(2,6)$
> and no vertical asymptote --- and a design task previewing 5.5 (build an expression with a hole at
> $x=2$ and a wall at $x=-1$). All graphs pre-drawn via `plot`/line + `\clip` with holes as open circles
> (no sketch-from-scratch). Standards: **2023 VA SOL A2.EO.1b** (justify and determine equivalent
> rational expressions, monomial and binomial factors, linear and quadratic) and **A2.EO.1d**
> (equivalence of forms); builds on **A2.EO.3b** (4.2) and 5.0's restrictions/holes; prerequisite for
> A2.EO.1a (5.2--5.3), A2.F.2h from the equation (5.5), and A2.EI.4c (5.6). Warm-up & exit ticket each
> fit one page (blank+key); notes 4pp, activity 3pp, homework 2pp (key 3pp --- extra page is the teacher
> note), cover 1pp; exit ticket includes an SOL-style MC item ($\frac{4-x^2}{x^2-x-2}$; the three
> distractors drop the $-1$, read restrictions off the simplified denominator, and cancel the $x^2$
> terms). `make -C unit05/lesson01 all` → EXIT 0 (student 12pp, full 26pp).
> **Lesson 5.2 authored & builds (2026-07-26):** all components + keys + 10-slide deck done; the lesson
> where the restriction list stops being readable off the page. Multiplying is 5.1's four steps with one
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
> expanding (an expanded product **hides its own factors** --- the Unit 4 cost argument), and **flip
> before you cancel**, disproved numerically because top-with-top *does* happen to work for division while
> the other diagonal never does ($\frac43\div\frac54$: $\frac1{15}$ vs.\ $\frac{16}{15}$; with letters,
> $\frac x4\div\frac5x=\frac{x^2}{20}$, not $\frac1{20}$). Anchors: the product
> $\frac{x^2-9}{x^2+2x-8}\cdot\frac{x+4}{x^2+3x}=\frac{x-3}{x(x-2)}$ ($x\neq0,2,-3,-4$, two invisible) and
> the quotient $\frac{x^2-4}{x^2+7x+12}\div\frac{x^2+2x}{x+3}=\frac{x-2}{x(x+4)}$ ($x\neq0,-2,-3,-4$,
> one value from each of the three sources). Opposite binomials (5.1) carry forward inside products
> ($\frac{x^2-25}{x+2}\cdot\frac{2x+4}{5-x}=-2(x+5)$). Graph-reading closes the notes:
> $P(x)=\frac{x^2-1}{x}\cdot\frac{x}{x+1}$ is the **line $y=x-1$ with two holes**, at $(0,-1)$ and
> $(-1,-2)$ --- one per denominator --- pre-drawn with open circles (no sketch-from-scratch). Repeated
> beat: **a polynomial answer still carries restrictions** ($2x(x-6)$ with $x\neq0,-6$; a homework item
> whose written denominators are the constants $2$ and $5$, so *every* restriction comes from the divisor's
> numerator). Flagged traps: multiplying out first; missing the divisor's-numerator restriction (the
> signature error); cancelling across the $\div$; flipping the *first* fraction; restrictions read off the
> answer (5.1's error, now worse with two denominators); a lost $-1$. Tier E adds a **restriction
> detective** table (attribute each of $x\neq0,1,-2,-3$ to its source, one value having *two*), a
> build-it-backwards division, and a rectangle whose length is recovered by division, verified by
> multiplying back, with the source-3 restriction interpreted geometrically (zero width) and a feasible
> domain that is a **union**. Standards: **2023 VA SOL A2.EO.1a** (multiply, divide, simplify the result),
> applying **A2.EO.1b** and **A2.EO.1d**; builds on **A2.EO.3b** (4.2) and 5.1; prerequisite for
> **A2.EO.1a/c** (5.3 --- a complex fraction *is* a division) and **A2.EI.4c** (5.6). Warm-up & exit
> ticket each fit one page (blank+key); notes 4pp, activity 2pp (key 3pp --- extra page is the teacher
> note), homework 2pp (key 3pp), cover 1pp; exit ticket includes an SOL-style MC item on
> $\frac{x^2-25}{x^2+3x}\div\frac{x-5}{x+3}$ (distractors: restrictions off the answer / divisor's
> numerator forgotten / wrong fraction flipped). `make -C unit05/lesson02 all` → EXIT 0 (student 11pp,
> full 27pp).
> **Lesson 5.3 authored & builds (2026-07-26):** all components + keys + 11-slide deck done; the lesson
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
> it must be built from the *original* denominators, never read off the answer (5.1's error at its third
> appearance). **Complex fractions** are taught in the standard's own words, as a *quotient of simple
> fractions*: Method 1 (combine top, combine bottom, keep--change--flip --- 5.2 reused outright) is the
> assessed method, Method 2 (multiply through by the LCD of the inner fractions) is the speed trick, and
> the conceptual beat is that **Method 2 erases the evidence for the inner-denominator restriction**
> since clearing them is exactly what it does. Restrictions come from two levels --- every inner
> denominator, and the *whole bottom*, which is Lesson 5.2's **source 3** in a new costume. Anchors: the
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
> **A2.EO.1d**; builds on **A2.EO.3b** (4.2) and 5.1--5.2; prerequisite for **A2.EI.4b/c** (5.6 --- solving
> begins by multiplying through by an LCD, and an extraneous solution is one of today's excluded values
> returning). Warm-up & exit ticket each fit one page (blank+key); notes 5pp, activity 3pp, homework 3pp,
> cover 1pp --- **every key paginates identically to its blank**; exit ticket includes an SOL-style MC item
> on $\frac{1/x-1/5}{x-5}$ (distractors: the lost $-1$ from opposite binomials / the main bar's restriction
> forgotten / never simplified, restrictions read off its own denominator).
> `make -C unit05/lesson03 all` → EXIT 0 (student 14pp, full 30pp); `make -C unit05 all` → EXIT 0.
> **Lesson 5.4 authored & builds (2026-07-26):** all components + keys + 11-slide deck done; the lesson
> where the unit's expressions go back on the grid. Everything hangs on one sentence --- **the asymptotes
> are the parent's axes, and they travel with the graph** --- and it is discovered numerically before it is
> named: the Hook puts two tables side by side, $y=\frac1x$ at $x=-2\ldots2$ and $y=\frac{1}{x-3}$ at
> $x=1\ldots5$, whose \emph{output} columns come out identical ($-\frac12,-1,\text{undef.},1,\frac12$), so
> the blow-up moved to $x=3$ while the settling-down value stayed at $y=0$. Introduces the **rational
> parent** $f(x)=\frac1x$ --- the two-branch **hyperbola**, VA $x=0$, HA $y=0$, origin symmetry (4.0),
> decreasing on *each* branch (5.0's union rule), and the fact no other parent in the course shares:
> **no intercepts at all** (a fraction is zero only when its numerator is; $x=0$ is not in the domain).
> Then **general form** $g(x)=\frac{a}{x-h}+k$ read in a fixed order --- $h\Rightarrow$ VA, $k\Rightarrow$ HA,
> $(h,k)$ the **center** where they cross (*not* a point of the graph), $a$ the stretch/reflection that moves
> **neither** asymptote. The four A2.F.1c transformations are all met, including the honest treatment of
> $f(kx)$: on this parent it collapses into $kf(x)$, since $\frac{1}{4x}=\frac{1/4}{x}$ --- which is why one
> letter $a$ suffices. Anchor $g(x)=\frac{2}{x-3}+1$ (VA $x=3$, HA $y=1$, center $(3,1)$, $y$-int $\frac13$,
> $x$-int $(1,0)$), plus the sharpened asymptote claim: a *transformed parent* **never** crosses its HA
> (that needs $\frac{2}{x-3}=0$) --- stronger than 5.0's "may cross," and worth contrasting with
> $\frac{2x}{x^2+1}$. **A2.F.1b** gets its own section (asymptotes $\rightarrow h,k$; one point $\rightarrow a$;
> **second point $\rightarrow$ check**) on $y=\frac{2}{x+1}-2$, and it is flagged as the likeliest SOL item on
> the standard. Closes on **A2.F.1a/e**: a compare-and-contrast table against $y=x^2$/$y=|x|$, then **the
> disguise** --- $\frac{x-1}{x-3}=\frac{(x-3)+2}{x-3}=1+\frac{2}{x-3}$, which *is* the anchor, and which lands
> on exactly the Warm-Up's item-3 pattern from the opposite direction; this is also *why* 5.0's degree rule
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
> *products* ($xy=12$) --- which quietly seeds **5.7**'s inverse variation; do not name it there. All graphs
> pre-drawn via `plot`+`\clip` with branches truncated at the window edge (no sketch-from-scratch); the
> activity's three matching windows share $y\in[-5,5]$ so they sit on a common baseline. Standards:
> **2023 VA SOL A2.F.1a/b/c/e** (new), applying **A2.F.2h**, **A2.F.2a**, **A2.F.2c**, **A2.F.2g**, and
> **A2.F.2f**; builds on Units 2--3 transformations and 5.3's combining. Warm-up & exit ticket each fit one
> page (blank+key); notes 5pp, activity 3pp, homework 3pp, cover 1pp --- **every key paginates identically to
> its blank**; exit ticket includes an SOL-style MC item (VA $x=-4$, HA $y=3$; the three distractors flip the
> sign of $h$, swap the two jobs, and read the HA off the numerator).
> `make -C unit05/lesson04 all` → EXIT 0 (student 14pp, full 30pp); `make -C unit05 all` → EXIT 0.
> **Lesson 5.5 authored & builds (2026-07-27):** all components + keys + 13-slide deck done; the lesson
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
> asymptote, at its own $x$-intercept --- which reconciles 5.0's "may cross" with 5.4's "never," both
> being the single fact that a fraction is zero only when its numerator is. Anchor B
> $g(x)=\frac{x^2-4}{x^2-x-6}$ adds the hole $(-2,\frac45)$, wall $x=3$, HA $y=1$, and the trap that
> $(-2,0)$ is **not** an $x$-intercept though the original numerator vanishes there; simplified it is
> $\frac{x-2}{x-3}=1+\frac{1}{x-3}$ --- yesterday's anchor family with one point punched out, so
> **5.5 did not replace 5.4, it surrounded it**. Flagged traps: restrictions read off the *simplified*
> form (the costliest, and tomorrow's extraneous solution); a wall announced at every excluded value
> without the cancel test; a cancelled zero called an intercept; the hole used as a boundary point;
> degrees compared factor-by-factor; refusing "no $x$-intercept" when the numerator is a nonzero
> constant; assuming signs alternate (homework 1(f), $\frac{x^2-9}{x^2-6x+9}$, breaks it --- two copies
> down, one up, so the restriction survives as a wall and there is *no* hole); one interval spanning a
> wall. Modeling (**A2.F.2f**) deliberately reverses 5.4's: activity Tier E is the **round trip**,
> $T(x)=\frac{30}{x}+\frac{30}{x+10}=\frac{60x+300}{x(x+10)}$ (5.3 run forwards), where the wall $x=0$
> and the floor $y=0$ both mean something and $x=-10$, $(-5,0)$ are negative speeds; the homework is
> **pollution cost**, $C(p)=\frac{25p}{100-p}$ ($25\to100\to225\to475\to2475$), where the *vertical*
> asymptote carries the meaning (no finite budget buys $100\%$ removal) and HA $y=-25$ means nothing.
> **Slant asymptotes appear once**, as activity Tier E Part 2 --- divide $\frac{x^2-4}{x+1}$ by 4.3
> long division to get $x-1-\frac{3}{x+1}$ against a pre-drawn dashed $y=x-1$ --- explicitly labelled
> enrichment and **never assessed**. All graphs pre-drawn via `plot`+`\clip` with holes as open circles
> (no sketch-from-scratch). Standards: **A2.F.2h**, **A2.F.2a**, **A2.F.2g** (new emphasis), applying
> **A2.F.1c**, **A2.F.2c**, **A2.F.2f**; builds on A2.EO.3b (4.2), A2.EO.1b/d (5.1), and the 4.6 sign
> chart. Warm-up & exit ticket each fit one page (blank+key); notes 5pp, activity 4pp, homework 3pp,
> cover 1pp --- **every key paginates identically to its blank**; exit ticket includes an SOL-style MC
> item (hole $x=1$, VA $x=-2$, HA $y=1$; the three distractors ignore the degree comparison, flip every
> sign, and cancel the wrong factor). `make -C unit05/lesson05 all` → EXIT 0 (student 15pp, full 33pp);
> `make -C unit05 all` → EXIT 0.
> **Lesson 5.6 authored & builds (2026-07-27):** all components + keys + 11-slide deck done; the unit's
> payoff loop, where the excluded values students have listed since 5.1 come back as answers to throw
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
> than re-substituting. A dedicated opening section separates **5.3 from 5.6** (*you may clear
> denominators only when there is an equals sign*) --- the predictable carry-over error after a
> combining lesson. Anchors: $\frac{6}{x}-\frac{2}{x-1}=1$ (candidates $2,3$, nothing thrown away) and
> $\frac{x}{x+1}+\frac{2}{x-1}=\frac{2}{x^2-1}$ ($-1$ extraneous, $0$ survives). **5.5 pays its debt in
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
> ($\frac{6}{4-c}+\frac{6}{4+c}=4$, $c=\pm2$, with $c\neq4$ a 5.5 vertical asymptote meaning the paddler
> exactly matches the river). Activity Tier E part 3 answers the question sharp students ask --- clearing
> can *add* solutions but dividing by a variable expression *loses* them --- on
> $\frac{x^2}{x-1}=\frac{x}{x-1}$, where the careless division discards the only real solution ($0$) and
> keeps the extraneous one ($1$). Flagged traps: no restriction list on the page; restrictions off the
> *simplified* form; only the fractions multiplied by the LCD (homework 5's error analysis is built on
> it, and Tier A's error analysis has **no error in it at all** --- every line correct, Step 4 skipped);
> cross-multiplying a three-term equation; a negative or fractional answer rejected on reflex; and
> ``extraneous'' used as a synonym for ``rejected.'' Standards: **2023 VA SOL A2.EI.4b** (new),
> **A2.EI.4c**, **A2.EI.4d**, **A2.EI.4a**; applying A2.F.2h + the 5.5 cancel test and A2.EO.1a/b
> (5.1--5.3); builds on A2.EO.3b (4.2). Prerequisite for **6.4** (radical equations reuse the same
> extraneous logic). Warm-up & exit ticket each fit one page (blank+key); notes 4pp (key 5pp), activity
> 3pp (key 4pp), homework 3pp, cover 1pp --- the extra key page in notes/activity is the teacher note
> only, so every answer page paginates identically to its blank; exit ticket includes an SOL-style MC
> item on $\frac{x}{x+3}+\frac{3}{x-3}=\frac{18}{x^2-9}$, which clears to $x^2=9$ so *both* candidates
> are excluded (answer: no solution; the distractors keep one candidate or both --- a student choosing
> $\{3,-3\}$ did the algebra perfectly and skipped Step 4).
> `make -C unit05/lesson06 all` → EXIT 0 (student 13pp, full 31pp); `make -C unit05 all` → EXIT 0.
> **Lesson 5.7 authored & builds (2026-07-27):** all components + keys + 11-slide deck done; the unit's
> modeling capstone and its last lesson. Everything hangs on one instruction --- **run both rows of
> arithmetic, on every row of the table** --- seeded in the Warm-Up before either name is spoken: two
> tables where students fill a *quotient* row and a *product* row and discover that P's quotients settle
> ($5$) while Q's products do ($60$), with Q's quotient row deliberately ugly ($15$, $3.75$,
> $1.\overline{6}$, $0.6$). Constant quotient ⇒ **direct**, $y=kx$; constant product ⇒ **inverse**,
> $y=k/x$; neither ⇒ **neither**, which A2.F.1d names explicitly and students never volunteer. The Hook
> copies 5.6's design (identical surface features, different verdicts): Tables A ($y=6x$) and B
> ($y=3x+6$) both climb by a constant amount and are both lines, but doubling $x$ from $2$ to $4$ sends
> A's $y$ from $12$ to $24$ and B's only to $18$ --- and at $x=0$, B gives $6$. **A direct variation is
> a line through the origin; "climbs steadily" is not the test.** Anchors: gasoline $c=3.40g$ ($k$ =
> dollars *per gallon*, graph through $(0,0)$ because zero gallons costs zero dollars) and the
> $240$-mile trip $t=240/r$, where **$k$ is not a rate but the distance** ($rt=d$ in disguise) --- and
> where the unit closes its loop, because $t=240/r$ *is* the 5.4 parent stretched by $240$, so both
> asymptotes become sentences (VA $r=0$: "standing still, you never get there"; HA $t=0$: "no speed makes
> a trip take no time"). The "neither" section carries two traps in opposite directions: $y=5x+15$ (rises
> steadily, not direct --- a *fee before you buy anything*) and $y=10-x$ (falls steadily, products
> $9,16,21,24$, not inverse). Finding $k$ closes with the shortcut named as **yesterday's**: a direct
> variation is literally $y_1/x_1 = y_2/x_2$, a proportion, so cross-multiply (5.6); an inverse one is
> $x_1y_1=x_2y_2$. Joint/combined variation ($y=kxz$, $y=kx/z$) is present and **labeled enrichment,
> not assessed** --- A2.F.1d names direct and inverse only --- with students deriving $V=\pi r^2h$ from
> "$V$ varies jointly as $h$ and $r^2$." **5.6 pays its debt in the interpretation items:** every
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
> never have an asymptote?* (it is a polynomial --- the 5.0 compare-and-contrast table, fair game on the
> test); and homework Extension part 3, proving no four-row table can be both direct and inverse
> ($kx=m/x$ forces $x^2=m/k$, at most two $x$-values), landing on a direct and an inverse through
> $(2,6)$ meeting again at $(-2,-6)$. Exit ticket item 2's table has products $12,18,18,12$ --- two
> match on purpose, so anyone who checks a pair and stops agrees with the wrong classmate. Warm-up &
> exit ticket each fit one page (blank+key); notes 5pp (key 5pp), activity 3pp (key 4pp), homework 3pp
> (key 4pp), cover 1pp, slides 11 frames --- the extra key pages are the teacher note.
> `make -C unit05/lesson07 all` → EXIT 0 (student 14pp, full 32pp).
> **Unit 5 tests authored & built (2026-07-27):** practice + actual and both keys, all 5pp, all four
> building clean (`make -C unit05/tests all` and `make -C unit05/test_keys all` → EXIT 0), and the
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
> error-by-error item analysis. **Slant asymptotes deliberately absent** (5.5 Tier E only, never
> assessed), and every expression stays inside the A2.EO.1b / A2.EI.4b linear-and-quadratic bound.

- **5.0** Characteristics of rational functions *(introduces: vertical & horizontal
  asymptotes, holes/removable discontinuity, domain restrictions)* — A2.F.2a/b/c/g/**h**
- **5.1** Simplifying rational expressions & domain restrictions *(factor-and-cancel with the
  4.2 toolkit; restrictions read off the **original** denominator — the algebraic engine behind
  5.0's holes)* — A2.EO.1b/d
- **5.2** Multiplying & dividing rational expressions *(factor first; keep-change-flip;
  restrictions from every denominator including the divisor)* — A2.EO.1a
- **5.3** Adding & subtracting rational expressions + complex fractions *(LCD from factored
  denominators; a complex fraction as combine-then-divide)* — A2.EO.1a/**c**
- **5.4** The rational parent function & transformations *(the $y=1/x$ hyperbola; the four
  transformations move the asymptotes; write the equation from a graph)* — A2.F.1a/b/c/e
- **5.5** Graphing rational functions from the equation *(factor → holes vs. vertical asymptotes
  → horizontal asymptote by degree comparison → intercepts → sign chart reused from 4.6 → end
  behavior; slant asymptote as Tier E only)* — A2.F.2a/g/h + A2.F.1c
- **5.6** Solving rational equations & extraneous solutions *(LCD-multiply or cross-multiply;
  extraneous roots are exactly 5.1's excluded values — the unit's payoff loop)* — A2.EI.4a/b/c/d
- **5.7** Direct, inverse & joint variation *(modeling capstone: proportional vs. inversely
  proportional from a table, find $k$, write and interpret the equation; joint variation is not
  named in A2.F.1d — carry it as enrichment)* — A2.F.1d (+ A2.F.2f)

### Unit 6 — Radical Functions
> **Status (map confirmed & scaffolded 2026-07-27):** lesson map locked at **8 lessons (6.0–6.7)**,
> grounded against `spec/algebra2-vdoe-sol.pdf`. Two changes from the original ~5-lesson sketch:
> the single "simplifying & operations" lesson was **split into 6.2 (simplify + add/subtract) and
> 6.3 (multiply/divide + rationalizing)** — A2.EO.2a/b carries the same load the parallel rational-
> expression standard got across 5.1–5.3 — and the "inverse functions & composition" lesson was
> **split into 6.6 (composition) and 6.7 (inverses)**, since A2.F.2i, j, and k are three separate
> K&S and composition is the *prerequisite* that verifies an inverse. All 8 lesson dirs
> `unit06/lesson00`–`lesson07` scaffolded with skeleton `main.tex` for lesson plan + cover, warmup,
> notes, activity, exit_ticket, homework, slides, and each `*_key`. Unit assessments scaffolded:
> `tests/{practice_test,actual_test}`, `test_keys/`, `sample_test{,_key}/`. Skeletons compile
> (`make -C unit06/lesson01 all` → EXIT 0). **No content authored yet.**
> Unit shape deliberately mirrors Unit 5: characteristics → algebra engine → graphing → solving →
> capstone. Lesson 6.0 introduces the two new spine rows: ● restricted domain from the radicand,
> ● inverse relationship of families.
> **Standards coverage:** **A2.EO.2a/b/c** (simplify, operate on, and convert radical expressions ⇄
> rational exponents), **A2.EI.5a/b/c** (solve/verify/justify radical equations), **A2.F.1a/b/c/e**
> (square root *and* cube root parents + transformations), **A2.F.2a–g** (characteristics), and
> **A2.F.2i/j/k** (inverses and composition — Unit 6 is their only home in the course; Unit 8
> revisits the idea only as exponential ⇄ logarithmic).
> **Authoring note:** apply the §7 vocab-box paragraph-break fix in every notes/notes_key.
> **Lesson 6.0 authored & builds (2026-07-27):** all components + keys + 10-slide deck done; teaches
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
> index as unrestricted). `make -C unit06/lesson00 all` → EXIT 0 (student 13pp, full 28pp);
> `make -C unit06 all` → EXIT 0.
> **Lesson 6.1 authored & builds (2026-07-27):** all components + keys + 10-slide deck done; supplies
> the *algebra* underneath 6.0's geometry. One thesis, stated as a derivation rather than a
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
> a notation drill: 6.0's two parents are relabeled $y=x^{1/2}$ and $y=x^{1/3}$ (same pre-drawn
> graphs, new notation) and the domain rule is re-derived from the **denominator**, with the closing
> claim that "even index restricts the domain" and "even denominator restricts the domain" are one
> sentence in two notations — the homework's item 6 makes students say it. Tier E does the four
> mismatched-index problems no radical rule can touch (incl. nested $\sqrt{\sqrt[3]{x}}$, indices
> multiply) plus **Kepler's third law** $T(a)=a^{3/2}$ on a perfect-power table ($a=1,4,9,25$),
> Jupiter estimated at $5.2$ AU, and $a=T^{2/3}$ obtained by raising both sides to the **reciprocal**
> — the algebraic form of 6.0's reflection over $y=x$ and a genuine preview of 6.7. The homework
> extension is **Kleiber's law** $M(w)=70w^{3/4}$, deliberately the same shape: $16\times$ the mass
> buys only $8\times$ the calories, which is what an exponent below $1$ does to growth (the
> flattening read off the square root graph in 6.0), inverted to $w=\left(\frac{M}{70}\right)^{4/3}$.
> Standards: **2023 VA SOL A2.EO.2c** (governing — convert radical ⇄ rational exponent, assessed in
> every component) and **A2.EO.2a** (equivalent radical expressions, via the evaluations and
> property work — this lesson supplies the tool 6.2–6.3 lean on), revisiting **A2.F.2a**/**A2.F.1a**
> (domain and parent graphs) and reaching **A2.F.2f** (evaluate and interpret in context) through the
> two models, which also preview **A2.F.2i/j**. Warm-up & exit ticket each fit one page (blank+key);
> notes 4pp (key 4pp), activity 3pp (key 3pp), homework 3pp (key 3pp) — blank and key paginate
> identically throughout. Exit ticket includes an SOL-style MC item (which expression equals
> $\sqrt[4]{x^3}$; distractors = the flipped fraction, index×power, and reading a root as a negative
> exponent). `make -C unit06/lesson01 all` → EXIT 0 (student 13pp, full 27pp);
> `make -C unit06 all` → EXIT 0.
> **Lesson 6.2 authored & builds (2026-07-27):** all components + keys + 11-slide deck done. One
> sentence carries the lesson — **a radical splits over multiplication and never over addition** —
> and it is *established by the students* rather than announced: the Hook puts three statements on
> the board ($\sqrt8\cdot\sqrt2=4$, $\sqrt9+\sqrt{16}=\sqrt{25}$, $\sqrt8+\sqrt{18}=5\sqrt2$) and asks
> which is the lie. The one that *looks* absurd is true (to three decimals) and the reasonable-looking
> one is false, so the class discovers both halves of the day in three minutes. The properties are
> then **derived, not stated**: $\sqrt[n]{ab}=(ab)^{1/n}=a^{1/n}b^{1/n}$ is 6.1's power-of-a-product
> rule, with the even-index fine print ($a,b\ge0$) flagged as the place a student who cannot tell when
> a root exists will turn $\sqrt{-8}$ into $\sqrt{-4}\cdot\sqrt2$ — the exact pile 6.1's exit ticket
> told the teacher to sort for. Four further beats: **simplest form** as three conditions with
> condition 3 (no radical in a denominator) *explicitly deferred to 6.3* so students know something is
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
> =\frac{n(n+1)}2\sqrt2$, and closes with a deliberate bridge to 6.4: $f(x)=\sqrt{8x}=2\sqrt{2x}$ is
> $g(x)=\sqrt{2x}$ **vertically stretched**, domain and endpoint unchanged. Homework extension is the
> **pendulum** $T(L)=2\pi\sqrt{L/32}$ — same shape as 6.1's Kepler and 6.0's free-fall models — with
> $L=2,8,18,32$ ft chosen so the fraction reduces to a perfect square and the periods come out exactly
> $\frac\pi2,\pi,\frac{3\pi}2,2\pi$; quadrupling the length only doubles the period (what a $\frac12$
> exponent does), a clockmaker's "just double the length" is refuted, and $\sqrt{L/32}=\sqrt{2L}/8$
> previews rationalizing before the word exists. Standards: **2023 VA SOL A2.EO.2a** (governing) and
> the *additive half* of **A2.EO.2b** — multiply/divide/rationalize are held for 6.3, which is why
> A2.EO.2b splits across the pair — revisiting **A2.EO.2c** as the source of both properties, and
> reaching **A2.F.2f** / previewing **A2.F.1b/c** through the pendulum and the vertical-stretch item.
> Warm-up & exit ticket each fit one page (blank+key); notes 4pp/4pp, activity 3pp/3pp, homework
> 2pp (key 3pp); exit ticket includes an SOL-style MC item ($\sqrt{50}+\sqrt{32}$; distractors =
> added radicands, simplified-then-added-radicands, and multiplied coefficients).
> `make -C unit06/lesson02 all` → EXIT 0 (student 12pp, full 28pp); `make -C unit06 all` → EXIT 0.

- **6.0** Characteristics of radical functions *(introduces: restricted domain from the radicand,
  endpoint behavior, inverse relationship of families; both parents side by side — $y=\sqrt{x}$
  with domain $x\ge0$, an endpoint at the origin, an absolute min, one arm, vs. $y=\sqrt[3]{x}$
  with all reals, origin symmetry, and no extrema)* — A2.F.2a/b/c/d/e/f/g + A2.F.1a/e
- **6.1** $n$th roots & rational exponents *(index, even vs. odd index — why $\sqrt{-16}$ fails but
  $\sqrt[3]{-8}$ does not, principal root, $a^{m/n}=\sqrt[n]{a^m}$, exponent properties on rational
  exponents; the algebraic reason behind 6.0's domain split)* — A2.EO.2c
- **6.2** Simplifying radicals; adding & subtracting *(product/quotient properties, algebraic
  radicands, higher indices, then like-radical collection)* — A2.EO.2a/b
- **6.3** Multiplying & dividing radicals; rationalizing *(distribute/FOIL over radicals;
  **conjugates** for binomial denominators — callback to 3.4's complex conjugates)* — A2.EO.2b
- **6.4** Graphing radical functions & transformations *($y=a\sqrt{x-h}+k$ and
  $y=a\sqrt[3]{x-h}+k$; the endpoint is the transformation anchor; equation→graph and graph→equation
  both directions)* — A2.F.1b/c/e + A2.F.2a
- **6.5** Solving radical equations & extraneous solutions *(isolate → raise to the $n$th power →
  **always check**; extraneous roots explained as squaring destroying sign information — the
  structural echo of 5.6's excluded values; also $x^{m/n}=k$; verified graphically as an
  intersection)* — A2.EI.5a/b/c
- **6.6** Composition of functions *($(f\circ g)(x)$ numerically, graphically, and algebraically;
  order matters; domain of a composition)* — A2.F.2k
- **6.7** Inverse functions *(unit capstone: swap-and-solve, reflection over $y=x$, domain/range
  swap, why $y=x^2$ needs a restricted domain to have a square-root inverse — closes the loop opened
  in 6.0 — verified with 6.6's composition, $f(g(x))=g(f(x))=x$)* — A2.F.2i/j

### Unit 7 — Exponential Functions
> **Status (map confirmed & scaffolded 2026-07-27):** lesson map locked at **6 lessons (7.0–7.5)**,
> grounded against `spec/algebra2-vdoe-sol.pdf`. Two changes from the original ~5-lesson sketch:
> the order was set to characteristics → model form → graphing → solving → modeling → capstone
> (matching the Unit 5/6 shape), and a **new 7.5 (exponential regression & choosing a model)** was
> added because **A2.ST.2's exponential branch is otherwise unaddressed** — Lesson 2.5 covered that
> standard for lines only. All 6 lesson dirs `unit07/lesson00`–`lesson05` scaffolded with skeleton
> `main.tex` for lesson plan + cover, warmup, notes, activity, exit_ticket, homework, slides, and
> each `*_key`. Unit assessments scaffolded: `tests/{practice_test,actual_test}`, `test_keys/`,
> `sample_test{,_key}/`. Skeletons compile (`make -C unit07/lesson00 all` and
> `make -C unit07/lesson04 all` → EXIT 0). **No content authored yet.**
> **Standards coverage — note the shape:** there is **no `A2.EI` standard for exponential
> equations** (the EI strand runs absolute value → quadratic → quadratic systems → rational →
> radical → polynomial and stops), and **no `A2.EO` standard either**. Unit 7 therefore rests
> entirely on **A2.F.1a/b/c/e** (exponential parent + transformations + compare/contrast),
> **A2.F.2a–h** (characteristics; **h** names exponential explicitly for horizontal asymptotes),
> and **A2.ST.2d/e/g** (exponential curve of best fit). This is a genuinely lighter standards load
> than Units 5–6, which is why the unit is 6 lessons rather than 8.
> Lesson 7.0 introduces the one new spine row: ● growth vs. decay / constant ratio, and revisits
> ○ horizontal asymptote (● in U5) now as a **range boundary**.
> **Authoring note:** apply the §7 vocab-box paragraph-break fix in every notes/notes_key.

- **7.0** Characteristics of exponential functions *(introduces: growth vs. decay and the constant
  multiplicative rate / **constant ratio**; revisits the horizontal asymptote as a **range
  boundary**. Growth $y=2^x$ and decay $y=(\frac12)^x$ taught side by side, as Unit 6 did for the
  two radical parents. The escalation reverses: U6 took away half the **domain**, exponential hands
  the domain back and takes half the **range**. First family in the course with **no zeros, ever**;
  no extrema, no turning points; end behavior with two different *kinds* of end — one arm to
  $\infty$, the other flattening onto the asymptote, the mirror of 6.0's "the graph stops". Family
  fingerprint from a table: constant difference (2.0) / constant second difference (3.0) /
  **constant ratio**)* — A2.F.2a/b/c/d/f/g/h + A2.F.1a/e
- **7.1** Exponential growth & decay — building $y=ab^x$ *($a$ = initial value, $b$ = growth factor;
  why $b>0$ and $b\ne1$; the percent↔factor translation ("up 8%" $\Rightarrow b=1.08$; "loses 15%"
  $\Rightarrow b=0.85$) with its two signature errors ($b=0.08$, and $b=1.15$ for a decrease);
  writing the equation from a table, from two points, from a story)* — A2.F.2f, feeding A2.ST.2d/e
- **7.2** Graphing exponential functions & transformations *($f(x)+k$ is the only transformation
  that **moves the asymptote** — and therefore the range; $kf(x)$ moves the $y$-intercept but not
  the HA; $f(x+k)$ and $f(kx)$; reflections carry real content — $f(-x)$ turns growth into decay
  because $2^{-x}=(\frac12)^x$, a 6.1 exponent identity rather than a new rule)* —
  A2.F.1b/c/e + A2.F.2a/h
- **7.3** Solving exponential equations with a common base *(one-to-one property: rewrite both sides
  over one base, equate exponents; runs on Unit 6's machinery — $8^x=4$, $3^x=\frac1{27}$,
  $\sqrt[3]{2}=2^{1/3}$; verified graphically as an intersection)* — **supporting skill, no SOL
  standard**; kept because Unit 8 needs it and it sets up 7.4's wall
- **7.4** Modeling: compound interest, half-life, and $e$ *($A=P(1+\frac rn)^{nt}$ compounded
  annually → quarterly → daily, the limit that **produces $e$**, then $A=Pe^{rt}$; half-life
  $A_0(\frac12)^{t/h}$, doubling time, depreciation. Ends on a deliberate **wall**:
  $2000=1000(1.05)^t$ has no common base — readable off a graph, not yet solvable — which is Unit
  8's opening move, the same device used at 4.2→4.3)* — A2.F.2f/a/h
- **7.5** Exponential regression & choosing a model *(unit capstone: linear vs. quadratic vs.
  exponential from real data — 7.0's fingerprint test applied to a scatterplot — model from
  technology, interpret $a$ and $b$ in context, predict, and an "extrapolation breaks" beat that
  bites far harder on an exponential than it did on 2.5's line)* — A2.ST.2d/e/g + A2.F.2b

### Unit 8 — Logarithmic Functions
> **Status (scaffolded 2026-07-27; Lesson 8.0 authored & building):** locked at
> **7 lessons (8.0–8.6)**. The unit was opened ahead of Units 6–7 at the user's request. So far only
> `unit08/lesson00` has been scaffolded; `lesson01`–`lesson06` still need `new_lesson.py` runs. The
> unit assessments were laid down with the unit (`tests/{practice_test,actual_test}`, `test_keys/`,
> `sample_test{,_key}/`) and are still skeletons. **Lesson 8.0 is
> fully authored**: lesson plan, cover, warm-up, guided notes, activity, exit ticket, homework, a
> 11-frame slide deck, and all five answer keys. `make -C unit08/lesson00 all` → EXIT 0
> (`lesson00_student.pdf` 13 pp, `lesson00_full.pdf` 31 pp); the warm-up and exit ticket each fit
> **exactly one page** in blank *and* key, and notes/notes_key paginate identically at 5 pp. The §7
> vocab-box paragraph-break fix is applied in `notes/` and `notes_key/`. The unit tests and Lessons
> 8.1–8.6 are still to be scaffolded/authored.
>
> **Authoring note for the rest of the unit — the TikZ logarithm macro.** pgfmath has no `log_b`, so
> every logarithmic curve in 8.0 is drawn by *parameterizing on $y$* rather than $x$, which also
> gives a perfectly smooth curve near the asymptote:
> ```latex
> % y = log_b(x-h) + k   <=>   x = b^(y-k) + h.   Args: {b}{h}{k}{ymin}{ymax}
> \newcommand{\logcurve}[5]{\draw[very thick, forest, domain=#4:#5, samples=120, smooth]
>   plot ({pow(#1,\x-(#3))+(#2)},{\x});}
> ```
> Reuse it verbatim in 8.1–8.6. Asymptotes follow the Unit 5 convention:
> `\draw[navy, dashed, semithick]`.
> The map moved twice in one day. It was first cut from a 6-lesson sketch to 5 after a standards
> audit of `spec/algebra2-vdoe-sol.pdf` found **logarithms in only two 2023 VA SOL standards** —
> `A2.F.1` (a/b/c/e) and `A2.F.2` (a–h, i/j) — with **no `A2.EO` standard for log properties and
> no `A2.EI` standard for logarithmic equations** (the same gap Unit 7 documents for exponentials).
> It then grew to 7 when the Unit 7 map landed and three collisions were resolved (below).
>
> **Collisions with Unit 7, resolved 2026-07-27.** Both unit maps were confirmed the same day in
> separate sessions; neither saw the other. Rulings:
> 1. **`A2.ST.2` belonged to Unit 7, not Unit 8.** The standard names the curve of best fit as
>    "linear, quadratic, exponential, or a combination" — **logarithmic is not in the list**, so
>    Unit 8 never had a real claim. **7.5 keeps the regression capstone outright**; the Unit 8
>    modeling lesson was rewritten as **8.5 (natural logs & log scales)** with an `A2.F.2f` anchor.
> 2. **Natural log now has a definite home: 8.5.** Unit 7's ruling assigned $\ln$ to "8.5", which
>    the interim 5-lesson map had deleted; the lesson is restored under that number. $e$ itself
>    stays in **7.4** as the limit of ever-more-frequent compounding, per the Unit 7 ruling.
> 3. **No-standard content is now handled symmetrically.** Unit 7 keeps **7.3** (common-base
>    solving) as a full lesson despite having no SOL standard; Unit 8's **8.4** (solving log &
>    exponential equations) is likewise **restored to a full lesson**, reversing the earlier Tier E
>    demotion. This keeps the promise **7.4** makes — it ends on $2000=1000(1.05)^t$, "no common
>    base … which is Unit 8's opening move" — for every student rather than only in enrichment.
>    **Consequence:** **8.3 (properties of logarithms) had to be promoted out of Tier E as well**,
>    since condensing is a prerequisite for solving $\log x + \log(x-3) = 1$. Both lessons are
>    labelled **beyond-SOL / precalculus prep** and must stay off the SOL-style test items.
>
> **Authoring constraint for 8.2:** `A2.F.1b` limits **graph → equation** for exponential and
> logarithmic functions to a **single transformation**. `A2.F.1c` (equation → graph) carries no such
> cap, so multi-step transformations are fair game in that direction only. *(Unit 7 recorded the
> identical constraint independently — it binds both units.)*
> **Authoring note:** apply the §7 vocab-box paragraph-break fix in every notes/notes_key.

- **8.0** Characteristics of logarithmic functions ***(authored & building 2026-07-27)*** *(the unit's only ● spine row — **inverse of
  exponential, domain/range swap**. Built by reflecting Unit 7's $y=b^x$ over $y=x$: domain $x>0$
  and **why** (the exponential's range becomes the log's domain), range all reals, **vertical
  asymptote $x=0$** — the exponential's horizontal asymptote reflected, revisiting the Unit 5
  asymptote row in a new place — $x$-intercept $(1,0)$ and no $y$-intercept, increasing $b>1$ vs.
  decreasing $0<b<1$, end behavior that grows without bound but slowly, no extrema. Inherits 7.0's
  "no zeros, ever" contrast: the exponential has no $x$-intercept and the log has no $y$-intercept
  — the same fact reflected. $\log_b x$ arrives as the **name of that curve**, not yet as an
  operation — the 6.0-before-6.1 move that let students read $\sqrt{x}$ before meeting rational
  exponents)* — A2.F.2a/b/c/d/e/f/g/h + A2.F.1a/e + A2.F.2i/j
- **8.1** Introduction to logarithms *(log ⇄ exponential form as one statement read two ways — "a
  logarithm **is** an exponent"; evaluating by asking "$b$ to what power?"; common log; the four
  identities $\log_b 1=0$, $\log_b b=1$, $\log_b b^x=x$, $b^{\log_b x}=x$; and **change of base**
  for calculator work. Domain re-derived algebraically — the log of a negative or zero is
  undefined, which is 8.0's $x>0$ restriction arriving a second time by a different road)* —
  supports A2.F.2a/f; the notational foundation the rest of the unit requires
- **8.2** Graphing logarithmic functions & transformations *($y=a\log_b(x-h)+k$, with the
  **vertical asymptote as the transformation anchor** — the structural role the endpoint played in
  6.4 and the vertex in 3.1. Mirrors 7.2 exactly: there, $f(x)+k$ was the only transformation that
  moved the *horizontal* asymptote and therefore the range; here $f(x+k)$ is the only one that moves
  the *vertical* asymptote, and therefore the domain. Respect the single-transformation cap on
  graph → equation)* — A2.F.1a/b/c/e + A2.F.2a/h
- **8.3** Properties of logarithms *(product, quotient, and power; expanding & condensing. Derived
  rather than announced — each property is an exponent law in disguise ($b^m\cdot b^n=b^{m+n}$
  *is* the product rule), the same "insist the old rules survive" move named aloud in 6.1.
  Signature trap: $\log(x+y)\ne\log x+\log y$, killed numerically. Change of base returns as a
  consequence rather than a memorized formula)* — **beyond-SOL / precalculus prep, no standard**;
  kept because 8.4 cannot run without condensing *(same reasoning that kept 7.3)*
- **8.4** Solving logarithmic & exponential equations *(the lesson **7.4's cliffhanger promises**:
  $2000=1000(1.05)^t$ finally falls. One-to-one property; take a log of both sides; condense-then-
  convert for log equations; and **extraneous solutions** — a candidate making any argument $\le 0$
  is rejected, the *third* appearance of that structure after 5.6 (excluded values) and 6.5
  (squaring destroys sign), and the first time the rejection comes from a **domain restriction**
  rather than an algebraic artifact. Verified graphically as an intersection)* — **beyond-SOL /
  precalculus prep, no standard**; kept for the same reason 7.3 was
- **8.5** Natural logarithms & logarithmic scales *($\ln$ as $\log_e$, the inverse of the $e^x$
  introduced in 7.4 — so the 8.0 reflection argument runs once more on a specific base; solving
  continuous-growth models $A=Pe^{rt}$ for time with $\ln$, half-life and doubling time finished
  properly. Then **log scales as the answer to "why did anyone invent this"**: pH, Richter, and
  decibels compress multiplicative ranges into additive ones, so "two points on the Richter scale"
  means a factor of 100, not a difference of 2 — read off pre-drawn scale diagrams and tables)* —
  A2.F.2f *(A2.ST.2 deliberately **not** claimed here — it is 7.5's, see collision 1)*
- **8.6** Comparing function families *(**course capstone**: identify the family from a graph,
  table, or equation across all eight families met since Unit 1; compare domain/range, asymptotes,
  intercepts, symmetry, and end behavior side by side; and settle the "which eventually wins"
  question — linear vs. quadratic vs. exponential vs. logarithmic growth rates off pre-drawn graphs
  and tables, with the exponential-beats-polynomial and log-loses-to-everything results made
  concrete. Extends 7.0's constant-difference / second-difference / constant-ratio fingerprint test
  into a full identification toolkit. Claims the `A2.F.1e` / `A2.F.2b` compare-and-contrast clauses,
  which every unit since 2.0 has applied in passing but no lesson has ever made the teaching
  focus)* — A2.F.1e + A2.F.2b

---

## 5. Assessment structure

Per Unit 1's pattern:
- **Per lesson:** warm-up, exit ticket, homework (each with key).
- **Per unit:** unit cover + sample test + sample test key.
- **Course-level reference exists** in `spec/`: mid-year test and final exam
  (All Things Algebra originals) — usable as models, not for redistribution.

*(Open: mid-year checkpoint placement — natural break after Unit 4.)*

---

## 6. Decisions & remaining open questions

**Resolved:**
- Absolute-value & piecewise functions → **Unit 2**.
- Complex numbers → **Unit 3** (with quadratics); quadratic systems → **Unit 3**.
- Advanced factoring (sum/difference of cubes, two-variable expressions) → **Unit 4**.
- Conic sections, sequences & series, probability & statistics, trigonometry →
  **out of scope** (no material taught).
- Systems of **linear** equations/inequalities & linear programming →
  **out of scope** (omitted). *(Systems of **quadratics** remain in Unit 3.)*
- **Direct/inverse variation → a required Unit 5 lesson (5.7)**, not optional — A2.F.1d has no
  other home in the course. *(Joint variation is not named in the standard; enrichment only.)*
- **Slant/oblique asymptotes → Tier E enrichment in 5.5, never assessed** — A2.F.2h covers
  vertical and horizontal asymptotes only.
- **Unit 5 lesson map → 8 lessons (5.0–5.7)**, splitting graphing into a transformations lesson
  (A2.F.1) and an analyze-and-graph lesson (A2.F.2).
- **Unit 6 lesson map → 8 lessons (6.0–6.7)**, splitting radical operations into 6.2/6.3 and
  composition (6.6) from inverses (6.7).
- **Radical equations capped at one radical** per A2.EI.5a — two-radical equations are Tier E
  enrichment only, never assessed *(same treatment slant asymptotes got in 5.5)*.
- **Cube root gets equal billing with square root** throughout Unit 6 — A2.F.1 and A2.F.2 both name
  the two families explicitly, so 6.0 and 6.4 teach them side by side rather than treating
  $\sqrt[3]{x}$ as an afterthought.
- **Inverse functions & composition → Unit 6 (6.6–6.7)**, not a standalone unit — A2.F.2i/j/k have
  no other home, and the square-root/quadratic pair is the natural motivating example.
- **Unit 7 lesson map → 6 lessons (7.0–7.5)**, not the original ~5 — a regression/model-choice
  capstone (7.5) was added to cover **A2.ST.2's exponential branch**, which Lesson 2.5 handled for
  lines only. The unit stays shorter than 5–6 because exponentials have **no A2.EO and no A2.EI
  standard** at all.
- **Common-base exponential solving (7.3) is kept despite having no SOL standard** — Unit 8's
  logarithmic solving depends on it, and it is what makes 7.4's "no common base exists" wall honest.
- **Exponential transformations given a *graph* are capped at a single transformation** per the
  explicit clause in A2.F.1b. Multi-transformation work is equation→graph and Tier E only *(same
  treatment slant asymptotes got in 5.5 and two-radical equations in 6.5)*.
- **$e$ does not get its own lesson** — it is introduced inside 7.4 as the limit of ever-more-
  frequent compounding, since the standards never name it separately. Natural log stays in 8.5.
- **A2.ST.1 (normal distribution, $z$-scores, Empirical Rule) → out of scope**, confirmed
  2026-07-27. Consistent with the probability & statistics exclusion above; A2.ST.2 remains in
  (Lesson 2.5 for lines, Lesson 7.5 for exponentials). Closed — do not re-raise.

- **Unit 8 lesson map → 7 lessons (8.0–8.6)** *(confirmed 2026-07-27)*. Full rationale in the
  Unit 8 status block in §4.
- **Properties of logarithms (8.3) and solving logarithmic/exponential equations (8.4) are kept as
  full lessons despite having no SOL standard** — the same ruling 7.3 got, applied symmetrically.
  The standards audit found logarithms only in `A2.F.1` and `A2.F.2`: there is **no `A2.EO`
  standard for log properties and no `A2.EI` standard for logarithmic equations**. Both are
  labelled **beyond-SOL / precalculus prep** and must stay **off the SOL-style test items**, but
  they are taught and assessed on the unit test. Keeping 8.4 is what makes 7.4's "no common base"
  cliffhanger honest for every student; keeping 8.3 is forced by 8.4, which cannot run without
  condensing. *(Supersedes the interim ruling that demoted both to Tier E.)*
- **`A2.ST.2` belongs to Unit 7 alone (7.5), not Unit 8** — the standard names the curve of best
  fit as "linear, quadratic, exponential, or a combination"; **logarithmic is not in the list**.
  Unit 8's modeling lesson (8.5) therefore claims `A2.F.2f` and covers $\ln$ and log scales
  instead of regression.
- **Natural log → Unit 8 (8.5)**, consistent with the 7.4 ruling above; $e$ itself stays in 7.4.
- **`A2.F.1e` / `A2.F.2b` (compare & contrast the families) → Unit 8 (8.6)** as an explicit lesson,
  the course capstone. Every unit applied these clauses in passing, but no lesson ever made them
  the teaching focus.

**Still open:**
- **Pacing:** days per lesson / target unit lengths, and how they fit the calendar. **Unit 8 at 7
  lessons is the longest of the back half** — if the calendar is tight, the compression candidate
  is merging 8.1 into 8.3 (intro + properties as one dense lesson), *not* cutting 8.6.
- **`A2.EI.2c` (quadratic inequalities in one variable) is uncovered** — cited by no lesson, and
  Unit 3 is marked complete. Unlike `A2.ST.1` and `A2.ST.3`, which are *knowingly* out of scope per
  the decisions above, this clause was never declared out. Needs a home. See §8.

---

## 7. Conventions

- **Directory:** `unitXX/lessonYY/` with the standard component subfolders
  (`warmup`, `notes`/`slides`, `activity`, `exit_ticket`, `homework`, `cover`,
  plus each `*_key`). Unit-level: `unit_cover`, `sample_test`, `sample_test_key`.
- **Lesson 0 numbering:** the characteristics lesson is `lesson00` in each unit
  (or `X.0` in titles) so content lessons keep 1-based numbers.
- **Build:** `make -C unitXX all`; root `make all` / `make student` / `make full`.
- **Authoring:** use the `lesson-planning` skill.

### Vocab-box paragraph breaks — required from Unit 5 onward

`\termblanklong` (blank) and the key-local `\vocabans` (key) both **open with `\noindent`, which is a
no-op in the middle of a paragraph**, and `\ansline` ends with `\dotfill` but never ends the
paragraph. Left alone, this produces two visible defects in the `vocabbox`:

1. **In the blank:** the intro sentence ("Fill in each term as we build it together.") and the *first*
   term label run together on one line.
2. **In the key:** every term label after the first is pulled onto the end of the *previous* answer's
   dotted line — badly garbled, worse than the blank.

**Do this in every notes/notes_key from Unit 5 on** (Lesson 5.0 is the reference implementation):

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
retrofit below, where the pagination of Units 2–4 can be re-verified in one pass.

---

## 8. Deferred cleanup — do after Unit 8 and the finals are done

Non-blocking issues intentionally postponed so unit authoring keeps moving. **Do not start these until
Units 6–8 and the final exams are complete.**

- [ ] **Give `A2.EI.2c` (quadratic inequalities in one variable, over $\mathbb{R}$, solved
      algebraically) a home.** Cited by no lesson in the course; Unit 3 was marked complete without
      it. Options: a Unit 3 addendum lesson (3.8), a Tier E strand retrofitted into 3.2/3.5, or a
      finals-review lesson. Decide before the final exam is authored — unlike `A2.ST.1`/`A2.ST.3`,
      this clause was never declared out of scope.
- [ ] **Retrofit the vocab-box paragraph-break fix into Units 2, 3, and 4** (§7 above). Affects
      `unit0{2,3,4}/lesson*/notes/main.tex` and `notes_key/main.tex`. All three units currently show
      defect 1, and every Lesson 0 key that defines `\vocabans` (Units 2, 3, 4) shows defect 2.
      Preferred approach once nothing else is in flight: fix `\termblanklong` in
      `shared/algebra2-article.sty` to emit a leading `\par`, add the trailing `\par` to `\ansline` in
      `shared/algebra2-key.sty`, then drop the per-lesson workarounds. **Re-verify after:** every
      warm-up and exit ticket still fits exactly one page (blank *and* key), and each key still
      paginates identically to its blank —
      `pdfinfo target/unitXX/lessonYY/<comp>/main.pdf | grep Pages`.
