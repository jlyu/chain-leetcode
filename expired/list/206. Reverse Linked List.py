# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/reverse-linked-list/

Reverse a singly linked list.
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

    def printList(self, node):
        while node is not None:
            print node.val,
            node = node.next
            if node is not None: print " -> ",
        print

    def showList(self, node):
        #print node
        result = []
        while node:
            result.append(node.val)
            node = node.next

        return result

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        l = [ ]
        while head:
            l.append(head.val)
            head = head.next

        node = ListNode(None)
        head = node
        for i in l[::-1]:
            node.next = ListNode(i)
            node = node.next

        node.next = None
        return head.next





def testcase(input, output):
    ins = Solution()
    head = ins.createList(input)
    before = ins.showList(head)
    after = ins.showList(ins.reverseList(head))
    print "test: %s -> %s \r\nrslt: %s -> %s" % (input, output, before, after)
    #assert (before == input)
    #assert (after == output)
    #print "...OK"
    print "-"*40



def unittest():
    testcase(input=[1, 2, 3], output=[3, 2, 1])
    testcase(input=[1], output=[1])
    testcase(input=[ ], output=[ ])
    testcase(input=[1,1,2,3,3], output=[3,3,2,1,1])
    #testcase(input=[1,1,1], output=[1])
    #testcase(input=[1,2,3], output=[1,2,3])



if __name__ == '__main__':
    unittest()

