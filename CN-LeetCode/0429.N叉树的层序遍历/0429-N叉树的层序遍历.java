/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public List<List<Integer>> levelOrder(Node root) {
        List<List<Integer>> res = new ArrayList<List<Integer>> ();
        if (root == null) { return res; }

        Queue<Node> q = new LinkedList<>();
        q.offer(root);

        while(!q.isEmpty()) {
            int n = q.size();
            List<Integer> list = new ArrayList<>();

            for (int i = 0; i < n; i++) {
                Node node = q.poll();
                list.add(node.val);
                q.addAll(node.children);

                // for (Node child : node.children) {
                //     q.offer(child);
                // }
                
                // int m = node.children.size();
                // for (int j = 0; j < m; j++) {
                //     Node child = node.children.get(j);
                //     // if (child.children.size() != 0) {
                //     //     q.offer(child);
                //     // }

                //     list.add(child.val);
                // }
            }
            res.add(new ArrayList<Integer> (list));
        }
        return res;
    }
}