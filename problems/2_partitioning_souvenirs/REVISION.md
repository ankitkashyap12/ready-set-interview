# Partitioning Souvenirs (3-Way Equal Partition)

- **Problem Number**: #082
- **Difficulty**: Medium
- **Topic**: Dynamic Programming
- **Pattern**: Subset Sum DP / Backtracking with Pruning
- **LeetCode Equivalent**: [LC 698: Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/)

## Active recall
How do you determine if a set of integers can be partitioned into 3 subsets with equal sums?

## Core idea
Total sum S must be divisible by 3 (target = S / 3). If S % 3 != 0, return 0. Use 2D/3D subset sum DP or backtracking with memoization. In DP: dp[i][s1][s2] = boolean whether prefix i can form subset 1 with sum s1 and subset 2 with sum s2 (subset 3 gets the remainder). If dp[N][target][target] is true, return 1.

## Hints
- **Hint 1**: First check: is the total sum divisible by 3?
- **Hint 2**: If total sum is S, each of the three subsets must sum to exactly S / 3.

## Pattern
**Pattern**: Subset Sum DP / Backtracking with Pruning
Use when: Dynamic Programming problems require efficient traversal or optimal sub-structure.

## Trick
Sort items descending before backtracking or DP to prune large impossible branches immediately.

## Complexity
Time: O(N * (S/3)^2) with DP, or O(3^N) pruned backtracking. Space: O((S/3)^2) DP table.

## Edge cases
- Total sum not divisible by 3: immediately return 0.
- Any single item > target: immediately return 0.
- Fewer than 3 items: return 0.
