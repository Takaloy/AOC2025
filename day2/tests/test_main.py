"""Tests for Day 2 helper functions."""

from __future__ import annotations

import pytest

from main import (
    count_invalid_ids,
    get_invalid_ids,
    get_invalid_ids_from_string,
    sum_invalid_ids,
)


def test_get_invalid_ids_returns_mirrored_candidates() -> None:
    """All mirrored two-digit IDs inside the range should be discovered."""
    assert get_invalid_ids(10, 200) == [int(str(value) * 2) for value in range(1, 10)]


def test_get_invalid_ids_rejects_invalid_range() -> None:
    """min_value > max_value should raise a ValueError."""
    with pytest.raises(ValueError):
        get_invalid_ids(300, 100)


def test_get_invalid_ids_from_string_handles_leading_zero() -> None:
    """Leading zeros trigger the special-case path that pre-fills the range."""
    result = get_invalid_ids_from_string("012", "50")
    expected = list(range(12, 20))
    expected.extend(get_invalid_ids(20, 50))

    assert result == expected


def test_count_and_sum_invalid_ids_match_helper() -> None:
    """Wrapper helpers should return consistent counts and sums."""
    expected = get_invalid_ids(10, 1500)

    assert count_invalid_ids("10", "1500") == len(expected)
    assert sum_invalid_ids("10", "1500") == sum(expected)
