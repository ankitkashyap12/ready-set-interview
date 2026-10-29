# DSA Revision Cards & Active-Recall Deck

A local-first, zero-dependency active recall study desk for the 100+ problem solutions in this repository. It features spaced-repetition scheduling, progressive hints, pattern taxonomies, difficulty levels, LeetCode equivalent links, and an automated agent framework for maintaining problem metadata.

---

## 🚀 Run Locally

From the repository root, build the catalog and start a local static server:

```sh
python3 revision/build_catalog.py
python3 -m http.server 8000
```

Open [http://localhost:8000/revision/](http://localhost:8000/revision/) in your browser.

- **Local & Private**: Review progress, ratings, and intervals are saved in browser `localStorage` under `dsa-revision-progress-v1`. No external APIs, logins, or tracking.
- **Offline Ready**: Operates completely offline with fast local search and zero CDN scripts.

---

## ✨ Features & UI Upgrades

- **Deterministic Problem Numbering**: Clean `#001` through `#102` identifiers assigned to every problem, replacing raw filesystem names.
- **Difficulty Badges & Filters**: Clear color-coded indicators for `Easy` (Green), `Medium` (Amber), and `Hard` (Coral), filterable from the sidebar.
- **LeetCode Integration**: Direct links to canonical or equivalent LeetCode problems (e.g. `[LC #11 ↗]`, `[LC #849 ↗]`) with problem number and problem title.
- **Progressive Hints Drawer (`H`)**: Interview-style hints: click "Need a hint?" or press `H` to reveal Hint 1, then Hint 2, before revealing the full answer.
- **Structured Answer Grid**:
  - **Core Idea & Approach**: Intuition and step-by-step logic.
  - **Pattern & Technique**: Reusable algorithm pattern and applicability.
  - **Key Trick & Invariant**: Highlighted callout card with the mathematical or pointer invariant.
  - **Time & Space Complexity**: Asymptotic complexity $O(...)$.
  - **Edge Cases Checklist**: Bulleted checklist of boundary cases.
- **Solution Reference & Clipboard Copy**: View source code in Java, Python, C++, etc., with a 1-click "Copy code" button (`Copied! ✓`).
- **Mastery Progress Bar**: Visual progress tracking in the header showing Mastered (Good/Easy), In Progress (Again/Hard), and Unreviewed problems.
- **Full Keyboard Navigation**:
  - `Space` — Reveal approach / reveal reference code
  - `H` — Toggle or unfold progressive hints
  - `C` — Toggle reference code
  - `1`, `2`, `3`, `4` — Rate recall (`Again`, `Hard`, `Good`, `Easy`)
  - `←` / `→` — Navigate to previous / next problem
  - `/` — Focus search input

---

## 🤖 Framework for Adding New Problems (`manage_problems.py`)

For AI agents and human contributors adding new problems, a CLI tool and schema are provided to ensure 100% metadata compliance.

See [FRAMEWORK.md](./FRAMEWORK.md) for the full protocol.

### Quick Commands

```sh
# 1. Audit all problem folders for metadata compliance (exit code 0 if compliant)
python3 revision/manage_problems.py audit

# 2. Scaffold a new problem REVISION.md template with auto-assigned problem number
python3 revision/manage_problems.py scaffold <folder-name>

# 3. Sync catalog.json with the latest problem files
python3 revision/manage_problems.py sync
```

### Standard `REVISION.md` Format

```md
# Problem Title

- **Problem Number**: #103
- **Difficulty**: Medium
- **Topic**: Two Pointers
- **Pattern**: Inward Shrinking Two Pointers
- **LeetCode Equivalent**: [LC 11: Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

## Active recall
What is the core question to test before looking at the solution?

## Core idea
Explain the main intuition and algorithmic steps.

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
```
