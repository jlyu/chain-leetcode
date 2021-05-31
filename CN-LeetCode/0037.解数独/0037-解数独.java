class Solution {
    public void solveSudoku(char[][] board) {
        backtracking(board, 0, 0);
    }

    private boolean backtracking(char[][] board, int row, int col) {
        int i = 9;
        int j = 9;

        if (col == j) {
            return backtracking(board, row + 1, 0);
        }

        if (row == i) {
            return true;
        }

        if (board[row][col] != '.') {
            return backtracking(board, row, col + 1);
        }

        for (char ch = '1'; ch <= '9'; ch++) {
            if (!isValid(board, row, col, ch)) { continue; }

            board[row][col] = ch;
            if (backtracking(board, row, col + 1)) {
                return true;
            }
            board[row][col] = '.';
        }
        return false;
    }

    private boolean isValid(char[][] board, int row, int col, char ch) {
        int n = board.length;
        for (int i = 0; i < n; i++) {
            if (board[row][i] == ch) { return false; }
            if (board[i][col] == ch) { return false; }
            if (board[(row/3)*3 + i/3][(col/3)*3 + i%3] == ch) { return false; }
        }
        return true;
    }
}