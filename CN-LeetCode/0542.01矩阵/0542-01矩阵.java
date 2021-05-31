class Solution {
    int[] dx = {0, 1, 0, -1};
    int[] dy = {1, 0, -1, 0};

    public int[][] updateMatrix(int[][] matrix) {
        int m = matrix.length;
        int n = (m > 0) ? matrix[0].length : 0;

        Queue<int[]> q = new LinkedList<>();
        boolean[][] visited = new boolean[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    q.offer(new int[] {i, j});
                    visited[i][j] = true;
                }
            }
        }

        int cost = 0;
        while (!q.isEmpty()) {
            int size = q.size();

            for (int i = 0; i < size; i++) {
                int[] point = q.poll();
                int x = point[0];
                int y = point[1];

                matrix[x][y] = cost;

                for (int j = 0; j < 4; j++) {
                    int newX = x + dx[j];
                    int newY = y + dy[j];

                    if (newX < 0 || newX >= m || newY < 0 || newY >= n || visited[newX][newY]) {
                        continue;
                    }

                    q.offer(new int[] { newX, newY });
                    visited[newX][newY] = true;
                }
            }
            cost++;       
        }
        return matrix;
    }
}