from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import main


def test_count_roll_neighbours_isolated_roll():
    data = [
        ".@.",
        "...",
        "...",
    ]

    assert main.count_roll_neighbours(data) == 1


def test_count_roll_neighbours_dense_cluster():
    data = [
        "@@",
        "@@",
    ]

    assert main.count_roll_neighbours(data) == 4


def test_input_should_be_result_in_13():
    puzzle_input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
    expected = main.count_roll_neighbours(puzzle_input.splitlines())

    assert 13 == expected
