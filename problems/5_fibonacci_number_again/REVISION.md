# Huge Fibonacci Number Modulo M

- **Problem Number**: #094
- **Difficulty**: Medium
- **Topic**: Math & Number Theory
- **Pattern**: Pisano Period Modulo M
- **LeetCode Equivalent**: [LC 509: Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)

## Active recall
How do you compute F(n) % m for astronomical n (up to 10^14) and m up to 10^3?

## Core idea
The Fibonacci sequence modulo m is strictly periodic, known as the Pisano Period. The period always begins with 0, 1. Find the period length P by generating Fibonacci numbers modulo m until seeing 0 followed by 1 (at i >= 1). Then F(n) % m = F(n % P) % m. Since P <= 6 * m, finding the period and computing the answer takes O(m) time.

## Hints
- **Hint 1**: The sequence F(n) % m repeats periodically.
- **Hint 2**: Detect the period by looking for the repeat of 0, 1.
- **Hint 3**: Once period length P is found, compute n % P.

## Pattern
**Pattern**: Pisano Period Modulo M
Use when: Math & Number Theory problems require efficient traversal or optimal sub-structure.

## Trick
Pisano period always starts with 0, 1. The period length never exceeds 6 * m, turning an exponential calculation into at most 6000 additions.

## Complexity
Time: O(m) to find Pisano period. Space: O(1) auxiliary variables.

## Edge cases
- n = 0: 0.
- n = 1: 1 % m.
- m = 2: period is 3.
