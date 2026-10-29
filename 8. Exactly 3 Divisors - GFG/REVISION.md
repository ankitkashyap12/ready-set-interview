# Exactly 3 Divisors

- **Problem Number**: #069
- **Difficulty**: Easy
- **Topic**: Math & Number Theory
- **Pattern**: Primes Squared via Sieve / Trial Division
- **LeetCode Equivalent**: [Three Divisors](https://leetcode.com/problems/three-divisors/)

## Active recall
Which numbers have EXACTLY 3 positive divisors, and how do you count how many exist up to N?

## Core idea
A number has exactly 3 divisors if and only if it is the square of a prime number p (its divisors are 1, p, and p^2). To count such numbers <= N, count all prime numbers p such that p^2 <= N (i.e. p <= sqrt(N)). Use a Sieve of Eratosthenes up to sqrt(N) and count primes.

## Hints
- **Hint 1**: If a number has divisors 1, d, and n, what must d be? d must be prime and d * d = n!
- **Hint 2**: Count prime numbers up to floor(sqrt(N)).

## Pattern
**Pattern**: Primes Squared via Sieve / Trial Division
Use when: Math & Number Theory problems require efficient traversal or optimal sub-structure.

## Trick
Only squares of prime numbers have exactly 3 divisors. Counting them up to N reduces to counting primes up to sqrt(N).

## Complexity
Time: O(sqrt(N) log log(sqrt(N))) using Sieve. Space: O(sqrt(N)) for sieve array.

## Edge cases
- N < 4: return 0 (smallest is 2^2 = 4).
- N = 4: return 1 (4 has divisors 1, 2, 4).
