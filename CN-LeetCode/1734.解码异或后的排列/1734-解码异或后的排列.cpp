class Solution {
public:
    /*!
     *  ��������.
     *  ǰ��֪ʶ��
     *      - a ^ b ^ a = b;
     *      - ������������n��1��n�������������: 1��0��1��0��1��0....
     *
     *      @param [in,out] encoded ��������
     *
     *      @return ԭ����
     */
    vector<int> decode(vector<int>& encoded) {
        size_t n{ encoded.size() + 1 };
        size_t sum = !((n & 3) / 2);    //����1��n�����
        for (size_t i{ 1 }; i < n - 1; i += 2)
        {
            sum ^= encoded[i];  //���ó���һ��Ԫ��
        }
        vector<int> ans;
        ans.push_back(sum);     //��Ԫ������
        for (size_t i{}; i < n - 1; ++i)
        {
            sum ^= encoded[i];
            ans.push_back(sum);
        }
        return ans;
    }
};