class Solution {
    public int maxProfit(int[] prices) {
        if (prices == null || prices.length == 0) { return 0; }
        int n = prices.length;
        int hold = -prices[0];
        int noHold = 0;

        for (int i = 1; i < n; i++) {
            noHold = Math.max(noHold, hold + prices[i]);
            hold = Math.max(hold, -prices[i]);
        }
        return noHold;
    }
}