# Path Sum

- **Problem Number**: #012
- **Difficulty**: Easy
- **Topic**: Trees
- **Pattern**: DFS Root-to-Leaf Path Recursion
- **LeetCode Equivalent**: [LC 112: Path Sum](https://leetcode.com/problems/path-sum/)

## Active recall
How do you check if a binary tree has a root-to-leaf path such that the sum of values along the path equals targetSum?

## Core idea
Base case: if root is null, return false. Subtract root.val from targetSum. If the current node is a leaf (left == null and right == null), check if remaining targetSum == 0. Otherwise, recurse on left and right subtrees: hasPathSum(root.left, targetSum) || hasPathSum(root.right, targetSum).

## Hints
- **Hint 1**: What defines a leaf node? A node with NO children.
- **Hint 2**: Instead of accumulating sum, subtract root.val from targetSum as you descend.

## Pattern
**Pattern**: DFS Root-to-Leaf Path Recursion
Use when: Trees problems require efficient traversal or optimal sub-structure.

## Trick
A path must go all the way to a leaf. If a node has only one child, you cannot claim a match at the missing child.

## Complexity
Time: O(N) visits each node once in the worst case. Space: O(H) call stack height.

## Edge cases
- Empty tree: root == null -> false (even if targetSum == 0).
- Negative node values and negative targets.
- Single node matching target: [5], target = 5 -> true.
