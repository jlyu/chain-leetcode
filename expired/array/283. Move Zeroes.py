# -*- coding: utf-8 -*-
import time
"""
https://leetcode.com/problems/move-zeroes/

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function,
nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

class Solution(object):

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        p0, p1= 0, 0  #p0:point Zero,  p1:point Non-Zero
        while True:
            try:
                while nums[p1] == 0: p1 += 1
                while nums[p0] != 0: p0 += 1

                if p0 < p1:
                    nums[p0], nums[p1] = nums[p1], nums[p0]
                else:
                    p1 = p0

            except:
                break

        """
        #l = len(nums)
        while i < l:
            while pNonzero < l and nums[pNonzero] == 0:
                pNonzero += 1

            while pZero < l and nums[pZero] != 0:
                pZero += 1

            print pZero, pNonzero, nums

            if pZero < pNonzero and pZero < l and pNonzero < l:
                nums[pZero], nums[pNonzero] = nums[pNonzero], nums[pZero]
            else:
                pNonzero = pZero

            i = max(pNonzero, i+1)
        """











def testcase(input, expected):
    ins = Solution()
    print "orig:", input

    output = ins.moveZeroes(input)
    if len(input) < 150:
        print "in: %s, expected: %s, out: %s" % (input, expected, output),
    if expected == output:
        print "...OK"#, output
    else:
        print "...NG"#, output
    print "-"*40


def unittest():

    testcase(input=[ ], expected=[ ])
    testcase(input=[0, 1, 0, 3, 12], expected=[1, 3, 12, 0, 0])
    testcase(input=[0, 0, 0, 0, 0], expected=[0, 0, 0, 0, 0])
    testcase(input=[0, 0, 0, 0, 1], expected=[1, 0, 0, 0, 0])
    testcase(input=[1,0], expected=[1,0])
    testcase(input=[1,0,1], expected=[1,1,0])









if __name__ == '__main__':
    start = time.time()
    unittest()
    print "run time:", time.time() - start

