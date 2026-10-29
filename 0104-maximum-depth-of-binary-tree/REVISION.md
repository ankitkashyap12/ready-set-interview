# Maximum Depth of Binary Tree

- **Problem Number**: #011
- **Difficulty**: Easy
- **Topic**: Trees
- **Pattern**: DFS Post-Order Recursion / BFS Level Order
- **LeetCode Equivalent**: [LC 104: Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

## Active recall
How do you compute the maximum depth (number of nodes along longest root-to-leaf path) of a binary tree?

## Core idea
Base case: if root is null, depth is 0. Recursively compute leftDepth = maxDepth(root.left) and rightDepth = maxDepth(root.right). The maximum depth is 1 + max(leftDepth, rightDepth).

## Hints
- **Hint 1**: What is the depth of an empty tree?
- **Hint 2**: If you know the max depths of left and right subtrees, what is the depth of the parent?

## Pattern
**Pattern**: DFS Post-Order Recursion / BFS Level Order
Use when: Trees problems require efficient traversal or optimal sub-structure.

## Trick
Post-order bottom-up calculation: 1 + max(maxDepth(left), maxDepth(right)) solves the problem in 2 lines.

## Complexity
Time: O(N) visits every node once. Space: O(H) stack depth where H is tree height.

## Edge cases
- Empty tree: root is null -> 0.
- Single node: root only -> 1.
- Skewed tree (linked list structure): depth is N.
