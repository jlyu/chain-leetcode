class Solution {
    public int trap(int[] height) {
        if (height == null || height.length == 0) {
            return 0;
        }

        int i = 0;
        int j = height.length - 1;
        int res = 0;

        int iMax = height[i];
        int jMax = height[j];

        while(i < j) {
            iMax = Math.max(iMax, height[i]);
            jMax = Math.max(jMax, height[j]);

            if (iMax < jMax) {
                res += iMax - height[i];
                i++;
            } else {
                res += jMax - height[j];
                j--;
            }
        }
        return res;
    }
}