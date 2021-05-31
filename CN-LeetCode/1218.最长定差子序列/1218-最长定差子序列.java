class Solution {
    public int longestSubsequence(int[] arr, int difference) {
        HashMap<Integer, Integer> dp = new HashMap<>();
        int ans = 1;
        for (int n: arr) {
            int v = dp.getOrDefault(n - difference, 0) + 1;
            ans = Math.max(ans, v);
            dp.put(n, v);
        }
        return ans;
    }
}