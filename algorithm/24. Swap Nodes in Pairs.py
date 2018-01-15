# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/swap-nodes-in-pairs/

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


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
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result




    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None: return None
        if head.next is None: return head

        first = head
        node = first

        orig = ListNode(0)
        orig.next = first.next

        while first is not None:

            second = first.next

            if second is None:
                first.next = second
                return orig.next

            else:
                #print "[exchage]:",
                third = second.next
                #if third: print "first %s -> second %s -> third %s" % (first.val, second.val, third.val)


                #if third: print "third = second.next: %s => %s" % (third.val, second.next.val)

                node.next = second
                #print "head=%s, node=%s" % (head.val, node.val),
                #print "node.next = second: %s => %s" % (node.next.val, second.val)

                second.next = first
                #print "second.next = first: %s => %s" % (second.next.val, first.val)

                first.next = third
                #if third: print "first.next = third: %s => %s" % (second.next.val, third.val)

                node = first
                #print "node = first: %s => %s" % (node.val, first.val)

            first = first.next
            #if first: print "now firt=", first.val

        #print "return head=%s, orig.next=%s" % (head.val, orig.next.val)
        return orig.next


def testCreateList():
    ins = Solution()
    head = ins.createList([1,2,3,4])
    print ins.showList(head)

def testcase(input, output):
    # In: 1->2->3->4
    # Out: 2->1->4->3
    ins = Solution()
    head = ins.createList(input)
    before = ins.showList(head)
    after = ins.showList(ins.swapPairs(head))
    print "test: %s -> %s, result: %s -> %s" % (input, output, before, after),
    assert (before == input)
    assert (after == output)
    print "...OK"



def unittest():
    testcase(input=[], output=[])
    testcase(input=[1], output=[1])
    testcase(input=[1,2], output=[2,1])
    testcase(input=[1,2,3,4], output=[2,1,4,3])
    testcase(input=[1,2,3,4,5], output=[2,1,4,3,5])



if __name__ == '__main__':
    unittest()

