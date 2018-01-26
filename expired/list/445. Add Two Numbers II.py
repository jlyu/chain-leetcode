# -*- coding: utf-8 -*-
import time
"""
https://leetcode.com/problems/add-two-numbers-ii/

You are given two linked lists representing two non-negative numbers.
The most significant digit comes first and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
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

        x1, x2 = 0, 0
        while l1:
            x1 = x1*10+l1.val
            l1 = l1.next
        while l2:
            x2 = x2*10+l2.val
            l2 = l2.next
        x = x1 + x2

        head = ListNode(0)
        if x == 0: return head
        while x:
            v, x = x%10, x//10
            head.next, head.next.next = ListNode(v), head.next

        return head.next




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
    pass






if __name__ == '__main__':
    start = time.time()
    unittest()
    print "run time:", time.time() - start

