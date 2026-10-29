# LCS of Three Sequences

- **Problem Number**: #095
- **Difficulty**: Medium
- **Topic**: Dynamic Programming
- **Pattern**: 3D Grid Dynamic Programming
- **LeetCode Equivalent**: [LC 1143: Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)

## Active recall
How do you find the longest common subsequence of three sequences of lengths up to 100?

## Core idea
Extend 2D LCS to a 3D DP table dp[i][j][k] representing the LCS of prefixes a[0..i-1], b[0..j-1], and c[0..k-1]. If a[i-1] == b[j-1] == c[k-1]: dp[i][j][k] = 1 + dp[i-1][j-1][k-1]. Otherwise: dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1]). Return dp[n1][n2][n3].

## Hints
- **Hint 1**: Can you generalize the 2D recurrence relation to three dimensions?
- **Hint 2**: If all three characters match, increment the 3D diagonal by 1; otherwise take max along the 3 axes.

## Pattern
**Pattern**: 3D Grid Dynamic Programming
Use when: Dynamic Programming problems require efficient traversal or optimal sub-structure.

## Trick
Notice that computing LCS(A, B) and then LCS with C does NOT work! All three sequences must be matched simultaneously in the 3D DP.

## Complexity
Time: O(N1 * N2 * N3) states. Space: O(N1 * N2 * N3) or O(N2 * N3) with 2D layer compression.

## Edge cases
- No elements common to all three: returns 0.
- Sequences of different lengths.
- Identical sequences.
