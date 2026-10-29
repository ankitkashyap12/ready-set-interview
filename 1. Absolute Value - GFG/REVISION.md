# Absolute Value

- **Problem Number**: #052
- **Difficulty**: Easy
- **Topic**: Math & Number Theory
- **Pattern**: Branchless / Conditional Sign Inversion
- **LeetCode Equivalent**: [Math.abs Implementation](https://leetcode.com/problems/calculate-money-in-leetcode-bank/)

## Active recall
How do you compute the absolute value of an integer without using library functions?

## Core idea
If the number is negative (I < 0), return -I; otherwise return I. In bitwise manipulation, (n ^ (n >> 31)) - (n >> 31) computes absolute value branchlessly.

## Hints
- **Hint 1**: Check if the number is less than zero.
- **Hint 2**: Remember that negating a negative number yields its positive magnitude.

## Pattern
**Pattern**: Branchless / Conditional Sign Inversion
Use when: Math & Number Theory problems require efficient traversal or optimal sub-structure.

## Trick
In 32-bit signed two's complement, watch out for Integer.MIN_VALUE (-2^31), as -MIN_VALUE overflows 32-bit signed int.

## Complexity
Time: O(1). Space: O(1).

## Edge cases
- Zero: 0 -> 0.
- Negative numbers: -32 -> 32.
- Integer MIN_VALUE.
