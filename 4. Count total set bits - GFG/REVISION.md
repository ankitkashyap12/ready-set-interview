# Count Total Set Bits from 1 to N

- **Problem Number**: #059
- **Difficulty**: Medium
- **Topic**: Bit Manipulation
- **Pattern**: Bit Position Periodicity (2^i cycles)
- **LeetCode Equivalent**: [LC 338: Counting Bits](https://leetcode.com/problems/counting-bits/)

## Active recall
How do you count the total number of set bits across all numbers from 1 to N in O(log N) time?

## Core idea
For each bit position i (from 0 up to 2^i <= N): the bit toggles every 2^i numbers with a cycle length of 2^(i+1). In each complete cycle, there are 2^i set bits. Total complete cycles = (N + 1) // 2^(i+1). Remaining numbers = (N + 1) % 2^(i+1). Add fullCycles * 2^i + max(0, remainder - 2^i) to the total.

## Hints
- **Hint 1**: Look at each bit position independently. Does bit i follow a regular periodic cycle of 0s and 1s?
- **Hint 2**: Bit i has a period of 2^(i+1), with 2^i consecutive 1s in every period.

## Pattern
**Pattern**: Bit Position Periodicity (2^i cycles)
Use when: Bit Manipulation problems require efficient traversal or optimal sub-structure.

## Trick
Formula for bit i: ((N + 1) // 2^(i+1)) * 2^i + max(0, (N + 1) % 2^(i+1) - 2^i). Sum this over all i where 2^i <= N in O(log N).

## Complexity
Time: O(log N) operations (at most 32 iterations). Space: O(1).

## Edge cases
- N = 0 or N = 1.
- Powers of 2 (e.g. N = 2^k - 1: total set bits is k * 2^(k-1)).
