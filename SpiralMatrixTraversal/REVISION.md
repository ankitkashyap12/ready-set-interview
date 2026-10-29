# Spiral Matrix Traversal

- **Problem Number**: #044
- **Difficulty**: Medium
- **Topic**: Matrix
- **Pattern**: 4-Boundary Shrinking Loop
- **LeetCode Equivalent**: [LC 54: Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)

## Active recall
How do you traverse an N x M 2D matrix in spiral order (clockwise from top-left) in O(N*M) time without visiting any cell twice?

## Core idea
Define four boundaries: startRow = 0, endRow = n - 1, startCol = 0, endCol = m - 1. While startRow <= endRow and startCol <= endCol: 1. Traverse top row from startCol to endCol; 2. Traverse right col from startRow + 1 to endRow; 3. If startRow < endRow, traverse bottom row from endCol - 1 down to startCol; 4. If startCol < endCol, traverse left col from endRow - 1 down to startRow + 1. Shrink boundaries: startRow++, endRow--, startCol++, endCol--.

## Hints
- **Hint 1**: Track 4 moving boundaries: top, bottom, left, right.
- **Hint 2**: Ensure you do not double-traverse single-row or single-column matrices by checking startRow < endRow and startCol < endCol before the return loops.

## Pattern
**Pattern**: 4-Boundary Shrinking Loop
Use when: Matrix problems require efficient traversal or optimal sub-structure.

## Trick
Boundary checks (startRow < endRow and startCol < endCol) before moving left and moving up prevent duplicate traversals in non-square matrices.

## Complexity
Time: O(N * M) visits every cell exactly once. Space: O(1) auxiliary space (excluding result list).

## Edge cases
- Single row matrix: [[1, 2, 3, 4]].
- Single column matrix: [[1], [2], [3]].
- 1x1 matrix: [[1]].
