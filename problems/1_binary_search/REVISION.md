# Binary Search

- **Problem Number**: #073
- **Difficulty**: Easy
- **Topic**: Binary Search
- **Pattern**: Sorted Array Halving
- **LeetCode Equivalent**: [LC 704: Binary Search](https://leetcode.com/problems/binary-search/)

## Active recall
How do you search for a target value in a sorted array in guaranteed O(log N) time?

## Core idea
Set low = 0, high = n - 1. While low <= high: mid = low + (high - low) // 2. If a[mid] == target, return mid. If a[mid] < target, target must be in right half (low = mid + 1). If a[mid] > target, target must be in left half (high = mid - 1). Return -1 if not found.

## Hints
- **Hint 1**: At each step, compare target with the middle element.
- **Hint 2**: Half of the remaining search space is eliminated in each iteration.

## Pattern
**Pattern**: Sorted Array Halving
Use when: Binary Search problems require efficient traversal or optimal sub-structure.

## Trick
Compute mid using low + (high - low) // 2 to avoid integer overflow that occurs with (low + high) // 2 in 32-bit languages.

## Complexity
Time: O(log N) iterations. Space: O(1) iterative.

## Edge cases
- Target not present: returns -1.
- Target at index 0 or index n - 1.
- Single element array.
