# -*- coding: utf-8 -*-
import time
"""
https://leetcode.com/problems/add-two-numbers/

You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
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

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #if l1 is None: return l2
        #if l2 is None: return l1

        head = ListNode(None)
        node = head
        last = 0

        while l1 or l2:
            l1v, l2v = 0, 0
            if l1:
                l1v = l1.val
                l1 = l1.next

            if l2:
                l2v = l2.val
                l2 = l2.next

            val = (l1v + l2v + last) % 10
            last = (l1v + l2v + last) / 10
            #print l1v, l2v, val, last
            head.next = ListNode(val)
            head = head.next

        if last != 0:
            head.next = ListNode(last)
            head = head.next
            head.next = None

        return node.next




def testcase(input1, input2, output):
    ins = Solution()

    l1 = ins.createList(input1)
    l2 = ins.createList(input2)

    before1 = ins.showList(l1)
    before2 = ins.showList(l2)

    after = ins.showList(ins.addTwoNumbers(l1,l2))
    print "in: %s + %s          out: %s" % (input1, input2, output)
    print "  : %s + %s             : %s" % (before1,before2, after)
    #assert (before == input)
    #assert (after == output)
    #print "...OK"
    print "-"*40





def unittest():
    testcase(input1=[2,4,3], input2=[5,6,4], output=[7,0,8])
    testcase(input1=[0,0,3], input2=[0,0,0,0], output=[0,0,3,0])
    testcase(input1=[ ], input2=[ ], output=[ ])
    testcase(input1=[ ], input2=[1], output=[1])
    testcase(input1=[0], input2=[ ], output=[0])
    testcase(input1=[5], input2=[5], output=[0,1])
    testcase(input1=[9,9,9], input2=[9], output=[8,0,1])






if __name__ == '__main__':
    start = time.time()
    unittest()
    print "run time:", time.time() - start

