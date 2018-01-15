# -*- coding: utf-8 -*-
import time
"""
https://leetcode.com/problems/plus-one/

Given a non-negative number represented as an array of digits, plus one to the number.
The digits are stored such that the most significant digit is at the head of the list.
"""

class Solution(object):

    def binarySearch(self, nums, x):
        start = 0
        final = len(nums) - 1

        while start <= final:
            mid = start + (final - start) / 2 #+ 1 if end % 2 == 0 else end / 2
            #print start, mid, final, "===", nums[mid], x

            if   nums[mid] > x: final = mid - 1
            elif nums[mid] < x: start = mid + 1
            else:               return mid, nums[mid]

    def testBS(input, target):
        ins = Solution()
        output = ins.binarySearch(input, target)
        print "in: %s, target=%s,  out: %s" % (input, target, output)


    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #print "digits=",digits

        if len(digits) == 1 and digits[0] == 9:
            digits[0] = 0
            digits.insert(0, 1)
            return digits

        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        else:
            digits[-1] = 0
            digits[:-1] = self.plusOne(digits[:-1])
            return digits





def testcase(input, expected):
    ins = Solution()
    output = ins.plusOne(input)
    if len(input) < 150:
        print "in: %s, expected: %s,  out: %s" % (input, expected, input),
    if expected == input:
        print "...OK"
    else:
        print "...NG"
    print "-"*40


def unittest():

    testcase([1,2,3], expected=[1,2,4])
    testcase([9,9,9], expected=[1,0,0,0])





if __name__ == '__main__':
    start = time.time()
    unittest()
    print "run time:", time.time() - start

