class Solution {
    private List<List<Integer>> ans = new ArrayList<List<Integer>>();

    public int numSquarefulPerms(int[] nums) {
        Arrays.sort(nums);
        boolean[] visited = new boolean[nums.length];
        List<Integer> list = new ArrayList<Integer>();
        backtracking(nums, visited, list);
        return ans.size();
    }

    private void backtracking(int[] nums, boolean[] visited, List<Integer> list) {
        if (list.size() == nums.length) {
            ans.add(new ArrayList<Integer>(list));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (visited[i]) { continue; }
            if (i > 0 && nums[i] == nums[i-1] && !visited[i-1]) { continue; }
            if (list.size() > 0 && !isSqrt(nums[i] + list.get(list.size() - 1))) { continue; }

            visited[i] = true;
            list.add(nums[i]);
            backtracking(nums, visited, list);
            list.remove(list.size() - 1);
            visited[i] = false;
        }
    }

    private boolean isSqrt(int x) {
        int sqrtX = (int)Math.sqrt(x);
        return sqrtX * sqrtX == x;
    }
}