# Maximum Number of Prizes (Distinct Summands)

- **Problem Number**: #099
- **Difficulty**: Easy
- **Topic**: Greedy
- **Pattern**: Triangular Progression Greedy Choice
- **LeetCode Equivalent**: [Distinct Summands](https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/)

## Active recall
How do you represent integer n as the sum of the maximum possible number of distinct positive integers?

## Core idea
To maximize count, pick the smallest available integers greedily: 1, 2, 3, ... In each step k: if remaining n - k > k, take k, add to prizes, and decrement n -= k. If n - k <= k, taking k would leave a remainder that cannot be strictly greater than k, so take the entire remaining n as the final prize.

## Hints
- **Hint 1**: To maximize the number of distinct prizes, give 1 to first place, 2 to second place, etc.
- **Hint 2**: When the remaining candies cannot support the next distinct number + a strictly larger remainder, give all remaining candies to the current prize.

## Pattern
**Pattern**: Triangular Progression Greedy Choice
Use when: Greedy problems require efficient traversal or optimal sub-structure.

## Trick
Condition n - k > k guarantees that whatever remains will be strictly greater than k, keeping all summands distinct.

## Complexity
Time: O(sqrt(N)) since 1 + 2 + ... + k ~= k^2 / 2 = n. Space: O(sqrt(N)) to store prizes.

## Edge cases
- n = 1: [1].
- n = 2: [2].
- n = 6: [1, 2, 3].
