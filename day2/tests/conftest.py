"""Pytest configuration helpers for Day 2."""

from __future__ import annotations

import sys
from pathlib import Path

# Ensure the Day 2 package directory is importable as the module root.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
project_root_str = PROJECT_ROOT.as_posix()
if project_root_str not in sys.path:
    sys.path.insert(0, project_root_str)
