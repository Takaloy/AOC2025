import pytest

from main import get_largest_joltage, get_total_joltage


BANKS = [
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111",
]


@pytest.mark.parametrize(
    ("bank", "batteries", "expected"),
    [
        ("987654321111111", 2, 98),
        ("811111111111119", 2, 89),
        ("234234234234278", 2, 78),
        ("818181911112111", 2, 92),
        ("987654321111111", 3, 987),
        ("811111111111119", 3, 819),
        ("234234234234278", 3, 478),
        ("818181911112111", 3, 921),
        ("1029384756", 4, 9876),
    ],
)
def test_get_largest_joltage_returns_highest_possible_value(bank: str, batteries: int, expected: int) -> None:
    assert get_largest_joltage(bank, batteries) == expected


@pytest.mark.parametrize(
    ("batteries", "expected"),
    [
        (2, 357),
        (3, 3205),
    ],
)
def test_get_total_joltage_sums_all_banks(batteries: int, expected: int) -> None:
    assert get_total_joltage(BANKS, batteries) == expected
