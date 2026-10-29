# Non-Constructible Change

- **Problem Number**: #040
- **Difficulty**: Easy
- **Topic**: Greedy
- **Pattern**: Sorted Greedy Change Invariant
- **LeetCode Equivalent**: [LC 330: Patching Array](https://leetcode.com/problems/patching-array/)

## Active recall
Given an array of positive coin values, what is the minimum sum of money that you CANNOT make change for?

## Core idea
Sort the coins in ascending order. Maintain currentChangeCreated = 0 (representing the ability to make all change from 1 to currentChangeCreated). For each coin: if coin > currentChangeCreated + 1, you can NEVER form currentChangeCreated + 1; return currentChangeCreated + 1 immediately! Otherwise, add coin to currentChangeCreated. If all coins processed, return currentChangeCreated + 1.

## Hints
- **Hint 1**: If you can create all change values from 1 to C, and your next coin is V: what happens if V > C + 1?
- **Hint 2**: Sort the coins first so you process them in increasing order.

## Pattern
**Pattern**: Sorted Greedy Change Invariant
Use when: Greedy problems require efficient traversal or optimal sub-structure.

## Trick
Invariant: with coins up to index i, you can create all values in [1, C]. If coin <= C + 1, your reachable range expands to [1, C + coin]. If coin > C + 1, C + 1 is permanently unreachable.

## Complexity
Time: O(N log N) dominated by sorting coins. Space: O(1) or O(log N) sorting space.

## Edge cases
- Empty coins array: return 1.
- First coin > 1: [2] -> return 1.
- Consecutive powers of 2: [1, 2, 4, 8] -> returns 16.
