# Majority Element (Divide & Conquer)

- **Problem Number**: #079
- **Difficulty**: Medium
- **Topic**: Divide & Conquer
- **Pattern**: Divide and Conquer / Boyer-Moore Voting
- **LeetCode Equivalent**: [LC 169: Majority Element](https://leetcode.com/problems/majority-element/)

## Active recall
How do you check if a sequence contains an element appearing strictly more than n/2 times using Divide and Conquer?

## Core idea
Divide: split array into left and right halves. If a majority element exists in the whole array, it must be the majority element of at least one of the two halves. Recursively find majority candidate of left half and right half. If they agree, that candidate wins. If they disagree, count occurrences of both candidates across the current range and return whichever has count > (high - low + 1) // 2.

## Hints
- **Hint 1**: If an element appears more than n/2 times in the whole array, it must appear more than half the time in at least one half.
- **Hint 2**: Recurse on left and right, then compare candidate frequencies in O(N).

## Pattern
**Pattern**: Divide and Conquer / Boyer-Moore Voting
Use when: Divide & Conquer problems require efficient traversal or optimal sub-structure.

## Trick
Recurrence T(N) = 2T(N/2) + O(N) yields O(N log N) time via Master Theorem. Boyer-Moore Voting optimizes this to O(N).

## Complexity
Time: O(N log N) for D&C, or O(N) for Boyer-Moore. Space: O(log N) recursion depth.

## Edge cases
- No element has frequency > n/2: return -1.
- All elements distinct.
- Single element array.
