# Factorial of Number

- **Problem Number**: #060
- **Difficulty**: Easy
- **Topic**: Math & Number Theory
- **Pattern**: Iterative Product Accumulator
- **LeetCode Equivalent**: [LC 172: Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/)

## Active recall
How do you calculate n! for non-negative integers?

## Core idea
Base cases: 0! = 1, 1! = 1. Iteratively multiply fact *= i for i from 2 up to n. Use 64-bit integer (long) or BigInteger for larger values.

## Hints
- **Hint 1**: 0! is defined as 1.
- **Hint 2**: Factorials grow super-exponentially; use 64-bit integer types.

## Pattern
**Pattern**: Iterative Product Accumulator
Use when: Math & Number Theory problems require efficient traversal or optimal sub-structure.

## Trick
Factorial of 0 is 1. An iterative loop from 1 to N avoids call stack overhead.

## Complexity
Time: O(N). Space: O(1).

## Edge cases
- n = 0: returns 1.
- n = 1: returns 1.
