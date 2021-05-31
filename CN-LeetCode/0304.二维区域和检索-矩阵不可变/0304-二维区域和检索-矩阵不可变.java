class NumMatrix {
    private int[][] preSum;

    public NumMatrix(int[][] matrix) {
        int m = matrix.length;
        int n = (m > 0) ? matrix[0].length : 0;
        preSum = new int[m][n+1];

        for(int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                preSum[i][j+1] = preSum[i][j] + matrix[i][j];
            }
        }
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        int result = preSum[0][0];
        for (int i = row1; i <= row2; i++) {
            result += preSum[i][col2 + 1] - preSum[i][col1];
        }
        return result;
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */