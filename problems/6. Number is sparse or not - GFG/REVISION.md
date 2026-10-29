# Number Is Sparse or Not

- **Problem Number**: #065
- **Difficulty**: Easy
- **Topic**: Bit Manipulation
- **Pattern**: Adjacent Bit Check (n & (n >> 1))
- **LeetCode Equivalent**: [Sparse Number Check](https://leetcode.com/problems/number-of-1-bits/)

## Active recall
A number is sparse if there are no two consecutive set bits in its binary representation. How do you check this in O(1) time?

## Core idea
If a number has two consecutive set bits, shifting it right by 1 position will align one of those set bits with the other. Therefore, (n & (n >> 1)) == 0 if and only if no two consecutive bits are both 1.

## Hints
- **Hint 1**: What happens when you bitwise AND a number with its right-shifted self?
- **Hint 2**: If any two adjacent bits were 1, (n & (n >> 1)) will have a non-zero bit at that position.

## Pattern
**Pattern**: Adjacent Bit Check (n & (n >> 1))
Use when: Bit Manipulation problems require efficient traversal or optimal sub-structure.

## Trick
Single expression (n & (n >> 1)) == 0 checks all adjacent bits in parallel across the entire word in 1 CPU cycle.

## Complexity
Time: O(1). Space: O(1).

## Edge cases
- n = 0: sparse (no set bits).
- Powers of 4 or alternating bits (e.g. 101010b = 42) -> sparse.
- Numbers like 3 (11b), 6 (110b) -> not sparse.
