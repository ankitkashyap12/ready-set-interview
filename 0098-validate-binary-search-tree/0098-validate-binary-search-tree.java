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
    public boolean isValidBST(TreeNode root) {
        return dfs(root,Long.MAX_VALUE,Long.MIN_VALUE);
    }

    boolean dfs(TreeNode root,long max,long min){
        if(root==null){
            return true;
        }
        int val =root.val;
        //System.out.println(val+">="+max+" || "+val+"<="+min);
        if(val>=max || val<=min){
            
            return false;
        }
        boolean isLeftBalanced = dfs(root.left,val,min);
        boolean isRightBalanced = dfs(root.right,max,val);

        return isLeftBalanced && isRightBalanced;
        
    }
}