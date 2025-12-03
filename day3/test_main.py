import pytest

from main import get_largest_joltage_for, get_total_joltage_for


@pytest.mark.parametrize(
    ("bank", "expected"),
    [
        ("987654321111111", 98),
        ("811111111111119", 89),
        ("234234234234278", 78),
        ("818181911112111", 92),
    ],
)
def test_get_largest_joltage_for_returns_highest_adjacent_pair(bank: str, expected: int) -> None:
    assert get_largest_joltage_for(bank) == expected


def test_get_total_joltage_for_sums_each_bank() -> None:
    banks = [
        "987654321111111",  # 98
        "811111111111119",  # 89
        "234234234234278",  # 78
        "818181911112111",  # 92
    ]
    assert get_total_joltage_for(banks) == 357
