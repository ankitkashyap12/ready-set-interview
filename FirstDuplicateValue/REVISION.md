# First Duplicate Value

- **Problem Number**: #032
- **Difficulty**: Medium
- **Topic**: Arrays & Hashing
- **Pattern**: In-place Sign Flipping (Index as Hash Key)
- **LeetCode Equivalent**: [LC 287: Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)

## Active recall
Given an array of integers between 1 and n inclusive, how do you find the first duplicate value in O(N) time and O(1) auxiliary space?

## Core idea
Since values are bounded in [1, n], map each value val = abs(array[i]) to index val - 1. Check the sign of array[val - 1]: if array[val - 1] < 0, then val has been seen before; return val immediately as the first duplicate! Otherwise, mark it seen by negating array[val - 1] = -array[val - 1].

## Hints
- **Hint 1**: The values are between 1 and n, matching the array indices [0, n - 1].
- **Hint 2**: Can you use the sign of array[value - 1] as a visited marker without allocating a set?

## Pattern
**Pattern**: In-place Sign Flipping (Index as Hash Key)
Use when: Arrays & Hashing problems require efficient traversal or optimal sub-structure.

## Trick
Always use abs(array[i]) to get the original number value, because preceding elements may have already been negated.

## Complexity
Time: O(N) single pass with early exit. Space: O(1) in-place sign modification.

## Edge cases
- No duplicates: return -1.
- Multiple duplicates: return the one whose second appearance has the minimum index.
- All elements duplicate: [2, 1, 5, 2, 3, 3, 4] -> returns 2.
