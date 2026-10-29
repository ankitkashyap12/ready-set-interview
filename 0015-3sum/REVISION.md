# 3Sum

- **Problem Number**: #006
- **Difficulty**: Medium
- **Topic**: Two Pointers
- **Pattern**: Sort + Fixed Pivot + Two Pointers
- **LeetCode Equivalent**: [LC 15: 3Sum](https://leetcode.com/problems/3sum/)

## Active recall
How do you find all unique triplets in an array that sum to zero in O(N^2) time without duplicate triplets?

## Core idea
Sort the array. Iterate pivot i from 0 to n - 3. If nums[i] > 0, stop early (three positive numbers cannot sum to 0). Skip duplicate pivots if nums[i] == nums[i-1]. For each i, run two pointers left = i + 1, right = n - 1. If sum == 0, record triplet and advance both pointers past duplicate values. If sum < 0, advance left; if sum > 0, decrement right.

## Hints
- **Hint 1**: Can sorting simplify finding pairs and skipping duplicates?
- **Hint 2**: Fix the first element, then reduce the problem to 2Sum on the remaining sorted sub-array.

## Pattern
**Pattern**: Sort + Fixed Pivot + Two Pointers
Use when: Two Pointers problems require efficient traversal or optimal sub-structure.

## Trick
Duplicate elimination: skip duplicate pivots (i > 0 and nums[i] == nums[i-1]) and skip duplicates for left and right after finding a valid triplet.

## Complexity
Time: O(N^2) total (O(N log N) sort + O(N) iterations of O(N) two pointers). Space: O(log N) or O(N) for sorting depending on language.

## Edge cases
- Fewer than 3 elements: [] or [0, 1] -> [].
- All zeros: [0, 0, 0, 0] -> [[0, 0, 0]].
- No valid triplets: [-1, -2, -3, 0].
