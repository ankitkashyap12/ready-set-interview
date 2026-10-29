# Two Sum

- **Problem Number**: #049
- **Difficulty**: Easy
- **Topic**: Arrays & Hashing
- **Pattern**: Hash Set / Map Complement Lookup
- **LeetCode Equivalent**: [LC 1: Two Sum](https://leetcode.com/problems/two-sum/)

## Active recall
How do you find two distinct numbers in an array that sum to a given target?

## Core idea
Use a hash set to store seen numbers. For each num in array, compute potentialMatch = target - num. If potentialMatch is in the hash set, return [potentialMatch, num]. Otherwise, add num to hash set.

## Hints
- **Hint 1**: For each number x, what number y do you need such that x + y = target?
- **Hint 2**: Store visited numbers in a hash table for instant O(1) membership checks.

## Pattern
**Pattern**: Hash Set / Map Complement Lookup
Use when: Arrays & Hashing problems require efficient traversal or optimal sub-structure.

## Trick
Checking set membership before inserting the current number ensures we never pair a number with itself.

## Complexity
Time: O(N) average time. Space: O(N) auxiliary space for the hash set.

## Edge cases
- Target can be formed by two identical numbers if array contains both: [3, 3] target 6.
- No pair sums to target: return empty array.
