class Solution {
    private List<List<Integer>> ans = new ArrayList<List<Integer>>();

    public List<List<Integer>> combinationSum3(int k, int n) {
        List<Integer> list = new ArrayList<Integer>();
        backtracking(1, k, n, list);
        return ans;
    }

    private void backtracking(int start, int k, int target, List<Integer> list) {
        if (k == 0 && target == 0) {
            ans.add(new ArrayList<Integer> (list));
            return;
        }

        for (int i = start; i <= 9; i++) {
            list.add(i);
            backtracking(i + 1, k - 1, target - i, list);
            list.remove(list.size() -  1);
        }
    }
}