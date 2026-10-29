# Array of Products

- **Problem Number**: #028
- **Difficulty**: Medium
- **Topic**: Arrays & Hashing
- **Pattern**: Prefix & Suffix Running Products
- **LeetCode Equivalent**: [LC 238: Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

## Active recall
How do you compute an array of products where output[i] is the product of every other element without division?

## Core idea
Build the product of all elements to the left of i into products[i]. Then traverse backwards, maintaining a running rightProduct and multiplying products[i] *= rightProduct. Each element ends up as (product of left elements) * (product of right elements).

## Hints
- **Hint 1**: Think of the product at index i as two halves: everything to the left of i, and everything to the right of i.
- **Hint 2**: Fill the array with left running products first, then multiply right running products on a second backwards pass.

## Pattern
**Pattern**: Prefix & Suffix Running Products
Use when: Arrays & Hashing problems require efficient traversal or optimal sub-structure.

## Trick
Keep running rightProduct in a single variable during the backwards pass to avoid allocating a second suffix array.

## Complexity
Time: O(N) two linear passes. Space: O(N) for the output array (O(1) auxiliary space).

## Edge cases
- Arrays containing a single zero or multiple zeros.
- Two element array [a, b] -> [b, a].
- Arrays containing negative numbers.
