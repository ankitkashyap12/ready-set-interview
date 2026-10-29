import tempfile
import unittest
from pathlib import Path

from build_catalog import (
    build_catalog,
    extract_prompt,
    linked_groups,
    read_revision_details,
    read_revision_sections,
)


class CatalogTests(unittest.TestCase):
    def test_discovers_source_only_problem_and_all_languages(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            problem = root / "new_problem"
            problem.mkdir()
            (problem / "solution.py").write_text("print('hello')\n", encoding="utf-8")
            (problem / "Solution.java").write_text("class Solution {}\n", encoding="utf-8")
            (root / "README.md").write_text("# Test repo\n", encoding="utf-8")

            catalog = build_catalog(root)

            self.assertEqual(catalog["problemCount"], 1)
            card = catalog["cards"][0]
            self.assertEqual(card["title"], "new problem")
            self.assertFalse(card["hasReadme"])
            self.assertEqual({source["language"] for source in card["sources"]}, {"Java", "Python"})

    def test_extracts_problem_statement_and_topic_links(self):
        statement = (
            "<h2><a href='https://leetcode.com/problems/two-sum'>1. Two Sum</a></h2>"
            "<p>Given an array, find two values whose sum equals the target.</p>"
            "<p><strong>Example 1:</strong> input = [2, 7]</p>"
        )
        self.assertEqual(
            extract_prompt(statement, "1. Two Sum"),
            "Given an array, find two values whose sum equals the target.",
        )
        groups = linked_groups(
            "## Core Patterns\n### Arrays\n- [Two Sum](./TwoSum/)\n"
            "<!---LeetCode Topics Start-->\n"
            "# LeetCode Topics\n## Hash Table\n"
            "- [Two Sum](https://github.com/x/repo/tree/master/0001-two-sum)\n"
        )
        self.assertEqual(groups["TwoSum"], ["Core Patterns / Arrays"])
        self.assertEqual(groups["0001-two-sum"], ["Topic / Hash Table"])

    def test_extracts_gfg_problem_without_title_or_difficulty_prefix(self):
        statement = (
            "# 1. Array insert at end\n## Easy\n"
            "<div><p>Given an array, insert one element at the end.</p>"
            "<p><strong>Example 1:</strong> input and output</p></div>"
        )
        self.assertEqual(
            extract_prompt(statement, "1. Array insert at end"),
            "Given an array, insert one element at the end.",
        )

    def test_extracts_course_prompt_after_course_metadata(self):
        prompt = extract_prompt(
            "# Maximum Pairwise Product\n\n"
            "Course: UC San Diego Algorithmic Toolbox, Week 1 — Programming Challenges.\n\n"
            "Find the maximum product of two distinct numbers in the sequence.\n",
            "Maximum Pairwise Product",
        )
        self.assertEqual(prompt, "Find the maximum product of two distinct numbers in the sequence.")

    def test_reads_named_revision_sections(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            problem = Path(temporary_directory)
            (problem / "REVISION.md").write_text(
                "## Core idea\nUse the prefix sum.\n\n"
                "## Trick\nRemember the empty prefix.\n\n"
                "## Edge cases\n- Empty input\n",
                encoding="utf-8",
            )
            notes = read_revision_sections(problem)
            self.assertEqual(notes["concept"], "Use the prefix sum.")
            self.assertEqual(notes["trick"], "Remember the empty prefix.")
            self.assertEqual(notes["edgeCases"], "- Empty input")
            self.assertNotIn("complexity", notes)

    def test_reads_revision_metadata_and_hints(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            problem = Path(temporary_directory)
            (problem / "REVISION.md").write_text(
                "# Longest Peak\n\n"
                "- **Problem Number**: #033\n"
                "- **Difficulty**: Medium\n"
                "- **Topic**: Arrays & Hashing\n"
                "- **Pattern**: Peak Detection\n"
                "- **LeetCode Equivalent**: [LC 845: Longest Mountain in Array](https://leetcode.com/problems/longest-mountain-in-array/)\n\n"
                "## Active recall\nHow do you find the longest peak in O(N)?\n\n"
                "## Core idea\nIdentify local peaks and expand outwards.\n\n"
                "## Hints\n- **Hint 1**: Look for elements greater than both neighbors.\n- **Hint 2**: Expand left and right.\n\n"
                "## Complexity\nTime: O(N). Space: O(1).\n",
                encoding="utf-8",
            )
            sections, meta = read_revision_details(problem)
            self.assertEqual(meta["title"], "Longest Peak")
            self.assertEqual(meta["problemNumber"], 33)
            self.assertEqual(meta["difficulty"], "Medium")
            self.assertEqual(meta["topic"], "Arrays & Hashing")
            self.assertEqual(meta["pattern"], "Peak Detection")
            self.assertEqual(meta["lcNumber"], 845)
            self.assertEqual(meta["lcUrl"], "https://leetcode.com/problems/longest-mountain-in-array/")
            self.assertEqual(len(meta["hints"]), 2)
            self.assertIn("Look for elements greater than both neighbors.", meta["hints"][0])

    def test_build_catalog_assigns_formatted_numbers_and_metadata(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            problem = root / "0011-container-with-most-water"
            problem.mkdir()
            (problem / "solution.py").write_text("class Solution: pass\n", encoding="utf-8")
            (problem / "REVISION.md").write_text(
                "# Container With Most Water\n\n"
                "- **Problem Number**: #005\n"
                "- **Difficulty**: Medium\n"
                "- **Topic**: Two Pointers\n"
                "- **Pattern**: Inward Two Pointers\n"
                "- **LeetCode Equivalent**: [LC 11: Container With Most Water](https://leetcode.com/problems/container-with-most-water/)\n\n"
                "## Core idea\nShrink inward.\n",
                encoding="utf-8",
            )
            (root / "README.md").write_text("# Test\n", encoding="utf-8")

            catalog = build_catalog(root)
            self.assertEqual(catalog["problemCount"], 1)
            card = catalog["cards"][0]
            self.assertEqual(card["problemNumber"], 5)
            self.assertEqual(card["problemNumberFormatted"], "#005")
            self.assertEqual(card["difficulty"], "Medium")
            self.assertEqual(card["topic"], "Two Pointers")
            self.assertEqual(card["pattern"], "Inward Two Pointers")
            self.assertEqual(card["lcNumber"], 11)
            self.assertEqual(card["lcUrl"], "https://leetcode.com/problems/container-with-most-water/")


if __name__ == "__main__":
    unittest.main()
