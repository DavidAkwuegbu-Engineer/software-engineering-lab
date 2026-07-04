"""Data validation for the Developer Profile CLI.

Every public function in this module should treat input as untrusted.
The tests describe the required behavior for Milestone 1.
"""

from __future__ import annotations

from typing import Any


MAX_TEXT_LENGTH = 120
MAX_SKILLS = 10

KNOWN_SKILL_NAMES = {
    "css": "CSS",
    "git": "Git",
    "github": "GitHub",
    "html": "HTML",
    "javascript": "JavaScript",
    "next.js": "Next.js",
    "postgres": "Postgres",
    "python": "Python",
    "react": "React",
    "supabase": "Supabase",
    "typescript": "TypeScript",
}


def clean_text(raw_value: Any, field_name: str, max_length: int = MAX_TEXT_LENGTH) -> str:
    """Validate and normalize a short text field."""
    # TODO: reject non-strings with TypeError.
    # TODO: reject control characters with ValueError.
    # TODO: strip leading/trailing whitespace.
    # TODO: collapse repeated internal whitespace to one space.
    # TODO: reject blank text with ValueError.
    # TODO: reject values longer than max_length with ValueError.
    raise NotImplementedError("Implement clean_text")


def normalise_name(raw_name: Any) -> str:
    """Return a display-ready name."""
    # TODO: clean the name and title-case it.
    raise NotImplementedError("Implement normalise_name")


def normalise_skill(raw_skill: Any) -> str:
    """Return a display-ready skill name."""
    # TODO: clean the skill.
    # TODO: use KNOWN_SKILL_NAMES when the lowercase skill is known.
    # TODO: title-case unknown skills.
    raise NotImplementedError("Implement normalise_skill")


def parse_skills(raw_skills: Any) -> list[str]:
    """Return a deduplicated list of validated skills."""
    # TODO: accept a comma-separated string or a list/tuple of strings.
    # TODO: reject every other type with TypeError.
    # TODO: normalize each skill with normalise_skill.
    # TODO: remove duplicate skills case-insensitively while preserving order.
    # TODO: require at least one skill.
    # TODO: reject more than MAX_SKILLS skills.
    raise NotImplementedError("Implement parse_skills")


def normalise_github_username(raw_username: Any | None) -> str | None:
    """Validate an optional GitHub username."""
    # TODO: return None when raw_username is None or blank after trimming.
    # TODO: reject non-strings with TypeError.
    # TODO: allow only letters, numbers, and hyphens.
    # TODO: reject usernames longer than 39 characters.
    # TODO: reject usernames that start or end with a hyphen.
    raise NotImplementedError("Implement normalise_github_username")


def build_developer_profile(
    raw_name: Any,
    raw_role: Any,
    raw_skills: Any,
    raw_goal: Any,
    raw_github_username: Any | None = None,
) -> dict[str, Any]:
    """Build a validated developer profile dictionary."""
    # TODO: normalize each field using the functions above.
    # TODO: return name, role, skills, goal, github_username, and summary.
    raise NotImplementedError("Implement build_developer_profile")

