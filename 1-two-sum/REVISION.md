# Two Sum

- **Problem Number**: #002
- **Difficulty**: Easy
- **Topic**: Arrays & Hashing
- **Pattern**: Hash Map Complement Lookup
- **LeetCode Equivalent**: [LC 1: Two Sum](https://leetcode.com/problems/two-sum/)

## Active recall
How can you solve Two Sum in O(N) time and O(N) space using one single forward pass?

## Core idea
Maintain a hash table mapping each visited value to its index. For each number, compute complement = target - num. If complement is in the map, return the stored index and current index. Otherwise, record map[num] = index.

## Hints
- **Hint 1**: Do you need to sort the array? Sorting takes O(N log N) and loses original indices unless paired.
- **Hint 2**: Check complement existence before recording the current element.

## Pattern
**Pattern**: Hash Map Complement Lookup
Use when: Arrays & Hashing problems require efficient traversal or optimal sub-structure.

## Trick
Single-pass hash table check-then-insert guarantees you never reuse the same index.

## Complexity
Time: O(N) average time for hash table operations. Space: O(N) for the hash map.

## Edge cases
- Duplicate values forming target: [3, 3] target 6.
- Array with negative values.
