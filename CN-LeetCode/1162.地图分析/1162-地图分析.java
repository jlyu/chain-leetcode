class Solution {
    int[] dx = {0, 1, 0, -1};
    int[] dy = {1, 0, -1, 0};
    public int maxDistance(int[][] grid) {
        int m = grid.length;
        int n = (m > 0) ? grid[0].length : 0;

        boolean hasIsland = false;
        boolean hasOcean = false;
        Queue<int[]> q = new LinkedList<>();

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    q.offer(new int[] {i, j});
                    hasIsland = true;
                } else {
                    hasOcean = true;
                }
            }
        }

        if (!hasIsland || !hasOcean) { return -1; }

        int sr = 0;
        int sc = 0;
        while (!q.isEmpty()) {
            int[] point = q.poll();
            sr = point[0];
            sc = point[1];

            for (int i = 0; i < 4; i++) {
                int x = sr + dx[i];
                int y = sc + dy[i];

                if (x < 0 || x >= m || y < 0 || y >= n || grid[x][y] != 0) { 
                    continue; 
                }

                grid[x][y] = grid[sr][sc] + 1;
                q.offer(new int[] {x, y});
            }
        }
        return grid[sr][sc] - 1;

    }
}