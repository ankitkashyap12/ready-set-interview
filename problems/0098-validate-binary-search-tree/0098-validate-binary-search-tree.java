import java.util.ArrayDeque;
import java.util.Deque;

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
     * Approach 1: Recursive Range Validation (DFS)
     * Each node must satisfy min < node.val < max.
     * Note: We use Long.MIN_VALUE and Long.MAX_VALUE because a node value can be Integer.MIN_VALUE or Integer.MAX_VALUE.
     * Time Complexity: O(n)
     * Space Complexity: O(h) where h is tree height (call stack).
     */
    public boolean isValidBST(TreeNode root) {
        return dfs(root, Long.MAX_VALUE, Long.MIN_VALUE);
    }

    boolean dfs(TreeNode root, long max, long min) {
        if (root == null) {
            return true;
        }
        int val = root.val;
        if (val >= max || val <= min) {
            return false;
        }
        return dfs(root.left, val, min) && dfs(root.right, max, val);
    }

    /**
     * Approach 2: Iterative In-Order Traversal with Stack
     * In-order traversal of a BST visits nodes in strictly ascending order.
     * If any node value <= prev visited value, the tree is not a valid BST.
     * Time Complexity: O(n)
     * Space Complexity: O(h) auxiliary space for the stack.
     */
    public boolean isValidBSTInorder(TreeNode root) {
        if (root == null) return true;
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode curr = root;
        Integer prev = null;

        while (curr != null || !stack.isEmpty()) {
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }
            curr = stack.pop();
            if (prev != null && curr.val <= prev) {
                return false;
            }
            prev = curr.val;
            curr = curr.right;
        }
        return true;
    }
}