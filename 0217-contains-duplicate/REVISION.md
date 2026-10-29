# Contains Duplicate

- **Problem Number**: #018
- **Difficulty**: Easy
- **Topic**: Arrays & Hashing
- **Pattern**: Hash Set Early Exit
- **LeetCode Equivalent**: [LC 217: Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

## Active recall
How do you check if any value appears at least twice in an array in linear time?

## Core idea
Traverse the array while adding elements to a Hash Set. If set.add(num) returns false (or if num is already in set), return true immediately. If loop finishes without duplicates, return false.

## Hints
- **Hint 1**: What data structure provides O(1) average membership checking?
- **Hint 2**: Can you return true immediately as soon as a duplicate is seen?

## Pattern
**Pattern**: Hash Set Early Exit
Use when: Arrays & Hashing problems require efficient traversal or optimal sub-structure.

## Trick
Early return upon first duplicate gives best-case O(1) time without reading the entire array.

## Complexity
Time: O(N) average. Space: O(N) auxiliary space for the hash set.

## Edge cases
- All unique: [1, 2, 3, 4] -> false.
- Immediate duplicate: [1, 1, 1] -> true.
- Single element: [1] -> false.
