class Solution {
    public int maximalSquare(char[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] dp = new int[m+1][n+1];
        dp[0][0] = (matrix[0][0] == '1') ? 1 : 0;

        int sideLen = dp[0][0];
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (matrix[i-1][j-1] == '1') {
                    dp[i][j] = Math.min(dp[i-1][j-1], Math.min(dp[i-1][j], dp[i][j-1])) + 1;
                    sideLen = Math.max(sideLen, dp[i][j]);
                }
            }
        }
        return sideLen * sideLen;
    }
}