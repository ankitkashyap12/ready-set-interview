# Improving QuickSort (3-Way Partitioning)

- **Problem Number**: #087
- **Difficulty**: Medium
- **Topic**: Sorting
- **Pattern**: Dutch National Flag 3-Way Partitioning
- **LeetCode Equivalent**: [LC 75: Sort Colors](https://leetcode.com/problems/sort-colors/)

## Active recall
Why does standard QuickSort degrade to O(N^2) on arrays with many duplicate elements, and how does 3-way partitioning fix it?

## Core idea
Standard 2-way QuickSort puts equal elements on one side, leading to unbalanced N-1 vs 0 splits on arrays of identical elements. 3-way partitioning partitions the array into three segments: elements < pivot, elements == pivot, and elements > pivot. Recurse ONLY on the < pivot and > pivot sub-arrays, completely ignoring the == pivot middle segment.

## Hints
- **Hint 1**: When many duplicate elements exist, grouping all equal elements together into a middle segment eliminates them from further recursion.
- **Hint 2**: Use Dutch National Flag algorithm with three pointers: m1 (boundary for <), i (current), m2 (boundary for >).

## Pattern
**Pattern**: Dutch National Flag 3-Way Partitioning
Use when: Sorting problems require efficient traversal or optimal sub-structure.

## Trick
Sub-arrays containing only elements equal to pivot are completely skipped in subsequent recursive calls, running in O(N) on all-equal arrays.

## Complexity
Time: O(N log N) average, O(N) when only few distinct keys exist. Space: O(log N) stack space.

## Edge cases
- All elements identical: runs in O(N) time with 0 further recursive calls.
- Already sorted array.
