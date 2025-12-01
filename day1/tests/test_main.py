"""Tests for main.solve_part_one and main.solve_part_two."""

from main import solve_part_one, solve_part_two


def test_solve_part_one_with_sample_input() -> None:
    """Ensure the placeholder implementation remains stable until replaced."""
    lines = [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
    ]
    assert solve_part_one(lines) == 3


def test_solve_part_two_placeholder() -> None:
    """Ensure the placeholder implementation remains stable until replaced."""
    lines = [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
    ]
    assert solve_part_two(lines) == 6

def test_solve_part_two_with_additional_input() -> None:
    """Test part two with additional input."""
    lines = [
        "R1000",
    ]
    assert solve_part_two(lines) == 10