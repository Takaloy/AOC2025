import argparse
from pathlib import Path



def count_roll_neighbours(data: list[list[str]]) -> int:
    rows = len(data)
    cols = len(data[0]) if rows > 0 else 0
    count = 0
    matrix = [[0] * cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if data[r][c] == '@':
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        nr = (r + dr)
                        nc = (c + dc)

                        if nr < 0 or nr >= rows:
                            continue

                        if nc < 0 or nc >= cols:
                            continue
                            
                        matrix[nr][nc] += 1
    
    # now loop through again to count rolls that have less than 4 papers @
    for r in range(rows):
        for c in range(cols):
            if data[r][c] == '@' and matrix[r][c] < 4:
                print(f"Roll at ({r}, {c}) has {matrix[r][c]} neighbours")
                count += 1    
    
    return count


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

    print(f"Count of roll neighbours: {count_roll_neighbours(data)}")

if __name__ == "__main__":
    main()