# Container With Most Water

- **Problem Number**: #005
- **Difficulty**: Medium
- **Topic**: Two Pointers
- **Pattern**: Inward Shrinking Two Pointers
- **LeetCode Equivalent**: [LC 11: Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

## Active recall
How do you find two vertical lines that together with the x-axis hold the most water in O(N) time?

## Core idea
Start with two pointers at opposite ends (left = 0, right = n - 1). The area is min(height[left], height[right]) * (right - left). Since width decreases as pointers move inward, the only way to find a larger area is to seek a taller boundary by moving the pointer with the smaller height inward.

## Hints
- **Hint 1**: Width is maximized at the very ends. What happens to the width as you move pointers inward?
- **Hint 2**: Which pointer should you move inward: the shorter line or the taller line?

## Pattern
**Pattern**: Inward Shrinking Two Pointers
Use when: Two Pointers problems require efficient traversal or optimal sub-structure.

## Trick
Always move the pointer pointing to the shorter vertical bar. Keeping the shorter bar and moving the taller bar can only decrease width without any chance of increasing the limiting height.

## Complexity
Time: O(N) because left and right converge in N - 1 steps. Space: O(1) auxiliary space.

## Edge cases
- Two lines only: [1, 1] -> 1.
- Strictly increasing or decreasing heights: [1, 2, 3, 4, 5].
- Plateau of equal heights: [4, 4, 4, 4].
