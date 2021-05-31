/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    private boolean isSymmetricHelper(TreeNode leftNode, TreeNode rightNode) {
        if (leftNode == null && rightNode == null) { return true; }
        if ((leftNode != null && rightNode != null) && (leftNode.val != rightNode.val)) { return false; }
        if ((leftNode == null && rightNode != null) || (leftNode != null && rightNode == null)) { return false; }
        
        return isSymmetricHelper(leftNode.left, rightNode.right) && isSymmetricHelper(leftNode.right, rightNode.left);
    }

    public boolean isSymmetric(TreeNode root) {
        //return isSymmetricHelper(root, root);
        if (root == null || (root.left == null) && (root.right == null)) { 
            return true;
        }

        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root.left);
        q.offer(root.right);

        while(!q.isEmpty()) {
            TreeNode left = q.poll();
            TreeNode right = q.poll();

            if (left == null && right == null) { continue; }
            if (left == null || right == null) { return false; }
            if (left.val != right.val) { return false; }

            q.offer(left.left);
            q.offer(right.right);
            q.offer(left.right);
            q.offer(right.left);
        }
        return true;
    }
}


 
 