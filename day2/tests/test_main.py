"""Tests for Day 2 helper functions."""

from __future__ import annotations

import pytest

from part1 import Part1


@pytest.fixture()
def part1() -> Part1:
    """Provide a reusable Part1 instance for the tests."""
    return Part1()


def test_get_invalid_ids_returns_mirrored_candidates(part1: Part1) -> None:
    """All mirrored two-digit IDs inside the range should be discovered."""
    assert part1.get_invalid_ids(10, 200) == [int(str(value) * 2) for value in range(1, 10)]


def test_get_invalid_ids_rejects_invalid_range(part1: Part1) -> None:
    """min_value > max_value should raise a ValueError."""
    with pytest.raises(ValueError):
        part1.get_invalid_ids(300, 100)


def test_get_invalid_ids_from_string_handles_leading_zero(part1: Part1) -> None:
    """Leading zeros trigger the special-case path that pre-fills the range."""
    result = part1.get_invalid_ids_from_string("012", "50")
    expected = list(range(12, 20))
    expected.extend(part1.get_invalid_ids(20, 50))

    assert result == expected


def test_count_and_sum_invalid_ids_match_helper(part1: Part1) -> None:
    """Wrapper helpers should return consistent counts and sums."""
    expected = part1.get_invalid_ids(10, 1500)

    assert part1.count_invalid_ids("10", "1500") == len(expected)
    assert part1.sum_invalid_ids("10", "1500") == sum(expected)


def test_solve_from_ranges_delegates_to_sum_helper(part1: Part1, monkeypatch: pytest.MonkeyPatch) -> None:
    """solve_from_ranges should leverage sum_invalid_ids for each pair."""
    calls: list[tuple[str, str]] = []

    def fake_sum(min_value: str, max_value: str) -> int:
        calls.append((min_value, max_value))
        return 5

    monkeypatch.setattr(part1, "sum_invalid_ids", fake_sum)

    total = part1.solve_from_ranges([("10", "20"), ("30", "40")])

    assert total == 10
    assert calls == [("10", "20"), ("30", "40")]
