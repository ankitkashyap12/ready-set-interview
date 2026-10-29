# Merge Overlapping Intervals

- **Problem Number**: #035
- **Difficulty**: Medium
- **Topic**: Intervals
- **Pattern**: Sort by Start Time + Greedy Merge
- **LeetCode Equivalent**: [LC 56: Merge Intervals](https://leetcode.com/problems/merge-intervals/)

## Active recall
How do you merge overlapping intervals into an optimal set of disjoint intervals?

## Core idea
Sort intervals by start value. Initialize result with the first interval. For each subsequent interval, if its start <= currentMerged.end, merge by setting currentMerged.end = max(currentMerged.end, nextInterval.end). If its start > currentMerged.end, append nextInterval to result.

## Hints
- **Hint 1**: Sorting by start time ensures any potentially overlapping intervals appear adjacent in the list.
- **Hint 2**: Watch out for an interval that is completely contained within the previous one.

## Pattern
**Pattern**: Sort by Start Time + Greedy Merge
Use when: Intervals problems require efficient traversal or optimal sub-structure.

## Trick
Always use max(currentMerged.end, nextInterval.end) so a shorter contained interval does not shrink the end.

## Complexity
Time: O(N log N) for sorting. Space: O(N) for output array.

## Edge cases
- Intervals already non-overlapping.
- One giant interval subsuming all others: [[1, 10], [2, 3], [4, 5]].
- Intervals touching at endpoints: [[1, 2], [2, 3]] -> [[1, 3]].
