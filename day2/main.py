"""Entry point for Advent of Code 2025 Day 2 exercises."""


def get_invalid_ids(min_value: int, max_value: int) -> list[int]:
    """Return all even-length IDs whose halves are identical within [min_value, max_value]."""
    if min_value < 0 or max_value < 0:
        raise ValueError("ID ranges must be non-negative.")
    if min_value > max_value:
        raise ValueError("min_value cannot be greater than max_value.")

    max_len = len(str(max_value))
    invalid_ids: list[int] = []
    for id_len in range(2, max_len + 1):
        if id_len % 2 != 0:
            continue
        half_len = id_len // 2
        start = 1 if half_len == 1 else 10 ** (half_len - 1)
        end = 10 ** half_len
        for first_half in range(start, end):
            candidate = int(f"{first_half}{first_half}")
            if min_value <= candidate <= max_value:
                invalid_ids.append(candidate)

    return invalid_ids


def get_invalid_ids_from_string(min_value_string: str, max_value_string: str) -> list[int]:
    """Wrapper to convert string inputs to integers for get_invalid_ids."""

    invalid_ids: list[int] = []

    min_value = int(min_value_string)    
    max_value = int(max_value_string)

    if str(min_value_string).startswith("0"):
        print("Warning: Leading zeros in min_value_string may affect results.")
        new_min_value = len(str(abs(min_value))) * 10  # round up to nearest 10
        for min_num in range(min_value, new_min_value):
            invalid_ids.append(min_num)
        min_value = new_min_value

    invalid_ids.extend(get_invalid_ids(min_value, max_value))
    return invalid_ids


def count_invalid_ids(min_value_string: str, max_value_string: str) -> int:
    counter = len(get_invalid_ids_from_string(min_value_string, max_value_string))
    print(f"Found {counter} invalid IDs between {min_value_string} and {max_value_string}.")
    return counter

def sum_invalid_ids(min_value_string: str, max_value_string: str) -> int:
    listOfInvalids = get_invalid_ids_from_string(min_value_string, max_value_string)
    total = sum(listOfInvalids)
    print(f"Sum of invalid IDs between {min_value_string} and {max_value_string} is {total}.")
    return total

def main() -> None:
    """Run the Day 2 solution."""
    try:
        with open("textinput.txt", "r", encoding="utf-8") as handle:
            content = handle.read().strip()
    except FileNotFoundError as exc:
        raise SystemExit("Missing textinput.txt input file.") from exc

    if not content:
        raise SystemExit("textinput.txt is empty.")

    result = []

    # Split by comma, then by hyphen
    for part in content.split(","):
        a, b = part.split("-")
        result.append([a, b])
    
    print("Part 1:", sum(sum_invalid_ids(a, b) for a, b in result))

if __name__ == "__main__":
    main()
