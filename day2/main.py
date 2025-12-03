"""Entry point for Advent of Code 2025 Day 2 exercises."""

from __future__ import annotations

from part1 import Part1
from part2 import Part2

def main() -> None:
    """Run the Day 2 solution."""
    try:
        with open("textinput.txt", "r", encoding="utf-8") as handle:
            content = handle.read().strip()
    except FileNotFoundError as exc:
        raise SystemExit("Missing textinput.txt input file.") from exc

    if not content:
        raise SystemExit("textinput.txt is empty.")

    ranges: list[tuple[str, str]] = []
    for part in content.split(","):
        a, b = part.split("-")
        ranges.append((a, b))


    solver1 = Part1()
    solver2 = Part2()
    print("Part 1:", solver1.solve_from_ranges(ranges))
    print("Part 2:", solver2.solve_from_ranges(ranges))


if __name__ == "__main__":
    main()
