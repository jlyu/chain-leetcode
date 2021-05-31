/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    const n = nums.length;
    const dp = new Array(n);
    dp[0] = nums[0];
    let ans = dp[0];
    for (let i = 1; i < n; i++) {
        dp[i] = Math.max(nums[i], dp[i-1] + nums[i]);
        ans = Math.max(ans, dp[i]);
    }
    return ans;
};

