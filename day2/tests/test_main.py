"""Tests for Day 2 helper functions."""

from __future__ import annotations

import pytest

from part1 import Part1
from part2 import Part2


@pytest.fixture()
def part1() -> Part1:
    """Provide a reusable Part1 instance for the tests."""
    return Part1()


@pytest.fixture()
def part2() -> Part2:
    """Provide a reusable Part2 instance for the tests."""
    return Part2()


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


def test_sum_invalid_ids_matches_helper(part1: Part1) -> None:
    """String wrapper sum should align with the integer helper."""
    expected = part1.get_invalid_ids(10, 1500)
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


def test_part2_get_divisors_excludes_trivial_values(part2: Part2) -> None:
    """Divisor helper should only return factors strictly between 1 and n."""
    assert part2.get_divisors(12) == [2, 3, 4, 6]


def test_part2_is_valid_id_detects_repeated_patterns(part2: Part2) -> None:
    """Repeated halves should be invalid while mixed digits remain valid."""
    assert part2.is_valid_id(7)  # single-digit is accepted
    assert not part2.is_valid_id(11)
    assert not part2.is_valid_id(1212)
    assert part2.is_valid_id(1234)


def test_part2_sum_invalid_ids_in_range_matches_manual(part2: Part2) -> None:
    """Summation helper should align with a manual iteration."""
    min_value, max_value = 10, 40
    manual = sum(value for value in range(min_value, max_value + 1) if not part2.is_valid_id(value))
    assert part2.sum_invalid_ids_in_range(min_value, max_value) == manual


def test_part2_solve_from_ranges_accepts_string_ranges(part2: Part2, monkeypatch: pytest.MonkeyPatch) -> None:
    """solve_from_ranges should cast inputs to ints and accumulate results."""
    calls: list[tuple[int, int]] = []

    def fake_sum(min_value: int, max_value: int) -> int:
        calls.append((min_value, max_value))
        return 5

    monkeypatch.setattr(part2, "sum_invalid_ids_in_range", fake_sum)

    total = part2.solve_from_ranges([("10", "12"), ("20", "21")])

    assert total == 10
    assert calls == [(10, 12), (20, 21)]
