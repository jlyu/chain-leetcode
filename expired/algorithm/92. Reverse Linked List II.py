# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/reverse-linked-list-ii/

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
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

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None: return head

        node = ListNode(None)
        node.next = head
        rnode = node

        l = [ ]
        counter = 1
        while head:
            print "head=", head.val, "counter=",counter

            if counter < m or counter > n:
                node.next = head
                node = node.next

            if m <= counter <= (n + m):
                l.append(head.val)

            if len(l) == (n - m + 1):
                print "in l:", l
                for i in l[::-1]:
                    node.next = ListNode(i)
                    node = node.next

            counter += 1
            head = head.next

        node.next = None
        return rnode.next





def testcase(input, m, n, output):
    ins = Solution()
    head = ins.createList(input)
    before = ins.showList(head)
    after = ins.showList(ins.reverseBetween(head, m, n))
    print "test: %s -> %s m=%s, n=%s\r\nrslt: %s -> %s" % (input, output, m, n, before, after)
    #assert (before == input)
    #assert (after == output)
    #print "...OK"
    print "-"*40



def unittest():
    testcase(input=[], m=2, n=2, output=[])
    testcase(input=[2], m=1, n=1, output=[1])
    testcase(input=[1, 2, 3, 4, 5], m=2, n=2, output=[1,4,3,2,5])

    testcase(input=[1, 2, 3, 4, 5], m=2, n=4, output=[1,4,3,2,5])




if __name__ == '__main__':
    unittest()

