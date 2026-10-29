# Validate Binary Search Tree

- **Problem Number**: #010
- **Difficulty**: Medium
- **Topic**: Trees
- **Pattern**: DFS Valid Range Propagation / Inorder Traversal
- **LeetCode Equivalent**: [LC 98: Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)

## Active recall
How do you verify whether a binary tree satisfies the BST invariant across all nodes, not just immediate children?

## Core idea
A node's value must be strictly greater than all nodes in its left subtree and strictly less than all in its right subtree. Recurse with bounds: validate(node, low, high). For node: check low < node.val < high, then validate(node.left, low, node.val) and validate(node.right, node.val, high). Alternatively, do an inorder traversal and ensure strictly increasing values.

## Hints
- **Hint 1**: Does checking node.left.val < node.val < node.right.val suffice? Why not?
- **Hint 2**: Pass down the valid minimum and maximum bounds (low, high) as you traverse.

## Pattern
**Pattern**: DFS Valid Range Propagation / Inorder Traversal
Use when: Trees problems require efficient traversal or optimal sub-structure.

## Trick
Use Long or null objects for low and high bounds to handle nodes whose values equal Integer.MIN_VALUE or Integer.MAX_VALUE.

## Complexity
Time: O(N) visits each node once. Space: O(H) recursion stack where H is tree height (O(log N) balanced, O(N) skewed).

## Edge cases
- Node values equal to INT_MIN or INT_MAX: [2147483647].
- Duplicate values: [2, 2, 2] -> false (BST requires strict inequality).
- Valid local children but invalid ancestor: [5, 1, 4, null, null, 3, 6].
