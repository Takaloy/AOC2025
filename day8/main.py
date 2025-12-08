#!/usr/bin/env python3
"""Advent of Code 2025 Day 8 runner."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence
import math
from disjoint_set import DisjointSet


def parse_args() -> argparse.Namespace:
    """Build the command-line interface."""
    parser = argparse.ArgumentParser(
        description="Run Advent of Code Day 8 solutions against an input file.",
    )
    parser.add_argument(
        "input_file",
        nargs="?",
        default=Path("input.txt"),
        type=Path,
        help="Path to the puzzle input (default: input.txt).",
    )
    return parser.parse_args()


def load_input(path: Path) -> list[str]:
    """Read the raw puzzle input."""
    try:
        raw = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise SystemExit(f"Input file not found: {path}") from exc
    return raw.splitlines()


def parse_input(lines: Sequence[str]) -> Sequence[str]:
    """Transform the raw lines into the structure the solver expects."""
    return lines


def _sorted_distances(data: Sequence[str]) -> dict[float, tuple[int, int]]:
    """Return pairwise distances sorted ascending by their value."""
    distances: dict[float, tuple[int, int]] = {}

    for i in range(0, len(data) - 1):
        for j in range(i + 1, len(data)):
            val = (i, j)
            p1 = tuple(map(int, data[i].split(',')))
            p2 = tuple(map(int, data[j].split(',')))
            key = math.dist(p1, p2)  # hoping float distances stay unique
            distances[key] = val

    return dict(sorted(distances.items(), key=lambda x: x[0]))


def part_one(data: Sequence[str]) -> int:
    """Solve Part 1 of the puzzle."""

    sorted_distances = _sorted_distances(data)

    ds = DisjointSet(1000)
    for (_, value) in list(sorted_distances.items())[:1000]:
        (i,j) = value
        ds.union(i,j)

    # collect all sizes where index is a root
    sizes = [ds.set_size(i) for i in range(len(ds.parent)) if ds.parent[i] == i]

    return math.prod(sorted(sizes, reverse=True)[:3])


def part_two(data: Sequence[str]) -> int:
    """Solve Part 2 of the puzzle."""
    length = len(data)
    sorted_distances = _sorted_distances(data)

    ds = DisjointSet(length)

    answer = 0

    for (_, value) in list(sorted_distances.items()):
        (i,j) = value
        ds.union(i,j)

        parent = ds.find(i)
        if (ds.set_size(parent) == length):
            p1 = tuple(map(int, data[i].split(',')))
            p2 = tuple(map(int, data[j].split(',')))
            answer = p1[0] * p2[0]
            break

    return answer


def main() -> None:
    args = parse_args()
    raw_lines = load_input(args.input_file)
    parsed = parse_input(raw_lines)

    part1_answer = part_one(parsed)
    part2_answer = part_two(parsed)

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


if __name__ == "__main__":
    main()
