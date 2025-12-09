"""Advent of Code helper script.

Read your puzzle input (defaults to ``input.txt``), then dispatches to
``solve_part_one`` and ``solve_part_two`` for the two puzzle parts.
Fill in the solver functions with the actual logic for the problem of the day.
"""

from __future__ import annotations

from argparse import ArgumentParser, Namespace
from pathlib import Path
from typing import Sequence


def parse_args(argv: Sequence[str] | None = None) -> Namespace:
    parser = ArgumentParser(description="Run Advent of Code solutions for the day.")
    parser.add_argument(
        "input",
        nargs="?",
        default="input.txt",
        help="Path to the puzzle input (defaults to %(default)s)",
    )
    return parser.parse_args(argv)


def load_data(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8").rstrip("\n")
    return text.splitlines()

def translate_to_coords(lines: list[str]) -> list[(int,int)]:
    result = []
    for line in lines:
        result.append(tuple(map(int, line.split(","))))
    return result

def solve_part_one(lines: list[str]) -> int:
    coords = translate_to_coords(lines)
    areas = []

    for i in range(len(coords)-1):
        for j in range(1, len(coords)):
            (ix,iy) = coords[i]
            (jx,jy) = coords[j]
            area = (abs(ix-jx)+1) * (abs(iy-jy)+1)
            areas.append(area)

    return sorted(areas, reverse=True)[0]


def solve_part_two(lines: list[str]) -> int | str:    
    pass


def main(argv: Sequence[str] | None = None) -> None:
    args = parse_args(argv)
    data = load_data(Path(args.input))

    part_one = solve_part_one(data)
    print(f"Part 1: {part_one}")

    part_two = solve_part_two(data)
    print(f"Part 2: {part_two}")


if __name__ == "__main__":
    main()
