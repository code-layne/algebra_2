# Algebra 2 Curriculum

A LaTeX-based curriculum for Algebra 2, organized by unit and lesson. Includes slides, notes, activities, homework, exit tickets, and answer keys — all built from source into print-ready PDFs.

## Structure

Each lesson lives in `unitXX/lessonYY/`. Its lesson plan is the directory's own `main.tex`, and
each component is a subdirectory with its own `main.tex`:

- `cover` (lesson cover sheet)
- `warmup` / `warmup_key`
- `notes` / `notes_key`
- `activity` / `activity_key`
- `exit_ticket` / `exit_ticket_key`
- `homework` / `homework_key`
- `slides` (Beamer deck, no key)

## Work products

Every lesson builds **five files** into `target/compiled/unitXX/`:

| File | What it is |
| --- | --- |
| `lessonYY_plan.pdf` | the teacher-facing lesson plan |
| `lessonYY_slides.pdf` | the Beamer deck |
| `lessonYY_slides.pptx` | the same deck for PowerPoint, one page image per slide |
| `lessonYY_student.pdf` | cover + blank components, numbered packet-wide, components start recto |
| `lessonYY_key.pdf` | that packet answered, page for page with the student copy |

Units aggregate only the two packets, into `target/compiled/unitXX_{student,key}.pdf`.

A unit may also carry bookend components of its own, merged around the lessons:

| Directory | What it is |
| --- | --- |
| `unit_cover/` | the unit overview page (`main.tex`) |
| `sample_test/`, `sample_test_key/` | prefab PDFs, merged at the end |

## Getting the source

`math-shared/` is a git submodule, [code-layne/math-shared](https://github.com/code-layne/math-shared),
which holds the grading package shared across the courses. It sits at the project root, not under
`shared/`: the build searches `shared/` recursively, and `math-shared/examples` holds `main.tex`
files a component build would pick up. Clone with it:

```bash
git clone --recurse-submodules https://github.com/code-layne/algebra_2
```

In a clone made without `--recurse-submodules`, run `git submodule update --init` once. Ordinary
builds still work without the submodule. Only the grading targets below need it.

## Building from Source

Requires [XeLaTeX](https://tug.org/xetex/), `latexmk`, `poppler` (`pdfunite`, `pdftoppm`,
`pdfinfo`), and `python3`.

```bash
make -C unit01/lesson02 all   # all five work products for one lesson
make -C unit01 student key    # merge a whole unit
make all                      # build every unit
make student key              # merge the whole curriculum
```

Per-lesson targets `plan`, `slides`, `pptx`, `student`, and `key` build one product each. Output
lands in `target/`.

### Graded components

A component that loads `grading` (from `math-shared/grading.sty`) marks its graded answers with
`\gradedblank`. Each page then carries corner registration marks, a QR code, and a name strip.
Write each `\gradedblank` line identically in the blank and the key. The key prints the
answer inside the box (`algebra2-key` turns this on whenever a document loads `grading`). See
`math-shared/README.md` for the macros and `math-shared/grading-system-design.md` for the
plan.

```bash
make -C unit03/lesson01 manifest COMP=exit_ticket
make -C unit03/lesson01 roster-packets COMP=exit_ticket ROSTER=~/Rosters/algebra2/roster-map.csv
```

- **`manifest`** builds the component and its key, writes
  `target/unitXX/lessonYY/grading/<COMP>/manifest.json`, and checks that the blank and key
  agree on every graded item.
- **`roster-packets`** builds one copy of the lesson's student packet per student, in roster
  order. Each copy has that student's personalized component (her tracking id in the QR codes,
  her name in the strip) in place of the master. It is paginated exactly like `make student` and
  joined into `target/compiled/unitXX/lessonYY_<COMP>_roster.pdf`, to print as one collated
  job. Add `SECTION=…` to build one section.
- **`graded`** (`COMP=…`) is `manifest`, then copies the blank and key PDFs to
  `target/compiled/`. It is for a graded component kept out of the packets.

`roster-map.csv` pairs names with tracking ids. Keep it outside every repository, for example
in `~/Rosters/algebra2/`. Roster packets carry names, but they live under `target/`, which is
never committed.

`unit03/lesson01/graded_sample/` is a one-page graded quiz kept out of the packets
(`make -C unit03/lesson01 graded_sample`). Its `eval/` directory holds a synthetic scanned class
set: 12 invented students, with expected scores, rebuilt with `make -C unit03/lesson01
graded_sample_eval`.

## Downloading Prebuilt PDFs

> Coming soon — versioned releases for each unit will be available on the [Releases](../../releases) page.

## License

TBD
