# Conventions

Extracted from the `shared/algebra2-*.sty` packages. The live project is always the source of
truth — if the styles diverge from this, follow the styles.

## Style packages

| Package | Purpose | Required by |
| --- | --- | --- |
| `algebra2-colors` | Color palette (loads `xcolor`) | everything |
| `algebra2-article` | Article preamble: geometry, lists, fill-in helpers, page header, name rows | student components |
| `algebra2-boxes` | All `tcolorbox` environments | components + lesson plan |
| `algebra2-key` | Answer macros + teacher note; requires `-boxes` | answer keys |
| `algebra2-beamer` | Slide theme (`\forestheader{}`, `\sectionlabel[color]{}`) | `slides/` |

## Per-document-type preambles

**Student component** (warmup, notes, activity, exit_ticket, homework, cover):
```latex
\documentclass[10pt]{article}
\usepackage{algebra2-article}
\usepackage{algebra2-boxes}
% cover and some components also: \usepackage{ltablex}\keepXColumns
```

**Answer key** (the matching `_key` directory):
```latex
\documentclass[10pt]{article}
\usepackage{algebra2-article}
\usepackage{algebra2-key}     % pulls in -boxes; do NOT also load -boxes
```

**Lesson plan** (`main.tex` at the lesson root): loads `-boxes` and **defines the course/unit/
lesson macros inline** — this course does not define them in `shared/`:
```latex
\newcommand{\CourseName}{Algebra 2: Shepherd}
\newcommand{\SchoolYear}{2026--2027}
\newcommand{\MeetingLength}{...}   % if the plan uses it
\newcommand{\UnitNumberName}{Unit X: ...}
\newcommand{\LessonNumberName}{Lesson X.Y: ...}
```
The lesson plan also loads a richer set of packages directly (`graphicx` with
`\graphicspath{{images/}}`, `tabularx`, `multicol`). The `\TallMath` helper for tall inline math
is defined per-document where needed:
```latex
\newcommand{\TallMath}[1]{$\displaystyle #1\rule[-1.4em]{0pt}{3.2em}$}
```

**Unit test / test key** (`tests/*/main.tex`, `test_keys/*/main.tex`): same preambles as a
component / key, plus a local `\parthead{...}` macro that draws a `headlinebox{forest}` part
divider. The scaffolder writes these; see `assets/skeletons/test.tex`.

## Fill-in helpers (from `-article`)

| Macro | Effect |
| --- | --- |
| `\blank{width}` | Underlined gap of the given width (e.g. `\blank{4.8cm}`) |
| `\writeline` | A full-width gray rule to write on |
| `\writelines{n}` | `n` stacked write-lines |
| `\termblank{Term}` | Bold forest term + inline blank, then a write-line |
| `\termblanklong{Term}` | Bold forest term on its own line + two write-lines (vocab style) |
| `\namedateperiod` | Name / Date / Period row — **cover and unit tests only** (Namestrip) |
| `\namepartnerperiod` | Name / Partner / Period row — **not used**; superseded by Namestrip |
| `\pageheader{Unit X, Lesson Y.Z}{Document Type}` | Full-width forest banner header |

**`\noindent` trap — required fix in every `vocabbox` from Unit 5 on.** `\termblanklong` opens with
`\noindent`, which is a **no-op mid-paragraph**, and `\ansline` ends with `\dotfill` without ending the
paragraph. Unfixed, the intro sentence and the first term collide in the blank, and in the key every
term label after the first is dragged onto the previous answer's dotted line. So:

```latex
% notes/main.tex
Fill in each term as we build it together.
\par\vspace{2pt}                 % \par is REQUIRED here
\termblanklong{First term}

% notes_key/main.tex — \par on BOTH ends
\newcommand{\vocabans}[2]{%
  \par\noindent\textbf{\textcolor{forest}{#1:}}\\[1pt]\ansline{#2}\par}
```

`unit05/lesson00` is the reference implementation. Fix it per-lesson, **not** in `shared/` — a
shared-package change re-flows every already-verified unit at once. See `COURSE_PLAN.md` §7 and the
deferred Units 2–4 retrofit in §8.

## Box environments (from `-boxes`)

Lesson-plan boxes have a **forest** frame and take a background color as the last argument
(use the aliases `goldbox`, `forestbox`, `redbox`, or palette colors like `forestbg`):
```latex
\begin{skillbox}[Priority Ideas \& Skills]{goldbox} ... \end{skillbox}   % breakable
\begin{fixedskillbox}[Spiral Review]{forestbg} ... \end{fixedskillbox}   % no page break
```

Titled student boxes (title is fixed by the environment unless it takes an argument):

| Environment | Title / use | Arg |
| --- | --- | --- |
| `objectivebox` | "Primary Objective" | — |
| `learningtargetbox` | "Learning Targets — I Can…" (cover sheet) | — |
| `vocabbox` | "Vocabulary & Key Concepts" (navy accent) | — |
| `hookbox` | "Hook" | — |
| `notesbox{Title}` | generic titled notes section | title |
| `practicebox` | "Guided Practice" | — |
| `spiralbox` | "Connections & Big Ideas" | — |
| `scenariobox[Title]{color}` | activity/homework scenario | title, color |
| `headlinebox{color}` | colored callout strip (content in the body) | color |
| `blurbbox[Title]{color}` | study/excerpt blurb | title, color |
| `reflectionbox` | "Reflection" (homework) | — |
| `extensionbox` | "Extension — optional" | — |
| `tocbox` | "What's in This Packet" (cover) | — |
| `remindbox` | "Keep in Mind" (cover / practice-test intro) | — |

## The work rule — `\begin{work}` (from `-boxes`, visible under `-key`)

**Any worked solution goes in a `work` block, and that block is byte-identical in the blank and
the key.** The package swap decides only whether it is shipped: under `-boxes` the blank builds
the box and emits a `\vphantom` of it (exact height, nothing on the page and nothing in the PDF's
text layer); under `-key` the same box is printed in `keyred`. The two therefore *cannot* drift —
which is what keeps a component the same length on both sides.

```latex
% notes/main.tex AND notes_key/main.tex — the same six lines in both files
\begin{work}
  3(x-2) &= 3x-5 \\
    3x-6 &= 3x-5 \\
      -6 &= -5
\end{work}
```

Format, non-negotiable:

- **One statement per line.** Never two steps on one row, and never an inline
  `a=b \Rightarrow c=d` chain — that is the idiom this rule replaces.
- **The `&` goes immediately before the relation**, so every relation in the block lands in one
  column. This works for `=`, `<`, `>`, `\le`, `\ge` — including a line where the symbol reverses.
- **Simplifying:** row 1 is the original expression, the relation, and the first simplification;
  every later row starts at the `&=` and aligns to the one above.
- **Solving:** one row per step, each aligned on its relation.

Do not wrap a `work` block in `\[ \]`, `align`, or `equation` — it supplies its own display. It is
set flush left (2em indent), not centered.

**When it applies:** a task that asks for multi-step work. A table cell holding a single final
answer is already the same size in both files — leave those as `\blank{}`/`\ans{}`. `work` blocks
do not go inside table cells; if a table asks for real work, pull the items out of the table.

`\workrowsep` (default `0pt`) adds leading between rows. It moves the blank and the key together,
so raising it for handwriting room can never break the match.

`unit01/lesson02` is the reference implementation.

### `steptable` / `\step` — a *printed* solution, aligned on its relation

`work` is for steps the **student** writes. Its counterpart is for steps that are **printed in
both files** — the "justify every line" tables, where the algebra is given and the student names
the property beside it. Same alignment requirement, different mechanism: a plain one-column table
cannot align relations (`$3x-12=18$` above `$3x-12+12=18+12$` puts the two `=` in different
places), so the step is split into a right-aligned left side and a left-aligned relation + right
side.

```latex
\begin{steptable}                       % or [Property] to retitle column 3
  \step{3(x-4)}{=18}{Given}
  \step{3x-12}{=18}{\blank{6.0cm}}
  \step{3x-12+12}{=18+12}{\blank{6.0cm}}
\end{steptable}
```

Argument 2 begins with the relation. Use `\steprel{lhs}{cell}{prop}` when the *relation itself* is
what the student supplies — the flip demonstration, where the symbol turning around is the point:
`\steprel{\dfrac{-3x}{-3}}{\blank{0.9cm} $\dfrac{12}{-3}$}{\blank{6.0cm}}`.

Only column 3 differs between the blank and the key, so the two cannot drift.

**It is a chain rule.** A table of *independent* statements to classify — Lesson 1.0's exit ticket
item 2, where one row is `$2x-9=5 \Rightarrow 2x-9+9=5+9$` — is a list, not a solution, and stays
a plain table.

`unit01/lesson00` is the reference implementation.

## Teacher notes — in the lesson plan, one per component

