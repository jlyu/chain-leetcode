class Solution {
    private List<List<Integer>> ans = new ArrayList<List<Integer>>();

    public List<List<Integer>> permute(int[] nums) {
        if (nums == null || nums.length == 0) {
            return ans;
        }

        List<Integer> list = new ArrayList<Integer> ();
        backtracking(nums, list);
        return ans;
    }

    private void backtracking(int[] nums, List<Integer> list) {
        if (list.size() == nums.length) {
            ans.add(new ArrayList<Integer>(list));
            return;
        }

        for(int i = 0; i < nums.length; i++) {
            if (list.contains(nums[i])) {
                continue;
            }
            
            list.add(nums[i]);
            backtracking(nums, list);
            list.remove(list.size() -1);
        }
    }
}