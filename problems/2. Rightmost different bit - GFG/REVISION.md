# Rightmost Different Bit

- **Problem Number**: #056
- **Difficulty**: Easy
- **Topic**: Bit Manipulation
- **Pattern**: XOR + Two's Complement LSB Isolation
- **LeetCode Equivalent**: [LC 461: Hamming Distance](https://leetcode.com/problems/hamming-distance/)

## Active recall
Given two numbers m and n, how do you find the 1-based position of the rightmost bit where they differ?

## Core idea
XOR m and n: x = m ^ n. In x, set bits represent positions where m and n differ. Finding the rightmost different bit is equivalent to finding the first set bit of x. Compute isolated = x & -x and return log2(isolated) + 1. If m == n, return -1.

## Hints
- **Hint 1**: Which bitwise operation highlights differing bits between two numbers? XOR!
- **Hint 2**: Once you have m ^ n, find its lowest set bit using x & -x.

## Pattern
**Pattern**: XOR + Two's Complement LSB Isolation
Use when: Bit Manipulation problems require efficient traversal or optimal sub-structure.

## Trick
m ^ n produces 1s exactly where m and n have different bits. Then x & -x isolates the rightmost difference in O(1).

## Complexity
Time: O(1) bitwise operations. Space: O(1).

## Edge cases
- m == n: numbers are identical, return -1.
- Difference is at bit 0 (one even, one odd): returns 1.
