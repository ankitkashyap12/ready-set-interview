#!/usr/bin/env python3
"""Build a static study-card catalog from problem folders in the repository."""

from __future__ import annotations

import argparse
import html
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from typing import Optional
from urllib.parse import unquote, urlparse


CODE_EXTENSIONS = {
    ".c": "C",
    ".cc": "C++",
    ".cpp": "C++",
    ".cs": "C#",
    ".go": "Go",
    ".h": "C/C++",
    ".hs": "Haskell",
    ".hpp": "C++",
    ".java": "Java",
    ".js": "JavaScript",
    ".jsx": "JavaScript",
    ".kt": "Kotlin",
    ".php": "PHP",
    ".py": "Python",
    ".rb": "Ruby",
    ".rs": "Rust",
    ".swift": "Swift",
    ".ts": "TypeScript",
    ".tsx": "TypeScript",
}
IGNORED_DIRECTORIES = {
    ".git",
    ".idea",
    ".vscode",
    "__pycache__",
    "build",
    "dist",
    "node_modules",
    "out",
    "revision",
    "target",
}
SECTION_ALIASES = {
    "recall": {"recall", "question", "active recall", "prompt"},
    "concept": {"concept", "core idea", "approach", "solution idea"},
    "hints": {"hints", "hint", "progressive hints"},
    "pattern": {"pattern", "technique", "when to use"},
    "trick": {"trick", "invariant", "gotcha", "gotchas", "important points"},
    "complexity": {"complexity", "time and space", "time complexity"},
    "edgeCases": {"edge cases", "edge case", "pitfalls", "common mistakes"},
}
SECTION_FILES = ("REVISION.md", "NOTES.md")

FREQUENTLY_ASKED_FOLDERS = {
    "0001-two-sum",
    "1-two-sum",
    "TwoSum",
    "0003-longest-substring-without-repeating-characters",
    "0009-palindrome-number",
    "0011-container-with-most-water",
    "0015-3sum",
    "TripleSum",
    "0020-valid-parentheses",
    "0056-merge-intervals",
    "MergeOverlappinIntervals",
    "0075-sort-colors",
    "3_improving_quicksort",
    "0098-validate-binary-search-tree",
    "0104-maximum-depth-of-binary-tree",
    "0112-path-sum",
    "0121-best-time-to-buy-and-sell-stock",
    "0125-valid-palindrome",
    "0146-lru-cache",
    "0167-two-sum-ii-input-array-is-sorted",
    "0215-kth-largest-element-in-an-array",
    "0217-contains-duplicate",
    "217-contains-duplicate",
    "0238-product-of-array-except-self",
    "ArrayOfProducts",
    "0283-move-zeroes",
    "MoveToEnd",
    "0347-top-k-frequent-elements",
    "0875-koko-eating-bananas",
    "1448-count-good-nodes-in-binary-tree",
    "268-missing-number",
    "53-maximum-subarray",
    "BestSeat",
    "CombinationSum",
    "FirstDuplicateValue",
    "LongestPeak",
    "MajorityElement",
    "2_majority_element",
    "MonotonicArray",
    "NonConstructibleChange",
    "SortedSquaredArray",
    "SpiralMatrixTraversal",
    "ValidateSubsequence",
    "ZeroSumSubArray",
    "1_binary_search",
    "1_fibonacci_number",
    "1_money_change_again",
    "3_car_fueling",
    "3_edit_distance",
    "4_longest_common_subsequence_of_two_sequences",
    "7_maximum_salary",
}



class PlainTextHTMLParser(HTMLParser):
    """Extract readable text from problem statements that contain HTML."""

    block_tags = {
        "article",
        "br",
        "div",
        "h1",
        "h2",
        "h3",
        "h4",
        "hr",
        "li",
        "ol",
        "p",
        "pre",
        "section",
        "tr",
        "ul",
    }

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.ignored_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, Optional[str]]]) -> None:
        if tag in {"script", "style"}:
            self.ignored_depth += 1
        elif tag in self.block_tags:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style"} and self.ignored_depth:
            self.ignored_depth -= 1
        elif tag in self.block_tags:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self.ignored_depth:
            self.parts.append(data)


