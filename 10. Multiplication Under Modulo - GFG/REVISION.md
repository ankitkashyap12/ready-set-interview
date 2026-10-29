# Multiplication Under Modulo

- **Problem Number**: #071
- **Difficulty**: Easy
- **Topic**: Math & Number Theory
- **Pattern**: Modular Arithmetic Multiplication Identity
- **LeetCode Equivalent**: [Modular Multiplication](https://leetcode.com/problems/powx-n/)

## Active recall
How do you calculate (a * b) % M safely without integer overflow?

## Core idea
Modular multiplication rule: (a * b) % M = ((a % M) * (b % M)) % M. Cast operands to 64-bit integers (long / unsigned long long) before multiplying to avoid 32-bit overflow before modulo.

## Hints
- **Hint 1**: Take modulo of each operand first.
- **Hint 2**: Cast operands to 64-bit long before the multiplication.

## Pattern
**Pattern**: Modular Arithmetic Multiplication Identity
Use when: Math & Number Theory problems require efficient traversal or optimal sub-structure.

## Trick
Even after modulo M, (a % M) * (b % M) can be up to (M-1)^2. If M = 10^9 + 7, (M-1)^2 ~= 10^18, requiring a 64-bit long in C++/Java.

## Complexity
Time: O(1). Space: O(1).

## Edge cases
- Large a and b near 10^9.
- Operand divisible by M -> result 0.
