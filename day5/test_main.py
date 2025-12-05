from textwrap import dedent

from main import (
    find_fresh_incredient_ids_count,
    find_fresh_ingredients,
)


SAMPLE_INPUT = dedent(
    """\
    3-5
    10-14
    16-20
    12-18

    1
    5
    8
    11
    17
    32
    """
).strip()


def sample_lines():
    return SAMPLE_INPUT.splitlines()


def test_find_fresh_ingredients_returns_expected_ids():
    result = find_fresh_ingredients(sample_lines())
    assert result == [5, 11, 17]


def test_find_fresh_incredient_ids_count_handles_overlap_and_gaps():
    result = find_fresh_incredient_ids_count(sample_lines())
    assert result == 14
