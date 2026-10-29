# Longest Common Subsequence of Two Sequences

- **Problem Number**: #090
- **Difficulty**: Medium
- **Topic**: Dynamic Programming
- **Pattern**: 2D Grid LCS DP
- **LeetCode Equivalent**: [LC 1143: Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)

## Active recall
How do you find the length of the longest subsequence common to two sequences of integers?

## Core idea
Define dp[i][j] = LCS length of prefix a[0..i-1] and b[0..j-1]. If a[i-1] == b[j-1]: dp[i][j] = 1 + dp[i-1][j-1]. Otherwise: dp[i][j] = max(dp[i-1][j], dp[i][j-1]). Initialize (n+1) x (m+1) table with 0s. Return dp[n][m].

## Hints
- **Hint 1**: If current characters match, can we extend the LCS of both prefixes?
- **Hint 2**: If they mismatch, the LCS is the maximum of dropping the char from sequence A or from sequence B.

## Pattern
**Pattern**: 2D Grid LCS DP
Use when: Dynamic Programming problems require efficient traversal or optimal sub-structure.

## Trick
dp[i][j] only depends on current row and previous row, allowing space optimization to O(min(N, M)).

## Complexity
Time: O(N * M). Space: O(N * M) or O(min(N, M)).

## Edge cases
- No common elements: returns 0.
- One sequence is a subsequence of the other: returns min(n, m).
- Identical sequences.
