class Solution {
public:
    /*!
     *  解码排列.
     *  前置知识：
     *      - a ^ b ^ a = b;
     *      - 对于所有奇数n，1到n的异或满足数列: 1、0、1、0、1、0....
     *
     *      @param [in,out] encoded 传入数组
     *
     *      @return 原数组
     */
    vector<int> decode(vector<int>& encoded) {
        size_t n{ encoded.size() + 1 };
        size_t sum = !((n & 3) / 2);    //计算1到n的异或
        for (size_t i{ 1 }; i < n - 1; i += 2)
        {
            sum ^= encoded[i];  //最后得出第一个元素
        }
        vector<int> ans;
        ans.push_back(sum);     //首元素入列
        for (size_t i{}; i < n - 1; ++i)
        {
            sum ^= encoded[i];
            ans.push_back(sum);
        }
        return ans;
    }
};