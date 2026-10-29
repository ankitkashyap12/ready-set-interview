# Digits in Factorial

- **Problem Number**: #062
- **Difficulty**: Easy
- **Topic**: Math & Number Theory
- **Pattern**: Logarithmic Summation (Kamenetsky's Formula)
- **LeetCode Equivalent**: [Number of Digits in Factorial](https://leetcode.com/problems/calculate-money-in-leetcode-bank/)

## Active recall
How do you find the number of digits in n! for large n without actually computing the massive factorial?

## Core idea
The number of digits in an integer X in base 10 is floor(log10(X)) + 1. Since n! = 1 * 2 * ... * n, log10(n!) = sum(log10(i)) for i = 1 to n. Compute sum of log10(i) and return floor(sum) + 1.

## Hints
- **Hint 1**: Number of digits in X is floor(log10(X)) + 1.
- **Hint 2**: Use the log product identity: log(a * b) = log(a) + log(b).

## Pattern
**Pattern**: Logarithmic Summation (Kamenetsky's Formula)
Use when: Math & Number Theory problems require efficient traversal or optimal sub-structure.

## Trick
Summing log10(i) for i from 1 to n avoids computing gigantic factorials while giving exact digit counts.

## Complexity
Time: O(N) simple floating-point loop. Space: O(1).

## Edge cases
- n <= 1: 0! and 1! both equal 1, which has 1 digit.
- Floating point precision: use double.
