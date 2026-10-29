# Sorted Squared Array

- **Problem Number**: #043
- **Difficulty**: Easy
- **Topic**: Two Pointers
- **Pattern**: Opposite Ends Pointers Filling Result from Back
- **LeetCode Equivalent**: [LC 977: Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)

## Active recall
Given a sorted array of integers that may contain negative numbers, how do you return an array of their squares, also in sorted order, in O(N) time?

## Core idea
Since the input is sorted, the largest squares must come from either the most negative numbers at the left end or the largest positive numbers at the right end. Initialize left = 0, right = n - 1, and fill result array from index n - 1 down to 0. In each step: compare abs(array[left]) with abs(array[right]). Place the larger square at result[idx], and advance that pointer inward.

## Hints
- **Hint 1**: Where can the largest square in the array come from? Only from the extreme left or extreme right!
- **Hint 2**: Fill the output array backwards from largest to smallest.

## Pattern
**Pattern**: Opposite Ends Pointers Filling Result from Back
Use when: Two Pointers problems require efficient traversal or optimal sub-structure.

## Trick
Filling from back to front (index n-1 down to 0) avoids needing to reverse the output array.

## Complexity
Time: O(N) single pass through the array. Space: O(N) for the result array.

## Edge cases
- All negative numbers: [-5, -3, -1] -> squares are reversed.
- All positive numbers: [1, 2, 3] -> squares remain in original order.
- Mix of negative and positive with zeros: [-4, 0, 1, 4].
