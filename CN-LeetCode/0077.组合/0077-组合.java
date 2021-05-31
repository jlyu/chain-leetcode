class Solution {
    List<List<Integer>> ans = new ArrayList<List<Integer>> ();

    public List<List<Integer>> combine(int n, int k) {
        List<Integer> list = new ArrayList<Integer> ();
        backtracking(n, 1, k, list);
        return ans;
    }

    private void backtracking(int n, int start, int k, List<Integer> list) {
        if (k == 0) {
            ans.add(new ArrayList<Integer> (list));
            return;
        }

        for (int i = start; i <= n; i++) {
            list.add(i);
            backtracking(n, i + 1, k - 1, list);
            list.remove(list.size() - 1);
        }
    }
}