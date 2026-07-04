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
    if not isinstance(raw_value, str):
        raise TypeError(f"{field_name} must be a string")

    if any(ord(character) < 32 or ord(character) == 127 for character in raw_value):
        raise ValueError(f"{field_name} must not contain control characters")

    cleaned_value = " ".join(raw_value.strip().split())

    if not cleaned_value:
        raise ValueError(f"{field_name} must not be blank")

    if len(cleaned_value) > MAX_TEXT_LENGTH:
        raise ValueError(f"{field_name} must be {MAX_TEXT_LENGTH} characters or fewer")

    return cleaned_value


def normalise_name(raw_name: Any) -> str:
    """Return a cleaned display name."""
    return clean_text(raw_name, "name").title()


def parse_age(raw_age: Any) -> int:
    """Return a validated age as an integer."""
    if isinstance(raw_age, bool):
        raise TypeError("age must be an integer, not a boolean")

    if isinstance(raw_age, int):
        age = raw_age
    elif isinstance(raw_age, str):
        stripped_age = raw_age.strip()
        if not stripped_age.isdecimal():
            raise ValueError("age must be a digit-only string")
        age = int(stripped_age)
    else:
        raise TypeError("age must be an integer or digit-only string")

    if age < 0 or age > MAX_AGE:
        raise ValueError(f"age must be between 0 and {MAX_AGE}")

    return age


def build_profile_card(raw_name: Any, raw_age: Any, raw_role: Any, raw_city: Any) -> dict[str, Any]:
    """Build a deterministic profile-card dictionary from untrusted values."""
    display_name = normalise_name(raw_name)
    age = parse_age(raw_age)
    role = clean_text(raw_role, "role")
    city = clean_text(raw_city, "city")

    return {
        "display_name": display_name,
        "age": age,
        "role": role,
        "city": city,
        "summary": f"{display_name} is a {age}-year-old {role} based in {city}.",
    }
