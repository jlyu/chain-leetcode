class Solution {

    //private int oldColor;

    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        //Pair<String, String> pair = new Pair<>("aku", "female");
        //Stack<Pair<Integer, Integer>> stack = new Stack<> ();
        //stack.push(new Pair<>(sr, sc));
        //oldColor = image[sr][sc];
        dfs(image, sr, sc, newColor);
        return image;
    }

    private void dfs(int[][] image, int sr, int sc, int newColor) {
        int m = image.length;
        int n = (m > 0) ? image[0].length : 0;

        // up, right, bottom, left
        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0,  1, 0,-1};

        int oldColor = image[sr][sc];
        if (oldColor == newColor) { return; }
        image[sr][sc] = newColor;

        for (int i = 0; i < 4; i++) {
            int x = sr + dx[i];
            int y = sc + dy[i];

            if (x >= 0 && x < m && y >= 0 && y < n && image[x][y] == oldColor) { 
                dfs(image, x, y, newColor);
            }

        }

 

    }
}