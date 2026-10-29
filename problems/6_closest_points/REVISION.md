# Closest Pair of Points

- **Problem Number**: #097
- **Difficulty**: Hard
- **Topic**: Divide & Conquer
- **Pattern**: Divide and Conquer 2D Plane Split ($O(N \log N)$)
- **LeetCode Equivalent**: [LC 973: K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)

## Active recall
How do you find the minimum Euclidean distance between any two points in a 2D plane in O(N log N) time?

## Core idea
Sort points by x-coordinate. Divide: split by vertical line at median x. Recursively find min distance d = min(d_left, d_right). Conquer: build a 'strip' of points within distance d of the dividing line, sorted by y-coordinate. For each point in the strip, only inspect points within vertical distance d. Geometrically, at most 7 points can lie in this d x 2d bounding box! Update d with any closer pair.

## Hints
- **Hint 1**: Split the plane vertically in half and recurse on left and right.
- **Hint 2**: The magic is in the strip: points in the strip within distance d of the midline only need to be compared with at most 7 subsequent points sorted by y.

## Pattern
**Pattern**: Divide and Conquer 2D Plane Split ($O(N \log N)$)
Use when: Divide & Conquer problems require efficient traversal or optimal sub-structure.

## Trick
Geometric sparsity: inside a d x 2d box, no two points on the same side can be closer than d, mathematically capping comparisons in the strip to 7 per point.

## Complexity
Time: O(N log N) with presorted y-coordinates. Space: O(N) auxiliary space.

## Edge cases
- 2 points: base case.
- Points with identical x or y coordinates.
- Points situated directly on the dividing line.
