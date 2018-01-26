# -*- coding: utf-8 -*-
"""

Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
https://leetcode.com/problems/merge-two-sorted-lists/

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

    def printList(self, node):
        while node is not None:
            print node.val,
            node = node.next
            if node is not None: print " -> ",
        print

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (l1 is None) and (l2 is None): return None
        if l1 is None: return l2
        if l2 is None: return l1

        orig = head = ListNode(0)
        while (l1 is not None) and (l2 is not None):

            if l1.val <= l2.val:
                head.next = l1
                head = l1
                l1 = l1.next

            else:
                head.next = l2
                head = l2
                l2 = l2.next

        if l1 is None: head.next = l2
        if l2 is None: head.next = l1
        return orig.next




def unittest():
    #[1], [2] => [1,2]
    ins = Solution()
    l1 = ins.createList(start=1, size=1)
    l2 = ins.createList(start=2, size=1)
    ins.printList(l1)
    ins.printList(l2)
    mergedhead = ins.mergeTwoLists(l1, l2)
    ins.printList(mergedhead)



if __name__ == '__main__':
    unittest()

