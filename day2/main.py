"""Entry point for Advent of Code 2025 Day 2 exercises."""

from __future__ import annotations

from part1 import Part1

class Part2:
    def is_valid_id(self, number : int) -> bool:
        
        first_digit = str(number)[0]
        if (number == int(first_digit)):
            return True
        
        if (number == int(first_digit * len(str(number)))):
            return False

        divisibles = self.get_divisors(len(str(number)))
        for div in divisibles:
            half_len = len(str(number)) // div
            all_equal = True
            for i in range(0, len(str(number)), half_len):
                part = str(number)[i:i+half_len]
                if part != str(number)[0:half_len]:
                    all_equal = False
                    break
            if all_equal:
                return False
        return True


    def get_divisors(self, n):
        divs = set()
        i = 1
        while i * i <= n:
            if n % i == 0:
                divs.add(i)
                divs.add(n // i)
            i += 1
        return sorted(d for d in divs if 1 < d < n)

    def sum_invalid_ids_in_range(self, min_value: int, max_value: int) -> int:
        """Sum all invalid IDs within the given range."""
        total = 0
        for number in range(min_value, max_value + 1):
            if not self.is_valid_id(number):
                total += number
        return total

    def solve_from_ranges(self, ranges: list[tuple[int, int]]) -> int:
        """Compute the total across a collection of string range pairs."""
        return sum(self.sum_invalid_ids_in_range(int(min_value), int(max_value)) for min_value, max_value in ranges)

def main() -> None:
    """Run the Day 2 solution."""
    try:
        with open("textinput.txt", "r", encoding="utf-8") as handle:
            content = handle.read().strip()
    except FileNotFoundError as exc:
        raise SystemExit("Missing textinput.txt input file.") from exc

    if not content:
        raise SystemExit("textinput.txt is empty.")

    ranges: list[tuple[str, str]] = []
    for part in content.split(","):
        a, b = part.split("-")
        ranges.append((a, b))


    solver1 = Part1()
    solver2 = Part2()
    print("Part 1:", solver1.solve_from_ranges(ranges))
    print("Part 2:", solver2.solve_from_ranges(ranges))


if __name__ == "__main__":
    main()
