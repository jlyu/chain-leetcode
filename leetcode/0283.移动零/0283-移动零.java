class Solution {
    public void moveZeroes(int[] nums) {
        int i = 0;
        int j = 0;
        int n = nums.length;

    //[1, 0]
        while (j < n) {
            //if (j < n && nums[j] == 0) { ++j; }
            //if (i < n && nums[i] != 0) { ++i; }

            //System.out.printf("i=%d, j=%d\r\n", i, j);

            if (nums[j] != 0) {
                int tmp = nums[i];
                nums[i] = nums[j];
                nums[j] = tmp;
                i++;
            }
            j++;
        }
    }
}