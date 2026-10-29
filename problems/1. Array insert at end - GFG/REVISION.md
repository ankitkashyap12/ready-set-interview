# Array Insert at End

- **Problem Number**: #053
- **Difficulty**: Easy
- **Topic**: Arrays & Hashing
- **Pattern**: Direct Index Assignment
- **LeetCode Equivalent**: [LC 27: Remove Element (Array Operations)](https://leetcode.com/problems/remove-element/)

## Active recall
How do you insert an element at the end of a fixed-capacity array at index sizeOfArray - 1?

## Core idea
Directly assign arr[sizeOfArray - 1] = element. Since array indexing is random access, assigning to the final slot takes O(1) time.

## Hints
- **Hint 1**: What is the index of the last element in an array of size N?
- **Hint 2**: Remember that array indexing is 0-based.

## Pattern
**Pattern**: Direct Index Assignment
Use when: Arrays & Hashing problems require efficient traversal or optimal sub-structure.

## Trick
In fixed-size arrays, inserting at the end is an O(1) assignment arr[size - 1] = element without shifting.

## Complexity
Time: O(1). Space: O(1).

## Edge cases
- Array of size 1.
- Negative or zero element values.
