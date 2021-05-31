class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int m = triangle.size();
        int n = triangle.get(m-1).size();
        int[][] dp = new int[m][n];
        dp[0][0] = triangle.get(0).get(0);

        for (int i = 0; i < m; i++) {
            for (int j = 0; j <= i; j++) { 
                if (j == 0) {
                    dp[i][j] = (i > 0) ? dp[i-1][j] + triangle.get(i).get(j) : triangle.get(0).get(0);
                }
                else if (j == i) {
                    dp[i][j] = (i > 0 && j > 0) ? dp[i-1][j-1] + triangle.get(i).get(j) : triangle.get(0).get(0);
                    continue;
                } 
                if (i > 0 && j > 0) {
                     dp[i][j] = Math.min(dp[i-1][j-1], dp[i-1][j]) + triangle.get(i).get(j);
                }
            }
        }

        int result = Integer.MAX_VALUE;
        for(int i = 0; i < n; i++) {
            result = Math.min(result, dp[m-1][i]);
        }
        return result;
    }
}