import argparse
from pathlib import Path
from collections import deque


def _increment_matrix(matrix: list[list[int]], r: int, c: int, increment: int) -> None:
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr = r + dr
            nc = c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                matrix[nr][nc] += increment

def _count_roll_matrix_with_queue(matrix: list[list[int]], queue: deque, recursive = False, count: int = 0) -> int:
    shouldRecurse = False
    new_queue = deque()
    while queue:
        (r, c)= queue.popleft()
        if matrix[r][c] < 4:
            count += 1
            if (recursive): # modifying matrix only if recursive, or else you'd change the value on the fly
                _increment_matrix(matrix, r, c, -1)
            shouldRecurse = True
        else:
            new_queue.append((r, c)) #put it back for next round

    if shouldRecurse and recursive:
        return _count_roll_matrix_with_queue(matrix, new_queue, recursive, count)
    else:
        return count

def count_roll_neighbours(data: list[list[str]], recursive: bool = False, count: int = 0) -> int:
    rows = len(data)
    cols = len(data[0]) if rows > 0 else 0
    matrix = [[0] * cols for _ in range(rows)]
    queue = deque()
    for r in range(rows):
        for c in range(cols):
            if data[r][c] == '@':
                _increment_matrix(matrix, r, c, 1)
                queue.append((r, c))

    return _count_roll_matrix_with_queue(matrix, queue, recursive, count)


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

    print(f"Part1: Count of roll neighbours: {count_roll_neighbours(data)}")
    print(f"Part2: Count of roll neighbours (with recursion): {count_roll_neighbours(data, recursive=True)}")
if __name__ == "__main__":
    main()
