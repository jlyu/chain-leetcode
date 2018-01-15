# -*- coding: utf-8 -*-
import time
"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/#/description

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. 
Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""

class Solution(object):
    def binarySearch(self, nums, x):
        start = 0
        final = len(nums) - 1

        while start <= final:
            mid = (final - start) / 2 + start #   start + final / 2 #+ 1 if end % 2 == 0 else end / 2
            #print start, mid, final

            if   nums[mid] == x: return mid
            elif nums[mid] < x: start = mid + 1
            else:               final = mid - 1


    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        ## V1 = dict
        #d = { }
        #for i, n in enumerate(numbers):
        #    if target-n in d:
        #        return [min(i, d[target-n]) + 1, max(i, d[target-n]) + 1]
        #    d[n] = i

        ## V2 = binarySearch
        #n = len(numbers)
        #for i in xrange(n):
        #    low, high = i+1, n-1
        #    x = target - numbers[i]
        #    while low <= high:
        #        mid = (high - low) // 2 + low
        #        if numbers[mid] == x: return [i+1, mid+1]
        #        elif numbers[mid] < x: low = mid + 1
        #        else: high = mid - 1

        ## V3 = dict
        d = { }
        for i, n in enumerate(numbers, 1):
            try:
                return [d[n], i]
            except KeyError:
                d[target - n] = i




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

    testcase(input=[2, 7, 11, 15], target=9, expected=[1, 2])
    testcase(input=[2, 7, 11, 15], target=18, expected=[2,3])
    testcase(input=[2, 7, 11, 15], target=28, expected=None)



if __name__ == '__main__':
    start = time.time()
    unittest()
    print "run time:", time.time() - start