**Teacher-only prose goes in the lesson plan, never in a `_key`.** A `teachernote` is the one block
in a key with no counterpart in the blank, so it made the key run longer than its blank for no
student-facing reason — the last thing costing a packet blank pages once the work rule is in.

The lesson plan closes with one note per component, in packet order, each titled for it:

```latex
\begin{teachernote}[Warm-Up]        ... \end{teachernote}   % → "Teacher Note: Warm-Up"
\begin{teachernote}[Guided Notes]   ... \end{teachernote}
\begin{teachernote}[Group Activity] ... \end{teachernote}
\begin{teachernote}[Exit Ticket]    ... \end{teachernote}
\begin{teachernote}[Homework]       ... \end{teachernote}
```

The environment is defined in **`-boxes`** (the lesson plan does not load `-key`) and the argument
is **optional** — a bare `\begin{teachernote}` still renders plain "Teacher Note", so lessons not
yet migrated keep compiling. To migrate one:

```bash
python3 .claude/skills/lesson-planning/scripts/movenotes.py unit01/lesson02
```

It lifts the note out of each `_key`, appends it to the plan with the right title, and refuses to
run twice on the same lesson. Add `--check` to report without changing anything. Rebuild
afterward and confirm every component matches its key page for page.

## Answer-key macros (from `-key`)

| Macro / env | Effect |
| --- | --- |
| `\ans{text}` | Inline answer in bold `keyred`; use in place of a blank |
| `\ansline{text}` | Bold `keyred` answer that fills a write-line with a dotted trail |
| `work` (env) | Worked steps — **defined in `-boxes`**, authored identically in both files; see "The work rule" |

**`teachernote` is no longer a key macro.** It lives in `-boxes` and belongs in the **lesson
plan** — see "Teacher notes" below.

**`\ansline` is the other place lengths drift.** A `\writeline` in the blank is exactly one line;
an `\ansline` whose prose wraps to four is three lines longer. When a key's prose answer runs long,
give the blank `\writelines{n}` for the same n — the same principle as the work rule, applied by
hand because prose cannot be measured from a shared body.

**`\writelines{n}` occupies n+1 line slots** — it ends in `\\`, so `\writelines{3}` takes four
lines' worth of room. Raising one is *not* free: on Unit 2 Lesson 2.3 a `{2}` → `{3}` raise
overflowed the blank to 3pp against a 2pp key and had to be reverted. Set n from the key's true
wrapped length, then rebuild and re-measure the **blank** before moving on.

**Reach for `work` before `\writelines`.** If the answer is a multi-step solve rather than prose, a
`work` block fixes the drift correctly and cannot come apart; a lengthened write-line only papers
over it. On Lesson 2.2 every apparent `\ansline` drift turned out to be a solve, so the lesson
needed 16 `work` blocks and zero `\writelines` changes.

**Key-authoring rule:** copy the blank component verbatim, then replace each blank/`\writeline`
with `\ans{…}`/`\ansline{…}` and mark correct multiple-choice options, e.g.
`\textcolor{keyred}{\textbf{$\leftarrow$ correct}}`. `\ans` is **text-mode** — never place it
inside `$...$` (wrap math fragments instead: `\ans{$\sqrt{n}$}`) and never let it span a blank
line. The key and blank must stay structurally identical so they paginate the same way.

## Color palette (from `-colors`)

**Forest-green based.** Primary accent (frames, page headers, banners, slide titles):
`forest` (#1E5631), with `forestlight`, `forestbg` (pale green background), `forestmid`.
Secondary accent — used by the **vocabulary** box and related callouts: `navy` (#1F3A5F),
`navylight`, `sky` (pale blue background), `skymid`. Other accents: `goldacc`/`goldbg`/`hookbg`
(gold), `redbg`/`redacc` (red), `greenbg`/`greenacc` (generic green swatch), `charcoal`,
`slate`, `linegray`, `keyred` (#CC0000). Lesson-plan background aliases: `goldbox`,
`forestbox`, `greenbox`, `redbox`.

## Lesson-plan section order (canonical)

Primary Objective → Priority Ideas & Skills → Vocabulary, Concepts & Theorems → Activate
Prior Knowledge & Spiral Review (embeds the warm-up thumbnail) → Hook → Lesson (and
"Lesson (cont.)") → Explicit Instruction (one box per technique) → Active Monitoring →
Group Work & Differentiation (Tiers R / A / E) → Individual Work & Assessment (Exit Ticket +
SOL-style MC) → Reinforcement & Extension (Homework + Extension + Preview). See
`references/components.md` for the full spec and `references/course-workflow.md` for where
content comes from.
