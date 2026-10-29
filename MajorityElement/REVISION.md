# Majority Element

- **Problem Number**: #034
- **Difficulty**: Easy
- **Topic**: Arrays & Hashing
- **Pattern**: Boyer-Moore Voting Algorithm
- **LeetCode Equivalent**: [LC 169: Majority Element](https://leetcode.com/problems/majority-element/)

## Active recall
How do you find the majority element (element appearing more than n/2 times) in O(N) time and O(1) space?

## Core idea
Boyer-Moore Voting: Maintain candidate and count = 0. For each num in array: if count == 0, set candidate = num. If num == candidate, increment count; otherwise decrement count. Since the majority element appears more than N/2 times, its count will strictly overcome all other elements combined.

## Hints
- **Hint 1**: Think of pairing distinct elements to cancel each other out.
- **Hint 2**: If the majority element has frequency > n/2, can all minority elements combined cancel it completely?

## Pattern
**Pattern**: Boyer-Moore Voting Algorithm
Use when: Arrays & Hashing problems require efficient traversal or optimal sub-structure.

## Trick
Resetting candidate when count == 0 guarantees that the majority element survives cancellations.

## Complexity
Time: O(N) single pass. Space: O(1) constant extra memory.

## Edge cases
- Array with 1 element: return array[0].
- Majority element barely exceeding half: [2, 2, 1, 1, 2].
