class Solution {
    public int totalHammingDistance(int[] nums) {
        int res = 0;
        int len = nums.length;
        for(int i = 0; i < 30; i++){
            int oneCount = 0;
            int temp = 0;
            for(int j = 0; j < len; j++){
                oneCount += nums[j] & 1;
                nums[j] >>= 1;
                temp += nums[j] == 0 ? 1 : 0;
            }
            res += oneCount * (len - oneCount);
            if(temp == len)break;
        }
        return res;
    }
}