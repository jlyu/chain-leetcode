class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        int n = (m >= 0) ? obstacleGrid[0].length : 0;

        if (obstacleGrid[0][0] == 1) { return 0; }
        int[][] dp = new int[m][n];
        dp[0][0] = 1;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (obstacleGrid[i][j] != 1) {
                    if(i == 0 && j > 0) {
                        dp[i][j] = dp[i][j-1] == 0 ? 0 : 1;
                        continue;
                    }
                    if (j == 0 && i > 0) {
                        dp[i][j] = dp[i-1][j] == 0 ? 0 : 1;
                        continue;
                    }
                    if (i > 0 && j > 0) {
                        dp[i][j] = dp[i-1][j] + dp[i][j-1];
                    }
                    
                }
            }
        }
        return dp[m-1][n-1];
        
    }
}