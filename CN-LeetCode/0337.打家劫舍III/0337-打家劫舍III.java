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
    private HashMap<TreeNode, Integer> memo = new HashMap<>();
    public int rob(TreeNode root) {
        if (root == null) { 
            return 0;
        }

        // Memo
        if (memo.containsKey(root)) {
            return memo.get(root);
        }

        int toRob = root.val + ((root.left == null) ? 0 : rob(root.left.left) + rob(root.left.right))
                             + ((root.right == null) ? 0 : rob(root.right.left) + rob(root.right.right));
        int notRob = rob(root.left) + rob(root.right);
        int ans = Math.max(toRob, notRob);
        memo.put(root, ans);

        return ans;
    }
}