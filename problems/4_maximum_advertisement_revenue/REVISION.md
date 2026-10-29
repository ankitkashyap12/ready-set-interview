# Maximum Advertisement Revenue

- **Problem Number**: #091
- **Difficulty**: Easy
- **Topic**: Greedy
- **Pattern**: Rearrangement Inequality / Dot Product Sort
- **LeetCode Equivalent**: [LC 646: Maximum Length of Pair Chain](https://leetcode.com/problems/maximum-length-of-pair-chain/)

## Active recall
Given click values a and slot prices b, how do you pair them to maximize the dot product sum(a_i * b_i)?

## Core idea
By the Rearrangement Inequality, the sum of products sum(a_i * b_i) is strictly maximized when both sequences are sorted in the same monotonic order. Sort sequence a in ascending order and sequence b in ascending order. Then sum a[i] * b[i] for all i. Use 64-bit integer to prevent overflow.

## Hints
- **Hint 1**: Pair the largest click value with the largest price, second largest with second largest, etc.
- **Hint 2**: Sort both sequences ascending and compute their dot product.

## Pattern
**Pattern**: Rearrangement Inequality / Dot Product Sort
Use when: Greedy problems require efficient traversal or optimal sub-structure.

## Trick
The Rearrangement Inequality proves that pairing sorted elements greedily produces the global maximum.

## Complexity
Time: O(N log N) for sorting both arrays. Space: O(1) or O(log N) sorting space.

## Edge cases
- Negative values: product of two negative values is positive, which sorting naturally pairs correctly.
- Use 64-bit long for accumulated sum.
