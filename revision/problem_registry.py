#!/usr/bin/env python3
"""Unified Problem Registry containing full metadata for all 102 problems in the repository."""

from pathlib import Path
from generate_all_revisions import PROBLEMS_DATA
from gfg_data import GFG_PROBLEMS
from ucsd_data import UCSD_PROBLEMS

# Combine and assign sequential problem numbers 1..102
ALL_PROBLEMS = []

# Group 1: LeetCode Problems (1 to 27)
# Group 2: AlgoExpert Problems (28 to 51)
# Group 3: GeeksforGeeks Problems (52 to 72)
# Group 4: UC San Diego Algorithmic Toolbox (73 to 102)

combined_raw = PROBLEMS_DATA + GFG_PROBLEMS + UCSD_PROBLEMS

for idx, prob in enumerate(combined_raw, start=1):
    item = dict(prob)
    item["problem_number"] = idx
    ALL_PROBLEMS.append(item)

PROBLEMS_BY_FOLDER = {p["folder"]: p for p in ALL_PROBLEMS}

def format_revision_markdown(prob: dict) -> str:
    lc_text = "None"
    if prob.get("lc_url"):
        lc_num_prefix = f"LC {prob['lc_number']}: " if prob.get("lc_number") else ""
        lc_title = prob.get("lc_title") or prob["title"]
        lc_text = f"[{lc_num_prefix}{lc_title}]({prob['lc_url']})"

    hints_formatted = "\n".join(f"- **Hint {i+1}**: {h}" for i, h in enumerate(prob.get("hints", [])))
    edge_cases_formatted = "\n".join(f"- {ec}" for ec in prob.get("edge_cases", []))

    return f"""# {prob['title']}

- **Problem Number**: #{prob['problem_number']:03d}
- **Difficulty**: {prob['difficulty']}
- **Topic**: {prob['topic']}
- **Pattern**: {prob['pattern']}
- **LeetCode Equivalent**: {lc_text}

## Active recall
{prob['recall']}

## Core idea
{prob['concept']}

## Hints
{hints_formatted}

## Pattern
**Pattern**: {prob['pattern']}
Use when: {prob['topic']} problems require efficient traversal or optimal sub-structure.

## Trick
{prob['trick']}

## Complexity
{prob['complexity']}

## Edge cases
{edge_cases_formatted}
"""

def write_all_revisions(root: Path = Path('.')):
    written = 0
    for prob in ALL_PROBLEMS:
        folder = (root / "problems" / prob["folder"]) if (root / "problems").is_dir() else (root / prob["folder"])
        if folder.is_dir():
            md_path = folder / "REVISION.md"
            content = format_revision_markdown(prob)
            md_path.write_text(content, encoding="utf-8")
            written += 1
    return written

if __name__ == "__main__":
    count = write_all_revisions()
    print(f"Successfully generated REVISION.md for {count} problems.")
