# Quick Sort

- **Problem Number**: #041
- **Difficulty**: Medium
- **Topic**: Sorting
- **Pattern**: Pivot Partitioning Divide and Conquer
- **LeetCode Equivalent**: [LC 912: Sort an Array](https://leetcode.com/problems/sort-an-array/)

## Active recall
How does Quick Sort partition an array around a pivot, and how do you prevent worst-case O(N^2) stack depth?

## Core idea
Choose pivot (e.g. array[startIdx]). Partition elements such that all elements <= pivot are placed to its left, and all > pivot to its right. Swap pivot into its final position. To optimize stack space, always recurse into the smaller sub-array first and use tail-call iteration for the larger sub-array.

## Hints
- **Hint 1**: Place the pivot into its correct final position, then recursively sort left and right sub-arrays.
- **Hint 2**: Recurse on the smaller partition first to guarantee O(log N) maximum stack depth.

## Pattern
**Pattern**: Pivot Partitioning Divide and Conquer
Use when: Sorting problems require efficient traversal or optimal sub-structure.

## Trick
Always recurse on the smaller sub-array first; this bounds recursion depth to O(log N) even in worst-case partitions.

## Complexity
Time: O(N log N) average, O(N^2) worst case if already sorted without random pivot. Space: O(log N) stack space.

## Edge cases
- All identical values: 3-way partition helps prevent degradation to O(N^2).
- Already sorted array.
