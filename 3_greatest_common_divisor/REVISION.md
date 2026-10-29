# Greatest Common Divisor

- **Problem Number**: #086
- **Difficulty**: Easy
- **Topic**: Math & Number Theory
- **Pattern**: Euclidean Algorithm (gcd(a, b) = gcd(b, a % b))
- **LeetCode Equivalent**: [LC 1979: Find Greatest Common Divisor of Array](https://leetcode.com/problems/find-greatest-common-divisor-of-array/)

## Active recall
How does Euclid's algorithm find the GCD of two integers in logarithmic time?

## Core idea
Euclid's lemma: gcd(a, b) = gcd(b, a % b). Base case: when b == 0, gcd is a. In each step, the remainder a % b is strictly less than a / 2 when a >= b, guaranteeing logarithmic convergence.

## Hints
- **Hint 1**: Division remainder theorem: any common divisor of a and b also divides a % b.
- **Hint 2**: Repeat a, b = b, a % b until b == 0.

## Pattern
**Pattern**: Euclidean Algorithm (gcd(a, b) = gcd(b, a % b))
Use when: Math & Number Theory problems require efficient traversal or optimal sub-structure.

## Trick
In each two iterations, the larger number is at least halved: (a % b) < a / 2, guaranteeing at most 2 * log2(b) steps.

## Complexity
Time: O(log(min(a, b))) Euclidean divisions. Space: O(1) iterative.

## Edge cases
- b = 0: gcd is a.
- a = b: gcd is a.
- Prime numbers: gcd is 1.
