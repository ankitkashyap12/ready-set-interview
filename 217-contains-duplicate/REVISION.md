# Contains Duplicate

- **Problem Number**: #019
- **Difficulty**: Easy
- **Topic**: Arrays & Hashing
- **Pattern**: Hash Set Early Exit
- **LeetCode Equivalent**: [LC 217: Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

## Active recall
How to determine if an integer array contains any duplicate values in O(N) time?

## Core idea
Insert elements into a hash set. If an element is already present in the set, a duplicate exists; return true. Otherwise return false after processing all elements.

## Hints
- **Hint 1**: Sort vs Hash Set trade-off: Sort is O(N log N) time and O(1) space; Hash Set is O(N) time and O(N) space.
- **Hint 2**: In Java, set.add(num) returns false if the item was already present, allowing a single lookup-and-insert step.

## Pattern
**Pattern**: Hash Set Early Exit
Use when: Arrays & Hashing problems require efficient traversal or optimal sub-structure.

## Trick
set.contains or !set.add(num) enables instant early exit on first duplicate found.

## Complexity
Time: O(N) average. Space: O(N) for set.

## Edge cases
- Empty or 1 element: false.
- Immediate duplicate: [1, 1, 1] -> true.
- All distinct negative & positive numbers: [-1, 2, -3, 4] -> false.
