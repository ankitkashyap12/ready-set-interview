# Reverse Array in Groups

- **Problem Number**: #068
- **Difficulty**: Easy
- **Topic**: Two Pointers
- **Pattern**: Block-wise Two Pointers Reversal
- **LeetCode Equivalent**: [LC 189: Rotate Array](https://leetcode.com/problems/rotate-array/)

## Active recall
Given an array and integer k, how do you reverse every contiguous sub-array of size k in-place?

## Core idea
Iterate i from 0 to n in steps of k. For each block, define left = i and right = min(i + k - 1, n - 1). Reverse the sub-array arr[left..right] in-place using two pointers: while left < right: swap(arr[left], arr[right]), left++, right--.

## Hints
- **Hint 1**: Process the array in chunks of size k.
- **Hint 2**: Use min(i + k - 1, n - 1) as the right boundary to handle the final partial chunk.

## Pattern
**Pattern**: Block-wise Two Pointers Reversal
Use when: Two Pointers problems require efficient traversal or optimal sub-structure.

## Trick
The right boundary of the last group must be clamped to min(i + k - 1, n - 1) so trailing elements are reversed safely without index errors.

## Complexity
Time: O(N) every element swapped at most once. Space: O(1) in-place.

## Edge cases
- k >= n: reverses the entire array.
- k == 1: array remains unchanged.
- n is not a multiple of k: last chunk of size n % k is reversed correctly.
