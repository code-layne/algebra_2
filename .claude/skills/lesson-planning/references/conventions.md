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

## Answer-key macros (from `-key`)

| Macro / env | Effect |
| --- | --- |
| `\ans{text}` | Inline answer in bold `keyred`; use in place of a blank |
| `\ansline{text}` | Bold `keyred` answer that fills a write-line with a dotted trail |
| `teachernote` (env) | Red "Teacher Note" callout for teacher-only guidance |

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
