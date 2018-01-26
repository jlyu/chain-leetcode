# -*- coding: utf-8 -*-
import time
"""
https://leetcode.com/problems/min-stack/

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.min = self.getMin()
        if self.min is None or x < self.min:
            self.min = x

        self.stack.append((x, self.min))



    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            self.stack.pop()


    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][0]


    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[len(self.stack)-1][1]










def testcase(x=42):
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(x)
    #obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()
    print  param_3, param_4

    """
    ins = Solution()
    output = ins.evalRPN(input)

    print "in: %s,  expected: %s,  out: %s" % (input, expected, output)

    #assert (before == input)
    #assert (after == output)
    """
    print "-"*40





def unittest():

    testcase()







if __name__ == '__main__':
    start = time.time()
    unittest()
    print "run time:", time.time() - start

