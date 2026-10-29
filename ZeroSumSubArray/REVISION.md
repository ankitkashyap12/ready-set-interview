# Zero Sum Subarray

- **Problem Number**: #051
- **Difficulty**: Medium
- **Topic**: Arrays & Hashing
- **Pattern**: Prefix Sum Frequency / Set
- **LeetCode Equivalent**: [LC 560: Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

## Active recall
How do you check if an array contains a contiguous subarray that sums to zero in O(N) time?

## Core idea
Maintain a running prefixSum and a hash set of seen prefix sums, initialized with {0}. For each num in nums: prefixSum += num. If prefixSum is already in the set, then the elements between that previous occurrence and the current index sum to zero; return true! Otherwise, add prefixSum to set. If loop finishes, return false.

## Hints
- **Hint 1**: If prefix sum at index i equals prefix sum at index j (i < j), what is the sum of subarray [i+1..j]?
- **Hint 2**: Remember to initialize your set with 0 to catch subarrays starting at index 0.

## Pattern
**Pattern**: Prefix Sum Frequency / Set
Use when: Arrays & Hashing problems require efficient traversal or optimal sub-structure.

## Trick
A subarray sum(A[i..j]) equals prefixSum[j] - prefixSum[i-1]. If prefixSum[j] == prefixSum[i-1], the sum is 0. Initializing the set with 0 covers subarrays starting at index 0.

## Complexity
Time: O(N) single pass. Space: O(N) to store prefix sums in a set.

## Edge cases
- Single element 0: [0] -> true.
- The entire array sums to zero: [-1, 1] -> true.
- No zero sum subarray: [1, 2, 3] -> false.
