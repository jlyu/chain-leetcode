class Solution {
    private List<String> ans = new LinkedList<String>();
    HashMap<String, String> phoneMap = new HashMap<>() {{
        put("2", "abc");
        put("3", "def");
        put("4", "ghi");
        put("5", "jkl");
        put("6", "mno");
        put("7", "pqrs");
        put("8", "tuv");
        put("9", "wxyz");
    }};

    public List<String> letterCombinations(String digits) {
        if(digits == null || digits.length() == 0) {
            return ans;
        }
        backtracking("", digits);
        return ans;
    }

    private void backtracking(String combination, String nextDigits) {
        if (nextDigits.length() == 0) {
            ans.add(combination);
            return;
        }

        String digit = nextDigits.substring(0, 1);
        String letters = phoneMap.get(digit);
        
        for (int i = 0; i < letters.length(); i++) {      
            String letter = String.valueOf(letters.charAt(i));
            backtracking(combination + letter, nextDigits.substring(1));
        }
        
    }
}