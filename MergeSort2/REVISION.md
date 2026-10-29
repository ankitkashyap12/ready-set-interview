# Merge Sort (Optimized Auxiliary Array)

- **Problem Number**: #037
- **Difficulty**: Medium
- **Topic**: Sorting
- **Pattern**: Divide & Conquer with In-place Buffer Swapping
- **LeetCode Equivalent**: [LC 912: Sort an Array](https://leetcode.com/problems/sort-an-array/)

## Active recall
How can Merge Sort be optimized to avoid creating new sub-arrays at every recursive call?

## Core idea
Allocate a single auxiliary array of size N upfront. Alternating roles between main array and auxiliary array across recursive levels avoids reallocating memory. Merge elements from auxiliary array back into main array in-place.

## Hints
- **Hint 1**: Can you allocate only one auxiliary buffer upfront and alternate roles between source and destination?
- **Hint 2**: Pass startIdx and endIdx indices instead of slicing sub-arrays.

## Pattern
**Pattern**: Divide & Conquer with In-place Buffer Swapping
Use when: Sorting problems require efficient traversal or optimal sub-structure.

## Trick
Passing auxiliary array and swapping source/destination arrays at alternating recursion depths reduces memory allocations from O(N log N) to O(N).

## Complexity
Time: O(N log N). Space: O(N) auxiliary space allocated exactly once.

## Edge cases
- Odd length arrays.
- Large arrays where slicing memory overhead causes performance degradation.
