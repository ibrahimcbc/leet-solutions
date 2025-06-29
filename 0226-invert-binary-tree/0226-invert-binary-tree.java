/*
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
    public TreeNode invertTree(TreeNode root) {
        if(root == null ){
            return null;
        }
        TreeNode node= root;
        
        TreeNode tempNode= node.right;
        node.right = node.left;
        node.left = tempNode;

        if(node.left != null){
            invertTree(node.left);
            }
        if(node.right!= null){
            invertTree(node.right);
            }
    
    return node;
    }
}