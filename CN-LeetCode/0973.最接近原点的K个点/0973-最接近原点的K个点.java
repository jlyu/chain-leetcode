class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> b[0]*b[0] + b[1]*b[1] - a[0]*a[0] - a[1]*a[1]);

        for (int i = 0; i < points.length; i++) {
            int x1 = points[i][0];
            int y1 = points[i][1];

            if (pq.size() < k || x1*x1 + y1*y1 <= pq.peek()[0]*pq.peek()[0] + pq.peek()[1]*pq.peek()[1]) {
                pq.offer(new int[] { x1, y1 });
            }
            if (pq.size() > k) {
                pq.poll();
            }
        }

        int[][] res = new int[pq.size()][2];
        int row = 0;
        while(!pq.isEmpty()) {
            res[row++] = pq.poll();
        }
        return res;
    }
}