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
    int xd = 0;
    int yd = 0;
    TreeNode xp = null;
    TreeNode yp = null;

    public boolean isCousins(TreeNode root, int x, int y) {
        dfs(root, 1, null, x, y);
        return (xd == yd) && (xp != yp);
    }

    private void dfs(TreeNode root, int depth, TreeNode parent, int x, int y) {
        if (root == null) { return; }

        if (root.val == x) { xd = depth; xp = parent; }
        if (root.val == y) { yd = depth; yp = parent; }

        dfs(root.left,  depth + 1, root, x, y);
        dfs(root.right, depth + 1, root, x, y);
    }

}