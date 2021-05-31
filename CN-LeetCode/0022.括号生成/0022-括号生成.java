class Solution {
    private List<String> ans = new ArrayList<String>();

    public List<String> generateParenthesis(int n) {
        StringBuffer sb = new StringBuffer();
        backtracking(n, 0, 0, sb);
        return ans;
    }

    private void backtracking(int n, int L, int R, StringBuffer S) {
        if (L == R && S.length() == n * 2) {
            ans.add(S.toString());
            return;
        }

        if (L < n) {
            S.append('(');
            backtracking(n, L + 1, R, S);
            S.deleteCharAt(S.length() - 1);
        }
        if (R < L) {
            S.append(')');
            backtracking(n, L, R + 1, S);
            S.deleteCharAt(S.length() - 1);
        }
    }
}