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
    public List<Integer> largestValues(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if (root == null) { return res; }

        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);

        while(!q.isEmpty()) {
            int n = q.size();
            int maxValue = Integer.MIN_VALUE;
            for (int i = 0; i < n; i++) {
                TreeNode node = q.poll();
                maxValue = Math.max(maxValue, node.val);

                if (node.left != null) { q.offer(node.left); }
                if (node.right != null) { q.offer(node.right); }
            }
            res.add(maxValue);
        }
        return res;
    }
}