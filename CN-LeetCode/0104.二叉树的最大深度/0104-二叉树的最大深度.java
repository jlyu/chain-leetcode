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
    public int maxDepth(TreeNode root) {
        //return dfs(root, 0);
        
        int maxDepth = 0;
        if (root == null) { return maxDepth; }
        

        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);

        while(!q.isEmpty()) {
            
            maxDepth++;

            int n = q.size();
            for (int i = 0; i < n; i++) {
                TreeNode node = q.poll();

                if (node.left != null) { q.offer(node.left); }
                if (node.right != null) { q.offer(node.right); }
            }
        }
        return maxDepth;

    }

    private int dfs(TreeNode root, int depth) {
        if (root == null) { return depth; }
        return Math.max(
            dfs(root.left, depth + 1),
            dfs(root.right, depth + 1)
        );
    }
}