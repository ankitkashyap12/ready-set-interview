# Maximum Pairwise Product

- **Problem Number**: #080
- **Difficulty**: Easy
- **Topic**: Greedy
- **Pattern**: Single Pass Top-2 Largest Elements
- **LeetCode Equivalent**: [LC 1464: Maximum Product of Two Elements in an Array](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/)

## Active recall
How do you find the maximum product of two distinct elements in an array in O(N) time without sorting?

## Core idea
The maximum product of two positive numbers is the product of the two largest numbers. Find max1 and max2 in a single linear pass: maintain max1 = -1, max2 = -1. For each x: if x > max1: max2 = max1, max1 = x; else if x > max2: max2 = x. The maximum pairwise product is (long) max1 * max2.

## Hints
- **Hint 1**: Sorting takes O(N log N); can you find the two largest numbers in one pass?
- **Hint 2**: Watch out for 32-bit integer overflow when multiplying two numbers up to 10^5.

## Pattern
**Pattern**: Single Pass Top-2 Largest Elements
Use when: Greedy problems require efficient traversal or optimal sub-structure.

## Trick
Cast operands to 64-bit integer (long / uint64) before multiplying to avoid 32-bit overflow.

## Complexity
Time: O(N) single pass. Space: O(1) auxiliary space.

## Edge cases
- Two largest elements are equal: [5, 5, 2] -> max1 = 5, max2 = 5.
- Large numbers near 2 * 10^5: product exceeds 2^31 - 1.
