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
    
    public int goodNodes(TreeNode root) {
       
       return countGoodNodesDfs(root,Integer.MIN_VALUE);
        
    }

    int countGoodNodesDfs(TreeNode root, int maxVal){

         if(root==null)
            return 0;
        int count=0;
        if(root.val>=maxVal){
            maxVal=root.val;
            count+=1;
        }
        int leftCount= countGoodNodesDfs(root.left,maxVal);
        int rightCount =  countGoodNodesDfs(root.right,maxVal);
        return count+leftCount+rightCount;
    }
}