/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canPartition = function(nums) {
    let sum = 0;
    for (let num of nums) {
        sum += num;
    }

    if (sum % 2 !== 0) { return false; }
    const target = sum / 2;
    const dp = new Array(target + 1).fill(0);

    const N = nums.length;
    for (let i = 1; i < N; i++) {
        for (let j = target; j >= nums[i]; j--) {

            dp[j] = Math.max(dp[j], dp[j - nums[i]] + nums[i]);
        }
    }
    return dp[target] === target;
};