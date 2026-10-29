# Modular Multiplicative Inverse

- **Problem Number**: #072
- **Difficulty**: Easy
- **Topic**: Math & Number Theory
- **Pattern**: Extended Euclidean Algorithm (Bézout Identity)
- **LeetCode Equivalent**: [Modular Multiplicative Inverse](https://leetcode.com/problems/super-pow/)

## Active recall
Given integers a and m, how do you find an integer x in [1, m - 1] such that (a * x) % m == 1?

## Core idea
A modular inverse exists if and only if gcd(a, m) == 1. Use the Extended Euclidean Algorithm to find coefficients x and y such that a*x + m*y = gcd(a, m) = 1. Taking modulo m: (a * x) % m = 1. The result is (x % m + m) % m. If gcd != 1, return -1.

## Hints
- **Hint 1**: Does a modular inverse exist if gcd(a, m) != 1? No, return -1.
- **Hint 2**: Extended Euclidean algorithm finds integers x and y satisfying a*x + m*y = 1.

## Pattern
**Pattern**: Extended Euclidean Algorithm (Bézout Identity)
Use when: Math & Number Theory problems require efficient traversal or optimal sub-structure.

## Trick
The coefficient x returned by Extended GCD may be negative. Normalize it into [1, m - 1] via (x % m + m) % m.

## Complexity
Time: O(log(min(a, m))) Euclidean steps. Space: O(1).

## Edge cases
- gcd(a, m) > 1: inverse does not exist -> return -1.
- m = 1: no valid inverse in [1, m - 1].
- a = 1: inverse is 1.
