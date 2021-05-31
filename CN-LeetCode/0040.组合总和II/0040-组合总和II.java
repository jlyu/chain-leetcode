class Solution {
    private List<List<Integer>> ans = new ArrayList<List<Integer>> ();

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        if (candidates == null || candidates.length == 0 ) { return ans; }
        List<Integer> list = new ArrayList<Integer> ();
        Arrays.sort(candidates);
        backtracking(candidates, 0, target, list);
        return ans;
    }

    private void backtracking(int[] candidates, int start, int target, List<Integer> list) {
        if (target == 0) {
            ans.add(new ArrayList<Integer>(list));
            return;
        }

        for (int i = start; i < candidates.length && target >= candidates[i]; i++) {
            if (i > start && candidates[i] == candidates[i - 1]) {
                continue;
            }

            list.add(candidates[i]);
            backtracking(candidates, i + 1, target - candidates[i], list);
            list.remove(list.size() - 1);
        }

    }
}