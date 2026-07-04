"""Profile card exercise for Lesson 1.

The functions in this module should treat every argument as untrusted input.
Keep the implementation small, explicit, and easy to test.
"""

from __future__ import annotations

from typing import Any


MAX_TEXT_LENGTH = 80
MAX_AGE = 130


def clean_text(raw_value: Any, field_name: str) -> str:
    """Validate and normalize a short human-entered text field."""
    # TODO: reject non-strings with TypeError.
    # TODO: strip leading/trailing whitespace.
    # TODO: collapse repeated internal whitespace to one space.
    # TODO: reject blank text with ValueError.
    # TODO: reject text longer than MAX_TEXT_LENGTH with ValueError.
    # TODO: reject control characters with ValueError.
    raise NotImplementedError("Implement clean_text")


def normalise_name(raw_name: Any) -> str:
    """Return a cleaned display name."""
    # TODO: clean the value and return it title-cased.
    raise NotImplementedError("Implement normalise_name")


def parse_age(raw_age: Any) -> int:
    """Return a validated age as an integer."""
    # TODO: reject booleans with TypeError.
    # TODO: accept integers directly.
    # TODO: accept digit-only strings after trimming whitespace.
    # TODO: reject every other type or format.
    # TODO: enforce the inclusive 0..MAX_AGE range.
    raise NotImplementedError("Implement parse_age")


def build_profile_card(raw_name: Any, raw_age: Any, raw_role: Any, raw_city: Any) -> dict[str, Any]:
    """Build a deterministic profile-card dictionary from untrusted values."""
    # TODO: normalize each field with the functions above.
    # TODO: return display_name, age, role, city, and summary keys.
    raise NotImplementedError("Implement build_profile_card")

