class Solution {
    public int maxSubArray(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        dp[0] = nums[0];

        int ans = dp[0];
        for (int i = 1; i < n; i++) {
             
            dp[i] = Math.max(nums[i], dp[i-1] + nums[i]); //(dp[i - 1] < 0 && nums[i] > dp[i - 1]) ? nums[i] : dp[i-1] + nums[i];
            ans = Math.max(ans, dp[i]);
        }

        return ans;// dp[n-1];
    }
}