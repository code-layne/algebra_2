#!/usr/bin/env python3
"""Write fake-roster.csv: an invented 12-student class in the roster-map format.

Every name here is made up for the synthetic eval set; none belongs to a real
student. roster_import.py refuses to write inside a git work tree (a real
roster-map.csv must never be committed), so this fake one is written by this
script instead. Tracking ids come from a fixed seed, so rerunning it rewrites
the same file.

    python3 make_fake_roster.py
"""

import csv
import random
from pathlib import Path

ALPHABET = "ABCDEFGHJKMNPQRSTUVWXYZ23456789"  # roster_import.py's: no 0/O/1/I/L
SECTION = "Algebra 2 - Sample"

# (legal name "Last, First", preferred name, class year)
STUDENTS = [
    ("Arden, Juniper", "June", 2028),
    ("Bellweather, Tamsin", "Tamsin", 2028),
    ("Castellane, Odette", "Detta", 2027),
    ("Delacorte-Vey, Imogen", "Imogen", 2028),
    ("Ellisworth, Marisol", "Marisol", 2028),
    ("Fairbourne, Wren", "Wren", 2028),
    ("Galloway-Prue, Sabine", "Bina", 2027),
    ("Halvorsen-Teague, Liesl", "Liesl", 2028),
    ("Ingleby, Rosalind", "Roz", 2028),
    ("Jessamyn, Coralie", "Coralie", 2028),
    ("Kittredge-Moss, Anouk", "Anouk", 2027),
    ("Larkspur, Delphine", "Del", 2028),
]


def main():
    rng = random.Random(3101)
    ids = set()
    rows = []
    for legal, preferred, year in STUDENTS:
        while True:
            tid = "".join(rng.choice(ALPHABET) for _ in range(6))
            if tid not in ids:
                ids.add(tid)
                break
        rows.append({"tracking_id": tid, "legal_name": legal, "preferred_name": preferred,
                     "class_year": year, "section": SECTION})
    out = Path(__file__).resolve().parent / "fake-roster.csv"
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows)} invented students -> {out}")


if __name__ == "__main__":
    main()
