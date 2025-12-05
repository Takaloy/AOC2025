from __future__ import annotations

import argparse
from importlib.resources import path
from pathlib import Path
from typing import Iterable, List


def find_fresh_ingredients(lines : Iterable[str]) -> List[str]:
    
    freshStuff = []
    fresh_inregredient_ranges = []

    ranges_end = False

    for line in lines:
        if line is None or line == "" or len(line) == 0 or line == "\n":
            ranges_end = True
            continue

        if (not ranges_end):
            parts = line.split("-")
            r_start = int(parts[0])
            r_end = int(parts[1])
            fresh_inregredient_ranges.append( (r_start, r_end) )

        if (ranges_end):
            item = int(line)
            for (r,c) in fresh_inregredient_ranges:
                if (item >= r and item <= c):
                    freshStuff.append(item)
                    break

    return freshStuff


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Parse the puzzle input from textinput.txt (or a provided file)."
    )
    parser.add_argument(
        "input_file",
        nargs="?",
        default="textinput.txt",
        help="Path to the input file. Defaults to textinput.txt in this directory.",
    )
    args = parser.parse_args()

    path = Path(args.input_file)

    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    with path.open(encoding="utf-8") as file:
        fresh_ingredients = find_fresh_ingredients(file)

    # for ingredient in fresh_ingredients:
    #     print(ingredient)

    print(f"Number of fresh ingredients: {len(fresh_ingredients)}")

if __name__ == "__main__":
    main()
