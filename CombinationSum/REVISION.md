# Combination Sum

- **Problem Number**: #031
- **Difficulty**: Medium
- **Topic**: Backtracking
- **Pattern**: Backtracking with Unbounded Element Reuse
- **LeetCode Equivalent**: [LC 39: Combination Sum](https://leetcode.com/problems/combination-sum/)

## Active recall
How do you find all unique combinations of candidate numbers that sum to a target when each number may be used an unlimited number of times?

## Core idea
Sort candidates. Use recursive backtracking: backtrack(startIndex, currentCombination, remainingTarget). If remainingTarget == 0, save a copy of currentCombination. If remainingTarget < 0, return. Loop index i from startIndex to len(candidates) - 1: add candidates[i] to combination, recurse with same index i (allowing reuse) and remainingTarget - candidates[i], then backtrack by popping candidates[i].

## Hints
- **Hint 1**: Can you choose to either include candidates[i] again or move to candidates[i+1]?
- **Hint 2**: Sorting candidates allows early termination of the loop when candidates[i] > remainingTarget.

## Pattern
**Pattern**: Backtracking with Unbounded Element Reuse
Use when: Backtracking problems require efficient traversal or optimal sub-structure.

## Trick
Passing startIndex = i into the recursive call allows unlimited reuse of the current element while preventing duplicate combinations in different orders.

## Complexity
Time: O(2^T) where T is target / min(candidates). Space: O(T) maximum recursion depth.

## Edge cases
- Target smaller than minimum candidate: returns empty list.
- Single candidate dividing target evenly: candidates=[2], target=6 -> [[2, 2, 2]].
- Ensure combinations returned are deep copies of current state.
