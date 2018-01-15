# -*- coding: utf-8 -*-
import time
"""
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

UPDATE (2016/2/13):
The return format had been changed to zero-based indices. Please read the above updated description carefully.
"""

class Solution(object):
    def binarySearch(self, nums, x):
        start = 0
        final = len(nums) - 1

        while start < final:
            mid = start + final / 2 #+ 1 if end % 2 == 0 else end / 2
            print start, mid, final

            if   nums[mid] > x: final = mid - 1
            elif nums[mid] < x: start = mid + 1
            else:               return mid



    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = { }
        for i, n in enumerate(nums):
            if target-n in d:
                return [min(i, d[target-n]), max(i, d[target-n])]
            d[n] = i

                #for i in xrange(len(nums)):
        #    if target-nums[i] in d:
        #        return [min(i, d[target-nums[i]]), max(i, d[target-nums[i]])]
        #    d[nums[i]] = i




def testBS(input, target):
    ins = Solution()
    output = ins.binarySearch(input, target)
    print "in: %s, target=%s,  out: %s" % (input, target, output)


def testcase(input, target, expected):
    ins = Solution()
    output = ins.twoSum(input, target)
    if len(input) < 150:
        print "in: %s, target=%s, expected: %s,  out: %s" % (input, target,  expected, output),
    if expected == output:
        print "...OK"
    else:
        print "...NG"
    print "-"*40


def unittest():

    #testBS(input=[2, 7, 11, 15], target=7)
    #testBS(input=[2, 7, 11, 15], target=16)

    testcase(input=[2, 7, 11, 15], target=9, expected=[0, 1])
    testcase(input=[2, 7, 11, 15], target=28, expected=None)



if __name__ == '__main__':
    start = time.time()
    unittest()
    print "run time:", time.time() - start

