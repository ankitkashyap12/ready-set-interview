# Mean and Median of Array

- **Problem Number**: #058
- **Difficulty**: Easy
- **Topic**: Math & Sorting
- **Pattern**: Sum Division & Midpoint of Sorted Array
- **LeetCode Equivalent**: [Find Median of Array](https://leetcode.com/problems/median-of-two-sorted-arrays/)

## Active recall
How do you compute the mean (floor) and median of an unsorted integer array?

## Core idea
Mean: sum all elements and compute sum // N. Median: sort the array. If N is odd, median is a[N // 2]. If N is even, median is floor((a[(N - 1) // 2] + a[N // 2]) / 2).

## Hints
- **Hint 1**: Mean is total sum divided by N.
- **Hint 2**: Median requires sorting the array first, then picking the middle element (or average of two middles).

## Pattern
**Pattern**: Sum Division & Midpoint of Sorted Array
Use when: Math & Sorting problems require efficient traversal or optimal sub-structure.

## Trick
Watch for integer division vs floor: in Java/C++, integer division truncates towards zero. Use 64-bit sum to prevent overflow.

## Complexity
Time: O(N log N) to sort for median; O(N) for mean. Space: O(1) or O(log N) sorting space.

## Edge cases
- Even vs odd N for median calculation.
- Large array elements where total sum exceeds 32-bit integer limit.
