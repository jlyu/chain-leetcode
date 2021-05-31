class Solution {
    Map<Integer, Integer> map = new HashMap<>();

    
    public int getKth(int lo, int hi, int k) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) -> a[1] == b[1] ? b[0] - a[0] : b[1] - a[1]);
        for (int i = lo; i <= hi; i++) {
            int weight = step(i);
            //System.out.printf("%d = %d\r\n", i, weight);
            pq.offer(new int[] {i, weight});

            if (pq.size() > k) {
                pq.poll();
            }
        }
        return pq.peek()[0];
    }

    public int step(int num) {
        int count = 0;
        while (num != 1) {
            // int cachedStep = map.getOrDefault(num, -1);
            // if (cachedStep != -1) {
            //     int totalStep = count + cachedStep;
            //     map.put(num, totalStep);
            //     return totalStep;
            // }

            if ((num & 1) == 0) {
                num >>= 1;
            } else {
                num += (num << 1) + 1;
            }
            count++;
        }
        return count;
    }

    private int calcWeight(int x) {
        int step = 0;
        while(x != 1) {
            int cachedStep = map.getOrDefault(x, -1);
            if (cachedStep != -1) {
                int totalStep = step + cachedStep;
                map.put(x, totalStep);
                return totalStep;
            }
            if (x % 2 == 0) {
                x = x / 2;
            } else {
                x = 3 * x + 1;
            }
            step++;
        }
        return step;
    }
}