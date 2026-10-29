import java.util.LinkedList;
import java.util.Queue;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    /**
     * Approach 1: Recursive DFS (Divide and Conquer)
     * Depth is 1 + max(depth(left), depth(right)).
     * Time Complexity: O(n) - visits every node once.
     * Space Complexity: O(h) recursion stack where h is tree height (O(log n) balanced, O(n) worst).
     */
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int leftDepth = maxDepth(root.left);
        int rightDepth = maxDepth(root.right);
        return Math.max(leftDepth, rightDepth) + 1;
    }

    /**
     * Approach 2: Iterative BFS (Level-Order Traversal)
     * Processes tree level-by-level using a FIFO queue; avoids call-stack recursion.
     * Time Complexity: O(n)
     * Space Complexity: O(w) where w is max tree width (up to n/2 in complete binary tree).
     */
    public int maxDepthBFS(TreeNode root) {
        if (root == null) return 0;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        int depth = 0;

        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            for (int i = 0; i < levelSize; i++) {
                TreeNode curr = queue.poll();
                if (curr.left != null) queue.offer(curr.left);
                if (curr.right != null) queue.offer(curr.right);
            }
            depth++;
        }
        return depth;
    }
}