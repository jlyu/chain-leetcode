class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b) -> b - a);
        
        int m = matrix.length;
        int n = (m > 0) ? matrix[0].length : 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pq.size() < k || matrix[i][j] <= pq.peek()) {
                    pq.offer(matrix[i][j]);
                }
                if (pq.size() > k) {
                    pq.poll();
                }
            }
        }
        return pq.peek();
    }
}