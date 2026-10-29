# Maximum Subarray

- **Problem Number**: #027
- **Difficulty**: Medium
- **Topic**: Dynamic Programming
- **Pattern**: Kadane's Algorithm
- **LeetCode Equivalent**: [LC 53: Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

## Active recall
How do you find the contiguous subarray with the largest sum in O(N) time and O(1) space?

## Core idea
Kadane's Algorithm: Maintain currentSum and maxSum initialized to nums[0]. For each subsequent number x: currentSum = max(x, currentSum + x). Update maxSum = max(maxSum, currentSum). If currentSum becomes negative, resetting to x means abandoning a dragged-down prefix.

## Hints
- **Hint 1**: If your running sum is negative, does extending it help any future subarray?
- **Hint 2**: At each step, decide: start a new subarray at nums[i], or extend the existing one?

## Pattern
**Pattern**: Kadane's Algorithm
Use when: Dynamic Programming problems require efficient traversal or optimal sub-structure.

## Trick
Initialize both currentSum and maxSum to nums[0] (not 0) to correctly handle arrays with all negative numbers.

## Complexity
Time: O(N) single linear pass. Space: O(1) constant space.

## Edge cases
- All negative numbers: [-3, -1, -5] -> -1.
- Single element: [1] -> 1, [-2] -> -2.
- Alternating signs: [5, -3, 5] -> 7.
