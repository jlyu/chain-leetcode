class Solution {
    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> b[1] + b[0] - a[1] - a[0]);

        for(int i = 0; i < nums1.length; i++) {
            for (int j = 0; j < nums2.length; j++) {
                if (pq.size() < k || nums1[i] + nums2[j] <= pq.peek()[0] + pq.peek()[1]) {
                    pq.offer(new int[]{ nums1[i], nums2[j] });
                }
                
                if (pq.size() > k) {
                    pq.poll();
                }
            }
        }
        
        List<List<Integer>> res = new LinkedList<List<Integer>>();
        while(!pq.isEmpty()) {
            int[] n = pq.poll();
            List<Integer> list = Arrays.asList(n[0], n[1]);
            res.add(0, list);
        }
        return res;
    }
}