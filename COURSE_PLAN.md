# Algebra 2 — Course Scope & Sequence

**Course:** Algebra 2: Shepherd · **School year:** 2026–2027

> **Status:** Unit 1 is built in source. **Units 2 and 3 are content-complete** — every lesson
> (plan, cover, warm-up, notes, activity, exit ticket, homework, all keys, and a slide deck) plus the
> unit tests (practice + actual and both keys, with the practice pair published to `sample_test/` +
> `sample_test_key/`). **Unit 4 is in progress:** all 7 lesson dirs scaffolded and assessments
> scaffolded; **4.0 and 4.1 are authored and building**; 4.2–4.6 and the Unit 4 tests remain.
> Units 5–8 are planned here and not yet scaffolded. Lesson lists below are proposals to react to and
> edit — pacing (days per lesson) is intentionally left open pending the school calendar.

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
| 4 | Polynomial Functions | Polynomial | 7 | **In progress (4.0–4.1 built)** |
| 5 | Rational Functions | Rational | ~6 | Planned |
| 6 | Radical Functions | Radical / power | ~5 | Planned |
| 7 | Exponential Functions | Exponential | ~5 | Planned |
| 8 | Logarithmic Functions | Logarithmic | ~5 | Planned |

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
| **Asymptotes (horizontal / slant)** | | | | | ● | | ○ | |
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
> **Next action: author Lesson 4.2 (Advanced Factoring).**
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
- **5.0** Characteristics of rational functions *(introduces: vertical &
  horizontal/slant asymptotes, holes/removable discontinuity, domain restrictions)*
- **5.1** Simplifying rational expressions
- **5.2** Multiplying & dividing rational expressions
- **5.3** Adding & subtracting rational expressions
- **5.4** Graphing rational functions
- **5.5** Solving rational equations (incl. extraneous solutions)
- *(Optional: direct/inverse/joint variation)*

### Unit 6 — Radical Functions
- **6.0** Characteristics of radical functions *(introduces: restricted domain
  from radicand, endpoint behavior, inverse relationship to power functions)*
- **6.1** nth roots & rational exponents
- **6.2** Simplifying & operations with radical expressions
- **6.3** Graphing radical functions & transformations
- **6.4** Solving radical equations (incl. extraneous solutions)
- **6.5** Inverse functions & composition
  *(natural home — radicals are inverses of power functions)*

### Unit 7 — Exponential Functions
- **7.0** Characteristics of exponential functions *(introduces: horizontal
  asymptote as range boundary, growth vs. decay, constant multiplicative
  rate/constant ratio)*
- **7.1** Exponential growth & decay
- **7.2** Graphing exponential functions & transformations
- **7.3** Modeling: compound interest, half-life, population
- **7.4** Solving exponential equations (common base)

### Unit 8 — Logarithmic Functions
- **8.0** Characteristics of logarithmic functions *(introduces: vertical
  asymptote revisited, inverse-of-exponential domain/range swap, domain restriction)*
- **8.1** Introduction to logarithms (log ⇄ exponential form)
- **8.2** Graphing logarithmic functions & transformations
- **8.3** Properties of logarithms
- **8.4** Solving exponential & logarithmic equations
- **8.5** Modeling with logarithms (natural log, applications)

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

**Still open:**
- **Pacing:** days per lesson / target unit lengths, and how they fit the calendar.

---

## 7. Conventions

- **Directory:** `unitXX/lessonYY/` with the standard component subfolders
  (`warmup`, `notes`/`slides`, `activity`, `exit_ticket`, `homework`, `cover`,
  plus each `*_key`). Unit-level: `unit_cover`, `sample_test`, `sample_test_key`.
- **Lesson 0 numbering:** the characteristics lesson is `lesson00` in each unit
  (or `X.0` in titles) so content lessons keep 1-based numbers.
- **Build:** `make -C unitXX all`; root `make all` / `make student` / `make full`.
- **Authoring:** use the `lesson-planning` skill.
