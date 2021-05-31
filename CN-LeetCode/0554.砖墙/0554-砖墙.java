class Solution {
    public int leastBricks(List<List<Integer>> wall) {
        int ans = wall.size();

        int max = 0;
        Map<Integer, Integer> map = new HashMap<>();
        for(List<Integer> list : wall) {
            int tmp = 0;
            for(int i = 0; i < list.size() - 1; i++) {
                tmp += list.get(i);
                int now = map.getOrDefault(tmp, 0);
                map.put(tmp, now + 1);
                if(now + 1 > max) max = now + 1;
            }
        }

        return ans - max;
    }
}