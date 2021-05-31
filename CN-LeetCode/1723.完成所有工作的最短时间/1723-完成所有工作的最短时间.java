class Solution {
    public int minimumTimeRequired(int[] jobs, int k) {
        int len = jobs.length, sc = 1 << len;
        int[] sum = new int[sc];
        for (int i = 1; i < sc; i++) {
            // sum��ʾ��ǰ״̬�����й���ʱ��֮��
            sum[i] = sum[i & (i - 1)] + jobs[Integer.numberOfTrailingZeros(i)];
        }
        int[][] dp = new int[k][sc];
        System.arraycopy(sum, 0, dp[0], 0, sc);
        for (int i = 1; i < k; i++) {
            for (int j = 0; j < sc; j++) {
                int min = Integer.MAX_VALUE;
                // x = (x - 1) & j ��ţ��������ֱ��ö������j��Χ�ڵ�״̬�Ӽ���
                // x - 1 ��ȡ���λ��1Ϊ0�������0Ϊ1���� &j �Ѳ���ɵ�λȥ����
                for (int x = j; x != 0; x = (x - 1) & j) {
                    min = Math.min(min, Math.max(dp[i - 1][j - x], sum[x]));
                }
                dp[i][j] = min;
            }
        }
        return dp[k - 1][sc - 1];
    }
}