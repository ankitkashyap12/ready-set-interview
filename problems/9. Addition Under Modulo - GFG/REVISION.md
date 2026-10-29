# Addition Under Modulo

- **Problem Number**: #070
- **Difficulty**: Easy
- **Topic**: Math & Number Theory
- **Pattern**: Modular Arithmetic Addition Identity
- **LeetCode Equivalent**: [Modular Arithmetic Operations](https://leetcode.com/problems/super-pow/)

## Active recall
How do you calculate (a + b) % M preventing 64-bit integer overflow?

## Core idea
Modular addition rule: (a + b) % M = ((a % M) + (b % M)) % M. Taking modulo before adding prevents large operands from overflowing the integer limit.

## Hints
- **Hint 1**: Take modulo of individual terms first.
- **Hint 2**: ((a % M) + (b % M)) % M prevents overflow.

## Pattern
**Pattern**: Modular Arithmetic Addition Identity
Use when: Math & Number Theory problems require efficient traversal or optimal sub-structure.

## Trick
In languages with fixed integer sizes, reduce both operands modulo M first to keep their sum within the representation limits.

## Complexity
Time: O(1). Space: O(1).

## Edge cases
- a + b exceeding 32-bit integer range.
- M = 10^9 + 7 (standard competitive programming modulo).
