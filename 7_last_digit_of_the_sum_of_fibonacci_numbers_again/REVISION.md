# Last Digit of a Partial Fibonacci Sum

- **Problem Number**: #100
- **Difficulty**: Medium
- **Topic**: Math & Number Theory
- **Pattern**: Prefix Sum Difference of Fibonacci Modulo 10
- **LeetCode Equivalent**: [LC 509: Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)

## Active recall
How do you find the last digit of the partial sum F(m) + F(m+1) + ... + F(n) for large m and n?

## Core idea
Partial sum S(m, n) = sum_{i=0}^n F(i) - sum_{i=0}^{m-1} F(i). Using the Fibonacci sum identity: sum_{i=0}^k F(i) = F(k+2) - 1. Therefore S(m, n) = (F(n+2) - 1) - (F(m+1) - 1) = F(n+2) - F(m+1). Compute (F((n + 2) % 60) - F((m + 1) % 60) + 10) % 10.

## Hints
- **Hint 1**: Partial sum from m to n is TotalSum(n) - TotalSum(m - 1).
- **Hint 2**: S(m, n) simplifies cleanly to F(n + 2) - F(m + 1).

## Pattern
**Pattern**: Prefix Sum Difference of Fibonacci Modulo 10
Use when: Math & Number Theory problems require efficient traversal or optimal sub-structure.

## Trick
S(m, n) = F(n + 2) - F(m + 1). Reduce indices modulo 60 and add 10 before modulo to avoid negative answers.

## Complexity
Time: O(1) (at most 60 Fibonacci iterations). Space: O(1).

## Edge cases
- m == n: returns F(m) % 10.
- m = 0: standard sum from 0 to n.
