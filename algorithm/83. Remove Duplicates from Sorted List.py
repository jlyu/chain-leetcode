# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
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

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return head

        n = head.val
        node = head
        fast = head

        while (fast.next is not None):

            if fast.val == n:
                fast = fast.next
                print "fast = ",fast.val


            else:
                node.next = fast
                node = node.next
                print "node.next = fast =", fast.val

                n = fast.val
                print "n =", n
                fast = fast.next

            if fast.next is None:
                if fast.val == n: 
                    node.next = None
                else:
                    node.next = fast

        return head







def testcase(input, output):
    ins = Solution()
    head = ins.createList(input)
    before = ins.showList(head)
    after = ins.showList(ins.deleteDuplicates(head))
    print "test: %s -> %s \r\nrslt: %s -> %s" % (input, output, before, after)
    #assert (before == input)
    #assert (after == output)
    #print "...OK"
    print "-"*40



def unittest():
    testcase(input=[], output=[])
    testcase(input=[1], output=[1])
    testcase(input=[1,1], output=[1])
    testcase(input=[1,1,2], output=[1,2])
    testcase(input=[1,1,2,3,3], output=[1,2,3])
    testcase(input=[1,2,2,3,3], output=[1,2,3])
    testcase(input=[1,1,1], output=[1])
    testcase(input=[1,2,3], output=[1,2,3])



if __name__ == '__main__':
    unittest()

