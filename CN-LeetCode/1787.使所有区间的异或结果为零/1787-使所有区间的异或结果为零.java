class Solution {
    // x �ķ�ΧΪ [0, 2^10)
    static final int MAXX = 1 << 10;
    // ����ֵ��Ϊ�˷�ֹ�������ѡ�� INT_MAX / 2
    static final int INFTY = Integer.MAX_VALUE / 2;

    public int minChanges(int[] nums, int k) {
        int n = nums.length;
        int[] f = new int[MAXX];
        Arrays.fill(f, INFTY);
        // �߽����� f(-1,0)=0
        f[0] = 0;
        
        for (int i = 0; i < k; ++i) {
            // �� i ����Ĺ�ϣӳ��
            Map<Integer, Integer> cnt = new HashMap<Integer, Integer>();
            int size = 0;
            for (int j = i; j < n; j += k) {
                cnt.put(nums[j], cnt.getOrDefault(nums[j], 0) + 1);
                ++size;
            }

            // ��� t2
            int t2min = Arrays.stream(f).min().getAsInt();

            int[] g = new int[MAXX];
            Arrays.fill(g, t2min);
            for (int mask = 0; mask < MAXX; ++mask) {
                // t1 ����Ҫö�� x �������
                for (Map.Entry<Integer, Integer> entry : cnt.entrySet()) {
                    int x = entry.getKey(), countx = entry.getValue();
                    g[mask] = Math.min(g[mask], f[mask ^ x] - countx);
                }
            }
            
            // �����˼��� size
            for (int j = 0; j < MAXX; ++j) {
                g[j] += size;
            }
            f = g;
        }

        return f[0];
    }
}