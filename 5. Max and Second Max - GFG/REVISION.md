# Max and Second Max

- **Problem Number**: #063
- **Difficulty**: Easy
- **Topic**: Arrays & Hashing
- **Pattern**: Single Pass Two-Variable Tracking
- **LeetCode Equivalent**: [Second Largest Element](https://leetcode.com/problems/third-maximum-number/)

## Active recall
How do you find the largest and second distinct largest elements in an array in a single pass?

## Core idea
Initialize max = -1, secondMax = -1. For each x in array: if x > max: secondMax = max, max = x. Else if x < max and x > secondMax: secondMax = x. Return [max, secondMax].

## Hints
- **Hint 1**: Track both maximum and strictly smaller second maximum in one loop.
- **Hint 2**: When a new maximum is found, what happens to the old maximum? It becomes secondMax.

## Pattern
**Pattern**: Single Pass Two-Variable Tracking
Use when: Arrays & Hashing problems require efficient traversal or optimal sub-structure.

## Trick
Only update secondMax when x < max to ensure the second maximum is STRICTLY distinct from the maximum.

## Complexity
Time: O(N) single pass. Space: O(1) auxiliary space.

## Edge cases
- All elements identical: [5, 5, 5] -> max = 5, secondMax = -1.
- Array with two elements.
- Negative numbers.
