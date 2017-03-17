# -*- coding: utf-8 -*-
import time
"""
https://leetcode.com/problems/3sum/

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution(object):

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

    def twoSumGai(self, nums, target):
        out = []
        d = { }
        for i, n in enumerate(nums):
            if target-n in d:
                out.append( (min(n, target-n), max(n, target-n)) )
            d[n] = 1
        return out

    def binarySearch(self, nums, x):
        start = 0
        final = len(nums) - 1

        while start <= final:
            mid = start + (final - start) / 2 #+ 1 if end % 2 == 0 else end / 2
            #print start, mid, final, "===", nums[mid], x

            if   nums[mid] > x: final = mid - 1
            elif nums[mid] < x: start = mid + 1
            else:               return mid, nums[mid]



    def threeSum_v1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out = [ ]
        d = { }
        l = len(nums)
        #if len(nums) < 3: return out
        #if len(nums) == 3: return out if sum(nums) != 0 else [nums]

        #nums.sort()  #
        nums = sorted(nums)
        for i in xrange(l):
            for j in xrange( i+1, l ):

                bs = self.binarySearch(nums[j+1:], -nums[i]-nums[j])

                #print "n[i=%s]=%s, n[j=%s]=%s, to find [%s] in %s => bs=%s" % (i, nums[i], j, nums[j], -nums[i]-nums[j], nums[j+1:], bs), d, l
                #print (bs > j or bs == j == 1) and ((bs != l-1) or (j != l-1))

                if bs is not None:

                    if (nums[i], nums[j]) not in d:
                        out.append( [nums[i], nums[j], bs[1]] )

                    d[(nums[i], nums[j])] = bs[1]

        return out




    def threeSum(self, nums):
        out = [ ]
        d = { }

        for i, n in enumerate(nums):
            twos = self.twoSumGai(nums[i+1:], 0-n)

            for t in twos:
                mx = max(n, t[0], t[1])
                mn = min(n, t[0], t[1])
                md = n + t[0] + t[1] - mx - mn

                if (mn, md, mx) not in d:
                    out.append( [mn, md, mx] )
                d[ (mn, md, mx) ] = 1
        return out


def testBS(input, target):
    ins = Solution()
    output = ins.binarySearch(input, target)
    print "in: %s, target=%s,  out: %s" % (input, target, output)



def testcase(input, expected):
    ins = Solution()
    output = ins.threeSum(input)
    if len(input) < 150:
        print "in: %s, expected: %s,  out: %s" % (input, expected, output),
    if expected == output:
        print "...OK"
    else:
        print "...NG"
    print "-"*40


def unittest():
    #testBS(input=[-4, -1, -1, 0, 1,2], target=-4)
    #testBS(input=[-4, -1, -1, 0, 1,2], target=-1)
    #testBS(input=[-4, -1, -1, 0, 1,2], target=0)
    #testBS(input=[-4, -1, -1, 0, 1,2], target=1)
    #testBS(input=[-4, -1, -1, 0, 1,2], target=2)
    #testBS(input=[-4, -1, -1, 0, 1,2], target=-7)
    #testBS(input=[-4, -1, -1, 0, 1,2], target=8)

    i1 = [0,14,-7,2,7,11,-9,11,-12,6,-10,-8,9,-3,7,-6,3,4,14,-10,-8,5,-1,6,12,9,12,-11,-15,-5,5,0,-6,13,9,9,10,7,5,13,-2,11,-10,-15,-15,4,-14,-4,-15,7,-7,-15,-3,8,-2,-13,-6,-5,-9,-14,5,12,1,6,2,-12,-8,-11,10,13,-13,-14,1,14,8,1,-4,9,4,-12,-6,13,10,6,6,-7,8,7,3,7,8,-15,-4,-14,-1,13,-11,6,-12,-15,4,12,8,-10,4,1,-1,7,-13,-12,10,-4,8,6,10,-1,6,-5,13,-13,9,6,-13,-10]

    testcase(input=[0, 0, 0], expected=[[0,0,0]])
    testcase(input=[0, 0, 0, 0], expected=[[0,0,0]])
    testcase(input=[-1,0,1,2,-1,-4], expected=[[-1,-1,2],[-1,0,1]])
    testcase(input=[-2,0,1,1,2], expected=[[-2,0,2],[-2,1,1]])
    testcase(input=[1,2,-2,-1], expected=[])

    testcase(input=i1, expected=[])



if __name__ == '__main__':
    start = time.time()
    unittest()
    print "run time:", time.time() - start

