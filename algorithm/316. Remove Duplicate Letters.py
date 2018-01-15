# -*- coding: utf-8 -*-
import time
"""
https://leetcode.com/problems/remove-duplicate-letters/

Given a string which contains only lowercase letters,
remove duplicate letters so that every letter appear once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"
"""

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        rindex = {c: i for i, c in enumerate(s)}
        #print rindex
        result = ''
        for i, c in enumerate(s):
            if c not in result:
                while c < result[-1:] and i < rindex[result[-1]]:
                    print c, result[-1:], "and", i, rindex[result[-1]],
                    result = result[:-1]
                    print "====", result
                result += c
                print "result=", result
        return result








def testcase(input, expected):
    ins = Solution()
    output = ins.removeDuplicateLetters(input)

    print "in: %s,  expected: %s,  out: %s" % (input, expected, output)

    #assert (before == input)
    #assert (after == output)
    print "-"*40





def unittest():


    testcase(input="bcabc", expected="abc")
    testcase(input="cbacdcbc", expected="acdb")









if __name__ == '__main__':
    start = time.time()
    unittest()
    print "run time:", time.time() - start

