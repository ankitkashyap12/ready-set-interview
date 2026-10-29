# DSA Problem Revision Framework & Agent Protocol

This framework ensures that all DSA problems in the repository maintain standardized, high-quality active-recall flashcard metadata (`REVISION.md`) and are automatically synced to the interactive flashcard study desk.

---

## 🤖 Protocol for AI Agents Adding New Problems

When an AI agent or contributor adds a new problem or solution to this repository, follow this mandatory 5-step workflow:

### Step 1: Add Problem Directory & Solution Code
Create the problem folder at repository root with at least one solution file:
```bash
mkdir 0042-trapping-rain-water
# Add solution code (e.g. Solution.java, solution.py, solution.cpp, etc.)
```

### Step 2: Scaffold the REVISION.md Template
Run the management framework CLI to generate a pre-filled template with the next sequential problem number:
```bash
python3 revision/manage_problems.py scaffold 0042-trapping-rain-water
```

### Step 3: Fill Out the Required REVISION.md Metadata
Edit `0042-trapping-rain-water/REVISION.md` adhering to the required schema:

```markdown
# Trapping Rain Water

- **Problem Number**: #103
- **Difficulty**: Hard
- **Topic**: Two Pointers
- **Pattern**: Two Pointers with Inward Max Tracking
- **LeetCode Equivalent**: [LC 42: Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

## Active recall
Given an elevation map represented by non-negative integers, how do you compute how much water can be trapped after raining in O(N) time and O(1) space?

## Core idea
Water trapped above bar i is determined by `min(maxLeft, maxRight) - height[i]`. Instead of precomputing prefix and suffix arrays in O(N) space, use two pointers converging from both ends (`left = 0`, `right = n - 1`) maintaining `leftMax` and `rightMax`. At each step, process the side with the smaller max bar, since that smaller max strictly limits the water height regardless of future taller bars on the other side.

## Hints
- **Hint 1**: The water level above any index is strictly bounded by the smaller of the maximum height to its left and to its right.
- **Hint 2**: If `leftMax < rightMax`, the height of trapped water at `left` is entirely determined by `leftMax`, so you can record water and advance `left`.

## Pattern
**Pattern**: Two Pointers with Inward Max Tracking
Use when: A quantity at index `i` depends on the minimum of the maximum elements to its left and right.

## Trick
If `leftMax < rightMax`, you know with certainty that the right boundary is >= `leftMax`, so the bottleneck is `leftMax`. Water trapped is `max(0, leftMax - height[left])`.

## Complexity
Time: O(N) single pass converging pointers. Space: O(1) auxiliary space.

## Edge cases
- Array with fewer than 3 bars: cannot trap water, return 0.
- Strictly monotonic elevation (strictly increasing or decreasing): traps 0.
- Flat terrain or all identical heights: traps 0.
```

### Step 4: Audit Compliance
Run the automated audit tool to verify 100% compliance across all required sections:
```bash
python3 revision/manage_problems.py audit
```
The audit checks:
- [x] Presence of `REVISION.md`
- [x] Header metadata: Problem Number, Difficulty (`Easy` | `Medium` | `Hard`), Topic, Pattern, LeetCode link
- [x] Required markdown sections: `## Active recall`, `## Core idea`, `## Hints`, `## Pattern`, `## Trick`, `## Complexity`, `## Edge cases`
- [x] At least one code file present in supported languages

### Step 5: Sync Catalog
Regenerate `catalog.json` for the web UI:
```bash
python3 revision/manage_problems.py sync
```

---

## 🛠️ CLI Reference (`manage_problems.py`)

| Command | Purpose |
|---|---|
| `python3 revision/manage_problems.py audit` | Audits all problem directories for schema and metadata compliance. Exits with code 0 if 100% compliant, 1 if issues exist. |
| `python3 revision/manage_problems.py scaffold <folder>` | Scaffolds a new `REVISION.md` with boilerplate headings, auto-detected title, and next problem number. |
| `python3 revision/manage_problems.py sync` | Rebuilds `revision/catalog.json` from disk. |

---

## 🏷️ Standard Taxonomies

### Difficulty Levels
- `Easy`: Basic implementation, direct pointer/hash map usage, elementary math.
- `Medium`: Classic algorithmic patterns (sliding window, two pointers, standard DP, trees, intervals, backtracking).
- `Hard`: Multi-dimensional DP, divide & conquer geometry/sweep-line, complex state machines.

### Standard Topics
- `Arrays & Hashing`
- `Two Pointers`
- `Sliding Window`
- `Stack`
- `Binary Search`
- `Trees`
- `Dynamic Programming`
- `Greedy`
- `Divide & Conquer`
- `Bit Manipulation`
- `Math & Number Theory`
- `Sorting`
- `Matrix`
- `Intervals`
- `Backtracking`
- `Design / Cache`

