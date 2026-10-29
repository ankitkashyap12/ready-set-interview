# Collecting Signatures (Segment Covering)

- **Problem Number**: #093
- **Difficulty**: Medium
- **Topic**: Greedy
- **Pattern**: Greedy Interval Scheduling by Right Endpoints
- **LeetCode Equivalent**: [LC 452: Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)

## Active recall
Given a set of segments [l_i, r_i], how do you find the minimum number of points such that each segment contains at least one point?

## Core idea
Sort segments by right endpoint r_i ascending. Pick the right endpoint of the first segment as your first point: point = segments[0].r. For each subsequent segment: if segment.l > point, the current segment is not covered; pick a new point = segment.r and add to points list. Otherwise, the segment is already covered by the existing point.

## Hints
- **Hint 1**: Sorting by right endpoints allows you to place a point as far right as possible, maximizing its chance of covering future segments.
- **Hint 2**: Only place a new point when a segment's left endpoint exceeds the current point.

## Pattern
**Pattern**: Greedy Interval Scheduling by Right Endpoints
Use when: Greedy problems require efficient traversal or optimal sub-structure.

## Trick
Always place the point at the segment's right endpoint segment.r. Placing it anywhere earlier would strictly reduce the opportunities to cover subsequent segments.

## Complexity
Time: O(N log N) to sort segments. Space: O(N) to store chosen points.

## Edge cases
- Segments overlapping at a single point: [[1, 3], [3, 5]] covered by point 3.
- One segment inside another: [[1, 5], [2, 3]] sorted by right endpoint puts [2, 3] first, covering both.
