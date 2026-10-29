# Koko Eating Bananas

- **Problem Number**: #024
- **Difficulty**: Medium
- **Topic**: Binary Search
- **Pattern**: Binary Search on Answer Range
- **LeetCode Equivalent**: [LC 875: Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)

## Active recall
How do you find the minimum integer speed k to eat all bananas within h hours?

## Core idea
The eating speed k has a monotonic feasibility property: if speed k works, any speed > k also works. Binary search speed in range [1, max(piles)]. For candidate speed mid, compute total hours = sum(ceil(pile / mid)). If hours <= h, mid is feasible; try smaller speed by setting high = mid. If hours > h, speed is too slow; set low = mid + 1.

## Hints
- **Hint 1**: Is the feasibility function monotonic with respect to eating speed k?
- **Hint 2**: Ceiling division of pile / k can be computed as (pile + k - 1) // k.

## Pattern
**Pattern**: Binary Search on Answer Range
Use when: Binary Search problems require efficient traversal or optimal sub-structure.

## Trick
Compute ceiling division without floating point inaccuracy: (pile + mid - 1) // mid. Watch out for 32-bit integer overflow when summing total hours (use 64-bit long in Java/C++).

## Complexity
Time: O(N log(max(piles))) where N is length of piles. Space: O(1) auxiliary space.

## Edge cases
- h == piles.length: speed must be max(piles).
- Very large pile values: total hours can overflow 32-bit int.
- Single pile: return ceil(pile[0] / h).
