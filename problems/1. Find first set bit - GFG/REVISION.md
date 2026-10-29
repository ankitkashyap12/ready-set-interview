# Find First Set Bit

- **Problem Number**: #054
- **Difficulty**: Easy
- **Topic**: Bit Manipulation
- **Pattern**: Two's Complement LSB Isolation (n & -n)
- **LeetCode Equivalent**: [LC 191: Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)

## Active recall
How do you find the 1-based position of the first set bit (from right to left) in an integer?

## Core idea
Isolate the lowest set bit using n & -n. The 1-based position corresponds to log2(n & -n) + 1. Alternatively, iteratively check (n & 1); if 1 return count, else right-shift n >>= 1 and increment count.

## Hints
- **Hint 1**: What does n & -n do in two's complement arithmetic?
- **Hint 2**: n & -n leaves ONLY the rightmost set bit active. Its position is log2(isolatedBit) + 1.

## Pattern
**Pattern**: Two's Complement LSB Isolation (n & -n)
Use when: Bit Manipulation problems require efficient traversal or optimal sub-structure.

## Trick
Two's complement -n is (~n + 1). Therefore n & -n isolates the lowest set bit in O(1) time.

## Complexity
Time: O(1) or O(log N) bit shifts. Space: O(1).

## Edge cases
- n == 0: no set bits, return 0.
- n is a power of 2: first set bit is the only set bit.
- n is odd: first set bit is at position 1.
