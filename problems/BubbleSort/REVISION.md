# Bubble Sort

- **Problem Number**: #030
- **Difficulty**: Easy
- **Topic**: Sorting
- **Pattern**: Adjacent Element Swapping with Early Termination
- **LeetCode Equivalent**: [LC 912: Sort an Array](https://leetcode.com/problems/sort-an-array/)

## Active recall
How does Bubble Sort work, and how can it achieve O(N) best-case time on already sorted inputs?

## Core idea
Repeatedly step through the array, compare adjacent elements, and swap them if they are in the wrong order. After the k-th pass, the k-th largest element has 'bubbled up' to its correct final position at the end. Use a boolean isSorted flag: if an entire pass completes without a single swap, terminate early.

## Hints
- **Hint 1**: Each pass bubbles the next largest unsorted element to the end of the array.
- **Hint 2**: Can you detect if the array is already sorted to stop immediately?

## Pattern
**Pattern**: Adjacent Element Swapping with Early Termination
Use when: Sorting problems require efficient traversal or optimal sub-structure.

## Trick
Reduce the inner loop limit by 1 on each pass (counter = 0..n-1) and break if isSorted remains true.

## Complexity
Time: O(N^2) average and worst case, O(N) best case with swapped flag. Space: O(1) in-place.

## Edge cases
- Already sorted array: finishes in 1 pass O(N).
- Reverse sorted array: triggers maximum swaps N*(N-1)/2.
- Single element array.
