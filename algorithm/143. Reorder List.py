# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/reorder-list/

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
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

    def xmerge(self, a, b):
        alen, blen = len(a), len(b)
        mlen = min(alen, blen)
        for i in xrange(mlen):
            yield a[i]
            yield b[i]

        if alen > blen:
            for i in xrange(mlen, alen):
                yield a[i]
        else:
            for i in xrange(mlen, blen):
                yield b[i]

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if (head is not None) and (head.next is not None):
            l = [ ]
            node = head
            while node:
                l.append(node.val)
                node = node.next

            pos = l[:len(l)/2:1]
            neg = l[:len(l)/2-1:-1]

            node = head
            first = True
            for v in self.xmerge(pos, neg):
                if first:
                    first = False
                    continue  #dirty

                head.next = ListNode(v)
                head = head.next

            head = node.next














def testcase(input, output):
    ins = Solution()
    head = ins.createList(input)
    before = ins.showList(head)
    ins.showList(ins.reorderList(head))
    print "test: %s -> %s \r\nrslt: %s -> %s" % (input, output, before, head)
    #assert (before == input)
    #assert (after == output)
    #print "...OK"
    print "-"*40



def unittest():
    testcase(input=[1], output=[1])
    testcase(input=[1,2,3,4,5], output=[1,5,2,4,3])
    testcase(input=[1,2,3], output=[1,3,2])




if __name__ == '__main__':
    unittest()

