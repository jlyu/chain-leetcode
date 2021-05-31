class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        Map<Integer, List<Cell>> map = new HashMap<>();
        for (int[] time: times) {
            List<Cell> edges = map.getOrDefault(time[0], new ArrayList<Cell>());
            edges.add(new Cell(time[1], time[2]));
            map.put(time[0], edges);
        }

        Map<Integer, Integer> costs = new HashMap<>();
        PriorityQueue<Cell> heap = new PriorityQueue<>();

        heap.offer(new Cell(k, 0));
        while(!heap.isEmpty()) {
            Cell curr = heap.poll();

            if (costs.containsKey(curr.node)) { continue; }
            costs.put(curr.node, curr.time);

            if (map.containsKey(curr.node)) {
                for (Cell ne: map.get(curr.node)) {
                    if (!costs.containsKey(ne.node)) {
                        heap.offer(new Cell(ne.node, ne.time + curr.time));
                    }
                }
            }
        }

        if (costs.size() != n) { return -1; }
        
        int res = 0;
        for (int cost: costs.values()) {
            res = Math.max(res, cost);
        }
        return res;
    }


}

class Cell implements Comparable<Cell> {
    int node;
    int time;
    Cell(int node, int time) {
        this.node = node;
        this.time = time;
    }

    public int compareTo(Cell cell) {
        return this.time - cell.time;
    }
}