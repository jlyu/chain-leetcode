# -*- coding: utf-8 -*-
import time
"""
https://leetcode.com/problems/flatten-nested-list-iterator/

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Given the list [1,[4,[6]]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
"""



# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        def gen(nestedList):
            for x in nestedList:
                if x.isInteger():
                    yield x.getInteger()
                else:
                    for y in gen(x.getList()):
                        yield y
        self.gen = gen(nestedList)


    def next(self):
        """
        :rtype: int
        """
        return self.value



    def hasNext(self):
        """
        :rtype: bool
        """
        try:
            self.value = next(self.gen)
            return True
        except StopIteration:
            return False




# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


def testcase(input, expected):
    ins = Solution()
    output = ins.removeDuplicateLetters(input)

    print "in: %s,  expected: %s,  out: %s" % (input, expected, output)

    #assert (before == input)
    #assert (after == output)
    print "-"*40





def unittest():


    testcase(input=[[1,1],2,[1,1]], expected=[1,1,2,1,1])
    testcase(input=[1,[4,[6]]], expected=[1,4,6])









if __name__ == '__main__':
    start = time.time()
    unittest()
    print "run time:", time.time() - start

