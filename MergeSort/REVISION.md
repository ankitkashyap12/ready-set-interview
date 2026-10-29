# Merge Sort

- **Problem Number**: #036
- **Difficulty**: Medium
- **Topic**: Sorting
- **Pattern**: Divide and Conquer (Merge Step)
- **LeetCode Equivalent**: [LC 912: Sort an Array](https://leetcode.com/problems/sort-an-array/)

## Active recall
How does Merge Sort guarantee stable O(N log N) worst-case time sorting?

## Core idea
Divide: find midpoint mid = len // 2 and recursively sort left half and right half. Conquer: merge the two sorted halves into a combined sorted array by comparing elements using two pointers i and j, copying the smaller element to output.

## Hints
- **Hint 1**: Break the list into two halves until length <= 1, then merge two sorted halves.
- **Hint 2**: Merging two sorted lists of total size N takes linear O(N) time.

## Pattern
**Pattern**: Divide and Conquer (Merge Step)
Use when: Sorting problems require efficient traversal or optimal sub-structure.

## Trick
Use <= when comparing left[i] <= right[j] to ensure stability (preserving original relative order of equal elements).

## Complexity
Time: O(N log N) in all cases (best, average, worst). Space: O(N) auxiliary space for merging.

## Edge cases
- Empty or 1 element: base case.
- Already sorted: still executes O(N log N) divisions and merges.
- All identical values.
