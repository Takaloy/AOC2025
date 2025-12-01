"""Pytest configuration helpers."""

from __future__ import annotations

import sys
from pathlib import Path

# Ensure the project root (where main.py lives) is importable when pytest runs.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if PROJECT_ROOT.as_posix() not in sys.path:
    sys.path.insert(0, PROJECT_ROOT.as_posix())
