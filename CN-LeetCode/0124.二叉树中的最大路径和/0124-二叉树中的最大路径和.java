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
    int res = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        dfs(root);
        return res;
    }

    private int dfs(TreeNode root) {
        if (root == null) { return 0; }

        int L = Math.max(dfs(root.left), 0);
        int R = Math.max(dfs(root.right), 0);
        res = Math.max(res, L + R + root.val);    
        return Math.max(L, R) + root.val;
    }
}