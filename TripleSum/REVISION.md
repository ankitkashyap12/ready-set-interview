# Triple Sum

- **Problem Number**: #048
- **Difficulty**: Medium
- **Topic**: Two Pointers
- **Pattern**: Sort + Fixed Element + Two Pointers (3Sum)
- **LeetCode Equivalent**: [LC 15: 3Sum](https://leetcode.com/problems/3sum/)

## Active recall
How do you find all triplets in an array that sum to a given target value in O(N^2) time?

## Core idea
Sort the array. Iterate i from 0 to n - 3. Set left = i + 1, right = n - 1. While left < right: currentSum = array[i] + array[left] + array[right]. If currentSum == target, append [array[i], array[left], array[right]], increment left, decrement right. If currentSum < target, increment left. If currentSum > target, decrement right.

## Hints
- **Hint 1**: Sorting the array turns the 3-variable problem into N iterations of 2Sum.
- **Hint 2**: Use two pointers converging from both ends of the remaining sub-array.

## Pattern
**Pattern**: Sort + Fixed Element + Two Pointers (3Sum)
Use when: Two Pointers problems require efficient traversal or optimal sub-structure.

## Trick
Sorted array allows deterministic pointer movements: sum too small means left must advance; sum too large means right must decrement.

## Complexity
Time: O(N^2) total (O(N log N) sort + O(N) iterations of O(N) two pointers). Space: O(N) to store triplets.

## Edge cases
- Target sum negative or zero.
- Array with fewer than 3 elements: return empty list.
- No triplet equals target.
