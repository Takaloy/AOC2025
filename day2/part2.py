"""Day 2 Part 2 helper utilities."""

from __future__ import annotations


class Part2:
    """Utility methods for validating IDs and summing invalid ranges."""

    def is_valid_id(self, number: int) -> bool:
        """Return True if the ID passes the repetition checks."""
        digits = str(number)
        first_digit = digits[0]
        if number < 10:
            return True
        if number == int(first_digit * len(digits)):
            return False

        divisibles = self.get_divisors(len(digits))
        for divisor in divisibles:
            base_num = digits[:divisor]
            if base_num * (len(digits) // divisor) == digits:
                return False
        return True

    def get_divisors(self, value: int) -> list[int]:
        """Return the divisors (excluding 1 and value)."""
        divisors = set()
        i = 1
        while i * i <= value:
            if value % i == 0:
                divisors.add(i)
                divisors.add(value // i)
            i += 1
        return sorted(d for d in divisors if 1 < d < value)

    def sum_invalid_ids_in_range(self, min_value: int, max_value: int) -> int:
        """Sum all invalid IDs within the given range."""
        total = 0
        for number in range(min_value, max_value + 1):
            if not self.is_valid_id(number):
                total += number
        return total

    def solve_from_ranges(self, ranges: list[tuple[int, int]]) -> int:
        """Compute the total across a collection of string range pairs."""
        return sum(
            self.sum_invalid_ids_in_range(int(min_value), int(max_value))
            for min_value, max_value in ranges
        )
