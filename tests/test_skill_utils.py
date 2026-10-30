

import unittest
import os
import sys

# Allow Python to find skill_utils.py
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from skill_utils import extract_skills


class TestSkillExtraction(unittest.TestCase):

    def test_single_skill(self):
        text = "I know Python."
        self.assertEqual(extract_skills(text), {"Python"})

    def test_multiple_skills(self):
        text = "Python SQL Pandas"
        self.assertEqual(
            extract_skills(text),
            {"Python", "SQL", "Pandas"}
        )

    def test_case_insensitive(self):
        text = "python sql PANDAS"
        self.assertEqual(
            extract_skills(text),
            {"Python", "SQL", "Pandas"}
        )

    def test_no_skills(self):
        text = "I like football and music."
        self.assertEqual(extract_skills(text), set())


if __name__ == "__main__":
    unittest.main()