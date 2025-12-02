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


def get_invalid_ids(min_value_string: str, max_value_string: str) -> list[int]:
    """Wrapper to convert string inputs to integers for get_invalid_ids."""
    
    invalid_ids: list[int] = []

    min_value = int(min_value_string)    
    max_value = int(max_value_string)


    if min_value_string.startswith("0"):
        new_min_value = len(str(abs(min_value_string))) * 10 #round up to nearest 10
        for min_num in range(min_value, new_min_value):
            invalid_ids.append(min_num)
        min_value = new_min_value

    invalid_ids.append(get_invalid_ids(min_value, max_value))
    return invalid_ids

def count_invalid_ids(min_value: int, max_value: int) -> int:
    """Convenience wrapper to count invalid IDs in the given range."""
    return len(get_invalid_ids(min_value, max_value))


def main() -> None:
    """Run the Day 2 solution."""
    try:
        with open("textinput.txt", "r", encoding="utf-8") as handle:
            content = handle.read().strip()
    except FileNotFoundError as exc:
        raise SystemExit("Missing textinput.txt input file.") from exc

    if not content:
        raise SystemExit("textinput.txt is empty.")

    


if __name__ == "__main__":
    main()
