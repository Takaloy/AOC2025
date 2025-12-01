"""Entrypoint for running Advent of Code 2025 Day 1 solutions."""

from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    """Build and parse the CLI arguments."""
    parser = argparse.ArgumentParser(description="Run Advent of Code solutions")
    parser.add_argument(
        "input",
        nargs="?",
        default="input.txt",
        help="Path to the puzzle input (defaults to input.txt)",
    )
    return parser.parse_args()


def read_input(path: str) -> list[str]:
    """Load the puzzle input and return the lines."""
    try:
        return Path(path).read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        sys.exit(f"Input file not found: {path}")


def solve_part_one(lines: list[str]) -> int:
    """Solve part one of the puzzle."""
    position = 50
    clicks = 0
    print(f"The dial starts by position {position}")
    for line in lines:
        direction = line[0]
        distance = int(line[1:])
        if direction == 'R':
            position = (position + distance) % 100
        elif direction == 'L':
            position = (position - distance) % 100
            if (position < 0):
                position += 100
        print(f"After moving {line}, the dial is at position {position}")
        if (position == 0):
            clicks += 1
            print(f"  Click! Total clicks: {clicks}")
    return clicks


def solve_part_two(lines: list[str]) -> int:
    """Solve part two of the puzzle."""
    position = 50
    clicks = 0

    print(f"The dial starts by position {position}")
    for line in lines:
        direction = line[0]
        distance = int(line[1:])
        if direction == 'R':
            position = (position + distance)
            while (position >= 100):
                clicks += 1
                position -= 100
        elif direction == 'L':
            starting_position = position
            position = (position - distance)
            
            if (position < 0 and starting_position == 0):
                clicks -= 1

            while (position < 0):
                clicks += 1
                position += 100
        
        
            if position == 0:
                clicks += 1    


        print(f"After moving {line}, the dial is at position {position}")
        print(f"  Click! Total clicks: {clicks}")

    return clicks


def main() -> None:
    args = parse_args()
    lines = read_input(args.input)

    part_one = solve_part_one(lines)
    part_two = solve_part_two(lines)

    print(f"Part 1: {part_one}")
    print(f"Part 2: {part_two}")


if __name__ == "__main__":
    main()
