# -*- coding: utf-8 -*-
import time
"""
https://leetcode.com/problems/missing-number/

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""

class Solution(object):

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        return l * (l + 1 ) / 2 - sum(nums)






def testcase(input, expected):
    ins = Solution()
    output = ins.missingNumber(input)
    if len(input) < 150:
        print "in: %s, expected: %s, out: %s" % (input, expected, output),
    if expected == output:
        print "...OK"#, output
    else:
        print "...NG"#, output
    print "-"*40


def unittest():

    testcase(input=[ ], expected=None)
    testcase(input=[0, 1, 3], expected=2)
    testcase(input=[0, 1, 2, 3, 5], expected=4)
    #testcase(input=[0,0,0], expected=[0])
    #testcase(input=[2,2], expected=[2])
    #testcase(input=[3,2,2,1,3,1,2,1], expected=[1,2])
    #testcase(input=[1,1], expected=1)
    #testcase(input=[1,1,1,1,1,2,3,1], expected=1)
    #testcase(input=[3,2,3], expected=3)

    #testcase(input=[1,2,3], expected=False)
    #testcase(input=i1, expected=True)




    #testcase(input=[1, 2, 3, 1], expected=2)
    #testcase([], expected=-1)
    #testcase(input=i1, expected=4)

    #testcase(input=[2,1,2,1,0,0,1], expected=2)





if __name__ == '__main__':
    start = time.time()
    unittest()
    print "run time:", time.time() - start

