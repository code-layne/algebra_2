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

## Downloading Prebuilt PDFs

> Coming soon — versioned releases for each unit will be available on the [Releases](../../releases) page.

## License

TBD
