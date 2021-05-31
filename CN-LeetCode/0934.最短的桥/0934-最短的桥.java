class Solution {

    private int[] dx = {-1, 0, 1, 0};
    private int[] dy = {0, 1, 0, -1};
    private int res = 0;

    public int shortestBridge(int[][] A) {
        int m = A.length;
        int n = (m > 0) ? A[0].length : 0;
        // 1. 先 dfs 将找到的第一座桥的值全部赋值为2，并将第一座桥旁边的 0 全部插入队列中
        // 2. 再 while 循环判断队列是否为空，循环体里会判断是否发现了第二座桥；
        Queue<int[]> q = new LinkedList<>();
        // 先 dfs，将第一座岛上所有值都该为 2
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

        // bfs 寻找下一座岛屿，遍历时将所有 0 值赋值为 2
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
        // 插入所有为 0 的值的坐标到队列中
        // 为 1 的值就改变为 2 并且继续遍历四个方向
        // 为 2 的值就直接退出
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