#!/usr/bin/env python3
"""Entry point for the AoC Day 3 solution."""

from __future__ import annotations

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Process input for AoC Day 3 from a text file.",
    )
    parser.add_argument(
        "input_file",
        nargs="?",
        default="textinput.txt",
        help="Path to the puzzle input file (default: textinput.txt).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input_file)
    if not input_path.exists():
        raise SystemExit(f"Input file not found: {input_path}")

    data = input_path.read_text(encoding="utf-8").splitlines()

    print(f"Part1: Total joltage: {get_total_joltage_for(data)}")
    print(f"Part1: Total joltage: {get_total_joltage(data, 2)}")
    print(f"Part2: Total joltage: {get_total_joltage(data, 12)}")

    

def get_largest_joltage_for(bank: str) -> int:

    largest_first_digit = int(bank[0])
    largest_second_digit = int(bank[1])

    for i in range(1, len(bank)-1):
        digit = int(bank[i])
        if digit > largest_first_digit:
            largest_first_digit = digit
            largest_second_digit = int(bank[i+1])
        elif digit > largest_second_digit:
            largest_second_digit = digit

    last_digit = int(bank[-1])
    if last_digit > largest_second_digit:    # Check last digit
        largest_second_digit = last_digit

    return (largest_first_digit * 10) + largest_second_digit

def get_largest_joltage(bank: str, batteries: int) -> int:
    jolts = list(bank[:batteries])
    hook = 0
    for j in range(0, batteries): #iterate through every battery position
        current_jolt = int(jolts[j])

        if hook < j:
            hook = j

        if current_jolt == 9:  # Can't do better than a 9
            hook += 1
            continue

        replaced = False
        for i in range(hook+1, len(bank)-batteries+1+j): #iterate through the bank
            contender_jolt = int(bank[i])
            if (contender_jolt > current_jolt):
                jolts[j:] = bank[i:i+batteries-j]
                current_jolt = contender_jolt
                hook = i
                replaced = True
            if (contender_jolt == 9):  # Can't do better than a 9
                hook += 1
                break
            if (i == len(bank)-batteries+j and replaced == False):  # Reached the end of the bank
                hook += 1
            


    value = int("".join(jolts))
    return value

def get_total_joltage_for(banks: list[str]) -> int:
    total_joltage = 0
    for bank in banks:
        total_joltage += get_largest_joltage_for(bank)
    return total_joltage

def get_total_joltage(banks: list[str], batteries: int) -> int:
    total_joltage = 0
    for bank in banks:
        total_joltage += get_largest_joltage(bank, batteries)
    return total_joltage

if __name__ == "__main__":
    main()
