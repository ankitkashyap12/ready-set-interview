#!/usr/bin/env python3
"""
Framework CLI for Managing DSA Problem Metadata & Active Recall Cards.
Used by AI agents and developers to audit, scaffold, and sync problem revision data.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

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

CODE_EXTENSIONS = {
    ".c", ".cc", ".cpp", ".cs", ".go", ".h", ".hs", ".hpp",
    ".java", ".js", ".jsx", ".kt", ".php", ".py", ".rb",
    ".rs", ".swift", ".ts", ".tsx"
}

REQUIRED_SECTIONS = [
    ("Core idea / Approach", r"^\s{0,3}#{1,4}\s+(?:core idea|approach|concept|solution idea)\b"),
    ("Active recall prompt", r"^\s{0,3}#{1,4}\s+(?:active recall|recall|prompt|question)\b"),
    ("Hints", r"^\s{0,3}#{1,4}\s+(?:hints|hint)\b"),
    ("Pattern", r"^\s{0,3}#{1,4}\s+(?:pattern|technique)\b"),
    ("Trick / Invariant", r"^\s{0,3}#{1,4}\s+(?:trick|invariant|gotcha)\b"),
    ("Complexity", r"^\s{0,3}#{1,4}\s+(?:complexity|time and space)\b"),
    ("Edge cases", r"^\s{0,3}#{1,4}\s+(?:edge cases|pitfalls)\b"),
]

METADATA_FIELDS = [
    ("Problem Number", r"[-*]?\s*\*{0,2}(?:Problem Number|Problem #|\bNumber\b)\*{0,2}:\s*#?(\d+)"),
    ("Difficulty", r"[-*]?\s*\*{0,2}Difficulty\*{0,2}:\s*(Easy|Medium|Hard)\b"),
    ("Topic", r"[-*]?\s*\*{0,2}Topic\*{0,2}:\s*([^\n\r]+)"),
    ("Pattern", r"[-*]?\s*\*{0,2}Pattern\*{0,2}:\s*([^\n\r]+)"),
    ("LeetCode Link", r"[-*]?\s*\*{0,2}(?:LeetCode Equivalent|LeetCode Link|LeetCode)\*{0,2}:\s*([^\n\r]+)"),
]


def find_problem_folders(root: Path) -> List[Path]:
    """Return all directories containing source code files."""
    folders: List[Path] = []
    scan_dir = root / "problems" if (root / "problems").is_dir() else root
    for d in sorted(scan_dir.iterdir(), key=lambda p: p.name.lower()):
        if not d.is_dir() or d.name.startswith(".") or d.name in IGNORED_DIRECTORIES or d.name == "problems":
            continue
        code_files = [f for f in d.iterdir() if f.is_file() and f.suffix.lower() in CODE_EXTENSIONS]
        if code_files:
            folders.append(d)
    return folders


def audit_problem(folder: Path) -> Dict[str, object]:
    """Audit a single problem folder for REVISION.md compliance."""
    rev_path = folder / "REVISION.md"
    has_rev = rev_path.is_file()
    text = rev_path.read_text(encoding="utf-8", errors="replace") if has_rev else ""

    missing_sections = []
    if has_rev:
        for section_name, pattern in REQUIRED_SECTIONS:
            if not re.search(pattern, text, re.IGNORECASE | re.MULTILINE):
                missing_sections.append(section_name)

    missing_meta = []
    meta_values: Dict[str, str] = {}
    if has_rev:
        for field_name, pattern in METADATA_FIELDS:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                meta_values[field_name] = match.group(1).strip()
            else:
                missing_meta.append(field_name)

    code_files = [f.name for f in folder.iterdir() if f.is_file() and f.suffix.lower() in CODE_EXTENSIONS]

    is_compliant = (
        has_rev
        and len(missing_sections) == 0
        and len(missing_meta) == 0
        and len(code_files) > 0
    )

    return {
        "folder": folder.name,
        "has_revision": has_rev,
        "code_files": code_files,
        "missing_sections": missing_sections,
        "missing_meta": missing_meta,
        "meta": meta_values,
        "is_compliant": is_compliant,
    }


def run_audit(root: Path) -> int:
    """Run full audit across all problem folders and report compliance."""
    folders = find_problem_folders(root)
    total = len(folders)
    compliant_count = 0
    issues: List[Dict[str, object]] = []

    print(f"\n🔍 Auditing {total} problem folders for DSA Revision Metadata...")
    print("=" * 70)

    for folder in folders:
        result = audit_problem(folder)
        if result["is_compliant"]:
            compliant_count += 1
        else:
            issues.append(result)

    percentage = (compliant_count / total * 100) if total else 0
    print(f"Compliance Status: {compliant_count} / {total} problems compliant ({percentage:.1f}%)\n")

    if issues:
        print("⚠️  Problems requiring attention:")
        print("-" * 70)
        for issue in issues:
            print(f"📁 {issue['folder']}:")
            if not issue["has_revision"]:
                print("   ❌ Missing REVISION.md (run: python3 revision/manage_problems.py scaffold '<folder>')")
            else:
                if issue["missing_meta"]:
                    print(f"   ⚠️  Missing header metadata: {', '.join(issue['missing_meta'])}")
                if issue["missing_sections"]:
                    print(f"   ⚠️  Missing sections: {', '.join(issue['missing_sections'])}")
            print()
        print("=" * 70)
        return 1

    print("✅ All problems have complete REVISION.md notes, topics, patterns, and LC links!")
    print("=" * 70)
    return 0


def scaffold_problem(root: Path, folder_name: str) -> None:
    """Scaffold a REVISION.md template for a new problem folder."""
    target_dir = (root / "problems" / folder_name) if (root / "problems").is_dir() else (root / folder_name)
    if not target_dir.is_dir():
        target_dir.mkdir(parents=True, exist_ok=True)
        print(f"Created problem directory: {target_dir}")

    rev_file = target_dir / "REVISION.md"
    if rev_file.exists():
        print(f"⚠️  {rev_file} already exists. Leaving untouched.")
        return

    # Count existing problems to determine next problem number
    existing = find_problem_folders(root)
    next_num = len(existing)

    # Derive clean title
    clean_title = folder_name.replace("-", " ").replace("_", " ").title()
    clean_title = re.sub(r"^\d+[\s\.\-]+", "", clean_title)

    template = f"""# {clean_title}

