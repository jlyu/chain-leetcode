# -*- coding: utf-8 -*-
import time
"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
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

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        cur = None
        for i, n in enumerate(nums):
            if cur == n:
                nums[i] = None
            else:
                cur = n
        nums[:] = [x for x in nums if x is not None]
        #print nums
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

    testcase(input=[1,1,2], expected=2)

    #testcase(input=[1,1,1], expected=1)
    #testcase(input=[1,1,1,1], expected=1)
    #testcase(input=[1,1,2,2,3,3,3,4], expected=4)
    #testcase(input=[ ], expected=0)
    #testcase(input=[1], expected=1)





if __name__ == '__main__':
    start = time.time()
    unittest()
    print "run time:", time.time() - start

