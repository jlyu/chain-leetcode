class Solution {
public:
    int countTriplets(vector<int>& arr) {
        int n = arr.size(),res = 0;
        for(int i = 0;i < n;i++){
            int sum = 0;
            for(int k = i;k < n;k++){
                sum ^= arr[k];
                if(sum == 0 && k > i) res += (k-i);
            }
        }
        return res;
    }
};