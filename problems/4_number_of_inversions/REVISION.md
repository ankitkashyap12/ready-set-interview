# Number of Inversions

- **Problem Number**: #092
- **Difficulty**: Medium
- **Topic**: Divide & Conquer
- **Pattern**: Merge Sort Inversion Counting
- **LeetCode Equivalent**: [LC 315: Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)

## Active recall
How do you count the number of inversions (pairs i < j with a[i] > a[j]) in O(N log N) time?

## Core idea
Count inversions during Merge Sort. Split array into left and right halves. Recursively count inversions in left half and right half. During the merge step, when an element from right half b[j] is smaller than element from left half a[i], it is smaller than ALL remaining elements in the left half from index i to mid! Add (mid - i) to inversion count. Return leftInversions + rightInversions + splitInversions.

## Hints
- **Hint 1**: When merging two sorted arrays, if right[j] < left[i], how many elements in left are strictly greater than right[j]?
- **Hint 2**: Every element from left[i] to left[mid] forms an inversion with right[j].

## Pattern
**Pattern**: Merge Sort Inversion Counting
Use when: Divide & Conquer problems require efficient traversal or optimal sub-structure.

## Trick
When right[j] < left[i], add (mid - i) directly to the inversion counter in O(1). This counts all split inversions without extra comparisons.

## Complexity
Time: O(N log N) same as Merge Sort. Space: O(N) auxiliary merge array.

## Edge cases
- Already sorted array: 0 inversions.
- Reverse sorted array: maximum N * (N - 1) / 2 inversions.
- Inversion count can exceed 32-bit int: use 64-bit long.
