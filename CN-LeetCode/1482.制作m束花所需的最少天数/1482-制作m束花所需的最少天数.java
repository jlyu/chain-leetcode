class Solution {
    public int minDays(int[] bloomDay, int m, int k) {
        if (m * k > bloomDay.length) return -1;
        int low = Integer.MAX_VALUE, high = Integer.MIN_VALUE;
        for (int d : bloomDay) {
            low = Math.min(low, d);
            high = Math.max(high, d);
        }
        while (low <= high) {
            int mid = (low + high) >>> 1;
            if (check(bloomDay, m, k, mid)) high = mid - 1;
            else low = mid + 1;
        }
        return low;
    }
    boolean check(int[] bloomDay, int m, int k, int target) {
        int l = 0, r = 0, n = bloomDay.length;
        while (r < n) {// [l, r)为连续开花的窗口，最大长度为k
            if (bloomDay[r++] <= target) {
                if (r - l < k) continue;
                if (--m == 0) return true;
            }
            l = r;
        }
        return false;
    }
}