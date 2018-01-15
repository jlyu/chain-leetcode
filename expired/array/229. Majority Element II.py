# -*- coding: utf-8 -*-
import time
"""
https://leetcode.com/problems/majority-element-ii/

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
The algorithm should run in linear time and in O(1) space.
"""

class Solution(object):

    def _majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        if len(nums) == 1:
            print "fin:",nums[0]
            return nums[0]
        a = self.majorityElement(nums[:len(nums)//2])
        b = self.majorityElement(nums[len(nums)//2:])
        if a == b:
            print "a==b", a
            return a
        print "a=%s, b=%s" % (a, b)
        return [b, a][nums.count(a) > len(nums)//2]

        ##Sorting
        #return sorted(nums)[len(nums)//2]

        """
        d = { }
        l = len(nums)
        if l == 1: return nums[0]
        for i, n in enumerate(nums):
            if n in d:
                if d[n] > l // 2:
                    return n
                else:
                    d[n] = d[n] + 1
            else:
                d[n] = 1


        print d.items()
        r = sorted(d.items(), key=lambda d:-d[1])
        #print r, d.items()
        if r:
            if r[0][1] > l // 2:
                return r[0][0]
            #print d
        """


    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #if not nums: return []
        counter1, counter2, candidate1, candidate2 = 0, 0, 0, 1
        for i, n in enumerate(nums):
            if   n == candidate1: counter1 += 1
            elif n == candidate2: counter2 += 1
            elif counter1 == 0:   candidate1, counter1 = n, 1
            elif counter2 == 0:   candidate2, counter2 = n, 1
            else: counter1, counter2 = counter1-1, counter2-1
            print "candidate1=%s, candidate2=%s, counter1=%s, counter2=%s" % (candidate1, candidate2, counter1, counter2)

        print "final (%s, %s)" % (candidate1, candidate2)
        return [n for n in (candidate1, candidate2) if nums.count(n) > len(nums) // 3]


        """
        out = []
        d = { }
        l = len(nums)
        if l < 3: return list(set(nums))

        for i, n in enumerate(nums):
            if n in d:
                #if d[n] > l // 2:
                #    return n

                d[n] = d[n] + 1
            else:
                d[n] = 1


        #print d.items()
        r = sorted(d.items(), key=lambda d:-d[1])
        print "r=",r

        for x in r:
            if x[1] > l // 3:
                out.append(x[0])

            #print d
        return list(set(out))
        """



def testcase(input, expected):
    ins = Solution()
    output = ins.majorityElement(input)
    if len(input) < 150:
        print "in: %s, expected: %s, out: %s" % (input, expected, output),
    if expected == output:
        print "...OK"#, output
    else:
        print "...NG"#, output
    print "-"*40


def unittest():

    testcase(input=[ ], expected=[ ])
    testcase(input=[0,0,0], expected=[0])
    testcase(input=[2,2], expected=[2])
    testcase(input=[3,2,2,1,3,1,2,1], expected=[1,2])
    #testcase(input=[1,1], expected=1)
    #testcase(input=[1,1,1,1,1,2,3,1], expected=1)
    #testcase(input=[3,2,3], expected=3)

    #testcase(input=[1,2,3], expected=False)
    #testcase(input=i1, expected=True)




    #testcase(input=[1, 2, 3, 1], expected=2)
    #testcase([], expected=-1)
    #testcase(input=i1, expected=4)

    #testcase(input=[2,1,2,1,0,0,1], expected=2)





if __name__ == '__main__':
    start = time.time()
    unittest()
    print "run time:", time.time() - start

