# Organizing a Lottery (Points and Segments)

- **Problem Number**: #096
- **Difficulty**: Hard
- **Topic**: Divide & Conquer & Sorting
- **Pattern**: Sweep-line Event Sorting
- **LeetCode Equivalent**: [LC 1851: Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/)

## Active recall
Given N segments and M query points, how do you find how many segments contain each point in O((N + M) log(N + M)) time?

## Core idea
Sweep-line algorithm: create events for segment starts, query points, and segment ends. Represent each as (coordinate, event_type, index). Crucial ordering of event_type at identical coordinates: START < POINT < END (e.g. -1 for START, 0 for POINT, +1 for END). Sort events. Iterate through sorted events: if START, activeSegments++; if END, activeSegments--; if POINT, result[point.index] = activeSegments.

## Hints
- **Hint 1**: Instead of checking each point against all segments (O(N * M)), treat points and segment boundaries as events along the number line.
- **Hint 2**: If a segment starts at the same coordinate as a point, the segment must be counted before processing the point.

## Pattern
**Pattern**: Sweep-line Event Sorting
Use when: Divide & Conquer & Sorting problems require efficient traversal or optimal sub-structure.

## Trick
Tie-breaking at identical coordinates: START (-1) must precede POINT (0), which must precede END (+1) so segments covering the boundary are correctly counted.

## Complexity
Time: O((N + M) log(N + M)) sorting events. Space: O(N + M) event storage.

## Edge cases
- Point exactly on segment start or end boundary.
- Segments with length 0 ([x, x]).
- Points outside all segments: return 0.