- **Problem Number**: #{next_num:03d}
- **Difficulty**: Medium
- **Topic**: Arrays & Hashing
- **Pattern**: Two Pointers / Hash Map
- **LeetCode Equivalent**: [LC XXX: {clean_title}](https://leetcode.com/problems/{folder_name}/)

## Active recall
What is the core question or prompt to test before looking at the solution?

## Core idea
Explain the main intuition and algorithm steps.

## Hints
- **Hint 1**: Progressive hint 1 for the mental model.
- **Hint 2**: Progressive hint 2 for implementation details.

## Pattern
**Pattern**: Named Pattern
Use when: Problem requires optimal search/partitioning.

## Trick
Capture the critical invariant, boundary check, or subtle detail.

## Complexity
Time: O(N). Space: O(1).

## Edge cases
- Empty or single-element inputs.
- Duplicates or boundary extreme values.
"""
    rev_file.write_text(template, encoding="utf-8")
    print(f"✅ Successfully scaffolded {rev_file}")
    print("👉 Next step: fill in the template sections, then run: python3 revision/build_catalog.py")


def main() -> None:
    parser = argparse.ArgumentParser(description="DSA Problem Revision Management Framework")
    subparsers = parser.add_subparsers(dest="command", help="Sub-commands")

    # audit command
    audit_parser = subparsers.add_parser("audit", help="Audit all problems for metadata compliance")
    audit_parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)

    # scaffold command
    scaffold_parser = subparsers.add_parser("scaffold", help="Scaffold a new problem REVISION.md")
    scaffold_parser.add_argument("folder", type=str, help="Problem folder name")
    scaffold_parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)

    # sync command
    sync_parser = subparsers.add_parser("sync", help="Rebuild catalog and ensure all metadata is synced")
    sync_parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)

    args = parser.parse_args()

    if args.command == "audit" or args.command is None:
        root = getattr(args, "root", Path(__file__).resolve().parent.parent)
        exit_code = run_audit(root)
        sys.exit(exit_code)
    elif args.command == "scaffold":
        scaffold_problem(args.root, args.folder)
    elif args.command == "sync":
        import subprocess
        build_script = Path(__file__).resolve().parent / "build_catalog.py"
        subprocess.run([sys.executable, str(build_script)], check=True)


if __name__ == "__main__":
    main()
