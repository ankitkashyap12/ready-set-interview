# Missing Number

- **Problem Number**: #026
- **Difficulty**: Easy
- **Topic**: Bit Manipulation
- **Pattern**: XOR Cancellation / Gauss Sum
- **LeetCode Equivalent**: [LC 268: Missing Number](https://leetcode.com/problems/missing-number/)

## Active recall
Given an array containing n distinct numbers in the range [0, n], how do you find the one missing number in O(N) time and O(1) space?

## Core idea
Approach 1 (XOR): XOR all numbers from 0 to n and XOR all numbers in the array. Since x ^ x = 0 and x ^ 0 = x, all present numbers cancel out, leaving exactly the missing number. Approach 2 (Gauss Sum): expectedSum = n * (n + 1) // 2. Missing = expectedSum - sum(nums).

## Hints
- **Hint 1**: What happens when you XOR a number with itself?
- **Hint 2**: XORing indices 0..n and array elements together cancels out everything except the missing value.

## Pattern
**Pattern**: XOR Cancellation / Gauss Sum
Use when: Bit Manipulation problems require efficient traversal or optimal sub-structure.

## Trick
XOR avoids any possibility of integer overflow that could occur with Gauss sum on large n.

## Complexity
Time: O(N) single pass. Space: O(1) constant extra memory.

## Edge cases
- Missing 0: [1, 2, 3] -> 0.
- Missing n: [0, 1, 2] -> 3.
- Single element: [0] -> 1, [1] -> 0.
