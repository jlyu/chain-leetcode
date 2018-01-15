# -*- coding: utf-8 -*-
import time
"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5
max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)

Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0
In this case, no transaction is done, i.e. max profit = 0.
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


    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #buy, profit = None, None
        #for i, n in enumerate(prices):
        #    if buy is None: buy = n; continue
        #    buy = min(buy, n)
        #    profit = max(profit, n-buy)
        #return profit or 0

        buy, profit = None, None
        for i, n in enumerate(prices):
            if buy is None or buy > n: buy = n

            if buy is not None and n > buy:
                if n - buy > profit:
                    profit = n - buy

            #print "buy=%s, profit=%s" % (buy, profit)

        return profit or 0







def testcase(input, expected):
    ins = Solution()
    output = ins.maxProfit(input)
    if len(input) < 150:
        print "in: %s, expected: %s, out: %s" % (input, expected, output),
    if expected == output:
        print "...OK"
    else:
        print "...NG"
    print "-"*40


def unittest():

    testcase(input=[7, 1, 5, 3, 6, 4], expected=5)
    testcase(input=[7, 6, 4, 3, 1], expected=0)
    testcase(input=[2,1,2,1,0,1,2], expected=2)






if __name__ == '__main__':
    start = time.time()
    unittest()
    print "run time:", time.time() - start

