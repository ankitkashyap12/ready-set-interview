# Move Zeroes

- **Problem Number**: #021
- **Difficulty**: Easy
- **Topic**: Two Pointers
- **Pattern**: Slow & Fast Two Pointers (In-place Write)
- **LeetCode Equivalent**: [LC 283: Move Zeroes](https://leetcode.com/problems/move-zeroes/)

## Active recall
How do you move all zeros to the end of an array in-place while maintaining the relative order of non-zero elements?

## Core idea
Maintain slow pointer insertPos = 0. Iterate fast pointer through array. Whenever nums[fast] != 0, swap nums[insertPos] with nums[fast] (or assign nums[insertPos] = nums[fast]) and increment insertPos. If using assignment, fill remaining indices from insertPos to n - 1 with 0.

## Hints
- **Hint 1**: Can you shift all non-zero elements forward to an insertion pointer?
- **Hint 2**: Swapping nums[insertPos] with nums[fast] handles both compaction and trailing zeros in one pass.

## Pattern
**Pattern**: Slow & Fast Two Pointers (In-place Write)
Use when: Two Pointers problems require efficient traversal or optimal sub-structure.

## Trick
Swapping nums[insertPos] with nums[fast] whenever nums[fast] != 0 automatically moves zeros forward without a second loop.

## Complexity
Time: O(N) single pass. Space: O(1) in-place.

## Edge cases
- No zeros: [1, 2, 3] -> [1, 2, 3].
- All zeros: [0, 0, 0] -> [0, 0, 0].
- Zeros already at end: [1, 2, 0, 0].
