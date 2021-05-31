class Solution {
    public int numSquares(int n) {
        Queue<Integer> q = new LinkedList<Integer>();
        q.offer(0);
    
        int[] dist = new int[n + 1];
        Arrays.fill(dist, Integer.MAX_VALUE); //MUST
        dist[0] = 0;

        while (!q.isEmpty()) {
    
            int t = q.poll();
            if (t == n) { return dist[t]; }

            for (int i = 1; t + i * i <= n; i++ ) {
                int k = t + i * i;
                if (dist[k] > dist[t] + 1) {
                    dist[k] = dist[t] + 1;
                    q.offer(k);
                }
            }
        }
        return -1;
    }
}