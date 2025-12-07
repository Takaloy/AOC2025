#!/usr/bin/env python3
"""Advent of Code runner for the current day."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable
import bisect


def add_unique(sorted_list, val):
    pos = bisect.bisect_left(sorted_list, val)
    if pos == len(sorted_list) or sorted_list[pos] != val:
        bisect.insort(sorted_list, val)


def parse_input(raw: str) -> list[str]:
    """Return cleaned puzzle input lines."""
    return [line.strip() for line in raw.splitlines() if line.strip()]


def part_one(data: Iterable[str]) -> int:
    
    pos = data[0].index("S")
    splitter_positions = [pos]
    length = len(data[0])
    printable = [data[0]]
    splitted_count = 0

    for line in data[1:]:
        new_splits = splitter_positions.copy() #create a modifyable copy so you don't go into an infinite loop

        # printables
        lineList = list(line)


        for split_index in splitter_positions:
            if (line[split_index]) == "^":
                if (split_index != 0):
                    add_unique(new_splits, split_index-1)
                if (length-1 != split_index):
                    add_unique(new_splits, split_index+1)
                splitted_count+=1
                new_splits.remove(split_index)
            else:
                lineList[split_index] = "|"
        splitter_positions = new_splits #replace it for the next line

        printable.append("".join(lineList))
    return splitted_count

def part_two(data: Iterable[str]) -> int:
    
    pos = data[0].index("S")

    grid = data
    rows, cols = len(grid), len(grid[0])

    # ways[r][c] = number of ways to reach cell (r, c)
    ways = [[0] * cols for _ in range(rows)]
    ways[0][pos] = 1


    for r in range(rows - 1):  # no movement from last row
        for c in range(cols):
            w = ways[r][c]
            if w == 0:
                continue
            ch = grid[r][c]

            if ch == "^":
                # split down-left and down-right
                for dc in (-1, 1):
                    nc = c + dc
                    if 0 <= nc < cols:
                        ways[r+1][nc] += w
            else:
                ways[r+1][c] += w

    # sum of all ways that end in the last row
    answer = sum(ways[rows - 1][c] for c in range(cols))
    return answer


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code solution runner")
    parser.add_argument(
        "input_file",
        nargs="?",
        type=Path,
        default=Path("input.txt"),
        help="path to puzzle input (default: %(default)s)",
    )
    args = parser.parse_args()

    raw_input = args.input_file.read_text(encoding="utf-8")
    data = parse_input(raw_input)

    # Copy iterables so both parts see the same data.
    part1_answer = part_one(list(data))
    part2_answer = part_two(list(data))

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


if __name__ == "__main__":
    main()
