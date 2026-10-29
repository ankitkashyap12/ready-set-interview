# Valid Triangle Number

- **Problem Number**: #023
- **Difficulty**: Medium
- **Topic**: Two Pointers
- **Pattern**: Sort + Reverse Pivot + Two Pointers
- **LeetCode Equivalent**: [LC 611: Valid Triangle Number](https://leetcode.com/problems/valid-triangle-number/)

## Active recall
How do you count the number of triplets that can form a valid triangle (a + b > c) in O(N^2) time?

## Core idea
Sort the array. The triangle condition simplifies: if sorted a <= b <= c, we only need to verify a + b > c. Fix the largest side k from n - 1 down to 2. Set left = 0, right = k - 1. If nums[left] + nums[right] > nums[k], then ALL elements from left to right - 1 also satisfy the condition with right, so add (right - left) to count and decrement right. Otherwise, increment left.

## Hints
- **Hint 1**: If sorted a <= b <= c, which triangle inequality is the ONLY one you need to check?
- **Hint 2**: Fix the largest side c = nums[k] and use two pointers for a and b.

## Pattern
**Pattern**: Sort + Reverse Pivot + Two Pointers
Use when: Two Pointers problems require efficient traversal or optimal sub-structure.

## Trick
When nums[left] + nums[right] > nums[k], every element from left to right - 1 paired with nums[right] also exceeds nums[k], contributing (right - left) valid triangles in O(1).

## Complexity
Time: O(N^2) (sorting O(N log N) + outer loop running N times with two pointers O(N)). Space: O(log N) sorting space.

## Edge cases
- Array with zeros: sides with length 0 can never form a triangle.
- Fewer than 3 elements: return 0.
- All equal elements: [2, 2, 2, 2].
