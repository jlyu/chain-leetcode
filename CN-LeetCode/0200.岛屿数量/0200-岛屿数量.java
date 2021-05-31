class Solution {
    public int numIslands(char[][] grid) {
        int m = grid.length;
        int n = (m > 0) ? grid[0].length : 0;

        int islands = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    islands++;
                    dfs(grid, i, j);
                }
            }
        }
        return islands;
    }

    private void dfs(char[][] grid, int sr, int sc) {
        int m = grid.length;
        int n = (m > 0) ? grid[0].length : 0;

        grid[sr][sc] = '0';

        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};
        for (int i = 0; i < 4; i++) {
            int x = sr + dx[i];
            int y = sc + dy[i];

            if (x < 0 || x >= m || y < 0 || y >= n || grid[x][y] == '0') {
                continue;
            }

            dfs(grid, x, y);
        }
    }
}