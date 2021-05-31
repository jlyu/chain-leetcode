class KthLargest {
    PriorityQueue<Integer> pq = new PriorityQueue<>();
    int K = 0;
    public KthLargest(int k, int[] nums) {
        this.K = k;
        for (int x: nums) {
            add(x);
        }
    }
    
    public int add(int val) {
        if (pq.size() < K || val > pq.peek()) {
            pq.offer(val);
        }
        
        if (pq.size() > K) {
            pq.poll();
        }
        return pq.peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */