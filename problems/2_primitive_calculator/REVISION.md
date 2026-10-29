# Primitive Calculator

- **Problem Number**: #083
- **Difficulty**: Medium
- **Topic**: Dynamic Programming
- **Pattern**: Shortest Path 1D DP with Predecessor Backtracking
- **LeetCode Equivalent**: [LC 279: Perfect Squares](https://leetcode.com/problems/perfect-squares/)

## Active recall
Given an integer n, how do you find the minimum operations (+1, *2, *3) to reach n starting from 1, and reconstruct the sequence?

## Core idea
Greedy fails (e.g. for n = 10: greedy does 10 -> 9 -> 3 -> 1 takes 3 ops, but 10 -> 5 -> 4 -> 2 -> 1 takes 4; for other numbers greedy gives suboptimal steps). Use DP: minOps[i] is min operations to reach i from 1. For i from 2 to n: minOps[i] = minOps[i - 1] + 1; if i % 2 == 0: minOps[i] = min(minOps[i], minOps[i // 2] + 1); if i % 3 == 0: minOps[i] = min(minOps[i], minOps[i // 3] + 1). Backtrack from n to 1 to reconstruct sequence.

## Hints
- **Hint 1**: Why does greedy fail? (e.g. dividing by 3 whenever possible doesn't always lead to the shortest path).
- **Hint 2**: Store min operations for all numbers from 1 to n in a DP table, then trace backwards.

## Pattern
**Pattern**: Shortest Path 1D DP with Predecessor Backtracking
Use when: Dynamic Programming problems require efficient traversal or optimal sub-structure.

## Trick
Backtrack from n down to 1 by checking which transition (curr - 1, curr / 2, curr / 3) achieved minOps[curr] - 1.

## Complexity
Time: O(N) linear DP. Space: O(N) array to store minimum operations.

## Edge cases
- n = 1: 0 operations, sequence [1].
- Powers of 3: optimal is repeated *3.
- Numbers where +1 early enables a *3 division.
