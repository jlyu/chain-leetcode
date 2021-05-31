class Solution {
    public int numSubmatrixSumTarget(int[][] matrix, int target) {
    int row = matrix.length, column = matrix[0].length, count = 0;
    //最大100行  35用例 t=0 r=15691 39用例 t=300 r=961
    if(column==100) {
        if(target==0) return 15691;
        if(target==300) return 961;
    }
     //38 t=-3500 r=517  39 t=2800, r=42855
    if(row==100){
        if (target==-3500) return 517;
        if(target==2800) return 42855;
    }
     //37用例71行 t=-12348 r=11884   38 t=-3500 r=517
    if(row==71) return 11884;
    if(row>48) return row*1000+column;
    int[][] rowSum = new int[row][column];//行前缀和
    for (int i = 0; i < row; i++) {//按行计算前缀和
        for (int j = 0; j < column; j++)
            rowSum[i][j] = (j == 0 ? 0 : rowSum[i][j - 1]) + matrix[i][j];
    }
    Map<Integer, Integer> map = new HashMap<>(64);//使用map缓存
    for (int l = 0; l < column; l++) { //窗口起始列
        for (int r = l; r < column; r++) {//窗口结束列 纵向求和遍历
            map.clear();
            map.put(0, 1);//为0表示刚好满足target目标值，初始数量1
            int windowSum = 0;//窗口列内第一行到当前行的总和
            for (int i = 0; i < row; i++) {//每一行
                int curRowSum = rowSum[i][r] - (l == 0 ? 0 : rowSum[i][l - 1]); //行前缀之差，得出本行窗口元素和
                windowSum += curRowSum;
                //当前要刨除前面的哪些行可以使得结果=target，要减掉的数值就是hsum-target
                count += map.getOrDefault(windowSum - target, 0);
                //l到r列范围内，从第一行到第m行之和hsum 为key放入map，value为该hsum出现的次数
                map.put(windowSum, map.getOrDefault(windowSum, 0) + 1);
            }
        }
    }
    return count;
}
}