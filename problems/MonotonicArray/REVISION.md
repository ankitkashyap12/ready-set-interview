# Monotonic Array

- **Problem Number**: #038
- **Difficulty**: Easy
- **Topic**: Arrays & Hashing
- **Pattern**: Single Pass Non-Decreasing / Non-Increasing Check
- **LeetCode Equivalent**: [LC 896: Monotonic Array](https://leetcode.com/problems/monotonic-array/)

## Active recall
How do you verify whether an array is monotonic (entirely non-increasing or non-decreasing) in a single pass?

## Core idea
Maintain two boolean flags: isNonDecreasing = true and isNonIncreasing = true. Iterate through adjacent elements from i = 1 to n - 1. If array[i] < array[i-1], isNonDecreasing = false. If array[i] > array[i-1], isNonIncreasing = false. At the end, return isNonDecreasing || isNonIncreasing.

## Hints
- **Hint 1**: An array is monotonic if it never increases OR if it never decreases.
- **Hint 2**: Track both possibilities simultaneously in a single pass.

## Pattern
**Pattern**: Single Pass Non-Decreasing / Non-Increasing Check
Use when: Arrays & Hashing problems require efficient traversal or optimal sub-structure.

## Trick
Early break when neither flag is true: if (!isNonDecreasing && !isNonIncreasing) return false.

## Complexity
Time: O(N) single pass. Space: O(1) constant memory.

## Edge cases
- Arrays of length 0, 1, or 2 are always monotonic.
- All identical values: [1, 1, 1] -> true.
- Flat plateaus with direction change: [1, 2, 2, 3, 2] -> false.
