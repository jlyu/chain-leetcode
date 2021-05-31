class Solution {

    private int[] dx = {-1, 0, 1, 0};
    private int[] dy = {0, 1, 0, -1};
    private int res = 0;

    public int shortestBridge(int[][] A) {
        int m = A.length;
        int n = (m > 0) ? A[0].length : 0;
        // 1. �� dfs ���ҵ��ĵ�һ���ŵ�ֵȫ����ֵΪ2��������һ�����Աߵ� 0 ȫ�����������
        // 2. �� while ѭ���ж϶����Ƿ�Ϊ�գ�ѭ��������ж��Ƿ����˵ڶ����ţ�
        Queue<int[]> q = new LinkedList<>();
        // �� dfs������һ����������ֵ����Ϊ 2
        boolean dfsFlag = false; 
        for (int i = 0; i < m; i++) {
            if (dfsFlag) {
                break;
            }
            for (int j = 0; j < n; j++) {
                if (A[i][j] == 1) {
                    dfs(A, q, i, j);
                    dfsFlag = true;
                    break;
                }
            }
        }

        // bfs Ѱ����һ�����죬����ʱ������ 0 ֵ��ֵΪ 2
        while (!q.isEmpty()) {
            res++;
            int size = q.size();
            while (size-- > 0) {
                int[] root = q.poll();
                for (int i = 0; i < 4; i++) {
                    int x1 = root[0] + dx[i];
                    int y1 = root[1] + dy[i];

                    if (x1 < 0 || x1 >= m || y1 < 0 || y1 >= n) { continue; }

                    if (A[x1][y1] == 1) {
                        return res;
                    } else if (A[x1][y1] == 2) {
                        continue;
                    }

                    A[x1][y1] = 2;
                    q.add(new int[]{x1,y1});
                    
                }
            } 
        }
        return res;
    }

    private void dfs(int[][] A, Queue<int[]> q, int x, int y) {
        int m = A.length;
        int n = (m > 0) ? A[0].length : 0;
        // ��������Ϊ 0 ��ֵ�����굽������
        // Ϊ 1 ��ֵ�͸ı�Ϊ 2 ���Ҽ��������ĸ�����
        // Ϊ 2 ��ֵ��ֱ���˳�
        if (x < 0 || x >= m || y < 0 || y >= n || A[x][y] == 2) {
            return;
        }
        if (A[x][y] == 0) {
            q.add(new int[]{x,y});
            return;
        }
        A[x][y] = 2;
        for (int i = 0; i < 4; i++) {
            int newX = x + dx[i];
            int newY = y + dy[i];
            dfs(A, q, newX, newY);
        }
    }
}