class Solution {
    public int minFallingPathSum(int[][] matrix) {
        int n = matrix.length;
        int ans = Integer.MAX_VALUE;
        int[][] dp = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int v = matrix[i][j];
                if (i == 0) {
                    dp[i][j] = v;
                    continue;
                }
                if (j == 0) {
                    dp[i][j] = Math.min(dp[i-1][j], dp[i-1][j+1]) + v;
                } else if (j == n-1) {
                    dp[i][j] = Math.min(dp[i-1][j], dp[i-1][j-1]) + v;
                } else {
                    dp[i][j] = Math.min(dp[i-1][j-1], Math.min(dp[i-1][j], dp[i-1][j+1])) + v;
                }
            }
        }

        
        for(int i = 0; i < n; i++) {
            ans = Math.min(ans, dp[n-1][i]);
        }
        return ans;
    }
}