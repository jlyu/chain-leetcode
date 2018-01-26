# -*- coding: utf-8 -*-
import time
"""
https://leetcode.com/problems/merge-sorted-array/

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
The number of elements initialized in nums1 and nums2 are m and n respectively.
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


    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        out = []
        i1, i2 = 0, 0
        while i1 < m and i2 < n:
            if nums1[i1] <= nums2[i2]:
                out.append(nums1[i1])
                i1 += 1
            else:
                out.append(nums2[i2])
                i2 += 1

        if m: out += nums1[i1:m]
        if n: out += nums2[i2:n]
        nums1[:] = out






def testcase(nums1, m, nums2, n):
    ins = Solution()
    output = ins.merge(nums1, m, nums2, n)
    if len(nums1) < 150:
        print "in: %s, in2: %s,  out: %s" % (nums1, nums2, nums1)
    #if expected == input:
    #    print "...OK"
    #else:
    #    print "...NG"
    #print "-"*40


def unittest():

    testcase([1,3,5], 3, [2,4,6], 3)
    testcase([0],0, [1], 1)
    testcase([1,2,3],2, [2,3,4], 1)
    testcase([1,2,3,4,5],0, [1,2,3,4], 1)
    testcase([1,2,3,4],3, [1], 1)






if __name__ == '__main__':
    start = time.time()
    unittest()
    print "run time:", time.time() - start

