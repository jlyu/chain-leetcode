class Solution {
    private List<List<Integer>> ans = new ArrayList<List<Integer>>();

    public List<List<Integer>> permuteUnique(int[] nums) {
        if (nums == null || nums.length == 0) {
            return ans;
        }
        Arrays.sort(nums);
        boolean[] visited = new boolean[nums.length];
        List<Integer> list = new ArrayList<Integer> ();
        backtracking(nums, visited, list);
        return ans;
    }

    private void backtracking(int[] nums, boolean[] visited, List<Integer> list) {
        if (list.size() == nums.length) {
            //if (ans.contains(list)) { return; }
            ans.add(new ArrayList<Integer>(list));
            return;
        }

        for (int i = 0; i < nums.length; i++) {


 

            if (visited[i] || (i > 0 && nums[i] == nums[i-1] && !visited[i-1]) ) {
                continue;
            }
            
                visited[i] = true;
                list.add(nums[i]);
                backtracking(nums, visited, list);
                list.remove(list.size() - 1);
                visited[i] = false;

        }
    }
}