# Strongest Neighbour

- **Problem Number**: #066
- **Difficulty**: Easy
- **Topic**: Arrays & Hashing
- **Pattern**: Adjacent Pair Sliding Maximum
- **LeetCode Equivalent**: [Adjacent Pair Maxima](https://leetcode.com/problems/sliding-window-maximum/)

## Active recall
For each adjacent pair of elements in an array, how do you find and print the maximum of the pair?

## Core idea
Loop i from 0 to n - 2: print max(arr[i], arr[i + 1]). This creates an array of size n - 1 where each element is the maximum of the window of size 2.

## Hints
- **Hint 1**: Slide a window of size 2 across the array.
- **Hint 2**: At each step i, output max(arr[i], arr[i + 1]).

## Pattern
**Pattern**: Adjacent Pair Sliding Maximum
Use when: Arrays & Hashing problems require efficient traversal or optimal sub-structure.

## Trick
Loop bounds stop at n - 2 to prevent an index out of bounds on arr[i + 1].

## Complexity
Time: O(N) single pass. Space: O(1) auxiliary space.

## Edge cases
- Array with exactly 2 elements.
- Array with negative numbers: max() preserves sign correctly.