def plain_text(markdown_or_html: str) -> str:
    text = re.sub(r"<!--.*?-->", " ", markdown_or_html, flags=re.DOTALL)
    if re.search(r"<(?:p|div|h[1-6]|pre|ul|ol|li|br)\b", text, re.IGNORECASE):
        parser = PlainTextHTMLParser()
        parser.feed(text)
        text = "".join(parser.parts)
    text = html.unescape(text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"(?m)^\s{0,3}#{1,6}\s*", "", text)
    text = re.sub(r"(?m)^\s*[-*+]\s+", "• ", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n[ \t]+", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def readme_title(raw: str, fallback: str) -> str:
    html_heading = re.search(r"<h[1-3]\b[^>]*>(.*?)</h[1-3]>", raw, re.IGNORECASE | re.DOTALL)
    if html_heading:
        title = plain_text(html_heading.group(1))
        if title:
            return title
    for line in raw.splitlines():
        match = re.match(r"^\s{0,3}#{1,3}\s+(.+?)\s*#*\s*$", line)
        if match:
            return plain_text(match.group(1)) or fallback
    return fallback


def extract_prompt(raw: str, title: str) -> str:
    text = plain_text(raw)
    paragraphs: list[str] = []
    current: list[str] = []
    stop = re.compile(
        r"^(?:example(?:\s+\d+)?\s*:|input\s*:|output\s*:|your task\b|constraints\b|"
        r"expected (?:time|auxiliary)\b)",
        re.IGNORECASE,
    )
    skip = {"easy", "medium", "hard", "problem statement"}

    def keep_current() -> bool:
        paragraph = " ".join(current).strip()
        current.clear()
        if not paragraph or paragraph.lower().rstrip(":") in skip:
            return False
        if paragraph.lower().startswith("course:"):
            return False
        if title and paragraph.lower() == title.lower():
            return False
        paragraphs.append(paragraph)
        return True

    for line in text.splitlines():
        line = line.strip()
        if not line:
            keep_current()
            continue
        if line.lower() in skip or (title and line.lower() == title.lower()):
            keep_current()
            continue
        if line.lower().startswith("course:"):
            keep_current()
            continue
        if stop.match(line):
            keep_current()
            break
        current.append(line)
    keep_current()
    return "\n\n".join(paragraphs[:5])[:2200]


def read_revision_sections(problem_dir: Path) -> dict[str, str]:
    sections: dict[str, str] = {}
    aliases = {
        alias: key
        for key, names in SECTION_ALIASES.items()
        for alias in names
    }
    heading_pattern = re.compile(r"^\s{0,3}#{1,4}\s+(.+?)\s*#*\s*$")

    for filename in SECTION_FILES:
        path = problem_dir / filename
        if not path.is_file():
            continue
        current_key: Optional[str] = None
        collected: list[str] = []
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            heading = heading_pattern.match(line)
            if heading:
                if current_key and collected and current_key not in sections:
                    sections[current_key] = "\n".join(collected).strip()
                label = re.sub(r"[*_`]", "", heading.group(1)).strip().lower()
                current_key = aliases.get(label)
                collected = []
            elif current_key:
                collected.append(line)
        if current_key and collected and current_key not in sections:
            sections[current_key] = "\n".join(collected).strip()
    return sections


def read_revision_details(problem_dir: Path) -> tuple[dict[str, str], dict[str, object]]:
    sections = read_revision_sections(problem_dir)
    metadata: dict[str, object] = {
        "title": None,
        "problemNumber": None,
        "difficulty": None,
        "topic": None,
        "pattern": None,
        "lcNumber": None,
        "lcTitle": None,
        "lcUrl": None,
        "frequentlyAsked": False,
        "hints": [],
    }

    for filename in SECTION_FILES:
        path = problem_dir / filename
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")

        # Title from # Title
        title_match = re.search(r"^\s{0,3}#\s+([^\n\r]+)", text, re.MULTILINE)
        if title_match and not metadata["title"]:
            metadata["title"] = plain_text(title_match.group(1).strip())

        # Metadata bullets
        num_m = re.search(r"[-*]?\s*\*{0,2}(?:Problem Number|Problem #|\bNumber\b)\*{0,2}:\s*#?(\d+)", text, re.IGNORECASE)
        if num_m and not metadata["problemNumber"]:
            metadata["problemNumber"] = int(num_m.group(1))

        diff_m = re.search(r"[-*]?\s*\*{0,2}Difficulty\*{0,2}:\s*(Easy|Medium|Hard)\b", text, re.IGNORECASE)
        if diff_m and not metadata["difficulty"]:
            metadata["difficulty"] = diff_m.group(1).title()

        topic_m = re.search(r"[-*]?\s*\*{0,2}Topic\*{0,2}:\s*([^\n\r]+)", text, re.IGNORECASE)
        if topic_m and not metadata["topic"]:
            metadata["topic"] = re.sub(r"[*_`]", "", topic_m.group(1)).strip()

        pat_m = re.search(r"[-*]?\s*\*{0,2}Pattern\*{0,2}:\s*([^\n\r]+)", text, re.IGNORECASE)
        if pat_m and not metadata["pattern"]:
            metadata["pattern"] = re.sub(r"[*_`]", "", pat_m.group(1)).strip()

        lc_m = re.search(
            r"[-*]?\s*\*{0,2}(?:LeetCode Equivalent|LeetCode Link|LeetCode)\*{0,2}:\s*\[(.*?)\]\((https?://[^\)]+)\)",
            text,
            re.IGNORECASE,
        )
        if lc_m and not metadata["lcUrl"]:
            metadata["lcTitle"] = lc_m.group(1).strip()
            metadata["lcUrl"] = lc_m.group(2).strip()
            lc_num_m = re.search(r"\bLC\s*#?(\d+)\b", metadata["lcTitle"], re.IGNORECASE)
            if lc_num_m:
                metadata["lcNumber"] = int(lc_num_m.group(1))

        freq_m = re.search(r"[-*]?\s*\*{0,2}(?:Frequently Asked|High Frequency|Top Asked)\*{0,2}:\s*(Yes|True)\b", text, re.IGNORECASE)
        if freq_m:
            metadata["frequentlyAsked"] = True

    # Parse hints if present in sections
    if "hints" in sections:
        hints_text = sections["hints"]
        parsed_hints = []
        for line in hints_text.splitlines():
            line = line.strip()
            if line.startswith("-") or line.startswith("*"):
                cleaned = re.sub(r"^[-*]\s*(?:\*\*Hint\s*\d+\*\*:\s*)?", "", line).strip()
                if cleaned:
                    parsed_hints.append(cleaned)
        metadata["hints"] = parsed_hints

    return sections, metadata


def linked_groups(root_readme: str) -> dict[str, list[str]]:
    groups: dict[str, set[str]] = {}
    major = ""
    minor = ""
    in_leetcode_topics = False

    for line in root_readme.splitlines():
        if "<!---LeetCode Topics Start-->" in line:
            in_leetcode_topics = True
            major = ""
            minor = ""
            continue
        heading = re.match(r"^\s{0,3}(#{1,3})\s+(.+?)\s*#*\s*$", line)
        if heading:
            level = len(heading.group(1))
            label = plain_text(heading.group(2))
            if in_leetcode_topics:
                if level == 1 and label == "LeetCode Topics":
                    continue
                if level == 2:
                    major = f"Topic / {label}"
                    minor = ""
            elif level == 2:
                major = label
                minor = ""
            elif level == 3:
                minor = label

        link = re.search(r"\[[^\]]+\]\((?:<([^>]+)>|([^)]*))\)", line)
        if not link:
            continue
        target = (link.group(1) or link.group(2)).strip()
        folder = folder_from_link(target)
        if not folder:
            continue
        if in_leetcode_topics and not re.match(r"^\d{3,4}-", folder):
            continue
        group = major
        if minor:
            group = f"{major} / {minor}" if major else minor
        if group and group != "Course handouts":
            groups.setdefault(folder, set()).add(group)
    return {folder: sorted(values) for folder, values in groups.items()}


def folder_from_link(target: str) -> Optional[str]:
    if target.startswith("./") or target.startswith("../"):
        candidate = unquote(target.split("#", 1)[0].rstrip("/").split("/")[-1])
        return candidate or None
    parts = [unquote(part) for part in urlparse(target).path.split("/") if part]
    for marker in ("master", "main"):
        if marker in parts:
            index = parts.index(marker)
            if index + 1 < len(parts):
                return parts[index + 1]
    return None


def fallback_group(problem_dir: Path, readme: str) -> str:
    name = problem_dir.name
    if "- GFG" in name:
        return "GeeksforGeeks"
    course = re.search(r"Course:\s*.*?(Week \d+)\s*[—-]\s*([^.\n]+)", readme, re.IGNORECASE)
    if course:
        return f"Algorithmic Foundations / {course.group(1)}: {course.group(2).strip()}"
    if re.match(r"^\d{4}-", name):
        return "LeetCode"
    return "Other problems"


def discover_cards(root: Path) -> list[dict[str, object]]:
    readme_file = root / "README.md"
    readme = readme_file.read_text(encoding="utf-8", errors="replace") if readme_file.is_file() else ""
    groups_by_folder = linked_groups(readme)
    cards: list[dict[str, object]] = []

    scan_dir = root / "problems" if (root / "problems").is_dir() else root
    for problem_dir in sorted(scan_dir.iterdir(), key=lambda path: path.name.casefold()):
        if (
            not problem_dir.is_dir()
            or problem_dir.name.startswith(".")
            or problem_dir.name in IGNORED_DIRECTORIES
            or problem_dir.name == "problems"
        ):
            continue
        sources = [
            path
            for path in problem_dir.rglob("*")
            if path.is_file()
            and path.suffix.lower() in CODE_EXTENSIONS
            and not any(part.startswith(".") or part in IGNORED_DIRECTORIES for part in path.relative_to(problem_dir).parts[:-1])
        ]
        if not sources:
            continue

        readme_path = problem_dir / "README.md"
        raw_readme = readme_path.read_text(encoding="utf-8", errors="replace") if readme_path.is_file() else ""
        raw_title = readme_title(raw_readme, problem_dir.name.replace("-", " ").replace("_", " "))
        prompt = extract_prompt(raw_readme, raw_title) if raw_readme else ""
        notes, meta = read_revision_details(problem_dir)

        # Prefer clean title from REVISION.md (free of raw number prefixes like "1544. Count Good Nodes")
        title = meta.get("title") or raw_title
        if not prompt and notes.get("recall"):
            prompt = notes["recall"]

        groups = groups_by_folder.get(problem_dir.name, [])
        if not groups:
            groups = [fallback_group(problem_dir, raw_readme)]

        problem_url = meta.get("lcUrl")
        if not problem_url:
            match = re.search(r"https?://(?:www\.)?(?:leetcode\.com|geeksforgeeks\.org)/[^\s\"')<>]+", raw_readme)
            if match:
                problem_url = match.group(0).rstrip(".,")

        is_freq = (problem_dir.name in FREQUENTLY_ASKED_FOLDERS) or bool(meta.get("frequentlyAsked"))

        cards.append(
            {
                "id": problem_dir.name,
                "problemNumber": meta.get("problemNumber"),
                "title": title,
                "folder": problem_dir.name,
                "difficulty": meta.get("difficulty") or "Medium",
                "frequentlyAsked": is_freq,
                "topic": meta.get("topic") or (groups[0].split(" / ")[-1] if groups else "General"),
                "pattern": meta.get("pattern") or (notes.get("pattern", "").split("\n")[0].replace("**Pattern**:", "").strip() if notes.get("pattern") else "General Technique"),
                "lcNumber": meta.get("lcNumber"),
                "lcTitle": meta.get("lcTitle"),
                "lcUrl": meta.get("lcUrl") or problem_url,
                "hints": meta.get("hints") or [],
                "groups": groups,
                "prompt": prompt,
                "hasReadme": readme_path.is_file(),
                "notes": notes,
                "sources": [
                    {
                        "path": path.relative_to(root).as_posix(),
                        "language": CODE_EXTENSIONS[path.suffix.lower()],
                        "filename": path.name,
                    }
                    for path in sorted(sources, key=lambda item: (CODE_EXTENSIONS[item.suffix.lower()], item.name.casefold()))
                ],
                "readme": (problem_dir / "README.md").relative_to(root).as_posix() if readme_path.is_file() else None,
                "revisionFile": next(
                    (filename for filename in SECTION_FILES if (problem_dir / filename).is_file()),
                    None,
                ),
                "problemUrl": problem_url,
            }
        )
    return cards


def build_catalog(root: Path) -> dict[str, object]:
    cards = discover_cards(root)
    # Sort cards deterministically by assigned problemNumber, falling back to folder
    cards.sort(key=lambda c: (c.get("problemNumber") is None, c.get("problemNumber") or 0, c["folder"].lower()))
    for idx, card in enumerate(cards, start=1):
        if not card.get("problemNumber"):
            card["problemNumber"] = idx
        card["problemNumberFormatted"] = f"#{card['problemNumber']:03d}"

    topics = sorted({card["topic"] for card in cards if card.get("topic")})
    patterns = sorted({card["pattern"] for card in cards if card.get("pattern")})
    difficulties = ["Easy", "Medium", "Hard"]

    return {
        "version": 2,
        "problemCount": len(cards),
        "sourceCount": sum(len(card["sources"]) for card in cards),
        "groups": sorted({group for card in cards for group in card["groups"]}),
        "topics": topics,
        "patterns": patterns,
        "difficulties": difficulties,
        "cards": cards,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent / "catalog.json")
    args = parser.parse_args()

    catalog = build_catalog(args.root.resolve())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(catalog, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        f"Built {catalog['problemCount']} cards from "
        f"{catalog['sourceCount']} source files: {args.output}"
    )


if __name__ == "__main__":
    main()
