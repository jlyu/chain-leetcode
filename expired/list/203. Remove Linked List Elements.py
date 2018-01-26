# -*- coding: utf-8 -*-
import time
"""
https://leetcode.com/problems/remove-linked-list-elements/

Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution(object):
    def createList(self, start, size):
        head = ListNode(start)
        node = head
        for i in range(1, size):
            newNode = ListNode(head.val + i)
            node.next = newNode
            node = newNode
        return head

    def createList(self, l):
        head = ListNode(0)
        node = head
        for x in l:
            newNode = ListNode(x)
            node.next = newNode
            node = newNode
        return head.next

    def showList(self, node):
        #print node
        result = []
        while node:
            result.append(node.val)
            node = node.next

        return result

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        dummy = ListNode(None)
        dummy.next = head
        cur = dummy
        while cur:
            nxt = cur.next
            while nxt and nxt.val == val:
                nxt = nxt.next

            cur.next = nxt
            cur = cur.next

        return dummy.next






def testcase(input, val, output):
    ins = Solution()
    head = ins.createList(input)
    
    before = ins.showList(head)
    after = ins.showList(ins.removeElements(head, val))
    print "in: %s                %s" % (input, before)
    print "out:%s                %s" % (output, after)

    #rslt: %s -> %s" % (inputA,, output, before, after)
    #assert (before == input)
    #assert (after == output)
    #print "...OK"
    print "-"*40





def unittest():
    
    testcase(input=[1,2,6,3,4,5,6], val=6, output=[1,2,3,4,5])
    testcase(input=[ ], val=1, output=[ ])
    testcase(input=[1], val=1, output=[ ])
    testcase(input=[1,1], val=1, output=[ ])
    testcase(input=[2], val=1, output=[2])
    testcase(input=[2,3], val=1, output=[2,3])
    testcase(input=[1,1,1,1], val=1, output=[ ])
    testcase(input=[1,2,3,4,5], val=1, output=[2,3,4,5])
    testcase(input=[1,2,1,3,1,4], val=1, output=[2,3,4])
    testcase(input=[2,3,1], val=1, output=[2,3])
    



if __name__ == '__main__':
    start = time.time()
    unittest()
    print "run time:", time.time() - start

