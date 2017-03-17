# -*- coding: utf-8 -*-
import time
"""
https://leetcode.com/problems/delete-node-in-a-linked-list/

Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, 
the linked list should become 1 -> 2 -> 4 after calling your function.
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

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        node.val = node.next.val
        node.next = node.next.next








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
    
    testcase(input=[1,2,6,3,4,5,6], output=[1,2,3,4,5])

    



if __name__ == '__main__':
    start = time.time()
    unittest()
    print "run time:", time.time() - start

