# Smallest Difference

- **Problem Number**: #042
- **Difficulty**: Medium
- **Topic**: Two Pointers
- **Pattern**: Two Sorted Arrays Two Pointers
- **LeetCode Equivalent**: [LC 1200: Minimum Absolute Difference](https://leetcode.com/problems/minimum-absolute-difference/)

## Active recall
Given two non-empty arrays of integers, how do you find the pair of numbers (one from each array) whose absolute difference is closest to zero?

## Core idea
Sort both arrays. Initialize ptrOne = 0, ptrTwo = 0. Compare arrayOne[ptrOne] and arrayTwo[ptrTwo]. Calculate currentDiff = abs(first - second). If currentDiff < smallestDiff, update smallestDiff and bestPair. If first < second, increment ptrOne (to bring it closer to second). If second < first, increment ptrTwo. If first == second, difference is 0 (return immediately!).

## Hints
- **Hint 1**: Sort both arrays so you can walk through them monotonically.
- **Hint 2**: Whichever pointer points to the smaller value should be incremented to decrease the gap.

## Pattern
**Pattern**: Two Sorted Arrays Two Pointers
Use when: Two Pointers problems require efficient traversal or optimal sub-structure.

## Trick
Advance the pointer of the smaller value. Moving the larger pointer would only increase the distance.

## Complexity
Time: O(N log N + M log M) to sort both arrays + O(N + M) two-pointer pass. Space: O(1) auxiliary space.

## Edge cases
- Exact match exists: diff == 0 returns immediately.
- Negative numbers: abs() correctly handles distances between negative values.
- Arrays of different lengths.
