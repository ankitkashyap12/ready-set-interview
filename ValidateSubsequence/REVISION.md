# Validate Subsequence

- **Problem Number**: #050
- **Difficulty**: Easy
- **Topic**: Two Pointers
- **Pattern**: Greedy Sequence Pointer Matching
- **LeetCode Equivalent**: [LC 392: Is Subsequence](https://leetcode.com/problems/is-subsequence/)

## Active recall
How do you determine if a sequence is a valid subsequence of an array (appears in the same relative order)?

## Core idea
Initialize seqIdx = 0. Iterate through array with arrIdx = 0. Whenever array[arrIdx] == sequence[seqIdx], increment seqIdx. If seqIdx == sequence.length at any point, all subsequence elements were found in order; return true. If loop finishes and seqIdx < sequence.length, return false.

## Hints
- **Hint 1**: A subsequence preserves relative order but does not need to be contiguous.
- **Hint 2**: Move a pointer through sequence only when a match is found in array.

## Pattern
**Pattern**: Greedy Sequence Pointer Matching
Use when: Two Pointers problems require efficient traversal or optimal sub-structure.

## Trick
Early return: if seqIdx == sequence.length, return true immediately without scanning the rest of the array.

## Complexity
Time: O(N) where N is array length. Space: O(1) auxiliary space.

## Edge cases
- Sequence longer than array: immediately false.
- Identical array and sequence: true.
- Empty sequence: always true.
