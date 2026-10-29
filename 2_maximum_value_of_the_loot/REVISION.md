# Maximum Value of the Loot (Fractional Knapsack)

- **Problem Number**: #081
- **Difficulty**: Medium
- **Topic**: Greedy
- **Pattern**: Greedy by Value-to-Weight Ratio
- **LeetCode Equivalent**: [Fractional Knapsack](https://leetcode.com/problems/maximum-units-on-a-truck/)

## Active recall
Given items with values and weights, and a knapsack of capacity W, how do you maximize total value if fractions of items can be taken?

## Core idea
Calculate unit value density for each item: density = value / weight. Sort items in descending order of unit density. Greedily take as much of the highest-density item as possible: take = min(item.weight, remainingCapacity). Add take * density to total value, and decrement remainingCapacity -= take. Stop when knapsack is full.

## Hints
- **Hint 1**: Since items can be divided continuously, which item gives the most bang for your buck per unit weight?
- **Hint 2**: Sort items by value / weight descending.

## Pattern
**Pattern**: Greedy by Value-to-Weight Ratio
Use when: Greedy problems require efficient traversal or optimal sub-structure.

## Trick
Fractional knapsack admits an optimal greedy solution because we can always fill any remaining fraction with the next densest item.

## Complexity
Time: O(N log N) dominated by sorting items. Space: O(1) auxiliary space.

## Edge cases
- Total weight of all items <= W: take everything.
- Items with zero weight (if permitted) or capacity W = 0.
- Use double precision for floating-point values.
