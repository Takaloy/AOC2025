"""Regression tests driven by the AoC sample input."""

from pathlib import Path

from main import part_one, part_two, parse_input


def load_sample_data() -> list[str]:
    """Load and parse the canonical AoC sample file."""
    sample_path = Path(__file__).resolve().parent.parent / "testinput.txt"
    return parse_input(sample_path.read_text(encoding="utf-8"))


def test_part_one_sample():
    """Sample from the puzzle statement should produce the known answer."""
    data = load_sample_data()
    assert part_one(data) == 21


def test_part_two_sample():
    """Part two should match the published sample result."""
    data = load_sample_data()
    assert part_two(data) == 40
