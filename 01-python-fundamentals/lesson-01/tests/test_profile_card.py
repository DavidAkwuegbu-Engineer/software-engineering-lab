import unittest

from src.profile_card import build_profile_card, clean_text, normalise_name, parse_age


class CleanTextTests(unittest.TestCase):
    def test_clean_text_strips_and_collapses_whitespace(self) -> None:
        self.assertEqual(clean_text("  backend   engineer  ", "role"), "backend engineer")

    def test_clean_text_rejects_non_string_values(self) -> None:
        with self.assertRaises(TypeError):
            clean_text(42, "role")

    def test_clean_text_rejects_blank_values(self) -> None:
        with self.assertRaises(ValueError):
            clean_text("   ", "city")

    def test_clean_text_rejects_control_characters(self) -> None:
        with self.assertRaises(ValueError):
            clean_text("London\nUK", "city")

    def test_clean_text_rejects_long_values(self) -> None:
        with self.assertRaises(ValueError):
            clean_text("x" * 81, "role")


class NameTests(unittest.TestCase):
    def test_normalise_name_title_cases_cleaned_name(self) -> None:
        self.assertEqual(normalise_name("  ada   lovelace "), "Ada Lovelace")


class AgeTests(unittest.TestCase):
    def test_parse_age_accepts_ints_and_digit_strings(self) -> None:
        self.assertEqual(parse_age(37), 37)
        self.assertEqual(parse_age(" 37 "), 37)

    def test_parse_age_rejects_bool(self) -> None:
        with self.assertRaises(TypeError):
            parse_age(True)

    def test_parse_age_rejects_non_digit_strings(self) -> None:
        with self.assertRaises(ValueError):
            parse_age("37 years")

    def test_parse_age_rejects_out_of_range_values(self) -> None:
        with self.assertRaises(ValueError):
            parse_age(-1)
        with self.assertRaises(ValueError):
            parse_age(131)


class ProfileCardTests(unittest.TestCase):
    def test_build_profile_card_returns_predictable_profile(self) -> None:
        card = build_profile_card(" grace   hopper ", "37", "Computer Scientist", "Arlington")

        self.assertEqual(
            card,
            {
                "display_name": "Grace Hopper",
                "age": 37,
                "role": "Computer Scientist",
                "city": "Arlington",
                "summary": "Grace Hopper is a 37-year-old Computer Scientist based in Arlington.",
            },
        )


if __name__ == "__main__":
    unittest.main()

