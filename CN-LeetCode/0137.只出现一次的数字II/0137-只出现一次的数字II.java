class Solution {
    public int singleNumber(int[] nums) {
        int one = 0, two = 0, three;
        for (int num : nums) {
            // two����Ӧ��λ����1����ʾ��λ����2��
            two |= (one & num);
            // one����Ӧ��λ����1����ʾ��λ����1��
            one ^= num;
            // three����Ӧ��λ����1����ʾ��λ����3��
            three = (one & two);
            // �����Ӧ��λ����3�Σ����λ����Ϊ0
            two &= ~three;
            one &= ~three;
        }
        return one;
    }
}