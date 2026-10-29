# Least Common Multiple

- **Problem Number**: #089
- **Difficulty**: Easy
- **Topic**: Math & Number Theory
- **Pattern**: GCD-to-LCM Relation (a * b) // gcd(a, b)
- **LeetCode Equivalent**: [Least Common Multiple](https://leetcode.com/problems/find-greatest-common-divisor-of-array/)

## Active recall
How do you compute the LCM of two large integers up to 10^7 without factoring?

## Core idea
Fundamental identity: a * b = gcd(a, b) * lcm(a, b). Therefore, lcm(a, b) = (a * b) // gcd(a, b). Compute gcd(a, b) first via Euclid's algorithm in O(log(min(a, b))). To avoid intermediate overflow, divide first: (a // gcd(a, b)) * b.

## Hints
- **Hint 1**: Identity: lcm(a, b) * gcd(a, b) = a * b.
- **Hint 2**: Compute (a // gcd(a, b)) * b to avoid overflow from a * b.

## Pattern
**Pattern**: GCD-to-LCM Relation (a * b) // gcd(a, b)
Use when: Math & Number Theory problems require efficient traversal or optimal sub-structure.

## Trick
Divide before multiplying: (a // gcd(a, b)) * b prevents integer overflow when a * b exceeds 64-bit integer limits.

## Complexity
Time: O(log(min(a, b))) for Euclidean gcd. Space: O(1).

## Edge cases
- a or b is 1: lcm is the other number.
- a == b: lcm is a.
- Coprime numbers: lcm is a * b.
