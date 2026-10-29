# Money Change Again (Coin Change DP)

- **Problem Number**: #077
- **Difficulty**: Medium
- **Topic**: Dynamic Programming
- **Pattern**: Unbounded Knapsack / Minimum Steps DP
- **LeetCode Equivalent**: [LC 322: Coin Change](https://leetcode.com/problems/coin-change/)

## Active recall
For non-canonical coin denominations (e.g. 1, 3, 4), why does greedy fail, and how does DP find the minimum coin count?

## Core idea
Greedy fails for amount 6 with coins [1, 3, 4]: greedy takes 4 + 1 + 1 = 3 coins, while optimal is 3 + 3 = 2 coins! Use Dynamic Programming: dp[m] = min coins to change amount m. Base case: dp[0] = 0. For m from 1 to money: dp[m] = 1 + min(dp[m - coin]) for each coin <= m. Return dp[money].

## Hints
- **Hint 1**: Why does greedy fail for amount = 6 with coins {1, 3, 4}?
- **Hint 2**: dp[m] depends on the optimal answers for m - 1, m - 3, and m - 4.

## Pattern
**Pattern**: Unbounded Knapsack / Minimum Steps DP
Use when: Dynamic Programming problems require efficient traversal or optimal sub-structure.

## Trick
Initialize dp array with infinity, dp[0] = 0. Sub-problems overlap, making bottom-up DP linear in amount.

## Complexity
Time: O(money * number of coin denominations). Space: O(money) DP array.

## Edge cases
- money = 0: 0 coins.
- money smaller than smallest coin (if 1-coin wasn't present).
