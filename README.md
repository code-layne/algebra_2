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
| `binder_cover/` | the binder cover sheet — generated, leads both packets |
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

## Binder Covers

`shared/cover.py` generates a unit's binder cover sheet — a two-page letter PDF (front and back
of the binder, the same sheet twice) whose background art is built from that unit's own lessons.
A unit opts in by having a `binder_cover/` directory, and the cover leads both packets.

```bash
mkdir unitXX/binder_cover        # opt the unit in
make -C unitXX binder_cover      # draw it, if it does not exist yet
```

**The cover is drawn once and then left alone.** `binder_cover/main.pdf` is a committed artifact,
so `make` creates it only when it is *absent* — editing a lesson never silently redraws the
cover. When you do want it caught up with the unit's current content, ask for it:

```bash
make -C unitXX clean_unit_cover  # throw the cover away and draw a new one
```

With no further work the art is auto-discovered from the unit's lesson sources. To compose it by
hand instead, add a `unitXX/binder_cover/spec.py` listing the elements and where they sit — see
[`unit01/binder_cover/spec.py`](unit01/binder_cover/spec.py) for a worked example.

### Extra requirements

The cover generator needs two things beyond the build requirements above. **Neither is in the
repo, and nothing else in the build depends on them** — the rest of `make` works without them.

**1. `cairosvg`**, for the SVG → PDF conversion:

```bash
python3 -m pip install --user cairosvg
```

Homebrew's Python refuses a plain install under [PEP 668](https://peps.python.org/pep-0668/); add
`--break-system-packages` alongside `--user` if so, which writes to your user site and leaves the
Homebrew prefix alone. `cairosvg` needs the native `cairo` library (`brew install cairo`).

**2. Five TeX OpenType fonts**, installed where the OS font service can see them. They ship with
TeX Live but live inside the TeX tree, which the OS font service does not read:

```bash
for f in lmroman10-regular.otf lmroman10-italic.otf latinmodern-math.otf \
         texgyretermes-regular.otf texgyrechorus-mediumitalic.otf; do
  cp "$(kpsewhich "$f")" ~/Library/Fonts/
done
```

On Linux use `~/.local/share/fonts/` and run `fc-cache -f` afterwards.

Preflight both before building:

```bash
python3 shared/cover.py --check-fonts
```

A missing font is reported but is *not* fatal to a build — the cover still generates, silently
substituting system faces. Run the check rather than trusting a clean `make`.

## Downloading Prebuilt PDFs

> Coming soon — versioned releases for each unit will be available on the [Releases](../../releases) page.

## License

TBD
