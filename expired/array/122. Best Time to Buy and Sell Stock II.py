# -*- coding: utf-8 -*-
import time
"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit.
You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times).
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
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


    def _maxProfit(self, prices):
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

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #return sum([p2-p1 for p1, p2 in zip(prices, prices[1:]) if p2-p1 > 0])

        diffs = (prices[i]-prices[i-1] for i in range(1, len(prices)))
        return sum(d for d in diffs if d > 0)
        """
        i, buy, sell, profit = 0,None,0,0
        while i < len(prices):

            if buy is None or prices[i] < buy:

                while i < len(prices) - 1:
                    buy = prices[i]

                    if i+1 < len(prices) and prices[i+1] > prices[i]:
                        break

                    i+=1

                sell = 0

            #print buy, i

            if buy is not None and prices[i] >= sell:
                while i < len(prices):
                    sell = prices[i]

                    if i+1 < len(prices) and prices[i+1] < prices[i]:
                        break

                    i += 1

                if sell > buy:
                    profit += sell - buy
                    #print "profit", sell, buy
                buy = None
                i += 1


            #print "i=%s, buy=%s, sell=%s, profit=%s" % (i, buy, sell, profit)
            if i == len(prices) -1: break

        return profit
        """








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

    #testcase(input=[7, 1, 5, 3, 6, 4], expected=7)
    #testcase(input=[7, 6, 4, 3, 1], expected=0)
    #testcase(input=[2,1,2,1,0,1,2], expected=3)
    #testcase(input=[1,2,4], expected=3)
    #testcase(input=[4,3,5,6,1,9,2,2,4,7], expected=16)

    testcase(input=[1,2,4,2,5,7,2,4,9,0], expected=15)


if __name__ == '__main__':
    start = time.time()
    unittest()
    print "run time:", time.time() - start

