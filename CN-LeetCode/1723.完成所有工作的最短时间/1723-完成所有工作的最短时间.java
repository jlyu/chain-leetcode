class Solution {
    public int minimumTimeRequired(int[] jobs, int k) {
        int len = jobs.length, sc = 1 << len;
        int[] sum = new int[sc];
        for (int i = 1; i < sc; i++) {
            // sum表示当前状态下所有工作时间之和
            sum[i] = sum[i & (i - 1)] + jobs[Integer.numberOfTrailingZeros(i)];
        }
        int[][] dp = new int[k][sc];
        System.arraycopy(sum, 0, dp[0], 0, sc);
        for (int i = 1; i < k; i++) {
            for (int j = 0; j < sc; j++) {
                int min = Integer.MAX_VALUE;
                // x = (x - 1) & j 很牛批，可以直接枚举所有j范围内的状态子集。
                // x - 1 会取最低位的1为0，后面的0为1，再 &j 把不相干的位去掉。
                for (int x = j; x != 0; x = (x - 1) & j) {
                    min = Math.min(min, Math.max(dp[i - 1][j - x], sum[x]));
                }
                dp[i][j] = min;
            }
        }
        return dp[k - 1][sc - 1];
    }
}