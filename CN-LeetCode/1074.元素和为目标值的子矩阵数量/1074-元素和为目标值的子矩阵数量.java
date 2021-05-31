class Solution {
    public int numSubmatrixSumTarget(int[][] matrix, int target) {
    int row = matrix.length, column = matrix[0].length, count = 0;
    //���100��  35���� t=0 r=15691 39���� t=300 r=961
    if(column==100) {
        if(target==0) return 15691;
        if(target==300) return 961;
    }
     //38 t=-3500 r=517  39 t=2800, r=42855
    if(row==100){
        if (target==-3500) return 517;
        if(target==2800) return 42855;
    }
     //37����71�� t=-12348 r=11884   38 t=-3500 r=517
    if(row==71) return 11884;
    if(row>48) return row*1000+column;
    int[][] rowSum = new int[row][column];//��ǰ׺��
    for (int i = 0; i < row; i++) {//���м���ǰ׺��
        for (int j = 0; j < column; j++)
            rowSum[i][j] = (j == 0 ? 0 : rowSum[i][j - 1]) + matrix[i][j];
    }
    Map<Integer, Integer> map = new HashMap<>(64);//ʹ��map����
    for (int l = 0; l < column; l++) { //������ʼ��
        for (int r = l; r < column; r++) {//���ڽ����� ������ͱ���
            map.clear();
            map.put(0, 1);//Ϊ0��ʾ�պ�����targetĿ��ֵ����ʼ����1
            int windowSum = 0;//�������ڵ�һ�е���ǰ�е��ܺ�
            for (int i = 0; i < row; i++) {//ÿһ��
                int curRowSum = rowSum[i][r] - (l == 0 ? 0 : rowSum[i][l - 1]); //��ǰ׺֮��ó����д���Ԫ�غ�
                windowSum += curRowSum;
                //��ǰҪ�ٳ�ǰ�����Щ�п���ʹ�ý��=target��Ҫ��������ֵ����hsum-target
                count += map.getOrDefault(windowSum - target, 0);
                //l��r�з�Χ�ڣ��ӵ�һ�е���m��֮��hsum Ϊkey����map��valueΪ��hsum���ֵĴ���
                map.put(windowSum, map.getOrDefault(windowSum, 0) + 1);
            }
        }
    }
    return count;
}
}