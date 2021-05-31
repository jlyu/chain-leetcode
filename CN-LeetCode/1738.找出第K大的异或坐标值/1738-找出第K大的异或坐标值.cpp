class Solution {
public:
    int kthLargestValue(vector<vector<int>>& matrix, int k) {
        vector<int> ret;
        int m = matrix.size();
        int n = matrix[0].size();
        int dp[m+1][n+1];
        memset(dp,0,sizeof(dp));
        dp[1][1] = matrix[0][0];
        ret.push_back(dp[1][1]);
        if(m==0||n==0) return 0;
        for(int i=2;i<=n;++i){
            dp[1][i] = matrix[0][i-1]^dp[1][i-1];
            ret.push_back(dp[1][i]);
        }
        for(int i=2;i<=m;++i){
            dp[i][1] = matrix[i-1][0]^dp[i-1][1];
            ret.push_back(dp[i][1]);
        }
        for(int i=2;i<=m;++i){
            for(int j=2;j<=n;++j){
                dp[i][j] = dp[i-1][j]^dp[i][j-1]^dp[i-1][j-1]^matrix[i-1][j-1];
                ret.push_back(dp[i][j]);
            }
        }
        sort(ret.begin(),ret.end(),[](auto&a,auto&b){return a>b;});
        return ret[k-1];
    }
};