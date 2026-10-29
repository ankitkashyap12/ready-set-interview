# Edit Distance

- **Problem Number**: #085
- **Difficulty**: Medium
- **Topic**: Dynamic Programming
- **Pattern**: 2D Grid Levenshtein Distance DP
- **LeetCode Equivalent**: [LC 72: Edit Distance](https://leetcode.com/problems/edit-distance/)

## Active recall
How do you compute the minimum number of insertions, deletions, and substitutions to transform string A into string B?

## Core idea
Define dp[i][j] = edit distance between prefix A[0..i-1] and B[0..j-1]. Base cases: dp[i][0] = i (i deletions), dp[0][j] = j (j insertions). If A[i-1] == B[j-1], dp[i][j] = dp[i-1][j-1] (match, cost 0). Otherwise, dp[i][j] = 1 + min(dp[i-1][j] (deletion), dp[i][j-1] (insertion), dp[i-1][j-1] (substitution)). Return dp[n][m].

## Hints
- **Hint 1**: If characters match, edit distance is unchanged from the prefixes.
- **Hint 2**: If characters mismatch, take 1 + min of insert, delete, or substitute.

## Pattern
**Pattern**: 2D Grid Levenshtein Distance DP
Use when: Dynamic Programming problems require efficient traversal or optimal sub-structure.

## Trick
Space can be optimized to O(min(n, m)) by keeping only the previous row in memory.

## Complexity
Time: O(N * M) filling N x M table. Space: O(N * M) or O(min(N, M)) with row compression.

## Edge cases
- One or both strings empty: return length of the other string.
- Identical strings: return 0.
- Completely disjoint characters: requires max(n, m) operations.
