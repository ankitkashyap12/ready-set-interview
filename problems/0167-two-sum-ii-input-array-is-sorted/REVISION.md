# Two Sum II - Input Array Is Sorted

- **Problem Number**: #016
- **Difficulty**: Medium
- **Topic**: Two Pointers
- **Pattern**: Opposite Ends Converging Pointers
- **LeetCode Equivalent**: [LC 167: Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

## Active recall
Given a 1-indexed sorted array, how do you find two numbers that sum to target in O(N) time and O(1) space?

## Core idea
Initialize left = 0, right = n - 1. Compute currentSum = numbers[left] + numbers[right]. If currentSum == target, return [left + 1, right + 1]. If currentSum < target, increment left to increase the sum. If currentSum > target, decrement right to decrease the sum.

## Hints
- **Hint 1**: The array is already sorted! How can you leverage sorted order to eliminate candidates?
- **Hint 2**: If the sum of extremes is too small, which pointer must move?

## Pattern
**Pattern**: Opposite Ends Converging Pointers
Use when: Two Pointers problems require efficient traversal or optimal sub-structure.

## Trick
Sorted monotonicity guarantees correctness: if numbers[left] + numbers[right] > target, numbers[right] cannot pair with ANY index >= left, so right can safely be decremented.

## Complexity
Time: O(N) since each step moves one pointer closer. Space: O(1) auxiliary space.

## Edge cases
- Negative numbers: [-1, 0], target = -1.
- Duplicate elements: [2, 2], target = 4.
- Remember 1-based indexing in return value.
