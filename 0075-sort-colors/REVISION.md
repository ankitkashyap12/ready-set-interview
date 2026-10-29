# Sort Colors

- **Problem Number**: #009
- **Difficulty**: Medium
- **Topic**: Two Pointers
- **Pattern**: Dutch National Flag (3-Way Partitioning)
- **LeetCode Equivalent**: [LC 75: Sort Colors](https://leetcode.com/problems/sort-colors/)

## Active recall
How do you sort an array with values 0, 1, and 2 in-place in a single pass without using a sorting library?

## Core idea
Maintain three pointers: low = 0 (boundary for 0s), mid = 0 (current element), high = n - 1 (boundary for 2s). While mid <= high: if nums[mid] == 0, swap(nums[low], nums[mid]), low++, mid++; if nums[mid] == 1, mid++; if nums[mid] == 2, swap(nums[mid], nums[high]), high-- (do not increment mid!).

## Hints
- **Hint 1**: Can you partition the array into three regions: [0..low-1] are 0s, [low..mid-1] are 1s, [high+1..n-1] are 2s?
- **Hint 2**: When swapping with high, why must mid NOT increment immediately?

## Pattern
**Pattern**: Dutch National Flag (3-Way Partitioning)
Use when: Two Pointers problems require efficient traversal or optimal sub-structure.

## Trick
When swapping nums[mid] with nums[high], the element brought from high has not been examined yet, so keep mid in place to inspect it in the next iteration.

## Complexity
Time: O(N) one pass with mid scanning up to high. Space: O(1) strictly in-place.

## Edge cases
- All same element: [0, 0, 0] or [2, 2, 2].
- Already sorted: [0, 1, 2].
- Reverse sorted: [2, 1, 0].
