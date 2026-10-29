# Move Element To End

- **Problem Number**: #039
- **Difficulty**: Easy
- **Topic**: Two Pointers
- **Pattern**: Converging Two Pointers (In-place Swap)
- **LeetCode Equivalent**: [LC 27: Remove Element](https://leetcode.com/problems/remove-element/)

## Active recall
How do you move all instances of a target integer to the end of an array in-place without preserving relative order?

## Core idea
Use two pointers: left = 0, right = len - 1. While left < right: decrement right while array[right] == toMove and left < right. If array[left] == toMove, swap(array[left], array[right]). Increment left. Repeat until pointers cross.

## Hints
- **Hint 1**: Does the problem require maintaining the relative order of other elements? No!
- **Hint 2**: Point left at candidates to move away and right at non-target elements to swap with.

## Pattern
**Pattern**: Converging Two Pointers (In-place Swap)
Use when: Two Pointers problems require efficient traversal or optimal sub-structure.

## Trick
Always check left < right inside the inner while loop when moving the right pointer backwards.

## Complexity
Time: O(N) linear time, each element examined once. Space: O(1) in-place swaps.

## Edge cases
- All elements equal to target toMove: no swaps performed.
- Target toMove not present in array: no swaps performed.
- Array with all targets already at the end.
