# Last Digit of the Sum of Fibonacci Numbers

- **Problem Number**: #098
- **Difficulty**: Medium
- **Topic**: Math & Number Theory
- **Pattern**: Fibonacci Sum Identity (Sum = F(n+2) - 1)
- **LeetCode Equivalent**: [LC 509: Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)

## Active recall
How do you find the last digit of the sum of the first n Fibonacci numbers (F(0) + F(1) + ... + F(n)) for n up to 10^14?

## Core idea
Mathematical identity: sum_{i=0}^n F(i) = F(n + 2) - 1. Therefore, (sum_{i=0}^n F(i)) % 10 = (F(n + 2) - 1) % 10. The Pisano period of Fibonacci numbers modulo 10 is 60. Thus compute index = (n + 2) % 60, find F(index) % 10, and compute (F(index) - 1 + 10) % 10.

## Hints
- **Hint 1**: Use the telescopic identity: F(i) = F(i+2) - F(i+1), which telescopes to sum = F(n+2) - 1.
- **Hint 2**: Combine this with the Pisano period modulo 10 (which is 60).

## Pattern
**Pattern**: Fibonacci Sum Identity (Sum = F(n+2) - 1)
Use when: Math & Number Theory problems require efficient traversal or optimal sub-structure.

## Trick
Adding 10 before modulo: (F((n + 2) % 60) - 1 + 10) % 10 handles negative results when F(n+2) ends in 0.

## Complexity
Time: O(1) (at most 60 Fibonacci iterations). Space: O(1).

## Edge cases
- n = 0: sum is 0.
- n = 1: sum is 1.
- F(n+2) % 10 == 0: subtraction yields -1, correctly adjusted to 9 by + 10.
