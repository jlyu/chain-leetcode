class Solution {
    private List<List<Integer>> ans = new ArrayList<List<Integer>>();

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        if (candidates == null || candidates.length == 0) { return ans; }
        Arrays.sort(candidates);

        List<Integer> list = new ArrayList<Integer> ();
        backtracking(candidates, 0, target, list);
        return ans;
    }

    private void backtracking(int[] candidates, int start, int target, List<Integer> list) {
        if (target < 0) { 
            return;
        }
        if (target == 0) {
            ans.add(new ArrayList<>(list));
            return;
        }

        for (int i = start; i < candidates.length && target >= candidates[i]; i++) {
            list.add(candidates[i]);

            backtracking(candidates, i, target - candidates[i], list);

            list.remove(list.size() - 1);
        }
    }
}