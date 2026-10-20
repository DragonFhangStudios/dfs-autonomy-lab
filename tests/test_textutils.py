import unittest

from lab.textutils import slugify, truncate, word_count


class WordCountTests(unittest.TestCase):
    def test_counts_words(self):
        self.assertEqual(word_count("dragon fhang studios"), 3)

    def test_ignores_extra_whitespace(self):
        self.assertEqual(word_count("  one \n two\tthree  "), 3)

    def test_empty_text_has_no_words(self):
        self.assertEqual(word_count(""), 0)


class TruncateTests(unittest.TestCase):
    def test_short_text_is_unchanged(self):
        self.assertEqual(truncate("hello", 10), "hello")

    def test_long_text_is_cut_with_suffix(self):
        self.assertEqual(truncate("hello world", 8), "hello...")

    def test_rejects_length_shorter_than_suffix(self):
        with self.assertRaises(ValueError):
            truncate("hello", 2)


class SlugifyTests(unittest.TestCase):
    def test_title_becomes_slug(self):
        self.assertEqual(slugify("Dragon Fhang Studios!"), "dragon-fhang-studios")

    def test_lowercases_text(self):
        self.assertEqual(slugify("HeLLo"), "hello")

    def test_collapses_runs_of_spaces_and_punctuation(self):
        self.assertEqual(slugify("one   two,  --three"), "one-two-three")

    def test_strips_leading_and_trailing_dashes(self):
        self.assertEqual(slugify("  --hello world?! "), "hello-world")

    def test_empty_text_gives_empty_slug(self):
        self.assertEqual(slugify(""), "")

    def test_only_punctuation_gives_empty_slug(self):
        self.assertEqual(slugify("!!!"), "")


if __name__ == "__main__":
    unittest.main()
