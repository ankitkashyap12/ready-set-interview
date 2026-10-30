# Who Has the Majority

- **Problem Number**: #059
- **Difficulty**: Easy
- **Topic**: Arrays & Frequency Counting
- **Pattern**: Dual Counter Frequency Comparison
- **LeetCode Equivalent**: [LC 169: Majority Element](https://leetcode.com/problems/majority-element/)

## Active recall
Given an array and two specific target values x and y, how do you find which has a higher frequency, breaking ties by returning the smaller value?

## Core idea
Iterate through the array once maintaining two counter variables, countX and countY. Increment countX when seeing x, and countY when seeing y. At the end, compare the two counts. If countX > countY return x; if countY > countX return y; if they are equal return min(x, y).

## Hints
- **Hint 1**: You only care about two specific numbers, so you do not need a full hash map.
- **Hint 2**: Single pass with two counters solves it in O(1) auxiliary space.

## Pattern
**Pattern**: Dual Counter Frequency Comparison
Use when: Frequency comparison is constrained to a fixed pair of candidate values.

## Trick
When frequencies tie (countX == countY), the problem statement requires returning the smaller element: Math.min(x, y).

## Complexity
Time: O(N) single pass through the array. Space: O(1) auxiliary space using two integer counters.

## Edge cases
- x or y does not appear at all (frequency 0).
- Both have equal frequency: tie-break with min(x, y).
- x == y: either branch correctly returns x.

