# Count Good Nodes in Binary Tree

- **Problem Number**: #025
- **Difficulty**: Medium
- **Topic**: Trees
- **Pattern**: DFS with Running Path Maximum
- **LeetCode Equivalent**: [LC 1448: Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)

## Active recall
In a binary tree, how do you count nodes where no node on the path from root to that node has a greater value?

## Core idea
Run a DFS passing the running maximum maxSoFar along the path from root. For current node: if node.val >= maxSoFar, this node is good (count = 1), and update currentMax = max(maxSoFar, node.val). Recurse on left and right children with currentMax. Return count + dfs(left, currentMax) + dfs(right, currentMax).

## Hints
- **Hint 1**: What information does a child need from its ancestors to decide if it is 'good'?
- **Hint 2**: Pass down the maximum value seen so far along the current root-to-node path.

## Pattern
**Pattern**: DFS with Running Path Maximum
Use when: Trees problems require efficient traversal or optimal sub-structure.

## Trick
Root is always good because there are no ancestors. Update path max as max(maxSoFar, node.val) before descending.

## Complexity
Time: O(N) visits each node once. Space: O(H) recursion stack where H is tree height.

## Edge cases
- All node values identical: every node is good.
- Strictly decreasing tree: only root is good.
- Negative node values: initialize maxSoFar with root.val, not 0.
