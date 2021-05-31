class Solution {
    private List<String> ans = new ArrayList<String>();

    public List<String> letterCasePermutation(String s) {
        char[] charArray = s.toCharArray();
        backtracking(charArray, 0);
        return ans;
    }

    private void backtracking(char[] charArray, int start) {
        if (start == charArray.length) {
            ans.add(new String(charArray));
            return;
        }

        backtracking(charArray, start + 1);

        if (Character.isLetter(charArray[start])) {
            charArray[start] ^= 1 << 5;
            backtracking(charArray, start + 1);
        }
    }
}