# Merge Intervals

- **Problem Number**: #008
- **Difficulty**: Medium
- **Topic**: Intervals
- **Pattern**: Sort by Start Time + Greedy Merge
- **LeetCode Equivalent**: [LC 56: Merge Intervals](https://leetcode.com/problems/merge-intervals/)

## Active recall
Given a collection of intervals, how do you merge all overlapping intervals into non-overlapping ones?

## Core idea
Sort intervals by start time intervals.sort(key=lambda x: x[0]). Initialize merged list with the first interval. For each subsequent interval, if current.start <= merged.last.end, merge by updating merged.last.end = max(merged.last.end, current.end). Otherwise, append current as a new interval.

## Hints
- **Hint 1**: If intervals are sorted by start time, when does interval B overlap with interval A?
- **Hint 2**: Keep updating the end of the current merged interval using max(endA, endB).

## Pattern
**Pattern**: Sort by Start Time + Greedy Merge
Use when: Intervals problems require efficient traversal or optimal sub-structure.

## Trick
Always use max(merged.last.end, current.end) because an interval may be completely subsumed inside the previous one (e.g. [1, 5] and [2, 3]).

## Complexity
Time: O(N log N) dominated by sorting. Space: O(N) to store merged intervals or O(log N) sorting space.

## Edge cases
- Single interval: [[1, 4]] -> [[1, 4]].
- Interval completely inside another: [[1, 6], [2, 4]] -> [[1, 6]].
- Touching boundaries: [[1, 4], [4, 5]] -> [[1, 5]].
