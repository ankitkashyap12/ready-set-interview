# Bit Difference

- **Problem Number**: #061
- **Difficulty**: Easy
- **Topic**: Bit Manipulation
- **Pattern**: Brian Kernighan's Algorithm on (a ^ b)
- **LeetCode Equivalent**: [LC 461: Hamming Distance](https://leetcode.com/problems/hamming-distance/)

## Active recall
How do you count the number of bits that need to be flipped to convert integer a to integer b?

## Core idea
XOR a and b to get diff = a ^ b. Every set bit in diff corresponds to a bit position that must be flipped. Count set bits in diff using Brian Kernighan's algorithm: while diff > 0: diff &= (diff - 1), count++.

## Hints
- **Hint 1**: XOR returns 1 wherever bits differ.
- **Hint 2**: Counting the number of flips equals counting set bits in a ^ b (the Hamming distance).

## Pattern
**Pattern**: Brian Kernighan's Algorithm on (a ^ b)
Use when: Bit Manipulation problems require efficient traversal or optimal sub-structure.

## Trick
Brian Kernighan's trick diff &= (diff - 1) clears the lowest set bit in each iteration, running in O(number of set bits) rather than 32 steps.

## Complexity
Time: O(K) where K is the number of flipped bits (at most 32). Space: O(1).

## Edge cases
- a == b: 0 bits to flip.
- a and b have no bits in common: all bits flip.
