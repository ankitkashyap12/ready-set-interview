# Two Sum

- **Problem Number**: #001
- **Difficulty**: Easy
- **Topic**: Arrays & Hashing
- **Pattern**: Hash Map Complement Lookup
- **LeetCode Equivalent**: [LC 1: Two Sum](https://leetcode.com/problems/two-sum/)

## Active recall
Given an array of integers and a target sum, how do you find the indices of the two numbers that add up to target in O(N) time?

## Core idea
Traverse the array once while maintaining a hash map of seen numbers to their indices. For each element num at index i, check if complement = target - num already exists in the map. If found, return [map[complement], i]. Otherwise, store map[num] = i.

## Hints
- **Hint 1**: What value would complete the pair with the current element nums[i]?
- **Hint 2**: Can you look up previously visited values in O(1) time using a hash map before inserting the current one?

## Pattern
**Pattern**: Hash Map Complement Lookup
Use when: Arrays & Hashing problems require efficient traversal or optimal sub-structure.

## Trick
Query the hash map for complement BEFORE inserting nums[i]. This prevents pairing an element with itself and handles duplicate numbers naturally.

## Complexity
Time: O(N) single pass through the array. Space: O(N) auxiliary space to store up to N entries in the hash map.

## Edge cases
- Exactly two elements matching target: [3, 3], target = 6.
- Negative numbers and zero: [-3, 4, 3, 90], target = 0.
- Target sum requires large integer values.
