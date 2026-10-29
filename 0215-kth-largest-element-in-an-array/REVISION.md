# Kth Largest Element in an Array

- **Problem Number**: #017
- **Difficulty**: Medium
- **Topic**: Sorting & Heap
- **Pattern**: Min-Heap of Size K / Quickselect
- **LeetCode Equivalent**: [LC 215: Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

## Active recall
How do you find the kth largest element in an unsorted array without fully sorting the array?

## Core idea
Approach 1 (Min-Heap): Maintain a min-heap of size k. For each num in array, push to heap. If heap size > k, pop the minimum. At the end, heap.peek() is the kth largest element. Approach 2 (Quickselect): Partition array around random pivot until pivot index is n - k in O(N) average time.

## Hints
- **Hint 1**: Do you need to sort all N elements if you only care about the top K?
- **Hint 2**: A min-heap of size K keeps the K largest elements seen so far; its root is the smallest of those K.

## Pattern
**Pattern**: Min-Heap of Size K / Quickselect
Use when: Sorting & Heap problems require efficient traversal or optimal sub-structure.

## Trick
Using a MIN-heap of size K keeps the K largest numbers, so the root is the kth largest. Heap size never exceeds K + 1.

## Complexity
Time: O(N log K) with min-heap, or O(N) average with Quickselect. Space: O(K) for the min-heap.

## Edge cases
- k == 1: maximum element.
- k == n: minimum element.
- Array with many duplicates: [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4.
