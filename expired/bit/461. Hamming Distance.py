# -*- coding: utf-8 -*-
import time
"""
https://leetcode.com/problems/hamming-distance/#/description

The Hamming distance (https://en.wikipedia.org/wiki/Hamming_distance) 
  between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note: 0 ≤ x, y < 2^31.

Example:

Input: x = 1, y = 4
Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""

class Solution(object):

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        if (x < 0 or x >= 2**31) or (y < 0 or y >= 2**31): return 

        return bin(x ^ y).count('1')








def testcase(x, y, expected):
    ins = Solution()
    output = ins.hammingDistance(x, y)
    #if len(x) < 150:
    print "in: %s, target=%s, expected: %s,  out: %s" % (x, y,  expected, output),
    if expected == output:
        print "...OK"
    else:
        print "...NG"
    print "-"*40


def unittest():

    testcase(x=1, y=4,  expected=2)
    testcase(x=93, y=73,  expected=2)




if __name__ == '__main__':
    start = time.time()
    unittest()
    print "run time:", time.time() - start

