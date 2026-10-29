# Fibonacci Number

- **Problem Number**: #074
- **Difficulty**: Easy
- **Topic**: Dynamic Programming
- **Pattern**: Bottom-Up Iterative DP (Two Variables)
- **LeetCode Equivalent**: [LC 509: Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)

## Active recall
How do you calculate F(n) in O(N) time and O(1) space, avoiding exponential recursion?

## Core idea
F(0) = 0, F(1) = 1. Iteratively compute F(i) = F(i-1) + F(i-2) using two variables: prev2 = 0, prev1 = 1. In each step: curr = prev1 + prev2, prev2 = prev1, prev1 = curr. Return prev1.

## Hints
- **Hint 1**: Naive recursion computes the same sub-problems repeatedly, taking O(2^N) time.
- **Hint 2**: You only need the previous two Fibonacci values to compute the next.

## Pattern
**Pattern**: Bottom-Up Iterative DP (Two Variables)
Use when: Dynamic Programming problems require efficient traversal or optimal sub-structure.

## Trick
Storing only the last two values reduces space from O(N) to O(1).

## Complexity
Time: O(N) additions. Space: O(1) constant variables.

## Edge cases
- n = 0: returns 0.
- n = 1: returns 1.
