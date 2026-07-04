import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from developer_profile.model import (  # noqa: E402
    build_developer_profile,
    clean_text,
    normalise_github_username,
    normalise_name,
    normalise_skill,
    parse_skills,
)


class CleanTextTests(unittest.TestCase):
    def test_clean_text_strips_and_collapses_whitespace(self) -> None:
        self.assertEqual(clean_text("  secure   software  ", "goal"), "secure software")

    def test_clean_text_rejects_non_strings(self) -> None:
        with self.assertRaises(TypeError):
            clean_text(123, "goal")

    def test_clean_text_rejects_blank_text(self) -> None:
        with self.assertRaises(ValueError):
            clean_text("   ", "goal")

    def test_clean_text_rejects_control_characters(self) -> None:
        with self.assertRaises(ValueError):
            clean_text("secure\nsoftware", "goal")


class NormalisationTests(unittest.TestCase):
    def test_normalise_name_title_cases_cleaned_name(self) -> None:
        self.assertEqual(normalise_name("  david   akwuegbu "), "David Akwuegbu")

    def test_normalise_skill_uses_known_display_names(self) -> None:
        self.assertEqual(normalise_skill(" javascript "), "JavaScript")
        self.assertEqual(normalise_skill("github"), "GitHub")

    def test_normalise_skill_title_cases_unknown_skills(self) -> None:
        self.assertEqual(normalise_skill(" secure coding "), "Secure Coding")


class SkillParsingTests(unittest.TestCase):
    def test_parse_skills_accepts_comma_separated_text(self) -> None:
        self.assertEqual(parse_skills("python, git, testing"), ["Python", "Git", "Testing"])

    def test_parse_skills_accepts_lists(self) -> None:
        self.assertEqual(parse_skills(["python", "TypeScript"]), ["Python", "TypeScript"])

    def test_parse_skills_deduplicates_case_insensitively(self) -> None:
        self.assertEqual(parse_skills("python, Python, PYTHON, git"), ["Python", "Git"])

    def test_parse_skills_requires_at_least_one_skill(self) -> None:
        with self.assertRaises(ValueError):
            parse_skills(" , ")


class GitHubUsernameTests(unittest.TestCase):
    def test_normalise_github_username_allows_valid_username(self) -> None:
        self.assertEqual(normalise_github_username(" DavidAkwuegbu-Engineer "), "DavidAkwuegbu-Engineer")

    def test_normalise_github_username_allows_blank_optional_value(self) -> None:
        self.assertIsNone(normalise_github_username(None))
        self.assertIsNone(normalise_github_username("   "))

    def test_normalise_github_username_rejects_invalid_characters(self) -> None:
        with self.assertRaises(ValueError):
            normalise_github_username("David_Akwuegbu")

    def test_normalise_github_username_rejects_edge_hyphens(self) -> None:
        with self.assertRaises(ValueError):
            normalise_github_username("-David")
        with self.assertRaises(ValueError):
            normalise_github_username("David-")


class ProfileBuilderTests(unittest.TestCase):
    def test_build_developer_profile_returns_predictable_profile(self) -> None:
        profile = build_developer_profile(
            " david akwuegbu ",
            " aspiring software engineer ",
            "python, git, testing",
            " build secure employer-ready software ",
            "DavidAkwuegbu-Engineer",
        )

        self.assertEqual(
            profile,
            {
                "name": "David Akwuegbu",
                "role": "Aspiring Software Engineer",
                "skills": ["Python", "Git", "Testing"],
                "goal": "build secure employer-ready software",
                "github_username": "DavidAkwuegbu-Engineer",
                "summary": "David Akwuegbu is an Aspiring Software Engineer building skill in Python, Git, Testing.",
            },
        )


if __name__ == "__main__":
    unittest.main()

