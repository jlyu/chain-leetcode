# -*- coding: utf-8 -*-
import time
"""
https://leetcode.com/problems/decode-string/

Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k.
For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        k = ''
        for char in s:
            if char.isdigit():
                k += char
                continue

            if char == '[':
                stack.append(k)
                k = ''

            elif char == ']':
                sub = ''
                while True:
                    x = stack.pop()
                    if x.isdigit():
                        sub = int(x) * sub
                        stack.append(sub)
                        break
                    sub = x + sub
            else:
                stack.append(char)

        result = ''
        while stack:
            result = stack.pop() + result
        return result



def testcase(input, expected):
    ins = Solution()
    output = ins.decodeString(input)

    print "in: %s,  expected: %s,  out: %s" % (input, expected, output)

    #assert (before == input)
    #assert (after == output)
    print "-"*40





def unittest():
    testcase(input="3[a]2[bc]", expected="aaabcbc")
    testcase(input="3[a2[c]]", expected="accaccacc")
    testcase(input="2[abc]3[cd]ef", expected="abcabccdcdcdef")
    testcase(input="13[a]", expected="aaaaaaaaaaaaa")
    testcase(input="1[2[3[4[5[s]e]r]x]a]df", expected=" ")








if __name__ == '__main__':
    start = time.time()
    unittest()
    print "run time:", time.time() - start

