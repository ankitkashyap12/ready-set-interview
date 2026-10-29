# Longest Peak

- **Problem Number**: #033
- **Difficulty**: Medium
- **Topic**: Arrays & Hashing
- **Pattern**: Peak Detection & Bidirectional Expansion
- **LeetCode Equivalent**: [LC 845: Longest Mountain in Array](https://leetcode.com/problems/longest-mountain-in-array/)

## Active recall
How do you find the length of the longest peak (strictly increasing then strictly decreasing subarray of length >= 3) in O(N) time?

## Core idea
A peak occurs at index i if array[i-1] < array[i] and array[i] > array[i+1]. Iterate i from 1 to n - 2 to find peaks. When a peak is found, expand leftwards while array[left-1] < array[left], and rightwards while array[right+1] < array[right]. The peak length is right - left + 1. Update longestPeak = max(longestPeak, peakLength) and jump i directly to right to maintain linear time.

## Hints
- **Hint 1**: First identify true peaks: elements strictly greater than both immediate neighbors.
- **Hint 2**: Once a peak is identified, expand two pointers outwards as far as the slopes remain strictly decreasing.

## Pattern
**Pattern**: Peak Detection & Bidirectional Expansion
Use when: Arrays & Hashing problems require efficient traversal or optimal sub-structure.

## Trick
Jump the outer loop index i = right after exploring a peak, because no intermediate index along a decreasing slope can be a new peak.

## Complexity
Time: O(N) because each element is visited at most a constant number of times. Space: O(1) auxiliary space.

## Edge cases
- Array length < 3: cannot form a peak -> return 0.
- Strictly increasing or strictly decreasing array: no peak -> return 0.
- Flat plateaus [1, 2, 2, 1]: not a valid peak.
