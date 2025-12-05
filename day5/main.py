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

def find_fresh_incredient_ids_count(lines : Iterable[str]) -> int:
    fresh_inregredient_ranges = []

    for line in lines:
        if line is None or line == "" or len(line) == 0 or line == "\n":
            break

        parts = line.split("-")
        r_start = int(parts[0])
        r_end = int(parts[1])
        fresh_inregredient_ranges.append( (r_start, r_end) )

    sorted_fresh_inregredient_ranges = sorted(fresh_inregredient_ranges, key=lambda x: x[0])
    fresh_ingredient_ids = []

    current_index = 0
    fresh_ids_total = 0

    for (r_start, r_end) in sorted_fresh_inregredient_ranges:
        if (r_start > current_index):
            fresh_ids_total += (r_end - r_start + 1)    # +1 to include both ends
            current_index = r_end
        elif (r_end > current_index):
            fresh_ids_total += (r_end - current_index)
            current_index = r_end

    return fresh_ids_total
     

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
        file.seek(0)
        ids_total = find_fresh_incredient_ids_count(file)
    # for ingredient in fresh_ingredients:
    #     print(ingredient)

    print(f"Number of fresh ingredients: {len(fresh_ingredients)}")
    print(f"Count of fresh ingredient IDs: {ids_total}")
if __name__ == "__main__":
    main()
