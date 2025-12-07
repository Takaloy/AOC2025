"""Unit tests for the Advent of Code Day 6 helpers."""

from __future__ import annotations

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

import main


TEST_INPUT_PATH = PROJECT_ROOT / "testinput.txt"


def _load_test_lines() -> list[str]:
    return TEST_INPUT_PATH.read_text(encoding="utf-8").splitlines()


def test_get_permutations_with_test_input() -> None:
    lines = _load_test_lines()
    assert main.get_permutations(lines) == [33210, 490, 4243455, 401]


def test_get_total_simples_with_test_input() -> None:
    lines = _load_test_lines()
    assert main.get_total_simples(lines) == 4277556


def test_get_cephalopods_math_insanity_with_test_input() -> None:
    lines = _load_test_lines()
    assert main.get_cephalopods_math_insanity(lines) == [8544, 625, 3253600, 1058]


def test_get_cephalopods_math_insanity_total_with_test_input() -> None:
    lines = _load_test_lines()
    assert main.get_cephalopods_math_insanity_total(lines) == 3263827
