#!/usr/bin/env python3
"""Fail when a graded document carries a name line.

A graded component (any main.tex that loads math-shared's grading package) is
scanned and sent to an outside API, so its pages carry only the tracking id.
The student's name goes on math-shared's cover sheet and nowhere else. This
check fails on any graded main.tex that uses a name-line macro
(\\namedateperiod, \\namepartnerperiod) or writes a name line by hand
("Name:", "Name \\underline", "Partner: \\blank", ...).

    python3 shared/check_namelines.py PATH [PATH ...]

Each PATH is a main.tex or a directory searched for main.tex files. Documents
that do not load grading are skipped: they keep their name line. Exit status 1
on any hit, with file:line for each.
"""

import os
import re
import sys

LOADS_GRADING = re.compile(r"\\usepackage\s*(\[[^\]]*\])?\s*\{grading\}")
NAME_LINE = re.compile(
    r"\\name(dateperiod|partnerperiod)\b"
    r"|\b(Name|Partner)\}?\s*(:|\\underline|\\rule|\\hrulefill|\\blank|___)"
)


def strip_comment(line):
    """The line up to its first unescaped %."""
    out = []
    i = 0
    while i < len(line):
        c = line[i]
        if c == "\\" and i + 1 < len(line):
            out.append(line[i : i + 2])
            i += 2
            continue
        if c == "%":
            break
        out.append(c)
        i += 1
    return "".join(out)


def tex_files(paths):
    for p in paths:
        if os.path.isdir(p):
            for root, dirs, files in os.walk(p):
                dirs[:] = sorted(d for d in dirs if not d.startswith("."))
                if "main.tex" in files:
                    yield os.path.join(root, "main.tex")
        elif os.path.isfile(p):
            yield p


def main(argv):
    if not argv:
        print(__doc__.strip())
        return 2
    hits = []
    checked = 0
    for path in tex_files(argv):
        with open(path, encoding="utf-8") as fh:
            lines = [strip_comment(l.rstrip("\n")) for l in fh]
        if not any(LOADS_GRADING.search(l) for l in lines):
            continue
        checked += 1
        for n, line in enumerate(lines, 1):
            if NAME_LINE.search(line):
                hits.append(f"{path}:{n}: {line.strip()}")
    if hits:
        print("!  name line in a graded component (graded pages carry only the tracking id):")
        for h in hits:
            print("   " + h)
        return 1
    print(f"OK  no name line in {checked} graded document(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
