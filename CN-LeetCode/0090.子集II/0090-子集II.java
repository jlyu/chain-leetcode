class Solution {
    private List<List<Integer>> ans = new ArrayList<List<Integer>> ();

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<Integer> list = new ArrayList<Integer> ();
        Arrays.sort(nums);
        backtracking(nums, 0, list);
        return ans;
    }

    private void backtracking(int[] nums, int start, List<Integer> list) {

        //if (!ans.contains(list)) {
            ans.add(new ArrayList<Integer> (list));
        //}
        

        for (int i = start; i < nums.length; i++) {
            if (i > start && nums[i] == nums[i-1]) { continue; }
            list.add(nums[i]);
            backtracking(nums, i + 1, list);
            list.remove(list.size() - 1);
        }
    }
}

