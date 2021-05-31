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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if (root == null) { return res; }
    
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);

        while(!q.isEmpty()) {
            int n = q.size();
            List<Integer> list = new ArrayList<Integer>();
            for(int i = 0; i < n; i++) {
                TreeNode node = q.poll();

                if (node.left != null) { q.offer(node.left); }
                if (node.right != null) { q.offer(node.right); }

                list.add(node.val);
            }
            res.add(new ArrayList<Integer>(list));
        }
        return res;
    }
}