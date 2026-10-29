# GP Term

- **Problem Number**: #064
- **Difficulty**: Easy
- **Topic**: Math & Number Theory
- **Pattern**: Geometric Progression Formula (a * r^(n-1))
- **LeetCode Equivalent**: [Geometric Progression Term](https://leetcode.com/problems/powx-n/)

## Active recall
Given first term A and second term B of a geometric progression, how do you find the N-th term?

## Core idea
The common ratio is r = B / A. The N-th term of a GP is given by term_N = A * r^(N - 1) = A * (B / A)^(N - 1).

## Hints
- **Hint 1**: Common ratio r = B / A.
- **Hint 2**: N-th term formula: T_n = A * r^(n-1).

## Pattern
**Pattern**: Geometric Progression Formula (a * r^(n-1))
Use when: Math & Number Theory problems require efficient traversal or optimal sub-structure.

## Trick
Use pow(B / A, N - 1) with double precision floating-point arithmetic.

## Complexity
Time: O(log N) for power computation. Space: O(1).

## Edge cases
- N = 1: returns A.
- N = 2: returns B.
- Ratio < 1: decaying GP.
