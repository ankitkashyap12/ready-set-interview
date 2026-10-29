# Array Insert at Index

- **Problem Number**: #055
- **Difficulty**: Easy
- **Topic**: Arrays & Hashing
- **Pattern**: Right Shift Array Elements
- **LeetCode Equivalent**: [LC 27: Remove Element](https://leetcode.com/problems/remove-element/)

## Active recall
How do you insert an element at a specified index in an array by shifting subsequent elements?

## Core idea
Shift all elements from index to sizeOfArray - 2 one position to the right, starting from the back (i = sizeOfArray - 1 down to index + 1: arr[i] = arr[i - 1]). Then assign arr[index] = element.

## Hints
- **Hint 1**: If you shift from left to right, you overwrite values before moving them! Shift from right to left.
- **Hint 2**: Insert the element at arr[index] after the shift completes.

## Pattern
**Pattern**: Right Shift Array Elements
Use when: Arrays & Hashing problems require efficient traversal or optimal sub-structure.

## Trick
Always iterate backwards (from size - 1 down to index + 1) when shifting elements to the right to avoid overwriting unshifted data.

## Complexity
Time: O(N) where N is the number of elements shifted. Space: O(1) in-place.

## Edge cases
- Inserting at index 0 (maximum shift).
- Inserting at the very end index (0 shifts).
