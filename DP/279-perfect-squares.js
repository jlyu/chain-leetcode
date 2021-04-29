/**
 * @param {number} n
 * @return {number}
 */
var numSquares = function(n) {
    const INF = Infinity;
    let sqrts = [];
    for (let i = 0; i * i <= n; i++) {
        sqrts[i] = i * i;
    }

    const dp = new Array(n + 1).fill(INF);
    for (let i = 0; i * i<= n; i++) {
        dp[i * i] = 1;
    }

    for (let i = 0; i <= n; i++) {
        for (let j = sqrts[i]; j <= n; j++) {
            dp[j] = Math.min(dp[j], dp[j-sqrts[i]] + 1);
        }
    }
    return dp[n];
};