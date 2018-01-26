# -*- coding: utf-8 -*-
"""-------------------------------------------------------------------------------
Given a linked list, remove the nth node from the end of list and return its head.

For example,
   Given linked list: 1->2->3->4->5, and n = 2.
   After removing the second node from the end, the linked list becomes 1->2->3->5.
-------------------------------------------------------------------------------"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def createList(self, size):
        head = ListNode(1)
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


    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        fast = head
        slow = head
        for i in range(n):
            fast = fast.next
            if fast is None:
                head = head.next
                return head

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head



if __name__ == '__main__':
    ins = Solution()
    head = ins.createList(3)
    ins.printList(head)

    head = ins.removeNthFromEnd(head, 1)
    ins.printList(head)
