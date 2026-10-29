# Last Digit of Fibonacci Number

- **Problem Number**: #078
- **Difficulty**: Easy
- **Topic**: Math & DP
- **Pattern**: Pisano Period Modulo 10 (Cycle of 60)
- **LeetCode Equivalent**: [LC 509: Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)

## Active recall
How do you find the last digit of the n-th Fibonacci number for n up to 10^7 without computing large numbers?

## Core idea
The last digit of F(n) is F(n) % 10. By modular arithmetic, (a + b) % 10 = ((a % 10) + (b % 10)) % 10. Furthermore, the last digits of Fibonacci numbers repeat with a Pisano period of exactly 60! Thus F(n) % 10 = F(n % 60) % 10. We only need to compute up to index n % 60.

## Hints
- **Hint 1**: You only care about the units digit in every addition step.
- **Hint 2**: The sequence of last digits of Fibonacci numbers is periodic with period 60.

## Pattern
**Pattern**: Pisano Period Modulo 10 (Cycle of 60)
Use when: Math & DP problems require efficient traversal or optimal sub-structure.

## Trick
Reducing n modulo 60 first reduces computation to at most 60 additions.

## Complexity
Time: O(1) or O(min(n, 60)) additions. Space: O(1).

## Edge cases
- n = 0: 0.
- n = 1: 1.
- n very large (e.g. 10^7): n % 60 handles it instantly.
