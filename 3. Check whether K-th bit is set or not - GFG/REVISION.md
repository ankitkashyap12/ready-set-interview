# Check K-th Bit Set

- **Problem Number**: #057
- **Difficulty**: Easy
- **Topic**: Bit Manipulation
- **Pattern**: Bitwise Shift and Mask ((n >> k) & 1)
- **LeetCode Equivalent**: [LC 191: Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)

## Active recall
How do you check if the k-th bit (0-indexed or 1-indexed) of an integer n is set?

## Core idea
Right shift n by k positions and test the lowest bit: (n >> k) & 1 == 1. Alternatively, create a mask 1 << k and check (n & (1 << k)) != 0.

## Hints
- **Hint 1**: Shift the k-th bit to the 0th position using n >> k, then AND with 1.
- **Hint 2**: Verify whether k is 0-indexed or 1-indexed in the problem statement.

## Pattern
**Pattern**: Bitwise Shift and Mask ((n >> k) & 1)
Use when: Bit Manipulation problems require efficient traversal or optimal sub-structure.

## Trick
Using (n >> k) & 1 avoids potential overflow that can occur when shifting 1 << 31 in signed integers.

## Complexity
Time: O(1). Space: O(1).

## Edge cases
- k == 0 (LSB).
- k == 31 (sign bit or MSB).
- n == 0 (all bits 0 -> false).
