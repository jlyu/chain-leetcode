class Solution {
    int[] dx = {-1, 0, 1, 0};
    int[] dy = { 0, 1, 0, -1};

    int m = 0;
    int n = 0;

    public void solve(char[][] board) {
        m = board.length;
        n = (m > 0) ? board[0].length : 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 || i == m -1 || j == 0 || j == n - 1) { 
                    if (board[i][j] == 'O') {
                        dfs(board, i, j);
                    }
                }
            }
        }
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                
                if (board[i][j] == 'O') { board[i][j] = 'X'; }
                if (board[i][j] == 'Y') { board[i][j] = 'O'; }
            }
        }
    }

    private void dfs(char[][] board, int sr, int sc) {
    
        board[sr][sc] = 'Y';
        
        boolean res = false;
        for (int i = 0; i < 4; i++) {
            int x = sr + dx[i];
            int y = sc + dy[i];

            if (x >= 0 && x < m && y >= 0 && y < n && board[x][y] == 'O') {
                dfs(board, x, y);
            }
        }
    }
}