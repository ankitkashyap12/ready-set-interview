# Primality Test

- **Problem Number**: #067
- **Difficulty**: Easy
- **Topic**: Math & Number Theory
- **Pattern**: 6k ± 1 Trial Division up to sqrt(N)
- **LeetCode Equivalent**: [Prime Number Test](https://leetcode.com/problems/count-primes/)

## Active recall
How do you test if an integer N is prime in O(sqrt(N)) time using the 6k ± 1 optimization?

## Core idea
If N <= 1, return false. If N <= 3, return true. If N % 2 == 0 or N % 3 == 0, return false. All primes greater than 3 are of the form 6k ± 1. Loop i from 5 to sqrt(N) stepping by 6: if N % i == 0 or N % (i + 2) == 0, return false. If loop finishes, return true.

## Hints
- **Hint 1**: Divisors always appear in pairs (d, N / d); checking up to sqrt(N) is sufficient.
- **Hint 2**: After ruling out multiples of 2 and 3, all remaining prime candidates are of the form 6k ± 1.

## Pattern
**Pattern**: 6k ± 1 Trial Division up to sqrt(N)
Use when: Math & Number Theory problems require efficient traversal or optimal sub-structure.

## Trick
Stepping by 6 checks both i (6k - 1) and i + 2 (6k + 1) in each iteration, skipping 2/3 of all numbers.

## Complexity
Time: O(sqrt(N)). Space: O(1).

## Edge cases
- N <= 1: not prime.
- N = 2, 3: prime.
- Perfect squares of primes (e.g. 25, 49): caught at i = sqrt(N).
