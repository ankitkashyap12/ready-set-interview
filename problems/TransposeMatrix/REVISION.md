# Transpose Matrix

- **Problem Number**: #047
- **Difficulty**: Easy
- **Topic**: Matrix
- **Pattern**: Row-to-Column Swapping [i][j] -> [j][i]
- **LeetCode Equivalent**: [LC 867: Transpose Matrix](https://leetcode.com/problems/transpose-matrix/)

## Active recall
How do you flip a matrix over its main diagonal, switching row and column indices for non-square matrices?

## Core idea
For a matrix of size R x C, its transpose has dimensions C x R. Allocate transposedMatrix of size C x R. Loop col from 0 to C - 1 and row from 0 to R - 1: transposedMatrix[col][row] = matrix[row][col]. Return transposedMatrix.

## Hints
- **Hint 1**: The element at row r and column c moves to row c and column r.
- **Hint 2**: For non-square matrices (R != C), the dimensions flip: a 2x3 matrix becomes a 3x2 matrix.

## Pattern
**Pattern**: Row-to-Column Swapping [i][j] -> [j][i]
Use when: Matrix problems require efficient traversal or optimal sub-structure.

## Trick
Output dimensions must be cols x rows, not rows x cols.

## Complexity
Time: O(R * C) visits every cell once. Space: O(R * C) to store the transposed matrix.

## Edge cases
- 1xN or Nx1 single vector matrix.
- Square matrices (where in-place transpose is possible, but general case requires new matrix).
