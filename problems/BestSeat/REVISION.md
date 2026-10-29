# Best Seat

- **Problem Number**: #029
- **Difficulty**: Medium
- **Topic**: Arrays & Hashing
- **Pattern**: Contiguous Zero Block Maximization (Midpoint)
- **LeetCode Equivalent**: [LC 849: Maximize Distance to Closest Person](https://leetcode.com/problems/maximize-distance-to-closest-person/)

## Active recall
In a row of theater seats (0 is empty, 1 is occupied), which seat maximizes your distance to the closest person on either side?

## Core idea
Scan the array to identify every contiguous sequence of 0s bounded by 1s. For each empty segment starting at left and ending at right (where seats[left-1] == 1 and seats[right] == 1), the length of available space is right - left. The most isolated seat in this segment is the integer midpoint (left + right - 1) // 2. Track the segment with the maximum length and return its midpoint.

## Hints
- **Hint 1**: You want to maximize the minimum distance to occupied seats on both sides.
- **Hint 2**: Find the longest contiguous run of zeros bounded by 1s; your best choice is sitting right in the middle.

## Pattern
**Pattern**: Contiguous Zero Block Maximization (Midpoint)
Use when: Arrays & Hashing problems require efficient traversal or optimal sub-structure.

## Trick
The best seat in a contiguous block of zeros between indices left and right - 1 is located at (left + right - 1) // 2. If no zeros exist, return -1.

## Complexity
Time: O(N) single linear scan of seats. Space: O(1) constant extra variables.

## Edge cases
- No empty seats (all 1s): return -1.
- Single empty seat: [1, 0, 1] -> seat 1.
- Multiple contiguous zero blocks of equal length: return the first one encountered.
