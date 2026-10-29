# Last Digit of Sum of Fibonacci Squares

- **Problem Number**: #102
- **Difficulty**: Medium
- **Topic**: Math & Number Theory
- **Pattern**: Fibonacci Area Geometry Identity (F(n) * F(n+1))
- **LeetCode Equivalent**: [LC 509: Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)

## Active recall
How do you find the last digit of F(0)^2 + F(1)^2 + ... + F(n)^2 for n up to 10^14?

## Core idea
Geometric identity of tiling Fibonacci squares into a rectangle: sum_{i=0}^n F(i)^2 = F(n) * F(n + 1). Therefore, the sum modulo 10 is (F(n) * F(n + 1)) % 10 = ((F(n % 60) % 10) * (F((n + 1) % 60) % 10)) % 10.

## Hints
- **Hint 1**: Think of Fibonacci squares forming a rectangle of dimensions F(n) by F(n + 1).
- **Hint 2**: Sum of squares identity: sum(F_i^2) = F(n) * F(n + 1).

## Pattern
**Pattern**: Fibonacci Area Geometry Identity (F(n) * F(n+1))
Use when: Math & Number Theory problems require efficient traversal or optimal sub-structure.

## Trick
The sum of squares equals the area of rectangle F(n) * F(n + 1). Reduce indices modulo 60 and multiply their last digits.

## Complexity
Time: O(1) (at most 60 Fibonacci iterations). Space: O(1).

## Edge cases
- n = 0: 0.
- n = 1: 1.
- Product of last digits ending in 0.
