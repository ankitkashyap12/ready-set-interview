# Product of Array Except Self

- **Problem Number**: #020
- **Difficulty**: Medium
- **Topic**: Arrays & Hashing
- **Pattern**: Prefix & Suffix Products
- **LeetCode Equivalent**: [LC 238: Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

## Active recall
How do you calculate the product of all elements except nums[i] for each index in O(N) without using the division operator?

## Core idea
The product of all elements except nums[i] is (prefix product of elements before i) * (suffix product of elements after i). Pass 1: compute prefix products into output array res[i] = res[i-1] * nums[i-1]. Pass 2: maintain a running right product suffixProduct from right to left, multiplying res[i] *= suffixProduct, then suffixProduct *= nums[i].

## Hints
- **Hint 1**: Can you break the product for index i into two parts: elements to its left and elements to its right?
- **Hint 2**: Use the output array to store left products first, then multiply right products on the fly.

## Pattern
**Pattern**: Prefix & Suffix Products
Use when: Arrays & Hashing problems require efficient traversal or optimal sub-structure.

## Trick
Using the result array itself to store prefix products achieves O(1) auxiliary space (excluding output array).

## Complexity
Time: O(N) two linear passes. Space: O(1) auxiliary space (output array does not count as extra space).

## Edge cases
- Array with one zero: all elements become 0 except the zero index.
- Array with two or more zeros: all elements become 0.
- Negative numbers.
