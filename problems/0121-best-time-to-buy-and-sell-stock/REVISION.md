# Best Time to Buy and Sell Stock

- **Problem Number**: #013
- **Difficulty**: Easy
- **Topic**: Arrays & Hashing
- **Pattern**: Single Pass Running Minimum (Prefix Min)
- **LeetCode Equivalent**: [LC 121: Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

## Active recall
How do you maximize profit from choosing a single day to buy and a later day to sell stock in O(N) time and O(1) space?

## Core idea
Maintain minPrice seen so far (initialized to infinity) and maxProfit (initialized to 0). Iterate through prices: minPrice = min(minPrice, price), and maxProfit = max(maxProfit, price - minPrice). Return maxProfit.

## Hints
- **Hint 1**: If you sell on day i, what price would have given you the best profit?
- **Hint 2**: Track the minimum price seen so far as you iterate through the list.

## Pattern
**Pattern**: Single Pass Running Minimum (Prefix Min)
Use when: Arrays & Hashing problems require efficient traversal or optimal sub-structure.

## Trick
Buying must happen BEFORE selling. Updating minPrice before calculating potential profit ensures correct chronological ordering.

## Complexity
Time: O(N) single loop over prices. Space: O(1) constant extra variables.

## Edge cases
- Strictly decreasing prices: [7, 6, 4, 3, 1] -> 0 profit.
- Single day: [5] -> 0 profit.
- All identical prices: [3, 3, 3] -> 0.
