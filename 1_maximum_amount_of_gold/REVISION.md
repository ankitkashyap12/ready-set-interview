# Maximum Amount of Gold (0-1 Knapsack)

- **Problem Number**: #075
- **Difficulty**: Medium
- **Topic**: Dynamic Programming
- **Pattern**: 0-1 Knapsack without Repetitions (1D Backward DP)
- **LeetCode Equivalent**: [LC 416: Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)

## Active recall
Given knapsack capacity W and gold bar weights, how do you pack the maximum weight of gold where each bar can be taken at most once?

## Core idea
Classic 0-1 knapsack where value equals weight. Maintain dp[w] = maximum weight attainable with capacity w. Initialize dp array of size W + 1 with 0. For each gold bar of weight barWeight: iterate w from W down to barWeight: dp[w] = max(dp[w], dp[w - barWeight] + barWeight). Return dp[W].

## Hints
- **Hint 1**: For each bar, decide whether to include it or skip it.
- **Hint 2**: Iterate capacity w backwards from W down to barWeight to ensure each bar is used at most once.

## Pattern
**Pattern**: 0-1 Knapsack without Repetitions (1D Backward DP)
Use when: Dynamic Programming problems require efficient traversal or optimal sub-structure.

## Trick
Iterating backwards across the capacity dimension in a 1D DP array guarantees 0-1 knapsack semantics (no item reuse) in O(W) space.

## Complexity
Time: O(N * W) where N is number of gold bars and W is knapsack capacity. Space: O(W) 1D DP array.

## Edge cases
- Capacity W smaller than all bars: returns 0.
- Sum of all bars <= W: take all bars.
- Single bar fitting capacity.
