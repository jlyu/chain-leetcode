# -*- coding: utf-8 -*-
import time
"""
https://leetcode.com/problems/remove-element/

Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.
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


    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i, n in enumerate(nums):
            if n == val:
                nums[i] = None
        nums[:] = [x for x in nums if x is not None]
        return len(nums)


def testcase(input, expected):
    ins = Solution()
    output = ins.removeDuplicates(input)
    if len(input) < 150:
        print "in: %s, expected: %s,  out: %s" % (input, expected, output),
    if expected == output:
        print "...OK"
    else:
        print "...NG"
    print "-"*40


def unittest():

    pass





if __name__ == '__main__':
    start = time.time()
    unittest()
    print "run time:", time.time() - start

