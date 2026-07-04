"""JSON storage for the Developer Profile CLI."""

from __future__ import annotations

from pathlib import Path
from typing import Any


def save_profile(profile: dict[str, Any], path: str | Path) -> None:
    """Save a developer profile as readable JSON."""
    # TODO: Milestone 2.
    raise NotImplementedError("Implement save_profile")


def load_profile(path: str | Path) -> dict[str, Any]:
    """Load a developer profile from JSON."""
    # TODO: Milestone 2.
    raise NotImplementedError("Implement load_profile")

