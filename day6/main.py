from __future__ import annotations
import argparse
from pathlib import Path
import sys
import re

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

    return total

def get_total_simples(elements: list[str]) -> int:
    results = get_permutations(elements)
    return sum (results)

def get_cephalopods_math_insanity(elements: list[str]) -> list[int]:

    total = []
    total_characters = len(elements[0])
    pivoted_matrix = [[''] * (len(elements)) for _ in range(total_characters)]
    operators = elements[-1].split()
    counting_indexes = []

    for i in range(total_characters):
        character = elements[-1][i]
        if (character == "+" or character == "*"):
            counting_indexes.append((i, character))

    for line in range(0, len(elements)-1):
        for i in range(total_characters):
            pivoted_matrix[i][line] = elements[line][i]

    for counter_index in range(0, len(counting_indexes)):
        (index, operator) = counting_indexes[counter_index]
        if (counter_index == len(counting_indexes)-1): # last item
            stopper = total_characters
        else:
            (stopper, _) = counting_indexes[counter_index+1]
            stopper -= 1 #stop one before the start of next

        temp = 0
        for line in pivoted_matrix[index:stopper]:
            value = int("".join(line))
            if operator == "+":
                temp += value
            elif operator == "*":
                if (temp == 0):
                    temp = 1
                temp *= value
        
        total.append(temp)
    return total

def get_cephalopods_math_insanity_total(elements: list[str]) -> int:
    totals = get_cephalopods_math_insanity(elements)
    return sum(totals)

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

    print(f"Part 1: {get_total_simples(lines)}")
    print(f"Part 2: {get_cephalopods_math_insanity_total(lines)}")

if __name__ == "__main__":
    main()
