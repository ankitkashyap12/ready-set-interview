# Sweet and Savoury

- **Problem Number**: #045
- **Difficulty**: Medium
- **Topic**: Two Pointers
- **Pattern**: Split by Sign + Two Pointers Bounded Optimization
- **LeetCode Equivalent**: [LC 1099: Two Sum Less Than K](https://leetcode.com/problems/two-sum-less-than-k/)

## Active recall
Given sweet dishes (< 0) and savoury dishes (> 0), how do you pair one sweet and one savoury dish such that their combined flavour <= target and is as close to target as possible?

## Core idea
Separate dishes into sweet dishes (negatives) and savoury dishes (positives). Sort sweet dishes by absolute value (or sort sweet ascending and savoury ascending). Use two pointers: sweetIdx = 0, savouryIdx = 0. Compute totalFlavour = sweet[sweetIdx] + savoury[savouryIdx]. If totalFlavour <= target, this is a feasible candidate; update bestPair if target - totalFlavour is smaller, then try to increase flavour by incrementing savouryIdx. If totalFlavour > target, savoury is too strong; decrement savouryIdx or advance sweetIdx.

## Hints
- **Hint 1**: Sweet dishes are negative, savoury are positive. You need exactly one of each.
- **Hint 2**: Sort both lists and use two pointers to find the closest sum <= target.

## Pattern
**Pattern**: Split by Sign + Two Pointers Bounded Optimization
Use when: Two Pointers problems require efficient traversal or optimal sub-structure.

## Trick
Only candidate pairs with combined sum <= target are valid. Among valid candidates, minimize target - combinedSum.

## Complexity
Time: O(N log N) to sort sweet and savoury arrays + O(N) two-pointer scan. Space: O(N) to separate dishes.

## Edge cases
- No sweet dishes or no savoury dishes available: return [0, 0].
- No pair has sum <= target: return [0, 0].
- Exact match: combined flavour == target gives immediate optimal solution.
