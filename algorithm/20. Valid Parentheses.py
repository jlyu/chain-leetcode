# -*- coding: utf-8 -*-
import time
"""
https://leetcode.com/problems/valid-parentheses/

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        brackets = { ')':'(', '}':'{', ']':'['}

        for char in s:
            if char in '({[':
                stack.append(char)

            if char in ']})':
                if stack == [] or stack.pop() != brackets[char]:
                    return False

        return stack == []




def testcase(input, expected):
    ins = Solution()
    output = ins.isValid(input)

    print "in: %s,  expected: %s,  out: %s" % (input, expected, output)

    #assert (before == input)
    #assert (after == output)
    print "-"*40





def unittest():
    testcase(input="()", expected=True)
    testcase(input="]", expected=False)
    testcase(input="([)]", expected=False)
    testcase(input="(()()()()()()()()", expected=False)
    testcase(input="[])", expected=False)







if __name__ == '__main__':
    start = time.time()
    unittest()
    print "run time:", time.time() - start

