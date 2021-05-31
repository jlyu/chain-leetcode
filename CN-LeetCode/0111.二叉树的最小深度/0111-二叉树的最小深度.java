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

    public int minDepth(TreeNode root) {
        int d = 0;
        if (root == null) { 
            return d;
        }

        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);

        while (!q.isEmpty()) {
            int n = q.size();
            d++;

            for (int i = 0; i < n; i++) {
                TreeNode node = q.poll();

                if (node.left == null && node.right == null) {
                    return d;
                }

                if (node.left != null) { q.offer(node.left); }
                if (node.right != null) { q.offer(node.right); }
            }
        }
        return d;
    }   


    public int dfs(TreeNode root) {
        if (root == null) { return 0; }
        int L = dfs(root.left);
        int R = dfs(root.right);
        if (L == 0 || R == 0) { return L + R + 1; }
        return Math.min(L, R) + 1;
    }
}