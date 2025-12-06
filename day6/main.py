from __future__ import annotations
import argparse
from pathlib import Path
import sys

def get_permutations(elements: list[str]) -> list[int]:

    # Allocate one slot per permutation we may want to fill in later.
    total = elements[0].split()

    operators = elements[-1].split()

    for line in range(1, len(elements) -1):
        currentIters = elements[line].split()
        for index in range(len(currentIters)):
            
            if operators[index] == '+':
                total[index] = int(total[index]) + int(currentIters[index])
            elif operators[index] == '*':
                total[index] = int(total[index]) * int(currentIters[index])
            elif operators[index] == '-':
                total[index] = int(total[index]) - int(currentIters[index])
            elif operators[index] == '/':
                total[index] = int(currentIters[index]) / int(total[index])

    return total

def get_total(elements: list[str]) -> int:
    
    results = get_permutations(elements)
    return sum (results)

def parse_args() -> argparse.Namespace:
    """Build and parse the CLI arguments."""
    parser = argparse.ArgumentParser(description="Run Advent of Code solutions")
    parser.add_argument(
        "input",
        nargs="?",
        default="textinput.txt",
        help="Path to the puzzle input (defaults to input.txt)",
    )
    return parser.parse_args()


def read_input(path: str) -> list[str]:
    """Load the puzzle input and return the lines."""
    try:
        return Path(path).read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        sys.exit(f"Input file not found: {path}")

def main() -> None:
    args = parse_args()
    lines = read_input(args.input)

    print(f"Part 1: {get_total(lines)}")


if __name__ == "__main__":
    main()
