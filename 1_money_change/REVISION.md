# Money Change (Greedy)

- **Problem Number**: #076
- **Difficulty**: Easy
- **Topic**: Greedy
- **Pattern**: Canonical Coin Denominations Greedy Choice
- **LeetCode Equivalent**: [LC 860: Lemonade Change](https://leetcode.com/problems/lemonade-change/)

## Active recall
With coins of denominations 10, 5, and 1, how do you make change for amount m with the minimum number of coins?

## Core idea
For canonical coin systems (like 10, 5, 1), the greedy choice is mathematically guaranteed to be optimal. Take as many 10-coins as possible: count += m // 10, m %= 10. Then take as many 5-coins as possible: count += m // 5, m %= 5. Finally, take remaining amount in 1-coins: count += m.

## Hints
- **Hint 1**: Always pick the largest denomination that does not exceed the remaining amount.
- **Hint 2**: Since denominations are multiples (10 = 2*5, 5 = 5*1), the greedy choice is strictly optimal.

## Pattern
**Pattern**: Canonical Coin Denominations Greedy Choice
Use when: Greedy problems require efficient traversal or optimal sub-structure.

## Trick
Integer division count = m // 10 + (m % 10) // 5 + (m % 5) computes the answer in O(1) math operations without loops.

## Complexity
Time: O(1). Space: O(1).

## Edge cases
- m < 5: all 1-coins.
- m exact multiple of 10: only 10-coins.
